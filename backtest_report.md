# Market Tracker Backtest Report

_Generated: 2026-08-03T03:58:11+00:00_

## Data Sources

- Crypto: Kraken -> Coinbase -> CoinGecko OHLC -> CoinPaprika fallback chain.
- Stocks / ETFs / indices: Stooq -> Yahoo Finance fallback chain.
- Data rows are generated from real market APIs. Mock OHLCV rows are not generated.

## Data Freshness

- Rows: **92,565**
- Symbols: **161**
- Date range: **2024-03-08** to **2026-08-03**

## Latest Signals

| symbol     | date                |         close |   composite_score | signal   | data_source   |
|:-----------|:--------------------|--------------:|------------------:|:---------|:--------------|
| ADBE       | 2026-07-31 00:00:00 |   250.41      |          31.0833  | LONG     | Yahoo Finance |
| AMGN       | 2026-07-31 00:00:00 |   385.16      |          65.0833  | LONG     | Yahoo Finance |
| AMZN       | 2026-07-31 00:00:00 |   271.58      |          57.4167  | LONG     | Yahoo Finance |
| BLK        | 2026-07-31 00:00:00 |  1090.39      |          59.6667  | LONG     | Yahoo Finance |
| COP        | 2026-07-31 00:00:00 |   120.48      |          77.4167  | LONG     | Yahoo Finance |
| CVX        | 2026-07-31 00:00:00 |   196.83      |          74.0833  | LONG     | Yahoo Finance |
| DBC        | 2026-07-31 00:00:00 |    29.45      |          77.75    | LONG     | Yahoo Finance |
| EOG        | 2026-07-31 00:00:00 |   148.69      |          77.4167  | LONG     | Yahoo Finance |
| FXI        | 2026-07-31 00:00:00 |    36.5       |          65.8333  | LONG     | Yahoo Finance |
| GE         | 2026-07-31 00:00:00 |   360.07      |          34.25    | LONG     | Yahoo Finance |
| HON        | 2026-07-31 00:00:00 |   243.05      |          70.75    | LONG     | Yahoo Finance |
| INTU       | 2026-07-31 00:00:00 |   316.07      |          31.0833  | LONG     | Yahoo Finance |
| MPC        | 2026-07-31 00:00:00 |   316.47      |          54.0833  | LONG     | Yahoo Finance |
| MSFT       | 2026-07-31 00:00:00 |   464.72      |          56.75    | LONG     | Yahoo Finance |
| OXY        | 2026-07-31 00:00:00 |    57.07      |          74.0833  | LONG     | Yahoo Finance |
| PM         | 2026-07-31 00:00:00 |   190.82      |          71.5833  | LONG     | Yahoo Finance |
| RTX        | 2026-07-31 00:00:00 |   215.22      |          60.0833  | LONG     | Yahoo Finance |
| SCHW       | 2026-07-31 00:00:00 |   105.24      |          36.5833  | LONG     | Yahoo Finance |
| SHIB-USD   | 2026-08-03 00:00:00 |     4.868e-06 |          46.6667  | LONG     | Kraken API    |
| T          | 2026-07-31 00:00:00 |    23.25      |          34.4167  | LONG     | Yahoo Finance |
| TGT        | 2026-07-31 00:00:00 |   144.49      |          78.5833  | LONG     | Yahoo Finance |
| TMO        | 2026-07-31 00:00:00 |   574.3       |          60.0833  | LONG     | Yahoo Finance |
| UNI-USD    | 2026-08-03 00:00:00 |     4.101     |          65.8333  | LONG     | Kraken API    |
| USO        | 2026-07-31 00:00:00 |   129.17      |          69.25    | LONG     | Yahoo Finance |
| VNQ        | 2026-07-31 00:00:00 |    98.95      |          50.0833  | LONG     | Yahoo Finance |
| VZ         | 2026-07-31 00:00:00 |    46.81      |          72.4167  | LONG     | Yahoo Finance |
| XLE        | 2026-07-31 00:00:00 |    59.55      |          79.4167  | LONG     | Yahoo Finance |
| XLF        | 2026-07-31 00:00:00 |    56.94      |          41.75    | LONG     | Yahoo Finance |
| XOM        | 2026-07-31 00:00:00 |   155.44      |          71.5833  | LONG     | Yahoo Finance |
| AAPL       | 2026-07-31 00:00:00 |   308.91      |          -3.83333 | NEUTRAL  | Yahoo Finance |
| AAVE-USD   | 2026-08-03 00:00:00 |    91.1       |          -6.41667 | NEUTRAL  | Kraken API    |
| ABBV       | 2026-07-31 00:00:00 |   250.94      |          13.75    | NEUTRAL  | Yahoo Finance |
| ADA-USD    | 2026-08-03 00:00:00 |     0.18543   |          41.4167  | NEUTRAL  | Kraken API    |
| ALGO-USD   | 2026-08-03 00:00:00 |     0.08508   |          18.4167  | NEUTRAL  | Kraken API    |
| AMAT       | 2026-07-31 00:00:00 |   507.67      |         -29.0833  | NEUTRAL  | Yahoo Finance |
| AMD        | 2026-07-31 00:00:00 |   476.15      |         -34.8333  | NEUTRAL  | Yahoo Finance |
| AVAX-USD   | 2026-08-03 00:00:00 |     6.417     |         -18.6667  | NEUTRAL  | Kraken API    |
| AVGO       | 2026-07-31 00:00:00 |   389.28      |          23.75    | NEUTRAL  | Yahoo Finance |
| BA         | 2026-07-31 00:00:00 |   216.14      |         -17.5833  | NEUTRAL  | Yahoo Finance |
| BAC        | 2026-07-31 00:00:00 |    61.95      |          30.1667  | NEUTRAL  | Yahoo Finance |
| BITO       | 2026-07-31 00:00:00 |     8.52      |         -25.4167  | NEUTRAL  | Yahoo Finance |
| BONK-USD   | 2026-08-03 00:00:00 |     2.885e-06 |         -33.9167  | NEUTRAL  | Kraken API    |
| BTC-USD    | 2026-08-03 00:00:00 | 62968.2       |         -48.25    | NEUTRAL  | Kraken API    |
| C          | 2026-07-31 00:00:00 |   132.45      |         -13.5833  | NEUTRAL  | Yahoo Finance |
| CAT        | 2026-07-31 00:00:00 |   814.81      |         -15.1667  | NEUTRAL  | Yahoo Finance |
| CL         | 2026-07-31 00:00:00 |    91.3       |          -2.16667 | NEUTRAL  | Yahoo Finance |
| CMCSA      | 2026-07-31 00:00:00 |    23.96      |           1       | NEUTRAL  | Yahoo Finance |
| COMP-USD   | 2026-08-03 00:00:00 |    16.44      |         -24.5     | NEUTRAL  | Kraken API    |
| COST       | 2026-07-31 00:00:00 |   951.89      |          11.25    | NEUTRAL  | Yahoo Finance |
| CRM        | 2026-07-31 00:00:00 |   184.02      |          22.3333  | NEUTRAL  | Yahoo Finance |
| CRV-USD    | 2026-08-03 00:00:00 |     0.20054   |         -48.25    | NEUTRAL  | Kraken API    |
| CSCO       | 2026-07-31 00:00:00 |   115.99      |          37.5     | NEUTRAL  | Yahoo Finance |
| DE         | 2026-07-31 00:00:00 |   592.67      |          15.3333  | NEUTRAL  | Yahoo Finance |
| DIA        | 2026-07-31 00:00:00 |   524.32      |          25.8333  | NEUTRAL  | Yahoo Finance |
| DIS        | 2026-07-31 00:00:00 |    96.19      |         -37.5     | NEUTRAL  | Yahoo Finance |
| DOGE-USD   | 2026-08-03 00:00:00 |     0.0699027 |          -9.66667 | NEUTRAL  | Kraken API    |
| DOT-USD    | 2026-08-03 00:00:00 |     0.7897    |         -18.6667  | NEUTRAL  | Kraken API    |
| DXY-INDEX  | 2026-08-02 00:00:00 |    99.753     |         -12.3656  | NEUTRAL  | Yahoo Finance |
| EEM        | 2026-07-31 00:00:00 |    64.09      |          -4.33333 | NEUTRAL  | Yahoo Finance |
| EFA        | 2026-07-31 00:00:00 |   105.58      |          46.8333  | NEUTRAL  | Yahoo Finance |
| ETC-USD    | 2026-08-03 00:00:00 |     6.559     |         -46.5833  | NEUTRAL  | Kraken API    |
| ETH-USD    | 2026-08-03 00:00:00 |  1858.99      |         -17.4167  | NEUTRAL  | Kraken API    |
| EWJ        | 2026-07-31 00:00:00 |    92.39      |          -2       | NEUTRAL  | Yahoo Finance |
| FCX        | 2026-07-31 00:00:00 |    62.63      |          46.6667  | NEUTRAL  | Yahoo Finance |
| FIL-USD    | 2026-08-03 00:00:00 |     0.716     |         -15       | NEUTRAL  | Kraken API    |
| GDX        | 2026-07-31 00:00:00 |    74.1       |         -29.3333  | NEUTRAL  | Yahoo Finance |
| GDXJ       | 2026-07-31 00:00:00 |    95.39      |         -37.6667  | NEUTRAL  | Yahoo Finance |
| GLD        | 2026-07-31 00:00:00 |   371.54      |         -17.8333  | NEUTRAL  | Yahoo Finance |
| GOOGL      | 2026-07-31 00:00:00 |   356.13      |          28.1667  | NEUTRAL  | Yahoo Finance |
| GS         | 2026-07-31 00:00:00 |  1018.38      |         -21.5     | NEUTRAL  | Yahoo Finance |
| HBAR-USD   | 2026-08-03 00:00:00 |     0.06924   |           4.5     | NEUTRAL  | Kraken API    |
| HD         | 2026-07-31 00:00:00 |   331.96      |         -51.5833  | NEUTRAL  | Yahoo Finance |
| IBIT       | 2026-07-31 00:00:00 |    35.64      |         -43.4167  | NEUTRAL  | Yahoo Finance |
| IEF        | 2026-07-31 00:00:00 |    92.95      |         -57.75    | NEUTRAL  | Yahoo Finance |
| IEMG       | 2026-07-31 00:00:00 |    77.61      |          -4.83333 | NEUTRAL  | Yahoo Finance |
| INJ-USD    | 2026-08-03 00:00:00 |     5.01      |          -1       | NEUTRAL  | Kraken API    |
| INTC       | 2026-07-31 00:00:00 |    90.2       |         -14.8333  | NEUTRAL  | Yahoo Finance |
| ITA        | 2026-07-31 00:00:00 |   239.66      |          28.3333  | NEUTRAL  | Yahoo Finance |
| IWM        | 2026-07-31 00:00:00 |   291.2       |           9.75    | NEUTRAL  | Yahoo Finance |
| JNJ        | 2026-07-31 00:00:00 |   256.35      |         -11.1667  | NEUTRAL  | Yahoo Finance |
| JPM        | 2026-07-31 00:00:00 |   351.79      |          31.3333  | NEUTRAL  | Yahoo Finance |
| KO         | 2026-07-31 00:00:00 |    87.59      |          60.3333  | NEUTRAL  | Yahoo Finance |
| LIN        | 2026-07-31 00:00:00 |   478.38      |         -57.3333  | NEUTRAL  | Yahoo Finance |
| LINK-USD   | 2026-08-03 00:00:00 |     8.28284   |         -16.0833  | NEUTRAL  | Kraken API    |
| LLY        | 2026-07-31 00:00:00 |  1148.84      |         -20.1667  | NEUTRAL  | Yahoo Finance |
| LRCX       | 2026-07-31 00:00:00 |   293.02      |         -14.8333  | NEUTRAL  | Yahoo Finance |
| MCD        | 2026-07-31 00:00:00 |   270.64      |         -22       | NEUTRAL  | Yahoo Finance |
| MRK        | 2026-07-31 00:00:00 |   130.2       |          64       | NEUTRAL  | Yahoo Finance |
| MS         | 2026-07-31 00:00:00 |   210.42      |         -24.8333  | NEUTRAL  | Yahoo Finance |
| MU         | 2026-07-31 00:00:00 |   823.03      |         -16.5     | NEUTRAL  | Yahoo Finance |
| NEAR-USD   | 2026-08-03 00:00:00 |     1.7006    |         -60.9167  | NEUTRAL  | Kraken API    |
| NEM        | 2026-07-31 00:00:00 |    93.71      |         -26.8333  | NEUTRAL  | Yahoo Finance |
| NKE        | 2026-07-31 00:00:00 |    41.71      |         -64.5     | NEUTRAL  | Yahoo Finance |
| NOW        | 2026-07-31 00:00:00 |   111.23      |          -8.58333 | NEUTRAL  | Yahoo Finance |
| NVDA       | 2026-07-31 00:00:00 |   200.75      |         -35.25    | NEUTRAL  | Yahoo Finance |
| PEP        | 2026-07-31 00:00:00 |   139.56      |          -1.5     | NEUTRAL  | Yahoo Finance |
| PEPE-USD   | 2026-08-03 00:00:00 |     2.864e-06 |          18.75    | NEUTRAL  | Kraken API    |
| PFE        | 2026-07-31 00:00:00 |    25.01      |          20.4167  | NEUTRAL  | Yahoo Finance |
| PG         | 2026-07-31 00:00:00 |   144.49      |         -44.5     | NEUTRAL  | Yahoo Finance |
| QQQ        | 2026-07-31 00:00:00 |   687.99      |         -13.5833  | NEUTRAL  | Yahoo Finance |
| SBUX       | 2026-07-31 00:00:00 |   105.25      |          32.4167  | NEUTRAL  | Yahoo Finance |
| SHY        | 2026-07-31 00:00:00 |    82         |           6.41667 | NEUTRAL  | Yahoo Finance |
| SLB        | 2026-07-31 00:00:00 |    49.59      |          36.5     | NEUTRAL  | Yahoo Finance |
| SLV        | 2026-07-31 00:00:00 |    52.36      |         -30.8333  | NEUTRAL  | Yahoo Finance |
| SMH        | 2026-07-31 00:00:00 |   540.53      |         -10.25    | NEUTRAL  | Yahoo Finance |
| SOXX       | 2026-07-31 00:00:00 |   504.89      |         -12.25    | NEUTRAL  | Yahoo Finance |
| SPY        | 2026-07-31 00:00:00 |   747.03      |          19.1667  | NEUTRAL  | Yahoo Finance |
| TMUS       | 2026-07-31 00:00:00 |   172.71      |         -46.5     | NEUTRAL  | Yahoo Finance |
| TRX-USD    | 2026-08-03 00:00:00 |     0.325764  |          17.25    | NEUTRAL  | Kraken API    |
| TXN        | 2026-07-31 00:00:00 |   275.74      |         -15.5833  | NEUTRAL  | Yahoo Finance |
| UNH        | 2026-07-31 00:00:00 |   414.4       |          14.9167  | NEUTRAL  | Yahoo Finance |
| VEA        | 2026-07-31 00:00:00 |    70.62      |          41.6667  | NEUTRAL  | Yahoo Finance |
| VIXY       | 2026-07-31 00:00:00 |    20.51      |         -14.1667  | NEUTRAL  | Yahoo Finance |
| VTI        | 2026-07-31 00:00:00 |   368.21      |          19.1667  | NEUTRAL  | Yahoo Finance |
| VWO        | 2026-07-31 00:00:00 |    58.75      |          15.4167  | NEUTRAL  | Yahoo Finance |
| WFC        | 2026-07-31 00:00:00 |    86.45      |          15.0833  | NEUTRAL  | Yahoo Finance |
| WIF-USD    | 2026-08-03 00:00:00 |     0.138     |         -54.25    | NEUTRAL  | Kraken API    |
| WMT        | 2026-07-31 00:00:00 |   111.2       |         -40.5     | NEUTRAL  | Yahoo Finance |
| XBI        | 2026-07-31 00:00:00 |   147.01      |          17.5833  | NEUTRAL  | Yahoo Finance |
| XLB        | 2026-07-31 00:00:00 |    50.43      |          12.75    | NEUTRAL  | Yahoo Finance |
| XLC        | 2026-07-31 00:00:00 |   108.24      |         -64.5     | NEUTRAL  | Yahoo Finance |
| XLI        | 2026-07-31 00:00:00 |   179.84      |          27.9167  | NEUTRAL  | Yahoo Finance |
| XLK        | 2026-07-31 00:00:00 |   175.35      |         -10.25    | NEUTRAL  | Yahoo Finance |
| XLM-USD    | 2026-08-03 00:00:00 |     0.171311  |         -57.25    | NEUTRAL  | Kraken API    |
| XLP        | 2026-07-31 00:00:00 |    85.05      |          58.8333  | NEUTRAL  | Yahoo Finance |
| XLU        | 2026-07-31 00:00:00 |    44.35      |         -49.25    | NEUTRAL  | Yahoo Finance |
| XLV        | 2026-07-31 00:00:00 |   162.55      |          26.5     | NEUTRAL  | Yahoo Finance |
| XLY        | 2026-07-31 00:00:00 |   116.09      |          30.1667  | NEUTRAL  | Yahoo Finance |
| XRP-USD    | 2026-08-03 00:00:00 |     1.07134   |         -48.25    | NEUTRAL  | Kraken API    |
| YFI-USD    | 2026-08-03 00:00:00 |  2103.1       |          10.6667  | NEUTRAL  | Kraken API    |
| ZEC-USD    | 2026-08-03 00:00:00 |   476.22      |          -8.58333 | NEUTRAL  | Kraken API    |
| AGG        | 2026-07-31 00:00:00 |    97.37      |         -43.0833  | SHORT    | Yahoo Finance |
| APT-USD    | 2026-08-03 00:00:00 |     0.5588    |         -37       | SHORT    | Kraken API    |
| ARB-USD    | 2026-08-03 00:00:00 |     0.0804    |         -37       | SHORT    | Kraken API    |
| ARKK       | 2026-07-31 00:00:00 |    71.24      |         -52.8333  | SHORT    | Yahoo Finance |
| ATOM-USD   | 2026-08-03 00:00:00 |     1.2579    |         -47.6667  | SHORT    | Kraken API    |
| BCH-USD    | 2026-08-03 00:00:00 |   210.61      |         -39.3333  | SHORT    | Kraken API    |
| BND        | 2026-07-31 00:00:00 |    72.23      |         -44.75    | SHORT    | Yahoo Finance |
| DASH-USD   | 2026-08-03 00:00:00 |    31.105     |         -53.8333  | SHORT    | Kraken API    |
| FET-USD    | 2026-08-03 00:00:00 |     0.1395    |         -43       | SHORT    | Kraken API    |
| GRT-USD    | 2026-08-03 00:00:00 |     0.01441   |         -37.3333  | SHORT    | Kraken API    |
| HYG        | 2026-07-31 00:00:00 |    79.48      |         -42.8333  | SHORT    | Yahoo Finance |
| IBM        | 2026-07-31 00:00:00 |   223.65      |         -48.0833  | SHORT    | Yahoo Finance |
| ICP-USD    | 2026-08-03 00:00:00 |     2.055     |         -37       | SHORT    | Kraken API    |
| LDO-USD    | 2026-08-03 00:00:00 |     0.324     |         -31.9167  | SHORT    | Kraken API    |
| LTC-USD    | 2026-08-03 00:00:00 |    44.46      |         -37       | SHORT    | Kraken API    |
| META       | 2026-07-31 00:00:00 |   556.71      |         -54.0833  | SHORT    | Yahoo Finance |
| NFLX       | 2026-07-31 00:00:00 |    71.71      |         -34.75    | SHORT    | Yahoo Finance |
| OP-USD     | 2026-08-03 00:00:00 |     0.0856    |         -41       | SHORT    | Kraken API    |
| ORCL       | 2026-07-31 00:00:00 |   129.87      |         -31.75    | SHORT    | Yahoo Finance |
| POL-USD    | 2026-08-03 00:00:00 |     0.07278   |         -36.6667  | SHORT    | Kraken API    |
| QCOM       | 2026-07-31 00:00:00 |   147.61      |         -51.5833  | SHORT    | Yahoo Finance |
| RENDER-USD | 2026-08-03 00:00:00 |     1.362     |         -49.3333  | SHORT    | Kraken API    |
| SKY-USD    | 2026-08-03 00:00:00 |     0.05548   |         -50       | SHORT    | Kraken API    |
| SNX-USD    | 2026-08-03 00:00:00 |     0.2098    |         -34.8333  | SHORT    | Kraken API    |
| SOL-USD    | 2026-08-03 00:00:00 |    72.87      |         -48.25    | SHORT    | Kraken API    |
| SUSHI-USD  | 2026-08-03 00:00:00 |     0.1546    |         -35       | SHORT    | Kraken API    |
| TIA-USD    | 2026-08-03 00:00:00 |     0.3248    |         -46.3333  | SHORT    | Kraken API    |
| TLT        | 2026-07-31 00:00:00 |    82.25      |         -46.5     | SHORT    | Yahoo Finance |
| TSLA       | 2026-07-31 00:00:00 |   311.21      |         -63.0833  | SHORT    | Yahoo Finance |
| UPS        | 2026-07-31 00:00:00 |   104.22      |         -31.5     | SHORT    | Yahoo Finance |

## Edge Summary

- Symbols with trades: **160** of 160
- Beat buy-and-hold: **31.87%** of traded symbols
- Positive return: **29.38%** of traded symbols
- Median strategy return: **-10.33%** (benchmark **13.65%**)
- Median excess vs benchmark: **-26.39%**
- Median Sharpe: **-0.15**
- Median exposure: **44.01%**

> Edge is real only if both _beat buy-and-hold_ and _median excess_ are convincingly positive across many symbols. Treat a single high-return symbol as noise.

## Portfolio Backtest

Actual capital-allocation books (not per-symbol averages). Benchmarks: `equal_weight_buyhold` (whole tracked universe), `spy_buyhold` (100% SPY), and `sixty_forty` (60% SPY / 40% AGG). `high_conf_voltarget` inverse-vol-weights the HIGH-confidence book; `conviction_long_short` is market-neutral. Judge on **Sharpe** and **max_drawdown** out-of-sample, not raw return: a fully-invested long book wins on return in a bull market but carries all the risk.

| strategy              | scope         | ann_return   | ann_vol   |   sharpe | max_drawdown   | total_return   |   avg_gross_exposure |
|:----------------------|:--------------|:-------------|:----------|---------:|:---------------|:---------------|---------------------:|
| equal_weight_buyhold  | full          | -0.24%       | 31.84%    |    -0.01 | -43.58%        | -15.00%        |                 1    |
| equal_weight_buyhold  | out_of_sample | -19.78%      | 29.14%    |    -0.68 | -35.70%        | -22.62%        |                 1    |
| all_signals_ew        | full          | -21.02%      | 26.70%    |    -0.79 | -64.15%        | -52.77%        |                 1    |
| all_signals_ew        | out_of_sample | 12.58%       | 24.21%    |     0.52 | -19.48%        | 10.87%         |                 1    |
| high_conf_ew          | full          | -3.38%       | 31.44%    |    -0.11 | -43.52%        | -22.25%        |                 0.88 |
| high_conf_ew          | out_of_sample | 4.52%        | 27.25%    |     0.17 | -20.30%        | 0.78%          |                 0.88 |
| high_conf_voltarget   | full          | -0.55%       | 28.96%    |    -0.02 | -35.26%        | -13.26%        |                 0.88 |
| high_conf_voltarget   | out_of_sample | -1.71%       | 24.08%    |    -0.07 | -16.94%        | -4.88%         |                 0.88 |
| conviction_long_short | full          | -18.89%      | 22.96%    |    -0.82 | -51.11%        | -48.13%        |                 0.97 |
| conviction_long_short | out_of_sample | -17.12%      | 24.48%    |    -0.7  | -23.73%        | -19.36%        |                 0.97 |
| spy_buyhold           | full          | 5.80%        | 13.38%    |     0.43 | -18.13%        | 16.13%         |                 0.78 |
| spy_buyhold           | out_of_sample | -0.75%       | 9.96%     |    -0.07 | -12.06%        | -1.31%         |                 0.78 |
| sixty_forty           | full          | 3.20%        | 8.46%     |     0.38 | -10.90%        | 9.05%          |                 0.78 |
| sixty_forty           | out_of_sample | -1.89%       | 6.59%     |    -0.29 | -8.26%         | -2.23%         |                 0.78 |

## Walk-Forward Robustness

Each book measured across contiguous time folds (each a different regime). A book has durable edge only if `mean_sharpe` is positive, `min_sharpe` isn't deeply negative, and `pct_positive_folds` is high — a single great fold doesn't count. `fold_sharpes` lists each fold oldest-to-newest.

| strategy              |   n_folds |   mean_sharpe |   median_sharpe |   min_sharpe | pct_positive_folds   | mean_return   | fold_sharpes                 |
|:----------------------|----------:|--------------:|----------------:|-------------:|:---------------------|:--------------|:-----------------------------|
| equal_weight_buyhold  |         5 |          0.3  |            0.86 |        -1.16 | 60.00%               | -1.45%        | 1.57;-0.64;0.86;-1.16;0.89   |
| all_signals_ew        |         5 |         -0.92 |           -0.97 |        -2.3  | 20.00%               | -12.50%       | -0.46;-0.97;-2.30;0.70;-1.55 |
| high_conf_ew          |         5 |          0.04 |            0.05 |        -1.1  | 60.00%               | -4.35%        | 0.90;-1.10;0.05;-0.12;0.49   |
| high_conf_voltarget   |         5 |          0.26 |           -0.01 |        -0.74 | 40.00%               | -2.37%        | 1.58;-0.74;-0.01;-0.24;0.73  |
| conviction_long_short |         5 |         -0.93 |           -1.27 |        -1.98 | 20.00%               | -11.74%       | -1.57;-1.98;0.54;-0.34;-1.27 |
| spy_buyhold           |         5 |          0.56 |            0.07 |        -1.05 | 80.00%               | 3.27%         | 1.72;0.03;2.04;-1.05;0.07    |
| sixty_forty           |         5 |          0.48 |            0.01 |        -0.95 | 60.00%               | 1.85%         | 1.73;0.01;1.95;-0.95;-0.35   |

## Strategy Comparison

Each decision rule backtested over the same data. `out_of_sample` is the most recent ~35% of each symbol's history (unseen tail). A rule has real edge only if `median_excess` and `beat_benchmark_pct` stay positive out-of-sample, not just full-sample.

| strategy        | scope         |   symbols | beat_benchmark_pct   | positive_pct   | median_return   | median_benchmark   | median_excess   |   median_sharpe |   total_trades |
|:----------------|:--------------|----------:|:---------------------|:---------------|:----------------|:-------------------|:----------------|----------------:|---------------:|
| trend           | full          |       160 | 31.87%               | 29.38%         | -10.33%         | 13.65%             | -26.39%         |           -0.15 |          11304 |
| trend           | out_of_sample |       160 | 40.62%               | 44.38%         | -1.70%          | 2.99%              | -6.49%          |           -0.01 |           3819 |
| mean_reversion  | full          |       157 | 42.68%               | 51.59%         | 0.09%           | 13.16%             | -13.43%         |            0.04 |           1280 |
| mean_reversion  | out_of_sample |       127 | 48.82%               | 59.84%         | 0.39%           | -1.16%             | -0.69%          |            0.63 |            454 |
| regime_adaptive | full          |       160 | 32.50%               | 30.63%         | -10.18%         | 13.65%             | -26.41%         |           -0.13 |          11587 |
| regime_adaptive | out_of_sample |       160 | 40.62%               | 45.00%         | -1.63%          | 2.99%              | -5.51%          |            0.02 |           3932 |

## Signal Calibration

Realized forward return in the signal's direction, grouped by confidence. HIGH should outrank LOW for the confidence score to be meaningful.

| confidence_level   |   horizon |     n | mean_return   | median_return   | win_rate   |
|:-------------------|----------:|------:|:--------------|:----------------|:-----------|
| HIGH               |         5 |  7812 | 0.08%         | 0.07%           | 51.23%     |
| MEDIUM             |         5 | 29123 | 0.02%         | 0.06%           | 50.66%     |
| LOW                |         5 |  3433 | -0.65%        | -0.56%          | 44.48%     |
| ALL                |         5 | 40368 | -0.02%        | 0.02%           | 50.25%     |
| HIGH               |        10 |  7775 | 0.33%         | 0.08%           | 50.91%     |
| MEDIUM             |        10 | 28925 | 0.13%         | 0.09%           | 50.65%     |
| LOW                |        10 |  3407 | -0.95%        | -0.79%          | 44.85%     |
| ALL                |        10 | 40107 | 0.07%         | 0.03%           | 50.21%     |
| HIGH               |        20 |  7713 | 0.64%         | 0.26%           | 52.13%     |
| MEDIUM             |        20 | 28500 | 0.72%         | 0.52%           | 52.95%     |
| LOW                |        20 |  3325 | -0.77%        | -0.68%          | 46.74%     |
| ALL                |        20 | 39538 | 0.58%         | 0.38%           | 52.27%     |

## Backtest Summary

### Data Quality / Signal Availability

- **ok**: 160 symbols

| symbol     |   trades | return   | benchmark_return   | mdd     |   sharpe | exposure   | skipped_reason   |
|:-----------|---------:|:---------|:-------------------|:--------|---------:|:-----------|:-----------------|
| AAPL       |       61 | 4.79%    | 80.93%             | -20.65% |     0.2  | 49.25%     | ok               |
| AAVE-USD   |       76 | -51.07%  | -52.69%            | -68.26% |    -0.47 | 38.89%     | ok               |
| ABBV       |       70 | -22.77%  | 40.31%             | -30.55% |    -0.49 | 46.92%     | ok               |
| ADA-USD    |       86 | -82.80%  | -70.70%            | -88.49% |    -0.67 | 46.17%     | ok               |
| ADBE       |       66 | -30.84%  | -54.61%            | -32.35% |    -0.37 | 56.91%     | ok               |
| AGG        |       69 | -6.23%   | -0.92%             | -10.17% |    -1.01 | 33.11%     | ok               |
| ALGO-USD   |       84 | -45.11%  | -64.24%            | -44.46% |    -0.46 | 36.97%     | ok               |
| AMAT       |       71 | -37.16%  | 146.97%            | -57.08% |    -0.37 | 50.42%     | ok               |
| AMD        |       54 | 2.60%    | 129.59%            | -44.27% |     0.24 | 35.44%     | ok               |
| AMGN       |       73 | -12.19%  | 40.70%             | -34.19% |    -0.2  | 47.42%     | ok               |
| AMZN       |       79 | -51.38%  | 54.88%             | -52.38% |    -1.46 | 38.94%     | ok               |
| APT-USD    |       70 | -27.57%  | -91.35%            | -66.73% |    -0.05 | 41.57%     | ok               |
| ARB-USD    |       78 | -30.33%  | -80.94%            | -62.55% |    -0.12 | 41.38%     | ok               |
| ARKK       |       89 | -32.04%  | 40.37%             | -37.98% |    -0.54 | 40.77%     | ok               |
| ATOM-USD   |       88 | -64.38%  | -72.87%            | -73.98% |    -1.01 | 46.55%     | ok               |
| AVAX-USD   |       79 | -58.65%  | -71.29%            | -65.75% |    -0.76 | 38.89%     | ok               |
| AVGO       |       62 | 22.76%   | 197.45%            | -35.76% |     0.42 | 41.10%     | ok               |
| BA         |       67 | 6.57%    | 8.89%              | -30.56% |     0.23 | 48.59%     | ok               |
| BAC        |       78 | -6.12%   | 74.02%             | -27.64% |    -0.08 | 51.08%     | ok               |
| BCH-USD    |       78 | 0.36%    | -33.19%            | -54.26% |     0.22 | 50.77%     | ok               |
| BITO       |       80 | -23.70%  | -73.21%            | -42.82% |    -0.16 | 39.60%     | ok               |
| BLK        |       83 | -11.50%  | 30.41%             | -26.90% |    -0.27 | 44.26%     | ok               |
| BND        |       67 | -7.01%   | -0.86%             | -9.98%  |    -1.11 | 34.61%     | ok               |
| BONK-USD   |       70 | 51.60%   | -78.84%            | -51.50% |     0.63 | 43.10%     | ok               |
| BTC-USD    |       74 | 6.22%    | -25.31%            | -23.38% |     0.24 | 51.92%     | ok               |
| C          |       79 | -30.84%  | 130.31%            | -38.11% |    -0.62 | 50.75%     | ok               |
| CAT        |       72 | 16.31%   | 140.22%            | -21.02% |     0.37 | 54.08%     | ok               |
| CL         |       62 | 5.38%    | 3.67%              | -14.32% |     0.24 | 44.09%     | ok               |
| CMCSA      |       80 | -45.38%  | -39.96%            | -48.04% |    -1.23 | 42.10%     | ok               |
| COMP-USD   |       93 | -43.71%  | -67.76%            | -57.10% |    -0.32 | 46.36%     | ok               |
| COP        |       72 | -18.12%  | 6.62%              | -43.77% |    -0.28 | 43.76%     | ok               |
| COST       |       62 | -1.10%   | 31.19%             | -29.73% |     0.03 | 41.93%     | ok               |
| CRM        |       63 | -39.56%  | -39.72%            | -41.36% |    -0.83 | 42.76%     | ok               |
| CRV-USD    |       70 | -0.17%   | -55.44%            | -39.89% |     0.23 | 36.59%     | ok               |
| CSCO       |       59 | 23.34%   | 134.32%            | -21.79% |     0.51 | 47.75%     | ok               |
| CVX        |       73 | -9.30%   | 31.33%             | -29.13% |    -0.19 | 40.60%     | ok               |
| DASH-USD   |       63 | -41.80%  | 20.03%             | -64.43% |    -0.02 | 29.50%     | ok               |
| DBC        |       62 | -10.34%  | 32.84%             | -25.70% |    -0.31 | 35.27%     | ok               |
| DE         |       70 | -5.05%   | 58.43%             | -24.56% |    -0.01 | 45.42%     | ok               |
| DIA        |       60 | -3.93%   | 35.14%             | -12.94% |    -0.18 | 43.59%     | ok               |
| DIS        |       66 | -17.76%  | -12.81%            | -28.17% |    -0.32 | 44.09%     | ok               |
| DOGE-USD   |       72 | -27.95%  | -65.35%            | -62.31% |    -0.05 | 49.04%     | ok               |
| DOT-USD    |       88 | -63.03%  | -83.24%            | -67.64% |    -0.74 | 48.08%     | ok               |
| DXY-INDEX  |       42 | -1.69%   | -1.42%             | -6.29%  |    -0.25 | 32.68%     | ok               |
| EEM        |       64 | -10.91%  | 57.01%             | -25.67% |    -0.3  | 41.26%     | ok               |
| EFA        |       60 | -10.31%  | 33.22%             | -13.72% |    -0.4  | 42.43%     | ok               |
| EOG        |       81 | -17.23%  | 25.24%             | -48.13% |    -0.3  | 48.92%     | ok               |
| ETC-USD    |       62 | -31.66%  | -66.46%            | -48.09% |    -0.43 | 28.93%     | ok               |
| ETH-USD    |       62 | 141.28%  | -16.87%            | -30.11% |     1.2  | 46.17%     | ok               |
| EWJ        |       62 | -22.06%  | 29.80%             | -30.73% |    -0.76 | 37.10%     | ok               |
| FCX        |       67 | -29.92%  | 57.16%             | -48.22% |    -0.35 | 45.92%     | ok               |
| FET-USD    |       87 | -47.71%  | -78.63%            | -52.82% |    -0.28 | 41.76%     | ok               |
| FIL-USD    |       70 | -50.07%  | -77.93%            | -51.27% |    -0.65 | 34.48%     | ok               |
| FXI        |       44 | -0.68%   | 55.52%             | -23.91% |     0.07 | 30.45%     | ok               |
| GDX        |       58 | 8.52%    | 150.00%            | -34.99% |     0.26 | 47.09%     | ok               |
| GDXJ       |       64 | -23.69%  | 165.49%            | -44.93% |    -0.23 | 45.26%     | ok               |
| GE         |       78 | -1.94%   | 168.62%            | -27.82% |     0.09 | 51.41%     | ok               |
| GLD        |       50 | 21.77%   | 84.27%             | -16.63% |     0.57 | 47.75%     | ok               |
| GOOGL      |       55 | 78.89%   | 163.00%            | -20.41% |     1.18 | 52.25%     | ok               |
| GRT-USD    |       83 | 2.87%    | -88.04%            | -50.20% |     0.25 | 43.87%     | ok               |
| GS         |       76 | -0.82%   | 163.15%            | -22.13% |     0.08 | 50.92%     | ok               |
| HD         |       73 | -7.53%   | -11.09%            | -18.58% |    -0.12 | 44.09%     | ok               |
| HON        |       95 | -27.63%  | 22.48%             | -29.81% |    -0.75 | 52.41%     | ok               |
| HYG        |       83 | -9.38%   | 2.69%              | -9.89%  |    -1.1  | 34.28%     | ok               |
| IBIT       |       34 | 30.82%   | -6.24%             | -18.95% |     0.66 | 31.29%     | ok               |
| IBM        |       75 | -24.56%  | 14.14%             | -47.10% |    -0.29 | 50.75%     | ok               |
| ICP-USD    |       77 | -20.89%  | -68.46%            | -52.30% |     0.04 | 34.67%     | ok               |
| IEF        |       82 | -11.24%  | -2.39%             | -11.70% |    -1.58 | 33.94%     | ok               |
| IEMG       |       58 | -9.40%   | 51.17%             | -26.84% |    -0.27 | 40.77%     | ok               |
| INJ-USD    |       75 | -52.79%  | -62.42%            | -76.24% |    -0.5  | 38.12%     | ok               |
| INTC       |       66 | 59.37%   | 105.00%            | -60.60% |     0.64 | 48.59%     | ok               |
| INTU       |       69 | -19.42%  | -51.50%            | -42.15% |    -0.23 | 41.76%     | ok               |
| ITA        |       72 | -5.10%   | 85.52%             | -23.75% |    -0.07 | 46.59%     | ok               |
| IWM        |       48 | 9.40%    | 40.79%             | -12.83% |     0.39 | 35.77%     | ok               |
| JNJ        |       70 | 6.86%    | 60.70%             | -17.51% |     0.29 | 50.75%     | ok               |
| JPM        |       77 | -23.06%  | 86.90%             | -33.43% |    -0.58 | 52.25%     | ok               |
| KO         |       51 | 23.75%   | 47.16%             | -8.20%  |     0.85 | 37.94%     | ok               |
| LDO-USD    |       78 | 34.87%   | -74.49%            | -61.16% |     0.54 | 43.10%     | ok               |
| LIN        |       66 | -8.27%   | 3.42%              | -21.53% |    -0.25 | 37.27%     | ok               |
| LINK-USD   |       73 | -17.43%  | -44.12%            | -49.94% |     0.06 | 43.87%     | ok               |
| LLY        |       71 | -27.76%  | 50.74%             | -53.34% |    -0.41 | 47.75%     | ok               |
| LRCX       |       82 | -24.73%  | 206.30%            | -60.21% |    -0.15 | 42.60%     | ok               |
| LTC-USD    |       72 | -30.38%  | -65.24%            | -47.04% |    -0.24 | 49.81%     | ok               |
| MCD        |       77 | -3.77%   | -7.49%             | -18.81% |    -0.1  | 38.27%     | ok               |
| META       |       76 | -33.48%  | 10.03%             | -42.12% |    -0.59 | 47.42%     | ok               |
| MPC        |       67 | -6.22%   | 76.26%             | -44.76% |     0.01 | 49.42%     | ok               |
| MRK        |       67 | -27.34%  | 5.43%              | -35.95% |    -0.63 | 43.59%     | ok               |
| MS         |       77 | -10.18%  | 141.75%            | -27.79% |    -0.16 | 49.58%     | ok               |
| MSFT       |       81 | -37.64%  | 14.40%             | -39.15% |    -0.99 | 47.09%     | ok               |
| MU         |       51 | 215.18%  | 743.10%            | -68.76% |     1.21 | 58.40%     | ok               |
| NEAR-USD   |       83 | -11.63%  | -44.52%            | -59.54% |     0.13 | 40.42%     | ok               |
| NEM        |       70 | -20.55%  | 176.35%            | -38.49% |    -0.15 | 52.75%     | ok               |
| NFLX       |       70 | 23.46%   | 18.56%             | -21.09% |     0.55 | 53.24%     | ok               |
| NKE        |       87 | -37.65%  | -57.94%            | -55.35% |    -0.53 | 43.93%     | ok               |
| NOW        |       80 | 1.54%    | -26.60%            | -26.78% |     0.18 | 45.76%     | ok               |
| NVDA       |       73 | -29.68%  | 117.87%            | -45.14% |    -0.24 | 59.18%     | ok               |
| OP-USD     |       66 | -13.59%  | -92.07%            | -71.26% |     0.09 | 34.87%     | ok               |
| ORCL       |       70 | 117.74%  | 15.52%             | -29.47% |     0.96 | 55.91%     | ok               |
| OXY        |       71 | 9.24%    | -6.13%             | -31.06% |     0.27 | 45.59%     | ok               |
| PEP        |       77 | -2.90%   | -14.41%            | -21.35% |    -0.02 | 48.75%     | ok               |
| PEPE-USD   |       83 | -5.04%   | -63.81%            | -57.66% |     0.24 | 46.17%     | ok               |
| PFE        |       79 | -41.91%  | -8.12%             | -42.74% |    -1.36 | 36.61%     | ok               |
| PG         |       66 | -19.26%  | -9.89%             | -24.25% |    -0.73 | 38.10%     | ok               |
| PM         |       83 | -5.09%   | 105.89%            | -34.41% |    -0.02 | 55.57%     | ok               |
| POL-USD    |       79 | 23.47%   | -73.25%            | -47.04% |     0.45 | 47.89%     | ok               |
| QCOM       |       77 | -16.48%  | -13.46%            | -56.59% |    -0.06 | 45.59%     | ok               |
| QQQ        |       60 | 20.33%   | 56.71%             | -12.88% |     0.58 | 43.59%     | ok               |
| RENDER-USD |      100 | -21.35%  | -64.37%            | -43.50% |     0.07 | 42.15%     | ok               |
| RTX        |       54 | 40.34%   | 136.82%            | -16.99% |     0.87 | 53.41%     | ok               |
| SBUX       |       62 | -19.04%  | 15.58%             | -29.22% |    -0.35 | 39.93%     | ok               |
| SCHW       |       76 | -9.83%   | 56.68%             | -31.92% |    -0.15 | 48.92%     | ok               |
| SHIB-USD   |       76 | -30.25%  | -65.03%            | -47.96% |    -0.21 | 52.49%     | ok               |
| SHY        |       46 | -2.23%   | 0.24%              | -2.85%  |    -0.78 | 34.11%     | ok               |
| SKY-USD    |       76 | -31.51%  | -4.06%             | -47.82% |    -0.38 | 42.16%     | ok               |
| SLB        |       77 | -28.71%  | -1.61%             | -54.23% |    -0.51 | 51.25%     | ok               |
| SLV        |       62 | 44.03%   | 135.54%            | -42.66% |     0.64 | 44.09%     | ok               |
| SMH        |       48 | 66.15%   | 140.25%            | -33.99% |     0.97 | 45.92%     | ok               |
| SNX-USD    |       64 | -15.33%  | -76.92%            | -36.73% |     0.08 | 37.74%     | ok               |
| SOL-USD    |       74 | -47.29%  | -50.79%            | -53.85% |    -0.34 | 59.58%     | ok               |
| SOXX       |       55 | 62.67%   | 121.32%            | -40.34% |     0.89 | 44.93%     | ok               |
| SPY        |       62 | 1.82%    | 45.98%             | -16.47% |     0.12 | 49.25%     | ok               |
| SUSHI-USD  |      104 | -83.25%  | -80.53%            | -86.63% |    -1.35 | 38.12%     | ok               |
| T          |       66 | 32.45%   | 35.17%             | -17.01% |     0.74 | 54.08%     | ok               |
| TGT        |       62 | -21.64%  | -14.87%            | -40.57% |    -0.47 | 37.27%     | ok               |
| TIA-USD    |       91 | -44.87%  | -92.04%            | -72.27% |    -0.29 | 39.08%     | ok               |
| TLT        |       72 | -19.44%  | -14.08%            | -21.87% |    -1.44 | 33.94%     | ok               |
| TMO        |       61 | 26.12%   | -3.90%             | -18.85% |     0.57 | 52.58%     | ok               |
| TMUS       |       68 | 4.31%    | 5.32%              | -25.71% |     0.19 | 46.59%     | ok               |
| TRX-USD    |       68 | 10.63%   | 39.61%             | -22.90% |     0.37 | 48.28%     | ok               |
| TSLA       |       74 | -22.15%  | 77.49%             | -57.89% |    -0.04 | 42.26%     | ok               |
| TXN        |       73 | -16.39%  | 60.03%             | -47.39% |    -0.11 | 51.25%     | ok               |
| UNH        |       76 | 23.80%   | -13.05%            | -28.45% |     0.45 | 52.58%     | ok               |
| UNI-USD    |       90 | -72.21%  | -45.28%            | -80.33% |    -0.84 | 46.17%     | ok               |
| UPS        |       72 | -41.40%  | -32.31%            | -41.64% |    -0.86 | 40.27%     | ok               |
| USO        |       70 | 10.30%   | 76.08%             | -43.35% |     0.29 | 34.78%     | ok               |
| VEA        |       56 | -2.39%   | 41.32%             | -17.93% |    -0.05 | 43.09%     | ok               |
| VIXY       |       96 | -80.41%  | -64.39%            | -88.42% |    -1.02 | 31.78%     | ok               |
| VNQ        |       73 | -17.46%  | 12.79%             | -24.92% |    -0.74 | 37.44%     | ok               |
| VTI        |       68 | -4.92%   | 44.72%             | -18.77% |    -0.12 | 49.58%     | ok               |
| VWO        |       82 | -16.67%  | 40.68%             | -25.20% |    -0.61 | 42.43%     | ok               |
| VZ         |       83 | -25.88%  | 18.48%             | -26.98% |    -0.83 | 38.10%     | ok               |
| WFC        |       84 | -19.95%  | 51.48%             | -29.78% |    -0.35 | 49.58%     | ok               |
| WIF-USD    |       72 | -52.90%  | -78.04%            | -61.76% |    -0.39 | 33.91%     | ok               |
| WMT        |       65 | 11.13%   | 84.96%             | -21.31% |     0.37 | 49.25%     | ok               |
| XBI        |       66 | -7.94%   | 48.57%             | -18.51% |    -0.13 | 39.93%     | ok               |
| XLB        |       62 | -10.08%  | 12.88%             | -24.41% |    -0.33 | 35.44%     | ok               |
| XLC        |       67 | 11.88%   | 36.00%             | -12.33% |     0.44 | 52.75%     | ok               |
| XLE        |       75 | -7.48%   | 35.08%             | -37.64% |    -0.11 | 45.26%     | ok               |
| XLF        |       80 | -12.29%  | 40.18%             | -23.61% |    -0.4  | 47.92%     | ok               |
| XLI        |       70 | -6.90%   | 47.05%             | -14.12% |    -0.23 | 42.93%     | ok               |
| XLK        |       40 | 65.83%   | 69.13%             | -14.75% |     1.22 | 45.59%     | ok               |
| XLM-USD    |       65 | 12.70%   | -40.20%            | -50.36% |     0.35 | 45.40%     | ok               |
| XLP        |       64 | 8.30%    | 13.16%             | -10.28% |     0.49 | 41.10%     | ok               |
| XLU        |       67 | -5.24%   | 39.14%             | -20.40% |    -0.19 | 39.10%     | ok               |
| XLV        |       66 | -14.73%  | 11.01%             | -18.49% |    -0.73 | 34.61%     | ok               |
| XLY        |       70 | 2.91%    | 28.77%             | -14.01% |     0.16 | 44.09%     | ok               |
| XOM        |       55 | 9.21%    | 43.42%             | -20.29% |     0.32 | 37.94%     | ok               |
| XRP-USD    |       54 | -22.96%  | -50.06%            | -38.94% |    -0.14 | 33.14%     | ok               |
| YFI-USD    |       81 | -64.19%  | -62.06%            | -71.12% |    -1.03 | 40.61%     | ok               |
| ZEC-USD    |       64 | 36.67%   | 1167.89%           | -50.14% |     0.52 | 37.16%     | ok               |

## AAPL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 12.97%   | 80.93%             | -21.71% |     0.34 |       68 | 53.41%     | ok               |
|          15 | 9.50%    | 80.93%             | -23.86% |     0.28 |       75 | 60.57%     | ok               |
|          30 | 4.79%    | 80.93%             | -20.65% |     0.2  |       61 | 49.25%     | ok               |
|          25 | 2.60%    | 80.93%             | -20.03% |     0.16 |       67 | 51.08%     | ok               |
|          35 | 2.44%    | 80.93%             | -22.04% |     0.16 |       61 | 47.75%     | ok               |

## AAVE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 6.80%    | -52.69%            | -43.61% |     0.29 |       42 | 31.61%     | ok               |
|          45 | -2.67%   | -52.69%            | -46.87% |     0.17 |       44 | 26.63%     | ok               |
|          35 | -11.47%  | -52.69%            | -51.96% |     0.09 |       52 | 34.87%     | ok               |
|          15 | -46.15%  | -52.69%            | -61.76% |    -0.25 |       81 | 52.87%     | ok               |
|          50 | -32.94%  | -52.69%            | -42.99% |    -0.36 |       42 | 19.35%     | ok               |

## ABBV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -12.92%  | 40.31%             | -28.51% |    -0.27 |       50 | 34.94%     | ok               |
|          25 | -22.86%  | 40.31%             | -31.26% |    -0.49 |       69 | 48.75%     | ok               |
|          30 | -22.77%  | 40.31%             | -30.55% |    -0.49 |       70 | 46.92%     | ok               |
|          20 | -23.45%  | 40.31%             | -30.60% |    -0.5  |       69 | 50.58%     | ok               |
|          40 | -21.93%  | 40.31%             | -26.61% |    -0.52 |       68 | 39.77%     | ok               |

## ADA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -78.58%  | -70.70%            | -85.80% |    -0.61 |       59 | 27.39%     | ok               |
|          45 | -80.19%  | -70.70%            | -87.45% |    -0.62 |       60 | 31.61%     | ok               |
|          35 | -82.54%  | -70.70%            | -89.22% |    -0.67 |       78 | 42.15%     | ok               |
|          30 | -82.80%  | -70.70%            | -88.49% |    -0.67 |       86 | 46.17%     | ok               |
|          40 | -82.69%  | -70.70%            | -89.23% |    -0.69 |       76 | 37.16%     | ok               |

## ADBE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 3.20%    | -54.61%            | -21.57% |     0.18 |       76 | 49.42%     | ok               |
|          40 | -14.98%  | -54.61%            | -29.34% |    -0.17 |       72 | 42.26%     | ok               |
|          25 | -20.57%  | -54.61%            | -28.88% |    -0.17 |       50 | 60.73%     | ok               |
|          20 | -28.49%  | -54.61%            | -32.09% |    -0.3  |       52 | 63.39%     | ok               |
|          15 | -31.07%  | -54.61%            | -36.64% |    -0.35 |       61 | 65.39%     | ok               |

## AGG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -6.23%   | -0.92%             | -10.17% |    -1.01 |       69 | 33.11%     | ok               |
|          20 | -7.77%   | -0.92%             | -11.49% |    -1.12 |       71 | 38.60%     | ok               |
|          50 | -5.20%   | -0.92%             | -7.92%  |    -1.14 |       52 | 18.14%     | ok               |
|          45 | -5.79%   | -0.92%             | -7.91%  |    -1.14 |       56 | 22.63%     | ok               |
|          25 | -7.95%   | -0.92%             | -12.13% |    -1.2  |       71 | 36.94%     | ok               |

## ALGO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -45.11%  | -64.24%            | -44.46% |    -0.46 |       84 | 36.97%     | ok               |
|          35 | -50.98%  | -64.24%            | -47.54% |    -0.69 |       62 | 30.46%     | ok               |
|          15 | -64.56%  | -64.24%            | -66.08% |    -0.77 |       86 | 49.23%     | ok               |
|          25 | -62.49%  | -64.24%            | -69.14% |    -0.78 |       82 | 43.68%     | ok               |
|          50 | -45.64%  | -64.24%            | -48.43% |    -0.81 |       42 | 16.86%     | ok               |

## AMAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -26.01%  | 146.97%            | -54.69% |    -0.14 |       68 | 59.40%     | ok               |
|          30 | -37.16%  | 146.97%            | -57.08% |    -0.37 |       71 | 50.42%     | ok               |
|          35 | -37.60%  | 146.97%            | -55.13% |    -0.39 |       73 | 48.09%     | ok               |
|          50 | -36.57%  | 146.97%            | -48.72% |    -0.42 |       52 | 36.11%     | ok               |
|          20 | -44.37%  | 146.97%            | -60.72% |    -0.47 |       74 | 55.74%     | ok               |

## AMD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 3.45%    | 129.59%            | -44.55% |     0.24 |       56 | 30.28%     | ok               |
|          40 | 2.60%    | 129.59%            | -44.27% |     0.24 |       54 | 35.44%     | ok               |
|          35 | -4.38%   | 129.59%            | -48.82% |     0.17 |       62 | 37.10%     | ok               |
|          30 | -16.99%  | 129.59%            | -54.80% |     0.04 |       63 | 39.60%     | ok               |
|          45 | -17.42%  | 129.59%            | -53.48% |     0.01 |       62 | 33.11%     | ok               |

## AMGN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -7.40%   | 40.70%             | -26.65% |    -0.07 |       71 | 53.41%     | ok               |
|          35 | -7.89%   | 40.70%             | -31.29% |    -0.09 |       69 | 43.59%     | ok               |
|          15 | -11.51%  | 40.70%             | -27.98% |    -0.15 |       68 | 58.24%     | ok               |
|          30 | -12.19%  | 40.70%             | -34.19% |    -0.2  |       73 | 47.42%     | ok               |
|          25 | -14.69%  | 40.70%             | -33.47% |    -0.25 |       67 | 49.92%     | ok               |

## AMZN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -21.50%  | 54.88%             | -27.15% |    -0.65 |       52 | 29.28%     | ok               |
|          50 | -26.31%  | 54.88%             | -34.08% |    -0.96 |       48 | 22.63%     | ok               |
|          45 | -31.84%  | 54.88%             | -34.08% |    -1.16 |       54 | 25.79%     | ok               |
|          35 | -46.98%  | 54.88%             | -48.08% |    -1.36 |       68 | 33.28%     | ok               |
|          30 | -51.38%  | 54.88%             | -52.38% |    -1.46 |       79 | 38.94%     | ok               |

## APT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 19.10%   | -91.35%            | -46.73% |     0.42 |       40 | 18.97%     | ok               |
|          45 | -11.65%  | -91.35%            | -63.86% |     0.05 |       56 | 24.52%     | ok               |
|          20 | -21.22%  | -91.35%            | -68.18% |     0.05 |       71 | 50.00%     | ok               |
|          35 | -17.11%  | -91.35%            | -60.63% |     0.04 |       66 | 35.25%     | ok               |
|          25 | -25.70%  | -91.35%            | -68.00% |    -0.02 |       68 | 45.59%     | ok               |

## ARB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 36.74%   | -80.94%            | -51.09% |     0.54 |       88 | 57.66%     | ok               |
|          20 | 5.11%    | -80.94%            | -58.28% |     0.32 |       74 | 51.53%     | ok               |
|          40 | -2.55%   | -80.94%            | -44.30% |     0.19 |       60 | 31.42%     | ok               |
|          25 | -11.76%  | -80.94%            | -55.53% |     0.16 |       76 | 47.32%     | ok               |
|          45 | -3.87%   | -80.94%            | -47.43% |     0.16 |       60 | 24.14%     | ok               |

## ARKK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -26.69%  | 40.37%             | -37.76% |    -0.32 |       94 | 52.25%     | ok               |
|          20 | -30.57%  | 40.37%             | -37.99% |    -0.43 |       91 | 47.75%     | ok               |
|          30 | -32.04%  | 40.37%             | -37.98% |    -0.54 |       89 | 40.77%     | ok               |
|          35 | -34.33%  | 40.37%             | -38.33% |    -0.63 |       88 | 38.10%     | ok               |
|          40 | -35.71%  | 40.37%             | -39.63% |    -0.71 |       80 | 33.28%     | ok               |

## ATOM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -60.79%  | -72.87%            | -69.46% |    -0.75 |       85 | 62.45%     | ok               |
|          25 | -60.73%  | -72.87%            | -71.09% |    -0.83 |       93 | 53.26%     | ok               |
|          45 | -56.80%  | -72.87%            | -67.17% |    -0.99 |       74 | 30.84%     | ok               |
|          30 | -64.38%  | -72.87%            | -73.98% |    -1.01 |       88 | 46.55%     | ok               |
|          20 | -68.44%  | -72.87%            | -74.75% |    -1.03 |       95 | 56.51%     | ok               |

## AVAX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -5.68%   | -71.29%            | -40.19% |     0.08 |       34 | 18.39%     | ok               |
|          45 | -15.96%  | -71.29%            | -47.25% |    -0.09 |       36 | 22.41%     | ok               |
|          40 | -24.78%  | -71.29%            | -51.30% |    -0.2  |       40 | 25.29%     | ok               |
|          15 | -40.87%  | -71.29%            | -51.60% |    -0.26 |       77 | 52.87%     | ok               |
|          35 | -36.63%  | -71.29%            | -52.74% |    -0.36 |       58 | 30.65%     | ok               |

## AVGO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 24.67%   | 197.45%            | -35.84% |     0.44 |       56 | 29.78%     | ok               |
|          30 | 22.76%   | 197.45%            | -35.76% |     0.42 |       62 | 41.10%     | ok               |
|          40 | 21.29%   | 197.45%            | -40.70% |     0.41 |       60 | 34.94%     | ok               |
|          25 | 20.18%   | 197.45%            | -38.01% |     0.39 |       70 | 42.60%     | ok               |
|          45 | 19.59%   | 197.45%            | -41.66% |     0.39 |       56 | 33.11%     | ok               |

## BA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 26.03%   | 8.89%              | -13.34% |     0.67 |       42 | 31.45%     | ok               |
|          35 | 30.93%   | 8.89%              | -23.77% |     0.6  |       70 | 44.43%     | ok               |
|          40 | 20.11%   | 8.89%              | -23.90% |     0.47 |       46 | 38.60%     | ok               |
|          25 | 9.53%    | 8.89%              | -32.48% |     0.28 |       70 | 51.91%     | ok               |
|          30 | 6.57%    | 8.89%              | -30.56% |     0.23 |       67 | 48.59%     | ok               |

## BAC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 0.06%    | 74.02%             | -21.48% |     0.09 |       80 | 55.74%     | ok               |
|          35 | -1.14%   | 74.02%             | -29.13% |     0.04 |       70 | 47.25%     | ok               |
|          45 | -0.84%   | 74.02%             | -22.29% |     0.04 |       64 | 38.60%     | ok               |
|          15 | -5.57%   | 74.02%             | -23.70% |    -0.04 |       80 | 60.73%     | ok               |
|          25 | -4.87%   | 74.02%             | -27.14% |    -0.04 |       80 | 53.74%     | ok               |

## BCH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 1.58%    | -33.19%            | -51.12% |     0.26 |       74 | 59.77%     | ok               |
|          30 | 0.36%    | -33.19%            | -54.26% |     0.22 |       78 | 50.77%     | ok               |
|          20 | -8.15%   | -33.19%            | -54.47% |     0.16 |       70 | 56.32%     | ok               |
|          40 | -15.34%  | -33.19%            | -61.24% |    -0    |       67 | 41.95%     | ok               |
|          25 | -21.45%  | -33.19%            | -61.06% |    -0.01 |       73 | 53.07%     | ok               |

## BITO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -7.06%   | -73.21%            | -31.98% |     0.03 |       54 | 22.96%     | ok               |
|          30 | -23.70%  | -73.21%            | -42.82% |    -0.16 |       80 | 39.60%     | ok               |
|          15 | -29.32%  | -73.21%            | -48.38% |    -0.18 |       89 | 48.59%     | ok               |
|          45 | -21.81%  | -73.21%            | -41.16% |    -0.2  |       62 | 26.62%     | ok               |
|          40 | -25.31%  | -73.21%            | -43.67% |    -0.23 |       66 | 31.45%     | ok               |

## BLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -2.59%   | 30.41%             | -21.48% |     0.01 |       82 | 49.08%     | ok               |
|          35 | -5.51%   | 30.41%             | -20.79% |    -0.1  |       88 | 40.43%     | ok               |
|          40 | -7.25%   | 30.41%             | -22.83% |    -0.17 |       78 | 36.11%     | ok               |
|          25 | -9.14%   | 30.41%             | -24.62% |    -0.19 |       79 | 46.92%     | ok               |
|          15 | -11.89%  | 30.41%             | -25.00% |    -0.24 |       83 | 52.75%     | ok               |

## BND Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.19%   | -0.86%             | -9.43%  |    -0.89 |       64 | 39.93%     | ok               |
|          25 | -6.89%   | -0.86%             | -10.55% |    -1.03 |       67 | 37.94%     | ok               |
|          30 | -7.01%   | -0.86%             | -9.98%  |    -1.11 |       67 | 34.61%     | ok               |
|          15 | -8.46%   | -0.86%             | -11.30% |    -1.2  |       76 | 42.76%     | ok               |
|          45 | -7.56%   | -0.86%             | -9.57%  |    -1.43 |       54 | 24.13%     | ok               |

## BONK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 166.73%  | -78.84%            | -35.57% |     1.22 |       50 | 22.61%     | ok               |
|          25 | 146.68%  | -78.84%            | -54.47% |     0.97 |       67 | 49.04%     | ok               |
|          15 | 134.59%  | -78.84%            | -62.48% |     0.91 |       72 | 57.66%     | ok               |
|          20 | 115.61%  | -78.84%            | -61.03% |     0.87 |       67 | 53.26%     | ok               |
|          40 | 78.19%   | -78.84%            | -53.34% |     0.77 |       56 | 35.25%     | ok               |

## BTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 56.10%   | -25.31%            | -14.50% |     1    |       44 | 33.91%     | ok               |
|          45 | 41.96%   | -25.31%            | -13.36% |     0.82 |       42 | 30.46%     | ok               |
|          35 | 39.83%   | -25.31%            | -21.56% |     0.75 |       68 | 40.80%     | ok               |
|          30 | 23.04%   | -25.31%            | -21.75% |     0.49 |       72 | 47.51%     | ok               |
|          50 | 14.00%   | -25.31%            | -18.05% |     0.4  |       42 | 25.29%     | ok               |

## C Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -6.65%   | 130.31%            | -22.28% |    -0.11 |       64 | 35.77%     | ok               |
|          45 | -18.87%  | 130.31%            | -30.30% |    -0.44 |       76 | 39.93%     | ok               |
|          25 | -27.33%  | 130.31%            | -34.97% |    -0.51 |       71 | 52.58%     | ok               |
|          20 | -29.76%  | 130.31%            | -36.33% |    -0.56 |       79 | 55.57%     | ok               |
|          40 | -24.56%  | 130.31%            | -35.18% |    -0.57 |       76 | 42.26%     | ok               |

## CAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 16.31%   | 140.22%            | -21.02% |     0.37 |       72 | 54.08%     | ok               |
|          25 | 16.42%   | 140.22%            | -26.37% |     0.37 |       68 | 56.91%     | ok               |
|          15 | 12.90%   | 140.22%            | -30.60% |     0.32 |       75 | 67.55%     | ok               |
|          45 | 11.56%   | 140.22%            | -27.12% |     0.31 |       56 | 42.76%     | ok               |
|          20 | 11.07%   | 140.22%            | -25.65% |     0.3  |       80 | 60.57%     | ok               |

## CL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 5.84%    | 3.67%              | -12.98% |     0.28 |       44 | 28.12%     | ok               |
|          30 | 5.38%    | 3.67%              | -14.32% |     0.24 |       62 | 44.09%     | ok               |
|          45 | 1.00%    | 3.67%              | -13.51% |     0.09 |       48 | 31.11%     | ok               |
|          35 | 0.36%    | 3.67%              | -13.83% |     0.07 |       64 | 40.43%     | ok               |
|          40 | -2.55%   | 3.67%              | -12.70% |    -0.04 |       58 | 35.11%     | ok               |

## CMCSA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -43.10%  | -39.96%            | -45.87% |    -1    |       89 | 56.57%     | ok               |
|          30 | -45.38%  | -39.96%            | -48.04% |    -1.23 |       80 | 42.10%     | ok               |
|          50 | -30.84%  | -39.96%            | -32.53% |    -1.23 |       48 | 14.14%     | ok               |
|          25 | -47.66%  | -39.96%            | -50.21% |    -1.29 |       87 | 47.25%     | ok               |
|          35 | -45.52%  | -39.96%            | -47.87% |    -1.33 |       93 | 36.44%     | ok               |

## COMP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -6.30%   | -67.76%            | -38.71% |     0.11 |       48 | 20.88%     | ok               |
|          30 | -43.71%  | -67.76%            | -57.10% |    -0.32 |       93 | 46.36%     | ok               |
|          25 | -47.19%  | -67.76%            | -60.58% |    -0.35 |       93 | 53.83%     | ok               |
|          15 | -54.07%  | -67.76%            | -65.55% |    -0.42 |      105 | 64.75%     | ok               |
|          40 | -47.97%  | -67.76%            | -53.06% |    -0.51 |       74 | 34.29%     | ok               |

## COP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.61%   | 6.62%              | -35.08% |     0.08 |       48 | 29.45%     | ok               |
|          35 | -13.64%  | 6.62%              | -43.58% |    -0.18 |       73 | 40.27%     | ok               |
|          45 | -12.05%  | 6.62%              | -41.35% |    -0.19 |       62 | 32.95%     | ok               |
|          30 | -18.12%  | 6.62%              | -43.77% |    -0.28 |       72 | 43.76%     | ok               |
|          40 | -17.60%  | 6.62%              | -47.05% |    -0.31 |       68 | 36.11%     | ok               |

## COST Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 10.40%   | 31.19%             | -24.32% |     0.37 |       66 | 48.42%     | ok               |
|          25 | 8.77%    | 31.19%             | -24.73% |     0.33 |       63 | 45.59%     | ok               |
|          35 | 4.79%    | 31.19%             | -26.58% |     0.22 |       54 | 38.77%     | ok               |
|          30 | -1.10%   | 31.19%             | -29.73% |     0.03 |       62 | 41.93%     | ok               |
|          40 | -1.58%   | 31.19%             | -28.41% |     0    |       54 | 35.77%     | ok               |

## CRM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -35.79%  | -39.72%            | -44.67% |    -0.57 |       90 | 54.91%     | ok               |
|          35 | -29.63%  | -39.72%            | -33.08% |    -0.59 |       60 | 37.94%     | ok               |
|          40 | -34.83%  | -39.72%            | -39.11% |    -0.8  |       66 | 33.94%     | ok               |
|          20 | -43.35%  | -39.72%            | -45.69% |    -0.82 |       74 | 48.59%     | ok               |
|          30 | -39.56%  | -39.72%            | -41.36% |    -0.83 |       63 | 42.76%     | ok               |

## CRV-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 27.72%   | -55.44%            | -37.78% |     0.48 |       70 | 31.80%     | ok               |
|          45 | 12.07%   | -55.44%            | -42.29% |     0.33 |       56 | 21.07%     | ok               |
|          50 | 7.86%    | -55.44%            | -29.30% |     0.28 |       46 | 17.43%     | ok               |
|          40 | 5.82%    | -55.44%            | -38.86% |     0.27 |       60 | 27.39%     | ok               |
|          30 | -0.17%   | -55.44%            | -39.89% |     0.23 |       70 | 36.59%     | ok               |

## CSCO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 35.16%   | 134.32%            | -19.34% |     0.75 |       48 | 36.61%     | ok               |
|          45 | 30.59%   | 134.32%            | -19.34% |     0.66 |       49 | 38.27%     | ok               |
|          35 | 25.61%   | 134.32%            | -23.68% |     0.55 |       51 | 45.09%     | ok               |
|          25 | 24.55%   | 134.32%            | -23.28% |     0.53 |       61 | 49.58%     | ok               |
|          30 | 23.34%   | 134.32%            | -21.79% |     0.51 |       59 | 47.75%     | ok               |

## CVX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -3.89%   | 31.33%             | -27.34% |    -0.04 |       75 | 35.44%     | ok               |
|          25 | -5.50%   | 31.33%             | -24.33% |    -0.06 |       73 | 43.26%     | ok               |
|          45 | -4.80%   | 31.33%             | -28.83% |    -0.08 |       65 | 31.95%     | ok               |
|          35 | -5.43%   | 31.33%             | -28.85% |    -0.08 |       67 | 37.77%     | ok               |
|          50 | -5.95%   | 31.33%             | -30.69% |    -0.15 |       56 | 27.45%     | ok               |

## DASH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 97.90%   | 20.03%             | -27.84% |     0.84 |       40 | 15.52%     | ok               |
|          40 | 58.79%   | 20.03%             | -31.16% |     0.64 |       46 | 22.22%     | ok               |
|          45 | 42.68%   | 20.03%             | -36.57% |     0.55 |       44 | 17.62%     | ok               |
|          35 | -38.65%  | 20.03%             | -63.23% |     0.01 |       69 | 26.63%     | ok               |
|          30 | -41.80%  | 20.03%             | -64.43% |    -0.02 |       63 | 29.50%     | ok               |

## DBC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -4.99%   | 32.84%             | -27.07% |    -0.1  |       74 | 40.77%     | ok               |
|          25 | -8.04%   | 32.84%             | -26.10% |    -0.22 |       64 | 37.10%     | ok               |
|          50 | -6.86%   | 32.84%             | -20.31% |    -0.23 |       44 | 23.29%     | ok               |
|          20 | -8.59%   | 32.84%             | -26.24% |    -0.24 |       67 | 38.94%     | ok               |
|          45 | -9.43%   | 32.84%             | -21.46% |    -0.31 |       60 | 26.96%     | ok               |

## DE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -2.76%   | 58.43%             | -21.46% |     0.01 |       66 | 31.11%     | ok               |
|          20 | -4.78%   | 58.43%             | -29.90% |    -0    |       74 | 51.25%     | ok               |
|          30 | -5.05%   | 58.43%             | -24.56% |    -0.01 |       70 | 45.42%     | ok               |
|          45 | -4.75%   | 58.43%             | -25.20% |    -0.03 |       66 | 35.61%     | ok               |
|          25 | -8.40%   | 58.43%             | -28.64% |    -0.08 |       76 | 48.25%     | ok               |

## DIA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -2.43%   | 35.14%             | -11.28% |    -0.09 |       60 | 44.76%     | ok               |
|          35 | -2.88%   | 35.14%             | -13.15% |    -0.12 |       62 | 41.60%     | ok               |
|          30 | -3.93%   | 35.14%             | -12.94% |    -0.18 |       60 | 43.59%     | ok               |
|          20 | -5.84%   | 35.14%             | -13.85% |    -0.27 |       66 | 47.25%     | ok               |
|          40 | -6.84%   | 35.14%             | -15.06% |    -0.37 |       68 | 38.77%     | ok               |

## DIS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 15.47%   | -12.81%            | -16.40% |     0.51 |       48 | 26.12%     | ok               |
|          40 | -8.86%   | -12.81%            | -24.07% |    -0.12 |       63 | 34.94%     | ok               |
|          45 | -10.23%  | -12.81%            | -18.50% |    -0.18 |       49 | 29.95%     | ok               |
|          15 | -15.62%  | -12.81%            | -31.15% |    -0.21 |       89 | 55.74%     | ok               |
|          35 | -15.89%  | -12.81%            | -25.70% |    -0.28 |       75 | 41.10%     | ok               |

## DOGE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -10.68%  | -65.35%            | -59.36% |     0.19 |       78 | 64.56%     | ok               |
|          25 | -13.89%  | -65.35%            | -55.33% |     0.13 |       69 | 54.60%     | ok               |
|          20 | -16.70%  | -65.35%            | -57.37% |     0.11 |       81 | 59.77%     | ok               |
|          30 | -27.95%  | -65.35%            | -62.31% |    -0.05 |       72 | 49.04%     | ok               |
|          35 | -49.30%  | -65.35%            | -61.79% |    -0.46 |       68 | 42.72%     | ok               |

## DOT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -38.95%  | -83.24%            | -50.02% |    -0.54 |       58 | 26.05%     | ok               |
|          45 | -41.62%  | -83.24%            | -53.12% |    -0.54 |       50 | 31.23%     | ok               |
|          35 | -57.95%  | -83.24%            | -63.08% |    -0.63 |       78 | 41.57%     | ok               |
|          15 | -66.17%  | -83.24%            | -73.29% |    -0.64 |       83 | 63.03%     | ok               |
|          20 | -63.64%  | -83.24%            | -68.03% |    -0.67 |       91 | 59.39%     | ok               |

## DXY-INDEX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -1.69%   | -1.42%             | -6.29%  |    -0.25 |       42 | 32.68%     | ok               |
|          15 | -3.50%   | -1.42%             | -11.37% |    -0.3  |       82 | 76.41%     | ok               |
|          40 | -4.66%   | -1.42%             | -8.24%  |    -0.59 |       68 | 50.43%     | ok               |
|          25 | -6.28%   | -1.42%             | -12.10% |    -0.68 |       78 | 66.45%     | ok               |
|          35 | -5.86%   | -1.42%             | -10.39% |    -0.72 |       71 | 56.49%     | ok               |

## EEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -4.53%   | 57.01%             | -15.88% |    -0.11 |       50 | 33.94%     | ok               |
|          45 | -6.21%   | 57.01%             | -17.36% |    -0.17 |       52 | 35.44%     | ok               |
|          40 | -6.55%   | 57.01%             | -19.52% |    -0.17 |       64 | 37.60%     | ok               |
|          35 | -7.20%   | 57.01%             | -23.88% |    -0.18 |       66 | 39.60%     | ok               |
|          25 | -10.02%  | 57.01%             | -25.60% |    -0.27 |       65 | 42.60%     | ok               |

## EFA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -5.32%   | 33.22%             | -10.80% |    -0.13 |       62 | 50.75%     | ok               |
|          30 | -10.31%  | 33.22%             | -13.72% |    -0.4  |       60 | 42.43%     | ok               |
|          20 | -11.88%  | 33.22%             | -12.73% |    -0.43 |       69 | 47.75%     | ok               |
|          40 | -11.67%  | 33.22%             | -15.58% |    -0.5  |       64 | 38.60%     | ok               |
|          50 | -11.19%  | 33.22%             | -17.56% |    -0.52 |       54 | 34.61%     | ok               |

## EOG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -12.14%  | 25.24%             | -39.69% |    -0.22 |       58 | 35.11%     | ok               |
|          30 | -17.23%  | 25.24%             | -48.13% |    -0.3  |       81 | 48.92%     | ok               |
|          40 | -17.34%  | 25.24%             | -43.26% |    -0.35 |       66 | 38.44%     | ok               |
|          35 | -18.15%  | 25.24%             | -46.26% |    -0.36 |       79 | 43.59%     | ok               |
|          25 | -21.44%  | 25.24%             | -51.99% |    -0.39 |       82 | 51.91%     | ok               |

## ETC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -2.84%   | -66.46%            | -31.28% |     0.08 |       26 | 15.90%     | ok               |
|          45 | -12.62%  | -66.46%            | -38.47% |    -0.1  |       26 | 17.62%     | ok               |
|          35 | -15.58%  | -66.46%            | -45.32% |    -0.12 |       44 | 25.29%     | ok               |
|          40 | -19.39%  | -66.46%            | -43.28% |    -0.23 |       40 | 21.26%     | ok               |
|          30 | -31.66%  | -66.46%            | -48.09% |    -0.43 |       62 | 28.93%     | ok               |

## ETH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 141.28%  | -16.87%            | -30.11% |     1.2  |       62 | 46.17%     | ok               |
|          30 | 96.21%   | -16.87%            | -32.89% |     0.94 |       68 | 54.79%     | ok               |
|          20 | 53.72%   | -16.87%            | -39.10% |     0.67 |       80 | 63.79%     | ok               |
|          25 | 52.59%   | -16.87%            | -40.90% |     0.67 |       64 | 59.58%     | ok               |
|          15 | 46.52%   | -16.87%            | -42.74% |     0.62 |       75 | 69.35%     | ok               |

## EWJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -22.06%  | 29.80%             | -30.73% |    -0.76 |       62 | 37.10%     | ok               |
|          20 | -23.38%  | 29.80%             | -31.32% |    -0.79 |       58 | 39.10%     | ok               |
|          25 | -25.59%  | 29.80%             | -31.18% |    -0.89 |       58 | 38.10%     | ok               |
|          45 | -22.81%  | 29.80%             | -27.68% |    -0.91 |       58 | 29.28%     | ok               |
|          35 | -25.79%  | 29.80%             | -32.54% |    -0.93 |       68 | 35.44%     | ok               |

## FCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -6.01%   | 57.16%             | -27.70% |     0.03 |       56 | 30.45%     | ok               |
|          45 | -10.07%  | 57.16%             | -35.18% |    -0.03 |       56 | 34.94%     | ok               |
|          40 | -21.91%  | 57.16%             | -44.37% |    -0.23 |       68 | 39.10%     | ok               |
|          30 | -29.92%  | 57.16%             | -48.22% |    -0.35 |       67 | 45.92%     | ok               |
|          35 | -34.24%  | 57.16%             | -51.41% |    -0.46 |       73 | 44.09%     | ok               |

## FET-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -17.78%  | -78.63%            | -61.20% |     0.16 |       92 | 52.68%     | ok               |
|          15 | -27.68%  | -78.63%            | -59.58% |     0.08 |       86 | 56.70%     | ok               |
|          25 | -40.18%  | -78.63%            | -60.10% |    -0.13 |       89 | 46.36%     | ok               |
|          30 | -47.71%  | -78.63%            | -52.82% |    -0.28 |       87 | 41.76%     | ok               |
|          45 | -44.89%  | -78.63%            | -48.61% |    -0.53 |       54 | 18.77%     | ok               |

## FIL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -21.24%  | -77.93%            | -34.38% |    -0.16 |       44 | 23.37%     | ok               |
|          35 | -44.50%  | -77.93%            | -44.50% |    -0.57 |       58 | 28.16%     | ok               |
|          45 | -39.54%  | -77.93%            | -42.42% |    -0.59 |       42 | 17.62%     | ok               |
|          30 | -50.07%  | -77.93%            | -51.27% |    -0.65 |       70 | 34.48%     | ok               |
|          15 | -62.47%  | -77.93%            | -63.49% |    -0.76 |       89 | 45.98%     | ok               |

## FXI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -0.40%   | 55.52%             | -22.57% |     0.08 |       46 | 31.95%     | ok               |
|          30 | -0.68%   | 55.52%             | -23.91% |     0.07 |       44 | 30.45%     | ok               |
|          15 | -2.01%   | 55.52%             | -21.68% |     0.04 |       50 | 35.61%     | ok               |
|          20 | -2.59%   | 55.52%             | -24.53% |     0.02 |       48 | 33.44%     | ok               |
|          35 | -5.12%   | 55.52%             | -27.53% |    -0.05 |       44 | 28.45%     | ok               |

## GDX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 13.64%   | 150.00%            | -35.59% |     0.33 |       72 | 51.41%     | ok               |
|          40 | 11.03%   | 150.00%            | -31.87% |     0.3  |       62 | 41.93%     | ok               |
|          30 | 8.52%    | 150.00%            | -34.99% |     0.26 |       58 | 47.09%     | ok               |
|          35 | 6.25%    | 150.00%            | -32.37% |     0.23 |       66 | 44.26%     | ok               |
|          25 | 2.77%    | 150.00%            | -38.90% |     0.18 |       62 | 48.25%     | ok               |

## GDXJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -11.84%  | 165.49%            | -45.05% |     0    |       66 | 51.25%     | ok               |
|          50 | -19.89%  | 165.49%            | -44.94% |    -0.22 |       58 | 37.60%     | ok               |
|          30 | -23.69%  | 165.49%            | -44.93% |    -0.23 |       64 | 45.26%     | ok               |
|          25 | -28.79%  | 165.49%            | -47.26% |    -0.3  |       69 | 48.09%     | ok               |
|          35 | -27.30%  | 165.49%            | -43.49% |    -0.31 |       66 | 42.93%     | ok               |

## GE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 17.48%   | 168.62%            | -22.29% |     0.42 |       66 | 37.94%     | ok               |
|          45 | 8.62%    | 168.62%            | -25.68% |     0.27 |       74 | 40.77%     | ok               |
|          20 | -0.29%   | 168.62%            | -26.63% |     0.12 |       73 | 55.41%     | ok               |
|          30 | -1.94%   | 168.62%            | -27.82% |     0.09 |       78 | 51.41%     | ok               |
|          35 | -1.71%   | 168.62%            | -27.11% |     0.09 |       82 | 46.26%     | ok               |

## GLD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 28.53%   | 84.27%             | -14.61% |     0.69 |       48 | 50.42%     | ok               |
|          25 | 27.86%   | 84.27%             | -14.61% |     0.68 |       48 | 48.92%     | ok               |
|          30 | 21.77%   | 84.27%             | -16.63% |     0.57 |       50 | 47.75%     | ok               |
|          15 | 20.66%   | 84.27%             | -17.54% |     0.52 |       50 | 54.58%     | ok               |
|          35 | 15.44%   | 84.27%             | -17.29% |     0.44 |       54 | 45.76%     | ok               |

## GOOGL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 83.32%   | 163.00%            | -18.25% |     1.25 |       57 | 48.75%     | ok               |
|          30 | 78.89%   | 163.00%            | -20.41% |     1.18 |       55 | 52.25%     | ok               |
|          45 | 67.79%   | 163.00%            | -14.13% |     1.15 |       52 | 42.10%     | ok               |
|          25 | 76.17%   | 163.00%            | -19.76% |     1.14 |       53 | 54.24%     | ok               |
|          50 | 60.60%   | 163.00%            | -14.89% |     1.09 |       48 | 37.27%     | ok               |

## GRT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 15.16%   | -88.04%            | -49.67% |     0.39 |       71 | 61.69%     | ok               |
|          50 | 14.84%   | -88.04%            | -36.42% |     0.37 |       44 | 21.65%     | ok               |
|          20 | 9.12%    | -88.04%            | -46.47% |     0.33 |       77 | 56.90%     | ok               |
|          30 | 2.87%    | -88.04%            | -50.20% |     0.25 |       83 | 43.87%     | ok               |
|          35 | 1.72%    | -88.04%            | -43.61% |     0.22 |       66 | 37.55%     | ok               |

## GS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 23.05%   | 163.15%            | -20.56% |     0.5  |       74 | 59.90%     | ok               |
|          20 | 6.27%    | 163.15%            | -23.19% |     0.23 |       74 | 55.91%     | ok               |
|          40 | 1.75%    | 163.15%            | -17.88% |     0.13 |       70 | 44.09%     | ok               |
|          25 | 0.89%    | 163.15%            | -23.32% |     0.12 |       74 | 53.41%     | ok               |
|          30 | -0.82%   | 163.15%            | -22.13% |     0.08 |       76 | 50.92%     | ok               |

## HD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -7.53%   | -11.09%            | -18.58% |    -0.12 |       73 | 44.09%     | ok               |
|          25 | -8.25%   | -11.09%            | -19.40% |    -0.14 |       72 | 46.09%     | ok               |
|          45 | -11.40%  | -11.09%            | -20.74% |    -0.33 |       60 | 28.29%     | ok               |
|          15 | -16.54%  | -11.09%            | -27.26% |    -0.34 |      109 | 55.07%     | ok               |
|          35 | -15.13%  | -11.09%            | -23.81% |    -0.38 |       82 | 39.93%     | ok               |

## HON Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -12.97%  | 22.48%             | -21.17% |    -0.38 |       72 | 31.95%     | ok               |
|          45 | -14.71%  | 22.48%             | -19.99% |    -0.41 |       74 | 36.94%     | ok               |
|          40 | -23.11%  | 22.48%             | -26.92% |    -0.65 |       76 | 41.26%     | ok               |
|          35 | -24.58%  | 22.48%             | -27.99% |    -0.67 |       91 | 47.59%     | ok               |
|          30 | -27.63%  | 22.48%             | -29.81% |    -0.75 |       95 | 52.41%     | ok               |

## HYG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -8.22%   | 2.69%              | -8.22%  |    -0.99 |       70 | 29.45%     | ok               |
|          15 | -9.79%   | 2.69%              | -10.64% |    -1.06 |       90 | 41.26%     | ok               |
|          20 | -9.53%   | 2.69%              | -10.64% |    -1.07 |       88 | 39.10%     | ok               |
|          25 | -9.68%   | 2.69%              | -10.41% |    -1.09 |       85 | 36.94%     | ok               |
|          30 | -9.38%   | 2.69%              | -9.89%  |    -1.1  |       83 | 34.28%     | ok               |

## IBIT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 53.73%   | -6.24%             | -17.37% |     1.05 |       22 | 21.77%     | ok               |
|          15 | 56.91%   | -6.24%             | -19.20% |     0.94 |       40 | 38.78%     | ok               |
|          45 | 44.27%   | -6.24%             | -17.37% |     0.89 |       26 | 23.13%     | ok               |
|          40 | 38.04%   | -6.24%             | -17.78% |     0.79 |       26 | 24.94%     | ok               |
|          30 | 30.82%   | -6.24%             | -18.95% |     0.66 |       34 | 31.29%     | ok               |

## IBM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -17.10%  | 14.14%             | -45.75% |    -0.11 |       91 | 62.90%     | ok               |
|          30 | -24.56%  | 14.14%             | -47.10% |    -0.29 |       75 | 50.75%     | ok               |
|          35 | -24.70%  | 14.14%             | -47.10% |    -0.3  |       69 | 46.59%     | ok               |
|          20 | -27.88%  | 14.14%             | -50.22% |    -0.32 |       73 | 55.41%     | ok               |
|          45 | -30.11%  | 14.14%             | -48.72% |    -0.44 |       56 | 37.27%     | ok               |

## ICP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 0.63%    | -68.46%            | -32.85% |     0.2  |       52 | 23.95%     | ok               |
|          35 | -7.43%   | -68.46%            | -39.11% |     0.12 |       62 | 29.12%     | ok               |
|          30 | -20.89%  | -68.46%            | -52.30% |     0.04 |       77 | 34.67%     | ok               |
|          50 | -18.44%  | -68.46%            | -43.65% |    -0.1  |       34 | 14.37%     | ok               |
|          45 | -24.91%  | -68.46%            | -40.57% |    -0.19 |       54 | 18.20%     | ok               |

## IEF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -7.17%   | -2.39%             | -10.10% |    -0.85 |       72 | 43.26%     | ok               |
|          15 | -7.72%   | -2.39%             | -10.83% |    -0.9  |       71 | 44.76%     | ok               |
|          25 | -10.74%  | -2.39%             | -11.63% |    -1.36 |       78 | 40.43%     | ok               |
|          45 | -8.43%   | -2.39%             | -9.73%  |    -1.38 |       56 | 23.63%     | ok               |
|          40 | -9.03%   | -2.39%             | -9.67%  |    -1.4  |       66 | 25.79%     | ok               |

## IEMG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -2.76%   | 51.17%             | -13.91% |    -0.05 |       52 | 31.78%     | ok               |
|          45 | -3.56%   | 51.17%             | -14.92% |    -0.08 |       48 | 34.28%     | ok               |
|          35 | -4.42%   | 51.17%             | -22.13% |    -0.09 |       63 | 39.77%     | ok               |
|          40 | -5.05%   | 51.17%             | -18.43% |    -0.13 |       60 | 37.27%     | ok               |
|          25 | -8.63%   | 51.17%             | -25.58% |    -0.24 |       59 | 42.60%     | ok               |

## INJ-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -10.15%  | -62.42%            | -52.34% |     0.06 |       44 | 23.37%     | ok               |
|          35 | -21.17%  | -62.42%            | -59.17% |    -0.02 |       60 | 32.57%     | ok               |
|          40 | -26.45%  | -62.42%            | -55.86% |    -0.14 |       50 | 29.12%     | ok               |
|          50 | -22.38%  | -62.42%            | -49.35% |    -0.14 |       48 | 20.11%     | ok               |
|          20 | -55.65%  | -62.42%            | -81.16% |    -0.45 |       78 | 46.74%     | ok               |

## INTC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 110.34%  | 105.00%            | -53.65% |     0.84 |       77 | 60.23%     | ok               |
|          45 | 83.34%   | 105.00%            | -49.32% |     0.78 |       56 | 33.78%     | ok               |
|          40 | 77.32%   | 105.00%            | -55.86% |     0.74 |       64 | 38.10%     | ok               |
|          50 | 70.40%   | 105.00%            | -48.35% |     0.72 |       64 | 29.95%     | ok               |
|          25 | 68.65%   | 105.00%            | -56.41% |     0.68 |       77 | 51.25%     | ok               |

## INTU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 0.68%    | -51.50%            | -40.16% |     0.13 |       69 | 27.45%     | ok               |
|          45 | -1.28%   | -51.50%            | -41.19% |     0.1  |       67 | 31.45%     | ok               |
|          40 | -8.34%   | -51.50%            | -44.97% |    -0.03 |       69 | 34.78%     | ok               |
|          35 | -15.62%  | -51.50%            | -46.75% |    -0.16 |       71 | 38.44%     | ok               |
|          25 | -18.36%  | -51.50%            | -39.87% |    -0.2  |       70 | 44.43%     | ok               |

## ITA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -1.69%   | 85.52%             | -21.48% |     0.01 |       76 | 36.61%     | ok               |
|          15 | -5.24%   | 85.52%             | -25.76% |    -0.05 |       87 | 58.90%     | ok               |
|          30 | -5.10%   | 85.52%             | -23.75% |    -0.07 |       72 | 46.59%     | ok               |
|          35 | -7.12%   | 85.52%             | -23.16% |    -0.14 |       76 | 44.93%     | ok               |
|          40 | -8.19%   | 85.52%             | -20.58% |    -0.19 |       78 | 41.43%     | ok               |

## IWM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 9.83%    | 40.79%             | -13.30% |     0.4  |       50 | 36.77%     | ok               |
|          40 | 8.60%    | 40.79%             | -14.08% |     0.39 |       42 | 31.28%     | ok               |
|          30 | 9.40%    | 40.79%             | -12.83% |     0.39 |       48 | 35.77%     | ok               |
|          35 | 8.35%    | 40.79%             | -14.11% |     0.36 |       48 | 33.61%     | ok               |
|          20 | 5.50%    | 40.79%             | -13.83% |     0.25 |       60 | 37.77%     | ok               |

## JNJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 19.99%   | 60.70%             | -10.57% |     0.81 |       54 | 37.10%     | ok               |
|          15 | 17.55%   | 60.70%             | -18.02% |     0.58 |       66 | 57.57%     | ok               |
|          45 | 11.43%   | 60.70%             | -13.35% |     0.48 |       54 | 41.93%     | ok               |
|          20 | 12.12%   | 60.70%             | -17.61% |     0.44 |       72 | 54.08%     | ok               |
|          30 | 6.86%    | 60.70%             | -17.51% |     0.29 |       70 | 50.75%     | ok               |

## JPM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 11.04%   | 86.90%             | -15.90% |     0.41 |       54 | 38.94%     | ok               |
|          45 | 0.49%    | 86.90%             | -21.91% |     0.09 |       56 | 41.93%     | ok               |
|          20 | -16.11%  | 86.90%             | -33.59% |    -0.28 |       86 | 56.91%     | ok               |
|          40 | -13.30%  | 86.90%             | -28.47% |    -0.32 |       68 | 44.59%     | ok               |
|          35 | -18.42%  | 86.90%             | -27.43% |    -0.46 |       76 | 48.59%     | ok               |

## KO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 23.75%   | 47.16%             | -8.20%  |     0.85 |       51 | 37.94%     | ok               |
|          35 | 19.96%   | 47.16%             | -8.07%  |     0.75 |       54 | 36.61%     | ok               |
|          40 | 17.46%   | 47.16%             | -9.28%  |     0.71 |       56 | 33.44%     | ok               |
|          25 | 18.64%   | 47.16%             | -9.73%  |     0.69 |       57 | 40.60%     | ok               |
|          50 | 10.20%   | 47.16%             | -12.31% |     0.48 |       38 | 26.96%     | ok               |

## LDO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 55.72%   | -74.49%            | -48.17% |     0.65 |       82 | 57.09%     | ok               |
|          50 | 33.03%   | -74.49%            | -48.04% |     0.57 |       52 | 18.20%     | ok               |
|          35 | 34.90%   | -74.49%            | -61.98% |     0.54 |       78 | 36.02%     | ok               |
|          20 | 34.18%   | -74.49%            | -45.55% |     0.54 |       82 | 51.92%     | ok               |
|          30 | 34.87%   | -74.49%            | -61.16% |     0.54 |       78 | 43.10%     | ok               |

## LIN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -3.99%   | 3.42%              | -23.70% |    -0.07 |       63 | 47.92%     | ok               |
|          25 | -4.23%   | 3.42%              | -22.01% |    -0.09 |       63 | 40.10%     | ok               |
|          20 | -6.28%   | 3.42%              | -23.00% |    -0.16 |       62 | 43.26%     | ok               |
|          35 | -7.68%   | 3.42%              | -21.18% |    -0.25 |       62 | 30.78%     | ok               |
|          30 | -8.27%   | 3.42%              | -21.53% |    -0.25 |       66 | 37.27%     | ok               |

## LINK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -17.43%  | -44.12%            | -49.94% |     0.06 |       73 | 43.87%     | ok               |
|          45 | -14.65%  | -44.12%            | -38.11% |     0.03 |       50 | 28.74%     | ok               |
|          50 | -18.83%  | -44.12%            | -36.52% |    -0.05 |       44 | 22.80%     | ok               |
|          35 | -26.71%  | -44.12%            | -49.77% |    -0.08 |       61 | 38.70%     | ok               |
|          40 | -30.73%  | -44.12%            | -51.13% |    -0.17 |       57 | 32.95%     | ok               |

## LLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 6.14%    | 50.74%             | -38.23% |     0.23 |       44 | 34.94%     | ok               |
|          15 | -3.35%   | 50.74%             | -48.12% |     0.09 |       63 | 58.40%     | ok               |
|          45 | -5.81%   | 50.74%             | -42.66% |     0    |       52 | 38.44%     | ok               |
|          20 | -18.92%  | 50.74%             | -51.34% |    -0.19 |       72 | 53.41%     | ok               |
|          25 | -20.26%  | 50.74%             | -53.47% |    -0.23 |       68 | 50.75%     | ok               |

## LRCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -18.21%  | 206.30%            | -48.71% |    -0.09 |       80 | 33.94%     | ok               |
|          35 | -21.16%  | 206.30%            | -57.54% |    -0.09 |       80 | 41.76%     | ok               |
|          40 | -21.38%  | 206.30%            | -55.33% |    -0.11 |       74 | 39.77%     | ok               |
|          15 | -26.89%  | 206.30%            | -58.63% |    -0.12 |       85 | 52.75%     | ok               |
|          30 | -24.73%  | 206.30%            | -60.21% |    -0.15 |       82 | 42.60%     | ok               |

## LTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -5.83%   | -65.24%            | -35.63% |     0.08 |       54 | 31.80%     | ok               |
|          35 | -20.52%  | -65.24%            | -46.80% |    -0.11 |       68 | 42.91%     | ok               |
|          30 | -30.38%  | -65.24%            | -47.04% |    -0.24 |       72 | 49.81%     | ok               |
|          40 | -29.68%  | -65.24%            | -48.26% |    -0.29 |       60 | 38.12%     | ok               |
|          25 | -33.69%  | -65.24%            | -47.60% |    -0.29 |       76 | 52.68%     | ok               |

## MCD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 3.90%    | -7.49%             | -9.22%  |     0.24 |       42 | 20.63%     | ok               |
|          30 | -3.77%   | -7.49%             | -18.81% |    -0.1  |       77 | 38.27%     | ok               |
|          25 | -4.80%   | -7.49%             | -20.47% |    -0.13 |       77 | 40.93%     | ok               |
|          40 | -6.63%   | -7.49%             | -16.86% |    -0.26 |       69 | 28.95%     | ok               |
|          35 | -8.84%   | -7.49%             | -15.45% |    -0.34 |       69 | 34.61%     | ok               |

## META Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -15.97%  | 10.03%             | -33.45% |    -0.23 |       70 | 36.61%     | ok               |
|          40 | -24.17%  | 10.03%             | -37.90% |    -0.4  |       70 | 39.93%     | ok               |
|          25 | -31.65%  | 10.03%             | -42.95% |    -0.52 |       71 | 50.58%     | ok               |
|          50 | -28.80%  | 10.03%             | -36.07% |    -0.58 |       74 | 32.78%     | ok               |
|          30 | -33.48%  | 10.03%             | -42.12% |    -0.59 |       76 | 47.42%     | ok               |

## MPC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 27.43%   | 76.26%             | -23.96% |     0.58 |       48 | 38.27%     | ok               |
|          45 | 19.35%   | 76.26%             | -25.09% |     0.45 |       54 | 41.93%     | ok               |
|          40 | 14.84%   | 76.26%             | -25.70% |     0.37 |       56 | 44.09%     | ok               |
|          35 | 11.29%   | 76.26%             | -35.90% |     0.31 |       64 | 46.59%     | ok               |
|          30 | -6.22%   | 76.26%             | -44.76% |     0.01 |       67 | 49.42%     | ok               |

## MRK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -17.49%  | 5.43%              | -29.92% |    -0.29 |       87 | 54.08%     | ok               |
|          25 | -16.47%  | 5.43%              | -31.07% |    -0.3  |       72 | 46.26%     | ok               |
|          20 | -20.57%  | 5.43%              | -29.39% |    -0.4  |       77 | 49.58%     | ok               |
|          50 | -21.52%  | 5.43%              | -27.68% |    -0.6  |       58 | 29.12%     | ok               |
|          45 | -23.47%  | 5.43%              | -27.72% |    -0.62 |       59 | 32.45%     | ok               |

## MS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -3.32%   | 141.75%            | -19.99% |     0    |       72 | 41.43%     | ok               |
|          15 | -4.98%   | 141.75%            | -22.02% |    -0.01 |       73 | 58.24%     | ok               |
|          20 | -5.09%   | 141.75%            | -25.68% |    -0.02 |       77 | 54.41%     | ok               |
|          30 | -10.18%  | 141.75%            | -27.79% |    -0.16 |       77 | 49.58%     | ok               |
|          35 | -10.11%  | 141.75%            | -25.26% |    -0.17 |       78 | 46.09%     | ok               |

## MSFT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -20.82%  | 14.40%             | -24.64% |    -0.57 |       64 | 33.78%     | ok               |
|          50 | -22.75%  | 14.40%             | -25.48% |    -0.66 |       58 | 28.95%     | ok               |
|          35 | -33.78%  | 14.40%             | -35.38% |    -0.9  |       71 | 42.43%     | ok               |
|          40 | -33.30%  | 14.40%             | -34.92% |    -0.93 |       67 | 37.44%     | ok               |
|          30 | -37.64%  | 14.40%             | -39.15% |    -0.99 |       81 | 47.09%     | ok               |

## MU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 316.92%  | 743.10%            | -61.96% |     1.34 |       51 | 66.56%     | ok               |
|          40 | 256.21%  | 743.10%            | -64.26% |     1.33 |       56 | 53.41%     | ok               |
|          25 | 228.17%  | 743.10%            | -67.90% |     1.23 |       51 | 60.07%     | ok               |
|          30 | 215.18%  | 743.10%            | -68.76% |     1.21 |       51 | 58.40%     | ok               |
|          35 | 206.30%  | 743.10%            | -69.35% |     1.19 |       63 | 56.07%     | ok               |

## NEAR-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 58.08%   | -44.52%            | -49.73% |     0.73 |       40 | 22.22%     | ok               |
|          50 | 38.01%   | -44.52%            | -52.97% |     0.58 |       34 | 17.82%     | ok               |
|          40 | 32.81%   | -44.52%            | -57.80% |     0.53 |       42 | 26.25%     | ok               |
|          35 | 7.85%    | -44.52%            | -61.61% |     0.31 |       66 | 31.03%     | ok               |
|          30 | -11.63%  | -44.52%            | -59.54% |     0.13 |       83 | 40.42%     | ok               |

## NEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 16.36%   | 176.35%            | -29.41% |     0.36 |       60 | 60.90%     | ok               |
|          20 | 3.91%    | 176.35%            | -30.47% |     0.22 |       70 | 56.41%     | ok               |
|          25 | -9.17%   | 176.35%            | -37.89% |     0.04 |       66 | 54.41%     | ok               |
|          30 | -20.55%  | 176.35%            | -38.49% |    -0.15 |       70 | 52.75%     | ok               |
|          50 | -18.33%  | 176.35%            | -33.24% |    -0.17 |       56 | 39.93%     | ok               |

## NFLX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 40.34%   | 18.56%             | -13.37% |     0.88 |       50 | 44.76%     | ok               |
|          50 | 33.40%   | 18.56%             | -16.28% |     0.82 |       48 | 36.61%     | ok               |
|          35 | 36.35%   | 18.56%             | -18.30% |     0.78 |       66 | 48.75%     | ok               |
|          15 | 32.49%   | 18.56%             | -26.59% |     0.64 |       69 | 64.39%     | ok               |
|          25 | 28.11%   | 18.56%             | -21.09% |     0.62 |       70 | 55.91%     | ok               |

## NKE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -30.97%  | -57.94%            | -49.34% |    -0.37 |       87 | 51.41%     | ok               |
|          35 | -27.76%  | -57.94%            | -42.13% |    -0.39 |       73 | 37.44%     | ok               |
|          25 | -33.83%  | -57.94%            | -51.20% |    -0.43 |       87 | 48.75%     | ok               |
|          15 | -35.42%  | -57.94%            | -54.28% |    -0.45 |       90 | 55.24%     | ok               |
|          30 | -37.65%  | -57.94%            | -55.35% |    -0.53 |       87 | 43.93%     | ok               |

## NOW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 1.54%    | -26.60%            | -26.78% |     0.18 |       80 | 45.76%     | ok               |
|          20 | -0.50%   | -26.60%            | -34.71% |     0.17 |       79 | 52.08%     | ok               |
|          25 | -4.29%   | -26.60%            | -32.31% |     0.12 |       74 | 49.08%     | ok               |
|          15 | -9.19%   | -26.60%            | -38.33% |     0.06 |       89 | 55.24%     | ok               |
|          40 | -6.73%   | -26.60%            | -30.91% |     0.04 |       70 | 35.11%     | ok               |

## NVDA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -16.27%  | 117.87%            | -35.26% |    -0.1  |       76 | 47.95%     | ok               |
|          20 | -21.14%  | 117.87%            | -40.59% |    -0.13 |       72 | 55.97%     | ok               |
|          25 | -21.02%  | 117.87%            | -37.16% |    -0.15 |       73 | 50.98%     | ok               |
|          15 | -29.68%  | 117.87%            | -45.14% |    -0.24 |       73 | 59.18%     | ok               |
|          35 | -27.58%  | 117.87%            | -42.39% |    -0.32 |       84 | 45.10%     | ok               |

## OP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 21.31%   | -92.07%            | -36.11% |     0.44 |       32 | 11.30%     | ok               |
|          45 | 20.44%   | -92.07%            | -45.76% |     0.42 |       34 | 15.90%     | ok               |
|          40 | 9.34%    | -92.07%            | -53.61% |     0.31 |       46 | 24.14%     | ok               |
|          35 | -9.66%   | -92.07%            | -59.71% |     0.1  |       52 | 28.35%     | ok               |
|          30 | -13.59%  | -92.07%            | -71.26% |     0.09 |       66 | 34.87%     | ok               |

## ORCL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 244.42%  | 15.52%             | -29.32% |     1.36 |       66 | 66.56%     | ok               |
|          25 | 157.26%  | 15.52%             | -27.76% |     1.11 |       69 | 59.23%     | ok               |
|          20 | 153.93%  | 15.52%             | -29.32% |     1.09 |       69 | 62.23%     | ok               |
|          35 | 121.50%  | 15.52%             | -31.95% |     0.99 |       64 | 51.58%     | ok               |
|          45 | 110.15%  | 15.52%             | -32.35% |     0.97 |       60 | 42.76%     | ok               |

## OXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 9.24%    | -6.13%             | -31.06% |     0.27 |       71 | 45.59%     | ok               |
|          35 | 7.07%    | -6.13%             | -29.95% |     0.24 |       68 | 40.77%     | ok               |
|          50 | 5.87%    | -6.13%             | -29.57% |     0.22 |       40 | 29.28%     | ok               |
|          40 | 0.48%    | -6.13%             | -31.66% |     0.12 |       58 | 36.61%     | ok               |
|          25 | -4.09%   | -6.13%             | -39.47% |     0.06 |       77 | 49.92%     | ok               |

## PEP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 13.43%   | -14.41%            | -11.62% |     0.6  |       46 | 27.45%     | ok               |
|          45 | 6.37%    | -14.41%            | -14.22% |     0.31 |       64 | 31.95%     | ok               |
|          40 | 3.54%    | -14.41%            | -18.04% |     0.19 |       72 | 37.60%     | ok               |
|          35 | 2.77%    | -14.41%            | -21.42% |     0.15 |       77 | 42.43%     | ok               |
|          30 | -2.90%   | -14.41%            | -21.35% |    -0.02 |       77 | 48.75%     | ok               |

## PEPE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -5.04%   | -63.81%            | -57.66% |     0.24 |       83 | 46.17%     | ok               |
|          15 | -14.35%  | -63.81%            | -61.96% |     0.22 |       80 | 62.07%     | ok               |
|          25 | -14.59%  | -63.81%            | -53.88% |     0.15 |       89 | 51.72%     | ok               |
|          35 | -11.41%  | -63.81%            | -51.35% |     0.14 |       70 | 40.42%     | ok               |
|          20 | -22.78%  | -63.81%            | -61.13% |     0.1  |       86 | 58.62%     | ok               |

## PFE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -24.28%  | -8.12%             | -25.48% |    -0.88 |       52 | 19.80%     | ok               |
|          50 | -26.27%  | -8.12%             | -27.31% |    -1.07 |       42 | 15.81%     | ok               |
|          35 | -33.57%  | -8.12%             | -34.52% |    -1.09 |       86 | 32.61%     | ok               |
|          40 | -31.34%  | -8.12%             | -32.45% |    -1.1  |       74 | 24.79%     | ok               |
|          30 | -41.91%  | -8.12%             | -42.74% |    -1.36 |       79 | 36.61%     | ok               |

## PG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -8.05%   | -9.89%             | -19.77% |    -0.29 |       56 | 31.45%     | ok               |
|          35 | -11.19%  | -9.89%             | -18.66% |    -0.41 |       64 | 34.94%     | ok               |
|          30 | -19.26%  | -9.89%             | -24.25% |    -0.73 |       66 | 38.10%     | ok               |
|          45 | -17.03%  | -9.89%             | -22.13% |    -0.74 |       56 | 28.95%     | ok               |
|          25 | -21.10%  | -9.89%             | -25.94% |    -0.81 |       78 | 39.60%     | ok               |

## PM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -2.02%   | 105.89%            | -32.95% |     0.05 |       88 | 52.08%     | ok               |
|          20 | -4.67%   | 105.89%            | -32.63% |    -0    |       87 | 60.57%     | ok               |
|          30 | -5.09%   | 105.89%            | -34.41% |    -0.02 |       83 | 55.57%     | ok               |
|          50 | -7.54%   | 105.89%            | -35.70% |    -0.11 |       76 | 42.26%     | ok               |
|          40 | -8.92%   | 105.89%            | -37.94% |    -0.13 |       82 | 48.42%     | ok               |

## POL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 31.39%   | -73.25%            | -52.88% |     0.51 |       74 | 60.15%     | ok               |
|          25 | 27.85%   | -73.25%            | -46.72% |     0.49 |       66 | 55.17%     | ok               |
|          30 | 23.47%   | -73.25%            | -47.04% |     0.45 |       79 | 47.89%     | ok               |
|          15 | -3.09%   | -73.25%            | -58.42% |     0.21 |       76 | 65.33%     | ok               |
|          50 | 2.85%    | -73.25%            | -23.33% |     0.18 |       56 | 18.77%     | ok               |

## QCOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 0.44%    | -13.46%            | -54.83% |     0.18 |       75 | 47.42%     | ok               |
|          20 | -3.64%   | -13.46%            | -54.71% |     0.13 |       71 | 50.25%     | ok               |
|          35 | -5.80%   | -13.46%            | -50.58% |     0.08 |       81 | 43.09%     | ok               |
|          30 | -16.48%  | -13.46%            | -56.59% |    -0.06 |       77 | 45.59%     | ok               |
|          15 | -19.66%  | -13.46%            | -58.24% |    -0.08 |       75 | 53.41%     | ok               |

## QQQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 20.33%   | 56.71%             | -12.88% |     0.58 |       60 | 43.59%     | ok               |
|          25 | 20.78%   | 56.71%             | -12.88% |     0.58 |       57 | 46.26%     | ok               |
|          15 | 22.51%   | 56.71%             | -14.17% |     0.57 |       63 | 52.58%     | ok               |
|          20 | 17.86%   | 56.71%             | -12.98% |     0.5  |       65 | 48.92%     | ok               |
|          35 | 8.03%    | 56.71%             | -18.29% |     0.29 |       66 | 39.93%     | ok               |

## RENDER-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 39.15%   | -64.37%            | -43.43% |     0.57 |       92 | 53.26%     | ok               |
|          15 | 31.57%   | -64.37%            | -44.59% |     0.52 |       92 | 56.70%     | ok               |
|          25 | 12.20%   | -64.37%            | -40.60% |     0.39 |       92 | 48.47%     | ok               |
|          30 | -21.35%  | -64.37%            | -43.50% |     0.07 |      100 | 42.15%     | ok               |
|          40 | -24.66%  | -64.37%            | -38.60% |    -0.06 |       74 | 27.39%     | ok               |

## RTX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 47.55%   | 136.82%            | -18.66% |     0.97 |       72 | 57.24%     | ok               |
|          35 | 37.30%   | 136.82%            | -18.00% |     0.9  |       50 | 51.41%     | ok               |
|          25 | 42.50%   | 136.82%            | -18.59% |     0.9  |       60 | 54.58%     | ok               |
|          30 | 40.34%   | 136.82%            | -16.99% |     0.87 |       54 | 53.41%     | ok               |
|          15 | 39.15%   | 136.82%            | -19.55% |     0.82 |       67 | 61.90%     | ok               |

## SBUX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -9.63%   | 15.58%             | -23.55% |    -0.11 |       59 | 42.10%     | ok               |
|          45 | -12.52%  | 15.58%             | -27.26% |    -0.25 |       70 | 30.62%     | ok               |
|          40 | -15.16%  | 15.58%             | -25.43% |    -0.29 |       66 | 34.28%     | ok               |
|          30 | -19.04%  | 15.58%             | -29.22% |    -0.35 |       62 | 39.93%     | ok               |
|          50 | -16.54%  | 15.58%             | -25.71% |    -0.38 |       58 | 26.29%     | ok               |

## SCHW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 7.81%    | 56.68%             | -16.53% |     0.29 |       60 | 35.61%     | ok               |
|          25 | 3.73%    | 56.68%             | -28.76% |     0.18 |       63 | 51.25%     | ok               |
|          50 | 2.63%    | 56.68%             | -13.28% |     0.15 |       52 | 32.61%     | ok               |
|          20 | 0.01%    | 56.68%             | -29.24% |     0.1  |       71 | 53.74%     | ok               |
|          40 | -2.53%   | 56.68%             | -23.35% |     0.01 |       66 | 38.77%     | ok               |

## SHIB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -21.04%  | -65.03%            | -50.97% |    -0.02 |       80 | 67.05%     | ok               |
|          25 | -20.07%  | -65.03%            | -45.80% |    -0.02 |       75 | 59.20%     | ok               |
|          20 | -24.88%  | -65.03%            | -48.24% |    -0.08 |       77 | 63.03%     | ok               |
|          35 | -23.80%  | -65.03%            | -52.76% |    -0.12 |       66 | 46.55%     | ok               |
|          40 | -27.54%  | -65.03%            | -49.11% |    -0.2  |       56 | 39.08%     | ok               |

## SHY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          30 | -2.23%   | 0.24%              | -2.85% |    -0.78 |       46 | 34.11%     | ok               |
|          35 | -2.34%   | 0.24%              | -3.27% |    -0.83 |       48 | 32.28%     | ok               |
|          40 | -2.46%   | 0.24%              | -3.33% |    -0.89 |       48 | 30.45%     | ok               |
|          45 | -2.44%   | 0.24%              | -3.23% |    -0.9  |       46 | 27.29%     | ok               |
|          50 | -2.61%   | 0.24%              | -3.40% |    -1.01 |       42 | 24.46%     | ok               |

## SKY-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -35.13%  | -4.06%             | -56.39% |    -0.37 |       65 | 51.91%     | ok               |
|          30 | -31.51%  | -4.06%             | -47.82% |    -0.38 |       76 | 42.16%     | ok               |
|          25 | -34.45%  | -4.06%             | -50.05% |    -0.42 |       70 | 45.76%     | ok               |
|          20 | -44.43%  | -4.06%             | -59.15% |    -0.6  |       67 | 49.15%     | ok               |
|          35 | -37.82%  | -4.06%             | -49.68% |    -0.6  |       70 | 34.75%     | ok               |

## SLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 15.85%   | -1.61%             | -21.46% |     0.42 |       54 | 33.78%     | ok               |
|          40 | 12.27%   | -1.61%             | -25.33% |     0.34 |       48 | 37.27%     | ok               |
|          50 | -5.47%   | -1.61%             | -29.66% |    -0.05 |       52 | 28.95%     | ok               |
|          35 | -15.70%  | -1.61%             | -43.52% |    -0.23 |       76 | 44.76%     | ok               |
|          30 | -28.71%  | -1.61%             | -54.23% |    -0.51 |       77 | 51.25%     | ok               |

## SLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 67.53%   | 135.54%            | -34.10% |     0.86 |       52 | 34.61%     | ok               |
|          45 | 65.50%   | 135.54%            | -31.82% |     0.84 |       58 | 35.77%     | ok               |
|          40 | 63.52%   | 135.54%            | -31.93% |     0.82 |       64 | 37.94%     | ok               |
|          35 | 49.58%   | 135.54%            | -36.89% |     0.69 |       72 | 40.77%     | ok               |
|          20 | 51.52%   | 135.54%            | -42.66% |     0.69 |       66 | 48.25%     | ok               |

## SMH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 85.75%   | 140.25%            | -31.01% |     1.12 |       49 | 48.92%     | ok               |
|          35 | 68.25%   | 140.25%            | -34.36% |     1    |       54 | 44.59%     | ok               |
|          25 | 68.13%   | 140.25%            | -32.94% |     0.98 |       46 | 47.59%     | ok               |
|          30 | 66.15%   | 140.25%            | -33.99% |     0.97 |       48 | 45.92%     | ok               |
|          45 | 54.06%   | 140.25%            | -32.75% |     0.91 |       52 | 38.77%     | ok               |

## SNX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.97%   | -76.92%            | -43.20% |     0.2  |       73 | 48.28%     | ok               |
|          35 | -3.45%   | -76.92%            | -30.08% |     0.2  |       62 | 30.08%     | ok               |
|          30 | -15.33%  | -76.92%            | -36.73% |     0.08 |       64 | 37.74%     | ok               |
|          40 | -14.38%  | -76.92%            | -36.47% |     0.01 |       50 | 24.14%     | ok               |
|          15 | -34.16%  | -76.92%            | -44.00% |    -0.09 |       83 | 52.68%     | ok               |

## SOL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -12.93%  | -50.79%            | -51.46% |     0.08 |       58 | 35.82%     | ok               |
|          25 | -38.45%  | -50.79%            | -49.89% |    -0.21 |       78 | 57.09%     | ok               |
|          35 | -36.38%  | -50.79%            | -59.27% |    -0.21 |       74 | 43.30%     | ok               |
|          45 | -32.93%  | -50.79%            | -58.76% |    -0.23 |       60 | 30.84%     | ok               |
|          15 | -45.75%  | -50.79%            | -56.24% |    -0.3  |       81 | 63.22%     | ok               |

## SOXX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 72.35%   | 121.32%            | -39.85% |     0.97 |       51 | 47.09%     | ok               |
|          35 | 67.54%   | 121.32%            | -38.63% |     0.95 |       59 | 42.43%     | ok               |
|          30 | 62.67%   | 121.32%            | -40.34% |     0.89 |       55 | 44.93%     | ok               |
|          20 | 59.86%   | 121.32%            | -38.67% |     0.84 |       57 | 47.75%     | ok               |
|          15 | 58.38%   | 121.32%            | -37.72% |     0.8  |       72 | 51.08%     | ok               |

## SPY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 13.36%   | 45.98%             | -14.25% |     0.48 |       59 | 53.08%     | ok               |
|          15 | 11.81%   | 45.98%             | -16.80% |     0.43 |       68 | 56.24%     | ok               |
|          25 | 6.31%    | 45.98%             | -15.22% |     0.27 |       59 | 52.08%     | ok               |
|          30 | 1.82%    | 45.98%             | -16.47% |     0.12 |       62 | 49.25%     | ok               |
|          35 | 1.21%    | 45.98%             | -16.72% |     0.1  |       58 | 46.26%     | ok               |

## SUSHI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -28.52%  | -80.53%            | -40.08% |    -0.27 |       54 | 14.94%     | ok               |
|          40 | -64.04%  | -80.53%            | -70.25% |    -0.83 |       65 | 24.90%     | ok               |
|          45 | -61.31%  | -80.53%            | -65.82% |    -0.84 |       58 | 18.39%     | ok               |
|          15 | -79.13%  | -80.53%            | -81.89% |    -0.98 |       93 | 49.04%     | ok               |
|          35 | -75.94%  | -80.53%            | -81.46% |    -1.1  |       86 | 31.03%     | ok               |

## T Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 52.89%   | 35.17%             | -18.13% |     1.04 |       62 | 58.40%     | ok               |
|          25 | 48.75%   | 35.17%             | -17.66% |     0.99 |       62 | 56.07%     | ok               |
|          15 | 50.93%   | 35.17%             | -15.08% |     0.98 |       71 | 62.56%     | ok               |
|          30 | 32.45%   | 35.17%             | -17.01% |     0.74 |       66 | 54.08%     | ok               |
|          35 | 18.59%   | 35.17%             | -14.49% |     0.5  |       68 | 50.42%     | ok               |

## TGT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -23.01%  | -14.87%            | -44.02% |    -0.42 |       86 | 44.76%     | ok               |
|          25 | -22.58%  | -14.87%            | -43.64% |    -0.47 |       68 | 39.93%     | ok               |
|          30 | -21.64%  | -14.87%            | -40.57% |    -0.47 |       62 | 37.27%     | ok               |
|          15 | -27.92%  | -14.87%            | -42.01% |    -0.52 |       78 | 49.42%     | ok               |
|          45 | -23.08%  | -14.87%            | -31.75% |    -0.6  |       58 | 27.62%     | ok               |

## TIA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -5.44%   | -92.04%            | -53.37% |     0.18 |       68 | 33.14%     | ok               |
|          45 | -2.76%   | -92.04%            | -49.52% |     0.16 |       56 | 19.73%     | ok               |
|          50 | -0.89%   | -92.04%            | -48.70% |     0.14 |       36 | 12.45%     | ok               |
|          40 | -12.63%  | -92.04%            | -52.29% |     0.08 |       70 | 27.78%     | ok               |
|          15 | -34.77%  | -92.04%            | -63.05% |    -0.03 |       96 | 54.98%     | ok               |

## TLT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -19.44%  | -14.08%            | -21.87% |    -1.44 |       72 | 33.94%     | ok               |
|          40 | -17.59%  | -14.08%            | -19.70% |    -1.6  |       58 | 23.46%     | ok               |
|          50 | -14.21%  | -14.08%            | -15.53% |    -1.64 |       36 | 15.97%     | ok               |
|          35 | -20.23%  | -14.08%            | -22.27% |    -1.7  |       66 | 28.12%     | ok               |
|          15 | -25.34%  | -14.08%            | -27.76% |    -1.72 |       77 | 41.93%     | ok               |

## TMO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 46.73%   | -3.90%             | -8.17%  |     1.04 |       44 | 33.11%     | ok               |
|          45 | 40.37%   | -3.90%             | -10.13% |     0.88 |       48 | 38.10%     | ok               |
|          40 | 39.09%   | -3.90%             | -9.91%  |     0.84 |       51 | 42.76%     | ok               |
|          35 | 32.04%   | -3.90%             | -14.06% |     0.68 |       61 | 47.42%     | ok               |
|          30 | 26.12%   | -3.90%             | -18.85% |     0.57 |       61 | 52.58%     | ok               |

## TMUS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 5.48%    | 5.32%              | -30.05% |     0.21 |       63 | 58.57%     | ok               |
|          30 | 4.31%    | 5.32%              | -25.71% |     0.19 |       68 | 46.59%     | ok               |
|          20 | -0.60%   | 5.32%              | -29.75% |     0.09 |       69 | 52.91%     | ok               |
|          25 | -3.94%   | 5.32%              | -31.45% |     0.01 |       73 | 49.08%     | ok               |
|          35 | -7.65%   | 5.32%              | -34.23% |    -0.08 |       68 | 43.43%     | ok               |

## TRX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 13.93%   | 39.61%             | -18.79% |     0.48 |       52 | 36.21%     | ok               |
|          30 | 10.63%   | 39.61%             | -22.90% |     0.37 |       68 | 48.28%     | ok               |
|          35 | 8.98%    | 39.61%             | -21.77% |     0.33 |       66 | 44.83%     | ok               |
|          50 | 7.63%    | 39.61%             | -18.49% |     0.31 |       44 | 31.80%     | ok               |
|          20 | 8.29%    | 39.61%             | -25.45% |     0.3  |       63 | 55.17%     | ok               |

## TSLA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 54.73%   | 77.49%             | -32.60% |     0.71 |       66 | 30.45%     | ok               |
|          40 | 31.77%   | 77.49%             | -45.90% |     0.5  |       67 | 35.44%     | ok               |
|          45 | 11.64%   | 77.49%             | -46.86% |     0.31 |       71 | 32.78%     | ok               |
|          35 | -5.92%   | 77.49%             | -54.51% |     0.14 |       78 | 38.27%     | ok               |
|          30 | -22.15%  | 77.49%             | -57.89% |    -0.04 |       74 | 42.26%     | ok               |

## TXN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 10.94%   | 60.03%             | -45.45% |     0.3  |       66 | 33.78%     | ok               |
|          20 | -3.95%   | 60.03%             | -38.49% |     0.1  |       62 | 57.40%     | ok               |
|          15 | -5.67%   | 60.03%             | -38.99% |     0.08 |       65 | 61.56%     | ok               |
|          35 | -5.71%   | 60.03%             | -43.28% |     0.04 |       74 | 48.25%     | ok               |
|          40 | -8.38%   | 60.03%             | -45.67% |    -0    |       72 | 46.09%     | ok               |

## UNH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 23.40%   | -13.05%            | -37.02% |     0.46 |       60 | 30.95%     | ok               |
|          30 | 23.80%   | -13.05%            | -28.45% |     0.45 |       76 | 52.58%     | ok               |
|          15 | 22.96%   | -13.05%            | -33.62% |     0.43 |       73 | 67.39%     | ok               |
|          35 | 21.24%   | -13.05%            | -29.78% |     0.42 |       68 | 47.25%     | ok               |
|          25 | 12.44%   | -13.05%            | -29.39% |     0.32 |       74 | 57.74%     | ok               |

## UNI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -18.96%  | -45.28%            | -63.24% |     0.02 |       60 | 34.48%     | ok               |
|          45 | -24.55%  | -45.28%            | -57.91% |    -0.07 |       62 | 29.50%     | ok               |
|          35 | -37.11%  | -45.28%            | -68.27% |    -0.19 |       74 | 40.42%     | ok               |
|          50 | -32.38%  | -45.28%            | -57.01% |    -0.23 |       58 | 22.99%     | ok               |
|          30 | -72.21%  | -45.28%            | -80.33% |    -0.84 |       90 | 46.17%     | ok               |

## UPS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -37.57%  | -32.31%            | -43.07% |    -0.71 |       84 | 48.59%     | ok               |
|          25 | -37.76%  | -32.31%            | -39.10% |    -0.73 |       78 | 45.09%     | ok               |
|          15 | -39.78%  | -32.31%            | -43.86% |    -0.75 |       86 | 52.41%     | ok               |
|          35 | -38.80%  | -32.31%            | -40.10% |    -0.8  |       67 | 34.44%     | ok               |
|          30 | -41.40%  | -32.31%            | -41.64% |    -0.86 |       72 | 40.27%     | ok               |

## USO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 26.59%   | 76.08%             | -44.92% |     0.49 |       75 | 40.60%     | ok               |
|          15 | 20.61%   | 76.08%             | -45.09% |     0.41 |       74 | 43.76%     | ok               |
|          45 | 18.38%   | 76.08%             | -33.25% |     0.4  |       50 | 27.29%     | ok               |
|          25 | 15.28%   | 76.08%             | -44.86% |     0.35 |       69 | 37.94%     | ok               |
|          30 | 10.30%   | 76.08%             | -43.35% |     0.29 |       70 | 34.78%     | ok               |

## VEA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 3.94%    | 41.32%             | -16.28% |     0.2  |       58 | 49.58%     | ok               |
|          20 | -0.25%   | 41.32%             | -17.70% |     0.04 |       59 | 46.92%     | ok               |
|          25 | -2.23%   | 41.32%             | -17.79% |    -0.04 |       55 | 45.26%     | ok               |
|          30 | -2.39%   | 41.32%             | -17.93% |    -0.05 |       56 | 43.09%     | ok               |
|          35 | -3.48%   | 41.32%             | -16.79% |    -0.09 |       54 | 42.10%     | ok               |

## VIXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -48.04%  | -64.39%            | -69.78% |    -0.43 |       46 | 10.48%     | ok               |
|          45 | -57.65%  | -64.39%            | -75.03% |    -0.58 |       58 | 16.47%     | ok               |
|          40 | -65.68%  | -64.39%            | -80.72% |    -0.69 |       72 | 20.80%     | ok               |
|          35 | -69.93%  | -64.39%            | -84.37% |    -0.74 |       90 | 25.79%     | ok               |
|          15 | -76.29%  | -64.39%            | -89.47% |    -0.75 |       99 | 43.43%     | ok               |

## VNQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -9.52%   | 12.79%             | -19.07% |    -0.42 |       58 | 28.62%     | ok               |
|          50 | -9.95%   | 12.79%             | -17.13% |    -0.46 |       54 | 26.12%     | ok               |
|          25 | -13.64%  | 12.79%             | -22.16% |    -0.53 |       66 | 40.77%     | ok               |
|          20 | -15.22%  | 12.79%             | -23.61% |    -0.59 |       69 | 43.43%     | ok               |
|          15 | -16.51%  | 12.79%             | -24.73% |    -0.64 |       66 | 44.59%     | ok               |

## VTI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 16.22%   | 44.72%             | -13.96% |     0.56 |       62 | 53.58%     | ok               |
|          15 | 10.27%   | 44.72%             | -15.70% |     0.38 |       65 | 56.07%     | ok               |
|          25 | 2.79%    | 44.72%             | -16.10% |     0.16 |       58 | 51.58%     | ok               |
|          30 | -4.92%   | 44.72%             | -18.77% |    -0.12 |       68 | 49.58%     | ok               |
|          35 | -7.31%   | 44.72%             | -20.89% |    -0.22 |       62 | 46.42%     | ok               |

## VWO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -7.42%   | 40.68%             | -21.18% |    -0.26 |       58 | 30.62%     | ok               |
|          45 | -9.23%   | 40.68%             | -23.26% |    -0.34 |       60 | 33.11%     | ok               |
|          40 | -10.27%  | 40.68%             | -23.57% |    -0.37 |       70 | 35.77%     | ok               |
|          15 | -12.14%  | 40.68%             | -24.01% |    -0.38 |       75 | 48.42%     | ok               |
|          20 | -13.14%  | 40.68%             | -26.14% |    -0.43 |       73 | 46.26%     | ok               |

## VZ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -5.96%   | 18.48%             | -12.71% |    -0.15 |       52 | 25.12%     | ok               |
|          25 | -19.40%  | 18.48%             | -22.13% |    -0.53 |       79 | 42.60%     | ok               |
|          45 | -17.19%  | 18.48%             | -21.44% |    -0.55 |       66 | 28.79%     | ok               |
|          35 | -18.37%  | 18.48%             | -22.73% |    -0.56 |       61 | 34.61%     | ok               |
|          40 | -22.94%  | 18.48%             | -24.21% |    -0.76 |       66 | 31.95%     | ok               |

## WFC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -10.64%  | 51.48%             | -22.54% |    -0.16 |       81 | 46.42%     | ok               |
|          50 | -7.89%   | 51.48%             | -18.29% |    -0.19 |       62 | 34.11%     | ok               |
|          20 | -17.66%  | 51.48%             | -29.87% |    -0.25 |       79 | 55.57%     | ok               |
|          30 | -19.95%  | 51.48%             | -29.78% |    -0.35 |       84 | 49.58%     | ok               |
|          25 | -23.41%  | 51.48%             | -33.38% |    -0.4  |       76 | 52.58%     | ok               |

## WIF-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 29.75%   | -78.04%            | -46.21% |     0.51 |       74 | 43.87%     | ok               |
|          20 | 26.38%   | -78.04%            | -40.67% |     0.48 |       67 | 41.00%     | ok               |
|          25 | -35.79%  | -78.04%            | -52.50% |    -0.07 |       71 | 37.74%     | ok               |
|          50 | -24.32%  | -78.04%            | -41.18% |    -0.22 |       42 | 12.26%     | ok               |
|          30 | -52.90%  | -78.04%            | -61.76% |    -0.39 |       72 | 33.91%     | ok               |

## WMT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 43.02%   | 84.96%             | -9.18%  |     1.22 |       40 | 40.27%     | ok               |
|          50 | 37.50%   | 84.96%             | -12.19% |     1.15 |       34 | 37.77%     | ok               |
|          40 | 31.12%   | 84.96%             | -13.41% |     0.91 |       46 | 41.60%     | ok               |
|          35 | 30.26%   | 84.96%             | -13.99% |     0.87 |       56 | 46.26%     | ok               |
|          15 | 16.70%   | 84.96%             | -25.74% |     0.45 |       72 | 60.40%     | ok               |

## XBI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 0.54%    | 48.57%             | -16.08% |     0.09 |       62 | 34.44%     | ok               |
|          45 | -0.23%   | 48.57%             | -15.46% |     0.07 |       54 | 31.28%     | ok               |
|          35 | -7.03%   | 48.57%             | -16.96% |    -0.1  |       68 | 38.10%     | ok               |
|          30 | -7.94%   | 48.57%             | -18.51% |    -0.13 |       66 | 39.93%     | ok               |
|          25 | -9.83%   | 48.57%             | -23.66% |    -0.17 |       74 | 42.10%     | ok               |

## XLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -2.42%   | 12.88%             | -19.67% |    -0.04 |       54 | 30.45%     | ok               |
|          50 | -3.71%   | 12.88%             | -17.59% |    -0.1  |       42 | 26.29%     | ok               |
|          35 | -5.63%   | 12.88%             | -22.65% |    -0.16 |       56 | 33.78%     | ok               |
|          45 | -5.36%   | 12.88%             | -19.78% |    -0.17 |       42 | 27.62%     | ok               |
|          25 | -8.74%   | 12.88%             | -22.63% |    -0.27 |       60 | 39.27%     | ok               |

## XLC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 11.88%   | 36.00%             | -12.33% |     0.44 |       67 | 52.75%     | ok               |
|          25 | 9.12%    | 36.00%             | -12.31% |     0.35 |       66 | 54.58%     | ok               |
|          40 | 7.83%    | 36.00%             | -13.38% |     0.34 |       66 | 45.76%     | ok               |
|          35 | 7.01%    | 36.00%             | -13.38% |     0.3  |       64 | 49.92%     | ok               |
|          45 | 2.84%    | 36.00%             | -13.21% |     0.16 |       64 | 42.93%     | ok               |

## XLE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 8.22%    | 35.08%             | -25.98% |     0.3  |       54 | 36.11%     | ok               |
|          45 | 3.79%    | 35.08%             | -29.68% |     0.18 |       60 | 38.10%     | ok               |
|          35 | 1.60%    | 35.08%             | -31.51% |     0.12 |       65 | 42.76%     | ok               |
|          25 | -5.13%   | 35.08%             | -36.05% |    -0.04 |       83 | 48.25%     | ok               |
|          40 | -5.02%   | 35.08%             | -34.51% |    -0.06 |       64 | 40.60%     | ok               |

## XLF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -4.38%   | 40.18%             | -18.01% |    -0.08 |       68 | 53.91%     | ok               |
|          15 | -8.34%   | 40.18%             | -19.58% |    -0.22 |       76 | 56.74%     | ok               |
|          25 | -11.05%  | 40.18%             | -23.22% |    -0.34 |       77 | 50.42%     | ok               |
|          30 | -12.29%  | 40.18%             | -23.61% |    -0.4  |       80 | 47.92%     | ok               |
|          35 | -20.14%  | 40.18%             | -27.24% |    -0.8  |       70 | 43.59%     | ok               |

## XLI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 2.50%    | 47.05%             | -10.36% |     0.15 |       78 | 50.75%     | ok               |
|          20 | -2.94%   | 47.05%             | -12.74% |    -0.06 |       71 | 45.76%     | ok               |
|          30 | -6.90%   | 47.05%             | -14.12% |    -0.23 |       70 | 42.93%     | ok               |
|          50 | -5.96%   | 47.05%             | -13.59% |    -0.24 |       62 | 31.45%     | ok               |
|          45 | -6.62%   | 47.05%             | -16.29% |    -0.25 |       68 | 34.28%     | ok               |

## XLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 78.33%   | 69.13%             | -14.75% |     1.27 |       43 | 51.25%     | ok               |
|          20 | 71.51%   | 69.13%             | -14.75% |     1.23 |       46 | 48.92%     | ok               |
|          25 | 68.02%   | 69.13%             | -14.75% |     1.23 |       40 | 46.76%     | ok               |
|          30 | 65.83%   | 69.13%             | -14.75% |     1.22 |       40 | 45.59%     | ok               |
|          35 | 47.33%   | 69.13%             | -13.61% |     0.99 |       52 | 42.93%     | ok               |

## XLM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 26.14%   | -40.20%            | -38.97% |     0.48 |       44 | 27.39%     | ok               |
|          45 | 22.34%   | -40.20%            | -43.99% |     0.44 |       50 | 31.03%     | ok               |
|          30 | 12.70%   | -40.20%            | -50.36% |     0.35 |       65 | 45.40%     | ok               |
|          25 | 9.24%    | -40.20%            | -48.11% |     0.32 |       67 | 47.89%     | ok               |
|          20 | 0.61%    | -40.20%            | -55.30% |     0.23 |       66 | 50.19%     | ok               |

## XLP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 12.41%   | 13.16%             | -5.66%  |     0.76 |       50 | 32.28%     | ok               |
|          40 | 10.14%   | 13.16%             | -7.77%  |     0.61 |       66 | 36.44%     | ok               |
|          50 | 8.95%    | 13.16%             | -6.08%  |     0.58 |       54 | 30.45%     | ok               |
|          35 | 9.18%    | 13.16%             | -9.73%  |     0.55 |       62 | 39.43%     | ok               |
|          30 | 8.30%    | 13.16%             | -10.28% |     0.49 |       64 | 41.10%     | ok               |

## XLU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 5.85%    | 39.14%             | -12.97% |     0.32 |       52 | 31.28%     | ok               |
|          45 | 4.45%    | 39.14%             | -14.27% |     0.25 |       54 | 32.28%     | ok               |
|          40 | 1.57%    | 39.14%             | -15.59% |     0.12 |       58 | 33.78%     | ok               |
|          35 | -4.35%   | 39.14%             | -19.71% |    -0.16 |       62 | 35.94%     | ok               |
|          30 | -5.24%   | 39.14%             | -20.40% |    -0.19 |       67 | 39.10%     | ok               |

## XLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -14.73%  | 11.01%             | -18.49% |    -0.73 |       66 | 34.61%     | ok               |
|          25 | -15.89%  | 11.01%             | -21.14% |    -0.78 |       68 | 36.61%     | ok               |
|          20 | -19.08%  | 11.01%             | -24.51% |    -0.94 |       73 | 38.44%     | ok               |
|          15 | -19.58%  | 11.01%             | -24.84% |    -0.94 |       81 | 41.43%     | ok               |
|          35 | -19.19%  | 11.01%             | -22.54% |    -1.04 |       64 | 32.11%     | ok               |

## XLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 2.91%    | 28.77%             | -14.01% |     0.16 |       70 | 44.09%     | ok               |
|          35 | 2.24%    | 28.77%             | -12.94% |     0.14 |       70 | 41.26%     | ok               |
|          15 | 0.18%    | 28.77%             | -15.77% |     0.08 |       74 | 50.75%     | ok               |
|          50 | -1.05%   | 28.77%             | -11.49% |     0.01 |       54 | 29.62%     | ok               |
|          20 | -4.37%   | 28.77%             | -19.25% |    -0.06 |       71 | 47.42%     | ok               |

## XOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 10.30%   | 43.42%             | -19.90% |     0.34 |       55 | 38.60%     | ok               |
|          50 | 9.35%    | 43.42%             | -21.35% |     0.34 |       38 | 30.78%     | ok               |
|          30 | 9.21%    | 43.42%             | -20.29% |     0.32 |       55 | 37.94%     | ok               |
|          20 | 2.51%    | 43.42%             | -25.56% |     0.14 |       64 | 40.77%     | ok               |
|          45 | 2.29%    | 43.42%             | -23.33% |     0.14 |       44 | 32.28%     | ok               |

## XRP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -13.80%  | -50.06%            | -38.85% |     0.02 |       64 | 38.89%     | ok               |
|          40 | -22.96%  | -50.06%            | -38.94% |    -0.14 |       54 | 33.14%     | ok               |
|          30 | -27.75%  | -50.06%            | -47.86% |    -0.17 |       66 | 43.10%     | ok               |
|          45 | -31.57%  | -50.06%            | -40.24% |    -0.3  |       54 | 28.93%     | ok               |
|          50 | -27.85%  | -50.06%            | -38.03% |    -0.32 |       56 | 21.46%     | ok               |

## YFI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -51.83%  | -62.06%            | -52.84% |    -0.88 |       60 | 27.97%     | ok               |
|          30 | -64.19%  | -62.06%            | -71.12% |    -1.03 |       81 | 40.61%     | ok               |
|          35 | -62.09%  | -62.06%            | -63.29% |    -1.04 |       65 | 35.25%     | ok               |
|          45 | -50.42%  | -62.06%            | -54.66% |    -1.05 |       70 | 22.61%     | ok               |
|          25 | -69.64%  | -62.06%            | -73.69% |    -1.18 |       80 | 46.55%     | ok               |

## ZEC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 116.41%  | 1167.89%           | -24.66% |     0.87 |       42 | 24.71%     | ok               |
|          35 | 85.19%   | 1167.89%           | -44.34% |     0.74 |       50 | 30.84%     | ok               |
|          25 | 58.00%   | 1167.89%           | -52.49% |     0.62 |       58 | 40.42%     | ok               |
|          50 | 48.76%   | 1167.89%           | -34.17% |     0.57 |       44 | 22.22%     | ok               |
|          40 | 47.48%   | 1167.89%           | -48.16% |     0.57 |       52 | 28.54%     | ok               |
