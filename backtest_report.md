# Market Tracker Backtest Report

_Generated: 2026-07-02T01:36:15+00:00_

## Data Sources

- Crypto: Kraken -> Coinbase -> CoinGecko OHLC -> CoinPaprika fallback chain.
- Stocks / ETFs / indices: Stooq -> Yahoo Finance fallback chain.
- Data rows are generated from real market APIs. Mock OHLCV rows are not generated.

## Data Freshness

- Rows: **92,454**
- Symbols: **161**
- Date range: **2024-02-07** to **2026-07-02**

## Latest Signals

| symbol     | date                |         close |   composite_score | signal   | data_source   |
|:-----------|:--------------------|--------------:|------------------:|:---------|:--------------|
| AAVE-USD   | 2026-07-02 00:00:00 |    84.24      |          45       | LONG     | Kraken API    |
| ABBV       | 2026-07-01 00:00:00 |   251.06      |          59.75    | LONG     | Yahoo Finance |
| AMAT       | 2026-07-01 00:00:00 |   650.91      |          65.4167  | LONG     | Yahoo Finance |
| AMZN       | 2026-07-01 00:00:00 |   241.7       |          35.6667  | LONG     | Yahoo Finance |
| BAC        | 2026-07-01 00:00:00 |    58.36      |          60.5833  | LONG     | Yahoo Finance |
| C          | 2026-07-01 00:00:00 |   140.13      |          48.5833  | LONG     | Yahoo Finance |
| CAT        | 2026-07-01 00:00:00 |   991.41      |          74.4167  | LONG     | Yahoo Finance |
| DE         | 2026-07-01 00:00:00 |   627.63      |          73.25    | LONG     | Yahoo Finance |
| DXY-INDEX  | 2026-07-01 00:00:00 |   101.399     |          81.7204  | LONG     | Yahoo Finance |
| GE         | 2026-07-01 00:00:00 |   374.94      |          60       | LONG     | Yahoo Finance |
| HD         | 2026-07-01 00:00:00 |   350.84      |          63.5     | LONG     | Yahoo Finance |
| IBM        | 2026-07-01 00:00:00 |   286.25      |          57       | LONG     | Yahoo Finance |
| ITA        | 2026-07-01 00:00:00 |   243.86      |          62.25    | LONG     | Yahoo Finance |
| JNJ        | 2026-07-01 00:00:00 |   253.98      |          74.9167  | LONG     | Yahoo Finance |
| JPM        | 2026-07-01 00:00:00 |   334.07      |          60.5833  | LONG     | Yahoo Finance |
| LRCX       | 2026-07-01 00:00:00 |   391.26      |          67.0833  | LONG     | Yahoo Finance |
| MS         | 2026-07-01 00:00:00 |   211.86      |          34.75    | LONG     | Yahoo Finance |
| RTX        | 2026-07-01 00:00:00 |   191.78      |          69.3333  | LONG     | Yahoo Finance |
| SCHW       | 2026-07-01 00:00:00 |    95.78      |          67.6667  | LONG     | Yahoo Finance |
| SPY        | 2026-07-01 00:00:00 |   745.76      |          30.25    | LONG     | Yahoo Finance |
| TGT        | 2026-07-01 00:00:00 |   130.29      |          30.5833  | LONG     | Yahoo Finance |
| TMO        | 2026-07-01 00:00:00 |   513.33      |          65.5833  | LONG     | Yahoo Finance |
| TSLA       | 2026-07-01 00:00:00 |   425.3       |          49.4167  | LONG     | Yahoo Finance |
| UNH        | 2026-07-01 00:00:00 |   426.54      |          60.5833  | LONG     | Yahoo Finance |
| VTI        | 2026-07-01 00:00:00 |   369.27      |          37.75    | LONG     | Yahoo Finance |
| WFC        | 2026-07-01 00:00:00 |    85.94      |          55.3333  | LONG     | Yahoo Finance |
| XBI        | 2026-07-01 00:00:00 |   156.55      |          70.75    | LONG     | Yahoo Finance |
| XLF        | 2026-07-01 00:00:00 |    54.78      |          64.25    | LONG     | Yahoo Finance |
| XLU        | 2026-07-01 00:00:00 |    44.77      |          30.6667  | LONG     | Yahoo Finance |
| AAPL       | 2026-07-01 00:00:00 |   294.38      |          20.0833  | NEUTRAL  | Yahoo Finance |
| ADA-USD    | 2026-07-02 00:00:00 |     0.153671  |         -24       | NEUTRAL  | Kraken API    |
| AGG        | 2026-07-01 00:00:00 |    98.5       |         -18.0833  | NEUTRAL  | Yahoo Finance |
| ALGO-USD   | 2026-07-02 00:00:00 |     0.0848    |         -43.9167  | NEUTRAL  | Kraken API    |
| AMD        | 2026-07-01 00:00:00 |   540.88      |          45       | NEUTRAL  | Yahoo Finance |
| AMGN       | 2026-07-01 00:00:00 |   361.33      |          67.3333  | NEUTRAL  | Yahoo Finance |
| APT-USD    | 2026-07-02 00:00:00 |     0.5946    |         -18.6667  | NEUTRAL  | Kraken API    |
| ARB-USD    | 2026-07-02 00:00:00 |     0.0769    |         -42.25    | NEUTRAL  | Kraken API    |
| ARKK       | 2026-07-01 00:00:00 |    81.85      |          42       | NEUTRAL  | Yahoo Finance |
| AVAX-USD   | 2026-07-02 00:00:00 |     6.679     |           7.41667 | NEUTRAL  | Kraken API    |
| AVGO       | 2026-07-01 00:00:00 |   369.34      |         -27.3333  | NEUTRAL  | Yahoo Finance |
| BA         | 2026-07-01 00:00:00 |   218.58      |         -10.9167  | NEUTRAL  | Yahoo Finance |
| BCH-USD    | 2026-07-02 00:00:00 |   214.05      |         -10.5833  | NEUTRAL  | Kraken API    |
| BLK        | 2026-07-01 00:00:00 |   980.38      |         -61.5     | NEUTRAL  | Yahoo Finance |
| BND        | 2026-07-01 00:00:00 |    73.06      |         -19.8333  | NEUTRAL  | Yahoo Finance |
| BONK-USD   | 2026-07-02 00:00:00 |     4.252e-06 |         -42.25    | NEUTRAL  | Kraken API    |
| CL         | 2026-07-01 00:00:00 |    92.76      |          68.1667  | NEUTRAL  | Yahoo Finance |
| CMCSA      | 2026-07-01 00:00:00 |    23.73      |          -6.41667 | NEUTRAL  | Yahoo Finance |
| COST       | 2026-07-01 00:00:00 |   924.67      |         -54       | NEUTRAL  | Yahoo Finance |
| CRV-USD    | 2026-07-02 00:00:00 |     0.20569   |         -28.3333  | NEUTRAL  | Kraken API    |
| CSCO       | 2026-07-01 00:00:00 |   117.01      |          18.0833  | NEUTRAL  | Yahoo Finance |
| DASH-USD   | 2026-07-02 00:00:00 |    33.597     |         -55.75    | NEUTRAL  | Kraken API    |
| DBC        | 2026-07-01 00:00:00 |    26.45      |         -15.4167  | NEUTRAL  | Yahoo Finance |
| DIA        | 2026-07-01 00:00:00 |   522.4       |          54.5     | NEUTRAL  | Yahoo Finance |
| DIS        | 2026-07-01 00:00:00 |    95.71      |         -59.5     | NEUTRAL  | Yahoo Finance |
| EEM        | 2026-07-01 00:00:00 |    66.48      |          16.5     | NEUTRAL  | Yahoo Finance |
| EFA        | 2026-07-01 00:00:00 |   103.02      |          -4.16667 | NEUTRAL  | Yahoo Finance |
| EOG        | 2026-07-01 00:00:00 |   128.59      |         -28.0833  | NEUTRAL  | Yahoo Finance |
| ETC-USD    | 2026-07-02 00:00:00 |     6.988     |         -31.25    | NEUTRAL  | Kraken API    |
| EWJ        | 2026-07-01 00:00:00 |    93.05      |          31.5     | NEUTRAL  | Yahoo Finance |
| FCX        | 2026-07-01 00:00:00 |    60.53      |         -18.3333  | NEUTRAL  | Yahoo Finance |
| GDX        | 2026-07-01 00:00:00 |    75.07      |         -43.6667  | NEUTRAL  | Yahoo Finance |
| GDXJ       | 2026-07-01 00:00:00 |    98.05      |         -45.4167  | NEUTRAL  | Yahoo Finance |
| GOOGL      | 2026-07-01 00:00:00 |   361.21      |          17.8333  | NEUTRAL  | Yahoo Finance |
| GRT-USD    | 2026-07-02 00:00:00 |     0.01774   |         -38.25    | NEUTRAL  | Kraken API    |
| GS         | 2026-07-01 00:00:00 |  1019.61      |           8.33333 | NEUTRAL  | Yahoo Finance |
| HON        | 2026-07-01 00:00:00 |   221.75      |          20.75    | NEUTRAL  | Yahoo Finance |
| HYG        | 2026-07-01 00:00:00 |    79.59      |         -47.0833  | NEUTRAL  | Yahoo Finance |
| ICP-USD    | 2026-07-02 00:00:00 |     2.149     |         -38.9167  | NEUTRAL  | Kraken API    |
| IEF        | 2026-07-01 00:00:00 |    94.03      |         -12.8333  | NEUTRAL  | Yahoo Finance |
| IEMG       | 2026-07-01 00:00:00 |    80.63      |          14.75    | NEUTRAL  | Yahoo Finance |
| INJ-USD    | 2026-07-02 00:00:00 |     4.478     |         -55.8333  | NEUTRAL  | Kraken API    |
| INTC       | 2026-07-01 00:00:00 |   127.02      |          37.3333  | NEUTRAL  | Yahoo Finance |
| IWM        | 2026-07-01 00:00:00 |   299.32      |          59.5     | NEUTRAL  | Yahoo Finance |
| KO         | 2026-07-01 00:00:00 |    81.29      |          46.5     | NEUTRAL  | Yahoo Finance |
| LDO-USD    | 2026-07-02 00:00:00 |     0.247     |         -47.25    | NEUTRAL  | Kraken API    |
| LIN        | 2026-07-01 00:00:00 |   533.55      |          63.3333  | NEUTRAL  | Yahoo Finance |
| LINK-USD   | 2026-07-02 00:00:00 |     7.36162   |         -29       | NEUTRAL  | Kraken API    |
| LLY        | 2026-07-01 00:00:00 |  1191.74      |          37.8333  | NEUTRAL  | Yahoo Finance |
| LTC-USD    | 2026-07-02 00:00:00 |    42.58      |         -40.25    | NEUTRAL  | Kraken API    |
| MCD        | 2026-07-01 00:00:00 |   269.43      |         -64.5     | NEUTRAL  | Yahoo Finance |
| META       | 2026-07-01 00:00:00 |   612.91      |          18.9167  | NEUTRAL  | Yahoo Finance |
| MPC        | 2026-07-01 00:00:00 |   264.87      |          41.8333  | NEUTRAL  | Yahoo Finance |
| MRK        | 2026-07-01 00:00:00 |   125.37      |          59.8333  | NEUTRAL  | Yahoo Finance |
| MU         | 2026-07-01 00:00:00 |  1032.28      |          12.5     | NEUTRAL  | Yahoo Finance |
| NEAR-USD   | 2026-07-02 00:00:00 |     1.862     |         -20.5833  | NEUTRAL  | Kraken API    |
| NEM        | 2026-07-01 00:00:00 |    93.3       |         -46.1667  | NEUTRAL  | Yahoo Finance |
| NKE        | 2026-07-01 00:00:00 |    43.06      |         -40.5833  | NEUTRAL  | Yahoo Finance |
| NOW        | 2026-07-01 00:00:00 |   105.8       |          -6.16667 | NEUTRAL  | Yahoo Finance |
| OP-USD     | 2026-07-02 00:00:00 |     0.0957    |         -60.5833  | NEUTRAL  | Kraken API    |
| PEP        | 2026-07-01 00:00:00 |   141.16      |         -57       | NEUTRAL  | Yahoo Finance |
| PG         | 2026-07-01 00:00:00 |   147.43      |          -6.58333 | NEUTRAL  | Yahoo Finance |
| PM         | 2026-07-01 00:00:00 |   177.69      |           8       | NEUTRAL  | Yahoo Finance |
| POL-USD    | 2026-07-02 00:00:00 |     0.07203   |         -38.9167  | NEUTRAL  | Kraken API    |
| QCOM       | 2026-07-01 00:00:00 |   181.92      |         -21.9167  | NEUTRAL  | Yahoo Finance |
| QQQ        | 2026-07-01 00:00:00 |   725.17      |          38       | NEUTRAL  | Yahoo Finance |
| SBUX       | 2026-07-01 00:00:00 |   103.39      |          61.1667  | NEUTRAL  | Yahoo Finance |
| SHY        | 2026-07-01 00:00:00 |    81.84      |         -31.4167  | NEUTRAL  | Yahoo Finance |
| SKY-USD    | 2026-07-02 00:00:00 |     0.05273   |         -55.75    | NEUTRAL  | Kraken API    |
| SMH        | 2026-07-01 00:00:00 |   620.46      |          34.3333  | NEUTRAL  | Yahoo Finance |
| SNX-USD    | 2026-07-02 00:00:00 |     0.2132    |         -48.25    | NEUTRAL  | Kraken API    |
| SOL-USD    | 2026-07-02 00:00:00 |    77.52      |          30.4167  | NEUTRAL  | Kraken API    |
| SOXX       | 2026-07-01 00:00:00 |   599.7       |          43.3333  | NEUTRAL  | Yahoo Finance |
| TLT        | 2026-07-01 00:00:00 |    85.52      |         -19.9167  | NEUTRAL  | Yahoo Finance |
| TRX-USD    | 2026-07-02 00:00:00 |     0.316108  |         -37.1667  | NEUTRAL  | Kraken API    |
| TXN        | 2026-07-01 00:00:00 |   298.41      |          15.3333  | NEUTRAL  | Yahoo Finance |
| UPS        | 2026-07-01 00:00:00 |   109.54      |          48.3333  | NEUTRAL  | Yahoo Finance |
| VEA        | 2026-07-01 00:00:00 |    70.36      |          18.5     | NEUTRAL  | Yahoo Finance |
| VIXY       | 2026-07-01 00:00:00 |    21.52      |         -45.5     | NEUTRAL  | Yahoo Finance |
| VNQ        | 2026-07-01 00:00:00 |    96.82      |           2.16667 | NEUTRAL  | Yahoo Finance |
| VWO        | 2026-07-01 00:00:00 |    59.22      |           9.5     | NEUTRAL  | Yahoo Finance |
| WIF-USD    | 2026-07-02 00:00:00 |     0.1682    |           5.75    | NEUTRAL  | Kraken API    |
| WMT        | 2026-07-01 00:00:00 |   108.82      |         -74.5833  | NEUTRAL  | Yahoo Finance |
| XLB        | 2026-07-01 00:00:00 |    51.02      |          -3.66667 | NEUTRAL  | Yahoo Finance |
| XLC        | 2026-07-01 00:00:00 |   109.74      |         -21.5     | NEUTRAL  | Yahoo Finance |
| XLE        | 2026-07-01 00:00:00 |    52.81      |         -16.8333  | NEUTRAL  | Yahoo Finance |
| XLI        | 2026-07-01 00:00:00 |   183.36      |          63.5     | NEUTRAL  | Yahoo Finance |
| XLK        | 2026-07-01 00:00:00 |   185.62      |          38       | NEUTRAL  | Yahoo Finance |
| XLM-USD    | 2026-07-02 00:00:00 |     0.194659  |         -19.5833  | NEUTRAL  | Kraken API    |
| XLP        | 2026-07-01 00:00:00 |    83.3       |         -22.75    | NEUTRAL  | Yahoo Finance |
| XLV        | 2026-07-01 00:00:00 |   159.54      |          55.8333  | NEUTRAL  | Yahoo Finance |
| XLY        | 2026-07-01 00:00:00 |   118.09      |          40.6667  | NEUTRAL  | Yahoo Finance |
| YFI-USD    | 2026-07-02 00:00:00 |  1738.7       |         -42.25    | NEUTRAL  | Kraken API    |
| ZEC-USD    | 2026-07-02 00:00:00 |   413.1       |          -2.25    | NEUTRAL  | Kraken API    |
| ADBE       | 2026-07-01 00:00:00 |   210.98      |         -40.5833  | SHORT    | Yahoo Finance |
| ATOM-USD   | 2026-07-02 00:00:00 |     1.5498    |         -47.6667  | SHORT    | Kraken API    |
| BITO       | 2026-07-01 00:00:00 |     8.13      |         -30.75    | SHORT    | Yahoo Finance |
| BTC-USD    | 2026-07-02 00:00:00 | 59865.8       |         -29       | SHORT    | Kraken API    |
| COMP-USD   | 2026-07-02 00:00:00 |    15.75      |         -49.3333  | SHORT    | Kraken API    |
| COP        | 2026-07-01 00:00:00 |   103.22      |         -48.0833  | SHORT    | Yahoo Finance |
| CRM        | 2026-07-01 00:00:00 |   163.23      |         -37.0833  | SHORT    | Yahoo Finance |
| CVX        | 2026-07-01 00:00:00 |   165.69      |         -47.5833  | SHORT    | Yahoo Finance |
| DOGE-USD   | 2026-07-02 00:00:00 |     0.0721626 |         -51.3333  | SHORT    | Kraken API    |
| DOT-USD    | 2026-07-02 00:00:00 |     0.8309    |         -38       | SHORT    | Kraken API    |
| ETH-USD    | 2026-07-02 00:00:00 |  1607.53      |         -48.75    | SHORT    | Kraken API    |
| FET-USD    | 2026-07-02 00:00:00 |     0.1798    |         -33       | SHORT    | Kraken API    |
| FIL-USD    | 2026-07-02 00:00:00 |     0.739     |         -31       | SHORT    | Kraken API    |
| FXI        | 2026-07-01 00:00:00 |    31.97      |         -54.9167  | SHORT    | Yahoo Finance |
| GLD        | 2026-07-01 00:00:00 |   370.6       |         -49.0833  | SHORT    | Yahoo Finance |
| HBAR-USD   | 2026-07-02 00:00:00 |     0.07255   |         -42.3333  | SHORT    | Kraken API    |
| IBIT       | 2026-07-01 00:00:00 |    34         |         -30.75    | SHORT    | Yahoo Finance |
| INTU       | 2026-07-01 00:00:00 |   267.08      |         -30.75    | SHORT    | Yahoo Finance |
| MSFT       | 2026-07-01 00:00:00 |   384.28      |         -45.0833  | SHORT    | Yahoo Finance |
| NFLX       | 2026-07-01 00:00:00 |    74.19      |         -48.5833  | SHORT    | Yahoo Finance |
| NVDA       | 2026-07-01 00:00:00 |   197.58      |         -24.8333  | SHORT    | Yahoo Finance |
| ORCL       | 2026-07-01 00:00:00 |   142.5       |         -65.5833  | SHORT    | Yahoo Finance |
| OXY        | 2026-07-01 00:00:00 |    47.94      |         -50.0833  | SHORT    | Yahoo Finance |
| PEPE-USD   | 2026-07-02 00:00:00 |     2.33e-06  |         -51.3333  | SHORT    | Kraken API    |
| PFE        | 2026-07-01 00:00:00 |    23.88      |         -44.25    | SHORT    | Yahoo Finance |
| RENDER-USD | 2026-07-02 00:00:00 |     1.509     |         -46.3333  | SHORT    | Kraken API    |
| SHIB-USD   | 2026-07-02 00:00:00 |     4.278e-06 |         -34.3333  | SHORT    | Kraken API    |
| SLB        | 2026-07-01 00:00:00 |    45.09      |         -46.3333  | SHORT    | Yahoo Finance |
| SLV        | 2026-07-01 00:00:00 |    53.58      |         -53.0833  | SHORT    | Yahoo Finance |
| SUSHI-USD  | 2026-07-02 00:00:00 |     0.1506    |         -53.3333  | SHORT    | Kraken API    |
| T          | 2026-07-01 00:00:00 |    20.48      |         -56.6667  | SHORT    | Yahoo Finance |
| TIA-USD    | 2026-07-02 00:00:00 |     0.3574    |         -52       | SHORT    | Kraken API    |
| TMUS       | 2026-07-01 00:00:00 |   173.06      |         -50.75    | SHORT    | Yahoo Finance |
| UNI-USD    | 2026-07-02 00:00:00 |     2.8037    |         -51.3333  | SHORT    | Kraken API    |
| USO        | 2026-07-01 00:00:00 |   103.27      |         -46.3333  | SHORT    | Yahoo Finance |
| VZ         | 2026-07-01 00:00:00 |    41.99      |         -47.5833  | SHORT    | Yahoo Finance |
| XOM        | 2026-07-01 00:00:00 |   136.28      |         -45.5833  | SHORT    | Yahoo Finance |
| XRP-USD    | 2026-07-02 00:00:00 |     1.04993   |         -43.5833  | SHORT    | Kraken API    |

## Edge Summary

- Symbols with trades: **160** of 160
- Beat buy-and-hold: **36.25%** of traded symbols
- Positive return: **34.38%** of traded symbols
- Median strategy return: **-9.22%** (benchmark **13.57%**)
- Median excess vs benchmark: **-25.73%**
- Median Sharpe: **-0.07**
- Median exposure: **44.78%**

> Edge is real only if both _beat buy-and-hold_ and _median excess_ are convincingly positive across many symbols. Treat a single high-return symbol as noise.

## Portfolio Backtest

Actual capital-allocation books (not per-symbol averages). Benchmarks: `equal_weight_buyhold` (whole tracked universe), `spy_buyhold` (100% SPY), and `sixty_forty` (60% SPY / 40% AGG). `high_conf_voltarget` inverse-vol-weights the HIGH-confidence book; `conviction_long_short` is market-neutral. Judge on **Sharpe** and **max_drawdown** out-of-sample, not raw return: a fully-invested long book wins on return in a bull market but carries all the risk.

| strategy              | scope         | ann_return   | ann_vol   |   sharpe | max_drawdown   | total_return   |   avg_gross_exposure |
|:----------------------|:--------------|:-------------|:----------|---------:|:---------------|:---------------|---------------------:|
| equal_weight_buyhold  | full          | -7.56%       | 33.35%    |    -0.23 | -52.54%        | -33.01%        |                 1    |
| equal_weight_buyhold  | out_of_sample | -14.99%      | 34.07%    |    -0.44 | -39.63%        | -19.83%        |                 1    |
| all_signals_ew        | full          | -11.02%      | 28.25%    |    -0.39 | -60.00%        | -36.66%        |                 1    |
| all_signals_ew        | out_of_sample | 9.11%        | 28.54%    |     0.32 | -20.85%        | 5.53%          |                 1    |
| high_conf_ew          | full          | 4.96%        | 32.34%    |     0.15 | -44.48%        | -0.60%         |                 0.89 |
| high_conf_ew          | out_of_sample | 9.09%        | 35.22%    |     0.26 | -18.37%        | 3.28%          |                 0.89 |
| high_conf_voltarget   | full          | 5.79%        | 29.88%    |     0.19 | -36.66%        | 4.38%          |                 0.89 |
| high_conf_voltarget   | out_of_sample | 4.50%        | 32.85%    |     0.14 | -16.94%        | -0.80%         |                 0.89 |
| conviction_long_short | full          | -12.91%      | 23.53%    |    -0.55 | -41.56%        | -37.95%        |                 0.97 |
| conviction_long_short | out_of_sample | -10.29%      | 26.83%    |    -0.38 | -21.15%        | -13.75%        |                 0.97 |
| spy_buyhold           | full          | 6.69%        | 13.40%    |     0.5  | -17.81%        | 19.24%         |                 0.79 |
| spy_buyhold           | out_of_sample | -4.91%       | 10.12%    |    -0.49 | -14.58%        | -5.61%         |                 0.79 |
| sixty_forty           | full          | 3.94%        | 8.49%     |     0.46 | -10.80%        | 11.48%         |                 0.79 |
| sixty_forty           | out_of_sample | -4.07%       | 6.57%     |    -0.62 | -9.86%         | -4.45%         |                 0.79 |

## Walk-Forward Robustness

Each book measured across contiguous time folds (each a different regime). A book has durable edge only if `mean_sharpe` is positive, `min_sharpe` isn't deeply negative, and `pct_positive_folds` is high — a single great fold doesn't count. `fold_sharpes` lists each fold oldest-to-newest.

| strategy              |   n_folds |   mean_sharpe |   median_sharpe |   min_sharpe | pct_positive_folds   | mean_return   | fold_sharpes                  |
|:----------------------|----------:|--------------:|----------------:|-------------:|:---------------------|:--------------|:------------------------------|
| equal_weight_buyhold  |         5 |          0.06 |            0.15 |        -1.37 | 60.00%               | -6.10%        | 1.63;-1.37;0.53;-0.66;0.15    |
| all_signals_ew        |         5 |         -0.31 |            0.04 |        -1.3  | 60.00%               | -8.10%        | 0.04;0.08;-1.30;-0.51;0.13    |
| high_conf_ew          |         5 |          0.32 |            0.46 |        -1    | 80.00%               | 0.85%         | 1.15;0.66;-1.00;0.46;0.34     |
| high_conf_voltarget   |         5 |          0.47 |            0.5  |        -1.13 | 80.00%               | 1.97%         | 2.05;0.89;-1.13;0.50;0.05     |
| conviction_long_short |         5 |         -0.61 |           -0.52 |        -1.6  | 0.00%                | -8.96%        | -1.60;-0.13;-0.52;-0.15;-0.64 |
| spy_buyhold           |         5 |          0.43 |            0.3  |        -0.24 | 60.00%               | 3.73%         | 1.61;0.30;0.64;-0.17;-0.24    |
| sixty_forty           |         5 |          0.38 |            0.04 |        -0.45 | 60.00%               | 2.28%         | 1.79;0.04;0.66;-0.12;-0.45    |

## Strategy Comparison

Each decision rule backtested over the same data. `out_of_sample` is the most recent ~35% of each symbol's history (unseen tail). A rule has real edge only if `median_excess` and `beat_benchmark_pct` stay positive out-of-sample, not just full-sample.

| strategy        | scope         |   symbols | beat_benchmark_pct   | positive_pct   | median_return   | median_benchmark   | median_excess   |   median_sharpe |   total_trades |
|:----------------|:--------------|----------:|:---------------------|:---------------|:----------------|:-------------------|:----------------|----------------:|---------------:|
| trend           | full          |       160 | 36.25%               | 34.38%         | -9.22%          | 13.57%             | -25.73%         |           -0.07 |          11236 |
| trend           | out_of_sample |       160 | 42.50%               | 53.75%         | 2.01%           | 3.07%              | -4.42%          |            0.26 |           3906 |
| mean_reversion  | full          |       157 | 42.04%               | 49.68%         | -0.03%          | 12.86%             | -16.09%         |            0.01 |           1256 |
| mean_reversion  | out_of_sample |       127 | 47.24%               | 58.27%         | 0.33%           | -1.00%             | -1.19%          |            0.65 |            478 |
| regime_adaptive | full          |       160 | 36.88%               | 35.00%         | -8.95%          | 13.57%             | -26.50%         |           -0.08 |          11503 |
| regime_adaptive | out_of_sample |       160 | 42.50%               | 54.37%         | 2.03%           | 3.07%              | -4.94%          |            0.26 |           4003 |

## Signal Calibration

Realized forward return in the signal's direction, grouped by confidence. HIGH should outrank LOW for the confidence score to be meaningful.

| confidence_level   |   horizon |     n | mean_return   | median_return   | win_rate   |
|:-------------------|----------:|------:|:--------------|:----------------|:-----------|
| HIGH               |         5 |  8056 | 0.18%         | 0.13%           | 52.15%     |
| MEDIUM             |         5 | 29247 | 0.08%         | 0.11%           | 51.22%     |
| LOW                |         5 |  3285 | -0.62%        | -0.53%          | 44.75%     |
| ALL                |         5 | 40588 | 0.05%         | 0.07%           | 50.88%     |
| HIGH               |        10 |  8014 | 0.49%         | 0.17%           | 52.00%     |
| MEDIUM             |        10 | 29056 | 0.26%         | 0.18%           | 51.47%     |
| LOW                |        10 |  3269 | -0.91%        | -0.74%          | 45.15%     |
| ALL                |        10 | 40339 | 0.21%         | 0.12%           | 51.06%     |
| HIGH               |        20 |  7944 | 0.85%         | 0.42%           | 53.35%     |
| MEDIUM             |        20 | 28661 | 0.93%         | 0.66%           | 53.82%     |
| LOW                |        20 |  3232 | -0.63%        | -0.49%          | 47.25%     |
| ALL                |        20 | 39837 | 0.79%         | 0.54%           | 53.19%     |

## Backtest Summary

### Data Quality / Signal Availability

- **ok**: 160 symbols

| symbol     |   trades | return   | benchmark_return   | mdd     |   sharpe | exposure   | skipped_reason   |
|:-----------|---------:|:---------|:-------------------|:--------|---------:|:-----------|:-----------------|
| AAPL       |       63 | 11.48%   | 55.42%             | -20.65% |     0.33 | 48.42%     | ok               |
| AAVE-USD   |       74 | -54.45%  | -72.40%            | -68.26% |    -0.55 | 36.78%     | ok               |
| ABBV       |       64 | -19.31%  | 43.45%             | -30.55% |    -0.41 | 47.25%     | ok               |
| ADA-USD    |       86 | -83.24%  | -83.55%            | -89.69% |    -0.68 | 46.36%     | ok               |
| ADBE       |       68 | -26.98%  | -65.74%            | -37.27% |    -0.31 | 57.40%     | ok               |
| AGG        |       69 | -6.61%   | 0.55%              | -10.16% |    -1.1  | 31.11%     | ok               |
| ALGO-USD   |       86 | -50.43%  | -78.09%            | -53.13% |    -0.57 | 38.12%     | ok               |
| AMAT       |       69 | -12.00%  | 280.87%            | -57.21% |     0.04 | 53.41%     | ok               |
| AMD        |       56 | 4.96%    | 216.42%            | -44.76% |     0.26 | 36.61%     | ok               |
| AMGN       |       69 | -15.57%  | 22.12%             | -34.14% |    -0.29 | 46.42%     | ok               |
| AMZN       |       78 | -37.52%  | 41.73%             | -42.48% |    -1.12 | 38.27%     | ok               |
| APT-USD    |       76 | -30.58%  | -92.22%            | -69.96% |    -0.06 | 43.87%     | ok               |
| ARB-USD    |       68 | -4.78%   | -88.03%            | -62.67% |     0.2  | 39.08%     | ok               |
| ARKK       |       81 | -30.62%  | 73.52%             | -33.21% |    -0.52 | 39.10%     | ok               |
| ATOM-USD   |       92 | -67.52%  | -74.12%            | -73.96% |    -1.11 | 45.40%     | ok               |
| AVAX-USD   |       74 | -34.19%  | -80.48%            | -60.45% |    -0.24 | 39.66%     | ok               |
| AVGO       |       62 | 24.07%   | 193.81%            | -35.76% |     0.43 | 44.09%     | ok               |
| BA         |       67 | 7.60%    | 3.14%              | -30.56% |     0.25 | 49.25%     | ok               |
| BAC        |       78 | -10.15%  | 75.89%             | -26.30% |    -0.2  | 48.09%     | ok               |
| BCH-USD    |       76 | 3.75%    | -49.95%            | -53.87% |     0.25 | 48.85%     | ok               |
| BITO       |       78 | 12.10%   | -61.19%            | -42.82% |     0.31 | 41.93%     | ok               |
| BLK        |       75 | -9.61%   | 23.36%             | -24.29% |    -0.22 | 43.26%     | ok               |
| BND        |       65 | -7.32%   | 0.61%              | -9.89%  |    -1.18 | 32.28%     | ok               |
| BONK-USD   |       66 | 59.52%   | -83.73%            | -43.77% |     0.67 | 41.76%     | ok               |
| BTC-USD    |       74 | 8.37%    | -41.38%            | -23.38% |     0.28 | 52.11%     | ok               |
| C          |       83 | -27.62%  | 156.93%            | -38.66% |    -0.54 | 51.75%     | ok               |
| CAT        |       72 | 28.61%   | 206.38%            | -21.02% |     0.54 | 57.07%     | ok               |
| CL         |       60 | 13.61%   | 10.61%             | -14.32% |     0.49 | 46.59%     | ok               |
| CMCSA      |       82 | -39.41%  | -40.92%            | -39.41% |    -1.04 | 43.76%     | ok               |
| COMP-USD   |       91 | -37.38%  | -77.63%            | -58.43% |    -0.21 | 46.36%     | ok               |
| COP        |       73 | -19.97%  | -8.10%             | -43.77% |    -0.34 | 40.93%     | ok               |
| COST       |       60 | 0.80%    | 28.47%             | -29.73% |     0.09 | 45.26%     | ok               |
| CRM        |       67 | -40.04%  | -43.49%            | -40.67% |    -0.84 | 43.59%     | ok               |
| CRV-USD    |       64 | -6.87%   | -72.17%            | -39.89% |     0.16 | 35.63%     | ok               |
| CSCO       |       59 | 26.07%   | 135.10%            | -21.79% |     0.55 | 50.08%     | ok               |
| CVX        |       71 | -11.65%  | 8.91%              | -26.75% |    -0.27 | 41.10%     | ok               |
| DASH-USD   |       63 | -37.83%  | 1.16%              | -64.43% |     0.03 | 31.61%     | ok               |
| DBC        |       58 | -12.57%  | 19.79%             | -25.35% |    -0.43 | 32.78%     | ok               |
| DE         |       72 | -2.16%   | 62.62%             | -25.24% |     0.05 | 46.59%     | ok               |
| DIA        |       60 | -2.48%   | 35.10%             | -12.94% |    -0.1  | 45.42%     | ok               |
| DIS        |       68 | -14.34%  | -3.46%             | -28.17% |    -0.2  | 47.42%     | ok               |
| DOGE-USD   |       78 | -18.46%  | -78.39%            | -62.31% |     0.07 | 50.38%     | ok               |
| DOT-USD    |       92 | -48.52%  | -86.04%            | -61.52% |    -0.38 | 49.23%     | ok               |
| DXY-INDEX  |       38 | -1.33%   | -0.30%             | -6.02%  |    -0.2  | 29.28%     | ok               |
| EEM        |       64 | -9.40%   | 67.75%             | -25.67% |    -0.25 | 43.43%     | ok               |
| EFA        |       60 | -7.84%   | 37.05%             | -13.41% |    -0.27 | 44.93%     | ok               |
| EOG        |       77 | -24.73%  | 14.28%             | -48.13% |    -0.54 | 46.09%     | ok               |
| ETC-USD    |       64 | -35.69%  | -73.02%            | -48.16% |    -0.51 | 31.23%     | ok               |
| ETH-USD    |       64 | 159.87%  | -49.45%            | -30.11% |     1.29 | 45.40%     | ok               |
| EWJ        |       64 | -18.12%  | 39.80%             | -30.73% |    -0.58 | 39.43%     | ok               |
| FCX        |       63 | -28.65%  | 54.41%             | -48.09% |    -0.33 | 45.09%     | ok               |
| FET-USD    |       83 | -21.67%  | -83.90%            | -54.02% |     0.08 | 40.61%     | ok               |
| FIL-USD    |       72 | -35.65%  | -84.08%            | -50.22% |    -0.33 | 33.33%     | ok               |
| FXI        |       44 | -2.41%   | 41.34%             | -23.91% |     0.03 | 29.45%     | ok               |
| GDX        |       60 | 11.28%   | 173.38%            | -34.99% |     0.3  | 48.09%     | ok               |
| GDXJ       |       68 | -23.13%  | 194.44%            | -44.93% |    -0.22 | 46.42%     | ok               |
| GE         |       74 | 25.81%   | 239.21%            | -27.82% |     0.51 | 53.58%     | ok               |
| GLD        |       48 | 27.83%   | 96.60%             | -16.63% |     0.69 | 46.09%     | ok               |
| GOOGL      |       63 | 76.10%   | 148.19%            | -20.41% |     1.14 | 53.58%     | ok               |
| GRT-USD    |       85 | -3.45%   | -89.97%            | -54.83% |     0.19 | 42.72%     | ok               |
| GS         |       76 | -2.38%   | 163.70%            | -22.13% |     0.05 | 52.08%     | ok               |
| HD         |       73 | -4.52%   | -3.27%             | -18.58% |    -0.04 | 43.76%     | ok               |
| HON        |       93 | -26.82%  | 21.21%             | -29.80% |    -0.72 | 52.41%     | ok               |
| HYG        |       79 | -9.05%   | 3.04%              | -9.59%  |    -1.05 | 34.44%     | ok               |
| IBIT       |       32 | 41.71%   | -10.55%            | -18.95% |     0.83 | 32.14%     | ok               |
| IBM        |       78 | 5.05%    | 55.79%             | -27.54% |     0.2  | 49.58%     | ok               |
| ICP-USD    |       83 | -2.66%   | -75.84%            | -55.67% |     0.24 | 38.31%     | ok               |
| IEF        |       76 | -10.90%  | -0.99%             | -11.70% |    -1.54 | 32.78%     | ok               |
| IEMG       |       58 | -5.52%   | 61.45%             | -26.84% |    -0.12 | 43.59%     | ok               |
| INJ-USD    |       77 | -51.80%  | -76.60%            | -76.97% |    -0.47 | 38.70%     | ok               |
| INTC       |       70 | 55.82%   | 196.91%            | -60.60% |     0.62 | 49.25%     | ok               |
| INTU       |       67 | -16.19%  | -58.47%            | -43.77% |    -0.16 | 42.60%     | ok               |
| ITA        |       72 | -0.93%   | 95.04%             | -23.75% |     0.05 | 47.59%     | ok               |
| IWM        |       48 | 9.40%    | 54.91%             | -12.83% |     0.39 | 35.77%     | ok               |
| JNJ        |       72 | 5.12%    | 60.77%             | -17.51% |     0.24 | 50.42%     | ok               |
| JPM        |       73 | -17.56%  | 90.43%             | -33.16% |    -0.41 | 53.91%     | ok               |
| KO         |       49 | 28.93%   | 35.51%             | -8.07%  |     1.03 | 37.77%     | ok               |
| LDO-USD    |       74 | 1.95%    | -87.05%            | -60.93% |     0.29 | 37.93%     | ok               |
| LIN        |       64 | 0.44%    | 28.00%             | -21.53% |     0.08 | 38.60%     | ok               |
| LINK-USD   |       71 | -11.55%  | -69.58%            | -49.35% |     0.12 | 41.76%     | ok               |
| LLY        |       71 | -24.08%  | 64.29%             | -53.34% |    -0.31 | 51.25%     | ok               |
| LRCX       |       80 | -10.17%  | 361.10%            | -63.56% |     0.06 | 46.26%     | ok               |
| LTC-USD    |       66 | -34.00%  | -63.00%            | -53.76% |    -0.29 | 48.47%     | ok               |
| MCD        |       75 | -2.55%   | -6.23%             | -18.81% |    -0.05 | 38.10%     | ok               |
| META       |       72 | -28.58%  | 30.52%             | -38.96% |    -0.48 | 49.25%     | ok               |
| MPC        |       71 | -15.24%  | 56.18%             | -44.76% |    -0.17 | 49.75%     | ok               |
| MRK        |       67 | -30.82%  | -1.65%             | -34.46% |    -0.75 | 45.26%     | ok               |
| MS         |       79 | -17.24%  | 146.35%            | -27.79% |    -0.36 | 49.58%     | ok               |
| MSFT       |       81 | -36.45%  | -7.19%             | -37.42% |    -0.95 | 47.92%     | ok               |
| MU         |       51 | 270.20%  | 1112.02%           | -68.76% |     1.34 | 59.90%     | ok               |
| NEAR-USD   |       87 | 3.87%    | -59.85%            | -60.07% |     0.29 | 42.15%     | ok               |
| NEM        |       74 | -31.05%  | 177.27%            | -38.49% |    -0.33 | 53.58%     | ok               |
| NFLX       |       62 | 37.22%   | 32.65%             | -21.09% |     0.76 | 54.74%     | ok               |
| NKE        |       91 | -48.19%  | -58.51%            | -57.25% |    -0.9  | 43.59%     | ok               |
| NOW        |       80 | 7.87%    | -33.07%            | -30.25% |     0.26 | 45.92%     | ok               |
| NVDA       |       76 | -26.19%  | 124.50%            | -45.02% |    -0.19 | 58.29%     | ok               |
| OP-USD     |       72 | -7.69%   | -93.44%            | -70.27% |     0.17 | 34.87%     | ok               |
| ORCL       |       74 | 89.73%   | 21.51%             | -29.47% |     0.84 | 53.58%     | ok               |
| OXY        |       63 | 11.64%   | -16.80%            | -30.85% |     0.31 | 43.76%     | ok               |
| PEP        |       83 | -8.02%   | -17.68%            | -21.35% |    -0.17 | 49.58%     | ok               |
| PEPE-USD   |       79 | 21.65%   | -82.22%            | -57.66% |     0.45 | 44.64%     | ok               |
| PFE        |       79 | -38.68%  | -13.35%            | -40.87% |    -1.24 | 34.94%     | ok               |
| PG         |       64 | -15.30%  | -7.35%             | -21.96% |    -0.56 | 41.43%     | ok               |
| PM         |       85 | -2.45%   | 94.32%             | -33.68% |     0.04 | 57.24%     | ok               |
| POL-USD    |       81 | 76.14%   | -82.65%            | -46.45% |     0.84 | 50.96%     | ok               |
| QCOM       |       75 | -10.63%  | 24.70%             | -56.59% |     0.03 | 46.92%     | ok               |
| QQQ        |       64 | 17.01%   | 67.87%             | -12.88% |     0.5  | 45.26%     | ok               |
| RENDER-USD |       98 | -14.45%  | -63.73%            | -45.00% |     0.15 | 44.06%     | ok               |
| RTX        |       58 | 21.89%   | 108.62%            | -16.99% |     0.57 | 51.58%     | ok               |
| SBUX       |       64 | -21.55%  | 8.48%              | -29.22% |    -0.42 | 39.93%     | ok               |
| SCHW       |       78 | -21.35%  | 53.42%             | -31.92% |    -0.49 | 46.09%     | ok               |
| SHIB-USD   |       78 | -23.81%  | -77.45%            | -47.96% |    -0.08 | 53.45%     | ok               |
| SHY        |       48 | -2.24%   | -0.02%             | -2.85%  |    -0.79 | 34.28%     | ok               |
| SKY-USD    |       70 | -28.56%  | -8.82%             | -43.98% |    -0.35 | 41.14%     | ok               |
| SLB        |       75 | -22.14%  | -4.97%             | -54.95% |    -0.35 | 50.58%     | ok               |
| SLV        |       58 | 48.12%   | 163.55%            | -42.66% |     0.68 | 41.76%     | ok               |
| SMH        |       48 | 90.12%   | 215.55%            | -33.99% |     1.16 | 49.42%     | ok               |
| SNX-USD    |       62 | -12.20%  | -85.64%            | -34.76% |     0.13 | 38.89%     | ok               |
| SOL-USD    |       68 | -37.91%  | -67.01%            | -56.90% |    -0.16 | 59.39%     | ok               |
| SOXX       |       55 | 83.50%   | 196.53%            | -40.34% |     1.05 | 48.42%     | ok               |
| SPY        |       62 | 3.17%    | 49.72%             | -16.47% |     0.17 | 50.08%     | ok               |
| SUSHI-USD  |       92 | -79.40%  | -87.80%            | -84.18% |    -1.18 | 35.82%     | ok               |
| T          |       64 | 45.13%   | 18.18%             | -17.01% |     0.97 | 51.75%     | ok               |
| TGT        |       58 | -14.21%  | -11.20%            | -41.74% |    -0.22 | 38.94%     | ok               |
| TIA-USD    |       90 | -34.81%  | -91.18%            | -64.54% |    -0.15 | 36.02%     | ok               |
| TLT        |       70 | -21.63%  | -9.59%             | -21.79% |    -1.68 | 31.45%     | ok               |
| TMO        |       57 | 10.63%   | -7.06%             | -18.85% |     0.31 | 48.25%     | ok               |
| TMUS       |       70 | 15.73%   | 6.97%              | -24.50% |     0.41 | 47.92%     | ok               |
| TRX-USD    |       74 | -1.76%   | 28.27%             | -22.90% |     0.04 | 49.23%     | ok               |
| TSLA       |       69 | 17.62%   | 126.73%            | -42.22% |     0.37 | 41.43%     | ok               |
| TXN        |       77 | -15.50%  | 87.95%             | -46.98% |    -0.09 | 53.58%     | ok               |
| UNH        |       74 | 30.41%   | -17.88%            | -27.86% |     0.52 | 52.58%     | ok               |
| UNI-USD    |       90 | -73.08%  | -74.50%            | -80.61% |    -0.9  | 42.15%     | ok               |
| UPS        |       74 | -35.53%  | -25.60%            | -38.25% |    -0.7  | 39.93%     | ok               |
| USO        |       66 | 8.43%    | 48.76%             | -43.35% |     0.26 | 34.11%     | ok               |
| VEA        |       58 | -0.98%   | 47.97%             | -17.93% |     0.01 | 44.09%     | ok               |
| VIXY       |       96 | -80.86%  | -61.41%            | -88.16% |    -1.03 | 32.78%     | ok               |
| VNQ        |       75 | -16.77%  | 15.85%             | -24.92% |    -0.7  | 37.60%     | ok               |
| VTI        |       68 | -1.95%   | 49.64%             | -18.77% |    -0.01 | 51.08%     | ok               |
| VWO        |       76 | -13.41%  | 45.58%             | -25.20% |    -0.47 | 44.09%     | ok               |
| VZ         |       89 | -27.45%  | 3.88%              | -27.82% |    -0.93 | 36.94%     | ok               |
| WFC        |       84 | -17.09%  | 77.27%             | -29.78% |    -0.28 | 49.25%     | ok               |
| WIF-USD    |       68 | -43.81%  | -85.76%            | -57.06% |    -0.24 | 32.18%     | ok               |
| WMT        |       59 | 20.12%   | 92.74%             | -21.31% |     0.58 | 50.75%     | ok               |
| XBI        |       62 | 4.15%    | 77.76%             | -19.90% |     0.18 | 40.77%     | ok               |
| XLB        |       66 | -10.84%  | 22.84%             | -26.57% |    -0.36 | 37.10%     | ok               |
| XLC        |       65 | 13.16%   | 39.30%             | -12.33% |     0.47 | 55.57%     | ok               |
| XLE        |       71 | -9.48%   | 26.11%             | -36.18% |    -0.17 | 46.59%     | ok               |
| XLF        |       76 | -10.37%  | 40.03%             | -23.61% |    -0.33 | 48.25%     | ok               |
| XLI        |       64 | 2.09%    | 57.05%             | -11.38% |     0.14 | 45.42%     | ok               |
| XLK        |       42 | 62.54%   | 81.59%             | -14.75% |     1.17 | 46.92%     | ok               |
| XLM-USD    |       69 | 0.26%    | -52.22%            | -50.36% |     0.22 | 45.59%     | ok               |
| XLP        |       68 | 6.56%    | 12.86%             | -11.16% |     0.4  | 42.93%     | ok               |
| XLU        |       67 | -6.16%   | 48.07%             | -20.40% |    -0.25 | 37.60%     | ok               |
| XLV        |       66 | -12.12%  | 10.51%             | -16.83% |    -0.59 | 35.61%     | ok               |
| XLY        |       70 | 3.26%    | 32.80%             | -14.01% |     0.17 | 44.43%     | ok               |
| XOM        |       58 | 4.73%    | 33.32%             | -20.29% |     0.21 | 36.94%     | ok               |
| XRP-USD    |       62 | -31.81%  | -65.63%            | -44.90% |    -0.29 | 34.10%     | ok               |
| YFI-USD    |       81 | -52.55%  | -75.98%            | -67.78% |    -0.75 | 40.80%     | ok               |
| ZEC-USD    |       64 | 60.04%   | 857.14%            | -47.68% |     0.63 | 36.40%     | ok               |

## AAPL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 17.81%   | 55.42%             | -21.71% |     0.43 |       67 | 52.91%     | ok               |
|          15 | 14.19%   | 55.42%             | -23.86% |     0.37 |       74 | 60.07%     | ok               |
|          25 | 12.18%   | 55.42%             | -20.03% |     0.34 |       65 | 50.75%     | ok               |
|          30 | 11.48%   | 55.42%             | -20.65% |     0.33 |       63 | 48.42%     | ok               |
|          35 | 6.37%    | 55.42%             | -22.04% |     0.23 |       63 | 46.26%     | ok               |

## AAVE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 5.46%    | -72.40%            | -43.61% |     0.28 |       38 | 30.08%     | ok               |
|          45 | -1.41%   | -72.40%            | -46.87% |     0.19 |       38 | 25.67%     | ok               |
|          35 | -13.26%  | -72.40%            | -51.96% |     0.07 |       50 | 32.76%     | ok               |
|          50 | -29.26%  | -72.40%            | -43.73% |    -0.28 |       42 | 19.54%     | ok               |
|          15 | -55.36%  | -72.40%            | -61.76% |    -0.39 |       80 | 50.96%     | ok               |

## ABBV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -3.96%   | 43.45%             | -23.80% |    -0.02 |       50 | 36.61%     | ok               |
|          40 | -15.97%  | 43.45%             | -26.61% |    -0.35 |       64 | 41.60%     | ok               |
|          35 | -17.17%  | 43.45%             | -27.83% |    -0.37 |       66 | 44.43%     | ok               |
|          30 | -19.31%  | 43.45%             | -30.55% |    -0.41 |       64 | 47.25%     | ok               |
|          45 | -18.58%  | 43.45%             | -29.59% |    -0.43 |       56 | 38.77%     | ok               |

## ADA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -83.12%  | -83.55%            | -91.83% |    -0.55 |       80 | 63.41%     | ok               |
|          50 | -77.92%  | -83.55%            | -85.97% |    -0.59 |       55 | 26.82%     | ok               |
|          45 | -80.28%  | -83.55%            | -88.02% |    -0.62 |       58 | 31.61%     | ok               |
|          20 | -84.45%  | -83.55%            | -92.33% |    -0.63 |       90 | 57.66%     | ok               |
|          35 | -82.47%  | -83.55%            | -89.77% |    -0.66 |       76 | 42.15%     | ok               |

## ADBE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 4.49%    | -65.74%            | -21.34% |     0.2  |       78 | 49.75%     | ok               |
|          25 | -12.48%  | -65.74%            | -30.47% |    -0.04 |       52 | 61.56%     | ok               |
|          40 | -8.99%   | -65.74%            | -21.60% |    -0.05 |       74 | 42.76%     | ok               |
|          15 | -21.82%  | -65.74%            | -31.45% |    -0.19 |       63 | 66.22%     | ok               |
|          20 | -23.35%  | -65.74%            | -33.63% |    -0.22 |       52 | 63.73%     | ok               |

## AGG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -6.61%   | 0.55%              | -10.16% |    -1.1  |       69 | 31.11%     | ok               |
|          45 | -5.75%   | 0.55%              | -7.89%  |    -1.16 |       52 | 20.47%     | ok               |
|          20 | -8.00%   | 0.55%              | -10.96% |    -1.18 |       73 | 36.61%     | ok               |
|          50 | -5.57%   | 0.55%              | -7.92%  |    -1.25 |       46 | 16.97%     | ok               |
|          25 | -8.17%   | 0.55%              | -11.60% |    -1.25 |       73 | 34.94%     | ok               |

## ALGO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -50.43%  | -78.09%            | -53.13% |    -0.57 |       86 | 38.12%     | ok               |
|          15 | -61.64%  | -78.09%            | -68.50% |    -0.67 |       84 | 50.38%     | ok               |
|          25 | -61.89%  | -78.09%            | -72.48% |    -0.74 |       84 | 45.02%     | ok               |
|          20 | -65.54%  | -78.09%            | -71.20% |    -0.8  |       86 | 48.08%     | ok               |
|          50 | -45.64%  | -78.09%            | -48.43% |    -0.81 |       42 | 16.86%     | ok               |

## AMAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 5.14%    | 280.87%            | -54.05% |     0.25 |       66 | 62.06%     | ok               |
|          30 | -12.00%  | 280.87%            | -57.21% |     0.04 |       69 | 53.41%     | ok               |
|          20 | -18.43%  | 280.87%            | -60.16% |    -0.03 |       72 | 58.57%     | ok               |
|          50 | -16.20%  | 280.87%            | -48.72% |    -0.05 |       52 | 39.27%     | ok               |
|          35 | -18.27%  | 280.87%            | -55.26% |    -0.06 |       71 | 51.25%     | ok               |

## AMD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 4.96%    | 216.42%            | -44.76% |     0.26 |       56 | 36.61%     | ok               |
|          50 | 5.05%    | 216.42%            | -44.44% |     0.25 |       58 | 31.11%     | ok               |
|          35 | -8.42%   | 216.42%            | -54.16% |     0.13 |       62 | 38.60%     | ok               |
|          45 | -16.15%  | 216.42%            | -53.38% |     0.02 |       64 | 33.94%     | ok               |
|          30 | -20.50%  | 216.42%            | -59.51% |    -0    |       63 | 41.10%     | ok               |

## AMGN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -10.00%  | 22.12%             | -26.64% |    -0.13 |       71 | 52.58%     | ok               |
|          15 | -13.18%  | 22.12%             | -27.92% |    -0.19 |       69 | 58.24%     | ok               |
|          35 | -11.49%  | 22.12%             | -31.23% |    -0.19 |       67 | 42.60%     | ok               |
|          30 | -15.57%  | 22.12%             | -34.14% |    -0.29 |       69 | 46.42%     | ok               |
|          25 | -19.01%  | 22.12%             | -33.41% |    -0.37 |       65 | 48.75%     | ok               |

## AMZN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -17.59%  | 41.73%             | -27.15% |    -0.51 |       50 | 29.28%     | ok               |
|          50 | -22.84%  | 41.73%             | -34.08% |    -0.79 |       46 | 23.46%     | ok               |
|          45 | -25.68%  | 41.73%             | -34.08% |    -0.88 |       50 | 26.46%     | ok               |
|          35 | -31.42%  | 41.73%             | -38.29% |    -0.98 |       66 | 32.78%     | ok               |
|          30 | -37.52%  | 41.73%             | -42.48% |    -1.12 |       78 | 38.27%     | ok               |

## APT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 42.94%   | -92.22%            | -46.73% |     0.65 |       44 | 20.31%     | ok               |
|          45 | 8.69%    | -92.22%            | -63.86% |     0.31 |       60 | 26.44%     | ok               |
|          40 | -12.19%  | -92.22%            | -63.33% |     0.1  |       66 | 31.99%     | ok               |
|          20 | -20.82%  | -92.22%            | -70.51% |     0.08 |       73 | 52.68%     | ok               |
|          35 | -18.63%  | -92.22%            | -64.45% |     0.05 |       70 | 37.74%     | ok               |

## ARB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 64.30%   | -88.03%            | -53.74% |     0.69 |       87 | 56.51%     | ok               |
|          40 | 39.22%   | -88.03%            | -47.60% |     0.57 |       50 | 30.08%     | ok               |
|          35 | 25.60%   | -88.03%            | -56.00% |     0.47 |       60 | 33.52%     | ok               |
|          45 | 24.86%   | -88.03%            | -50.83% |     0.46 |       56 | 23.37%     | ok               |
|          20 | 23.47%   | -88.03%            | -60.40% |     0.46 |       75 | 50.00%     | ok               |

## ARKK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -24.32%  | 73.52%             | -34.75% |    -0.28 |       90 | 50.25%     | ok               |
|          20 | -29.40%  | 73.52%             | -35.22% |    -0.42 |       87 | 45.76%     | ok               |
|          30 | -30.62%  | 73.52%             | -33.21% |    -0.52 |       81 | 39.10%     | ok               |
|          35 | -31.81%  | 73.52%             | -34.35% |    -0.58 |       80 | 36.77%     | ok               |
|          40 | -32.66%  | 73.52%             | -34.78% |    -0.64 |       70 | 31.78%     | ok               |

## ATOM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -63.61%  | -74.12%            | -70.52% |    -0.91 |       95 | 51.72%     | ok               |
|          15 | -67.86%  | -74.12%            | -71.82% |    -0.95 |       93 | 61.30%     | ok               |
|          45 | -59.05%  | -74.12%            | -65.47% |    -1.08 |       76 | 29.50%     | ok               |
|          30 | -67.52%  | -74.12%            | -73.96% |    -1.11 |       92 | 45.40%     | ok               |
|          20 | -71.23%  | -74.12%            | -74.51% |    -1.12 |      101 | 55.56%     | ok               |

## AVAX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 15.04%   | -80.48%            | -34.50% |     0.37 |       38 | 19.54%     | ok               |
|          45 | 4.12%    | -80.48%            | -41.07% |     0.23 |       40 | 23.56%     | ok               |
|          15 | -5.39%   | -80.48%            | -52.46% |     0.2  |       67 | 54.02%     | ok               |
|          40 | -10.50%  | -80.48%            | -47.98% |     0.04 |       46 | 26.63%     | ok               |
|          25 | -16.70%  | -80.48%            | -52.93% |     0.04 |       73 | 44.44%     | ok               |

## AVGO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 24.07%   | 193.81%            | -35.76% |     0.43 |       62 | 44.09%     | ok               |
|          35 | 18.10%   | 193.81%            | -36.19% |     0.37 |       70 | 41.26%     | ok               |
|          25 | 17.96%   | 193.81%            | -38.01% |     0.37 |       66 | 44.93%     | ok               |
|          40 | 17.70%   | 193.81%            | -40.70% |     0.37 |       60 | 38.10%     | ok               |
|          50 | 11.89%   | 193.81%            | -35.84% |     0.3  |       62 | 31.95%     | ok               |

## BA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 26.03%   | 3.14%              | -13.34% |     0.67 |       42 | 31.45%     | ok               |
|          35 | 30.46%   | 3.14%              | -23.77% |     0.59 |       72 | 44.59%     | ok               |
|          40 | 20.11%   | 3.14%              | -23.90% |     0.47 |       46 | 38.60%     | ok               |
|          25 | 10.59%   | 3.14%              | -32.48% |     0.29 |       70 | 52.58%     | ok               |
|          30 | 7.60%    | 3.14%              | -30.56% |     0.25 |       67 | 49.25%     | ok               |

## BAC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -3.63%   | 75.89%             | -22.31% |    -0.05 |       60 | 37.10%     | ok               |
|          20 | -6.24%   | 75.89%             | -21.70% |    -0.07 |       80 | 52.75%     | ok               |
|          35 | -5.39%   | 75.89%             | -27.81% |    -0.08 |       70 | 44.26%     | ok               |
|          50 | -5.20%   | 75.89%             | -20.84% |    -0.11 |       58 | 33.94%     | ok               |
|          25 | -8.96%   | 75.89%             | -25.79% |    -0.16 |       80 | 50.75%     | ok               |

## BCH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 3.75%    | -49.95%            | -53.87% |     0.25 |       76 | 48.85%     | ok               |
|          20 | -8.35%   | -49.95%            | -53.95% |     0.15 |       70 | 55.56%     | ok               |
|          15 | -18.83%  | -49.95%            | -60.14% |     0.04 |       78 | 60.15%     | ok               |
|          25 | -19.88%  | -49.95%            | -59.75% |     0.01 |       72 | 51.34%     | ok               |
|          35 | -18.38%  | -49.95%            | -64.08% |    -0.03 |       70 | 45.02%     | ok               |

## BITO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 26.14%   | -61.19%            | -31.98% |     0.47 |       54 | 25.79%     | ok               |
|          30 | 12.10%   | -61.19%            | -42.82% |     0.31 |       78 | 41.93%     | ok               |
|          15 | 5.07%    | -61.19%            | -48.38% |     0.25 |       87 | 50.75%     | ok               |
|          45 | 6.15%    | -61.19%            | -41.16% |     0.24 |       62 | 29.45%     | ok               |
|          25 | 3.23%    | -61.19%            | -41.73% |     0.22 |       82 | 44.93%     | ok               |

## BLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -3.55%   | 23.36%             | -17.97% |    -0.04 |       82 | 39.43%     | ok               |
|          20 | -5.80%   | 23.36%             | -21.48% |    -0.09 |       80 | 47.59%     | ok               |
|          40 | -5.38%   | 23.36%             | -20.08% |    -0.11 |       74 | 35.11%     | ok               |
|          30 | -9.61%   | 23.36%             | -24.29% |    -0.22 |       75 | 43.26%     | ok               |
|          25 | -10.52%  | 23.36%             | -23.36% |    -0.24 |       75 | 45.59%     | ok               |

## BND Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.17%   | 0.61%              | -9.05%  |    -0.9  |       63 | 38.10%     | ok               |
|          25 | -6.87%   | 0.61%              | -10.14% |    -1.05 |       67 | 36.11%     | ok               |
|          30 | -7.32%   | 0.61%              | -9.89%  |    -1.18 |       65 | 32.28%     | ok               |
|          15 | -8.39%   | 0.61%              | -10.58% |    -1.21 |       73 | 40.93%     | ok               |
|          45 | -7.56%   | 0.61%              | -9.57%  |    -1.47 |       50 | 21.96%     | ok               |

## BONK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 170.82%  | -83.73%            | -35.57% |     1.24 |       46 | 22.22%     | ok               |
|          25 | 170.13%  | -83.73%            | -46.61% |     1.04 |       65 | 48.08%     | ok               |
|          20 | 154.87%  | -83.73%            | -54.25% |     0.99 |       66 | 52.68%     | ok               |
|          15 | 160.70%  | -83.73%            | -62.48% |     0.98 |       70 | 57.66%     | ok               |
|          45 | 85.55%   | -83.73%            | -42.36% |     0.84 |       56 | 27.01%     | ok               |

## BTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 57.15%   | -41.38%            | -14.50% |     1.02 |       46 | 34.29%     | ok               |
|          45 | 42.19%   | -41.38%            | -13.36% |     0.83 |       46 | 30.65%     | ok               |
|          35 | 36.20%   | -41.38%            | -22.12% |     0.7  |       70 | 41.38%     | ok               |
|          30 | 19.84%   | -41.38%            | -21.75% |     0.45 |       74 | 48.08%     | ok               |
|          50 | 15.14%   | -41.38%            | -18.05% |     0.42 |       42 | 25.29%     | ok               |

## C Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -8.54%   | 156.93%            | -22.28% |    -0.17 |       66 | 36.44%     | ok               |
|          45 | -15.22%  | 156.93%            | -28.12% |    -0.33 |       78 | 40.60%     | ok               |
|          15 | -24.32%  | 156.93%            | -35.02% |    -0.41 |       74 | 60.23%     | ok               |
|          25 | -24.32%  | 156.93%            | -35.86% |    -0.44 |       73 | 53.74%     | ok               |
|          40 | -21.22%  | 156.93%            | -33.20% |    -0.47 |       82 | 43.09%     | ok               |

## CAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 28.61%   | 206.38%            | -21.02% |     0.54 |       72 | 57.07%     | ok               |
|          25 | 28.73%   | 206.38%            | -26.37% |     0.53 |       68 | 59.90%     | ok               |
|          20 | 26.12%   | 206.38%            | -25.65% |     0.5  |       78 | 63.23%     | ok               |
|          45 | 17.50%   | 206.38%            | -28.85% |     0.4  |       58 | 45.92%     | ok               |
|          15 | 16.34%   | 206.38%            | -30.60% |     0.37 |       71 | 69.22%     | ok               |

## CL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 14.10%   | 10.61%             | -12.98% |     0.6  |       42 | 30.62%     | ok               |
|          30 | 13.61%   | 10.61%             | -14.32% |     0.49 |       60 | 46.59%     | ok               |
|          45 | 8.88%    | 10.61%             | -13.51% |     0.39 |       46 | 33.61%     | ok               |
|          35 | 8.20%    | 10.61%             | -13.83% |     0.33 |       62 | 42.93%     | ok               |
|          40 | 5.06%    | 10.61%             | -12.70% |     0.24 |       56 | 37.60%     | ok               |

## CMCSA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -35.95%  | -40.92%            | -44.41% |    -0.79 |       86 | 58.74%     | ok               |
|          30 | -39.41%  | -40.92%            | -39.41% |    -1.04 |       82 | 43.76%     | ok               |
|          25 | -42.63%  | -40.92%            | -42.63% |    -1.13 |       89 | 48.92%     | ok               |
|          50 | -30.21%  | -40.92%            | -31.36% |    -1.17 |       48 | 15.47%     | ok               |
|          20 | -46.94%  | -40.92%            | -46.94% |    -1.24 |       92 | 54.74%     | ok               |

## COMP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -6.92%   | -77.63%            | -38.71% |     0.11 |       50 | 21.07%     | ok               |
|          25 | -38.52%  | -77.63%            | -60.58% |    -0.2  |       89 | 51.34%     | ok               |
|          30 | -37.38%  | -77.63%            | -58.43% |    -0.21 |       91 | 46.36%     | ok               |
|          15 | -46.69%  | -77.63%            | -65.55% |    -0.28 |      103 | 62.84%     | ok               |
|          40 | -41.77%  | -77.63%            | -47.89% |    -0.38 |       76 | 34.48%     | ok               |

## COP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -11.98%  | -8.10%             | -35.08% |    -0.2  |       50 | 27.45%     | ok               |
|          45 | -16.99%  | -8.10%             | -41.35% |    -0.33 |       62 | 30.62%     | ok               |
|          35 | -19.43%  | -8.10%             | -43.58% |    -0.34 |       75 | 37.77%     | ok               |
|          30 | -19.97%  | -8.10%             | -43.77% |    -0.34 |       73 | 40.93%     | ok               |
|          40 | -23.13%  | -8.10%             | -47.05% |    -0.48 |       70 | 33.61%     | ok               |

## COST Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 11.00%   | 28.47%             | -24.32% |     0.37 |       66 | 51.58%     | ok               |
|          25 | 9.36%    | 28.47%             | -24.73% |     0.33 |       63 | 48.75%     | ok               |
|          35 | 5.63%    | 28.47%             | -26.58% |     0.24 |       54 | 42.26%     | ok               |
|          30 | 0.80%    | 28.47%             | -29.73% |     0.09 |       60 | 45.26%     | ok               |
|          40 | -0.85%   | 28.47%             | -28.41% |     0.04 |       56 | 39.27%     | ok               |

## CRM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -35.50%  | -43.49%            | -43.50% |    -0.56 |       92 | 55.24%     | ok               |
|          35 | -30.20%  | -43.49%            | -35.48% |    -0.6  |       64 | 38.77%     | ok               |
|          30 | -40.04%  | -43.49%            | -40.67% |    -0.84 |       67 | 43.59%     | ok               |
|          40 | -36.50%  | -43.49%            | -41.30% |    -0.85 |       70 | 34.94%     | ok               |
|          20 | -45.01%  | -43.49%            | -45.75% |    -0.87 |       80 | 48.92%     | ok               |

## CRV-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 17.27%   | -72.17%            | -37.78% |     0.39 |       66 | 31.03%     | ok               |
|          45 | -1.09%   | -72.17%            | -42.29% |     0.18 |       54 | 20.69%     | ok               |
|          50 | -0.89%   | -72.17%            | -29.30% |     0.18 |       46 | 17.43%     | ok               |
|          30 | -6.87%   | -72.17%            | -39.89% |     0.16 |       64 | 35.63%     | ok               |
|          40 | -6.61%   | -72.17%            | -38.86% |     0.13 |       58 | 27.01%     | ok               |

## CSCO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 33.52%   | 135.10%            | -19.34% |     0.72 |       56 | 38.77%     | ok               |
|          45 | 32.02%   | 135.10%            | -19.34% |     0.68 |       51 | 41.10%     | ok               |
|          25 | 26.66%   | 135.10%            | -23.28% |     0.56 |       63 | 52.08%     | ok               |
|          35 | 26.06%   | 135.10%            | -23.68% |     0.56 |       51 | 47.59%     | ok               |
|          30 | 26.07%   | 135.10%            | -21.79% |     0.55 |       59 | 50.08%     | ok               |

## CVX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -5.62%   | 8.91%              | -28.32% |    -0.11 |       59 | 31.28%     | ok               |
|          35 | -9.08%   | 8.91%              | -27.83% |    -0.2  |       67 | 37.94%     | ok               |
|          20 | -10.21%  | 8.91%              | -26.07% |    -0.2  |       73 | 45.42%     | ok               |
|          25 | -10.59%  | 8.91%              | -25.65% |    -0.21 |       77 | 44.26%     | ok               |
|          40 | -9.32%   | 8.91%              | -26.30% |    -0.23 |       71 | 34.94%     | ok               |

## DASH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 129.69%  | 1.16%              | -31.38% |     0.96 |       40 | 17.05%     | ok               |
|          40 | 75.62%   | 1.16%              | -34.44% |     0.72 |       46 | 23.75%     | ok               |
|          45 | 65.87%   | 1.16%              | -39.58% |     0.68 |       44 | 19.35%     | ok               |
|          25 | -32.35%  | 1.16%              | -64.14% |     0.1  |       69 | 34.48%     | ok               |
|          35 | -32.14%  | 1.16%              | -63.23% |     0.09 |       69 | 28.16%     | ok               |

## DBC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -10.12%  | 19.79%             | -27.30% |    -0.31 |       71 | 37.60%     | ok               |
|          35 | -9.68%   | 19.79%             | -23.38% |    -0.31 |       60 | 31.61%     | ok               |
|          50 | -8.54%   | 19.79%             | -19.91% |    -0.32 |       42 | 21.13%     | ok               |
|          45 | -9.90%   | 19.79%             | -21.08% |    -0.35 |       54 | 24.46%     | ok               |
|          30 | -12.57%  | 19.79%             | -25.35% |    -0.43 |       58 | 32.78%     | ok               |

## DE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -1.24%   | 62.62%             | -28.94% |     0.07 |       72 | 51.91%     | ok               |
|          30 | -2.16%   | 62.62%             | -25.24% |     0.05 |       72 | 46.59%     | ok               |
|          25 | -3.68%   | 62.62%             | -26.67% |     0.02 |       74 | 49.25%     | ok               |
|          50 | -4.72%   | 62.62%             | -24.93% |    -0.05 |       72 | 31.61%     | ok               |
|          45 | -6.17%   | 62.62%             | -28.13% |    -0.07 |       70 | 35.94%     | ok               |

## DIA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -0.42%   | 35.10%             | -13.15% |     0.01 |       60 | 43.26%     | ok               |
|          25 | -0.96%   | 35.10%             | -11.28% |    -0.01 |       60 | 46.59%     | ok               |
|          30 | -2.48%   | 35.10%             | -12.94% |    -0.1  |       60 | 45.42%     | ok               |
|          20 | -4.35%   | 35.10%             | -13.85% |    -0.19 |       64 | 48.92%     | ok               |
|          40 | -4.45%   | 35.10%             | -15.06% |    -0.22 |       66 | 40.60%     | ok               |

## DIS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 30.08%   | -3.46%             | -14.24% |     0.77 |       50 | 29.28%     | ok               |
|          45 | 2.90%    | -3.46%             | -16.54% |     0.16 |       53 | 32.95%     | ok               |
|          40 | 1.97%    | -3.46%             | -22.77% |     0.14 |       65 | 38.10%     | ok               |
|          15 | -9.23%   | -3.46%             | -31.15% |    -0.06 |       88 | 58.74%     | ok               |
|          35 | -8.22%   | -3.46%             | -25.70% |    -0.07 |       75 | 44.09%     | ok               |

## DOGE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 19.46%   | -78.39%            | -59.36% |     0.44 |       82 | 65.71%     | ok               |
|          20 | 2.00%    | -78.39%            | -57.37% |     0.29 |       85 | 60.92%     | ok               |
|          25 | -2.23%   | -78.39%            | -55.33% |     0.25 |       75 | 55.56%     | ok               |
|          30 | -18.46%  | -78.39%            | -62.31% |     0.07 |       78 | 50.38%     | ok               |
|          35 | -42.62%  | -78.39%            | -61.79% |    -0.33 |       74 | 44.06%     | ok               |

## DOT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -21.12%  | -86.04%            | -46.17% |    -0.14 |       60 | 26.63%     | ok               |
|          45 | -29.29%  | -86.04%            | -53.47% |    -0.26 |       52 | 31.61%     | ok               |
|          20 | -48.79%  | -86.04%            | -65.30% |    -0.32 |       92 | 61.11%     | ok               |
|          30 | -48.52%  | -86.04%            | -61.52% |    -0.38 |       92 | 49.23%     | ok               |
|          35 | -47.51%  | -86.04%            | -63.05% |    -0.38 |       82 | 42.53%     | ok               |

## DXY-INDEX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -1.33%   | -0.30%             | -6.02%  |    -0.2  |       38 | 29.28%     | ok               |
|          40 | -2.56%   | -0.30%             | -7.30%  |    -0.31 |       72 | 49.02%     | ok               |
|          15 | -4.04%   | -0.30%             | -11.37% |    -0.36 |       84 | 76.79%     | ok               |
|          30 | -3.53%   | -0.30%             | -9.61%  |    -0.39 |       70 | 61.39%     | ok               |
|          35 | -4.15%   | -0.30%             | -9.74%  |    -0.49 |       77 | 55.97%     | ok               |

## EEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -4.96%   | 67.75%             | -19.52% |    -0.11 |       64 | 39.77%     | ok               |
|          35 | -5.62%   | 67.75%             | -23.88% |    -0.12 |       66 | 41.76%     | ok               |
|          50 | -4.94%   | 67.75%             | -15.88% |    -0.12 |       52 | 35.77%     | ok               |
|          45 | -6.04%   | 67.75%             | -17.36% |    -0.16 |       54 | 37.44%     | ok               |
|          30 | -9.40%   | 67.75%             | -25.67% |    -0.25 |       64 | 43.43%     | ok               |

## EFA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -3.02%   | 37.05%             | -10.80% |    -0.05 |       62 | 52.41%     | ok               |
|          30 | -7.84%   | 37.05%             | -13.41% |    -0.27 |       60 | 44.93%     | ok               |
|          20 | -9.75%   | 37.05%             | -12.70% |    -0.34 |       69 | 49.42%     | ok               |
|          25 | -10.09%  | 37.05%             | -14.67% |    -0.36 |       62 | 46.92%     | ok               |
|          35 | -11.00%  | 37.05%             | -15.19% |    -0.42 |       60 | 43.93%     | ok               |

## EOG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -19.61%  | 14.28%             | -39.32% |    -0.46 |       54 | 32.45%     | ok               |
|          50 | -20.79%  | 14.28%             | -40.21% |    -0.52 |       58 | 29.62%     | ok               |
|          30 | -24.73%  | 14.28%             | -48.13% |    -0.54 |       77 | 46.09%     | ok               |
|          35 | -25.10%  | 14.28%             | -45.93% |    -0.6  |       75 | 40.93%     | ok               |
|          40 | -24.37%  | 14.28%             | -42.91% |    -0.6  |       62 | 35.77%     | ok               |

## ETC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -7.93%   | -73.02%            | -27.89% |    -0.02 |       28 | 17.05%     | ok               |
|          35 | -15.03%  | -73.02%            | -42.62% |    -0.11 |       44 | 27.01%     | ok               |
|          45 | -16.07%  | -73.02%            | -35.44% |    -0.17 |       26 | 18.97%     | ok               |
|          40 | -21.04%  | -73.02%            | -40.48% |    -0.26 |       42 | 22.80%     | ok               |
|          30 | -35.69%  | -73.02%            | -48.16% |    -0.51 |       64 | 31.23%     | ok               |

## ETH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 159.87%  | -49.45%            | -30.11% |     1.29 |       64 | 45.40%     | ok               |
|          30 | 140.28%  | -49.45%            | -32.89% |     1.15 |       66 | 54.21%     | ok               |
|          40 | 59.16%   | -49.45%            | -33.11% |     0.77 |       60 | 37.93%     | ok               |
|          15 | 47.34%   | -49.45%            | -42.74% |     0.62 |       78 | 69.35%     | ok               |
|          20 | 40.92%   | -49.45%            | -39.10% |     0.58 |       83 | 63.98%     | ok               |

## EWJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -18.12%  | 39.80%             | -30.73% |    -0.58 |       64 | 39.43%     | ok               |
|          20 | -19.51%  | 39.80%             | -31.32% |    -0.62 |       60 | 41.43%     | ok               |
|          45 | -18.91%  | 39.80%             | -27.68% |    -0.72 |       60 | 31.61%     | ok               |
|          25 | -21.83%  | 39.80%             | -31.18% |    -0.72 |       60 | 40.43%     | ok               |
|          35 | -22.05%  | 39.80%             | -32.54% |    -0.75 |       70 | 37.77%     | ok               |

## FCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -3.73%   | 54.41%             | -27.80% |     0.07 |       52 | 29.45%     | ok               |
|          45 | -8.58%   | 54.41%             | -35.28% |    -0    |       52 | 33.78%     | ok               |
|          40 | -20.30%  | 54.41%             | -44.23% |    -0.2  |       62 | 38.44%     | ok               |
|          30 | -28.65%  | 54.41%             | -48.09% |    -0.33 |       63 | 45.09%     | ok               |
|          20 | -34.13%  | 54.41%             | -57.65% |    -0.39 |       70 | 51.91%     | ok               |

## FET-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 25.35%   | -83.90%            | -57.24% |     0.49 |       90 | 50.96%     | ok               |
|          15 | -6.25%   | -83.90%            | -59.58% |     0.28 |       86 | 54.02%     | ok               |
|          25 | -17.99%  | -83.90%            | -57.82% |     0.14 |       93 | 44.64%     | ok               |
|          30 | -21.67%  | -83.90%            | -54.02% |     0.08 |       83 | 40.61%     | ok               |
|          45 | -31.39%  | -83.90%            | -48.61% |    -0.24 |       58 | 19.35%     | ok               |

## FIL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -9.16%   | -84.08%            | -39.40% |     0.05 |       50 | 23.56%     | ok               |
|          45 | -27.58%  | -84.08%            | -43.98% |    -0.29 |       44 | 17.62%     | ok               |
|          35 | -32.45%  | -84.08%            | -47.50% |    -0.3  |       60 | 27.78%     | ok               |
|          50 | -26.52%  | -84.08%            | -44.97% |    -0.32 |       38 | 13.03%     | ok               |
|          30 | -35.65%  | -84.08%            | -50.22% |    -0.33 |       72 | 33.33%     | ok               |

## FXI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -1.85%   | 41.34%             | -22.57% |     0.04 |       44 | 30.62%     | ok               |
|          30 | -2.41%   | 41.34%             | -23.91% |     0.03 |       44 | 29.45%     | ok               |
|          15 | -4.76%   | 41.34%             | -21.68% |    -0.02 |       52 | 33.94%     | ok               |
|          45 | -4.90%   | 41.34%             | -26.75% |    -0.05 |       44 | 24.13%     | ok               |
|          20 | -5.80%   | 41.34%             | -24.53% |    -0.06 |       50 | 31.78%     | ok               |

## GDX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 18.06%   | 173.38%            | -35.59% |     0.39 |       73 | 52.91%     | ok               |
|          40 | 13.85%   | 173.38%            | -31.87% |     0.35 |       64 | 42.93%     | ok               |
|          30 | 11.28%   | 173.38%            | -34.99% |     0.3  |       60 | 48.09%     | ok               |
|          35 | 8.95%    | 173.38%            | -32.37% |     0.27 |       68 | 45.26%     | ok               |
|          25 | 6.77%    | 173.38%            | -38.90% |     0.24 |       63 | 49.75%     | ok               |

## GDXJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -7.90%   | 194.44%            | -45.05% |     0.06 |       67 | 53.24%     | ok               |
|          30 | -23.13%  | 194.44%            | -44.93% |    -0.22 |       68 | 46.42%     | ok               |
|          50 | -20.22%  | 194.44%            | -44.94% |    -0.22 |       58 | 37.77%     | ok               |
|          25 | -26.54%  | 194.44%            | -47.26% |    -0.25 |       72 | 49.92%     | ok               |
|          35 | -26.76%  | 194.44%            | -43.49% |    -0.3  |       70 | 44.09%     | ok               |

## GE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 43.87%   | 239.21%            | -22.29% |     0.8  |       66 | 40.43%     | ok               |
|          45 | 33.01%   | 239.21%            | -25.68% |     0.64 |       74 | 43.26%     | ok               |
|          20 | 32.03%   | 239.21%            | -26.63% |     0.58 |       69 | 57.07%     | ok               |
|          35 | 26.11%   | 239.21%            | -27.11% |     0.52 |       80 | 48.59%     | ok               |
|          40 | 25.15%   | 239.21%            | -26.97% |     0.52 |       76 | 44.76%     | ok               |

## GLD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 34.22%   | 96.60%             | -14.61% |     0.81 |       46 | 47.25%     | ok               |
|          20 | 32.22%   | 96.60%             | -14.61% |     0.77 |       48 | 48.59%     | ok               |
|          30 | 27.83%   | 96.60%             | -16.63% |     0.69 |       48 | 46.09%     | ok               |
|          15 | 24.12%   | 96.60%             | -17.54% |     0.59 |       50 | 52.75%     | ok               |
|          35 | 21.59%   | 96.60%             | -17.29% |     0.57 |       50 | 45.42%     | ok               |

## GOOGL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 80.98%   | 148.19%            | -19.76% |     1.18 |       57 | 56.07%     | ok               |
|          35 | 75.32%   | 148.19%            | -19.34% |     1.16 |       69 | 48.59%     | ok               |
|          30 | 76.10%   | 148.19%            | -20.41% |     1.14 |       63 | 53.58%     | ok               |
|          45 | 62.82%   | 148.19%            | -15.29% |     1.09 |       60 | 41.26%     | ok               |
|          20 | 67.31%   | 148.19%            | -20.57% |     1.03 |       68 | 58.40%     | ok               |

## GRT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 37.41%   | -89.97%            | -35.66% |     0.62 |       44 | 22.03%     | ok               |
|          45 | 21.41%   | -89.97%            | -46.59% |     0.44 |       50 | 27.39%     | ok               |
|          35 | 16.47%   | -89.97%            | -48.22% |     0.39 |       60 | 36.21%     | ok               |
|          15 | 14.49%   | -89.97%            | -49.67% |     0.39 |       75 | 61.88%     | ok               |
|          40 | 16.36%   | -89.97%            | -46.38% |     0.38 |       48 | 30.46%     | ok               |

## GS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 21.11%   | 163.70%            | -20.56% |     0.47 |       74 | 61.06%     | ok               |
|          20 | 4.59%    | 163.70%            | -23.19% |     0.19 |       74 | 57.07%     | ok               |
|          40 | 0.08%    | 163.70%            | -17.88% |     0.09 |       72 | 45.26%     | ok               |
|          25 | -0.70%   | 163.70%            | -23.32% |     0.09 |       74 | 54.58%     | ok               |
|          30 | -2.38%   | 163.70%            | -22.13% |     0.05 |       76 | 52.08%     | ok               |

## HD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -4.52%   | -3.27%             | -18.58% |    -0.04 |       73 | 43.76%     | ok               |
|          25 | -5.26%   | -3.27%             | -19.40% |    -0.06 |       72 | 45.76%     | ok               |
|          45 | -9.28%   | -3.27%             | -19.30% |    -0.25 |       58 | 28.29%     | ok               |
|          15 | -14.22%  | -3.27%             | -27.26% |    -0.28 |      107 | 54.41%     | ok               |
|          35 | -13.10%  | -3.27%             | -22.43% |    -0.32 |       80 | 39.93%     | ok               |

## HON Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -13.43%  | 21.21%             | -21.17% |    -0.4  |       72 | 31.78%     | ok               |
|          45 | -15.16%  | 21.21%             | -19.99% |    -0.43 |       74 | 36.77%     | ok               |
|          40 | -23.52%  | 21.21%             | -26.29% |    -0.66 |       76 | 41.10%     | ok               |
|          35 | -24.98%  | 21.21%             | -27.37% |    -0.69 |       91 | 47.42%     | ok               |
|          30 | -26.82%  | 21.21%             | -29.80% |    -0.72 |       93 | 52.41%     | ok               |

## HYG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -7.49%   | 3.04%              | -7.49%  |    -0.9  |       70 | 29.62%     | ok               |
|          45 | -8.18%   | 3.04%              | -8.21%  |    -1.02 |       66 | 26.46%     | ok               |
|          30 | -9.05%   | 3.04%              | -9.59%  |    -1.05 |       79 | 34.44%     | ok               |
|          15 | -9.75%   | 3.04%              | -10.10% |    -1.06 |       88 | 41.60%     | ok               |
|          20 | -9.79%   | 3.04%              | -10.39% |    -1.09 |       88 | 39.27%     | ok               |

## IBIT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 71.99%   | -10.55%            | -19.20% |     1.13 |       38 | 39.76%     | ok               |
|          50 | 53.73%   | -10.55%            | -17.37% |     1.08 |       22 | 22.86%     | ok               |
|          45 | 44.32%   | -10.55%            | -17.37% |     0.91 |       26 | 24.29%     | ok               |
|          30 | 41.71%   | -10.55%            | -18.95% |     0.83 |       32 | 32.14%     | ok               |
|          40 | 38.08%   | -10.55%            | -17.78% |     0.81 |       26 | 26.19%     | ok               |

## IBM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 18.40%   | 55.79%             | -28.20% |     0.41 |       92 | 61.90%     | ok               |
|          30 | 5.05%    | 55.79%             | -27.54% |     0.2  |       78 | 49.58%     | ok               |
|          20 | 0.42%    | 55.79%             | -34.12% |     0.12 |       76 | 54.24%     | ok               |
|          35 | 0.47%    | 55.79%             | -27.54% |     0.11 |       74 | 45.09%     | ok               |
|          50 | -3.42%   | 55.79%             | -22.50% |     0.01 |       54 | 32.45%     | ok               |

## ICP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 18.84%   | -75.84%            | -32.85% |     0.4  |       60 | 26.63%     | ok               |
|          35 | 7.56%    | -75.84%            | -46.18% |     0.3  |       70 | 32.18%     | ok               |
|          30 | -2.66%   | -75.84%            | -55.67% |     0.24 |       83 | 38.31%     | ok               |
|          50 | 3.52%    | -75.84%            | -43.65% |     0.23 |       42 | 16.48%     | ok               |
|          45 | -9.93%   | -75.84%            | -40.57% |     0.07 |       60 | 20.69%     | ok               |

## IEF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -7.23%   | -0.99%             | -10.09% |    -0.87 |       70 | 42.10%     | ok               |
|          15 | -7.78%   | -0.99%             | -10.82% |    -0.92 |       69 | 43.59%     | ok               |
|          40 | -8.39%   | -0.99%             | -9.67%  |    -1.31 |       60 | 24.79%     | ok               |
|          45 | -8.07%   | -0.99%             | -9.73%  |    -1.33 |       50 | 22.80%     | ok               |
|          25 | -10.80%  | -0.99%             | -11.49% |    -1.38 |       76 | 39.27%     | ok               |

## IEMG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -0.32%   | 61.45%             | -22.13% |     0.05 |       63 | 42.60%     | ok               |
|          50 | -2.14%   | 61.45%             | -13.91% |    -0.03 |       54 | 34.11%     | ok               |
|          40 | -2.44%   | 61.45%             | -18.43% |    -0.03 |       60 | 39.93%     | ok               |
|          45 | -2.35%   | 61.45%             | -14.92% |    -0.03 |       50 | 36.77%     | ok               |
|          25 | -4.72%   | 61.45%             | -25.58% |    -0.09 |       59 | 45.42%     | ok               |

## INJ-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -9.97%   | -76.60%            | -53.80% |     0.06 |       42 | 22.61%     | ok               |
|          35 | -18.70%  | -76.60%            | -60.42% |     0.01 |       62 | 32.76%     | ok               |
|          50 | -19.76%  | -76.60%            | -49.35% |    -0.1  |       46 | 19.54%     | ok               |
|          40 | -27.04%  | -76.60%            | -57.21% |    -0.15 |       52 | 28.93%     | ok               |
|          25 | -53.83%  | -76.60%            | -81.57% |    -0.46 |       77 | 43.30%     | ok               |

## INTC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 76.11%   | 196.91%            | -49.32% |     0.74 |       60 | 34.28%     | ok               |
|          15 | 83.79%   | 196.91%            | -53.65% |     0.74 |       82 | 61.06%     | ok               |
|          25 | 75.50%   | 196.91%            | -56.41% |     0.72 |       75 | 51.58%     | ok               |
|          40 | 70.33%   | 196.91%            | -55.86% |     0.7  |       68 | 38.60%     | ok               |
|          20 | 72.70%   | 196.91%            | -52.47% |     0.7  |       82 | 56.57%     | ok               |

## INTU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -1.59%   | -58.47%            | -42.82% |     0.09 |       73 | 28.62%     | ok               |
|          45 | -4.95%   | -58.47%            | -44.66% |     0.03 |       71 | 32.78%     | ok               |
|          25 | -13.17%  | -58.47%            | -42.24% |    -0.1  |       66 | 45.26%     | ok               |
|          40 | -11.92%  | -58.47%            | -48.32% |    -0.1  |       71 | 35.94%     | ok               |
|          15 | -14.19%  | -58.47%            | -46.90% |    -0.11 |       81 | 50.75%     | ok               |

## ITA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 2.62%    | 95.04%             | -21.48% |     0.15 |       76 | 37.60%     | ok               |
|          15 | -0.87%   | 95.04%             | -28.17% |     0.06 |       84 | 59.23%     | ok               |
|          30 | -0.93%   | 95.04%             | -23.75% |     0.05 |       72 | 47.59%     | ok               |
|          35 | -3.04%   | 95.04%             | -23.16% |    -0.02 |       76 | 45.92%     | ok               |
|          40 | -4.16%   | 95.04%             | -20.58% |    -0.06 |       78 | 42.43%     | ok               |

## IWM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 9.83%    | 54.91%             | -13.30% |     0.4  |       50 | 36.77%     | ok               |
|          40 | 8.60%    | 54.91%             | -14.08% |     0.39 |       42 | 31.28%     | ok               |
|          30 | 9.40%    | 54.91%             | -12.83% |     0.39 |       48 | 35.77%     | ok               |
|          35 | 8.35%    | 54.91%             | -14.11% |     0.36 |       48 | 33.61%     | ok               |
|          20 | 5.50%    | 54.91%             | -13.83% |     0.25 |       60 | 37.77%     | ok               |

## JNJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 21.03%   | 60.77%             | -10.57% |     0.89 |       56 | 37.27%     | ok               |
|          15 | 14.42%   | 60.77%             | -18.02% |     0.52 |       68 | 56.91%     | ok               |
|          45 | 11.38%   | 60.77%             | -13.35% |     0.5  |       58 | 42.26%     | ok               |
|          20 | 10.54%   | 60.77%             | -17.61% |     0.41 |       72 | 53.58%     | ok               |
|          40 | 8.94%    | 60.77%             | -14.77% |     0.39 |       64 | 46.42%     | ok               |

## JPM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 21.80%   | 90.43%             | -15.90% |     0.71 |       52 | 41.60%     | ok               |
|          45 | 10.23%   | 90.43%             | -21.91% |     0.36 |       54 | 44.59%     | ok               |
|          40 | -4.32%   | 90.43%             | -28.47% |    -0.05 |       66 | 47.09%     | ok               |
|          20 | -11.46%  | 90.43%             | -33.59% |    -0.17 |       84 | 58.40%     | ok               |
|          35 | -9.67%   | 90.43%             | -27.43% |    -0.19 |       72 | 50.75%     | ok               |

## KO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 28.93%   | 35.51%             | -8.07%  |     1.03 |       49 | 37.77%     | ok               |
|          35 | 24.98%   | 35.51%             | -8.07%  |     0.93 |       52 | 36.44%     | ok               |
|          40 | 22.37%   | 35.51%             | -9.28%  |     0.9  |       54 | 33.28%     | ok               |
|          25 | 23.60%   | 35.51%             | -9.37%  |     0.86 |       55 | 40.43%     | ok               |
|          50 | 14.81%   | 35.51%             | -11.40% |     0.68 |       36 | 26.79%     | ok               |

## LDO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 24.99%   | -87.05%            | -46.95% |     0.48 |       81 | 51.92%     | ok               |
|          20 | 13.39%   | -87.05%            | -44.97% |     0.4  |       85 | 47.32%     | ok               |
|          50 | 15.22%   | -87.05%            | -48.04% |     0.37 |       46 | 16.86%     | ok               |
|          30 | 1.95%    | -87.05%            | -60.93% |     0.29 |       74 | 37.93%     | ok               |
|          35 | -0.33%   | -87.05%            | -62.61% |     0.25 |       72 | 31.03%     | ok               |

## LIN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 5.16%    | 28.00%             | -23.68% |     0.23 |       62 | 49.42%     | ok               |
|          25 | 4.87%    | 28.00%             | -22.01% |     0.23 |       61 | 41.43%     | ok               |
|          20 | 2.62%    | 28.00%             | -23.00% |     0.15 |       60 | 44.59%     | ok               |
|          35 | 1.08%    | 28.00%             | -21.18% |     0.1  |       60 | 32.11%     | ok               |
|          30 | 0.44%    | 28.00%             | -21.53% |     0.08 |       64 | 38.60%     | ok               |

## LINK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -11.55%  | -69.58%            | -49.35% |     0.12 |       71 | 41.76%     | ok               |
|          45 | -13.28%  | -69.58%            | -38.11% |     0.05 |       50 | 26.63%     | ok               |
|          50 | -12.86%  | -69.58%            | -36.52% |     0.03 |       40 | 21.26%     | ok               |
|          35 | -24.33%  | -69.58%            | -49.18% |    -0.05 |       59 | 36.78%     | ok               |
|          25 | -34.17%  | -69.58%            | -46.32% |    -0.12 |       70 | 47.32%     | ok               |

## LLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 8.74%    | 64.29%             | -38.23% |     0.27 |       46 | 38.10%     | ok               |
|          15 | 1.58%    | 64.29%             | -48.12% |     0.17 |       63 | 61.90%     | ok               |
|          45 | -3.47%   | 64.29%             | -42.66% |     0.05 |       54 | 41.60%     | ok               |
|          20 | -14.78%  | 64.29%             | -51.34% |    -0.11 |       72 | 56.91%     | ok               |
|          25 | -16.19%  | 64.29%             | -53.47% |    -0.14 |       68 | 54.24%     | ok               |

## LRCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 10.61%   | 361.10%            | -60.45% |     0.3  |       83 | 55.57%     | ok               |
|          50 | 4.24%    | 361.10%            | -50.39% |     0.22 |       80 | 37.44%     | ok               |
|          40 | 1.11%    | 361.10%            | -56.86% |     0.19 |       72 | 43.26%     | ok               |
|          35 | -5.45%   | 361.10%            | -61.76% |     0.12 |       80 | 45.26%     | ok               |
|          20 | -8.19%   | 361.10%            | -67.64% |     0.09 |       87 | 51.25%     | ok               |

## LTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -12.22%  | -63.00%            | -44.78% |    -0    |       56 | 31.80%     | ok               |
|          35 | -22.47%  | -63.00%            | -54.86% |    -0.13 |       66 | 42.91%     | ok               |
|          30 | -34.00%  | -63.00%            | -53.76% |    -0.29 |       66 | 48.47%     | ok               |
|          40 | -31.40%  | -63.00%            | -56.10% |    -0.3  |       58 | 38.12%     | ok               |
|          25 | -36.79%  | -63.00%            | -54.26% |    -0.33 |       74 | 50.96%     | ok               |

## MCD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 2.85%    | -6.23%             | -9.22%  |     0.19 |       42 | 20.63%     | ok               |
|          30 | -2.55%   | -6.23%             | -18.81% |    -0.05 |       75 | 38.10%     | ok               |
|          25 | -3.59%   | -6.23%             | -20.47% |    -0.09 |       75 | 40.77%     | ok               |
|          35 | -7.68%   | -6.23%             | -15.45% |    -0.29 |       67 | 34.44%     | ok               |
|          40 | -7.95%   | -6.23%             | -16.86% |    -0.33 |       71 | 28.79%     | ok               |

## META Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -8.53%   | 30.52%             | -31.03% |    -0.07 |       66 | 38.77%     | ok               |
|          40 | -18.58%  | 30.52%             | -35.11% |    -0.28 |       66 | 41.76%     | ok               |
|          25 | -26.62%  | 30.52%             | -39.84% |    -0.41 |       67 | 52.41%     | ok               |
|          50 | -22.49%  | 30.52%             | -34.00% |    -0.42 |       70 | 34.94%     | ok               |
|          30 | -28.58%  | 30.52%             | -38.96% |    -0.48 |       72 | 49.25%     | ok               |

## MPC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 12.52%   | 56.18%             | -23.96% |     0.34 |       52 | 38.44%     | ok               |
|          45 | 5.38%    | 56.18%             | -25.09% |     0.21 |       58 | 42.10%     | ok               |
|          40 | 3.79%    | 56.18%             | -25.70% |     0.18 |       60 | 44.43%     | ok               |
|          35 | 0.58%    | 56.18%             | -35.90% |     0.13 |       68 | 46.92%     | ok               |
|          30 | -15.24%  | 56.18%             | -44.76% |    -0.17 |       71 | 49.75%     | ok               |

## MRK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -21.85%  | -1.65%             | -30.12% |    -0.41 |       87 | 56.24%     | ok               |
|          25 | -21.47%  | -1.65%             | -31.07% |    -0.44 |       72 | 48.25%     | ok               |
|          20 | -25.32%  | -1.65%             | -29.59% |    -0.54 |       77 | 51.58%     | ok               |
|          45 | -24.26%  | -1.65%             | -26.02% |    -0.65 |       57 | 34.44%     | ok               |
|          50 | -23.92%  | -1.65%             | -25.69% |    -0.69 |       56 | 31.45%     | ok               |

## MS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -4.22%   | 146.35%            | -19.99% |    -0.02 |       70 | 41.10%     | ok               |
|          35 | -10.89%  | 146.35%            | -25.26% |    -0.19 |       74 | 45.76%     | ok               |
|          15 | -15.45%  | 146.35%            | -23.25% |    -0.26 |       78 | 58.40%     | ok               |
|          20 | -15.55%  | 146.35%            | -25.68% |    -0.29 |       82 | 54.58%     | ok               |
|          30 | -17.24%  | 146.35%            | -27.79% |    -0.36 |       79 | 49.58%     | ok               |

## MSFT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -21.47%  | -7.19%             | -25.28% |    -0.59 |       64 | 35.11%     | ok               |
|          50 | -25.85%  | -7.19%             | -28.69% |    -0.77 |       62 | 30.62%     | ok               |
|          35 | -32.73%  | -7.19%             | -33.75% |    -0.86 |       73 | 43.43%     | ok               |
|          40 | -33.53%  | -7.19%             | -34.54% |    -0.93 |       69 | 38.44%     | ok               |
|          25 | -36.86%  | -7.19%             | -37.82% |    -0.94 |       87 | 51.25%     | ok               |

## MU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 421.65%  | 1112.02%           | -61.96% |     1.55 |       48 | 68.05%     | ok               |
|          25 | 334.60%  | 1112.02%           | -67.90% |     1.46 |       49 | 61.73%     | ok               |
|          40 | 287.64%  | 1112.02%           | -64.36% |     1.39 |       56 | 55.41%     | ok               |
|          20 | 297.89%  | 1112.02%           | -67.25% |     1.37 |       55 | 63.89%     | ok               |
|          30 | 270.20%  | 1112.02%           | -68.76% |     1.34 |       51 | 59.90%     | ok               |

## NEAR-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 103.12%  | -59.85%            | -48.01% |     0.99 |       44 | 23.37%     | ok               |
|          50 | 70.90%   | -59.85%            | -53.13% |     0.82 |       38 | 18.39%     | ok               |
|          40 | 60.91%   | -59.85%            | -56.35% |     0.73 |       48 | 27.78%     | ok               |
|          35 | 33.68%   | -59.85%            | -60.50% |     0.53 |       70 | 33.14%     | ok               |
|          15 | 2.00%    | -59.85%            | -54.94% |     0.31 |       89 | 56.13%     | ok               |

## NEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 3.36%    | 177.27%            | -29.41% |     0.22 |       64 | 61.90%     | ok               |
|          20 | -7.70%   | 177.27%            | -30.47% |     0.07 |       74 | 57.40%     | ok               |
|          25 | -21.17%  | 177.27%            | -37.89% |    -0.14 |       70 | 55.24%     | ok               |
|          50 | -25.02%  | 177.27%            | -33.36% |    -0.27 |       58 | 40.43%     | ok               |
|          30 | -31.05%  | 177.27%            | -38.49% |    -0.33 |       74 | 53.58%     | ok               |

## NFLX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 61.96%   | 32.65%             | -11.94% |     1.2  |       46 | 47.25%     | ok               |
|          50 | 48.20%   | 32.65%             | -16.28% |     1.05 |       48 | 39.77%     | ok               |
|          35 | 53.64%   | 32.65%             | -18.30% |     1.03 |       60 | 50.75%     | ok               |
|          45 | 44.45%   | 32.65%             | -15.48% |     0.95 |       52 | 43.59%     | ok               |
|          25 | 42.76%   | 32.65%             | -21.09% |     0.84 |       60 | 57.24%     | ok               |

## NKE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -33.86%  | -58.51%            | -50.44% |    -0.42 |       93 | 52.58%     | ok               |
|          40 | -26.46%  | -58.51%            | -31.19% |    -0.5  |       63 | 30.12%     | ok               |
|          15 | -38.38%  | -58.51%            | -55.52% |    -0.51 |       91 | 56.91%     | ok               |
|          25 | -45.09%  | -58.51%            | -52.84% |    -0.79 |       91 | 48.59%     | ok               |
|          35 | -39.10%  | -58.51%            | -43.08% |    -0.8  |       75 | 37.10%     | ok               |

## NOW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 8.34%    | -33.07%            | -26.36% |     0.27 |       79 | 51.91%     | ok               |
|          30 | 7.87%    | -33.07%            | -30.25% |     0.26 |       80 | 45.92%     | ok               |
|          15 | 2.48%    | -33.07%            | -26.36% |     0.2  |       87 | 55.24%     | ok               |
|          25 | 1.73%    | -33.07%            | -25.70% |     0.19 |       72 | 49.25%     | ok               |
|          35 | 0.90%    | -33.07%            | -29.30% |     0.16 |       81 | 40.60%     | ok               |

## NVDA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -1.32%   | 124.50%            | -35.26% |     0.14 |       70 | 47.59%     | ok               |
|          25 | -3.32%   | 124.50%            | -33.22% |     0.12 |       68 | 50.27%     | ok               |
|          20 | -8.57%   | 124.50%            | -40.59% |     0.06 |       71 | 54.90%     | ok               |
|          35 | -14.66%  | 124.50%            | -41.25% |    -0.08 |       78 | 44.74%     | ok               |
|          50 | -14.29%  | 124.50%            | -40.84% |    -0.11 |       56 | 32.09%     | ok               |

## OP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 59.93%   | -93.44%            | -36.11% |     0.81 |       32 | 12.26%     | ok               |
|          45 | 58.78%   | -93.44%            | -45.76% |     0.75 |       34 | 16.86%     | ok               |
|          40 | 35.66%   | -93.44%            | -53.61% |     0.55 |       48 | 25.29%     | ok               |
|          35 | 12.91%   | -93.44%            | -58.33% |     0.35 |       56 | 28.35%     | ok               |
|          30 | -7.69%   | -93.44%            | -70.27% |     0.17 |       72 | 34.87%     | ok               |

## ORCL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 194.74%  | 21.51%             | -29.32% |     1.24 |       74 | 65.22%     | ok               |
|          25 | 121.10%  | 21.51%             | -27.76% |     0.98 |       75 | 57.74%     | ok               |
|          20 | 117.30%  | 21.51%             | -29.32% |     0.95 |       77 | 60.90%     | ok               |
|          35 | 89.57%   | 21.51%             | -31.95% |     0.85 |       68 | 49.42%     | ok               |
|          30 | 89.73%   | 21.51%             | -29.47% |     0.84 |       74 | 53.58%     | ok               |

## OXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 11.64%   | -16.80%            | -30.85% |     0.31 |       63 | 43.76%     | ok               |
|          35 | 8.22%    | -16.80%            | -30.50% |     0.26 |       68 | 39.27%     | ok               |
|          40 | 5.57%    | -16.80%            | -32.21% |     0.21 |       56 | 35.27%     | ok               |
|          50 | 2.15%    | -16.80%            | -31.07% |     0.15 |       38 | 27.95%     | ok               |
|          25 | -3.81%   | -16.80%            | -40.42% |     0.05 |       71 | 47.25%     | ok               |

## PEP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 12.74%   | -17.68%            | -11.62% |     0.57 |       48 | 27.29%     | ok               |
|          45 | 4.51%    | -17.68%            | -14.22% |     0.23 |       70 | 31.95%     | ok               |
|          40 | -1.65%   | -17.68%            | -18.04% |    -0    |       82 | 38.10%     | ok               |
|          35 | -2.38%   | -17.68%            | -21.42% |    -0.01 |       87 | 42.93%     | ok               |
|          30 | -8.02%   | -17.68%            | -21.35% |    -0.17 |       83 | 49.58%     | ok               |

## PEPE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 21.68%   | -82.22%            | -61.96% |     0.47 |       78 | 60.15%     | ok               |
|          30 | 21.65%   | -82.22%            | -57.66% |     0.45 |       79 | 44.64%     | ok               |
|          35 | 14.71%   | -82.22%            | -51.35% |     0.39 |       64 | 39.27%     | ok               |
|          25 | -0.44%   | -82.22%            | -53.88% |     0.28 |       85 | 49.81%     | ok               |
|          20 | -5.13%   | -82.22%            | -61.13% |     0.26 |       84 | 56.51%     | ok               |

## PFE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -24.63%  | -13.35%            | -25.48% |    -0.91 |       50 | 18.97%     | ok               |
|          35 | -31.80%  | -13.35%            | -34.24% |    -1.03 |       86 | 31.28%     | ok               |
|          50 | -25.91%  | -13.35%            | -26.74% |    -1.06 |       40 | 15.31%     | ok               |
|          40 | -30.46%  | -13.35%            | -31.73% |    -1.08 |       76 | 23.96%     | ok               |
|          30 | -38.68%  | -13.35%            | -40.87% |    -1.24 |       79 | 34.94%     | ok               |

## PG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -3.55%   | -7.35%             | -20.08% |    -0.1  |       54 | 34.78%     | ok               |
|          35 | -6.84%   | -7.35%             | -18.99% |    -0.23 |       62 | 38.27%     | ok               |
|          45 | -12.97%  | -7.35%             | -20.75% |    -0.55 |       54 | 32.28%     | ok               |
|          30 | -15.30%  | -7.35%             | -21.96% |    -0.56 |       64 | 41.43%     | ok               |
|          25 | -16.32%  | -7.35%             | -22.86% |    -0.6  |       74 | 42.60%     | ok               |

## PM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 0.58%    | 94.32%             | -32.20% |     0.11 |       90 | 53.08%     | ok               |
|          20 | -2.02%   | 94.32%             | -31.89% |     0.06 |       89 | 62.23%     | ok               |
|          30 | -2.45%   | 94.32%             | -33.68% |     0.04 |       85 | 57.24%     | ok               |
|          50 | -6.95%   | 94.32%             | -35.70% |    -0.09 |       74 | 42.10%     | ok               |
|          25 | -9.02%   | 94.32%             | -37.05% |    -0.1  |       83 | 59.57%     | ok               |

## POL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 76.14%   | -82.65%            | -46.45% |     0.84 |       81 | 50.96%     | ok               |
|          25 | 79.39%   | -82.65%            | -46.72% |     0.82 |       66 | 58.81%     | ok               |
|          20 | 65.59%   | -82.65%            | -52.88% |     0.74 |       72 | 63.03%     | ok               |
|          15 | 47.77%   | -82.65%            | -58.42% |     0.62 |       74 | 67.82%     | ok               |
|          50 | 18.38%   | -82.65%            | -22.86% |     0.42 |       52 | 20.88%     | ok               |

## QCOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 1.37%    | 24.70%             | -54.50% |     0.19 |       73 | 48.59%     | ok               |
|          35 | 0.80%    | 24.70%             | -50.58% |     0.17 |       79 | 44.43%     | ok               |
|          20 | -2.75%   | 24.70%             | -54.38% |     0.14 |       69 | 51.41%     | ok               |
|          30 | -10.63%  | 24.70%             | -56.59% |     0.03 |       75 | 46.92%     | ok               |
|          15 | -18.91%  | 24.70%             | -57.94% |    -0.07 |       73 | 54.58%     | ok               |

## QQQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 22.02%   | 67.87%             | -12.88% |     0.6  |       59 | 48.25%     | ok               |
|          15 | 22.54%   | 67.87%             | -14.17% |     0.57 |       63 | 53.74%     | ok               |
|          20 | 19.07%   | 67.87%             | -12.98% |     0.52 |       67 | 50.92%     | ok               |
|          30 | 17.01%   | 67.87%             | -12.88% |     0.5  |       64 | 45.26%     | ok               |
|          35 | 5.05%    | 67.87%             | -19.00% |     0.22 |       70 | 41.60%     | ok               |

## RENDER-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 55.42%   | -63.73%            | -43.43% |     0.67 |       86 | 54.12%     | ok               |
|          15 | 37.38%   | -63.73%            | -44.59% |     0.57 |       86 | 57.14%     | ok               |
|          25 | 24.62%   | -63.73%            | -40.60% |     0.49 |       90 | 50.30%     | ok               |
|          30 | -14.45%  | -63.73%            | -45.00% |     0.15 |       98 | 44.06%     | ok               |
|          35 | -27.84%  | -63.73%            | -41.33% |    -0.07 |       84 | 35.61%     | ok               |

## RTX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 28.33%   | 108.62%            | -18.66% |     0.68 |       78 | 56.24%     | ok               |
|          25 | 23.77%   | 108.62%            | -18.59% |     0.6  |       64 | 52.75%     | ok               |
|          50 | 17.99%   | 108.62%            | -18.42% |     0.57 |       60 | 41.93%     | ok               |
|          30 | 21.89%   | 108.62%            | -16.99% |     0.57 |       58 | 51.58%     | ok               |
|          35 | 19.32%   | 108.62%            | -18.00% |     0.57 |       56 | 49.75%     | ok               |

## SBUX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -14.22%  | 8.48%              | -23.55% |    -0.22 |       65 | 42.26%     | ok               |
|          40 | -19.01%  | 8.48%              | -26.97% |    -0.4  |       62 | 34.44%     | ok               |
|          45 | -18.13%  | 8.48%              | -27.26% |    -0.41 |       70 | 29.95%     | ok               |
|          30 | -21.55%  | 8.48%              | -29.22% |    -0.42 |       64 | 39.93%     | ok               |
|          35 | -23.08%  | 8.48%              | -29.75% |    -0.48 |       60 | 37.27%     | ok               |

## SCHW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -0.45%   | 53.42%             | -16.53% |     0.06 |       56 | 33.44%     | ok               |
|          50 | -4.29%   | 53.42%             | -13.28% |    -0.09 |       50 | 30.95%     | ok               |
|          25 | -9.52%   | 53.42%             | -28.76% |    -0.14 |       65 | 48.42%     | ok               |
|          20 | -11.21%  | 53.42%             | -29.24% |    -0.18 |       73 | 51.08%     | ok               |
|          40 | -10.77%  | 53.42%             | -23.35% |    -0.23 |       64 | 36.44%     | ok               |

## SHIB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -0.51%   | -77.45%            | -49.21% |     0.24 |       80 | 69.35%     | ok               |
|          25 | -8.09%   | -77.45%            | -43.85% |     0.15 |       77 | 60.15%     | ok               |
|          20 | -12.53%  | -77.45%            | -46.38% |     0.11 |       79 | 64.56%     | ok               |
|          35 | -11.33%  | -77.45%            | -53.32% |     0.08 |       66 | 47.32%     | ok               |
|          40 | -17.78%  | -77.45%            | -49.96% |    -0.03 |       56 | 39.66%     | ok               |

## SHY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          30 | -2.24%   | -0.02%             | -2.85% |    -0.79 |       48 | 34.28%     | ok               |
|          35 | -2.36%   | -0.02%             | -3.27% |    -0.84 |       50 | 32.45%     | ok               |
|          40 | -2.47%   | -0.02%             | -3.33% |    -0.89 |       50 | 30.62%     | ok               |
|          45 | -2.45%   | -0.02%             | -3.23% |    -0.9  |       48 | 27.45%     | ok               |
|          50 | -2.62%   | -0.02%             | -3.40% |    -1.01 |       44 | 24.63%     | ok               |

## SKY-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -28.56%  | -8.82%             | -43.98% |    -0.35 |       70 | 41.14%     | ok               |
|          15 | -32.92%  | -8.82%             | -56.39% |    -0.35 |       60 | 51.36%     | ok               |
|          25 | -32.22%  | -8.82%             | -48.09% |    -0.4  |       65 | 44.77%     | ok               |
|          20 | -42.55%  | -8.82%             | -58.40% |    -0.59 |       62 | 48.41%     | ok               |
|          35 | -39.77%  | -8.82%             | -49.68% |    -0.7  |       64 | 34.77%     | ok               |

## SLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 25.49%   | -4.97%             | -23.07% |     0.58 |       46 | 36.11%     | ok               |
|          45 | 22.48%   | -4.97%             | -20.46% |     0.55 |       54 | 32.61%     | ok               |
|          50 | -1.66%   | -4.97%             | -28.89% |     0.05 |       50 | 28.29%     | ok               |
|          35 | -6.02%   | -4.97%             | -41.81% |    -0.02 |       74 | 44.09%     | ok               |
|          30 | -22.14%  | -4.97%             | -54.95% |    -0.35 |       75 | 50.58%     | ok               |

## SLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 75.61%   | 163.55%            | -34.10% |     0.92 |       52 | 34.44%     | ok               |
|          45 | 72.83%   | 163.55%            | -31.82% |     0.9  |       56 | 35.27%     | ok               |
|          40 | 70.76%   | 163.55%            | -31.93% |     0.88 |       62 | 37.44%     | ok               |
|          35 | 57.25%   | 163.55%            | -36.89% |     0.76 |       64 | 39.60%     | ok               |
|          30 | 48.12%   | 163.55%            | -42.66% |     0.68 |       58 | 41.76%     | ok               |

## SMH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 115.12%  | 215.55%            | -30.17% |     1.31 |       47 | 52.25%     | ok               |
|          35 | 92.52%   | 215.55%            | -34.36% |     1.19 |       54 | 48.09%     | ok               |
|          25 | 92.38%   | 215.55%            | -32.94% |     1.17 |       46 | 51.08%     | ok               |
|          30 | 90.12%   | 215.55%            | -33.99% |     1.16 |       48 | 49.42%     | ok               |
|          45 | 76.29%   | 215.55%            | -32.75% |     1.11 |       52 | 42.26%     | ok               |

## SNX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 16.73%   | -85.64%            | -43.20% |     0.42 |       73 | 49.04%     | ok               |
|          35 | -2.88%   | -85.64%            | -30.08% |     0.21 |       66 | 31.80%     | ok               |
|          30 | -12.20%  | -85.64%            | -34.76% |     0.13 |       62 | 38.89%     | ok               |
|          15 | -21.38%  | -85.64%            | -44.00% |     0.09 |       83 | 53.64%     | ok               |
|          25 | -17.39%  | -85.64%            | -38.88% |     0.09 |       74 | 43.49%     | ok               |

## SOL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -12.17%  | -67.01%            | -54.68% |     0.11 |       64 | 38.51%     | ok               |
|          25 | -27.49%  | -67.01%            | -53.21% |    -0.03 |       72 | 56.90%     | ok               |
|          35 | -28.53%  | -67.01%            | -61.96% |    -0.06 |       72 | 45.98%     | ok               |
|          15 | -33.19%  | -67.01%            | -59.14% |    -0.08 |       74 | 63.98%     | ok               |
|          20 | -37.91%  | -67.01%            | -56.90% |    -0.16 |       68 | 59.39%     | ok               |

## SOXX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 98.21%   | 196.53%            | -38.67% |     1.16 |       53 | 50.92%     | ok               |
|          25 | 94.42%   | 196.53%            | -39.85% |     1.13 |       51 | 50.58%     | ok               |
|          35 | 88.99%   | 196.53%            | -38.63% |     1.11 |       59 | 45.92%     | ok               |
|          15 | 93.24%   | 196.53%            | -37.72% |     1.08 |       66 | 53.74%     | ok               |
|          30 | 83.50%   | 196.53%            | -40.34% |     1.05 |       55 | 48.42%     | ok               |

## SPY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 14.84%   | 49.72%             | -14.25% |     0.52 |       61 | 53.91%     | ok               |
|          15 | 13.27%   | 49.72%             | -16.80% |     0.47 |       70 | 57.07%     | ok               |
|          25 | 7.69%    | 49.72%             | -15.22% |     0.31 |       61 | 52.91%     | ok               |
|          30 | 3.17%    | 49.72%             | -16.47% |     0.17 |       62 | 50.08%     | ok               |
|          35 | 2.42%    | 49.72%             | -16.72% |     0.15 |       58 | 47.25%     | ok               |

## SUSHI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -23.49%  | -87.80%            | -40.08% |    -0.19 |       52 | 14.75%     | ok               |
|          45 | -55.67%  | -87.80%            | -64.27% |    -0.7  |       56 | 18.20%     | ok               |
|          40 | -58.81%  | -87.80%            | -66.57% |    -0.7  |       63 | 24.71%     | ok               |
|          15 | -76.93%  | -87.80%            | -78.98% |    -0.89 |       89 | 47.13%     | ok               |
|          35 | -71.80%  | -87.80%            | -78.94% |    -0.97 |       78 | 30.27%     | ok               |

## T Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 68.20%   | 18.18%             | -18.13% |     1.27 |       58 | 55.91%     | ok               |
|          25 | 62.98%   | 18.18%             | -17.66% |     1.22 |       60 | 53.74%     | ok               |
|          15 | 59.02%   | 18.18%             | -15.08% |     1.12 |       67 | 59.73%     | ok               |
|          30 | 45.13%   | 18.18%             | -17.01% |     0.97 |       64 | 51.75%     | ok               |
|          35 | 30.20%   | 18.18%             | -14.49% |     0.74 |       66 | 48.25%     | ok               |

## TGT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -10.74%  | -11.20%            | -41.89% |    -0.1  |       81 | 46.42%     | ok               |
|          15 | -13.66%  | -11.20%            | -39.76% |    -0.15 |       71 | 50.92%     | ok               |
|          25 | -13.37%  | -11.20%            | -43.53% |    -0.18 |       63 | 41.60%     | ok               |
|          30 | -14.21%  | -11.20%            | -41.74% |    -0.22 |       58 | 38.94%     | ok               |
|          45 | -12.63%  | -11.20%            | -30.47% |    -0.22 |       52 | 29.28%     | ok               |

## TIA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 13.84%   | -91.18%            | -44.86% |     0.36 |       34 | 11.69%     | ok               |
|          45 | 13.21%   | -91.18%            | -45.43% |     0.34 |       54 | 18.97%     | ok               |
|          35 | 4.46%    | -91.18%            | -42.77% |     0.27 |       68 | 31.03%     | ok               |
|          40 | 4.90%    | -91.18%            | -41.47% |     0.27 |       70 | 26.25%     | ok               |
|          30 | -34.81%  | -91.18%            | -64.54% |    -0.15 |       90 | 36.02%     | ok               |

## TLT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -21.63%  | -9.59%             | -21.79% |    -1.68 |       70 | 31.45%     | ok               |
|          50 | -15.00%  | -9.59%             | -15.73% |    -1.79 |       32 | 14.14%     | ok               |
|          15 | -27.23%  | -9.59%             | -27.66% |    -1.93 |       76 | 39.43%     | ok               |
|          40 | -20.03%  | -9.59%             | -20.03% |    -1.95 |       58 | 20.80%     | ok               |
|          35 | -22.39%  | -9.59%             | -22.39% |    -1.99 |       64 | 25.62%     | ok               |

## TMO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 42.87%   | -7.06%             | -8.17%  |     0.99 |       38 | 30.45%     | ok               |
|          45 | 33.29%   | -7.06%             | -10.13% |     0.78 |       44 | 35.11%     | ok               |
|          40 | 31.32%   | -7.06%             | -9.91%  |     0.73 |       47 | 39.60%     | ok               |
|          35 | 16.19%   | -7.06%             | -14.06% |     0.43 |       57 | 43.93%     | ok               |
|          30 | 10.63%   | -7.06%             | -18.85% |     0.31 |       57 | 48.25%     | ok               |

## TMUS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 16.99%   | 6.97%              | -26.87% |     0.43 |       69 | 59.90%     | ok               |
|          30 | 15.73%   | 6.97%              | -24.50% |     0.41 |       70 | 47.92%     | ok               |
|          20 | 7.54%    | 6.97%              | -25.10% |     0.25 |       73 | 54.08%     | ok               |
|          25 | 6.58%    | 6.97%              | -26.30% |     0.24 |       75 | 50.42%     | ok               |
|          35 | 2.79%    | 6.97%              | -30.40% |     0.16 |       68 | 44.59%     | ok               |

## TRX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 3.96%    | 28.27%             | -18.79% |     0.2  |       54 | 37.36%     | ok               |
|          50 | 0.66%    | 28.27%             | -18.49% |     0.1  |       44 | 31.99%     | ok               |
|          30 | -1.76%   | 28.27%             | -22.90% |     0.04 |       74 | 49.23%     | ok               |
|          35 | -2.57%   | 28.27%             | -21.77% |     0.02 |       70 | 45.98%     | ok               |
|          25 | -3.52%   | 28.27%             | -26.84% |    -0    |       70 | 52.49%     | ok               |

## TSLA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 85.64%   | 126.73%            | -30.67% |     0.91 |       62 | 34.11%     | ok               |
|          45 | 57.27%   | 126.73%            | -31.89% |     0.73 |       66 | 31.45%     | ok               |
|          50 | 48.58%   | 126.73%            | -32.60% |     0.66 |       64 | 29.78%     | ok               |
|          35 | 44.94%   | 126.73%            | -37.58% |     0.61 |       73 | 36.94%     | ok               |
|          30 | 17.62%   | 126.73%            | -42.22% |     0.37 |       69 | 41.43%     | ok               |

## TXN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 13.38%   | 87.95%             | -45.45% |     0.33 |       72 | 35.77%     | ok               |
|          20 | 2.88%    | 87.95%             | -38.98% |     0.19 |       62 | 59.90%     | ok               |
|          15 | 0.75%    | 87.95%             | -39.48% |     0.17 |       65 | 64.06%     | ok               |
|          35 | -5.08%   | 87.95%             | -43.38% |     0.05 |       78 | 50.58%     | ok               |
|          40 | -5.71%   | 87.95%             | -45.67% |     0.04 |       76 | 48.42%     | ok               |

## UNH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 34.22%   | -17.88%            | -36.82% |     0.59 |       52 | 30.62%     | ok               |
|          30 | 30.41%   | -17.88%            | -27.86% |     0.52 |       74 | 52.58%     | ok               |
|          15 | 29.09%   | -17.88%            | -32.14% |     0.5  |       75 | 67.55%     | ok               |
|          35 | 26.86%   | -17.88%            | -29.20% |     0.49 |       66 | 47.42%     | ok               |
|          40 | 22.60%   | -17.88%            | -35.73% |     0.44 |       60 | 42.76%     | ok               |

## UNI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -18.89%  | -74.50%            | -58.49% |    -0.01 |       56 | 26.05%     | ok               |
|          40 | -24.21%  | -74.50%            | -63.75% |    -0.06 |       58 | 31.03%     | ok               |
|          50 | -25.93%  | -74.50%            | -57.60% |    -0.15 |       54 | 21.26%     | ok               |
|          35 | -36.39%  | -74.50%            | -68.71% |    -0.19 |       72 | 36.02%     | ok               |
|          20 | -73.88%  | -74.50%            | -81.22% |    -0.78 |      104 | 52.68%     | ok               |

## UPS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -30.36%  | -25.60%            | -35.58% |    -0.59 |       62 | 33.44%     | ok               |
|          40 | -29.94%  | -25.60%            | -35.75% |    -0.59 |       52 | 27.95%     | ok               |
|          20 | -34.36%  | -25.60%            | -44.52% |    -0.63 |       84 | 48.09%     | ok               |
|          25 | -35.41%  | -25.60%            | -40.93% |    -0.68 |       80 | 44.59%     | ok               |
|          30 | -35.53%  | -25.60%            | -38.25% |    -0.7  |       74 | 39.93%     | ok               |

## USO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 16.31%   | 48.76%             | -33.25% |     0.38 |       48 | 26.62%     | ok               |
|          30 | 8.43%    | 48.76%             | -43.35% |     0.26 |       66 | 34.11%     | ok               |
|          15 | 8.41%    | 48.76%             | -45.94% |     0.26 |       73 | 41.93%     | ok               |
|          20 | 5.29%    | 48.76%             | -45.77% |     0.21 |       74 | 39.27%     | ok               |
|          40 | 4.41%    | 48.76%             | -41.14% |     0.2  |       59 | 29.28%     | ok               |

## VEA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 5.44%    | 47.97%             | -16.28% |     0.25 |       60 | 50.58%     | ok               |
|          20 | 1.19%    | 47.97%             | -17.70% |     0.1  |       61 | 47.92%     | ok               |
|          25 | -0.82%   | 47.97%             | -17.79% |     0.02 |       57 | 46.26%     | ok               |
|          30 | -0.98%   | 47.97%             | -17.93% |     0.01 |       58 | 44.09%     | ok               |
|          35 | -2.09%   | 47.97%             | -16.79% |    -0.03 |       56 | 43.09%     | ok               |

## VIXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -48.04%  | -61.41%            | -69.78% |    -0.43 |       46 | 10.48%     | ok               |
|          45 | -59.37%  | -61.41%            | -75.03% |    -0.61 |       60 | 16.64%     | ok               |
|          40 | -67.66%  | -61.41%            | -80.72% |    -0.74 |       76 | 21.46%     | ok               |
|          35 | -70.62%  | -61.41%            | -84.37% |    -0.76 |       90 | 26.79%     | ok               |
|          15 | -77.15%  | -61.41%            | -89.47% |    -0.77 |      101 | 44.76%     | ok               |

## VNQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -8.60%   | 15.85%             | -19.07% |    -0.37 |       60 | 28.62%     | ok               |
|          50 | -9.03%   | 15.85%             | -17.13% |    -0.41 |       56 | 26.12%     | ok               |
|          25 | -13.12%  | 15.85%             | -22.34% |    -0.51 |       69 | 40.77%     | ok               |
|          40 | -14.13%  | 15.85%             | -24.84% |    -0.62 |       74 | 32.11%     | ok               |
|          20 | -16.52%  | 15.85%             | -23.79% |    -0.64 |       74 | 43.59%     | ok               |

## VTI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 18.76%   | 49.64%             | -13.96% |     0.63 |       64 | 54.91%     | ok               |
|          15 | 12.67%   | 49.64%             | -15.70% |     0.45 |       67 | 57.40%     | ok               |
|          25 | 5.03%    | 49.64%             | -16.10% |     0.23 |       60 | 52.91%     | ok               |
|          30 | -1.95%   | 49.64%             | -18.77% |    -0.01 |       68 | 51.08%     | ok               |
|          40 | -3.92%   | 49.64%             | -20.44% |    -0.09 |       68 | 44.26%     | ok               |

## VWO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -7.30%   | 45.58%             | -21.18% |    -0.25 |       60 | 32.61%     | ok               |
|          15 | -9.03%   | 45.58%             | -24.01% |    -0.26 |       69 | 49.42%     | ok               |
|          20 | -10.06%  | 45.58%             | -26.14% |    -0.31 |       67 | 47.25%     | ok               |
|          40 | -8.98%   | 45.58%             | -23.57% |    -0.31 |       70 | 37.94%     | ok               |
|          45 | -9.11%   | 45.58%             | -23.26% |    -0.33 |       62 | 35.11%     | ok               |

## VZ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -6.80%   | 3.88%              | -12.71% |    -0.19 |       50 | 24.29%     | ok               |
|          45 | -15.16%  | 3.88%              | -19.37% |    -0.49 |       58 | 27.29%     | ok               |
|          35 | -19.60%  | 3.88%              | -19.89% |    -0.63 |       65 | 32.95%     | ok               |
|          25 | -21.97%  | 3.88%              | -24.92% |    -0.64 |       83 | 41.26%     | ok               |
|          40 | -22.33%  | 3.88%              | -22.95% |    -0.77 |       66 | 29.95%     | ok               |

## WFC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -1.40%   | 77.27%             | -18.29% |     0.02 |       58 | 34.11%     | ok               |
|          35 | -7.42%   | 77.27%             | -22.53% |    -0.09 |       79 | 46.09%     | ok               |
|          20 | -14.72%  | 77.27%             | -29.87% |    -0.19 |       79 | 55.24%     | ok               |
|          45 | -10.33%  | 77.27%             | -24.02% |    -0.24 |       66 | 39.10%     | ok               |
|          30 | -17.09%  | 77.27%             | -29.78% |    -0.28 |       84 | 49.25%     | ok               |

## WIF-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 60.65%   | -85.76%            | -46.21% |     0.66 |       71 | 41.38%     | ok               |
|          20 | 54.98%   | -85.76%            | -40.67% |     0.64 |       65 | 38.70%     | ok               |
|          25 | -11.37%  | -85.76%            | -52.41% |     0.2  |       67 | 36.21%     | ok               |
|          50 | -24.32%  | -85.76%            | -41.18% |    -0.22 |       42 | 12.26%     | ok               |
|          30 | -43.81%  | -85.76%            | -57.06% |    -0.24 |       68 | 32.18%     | ok               |

## WMT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 56.94%   | 92.74%             | -9.18%  |     1.5  |       36 | 42.76%     | ok               |
|          50 | 50.56%   | 92.74%             | -12.19% |     1.43 |       30 | 40.60%     | ok               |
|          40 | 47.13%   | 92.74%             | -9.18%  |     1.26 |       40 | 43.93%     | ok               |
|          35 | 44.35%   | 92.74%             | -10.48% |     1.17 |       52 | 48.09%     | ok               |
|          30 | 20.12%   | 92.74%             | -21.31% |     0.58 |       59 | 50.75%     | ok               |

## XBI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 7.52%    | 77.76%             | -16.56% |     0.26 |       62 | 35.44%     | ok               |
|          45 | 6.69%    | 77.76%             | -16.74% |     0.25 |       54 | 32.28%     | ok               |
|          35 | 5.32%    | 77.76%             | -19.52% |     0.21 |       62 | 39.10%     | ok               |
|          30 | 4.15%    | 77.76%             | -19.90% |     0.18 |       62 | 40.77%     | ok               |
|          25 | -0.64%   | 77.76%             | -24.31% |     0.07 |       70 | 42.76%     | ok               |

## XLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -1.55%   | 22.84%             | -20.60% |    -0    |       58 | 31.78%     | ok               |
|          50 | -1.49%   | 22.84%             | -17.40% |    -0.01 |       42 | 27.45%     | ok               |
|          45 | -4.40%   | 22.84%             | -20.61% |    -0.13 |       42 | 28.95%     | ok               |
|          35 | -4.89%   | 22.84%             | -23.62% |    -0.13 |       58 | 35.27%     | ok               |
|          25 | -8.18%   | 22.84%             | -23.73% |    -0.24 |       66 | 40.93%     | ok               |

## XLC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 13.16%   | 39.30%             | -12.33% |     0.47 |       65 | 55.57%     | ok               |
|          25 | 11.03%   | 39.30%             | -12.31% |     0.41 |       62 | 57.40%     | ok               |
|          40 | 8.03%    | 39.30%             | -13.38% |     0.34 |       68 | 48.09%     | ok               |
|          35 | 8.00%    | 39.30%             | -13.38% |     0.33 |       64 | 52.58%     | ok               |
|          20 | 3.23%    | 39.30%             | -13.78% |     0.17 |       70 | 60.07%     | ok               |

## XLE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -1.92%   | 26.11%             | -25.98% |     0.02 |       56 | 36.77%     | ok               |
|          35 | -3.79%   | 26.11%             | -32.17% |    -0.02 |       65 | 44.59%     | ok               |
|          45 | -5.17%   | 26.11%             | -30.88% |    -0.07 |       62 | 39.60%     | ok               |
|          25 | -9.45%   | 26.11%             | -36.16% |    -0.15 |       79 | 49.75%     | ok               |
|          30 | -9.48%   | 26.11%             | -36.18% |    -0.17 |       71 | 46.59%     | ok               |

## XLF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -4.48%   | 40.03%             | -18.01% |    -0.09 |       68 | 53.91%     | ok               |
|          15 | -8.43%   | 40.03%             | -19.58% |    -0.22 |       76 | 56.74%     | ok               |
|          30 | -10.37%  | 40.03%             | -23.61% |    -0.33 |       76 | 48.25%     | ok               |
|          25 | -11.14%  | 40.03%             | -23.22% |    -0.35 |       77 | 50.42%     | ok               |
|          35 | -16.52%  | 40.03%             | -25.31% |    -0.64 |       66 | 44.76%     | ok               |

## XLI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 7.18%    | 57.05%             | -10.61% |     0.31 |       72 | 52.41%     | ok               |
|          20 | 4.38%    | 57.05%             | -12.74% |     0.22 |       63 | 47.92%     | ok               |
|          30 | 2.09%    | 57.05%             | -11.38% |     0.14 |       64 | 45.42%     | ok               |
|          50 | 1.51%    | 57.05%             | -9.25%  |     0.11 |       56 | 34.78%     | ok               |
|          45 | 1.50%    | 57.05%             | -12.27% |     0.11 |       62 | 36.61%     | ok               |

## XLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 82.39%   | 81.59%             | -14.75% |     1.32 |       41 | 52.41%     | ok               |
|          20 | 68.12%   | 81.59%             | -14.75% |     1.19 |       48 | 50.25%     | ok               |
|          25 | 64.69%   | 81.59%             | -14.75% |     1.18 |       42 | 48.09%     | ok               |
|          30 | 62.54%   | 81.59%             | -14.75% |     1.17 |       42 | 46.92%     | ok               |
|          35 | 44.41%   | 81.59%             | -13.61% |     0.94 |       54 | 44.26%     | ok               |

## XLM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 26.14%   | -52.22%            | -38.97% |     0.48 |       44 | 27.39%     | ok               |
|          45 | 22.34%   | -52.22%            | -43.99% |     0.44 |       50 | 31.03%     | ok               |
|          30 | 0.26%    | -52.22%            | -50.36% |     0.22 |       69 | 45.59%     | ok               |
|          40 | -3.03%   | -52.22%            | -43.80% |     0.17 |       49 | 35.25%     | ok               |
|          35 | -8.51%   | -52.22%            | -50.42% |     0.12 |       69 | 41.57%     | ok               |

## XLP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 10.15%   | 12.86%             | -6.85%  |     0.63 |       56 | 34.11%     | ok               |
|          40 | 9.44%    | 12.86%             | -7.77%  |     0.57 |       70 | 38.44%     | ok               |
|          50 | 8.23%    | 12.86%             | -7.01%  |     0.53 |       58 | 31.61%     | ok               |
|          35 | 8.49%    | 12.86%             | -9.73%  |     0.51 |       66 | 41.43%     | ok               |
|          30 | 6.56%    | 12.86%             | -11.16% |     0.4  |       68 | 42.93%     | ok               |

## XLU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 7.94%    | 48.07%             | -11.25% |     0.42 |       48 | 30.12%     | ok               |
|          45 | 5.79%    | 48.07%             | -13.02% |     0.32 |       52 | 30.95%     | ok               |
|          40 | 2.87%    | 48.07%             | -14.36% |     0.18 |       56 | 32.45%     | ok               |
|          35 | -3.12%   | 48.07%             | -18.54% |    -0.1  |       60 | 34.61%     | ok               |
|          30 | -6.16%   | 48.07%             | -20.40% |    -0.25 |       67 | 37.60%     | ok               |

## XLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -12.12%  | 10.51%             | -16.83% |    -0.59 |       66 | 35.61%     | ok               |
|          25 | -13.41%  | 10.51%             | -18.06% |    -0.66 |       68 | 36.94%     | ok               |
|          15 | -17.34%  | 10.51%             | -21.47% |    -0.84 |       79 | 41.76%     | ok               |
|          20 | -17.27%  | 10.51%             | -21.56% |    -0.86 |       73 | 38.60%     | ok               |
|          50 | -14.45%  | 10.51%             | -18.24% |    -0.87 |       54 | 24.29%     | ok               |

## XLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 5.14%    | 32.80%             | -12.94% |     0.23 |       70 | 41.43%     | ok               |
|          30 | 3.26%    | 32.80%             | -14.01% |     0.17 |       70 | 44.43%     | ok               |
|          15 | 1.20%    | 32.80%             | -15.77% |     0.11 |       74 | 51.25%     | ok               |
|          50 | 1.30%    | 32.80%             | -11.79% |     0.1  |       50 | 29.62%     | ok               |
|          40 | -1.91%   | 32.80%             | -16.99% |    -0.01 |       68 | 37.10%     | ok               |

## XOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 5.78%    | 33.32%             | -19.90% |     0.23 |       58 | 37.60%     | ok               |
|          30 | 4.73%    | 33.32%             | -20.29% |     0.21 |       58 | 36.94%     | ok               |
|          50 | 1.92%    | 33.32%             | -21.35% |     0.13 |       46 | 29.95%     | ok               |
|          20 | 1.87%    | 33.32%             | -25.56% |     0.13 |       63 | 40.10%     | ok               |
|          35 | 0.27%    | 33.32%             | -20.93% |     0.08 |       60 | 35.77%     | ok               |

## XRP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -24.83%  | -65.63%            | -46.89% |    -0.14 |       70 | 40.23%     | ok               |
|          40 | -31.81%  | -65.63%            | -44.90% |    -0.29 |       62 | 34.10%     | ok               |
|          30 | -38.93%  | -65.63%            | -56.11% |    -0.36 |       74 | 44.64%     | ok               |
|          45 | -39.45%  | -65.63%            | -46.83% |    -0.45 |       60 | 29.69%     | ok               |
|          50 | -36.16%  | -65.63%            | -39.26% |    -0.49 |       62 | 22.22%     | ok               |

## YFI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -32.83%  | -75.98%            | -52.37% |    -0.46 |       62 | 27.20%     | ok               |
|          45 | -38.27%  | -75.98%            | -54.04% |    -0.66 |       64 | 22.61%     | ok               |
|          35 | -49.34%  | -75.98%            | -64.08% |    -0.73 |       73 | 34.67%     | ok               |
|          30 | -52.55%  | -75.98%            | -67.78% |    -0.75 |       81 | 40.80%     | ok               |
|          50 | -41.48%  | -75.98%            | -51.80% |    -0.84 |       52 | 17.43%     | ok               |

## ZEC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 134.63%  | 857.14%            | -24.66% |     0.94 |       46 | 23.18%     | ok               |
|          35 | 107.78%  | 857.14%            | -44.34% |     0.82 |       54 | 30.84%     | ok               |
|          25 | 75.32%   | 857.14%            | -48.59% |     0.7  |       58 | 39.66%     | ok               |
|          50 | 61.29%   | 857.14%            | -37.62% |     0.64 |       48 | 20.69%     | ok               |
|          30 | 60.04%   | 857.14%            | -47.68% |     0.63 |       64 | 36.40%     | ok               |
