# Market Tracker Backtest Report

_Generated: 2026-07-03T04:16:03+00:00_

## Data Sources

- Crypto: Kraken -> Coinbase -> CoinGecko OHLC -> CoinPaprika fallback chain.
- Stocks / ETFs / indices: Stooq -> Yahoo Finance fallback chain.
- Data rows are generated from real market APIs. Mock OHLCV rows are not generated.

## Data Freshness

- Rows: **92,459**
- Symbols: **161**
- Date range: **2024-02-08** to **2026-07-03**

## Latest Signals

| symbol     | date                |         close |   composite_score | signal   | data_source   |
|:-----------|:--------------------|--------------:|------------------:|:---------|:--------------|
| AAPL       | 2026-07-02 00:00:00 |   308.63      |          40.9167  | LONG     | Yahoo Finance |
| AAVE-USD   | 2026-07-03 00:00:00 |    86.1       |          43.6667  | LONG     | Kraken API    |
| ABBV       | 2026-07-02 00:00:00 |   261.07      |          62.25    | LONG     | Yahoo Finance |
| AMAT       | 2026-07-02 00:00:00 |   603.04      |          61.4167  | LONG     | Yahoo Finance |
| AMZN       | 2026-07-02 00:00:00 |   242.67      |          53.1667  | LONG     | Yahoo Finance |
| BAC        | 2026-07-02 00:00:00 |    58.73      |          56.75    | LONG     | Yahoo Finance |
| C          | 2026-07-02 00:00:00 |   139.97      |          50.5833  | LONG     | Yahoo Finance |
| CAT        | 2026-07-02 00:00:00 |   963.53      |          33.4167  | LONG     | Yahoo Finance |
| DE         | 2026-07-02 00:00:00 |   621.27      |          71.5833  | LONG     | Yahoo Finance |
| DXY-INDEX  | 2026-07-03 00:00:00 |   100.803     |          69.6237  | LONG     | Yahoo Finance |
| GE         | 2026-07-02 00:00:00 |   377.52      |          62.25    | LONG     | Yahoo Finance |
| HD         | 2026-07-02 00:00:00 |   357.9       |          62.25    | LONG     | Yahoo Finance |
| IBM        | 2026-07-02 00:00:00 |   289.52      |          56.0833  | LONG     | Yahoo Finance |
| ITA        | 2026-07-02 00:00:00 |   248.19      |          65.9167  | LONG     | Yahoo Finance |
| JNJ        | 2026-07-02 00:00:00 |   263.04      |          74.0833  | LONG     | Yahoo Finance |
| JPM        | 2026-07-02 00:00:00 |   334.47      |          63.4167  | LONG     | Yahoo Finance |
| MS         | 2026-07-02 00:00:00 |   213.93      |          50.5833  | LONG     | Yahoo Finance |
| PG         | 2026-07-02 00:00:00 |   151.41      |          54.5     | LONG     | Yahoo Finance |
| RTX        | 2026-07-02 00:00:00 |   199.25      |          65.5833  | LONG     | Yahoo Finance |
| SCHW       | 2026-07-02 00:00:00 |    97         |          67.1667  | LONG     | Yahoo Finance |
| SPY        | 2026-07-02 00:00:00 |   744.78      |          35.5833  | LONG     | Yahoo Finance |
| TMO        | 2026-07-02 00:00:00 |   523.44      |          66       | LONG     | Yahoo Finance |
| UNH        | 2026-07-02 00:00:00 |   425.36      |          60.0833  | LONG     | Yahoo Finance |
| UNI-USD    | 2026-07-03 00:00:00 |     3.2068    |          38.3333  | LONG     | Kraken API    |
| VTI        | 2026-07-02 00:00:00 |   368.76      |          35.5833  | LONG     | Yahoo Finance |
| WFC        | 2026-07-02 00:00:00 |    85.51      |          54.8333  | LONG     | Yahoo Finance |
| XBI        | 2026-07-02 00:00:00 |   160.46      |          73.75    | LONG     | Yahoo Finance |
| XLF        | 2026-07-02 00:00:00 |    55.62      |          64.25    | LONG     | Yahoo Finance |
| XLI        | 2026-07-02 00:00:00 |   183.91      |          78.9167  | LONG     | Yahoo Finance |
| XLU        | 2026-07-02 00:00:00 |    45.76      |          65.9167  | LONG     | Yahoo Finance |
| ADA-USD    | 2026-07-03 00:00:00 |     0.166741  |          17.1667  | NEUTRAL  | Kraken API    |
| ADBE       | 2026-07-02 00:00:00 |   219.72      |          -4.58333 | NEUTRAL  | Yahoo Finance |
| AGG        | 2026-07-02 00:00:00 |    98.61      |         -40.0833  | NEUTRAL  | Yahoo Finance |
| ALGO-USD   | 2026-07-03 00:00:00 |     0.0869    |         -40.5     | NEUTRAL  | Kraken API    |
| AMD        | 2026-07-02 00:00:00 |   517.82      |          22       | NEUTRAL  | Yahoo Finance |
| AMGN       | 2026-07-02 00:00:00 |   374.15      |          67.8333  | NEUTRAL  | Yahoo Finance |
| APT-USD    | 2026-07-03 00:00:00 |     0.6166    |         -29.9167  | NEUTRAL  | Kraken API    |
| ARB-USD    | 2026-07-03 00:00:00 |     0.078     |         -42.25    | NEUTRAL  | Kraken API    |
| ARKK       | 2026-07-02 00:00:00 |    81.25      |          41.1667  | NEUTRAL  | Yahoo Finance |
| AVAX-USD   | 2026-07-03 00:00:00 |     6.844     |           4.08333 | NEUTRAL  | Kraken API    |
| AVGO       | 2026-07-02 00:00:00 |   360.45      |         -25.0833  | NEUTRAL  | Yahoo Finance |
| BA         | 2026-07-02 00:00:00 |   226.49      |          37       | NEUTRAL  | Yahoo Finance |
| BCH-USD    | 2026-07-03 00:00:00 |   220.9       |         -10.5833  | NEUTRAL  | Kraken API    |
| BLK        | 2026-07-02 00:00:00 |   995.73      |         -61.5     | NEUTRAL  | Yahoo Finance |
| BND        | 2026-07-02 00:00:00 |    73.11      |         -40.5833  | NEUTRAL  | Yahoo Finance |
| BONK-USD   | 2026-07-03 00:00:00 |     4.399e-06 |         -42.25    | NEUTRAL  | Kraken API    |
| CL         | 2026-07-02 00:00:00 |    95.13      |          66.5     | NEUTRAL  | Yahoo Finance |
| CMCSA      | 2026-07-02 00:00:00 |    23.79      |          12.0833  | NEUTRAL  | Yahoo Finance |
| COST       | 2026-07-02 00:00:00 |   951.67      |         -44.25    | NEUTRAL  | Yahoo Finance |
| CRM        | 2026-07-02 00:00:00 |   166.11      |         -20.25    | NEUTRAL  | Yahoo Finance |
| CRV-USD    | 2026-07-03 00:00:00 |     0.20843   |         -15       | NEUTRAL  | Kraken API    |
| CSCO       | 2026-07-02 00:00:00 |   112.69      |           6.91667 | NEUTRAL  | Yahoo Finance |
| DASH-USD   | 2026-07-03 00:00:00 |    35.247     |         -34.75    | NEUTRAL  | Kraken API    |
| DBC        | 2026-07-02 00:00:00 |    26.57      |         -11.1667  | NEUTRAL  | Yahoo Finance |
| DIA        | 2026-07-02 00:00:00 |   527.88      |          55       | NEUTRAL  | Yahoo Finance |
| DIS        | 2026-07-02 00:00:00 |    99.5       |         -57       | NEUTRAL  | Yahoo Finance |
| EEM        | 2026-07-02 00:00:00 |    65.7       |         -22.3333  | NEUTRAL  | Yahoo Finance |
| EFA        | 2026-07-02 00:00:00 |   104.37      |          24.3333  | NEUTRAL  | Yahoo Finance |
| EOG        | 2026-07-02 00:00:00 |   130.78      |          -9.33333 | NEUTRAL  | Yahoo Finance |
| ETC-USD    | 2026-07-03 00:00:00 |     7.046     |         -43.9167  | NEUTRAL  | Kraken API    |
| ETH-USD    | 2026-07-03 00:00:00 |  1705.01      |         -25.75    | NEUTRAL  | Kraken API    |
| EWJ        | 2026-07-02 00:00:00 |    93.14      |          52.3333  | NEUTRAL  | Yahoo Finance |
| FCX        | 2026-07-02 00:00:00 |    60.97      |         -19.5     | NEUTRAL  | Yahoo Finance |
| FIL-USD    | 2026-07-03 00:00:00 |     0.78      |          -0.5     | NEUTRAL  | Kraken API    |
| GDX        | 2026-07-02 00:00:00 |    78.43      |         -41.1667  | NEUTRAL  | Yahoo Finance |
| GDXJ       | 2026-07-02 00:00:00 |   102.91      |         -27.8333  | NEUTRAL  | Yahoo Finance |
| GOOGL      | 2026-07-02 00:00:00 |   359.91      |          28.6667  | NEUTRAL  | Yahoo Finance |
| GRT-USD    | 2026-07-03 00:00:00 |     0.01879   |         -32.75    | NEUTRAL  | Kraken API    |
| GS         | 2026-07-02 00:00:00 |  1021         |          -3.33333 | NEUTRAL  | Yahoo Finance |
| HON        | 2026-07-02 00:00:00 |   229.86      |          67.8333  | NEUTRAL  | Yahoo Finance |
| HYG        | 2026-07-02 00:00:00 |    79.71      |         -54.25    | NEUTRAL  | Yahoo Finance |
| ICP-USD    | 2026-07-03 00:00:00 |     2.212     |         -31.5833  | NEUTRAL  | Kraken API    |
| IEF        | 2026-07-02 00:00:00 |    94.12      |         -29.5     | NEUTRAL  | Yahoo Finance |
| IEMG       | 2026-07-02 00:00:00 |    79.84      |         -29       | NEUTRAL  | Yahoo Finance |
| INJ-USD    | 2026-07-03 00:00:00 |     4.75      |         -40.5     | NEUTRAL  | Kraken API    |
| INTC       | 2026-07-02 00:00:00 |   120.35      |          15.8333  | NEUTRAL  | Yahoo Finance |
| INTU       | 2026-07-02 00:00:00 |   275.35      |         -23.25    | NEUTRAL  | Yahoo Finance |
| IWM        | 2026-07-02 00:00:00 |   297.58      |          60.6667  | NEUTRAL  | Yahoo Finance |
| KO         | 2026-07-02 00:00:00 |    84.14      |          68.1667  | NEUTRAL  | Yahoo Finance |
| LDO-USD    | 2026-07-03 00:00:00 |     0.261     |         -24.25    | NEUTRAL  | Kraken API    |
| LIN        | 2026-07-02 00:00:00 |   546.64      |          67.8333  | NEUTRAL  | Yahoo Finance |
| LINK-USD   | 2026-07-03 00:00:00 |     7.75683   |         -18.75    | NEUTRAL  | Kraken API    |
| LLY        | 2026-07-02 00:00:00 |  1213.91      |          39.8333  | NEUTRAL  | Yahoo Finance |
| LRCX       | 2026-07-02 00:00:00 |   351.41      |          24.4167  | NEUTRAL  | Yahoo Finance |
| LTC-USD    | 2026-07-03 00:00:00 |    43.17      |         -16.75    | NEUTRAL  | Kraken API    |
| MCD        | 2026-07-02 00:00:00 |   280.63      |         -25.5     | NEUTRAL  | Yahoo Finance |
| META       | 2026-07-02 00:00:00 |   582.9       |         -11       | NEUTRAL  | Yahoo Finance |
| MPC        | 2026-07-02 00:00:00 |   266.35      |          50.5     | NEUTRAL  | Yahoo Finance |
| MRK        | 2026-07-02 00:00:00 |   129.56      |          67.8333  | NEUTRAL  | Yahoo Finance |
| MSFT       | 2026-07-02 00:00:00 |   390.49      |         -11.5833  | NEUTRAL  | Yahoo Finance |
| MU         | 2026-07-02 00:00:00 |   975.56      |          -3.33333 | NEUTRAL  | Yahoo Finance |
| NEAR-USD   | 2026-07-03 00:00:00 |     1.9596    |         -15.5833  | NEUTRAL  | Kraken API    |
| NEM        | 2026-07-02 00:00:00 |    97.04      |         -47.8333  | NEUTRAL  | Yahoo Finance |
| NFLX       | 2026-07-02 00:00:00 |    77.65      |         -18.25    | NEUTRAL  | Yahoo Finance |
| NKE        | 2026-07-02 00:00:00 |    44.09      |         -39.3333  | NEUTRAL  | Yahoo Finance |
| NOW        | 2026-07-02 00:00:00 |   106.32      |          24.1667  | NEUTRAL  | Yahoo Finance |
| OP-USD     | 2026-07-03 00:00:00 |     0.1011    |         -34.75    | NEUTRAL  | Kraken API    |
| PEP        | 2026-07-02 00:00:00 |   144.22      |         -13.8333  | NEUTRAL  | Yahoo Finance |
| PM         | 2026-07-02 00:00:00 |   182.27      |          40.8333  | NEUTRAL  | Yahoo Finance |
| POL-USD    | 2026-07-03 00:00:00 |     0.07331   |         -47.25    | NEUTRAL  | Kraken API    |
| QCOM       | 2026-07-02 00:00:00 |   176.25      |         -24.0833  | NEUTRAL  | Yahoo Finance |
| QQQ        | 2026-07-02 00:00:00 |   712.6       |          -2.66667 | NEUTRAL  | Yahoo Finance |
| SBUX       | 2026-07-02 00:00:00 |   104.27      |          61.1667  | NEUTRAL  | Yahoo Finance |
| SHY        | 2026-07-02 00:00:00 |    81.94      |         -31.75    | NEUTRAL  | Yahoo Finance |
| SKY-USD    | 2026-07-03 00:00:00 |     0.06      |         -10.5833  | NEUTRAL  | Kraken API    |
| SMH        | 2026-07-02 00:00:00 |   592.29      |          -8.08333 | NEUTRAL  | Yahoo Finance |
| SNX-USD    | 2026-07-03 00:00:00 |     0.2366    |         -19.25    | NEUTRAL  | Kraken API    |
| SOL-USD    | 2026-07-03 00:00:00 |    80.64      |          41.0833  | NEUTRAL  | Kraken API    |
| SOXX       | 2026-07-02 00:00:00 |   566.32      |          -6.33333 | NEUTRAL  | Yahoo Finance |
| TGT        | 2026-07-02 00:00:00 |   130.21      |          18.4167  | NEUTRAL  | Yahoo Finance |
| TIA-USD    | 2026-07-03 00:00:00 |     0.3699    |         -26.5833  | NEUTRAL  | Kraken API    |
| TLT        | 2026-07-02 00:00:00 |    85.51      |         -37.3333  | NEUTRAL  | Yahoo Finance |
| TRX-USD    | 2026-07-03 00:00:00 |     0.317243  |         -40.5     | NEUTRAL  | Kraken API    |
| TSLA       | 2026-07-02 00:00:00 |   393.45      |         -24.1667  | NEUTRAL  | Yahoo Finance |
| TXN        | 2026-07-02 00:00:00 |   293.08      |          -4.66667 | NEUTRAL  | Yahoo Finance |
| UPS        | 2026-07-02 00:00:00 |   110.66      |          57.8333  | NEUTRAL  | Yahoo Finance |
| USO        | 2026-07-02 00:00:00 |   103.98      |         -18.5833  | NEUTRAL  | Yahoo Finance |
| VEA        | 2026-07-02 00:00:00 |    70.81      |           2.33333 | NEUTRAL  | Yahoo Finance |
| VIXY       | 2026-07-02 00:00:00 |    21.23      |         -42.6667  | NEUTRAL  | Yahoo Finance |
| VNQ        | 2026-07-02 00:00:00 |    98.02      |          32.5     | NEUTRAL  | Yahoo Finance |
| VWO        | 2026-07-02 00:00:00 |    59.04      |         -16.3333  | NEUTRAL  | Yahoo Finance |
| WIF-USD    | 2026-07-03 00:00:00 |     0.1719    |          -1.91667 | NEUTRAL  | Kraken API    |
| XLB        | 2026-07-02 00:00:00 |    52.01      |          47       | NEUTRAL  | Yahoo Finance |
| XLE        | 2026-07-02 00:00:00 |    53.22      |         -13.1667  | NEUTRAL  | Yahoo Finance |
| XLK        | 2026-07-02 00:00:00 |   180.59      |           4.83333 | NEUTRAL  | Yahoo Finance |
| XLM-USD    | 2026-07-03 00:00:00 |     0.197224  |         -14.5833  | NEUTRAL  | Kraken API    |
| XLP        | 2026-07-02 00:00:00 |    84.99      |          23.8333  | NEUTRAL  | Yahoo Finance |
| XLV        | 2026-07-02 00:00:00 |   163.74      |          53       | NEUTRAL  | Yahoo Finance |
| XLY        | 2026-07-02 00:00:00 |   117.12      |          36.5     | NEUTRAL  | Yahoo Finance |
| XRP-USD    | 2026-07-03 00:00:00 |     1.08973   |         -40.25    | NEUTRAL  | Kraken API    |
| YFI-USD    | 2026-07-03 00:00:00 |  1772.9       |         -22.25    | NEUTRAL  | Kraken API    |
| ZEC-USD    | 2026-07-03 00:00:00 |   426.83      |         -15.5     | NEUTRAL  | Kraken API    |
| ATOM-USD   | 2026-07-03 00:00:00 |     1.5622    |         -47.6667  | SHORT    | Kraken API    |
| BITO       | 2026-07-02 00:00:00 |     8.34      |         -30.75    | SHORT    | Yahoo Finance |
| BTC-USD    | 2026-07-03 00:00:00 | 61384         |         -29       | SHORT    | Kraken API    |
| COMP-USD   | 2026-07-03 00:00:00 |    16.17      |         -31       | SHORT    | Kraken API    |
| COP        | 2026-07-02 00:00:00 |   104.73      |         -43.4167  | SHORT    | Yahoo Finance |
| CVX        | 2026-07-02 00:00:00 |   169.2       |         -43.4167  | SHORT    | Yahoo Finance |
| DOGE-USD   | 2026-07-03 00:00:00 |     0.0747061 |         -34.3333  | SHORT    | Kraken API    |
| DOT-USD    | 2026-07-03 00:00:00 |     0.8515    |         -36.3333  | SHORT    | Kraken API    |
| FET-USD    | 2026-07-03 00:00:00 |     0.1845    |         -31.3333  | SHORT    | Kraken API    |
| FXI        | 2026-07-02 00:00:00 |    31.91      |         -57.0833  | SHORT    | Yahoo Finance |
| GLD        | 2026-07-02 00:00:00 |   378.13      |         -30.75    | SHORT    | Yahoo Finance |
| HBAR-USD   | 2026-07-03 00:00:00 |     0.07145   |         -47.6667  | SHORT    | Kraken API    |
| IBIT       | 2026-07-02 00:00:00 |    34.87      |         -30.75    | SHORT    | Yahoo Finance |
| NVDA       | 2026-07-02 00:00:00 |   194.83      |         -26.5     | SHORT    | Yahoo Finance |
| ORCL       | 2026-07-02 00:00:00 |   140.27      |         -65.5833  | SHORT    | Yahoo Finance |
| OXY        | 2026-07-02 00:00:00 |    48.91      |         -45.4167  | SHORT    | Yahoo Finance |
| PEPE-USD   | 2026-07-03 00:00:00 |     2.46e-06  |         -36.3333  | SHORT    | Kraken API    |
| PFE        | 2026-07-02 00:00:00 |    24.32      |         -45.0833  | SHORT    | Yahoo Finance |
| RENDER-USD | 2026-07-03 00:00:00 |     1.595     |         -31       | SHORT    | Kraken API    |
| SHIB-USD   | 2026-07-03 00:00:00 |     4.253e-06 |         -36.3333  | SHORT    | Kraken API    |
| SLB        | 2026-07-02 00:00:00 |    45.13      |         -45.8333  | SHORT    | Yahoo Finance |
| SLV        | 2026-07-02 00:00:00 |    55.02      |         -52.25    | SHORT    | Yahoo Finance |
| SUSHI-USD  | 2026-07-03 00:00:00 |     0.1599    |         -33       | SHORT    | Kraken API    |
| T          | 2026-07-02 00:00:00 |    20.58      |         -50       | SHORT    | Yahoo Finance |
| TMUS       | 2026-07-02 00:00:00 |   177.52      |         -50.25    | SHORT    | Yahoo Finance |
| VZ         | 2026-07-02 00:00:00 |    42.56      |         -44       | SHORT    | Yahoo Finance |
| WMT        | 2026-07-02 00:00:00 |   111.84      |         -56.9167  | SHORT    | Yahoo Finance |
| XLC        | 2026-07-02 00:00:00 |   109.6       |         -31.25    | SHORT    | Yahoo Finance |
| XOM        | 2026-07-02 00:00:00 |   137.09      |         -40.1667  | SHORT    | Yahoo Finance |

## Edge Summary

- Symbols with trades: **160** of 160
- Beat buy-and-hold: **33.12%** of traded symbols
- Positive return: **35.00%** of traded symbols
- Median strategy return: **-10.12%** (benchmark **15.43%**)
- Median excess vs benchmark: **-28.18%**
- Median Sharpe: **-0.09**
- Median exposure: **44.51%**

> Edge is real only if both _beat buy-and-hold_ and _median excess_ are convincingly positive across many symbols. Treat a single high-return symbol as noise.

## Portfolio Backtest

Actual capital-allocation books (not per-symbol averages). Benchmarks: `equal_weight_buyhold` (whole tracked universe), `spy_buyhold` (100% SPY), and `sixty_forty` (60% SPY / 40% AGG). `high_conf_voltarget` inverse-vol-weights the HIGH-confidence book; `conviction_long_short` is market-neutral. Judge on **Sharpe** and **max_drawdown** out-of-sample, not raw return: a fully-invested long book wins on return in a bull market but carries all the risk.

| strategy              | scope         | ann_return   | ann_vol   |   sharpe | max_drawdown   | total_return   |   avg_gross_exposure |
|:----------------------|:--------------|:-------------|:----------|---------:|:---------------|:---------------|---------------------:|
| equal_weight_buyhold  | full          | -6.65%       | 33.35%    |    -0.2  | -52.54%        | -31.13%        |                 1    |
| equal_weight_buyhold  | out_of_sample | -12.74%      | 34.09%    |    -0.37 | -39.63%        | -17.90%        |                 1    |
| all_signals_ew        | full          | -11.41%      | 28.27%    |    -0.4  | -59.95%        | -37.42%        |                 1    |
| all_signals_ew        | out_of_sample | 8.99%        | 28.59%    |     0.31 | -19.08%        | 5.39%          |                 1    |
| high_conf_ew          | full          | 4.33%        | 32.35%    |     0.13 | -44.36%        | -2.49%         |                 0.89 |
| high_conf_ew          | out_of_sample | 9.09%        | 35.22%    |     0.26 | -17.35%        | 3.28%          |                 0.89 |
| high_conf_voltarget   | full          | 5.98%        | 29.90%    |     0.2  | -36.50%        | 4.98%          |                 0.89 |
| high_conf_voltarget   | out_of_sample | 5.85%        | 32.84%    |     0.18 | -16.94%        | 0.64%          |                 0.89 |
| conviction_long_short | full          | -13.83%      | 23.53%    |    -0.59 | -42.00%        | -39.65%        |                 0.97 |
| conviction_long_short | out_of_sample | -11.22%      | 26.87%    |    -0.42 | -20.87%        | -14.61%        |                 0.97 |
| spy_buyhold           | full          | 6.63%        | 13.40%    |     0.49 | -17.81%        | 19.03%         |                 0.79 |
| spy_buyhold           | out_of_sample | -4.77%       | 10.12%    |    -0.47 | -13.27%        | -5.46%         |                 0.79 |
| sixty_forty           | full          | 3.96%        | 8.49%     |     0.47 | -10.80%        | 11.55%         |                 0.79 |
| sixty_forty           | out_of_sample | -3.89%       | 6.57%     |    -0.59 | -9.26%         | -4.27%         |                 0.79 |

## Walk-Forward Robustness

Each book measured across contiguous time folds (each a different regime). A book has durable edge only if `mean_sharpe` is positive, `min_sharpe` isn't deeply negative, and `pct_positive_folds` is high — a single great fold doesn't count. `fold_sharpes` lists each fold oldest-to-newest.

| strategy              |   n_folds |   mean_sharpe |   median_sharpe |   min_sharpe | pct_positive_folds   | mean_return   | fold_sharpes                  |
|:----------------------|----------:|--------------:|----------------:|-------------:|:---------------------|:--------------|:------------------------------|
| equal_weight_buyhold  |         5 |          0.08 |            0.4  |        -1.26 | 60.00%               | -5.71%        | 1.54;-1.26;0.42;-0.70;0.40    |
| all_signals_ew        |         5 |         -0.35 |           -0.13 |        -1.27 | 20.00%               | -8.43%        | -0.07;0.06;-1.27;-0.37;-0.13  |
| high_conf_ew          |         5 |          0.29 |            0.54 |        -0.99 | 80.00%               | 0.45%         | 1.11;0.61;-0.99;0.54;0.14     |
| high_conf_voltarget   |         5 |          0.46 |            0.58 |        -1.11 | 60.00%               | 2.09%         | 1.98;0.89;-1.11;0.58;-0.05    |
| conviction_long_short |         5 |         -0.66 |           -0.53 |        -1.57 | 0.00%                | -9.46%        | -1.57;-0.31;-0.53;-0.01;-0.88 |
| spy_buyhold           |         5 |          0.43 |            0.37 |        -0.26 | 60.00%               | 3.68%         | 1.57;0.37;0.62;-0.17;-0.26    |
| sixty_forty           |         5 |          0.39 |            0.14 |        -0.45 | 60.00%               | 2.29%         | 1.74;0.14;0.64;-0.13;-0.45    |

## Strategy Comparison

Each decision rule backtested over the same data. `out_of_sample` is the most recent ~35% of each symbol's history (unseen tail). A rule has real edge only if `median_excess` and `beat_benchmark_pct` stay positive out-of-sample, not just full-sample.

| strategy        | scope         |   symbols | beat_benchmark_pct   | positive_pct   | median_return   | median_benchmark   | median_excess   |   median_sharpe |   total_trades |
|:----------------|:--------------|----------:|:---------------------|:---------------|:----------------|:-------------------|:----------------|----------------:|---------------:|
| trend           | full          |       160 | 33.12%               | 35.00%         | -10.12%         | 15.43%             | -28.18%         |           -0.09 |          11251 |
| trend           | out_of_sample |       160 | 40.00%               | 51.88%         | 1.74%           | 4.17%              | -6.30%          |            0.24 |           3898 |
| mean_reversion  | full          |       157 | 40.13%               | 50.32%         | 0.01%           | 15.18%             | -16.96%         |            0.01 |           1260 |
| mean_reversion  | out_of_sample |       127 | 47.24%               | 58.27%         | 0.33%           | 1.19%              | -2.11%          |            0.65 |            474 |
| regime_adaptive | full          |       160 | 33.12%               | 36.25%         | -10.60%         | 15.43%             | -29.06%         |           -0.11 |          11520 |
| regime_adaptive | out_of_sample |       160 | 38.75%               | 51.88%         | 1.99%           | 4.17%              | -6.88%          |            0.24 |           3995 |

## Signal Calibration

Realized forward return in the signal's direction, grouped by confidence. HIGH should outrank LOW for the confidence score to be meaningful.

| confidence_level   |   horizon |     n | mean_return   | median_return   | win_rate   |
|:-------------------|----------:|------:|:--------------|:----------------|:-----------|
| HIGH               |         5 |  8008 | 0.17%         | 0.13%           | 52.17%     |
| MEDIUM             |         5 | 29269 | 0.08%         | 0.10%           | 51.15%     |
| LOW                |         5 |  3293 | -0.61%        | -0.53%          | 44.79%     |
| ALL                |         5 | 40570 | 0.04%         | 0.06%           | 50.83%     |
| HIGH               |        10 |  7967 | 0.47%         | 0.17%           | 52.00%     |
| MEDIUM             |        10 | 29060 | 0.25%         | 0.17%           | 51.40%     |
| LOW                |        10 |  3271 | -0.87%        | -0.73%          | 45.31%     |
| ALL                |        10 | 40298 | 0.20%         | 0.12%           | 51.02%     |
| HIGH               |        20 |  7893 | 0.83%         | 0.41%           | 53.26%     |
| MEDIUM             |        20 | 28694 | 0.91%         | 0.66%           | 53.78%     |
| LOW                |        20 |  3238 | -0.58%        | -0.46%          | 47.47%     |
| ALL                |        20 | 39825 | 0.78%         | 0.53%           | 53.17%     |

## Backtest Summary

### Data Quality / Signal Availability

- **ok**: 160 symbols

| symbol     |   trades | return   | benchmark_return   | mdd     |   sharpe | exposure   | skipped_reason   |
|:-----------|---------:|:---------|:-------------------|:--------|---------:|:-----------|:-----------------|
| AAPL       |       63 | 12.75%   | 63.89%             | -20.65% |     0.35 | 48.25%     | ok               |
| AAVE-USD   |       74 | -53.44%  | -69.71%            | -68.26% |    -0.53 | 36.97%     | ok               |
| ABBV       |       66 | -16.01%  | 49.36%             | -30.55% |    -0.31 | 47.25%     | ok               |
| ADA-USD    |       86 | -83.24%  | -81.80%            | -89.69% |    -0.68 | 46.36%     | ok               |
| ADBE       |       68 | -30.13%  | -64.32%            | -37.38% |    -0.37 | 57.24%     | ok               |
| AGG        |       69 | -6.61%   | 0.97%              | -10.16% |    -1.1  | 31.11%     | ok               |
| ALGO-USD   |       86 | -50.43%  | -76.08%            | -53.13% |    -0.57 | 38.12%     | ok               |
| AMAT       |       69 | -19.88%  | 246.79%            | -57.21% |    -0.07 | 53.41%     | ok               |
| AMD        |       56 | 5.94%    | 205.77%            | -44.76% |     0.27 | 36.44%     | ok               |
| AMGN       |       69 | -15.57%  | 26.90%             | -34.14% |    -0.29 | 46.42%     | ok               |
| AMZN       |       80 | -37.03%  | 42.88%             | -42.48% |    -1.1  | 38.27%     | ok               |
| APT-USD    |       76 | -34.35%  | -91.44%            | -69.96% |    -0.11 | 43.68%     | ok               |
| ARB-USD    |       68 | -11.79%  | -86.82%            | -62.67% |     0.12 | 38.89%     | ok               |
| ARKK       |       83 | -32.73%  | 67.73%             | -35.25% |    -0.56 | 39.77%     | ok               |
| ATOM-USD   |       92 | -67.78%  | -72.48%            | -73.96% |    -1.12 | 45.59%     | ok               |
| AVAX-USD   |       74 | -34.19%  | -78.65%            | -60.45% |    -0.24 | 39.66%     | ok               |
| AVGO       |       62 | 22.35%   | 182.76%            | -35.76% |     0.41 | 43.93%     | ok               |
| BA         |       67 | 7.60%    | 8.25%              | -30.56% |     0.25 | 49.25%     | ok               |
| BAC        |       78 | -11.23%  | 77.32%             | -27.64% |    -0.23 | 48.42%     | ok               |
| BCH-USD    |       76 | 3.75%    | -46.18%            | -53.87% |     0.25 | 48.85%     | ok               |
| BITO       |       78 | 9.21%    | -61.35%            | -42.82% |     0.28 | 42.10%     | ok               |
| BLK        |       77 | -10.03%  | 25.53%             | -24.29% |    -0.24 | 42.93%     | ok               |
| BND        |       65 | -7.32%   | 0.94%              | -9.89%  |    -1.18 | 32.28%     | ok               |
| BONK-USD   |       68 | 69.11%   | -80.92%            | -43.77% |     0.72 | 41.95%     | ok               |
| BTC-USD    |       74 | 5.62%    | -39.40%            | -23.38% |     0.24 | 52.30%     | ok               |
| C          |       83 | -27.37%  | 157.82%            | -38.66% |    -0.53 | 51.75%     | ok               |
| CAT        |       72 | 25.61%   | 199.23%            | -21.02% |     0.5  | 57.07%     | ok               |
| CL         |       60 | 13.07%   | 12.90%             | -14.32% |     0.47 | 46.42%     | ok               |
| CMCSA      |       82 | -39.41%  | -38.46%            | -38.49% |    -1.04 | 43.76%     | ok               |
| COMP-USD   |       91 | -39.06%  | -75.76%            | -58.43% |    -0.24 | 46.55%     | ok               |
| COP        |       73 | -21.41%  | -8.05%             | -43.96% |    -0.38 | 40.93%     | ok               |
| COST       |       60 | 0.19%    | 31.42%             | -29.73% |     0.08 | 45.09%     | ok               |
| CRM        |       67 | -42.85%  | -43.10%            | -42.70% |    -0.93 | 43.76%     | ok               |
| CRV-USD    |       64 | -6.87%   | -69.21%            | -39.89% |     0.16 | 35.63%     | ok               |
| CSCO       |       59 | 26.53%   | 125.61%            | -21.79% |     0.56 | 49.92%     | ok               |
| CVX        |       71 | -14.90%  | 9.83%              | -26.75% |    -0.37 | 41.60%     | ok               |
| DASH-USD   |       63 | -37.83%  | 13.58%             | -64.43% |     0.03 | 31.61%     | ok               |
| DBC        |       56 | -12.95%  | 19.68%             | -25.67% |    -0.45 | 32.95%     | ok               |
| DE         |       72 | -3.15%   | 61.02%             | -25.24% |     0.03 | 46.76%     | ok               |
| DIA        |       60 | -2.66%   | 36.28%             | -12.94% |    -0.11 | 45.26%     | ok               |
| DIS        |       68 | -18.53%  | -9.99%             | -28.17% |    -0.33 | 47.25%     | ok               |
| DOGE-USD   |       78 | -21.30%  | -76.55%            | -62.31% |     0.04 | 50.57%     | ok               |
| DOT-USD    |       90 | -50.56%  | -84.92%            | -60.30% |    -0.42 | 49.04%     | ok               |
| DXY-INDEX  |       40 | -2.00%   | -1.01%             | -6.05%  |    -0.3  | 30.09%     | ok               |
| EEM        |       64 | -9.40%   | 66.71%             | -25.67% |    -0.25 | 43.43%     | ok               |
| EFA        |       60 | -7.42%   | 39.09%             | -13.02% |    -0.26 | 44.26%     | ok               |
| EOG        |       77 | -24.73%  | 15.67%             | -48.13% |    -0.54 | 46.09%     | ok               |
| ETC-USD    |       64 | -35.69%  | -71.76%            | -48.16% |    -0.51 | 31.23%     | ok               |
| ETH-USD    |       62 | 144.24%  | -44.58%            | -30.11% |     1.21 | 45.21%     | ok               |
| EWJ        |       64 | -17.91%  | 40.29%             | -30.73% |    -0.58 | 39.27%     | ok               |
| FCX        |       63 | -28.65%  | 59.94%             | -48.09% |    -0.33 | 45.09%     | ok               |
| FET-USD    |       83 | -30.73%  | -81.16%            | -54.02% |    -0.03 | 40.61%     | ok               |
| FIL-USD    |       72 | -35.65%  | -82.25%            | -50.22% |    -0.33 | 33.33%     | ok               |
| FXI        |       44 | -2.22%   | 44.39%             | -23.91% |     0.03 | 29.62%     | ok               |
| GDX        |       60 | 11.28%   | 187.29%            | -34.99% |     0.3  | 48.09%     | ok               |
| GDXJ       |       68 | -23.13%  | 210.62%            | -44.93% |    -0.22 | 46.42%     | ok               |
| GE         |       74 | 26.68%   | 240.19%            | -27.82% |     0.52 | 53.74%     | ok               |
| GLD        |       48 | 25.23%   | 100.78%            | -16.63% |     0.64 | 46.26%     | ok               |
| GOOGL      |       63 | 75.66%   | 146.67%            | -20.41% |     1.14 | 53.41%     | ok               |
| GRT-USD    |       85 | -3.45%   | -88.60%            | -54.83% |     0.19 | 42.72%     | ok               |
| GS         |       76 | -2.38%   | 165.17%            | -22.13% |     0.05 | 52.08%     | ok               |
| HD         |       73 | -2.60%   | -1.60%             | -18.58% |     0.01 | 43.93%     | ok               |
| HON        |       93 | -26.82%  | 26.06%             | -29.80% |    -0.72 | 52.41%     | ok               |
| HYG        |       79 | -9.05%   | 3.25%              | -9.59%  |    -1.05 | 34.44%     | ok               |
| IBIT       |       32 | 38.08%   | -8.26%             | -18.95% |     0.78 | 32.30%     | ok               |
| IBM        |       78 | 4.04%    | 57.04%             | -27.54% |     0.18 | 49.75%     | ok               |
| ICP-USD    |       83 | -6.90%   | -74.11%            | -55.89% |     0.2  | 37.55%     | ok               |
| IEF        |       76 | -10.90%  | -0.57%             | -11.70% |    -1.54 | 32.78%     | ok               |
| IEMG       |       58 | -5.52%   | 60.87%             | -26.84% |    -0.12 | 43.59%     | ok               |
| INJ-USD    |       77 | -51.80%  | -72.99%            | -76.97% |    -0.47 | 38.70%     | ok               |
| INTC       |       70 | 55.82%   | 183.18%            | -60.60% |     0.62 | 49.25%     | ok               |
| INTU       |       67 | -20.02%  | -57.84%            | -43.77% |    -0.23 | 42.60%     | ok               |
| ITA        |       72 | 0.83%    | 99.43%             | -23.75% |     0.1  | 47.75%     | ok               |
| IWM        |       48 | 9.40%    | 51.71%             | -12.83% |     0.39 | 35.77%     | ok               |
| JNJ        |       71 | 9.57%    | 68.18%             | -17.51% |     0.39 | 50.75%     | ok               |
| JPM        |       73 | -17.16%  | 91.34%             | -33.16% |    -0.39 | 53.91%     | ok               |
| KO         |       49 | 28.93%   | 40.63%             | -8.07%  |     1.03 | 37.77%     | ok               |
| LDO-USD    |       76 | -1.03%   | -85.37%            | -60.93% |     0.26 | 38.12%     | ok               |
| LIN        |       64 | 0.44%    | 32.04%             | -21.53% |     0.08 | 38.60%     | ok               |
| LINK-USD   |       71 | -16.15%  | -65.70%            | -49.35% |     0.07 | 41.76%     | ok               |
| LLY        |       71 | -25.16%  | 65.01%             | -53.34% |    -0.34 | 51.08%     | ok               |
| LRCX       |       80 | -20.80%  | 306.56%            | -63.56% |    -0.08 | 46.26%     | ok               |
| LTC-USD    |       66 | -34.00%  | -60.74%            | -53.76% |    -0.29 | 48.47%     | ok               |
| MCD        |       75 | -2.55%   | -3.87%             | -18.81% |    -0.05 | 38.10%     | ok               |
| META       |       72 | -28.65%  | 24.02%             | -38.96% |    -0.48 | 49.08%     | ok               |
| MPC        |       71 | -15.29%  | 56.97%             | -44.76% |    -0.17 | 49.58%     | ok               |
| MRK        |       67 | -30.35%  | 2.33%              | -34.46% |    -0.74 | 45.09%     | ok               |
| MS         |       81 | -16.46%  | 149.77%            | -27.79% |    -0.34 | 49.75%     | ok               |
| MSFT       |       81 | -37.49%  | -5.70%             | -38.43% |    -0.99 | 47.92%     | ok               |
| MU         |       51 | 270.20%  | 1049.34%           | -68.76% |     1.34 | 59.90%     | ok               |
| NEAR-USD   |       87 | 3.87%    | -54.24%            | -60.07% |     0.29 | 42.15%     | ok               |
| NEM        |       74 | -31.68%  | 191.06%            | -38.49% |    -0.34 | 53.41%     | ok               |
| NFLX       |       62 | 31.00%   | 39.03%             | -21.09% |     0.66 | 54.74%     | ok               |
| NKE        |       91 | -48.19%  | -57.51%            | -57.25% |    -0.9  | 43.59%     | ok               |
| NOW        |       80 | 6.62%    | -33.50%            | -30.25% |     0.24 | 45.76%     | ok               |
| NVDA       |       76 | -24.41%  | 123.60%            | -45.02% |    -0.16 | 58.29%     | ok               |
| OP-USD     |       72 | -12.93%  | -92.62%            | -70.27% |     0.11 | 34.67%     | ok               |
| ORCL       |       74 | 93.68%   | 20.22%             | -29.47% |     0.86 | 53.58%     | ok               |
| OXY        |       67 | 8.55%    | -15.75%            | -31.37% |     0.26 | 43.26%     | ok               |
| PEP        |       83 | -10.20%  | -17.04%            | -21.35% |    -0.24 | 49.08%     | ok               |
| PEPE-USD   |       79 | 14.92%   | -78.50%            | -57.66% |     0.4  | 44.83%     | ok               |
| PFE        |       77 | -39.75%  | -11.79%            | -40.87% |    -1.29 | 34.94%     | ok               |
| PG         |       64 | -15.05%  | -4.56%             | -21.96% |    -0.55 | 41.26%     | ok               |
| PM         |       83 | -5.17%   | 104.77%            | -33.68% |    -0.02 | 56.91%     | ok               |
| POL-USD    |       79 | 66.27%   | -81.22%            | -46.45% |     0.77 | 50.77%     | ok               |
| QCOM       |       75 | -12.01%  | 18.94%             | -56.59% |     0.01 | 46.76%     | ok               |
| QQQ        |       64 | 16.76%   | 64.65%             | -12.88% |     0.5  | 45.09%     | ok               |
| RENDER-USD |       98 | -19.07%  | -61.66%            | -45.00% |     0.1  | 43.98%     | ok               |
| RTX        |       58 | 27.88%   | 118.86%            | -16.99% |     0.68 | 51.58%     | ok               |
| SBUX       |       64 | -22.61%  | 7.95%              | -29.22% |    -0.45 | 39.77%     | ok               |
| SCHW       |       78 | -20.35%  | 55.27%             | -31.92% |    -0.45 | 46.26%     | ok               |
| SHIB-USD   |       78 | -27.51%  | -76.32%            | -48.95% |    -0.13 | 53.26%     | ok               |
| SHY        |       48 | -2.24%   | 0.12%              | -2.85%  |    -0.79 | 34.28%     | ok               |
| SKY-USD    |       70 | -28.56%  | 3.75%              | -43.98% |    -0.35 | 41.04%     | ok               |
| SLB        |       77 | -20.81%  | -5.57%             | -54.13% |    -0.32 | 50.92%     | ok               |
| SLV        |       58 | 44.14%   | 166.44%            | -42.66% |     0.64 | 41.93%     | ok               |
| SMH        |       48 | 87.45%   | 196.99%            | -33.99% |     1.13 | 49.25%     | ok               |
| SNX-USD    |       62 | -16.00%  | -83.31%            | -34.76% |     0.08 | 38.70%     | ok               |
| SOL-USD    |       68 | -35.74%  | -64.48%            | -56.90% |    -0.13 | 59.20%     | ok               |
| SOXX       |       57 | 75.69%   | 175.30%            | -41.89% |     0.99 | 48.09%     | ok               |
| SPY        |       64 | 2.96%    | 49.46%             | -16.47% |     0.16 | 50.08%     | ok               |
| SUSHI-USD  |       92 | -80.67%  | -86.13%            | -84.53% |    -1.23 | 36.02%     | ok               |
| T          |       64 | 44.42%   | 22.35%             | -17.01% |     0.96 | 51.91%     | ok               |
| TGT        |       58 | -12.54%  | -11.66%            | -40.57% |    -0.18 | 38.94%     | ok               |
| TIA-USD    |       90 | -28.18%  | -90.31%            | -60.92% |    -0.06 | 36.02%     | ok               |
| TLT        |       68 | -21.58%  | -9.07%             | -21.75% |    -1.68 | 31.61%     | ok               |
| TMO        |       61 | 13.93%   | -4.98%             | -18.85% |     0.38 | 49.08%     | ok               |
| TMUS       |       70 | 12.74%   | 10.31%             | -24.50% |     0.36 | 48.09%     | ok               |
| TRX-USD    |       72 | 0.99%    | 32.26%             | -22.90% |     0.12 | 49.04%     | ok               |
| TSLA       |       69 | 9.97%    | 107.56%            | -42.22% |     0.29 | 41.43%     | ok               |
| TXN        |       77 | -15.53%  | 82.93%             | -47.39% |    -0.09 | 53.91%     | ok               |
| UNH        |       74 | 33.82%   | -18.21%            | -26.96% |     0.56 | 52.41%     | ok               |
| UNI-USD    |       90 | -76.74%  | -71.20%            | -80.61% |    -1.01 | 42.15%     | ok               |
| UPS        |       70 | -35.75%  | -25.19%            | -38.75% |    -0.71 | 40.27%     | ok               |
| USO        |       68 | 7.65%    | 45.39%             | -43.35% |     0.25 | 34.28%     | ok               |
| VEA        |       58 | -0.98%   | 49.17%             | -17.93% |     0.01 | 44.09%     | ok               |
| VIXY       |       96 | -80.08%  | -61.73%            | -88.16% |    -1.01 | 32.11%     | ok               |
| VNQ        |       75 | -16.77%  | 16.34%             | -24.92% |    -0.7  | 37.60%     | ok               |
| VTI        |       70 | -2.68%   | 49.06%             | -18.77% |    -0.04 | 50.92%     | ok               |
| VWO        |       76 | -13.41%  | 45.89%             | -25.20% |    -0.47 | 44.09%     | ok               |
| VZ         |       89 | -27.52%  | 6.64%              | -27.84% |    -0.93 | 36.94%     | ok               |
| WFC        |       84 | -17.50%  | 76.86%             | -29.78% |    -0.29 | 49.42%     | ok               |
| WIF-USD    |       68 | -43.81%  | -83.71%            | -57.06% |    -0.24 | 32.18%     | ok               |
| WMT        |       59 | 20.12%   | 98.10%             | -21.31% |     0.58 | 50.58%     | ok               |
| XBI        |       62 | 5.64%    | 79.85%             | -20.73% |     0.22 | 40.77%     | ok               |
| XLB        |       66 | -10.72%  | 25.39%             | -26.57% |    -0.35 | 36.94%     | ok               |
| XLC        |       65 | 13.24%   | 38.59%             | -12.33% |     0.48 | 55.24%     | ok               |
| XLE        |       73 | -12.28%  | 25.80%             | -37.51% |    -0.24 | 46.59%     | ok               |
| XLF        |       76 | -8.64%   | 42.73%             | -23.61% |    -0.26 | 48.25%     | ok               |
| XLI        |       64 | 2.18%    | 57.50%             | -11.38% |     0.14 | 44.76%     | ok               |
| XLK        |       44 | 57.41%   | 76.12%             | -14.75% |     1.11 | 46.59%     | ok               |
| XLM-USD    |       69 | 5.21%    | -49.75%            | -50.36% |     0.28 | 45.79%     | ok               |
| XLP        |       68 | 6.56%    | 15.18%             | -11.16% |     0.4  | 42.93%     | ok               |
| XLU        |       67 | -4.08%   | 52.43%             | -20.40% |    -0.14 | 37.77%     | ok               |
| XLV        |       66 | -12.12%  | 13.61%             | -16.83% |    -0.59 | 35.61%     | ok               |
| XLY        |       72 | 2.75%    | 31.13%             | -14.01% |     0.15 | 44.26%     | ok               |
| XOM        |       58 | 2.35%    | 31.86%             | -20.29% |     0.14 | 36.94%     | ok               |
| XRP-USD    |       60 | -31.84%  | -64.36%            | -44.89% |    -0.29 | 33.91%     | ok               |
| YFI-USD    |       81 | -52.55%  | -73.98%            | -67.78% |    -0.75 | 40.80%     | ok               |
| ZEC-USD    |       62 | 62.53%   | 923.33%            | -47.68% |     0.64 | 35.82%     | ok               |

## AAPL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 23.44%   | 63.89%             | -21.71% |     0.52 |       68 | 53.08%     | ok               |
|          15 | 19.65%   | 63.89%             | -23.86% |     0.45 |       75 | 60.23%     | ok               |
|          30 | 12.75%   | 63.89%             | -20.65% |     0.35 |       63 | 48.25%     | ok               |
|          25 | 12.15%   | 63.89%             | -20.03% |     0.34 |       65 | 50.75%     | ok               |
|          35 | 7.14%    | 63.89%             | -22.04% |     0.25 |       63 | 45.92%     | ok               |

## AAVE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 7.79%    | -69.71%            | -43.61% |     0.3  |       38 | 30.27%     | ok               |
|          45 | -7.90%   | -69.71%            | -49.19% |     0.11 |       40 | 26.05%     | ok               |
|          35 | -11.34%  | -69.71%            | -51.96% |     0.09 |       50 | 32.95%     | ok               |
|          50 | -33.87%  | -69.71%            | -47.39% |    -0.36 |       42 | 19.73%     | ok               |
|          15 | -54.37%  | -69.71%            | -61.76% |    -0.38 |       80 | 51.15%     | ok               |

## ABBV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 2.39%    | 49.36%             | -21.96% |     0.14 |       50 | 36.44%     | ok               |
|          40 | -10.47%  | 49.36%             | -24.88% |    -0.19 |       66 | 41.43%     | ok               |
|          45 | -13.20%  | 49.36%             | -27.88% |    -0.27 |       56 | 38.60%     | ok               |
|          35 | -13.78%  | 49.36%             | -27.83% |    -0.27 |       68 | 44.43%     | ok               |
|          30 | -16.01%  | 49.36%             | -30.55% |    -0.31 |       66 | 47.25%     | ok               |

## ADA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -83.94%  | -81.80%            | -91.83% |    -0.58 |       80 | 63.41%     | ok               |
|          50 | -77.92%  | -81.80%            | -85.97% |    -0.59 |       55 | 26.82%     | ok               |
|          45 | -80.28%  | -81.80%            | -88.02% |    -0.62 |       58 | 31.61%     | ok               |
|          35 | -82.47%  | -81.80%            | -89.77% |    -0.66 |       76 | 42.15%     | ok               |
|          20 | -85.21%  | -81.80%            | -92.33% |    -0.66 |       90 | 57.66%     | ok               |

## ADBE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -0.01%   | -64.32%            | -21.34% |     0.12 |       78 | 49.58%     | ok               |
|          40 | -12.92%  | -64.32%            | -24.85% |    -0.13 |       74 | 42.60%     | ok               |
|          25 | -17.85%  | -64.32%            | -31.91% |    -0.13 |       52 | 61.56%     | ok               |
|          15 | -26.44%  | -64.32%            | -32.31% |    -0.27 |       61 | 66.39%     | ok               |
|          20 | -28.05%  | -64.32%            | -35.01% |    -0.31 |       52 | 63.73%     | ok               |

## AGG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -6.61%   | 0.97%              | -10.16% |    -1.1  |       69 | 31.11%     | ok               |
|          20 | -7.69%   | 0.97%              | -10.67% |    -1.13 |       73 | 36.77%     | ok               |
|          45 | -5.75%   | 0.97%              | -7.89%  |    -1.16 |       52 | 20.47%     | ok               |
|          25 | -7.87%   | 0.97%              | -11.31% |    -1.2  |       73 | 35.11%     | ok               |
|          50 | -5.57%   | 0.97%              | -7.92%  |    -1.25 |       46 | 16.97%     | ok               |

## ALGO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -50.43%  | -76.08%            | -53.13% |    -0.57 |       86 | 38.12%     | ok               |
|          15 | -61.07%  | -76.08%            | -69.47% |    -0.66 |       88 | 50.57%     | ok               |
|          25 | -61.32%  | -76.08%            | -73.33% |    -0.72 |       88 | 45.21%     | ok               |
|          20 | -65.02%  | -76.08%            | -72.09% |    -0.78 |       90 | 48.28%     | ok               |
|          50 | -45.64%  | -76.08%            | -48.43% |    -0.81 |       42 | 16.86%     | ok               |

## AMAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -4.26%   | 246.79%            | -54.05% |     0.15 |       66 | 62.06%     | ok               |
|          30 | -19.88%  | 246.79%            | -57.21% |    -0.07 |       69 | 53.41%     | ok               |
|          20 | -25.73%  | 246.79%            | -60.16% |    -0.13 |       72 | 58.57%     | ok               |
|          50 | -23.70%  | 246.79%            | -48.72% |    -0.16 |       52 | 39.27%     | ok               |
|          35 | -25.58%  | 246.79%            | -55.26% |    -0.16 |       71 | 51.25%     | ok               |

## AMD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 5.94%    | 205.77%            | -44.76% |     0.27 |       56 | 36.44%     | ok               |
|          50 | 6.10%    | 205.77%            | -44.42% |     0.26 |       56 | 30.95%     | ok               |
|          35 | -7.56%   | 205.77%            | -54.16% |     0.14 |       62 | 38.44%     | ok               |
|          45 | -15.31%  | 205.77%            | -53.37% |     0.03 |       62 | 33.78%     | ok               |
|          30 | -22.01%  | 205.77%            | -60.65% |    -0.02 |       65 | 41.10%     | ok               |

## AMGN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -10.00%  | 26.90%             | -26.64% |    -0.13 |       71 | 52.58%     | ok               |
|          15 | -13.18%  | 26.90%             | -27.92% |    -0.19 |       69 | 58.24%     | ok               |
|          35 | -11.49%  | 26.90%             | -31.23% |    -0.19 |       67 | 42.60%     | ok               |
|          30 | -15.57%  | 26.90%             | -34.14% |    -0.29 |       69 | 46.42%     | ok               |
|          25 | -19.01%  | 26.90%             | -33.41% |    -0.37 |       65 | 48.75%     | ok               |

## AMZN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -19.01%  | 42.88%             | -28.70% |    -0.56 |       52 | 29.28%     | ok               |
|          50 | -24.16%  | 42.88%             | -35.48% |    -0.84 |       48 | 23.46%     | ok               |
|          45 | -26.95%  | 42.88%             | -35.47% |    -0.93 |       52 | 26.46%     | ok               |
|          35 | -30.88%  | 42.88%             | -38.29% |    -0.96 |       68 | 32.78%     | ok               |
|          30 | -37.03%  | 42.88%             | -42.48% |    -1.1  |       80 | 38.27%     | ok               |

## APT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 35.19%   | -91.44%            | -46.73% |     0.58 |       44 | 20.11%     | ok               |
|          45 | 2.79%    | -91.44%            | -63.86% |     0.24 |       60 | 26.25%     | ok               |
|          40 | -16.95%  | -91.44%            | -63.33% |     0.05 |       66 | 31.80%     | ok               |
|          20 | -25.11%  | -91.44%            | -70.51% |     0.04 |       73 | 52.49%     | ok               |
|          35 | -23.04%  | -91.44%            | -64.45% |    -0    |       70 | 37.55%     | ok               |

## ARB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 52.21%   | -86.82%            | -53.74% |     0.63 |       87 | 56.32%     | ok               |
|          40 | 28.98%   | -86.82%            | -47.60% |     0.49 |       50 | 29.89%     | ok               |
|          20 | 14.39%   | -86.82%            | -60.40% |     0.39 |       75 | 49.81%     | ok               |
|          35 | 16.36%   | -86.82%            | -56.00% |     0.39 |       60 | 33.33%     | ok               |
|          45 | 15.68%   | -86.82%            | -50.83% |     0.37 |       56 | 23.18%     | ok               |

## ARKK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -23.32%  | 67.73%             | -34.75% |    -0.26 |       90 | 50.08%     | ok               |
|          20 | -28.47%  | 67.73%             | -34.36% |    -0.4  |       87 | 45.59%     | ok               |
|          30 | -32.73%  | 67.73%             | -35.25% |    -0.56 |       83 | 39.77%     | ok               |
|          35 | -36.28%  | 67.73%             | -38.66% |    -0.69 |       84 | 37.27%     | ok               |
|          40 | -38.33%  | 67.73%             | -39.74% |    -0.79 |       74 | 32.78%     | ok               |

## ATOM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -63.91%  | -72.48%            | -70.52% |    -0.92 |       95 | 51.92%     | ok               |
|          15 | -68.12%  | -72.48%            | -71.82% |    -0.96 |       93 | 61.49%     | ok               |
|          45 | -59.38%  | -72.48%            | -65.47% |    -1.09 |       76 | 29.69%     | ok               |
|          30 | -67.78%  | -72.48%            | -73.96% |    -1.12 |       92 | 45.59%     | ok               |
|          20 | -71.46%  | -72.48%            | -74.51% |    -1.13 |      101 | 55.75%     | ok               |

## AVAX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 15.04%   | -78.65%            | -34.50% |     0.37 |       38 | 19.54%     | ok               |
|          45 | 4.12%    | -78.65%            | -41.07% |     0.23 |       40 | 23.56%     | ok               |
|          15 | -5.39%   | -78.65%            | -52.46% |     0.2  |       67 | 54.02%     | ok               |
|          40 | -10.50%  | -78.65%            | -47.98% |     0.04 |       46 | 26.63%     | ok               |
|          25 | -16.70%  | -78.65%            | -52.93% |     0.04 |       73 | 44.44%     | ok               |

## AVGO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 22.35%   | 182.76%            | -35.76% |     0.41 |       62 | 43.93%     | ok               |
|          25 | 19.09%   | 182.76%            | -38.01% |     0.38 |       68 | 44.93%     | ok               |
|          35 | 16.46%   | 182.76%            | -36.19% |     0.35 |       70 | 41.10%     | ok               |
|          40 | 16.07%   | 182.76%            | -40.70% |     0.35 |       60 | 37.94%     | ok               |
|          20 | 10.30%   | 182.76%            | -40.10% |     0.29 |       74 | 47.92%     | ok               |

## BA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 26.03%   | 8.25%              | -13.34% |     0.67 |       42 | 31.45%     | ok               |
|          35 | 30.46%   | 8.25%              | -23.77% |     0.59 |       72 | 44.59%     | ok               |
|          40 | 20.11%   | 8.25%              | -23.90% |     0.47 |       46 | 38.60%     | ok               |
|          25 | 10.59%   | 8.25%              | -32.48% |     0.29 |       70 | 52.58%     | ok               |
|          30 | 7.60%    | 8.25%              | -30.56% |     0.25 |       67 | 49.25%     | ok               |

## BAC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -1.68%   | 77.32%             | -21.23% |     0.01 |       62 | 36.94%     | ok               |
|          20 | -5.39%   | 77.32%             | -21.48% |    -0.04 |       80 | 53.08%     | ok               |
|          50 | -3.28%   | 77.32%             | -19.75% |    -0.05 |       60 | 33.78%     | ok               |
|          35 | -6.52%   | 77.32%             | -29.13% |    -0.12 |       70 | 44.59%     | ok               |
|          40 | -7.13%   | 77.32%             | -25.32% |    -0.15 |       66 | 40.10%     | ok               |

## BCH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 3.75%    | -46.18%            | -53.87% |     0.25 |       76 | 48.85%     | ok               |
|          20 | -8.48%   | -46.18%            | -54.02% |     0.15 |       70 | 55.36%     | ok               |
|          15 | -18.95%  | -46.18%            | -60.20% |     0.04 |       79 | 59.96%     | ok               |
|          25 | -20.00%  | -46.18%            | -59.80% |     0    |       72 | 51.15%     | ok               |
|          35 | -18.38%  | -46.18%            | -64.08% |    -0.03 |       70 | 45.02%     | ok               |

## BITO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 26.14%   | -61.35%            | -31.98% |     0.47 |       54 | 25.79%     | ok               |
|          30 | 9.21%    | -61.35%            | -42.82% |     0.28 |       78 | 42.10%     | ok               |
|          45 | 6.12%    | -61.35%            | -41.16% |     0.24 |       62 | 29.45%     | ok               |
|          15 | 2.35%    | -61.35%            | -48.38% |     0.23 |       87 | 50.92%     | ok               |
|          25 | 0.56%    | -61.35%            | -41.73% |     0.19 |       82 | 45.09%     | ok               |

## BLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -3.94%   | 25.53%             | -17.97% |    -0.06 |       82 | 39.10%     | ok               |
|          20 | -5.80%   | 25.53%             | -21.48% |    -0.09 |       80 | 47.59%     | ok               |
|          40 | -5.71%   | 25.53%             | -20.08% |    -0.13 |       72 | 34.78%     | ok               |
|          30 | -10.03%  | 25.53%             | -24.29% |    -0.24 |       77 | 42.93%     | ok               |
|          25 | -10.94%  | 25.53%             | -23.36% |    -0.25 |       77 | 45.26%     | ok               |

## BND Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.17%   | 0.94%              | -9.05%  |    -0.9  |       63 | 38.10%     | ok               |
|          25 | -6.87%   | 0.94%              | -10.14% |    -1.05 |       67 | 36.11%     | ok               |
|          30 | -7.32%   | 0.94%              | -9.89%  |    -1.18 |       65 | 32.28%     | ok               |
|          15 | -8.39%   | 0.94%              | -10.58% |    -1.21 |       73 | 40.93%     | ok               |
|          45 | -7.56%   | 0.94%              | -9.57%  |    -1.47 |       50 | 21.96%     | ok               |

## BONK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 170.82%  | -80.92%            | -35.57% |     1.24 |       46 | 22.22%     | ok               |
|          25 | 186.54%  | -80.92%            | -46.61% |     1.08 |       65 | 48.28%     | ok               |
|          20 | 170.36%  | -80.92%            | -54.25% |     1.03 |       66 | 52.87%     | ok               |
|          15 | 176.55%  | -80.92%            | -62.48% |     1.02 |       69 | 57.85%     | ok               |
|          45 | 85.55%   | -80.92%            | -42.36% |     0.84 |       56 | 27.01%     | ok               |

## BTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 52.04%   | -39.40%            | -14.50% |     0.95 |       46 | 34.48%     | ok               |
|          45 | 37.57%   | -39.40%            | -15.18% |     0.76 |       46 | 30.84%     | ok               |
|          35 | 36.20%   | -39.40%            | -22.12% |     0.7  |       70 | 41.38%     | ok               |
|          30 | 19.84%   | -39.40%            | -21.75% |     0.45 |       74 | 48.08%     | ok               |
|          50 | 11.33%   | -39.40%            | -18.05% |     0.34 |       44 | 25.48%     | ok               |

## C Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -8.12%   | 157.82%            | -22.28% |    -0.15 |       66 | 36.27%     | ok               |
|          45 | -14.93%  | 157.82%            | -28.12% |    -0.33 |       78 | 40.60%     | ok               |
|          15 | -24.06%  | 157.82%            | -35.02% |    -0.4  |       74 | 60.23%     | ok               |
|          25 | -24.06%  | 157.82%            | -35.86% |    -0.43 |       73 | 53.74%     | ok               |
|          40 | -20.95%  | 157.82%            | -33.20% |    -0.47 |       82 | 43.09%     | ok               |

## CAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 25.61%   | 199.23%            | -21.02% |     0.5  |       72 | 57.07%     | ok               |
|          25 | 25.72%   | 199.23%            | -26.37% |     0.49 |       68 | 59.90%     | ok               |
|          20 | 23.18%   | 199.23%            | -25.65% |     0.46 |       78 | 63.23%     | ok               |
|          45 | 14.76%   | 199.23%            | -28.85% |     0.36 |       58 | 45.92%     | ok               |
|          15 | 13.63%   | 199.23%            | -30.60% |     0.33 |       71 | 69.22%     | ok               |

## CL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 13.56%   | 12.90%             | -12.98% |     0.58 |       42 | 30.45%     | ok               |
|          30 | 13.07%   | 12.90%             | -14.32% |     0.47 |       60 | 46.42%     | ok               |
|          45 | 8.37%    | 12.90%             | -13.51% |     0.37 |       46 | 33.44%     | ok               |
|          35 | 7.68%    | 12.90%             | -13.83% |     0.32 |       62 | 42.76%     | ok               |
|          40 | 4.56%    | 12.90%             | -12.70% |     0.23 |       56 | 37.44%     | ok               |

## CMCSA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -35.96%  | -38.46%            | -44.35% |    -0.79 |       86 | 58.74%     | ok               |
|          30 | -39.41%  | -38.46%            | -38.49% |    -1.04 |       82 | 43.76%     | ok               |
|          25 | -42.63%  | -38.46%            | -41.51% |    -1.13 |       89 | 48.92%     | ok               |
|          50 | -30.21%  | -38.46%            | -31.36% |    -1.17 |       48 | 15.47%     | ok               |
|          20 | -46.95%  | -38.46%            | -46.89% |    -1.24 |       92 | 54.74%     | ok               |

## COMP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -6.92%   | -75.76%            | -38.71% |     0.11 |       50 | 21.07%     | ok               |
|          25 | -40.17%  | -75.76%            | -60.58% |    -0.22 |       89 | 51.53%     | ok               |
|          30 | -39.06%  | -75.76%            | -58.43% |    -0.24 |       91 | 46.55%     | ok               |
|          15 | -48.12%  | -75.76%            | -65.55% |    -0.31 |      103 | 63.03%     | ok               |
|          40 | -43.33%  | -75.76%            | -48.44% |    -0.41 |       76 | 34.67%     | ok               |

## COP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -11.98%  | -8.05%             | -35.08% |    -0.2  |       50 | 27.45%     | ok               |
|          45 | -18.48%  | -8.05%             | -41.35% |    -0.37 |       62 | 30.62%     | ok               |
|          35 | -20.87%  | -8.05%             | -43.58% |    -0.37 |       75 | 37.77%     | ok               |
|          30 | -21.41%  | -8.05%             | -43.96% |    -0.38 |       73 | 40.93%     | ok               |
|          40 | -24.51%  | -8.05%             | -47.05% |    -0.52 |       70 | 33.61%     | ok               |

## COST Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 11.77%   | 31.42%             | -24.32% |     0.39 |       66 | 51.58%     | ok               |
|          25 | 10.12%   | 31.42%             | -24.73% |     0.35 |       63 | 48.75%     | ok               |
|          35 | 5.00%    | 31.42%             | -26.58% |     0.22 |       54 | 42.10%     | ok               |
|          30 | 0.19%    | 31.42%             | -29.73% |     0.08 |       60 | 45.09%     | ok               |
|          40 | -1.45%   | 31.42%             | -28.41% |     0.02 |       56 | 39.10%     | ok               |

## CRM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -38.30%  | -43.10%            | -44.49% |    -0.62 |       92 | 55.24%     | ok               |
|          35 | -33.46%  | -43.10%            | -36.58% |    -0.69 |       64 | 38.94%     | ok               |
|          40 | -37.19%  | -43.10%            | -41.17% |    -0.87 |       70 | 34.78%     | ok               |
|          30 | -42.85%  | -43.10%            | -42.70% |    -0.93 |       67 | 43.76%     | ok               |
|          20 | -47.40%  | -43.10%            | -47.55% |    -0.95 |       80 | 48.92%     | ok               |

## CRV-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 17.27%   | -69.21%            | -37.78% |     0.39 |       66 | 31.03%     | ok               |
|          45 | -1.09%   | -69.21%            | -42.29% |     0.18 |       54 | 20.69%     | ok               |
|          50 | -0.89%   | -69.21%            | -29.30% |     0.18 |       46 | 17.43%     | ok               |
|          30 | -6.87%   | -69.21%            | -39.89% |     0.16 |       64 | 35.63%     | ok               |
|          40 | -6.61%   | -69.21%            | -38.86% |     0.13 |       58 | 27.01%     | ok               |

## CSCO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 34.09%   | 125.61%            | -19.34% |     0.73 |       54 | 38.60%     | ok               |
|          45 | 32.50%   | 125.61%            | -19.34% |     0.69 |       51 | 40.93%     | ok               |
|          25 | 27.12%   | 125.61%            | -23.28% |     0.57 |       63 | 51.91%     | ok               |
|          35 | 26.51%   | 125.61%            | -23.68% |     0.56 |       51 | 47.42%     | ok               |
|          30 | 26.53%   | 125.61%            | -21.79% |     0.56 |       59 | 49.92%     | ok               |

## CVX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -10.20%  | 9.83%              | -23.25% |    -0.2  |       72 | 44.09%     | ok               |
|          20 | -11.14%  | 9.83%              | -25.18% |    -0.23 |       72 | 45.26%     | ok               |
|          45 | -11.04%  | 9.83%              | -28.32% |    -0.3  |       61 | 30.45%     | ok               |
|          30 | -14.90%  | 9.83%              | -26.75% |    -0.37 |       71 | 41.60%     | ok               |
|          35 | -14.65%  | 9.83%              | -27.83% |    -0.37 |       71 | 38.60%     | ok               |

## DASH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 126.59%  | 13.58%             | -32.30% |     0.95 |       40 | 16.67%     | ok               |
|          40 | 81.99%   | 13.58%             | -32.07% |     0.75 |       48 | 23.56%     | ok               |
|          45 | 63.64%   | 13.58%             | -40.40% |     0.67 |       44 | 18.97%     | ok               |
|          25 | -32.35%  | 13.58%             | -64.14% |     0.1  |       69 | 34.48%     | ok               |
|          35 | -32.14%  | 13.58%             | -63.23% |     0.09 |       69 | 28.16%     | ok               |

## DBC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -10.55%  | 19.68%             | -27.30% |    -0.33 |       73 | 37.77%     | ok               |
|          35 | -10.07%  | 19.68%             | -23.71% |    -0.33 |       58 | 31.78%     | ok               |
|          50 | -8.98%   | 19.68%             | -20.31% |    -0.34 |       42 | 21.13%     | ok               |
|          45 | -10.35%  | 19.68%             | -21.46% |    -0.37 |       54 | 24.46%     | ok               |
|          30 | -12.95%  | 19.68%             | -25.67% |    -0.45 |       56 | 32.95%     | ok               |

## DE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -2.24%   | 61.02%             | -28.94% |     0.05 |       72 | 52.08%     | ok               |
|          30 | -3.15%   | 61.02%             | -25.24% |     0.03 |       72 | 46.76%     | ok               |
|          25 | -4.66%   | 61.02%             | -26.67% |    -0    |       74 | 49.42%     | ok               |
|          50 | -3.53%   | 61.02%             | -23.21% |    -0.01 |       70 | 31.61%     | ok               |
|          45 | -5.51%   | 61.02%             | -26.88% |    -0.05 |       70 | 36.11%     | ok               |

## DIA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -0.60%   | 36.28%             | -13.15% |     0.01 |       60 | 43.09%     | ok               |
|          25 | -1.13%   | 36.28%             | -11.28% |    -0.02 |       60 | 46.42%     | ok               |
|          30 | -2.66%   | 36.28%             | -12.94% |    -0.11 |       60 | 45.26%     | ok               |
|          20 | -4.52%   | 36.28%             | -13.85% |    -0.19 |       64 | 48.75%     | ok               |
|          40 | -4.65%   | 36.28%             | -15.06% |    -0.24 |       66 | 40.27%     | ok               |

## DIS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 16.66%   | -9.99%             | -14.24% |     0.53 |       50 | 29.12%     | ok               |
|          40 | -8.55%   | -9.99%             | -22.77% |    -0.11 |       65 | 37.94%     | ok               |
|          45 | -7.71%   | -9.99%             | -16.54% |    -0.11 |       53 | 32.78%     | ok               |
|          15 | -16.79%  | -9.99%             | -31.15% |    -0.23 |       89 | 58.40%     | ok               |
|          35 | -14.61%  | -9.99%             | -25.70% |    -0.24 |       75 | 44.09%     | ok               |

## DOGE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 15.31%   | -76.55%            | -59.36% |     0.41 |       82 | 65.90%     | ok               |
|          20 | -1.55%   | -76.55%            | -57.37% |     0.26 |       85 | 61.11%     | ok               |
|          25 | -5.63%   | -76.55%            | -55.33% |     0.22 |       75 | 55.75%     | ok               |
|          30 | -21.30%  | -76.55%            | -62.31% |     0.04 |       78 | 50.57%     | ok               |
|          35 | -44.62%  | -76.55%            | -61.79% |    -0.36 |       74 | 44.25%     | ok               |

## DOT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -21.12%  | -84.92%            | -46.17% |    -0.14 |       60 | 26.63%     | ok               |
|          45 | -30.12%  | -84.92%            | -54.01% |    -0.27 |       52 | 31.61%     | ok               |
|          20 | -50.83%  | -84.92%            | -64.09% |    -0.36 |       90 | 60.92%     | ok               |
|          35 | -48.93%  | -84.92%            | -61.76% |    -0.41 |       80 | 42.15%     | ok               |
|          30 | -50.56%  | -84.92%            | -60.30% |    -0.42 |       90 | 49.04%     | ok               |

## DXY-INDEX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -2.00%   | -1.01%             | -6.05%  |    -0.3  |       40 | 30.09%     | ok               |
|          40 | -3.26%   | -1.01%             | -7.30%  |    -0.4  |       72 | 49.57%     | ok               |
|          15 | -4.46%   | -1.01%             | -11.37% |    -0.4  |       86 | 76.62%     | ok               |
|          30 | -3.91%   | -1.01%             | -9.83%  |    -0.43 |       70 | 61.04%     | ok               |
|          35 | -4.47%   | -1.01%             | -9.97%  |    -0.53 |       75 | 55.63%     | ok               |

## EEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -4.96%   | 66.71%             | -19.52% |    -0.11 |       64 | 39.77%     | ok               |
|          35 | -5.62%   | 66.71%             | -23.88% |    -0.12 |       66 | 41.76%     | ok               |
|          50 | -4.94%   | 66.71%             | -15.88% |    -0.12 |       52 | 35.77%     | ok               |
|          45 | -6.04%   | 66.71%             | -17.36% |    -0.16 |       54 | 37.44%     | ok               |
|          25 | -8.49%   | 66.71%             | -25.60% |    -0.21 |       65 | 44.76%     | ok               |

## EFA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -3.05%   | 39.09%             | -10.80% |    -0.05 |       62 | 52.41%     | ok               |
|          30 | -7.42%   | 39.09%             | -13.02% |    -0.26 |       60 | 44.26%     | ok               |
|          20 | -9.78%   | 39.09%             | -12.73% |    -0.34 |       69 | 49.42%     | ok               |
|          40 | -8.83%   | 39.09%             | -14.90% |    -0.35 |       64 | 40.43%     | ok               |
|          50 | -9.07%   | 39.09%             | -17.56% |    -0.4  |       54 | 36.27%     | ok               |

## EOG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -20.10%  | 15.67%             | -39.69% |    -0.48 |       54 | 32.28%     | ok               |
|          50 | -21.27%  | 15.67%             | -40.57% |    -0.53 |       58 | 29.45%     | ok               |
|          30 | -24.73%  | 15.67%             | -48.13% |    -0.54 |       77 | 46.09%     | ok               |
|          35 | -25.56%  | 15.67%             | -46.26% |    -0.61 |       75 | 40.77%     | ok               |
|          40 | -24.83%  | 15.67%             | -43.26% |    -0.61 |       62 | 35.61%     | ok               |

## ETC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -7.93%   | -71.76%            | -27.89% |    -0.02 |       28 | 17.05%     | ok               |
|          35 | -15.03%  | -71.76%            | -42.62% |    -0.11 |       44 | 27.01%     | ok               |
|          45 | -16.07%  | -71.76%            | -35.44% |    -0.17 |       26 | 18.97%     | ok               |
|          40 | -21.04%  | -71.76%            | -40.48% |    -0.26 |       42 | 22.80%     | ok               |
|          30 | -35.69%  | -71.76%            | -48.16% |    -0.51 |       64 | 31.23%     | ok               |

## ETH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 144.24%  | -44.58%            | -30.11% |     1.21 |       62 | 45.21%     | ok               |
|          30 | 125.69%  | -44.58%            | -32.89% |     1.08 |       66 | 54.02%     | ok               |
|          40 | 50.09%   | -44.58%            | -33.11% |     0.69 |       60 | 37.93%     | ok               |
|          15 | 38.47%   | -44.58%            | -42.74% |     0.56 |       78 | 69.54%     | ok               |
|          20 | 32.89%   | -44.58%            | -39.10% |     0.52 |       83 | 63.98%     | ok               |

## EWJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -17.91%  | 40.29%             | -30.73% |    -0.58 |       64 | 39.27%     | ok               |
|          20 | -19.30%  | 40.29%             | -31.32% |    -0.61 |       60 | 41.26%     | ok               |
|          45 | -18.70%  | 40.29%             | -27.68% |    -0.71 |       60 | 31.45%     | ok               |
|          25 | -21.63%  | 40.29%             | -31.18% |    -0.71 |       60 | 40.27%     | ok               |
|          35 | -21.85%  | 40.29%             | -32.54% |    -0.74 |       70 | 37.60%     | ok               |

## FCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -4.48%   | 59.94%             | -27.82% |     0.06 |       52 | 29.45%     | ok               |
|          45 | -8.60%   | 59.94%             | -35.29% |    -0    |       52 | 33.94%     | ok               |
|          40 | -20.30%  | 59.94%             | -44.23% |    -0.2  |       62 | 38.44%     | ok               |
|          30 | -28.65%  | 59.94%             | -48.09% |    -0.33 |       63 | 45.09%     | ok               |
|          20 | -34.13%  | 59.94%             | -57.65% |    -0.39 |       70 | 51.91%     | ok               |

## FET-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 8.75%    | -81.16%            | -57.95% |     0.38 |       88 | 50.96%     | ok               |
|          15 | -18.67%  | -81.16%            | -59.58% |     0.17 |       84 | 54.02%     | ok               |
|          25 | -28.85%  | -81.16%            | -58.52% |     0.02 |       91 | 44.64%     | ok               |
|          30 | -30.73%  | -81.16%            | -54.02% |    -0.03 |       83 | 40.61%     | ok               |
|          35 | -48.59%  | -81.16%            | -62.73% |    -0.39 |       69 | 33.91%     | ok               |

## FIL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -9.16%   | -82.25%            | -39.40% |     0.05 |       50 | 23.56%     | ok               |
|          45 | -27.58%  | -82.25%            | -43.98% |    -0.29 |       44 | 17.62%     | ok               |
|          35 | -32.45%  | -82.25%            | -47.50% |    -0.3  |       60 | 27.78%     | ok               |
|          50 | -26.52%  | -82.25%            | -44.97% |    -0.32 |       38 | 13.03%     | ok               |
|          30 | -35.65%  | -82.25%            | -50.22% |    -0.33 |       72 | 33.33%     | ok               |

## FXI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -1.66%   | 44.39%             | -22.57% |     0.05 |       44 | 30.78%     | ok               |
|          30 | -2.22%   | 44.39%             | -23.91% |     0.03 |       44 | 29.62%     | ok               |
|          15 | -4.58%   | 44.39%             | -21.68% |    -0.02 |       52 | 34.11%     | ok               |
|          45 | -4.73%   | 44.39%             | -26.75% |    -0.05 |       44 | 24.29%     | ok               |
|          20 | -5.63%   | 44.39%             | -24.53% |    -0.05 |       50 | 31.95%     | ok               |

## GDX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 18.06%   | 187.29%            | -35.59% |     0.39 |       73 | 52.91%     | ok               |
|          40 | 13.85%   | 187.29%            | -31.87% |     0.35 |       64 | 42.93%     | ok               |
|          30 | 11.28%   | 187.29%            | -34.99% |     0.3  |       60 | 48.09%     | ok               |
|          35 | 8.95%    | 187.29%            | -32.37% |     0.27 |       68 | 45.26%     | ok               |
|          25 | 6.77%    | 187.29%            | -38.90% |     0.24 |       63 | 49.75%     | ok               |

## GDXJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -7.90%   | 210.62%            | -45.05% |     0.06 |       67 | 53.24%     | ok               |
|          30 | -23.13%  | 210.62%            | -44.93% |    -0.22 |       68 | 46.42%     | ok               |
|          50 | -20.22%  | 210.62%            | -44.94% |    -0.22 |       58 | 37.77%     | ok               |
|          25 | -26.54%  | 210.62%            | -47.26% |    -0.25 |       72 | 49.92%     | ok               |
|          35 | -26.76%  | 210.62%            | -43.49% |    -0.3  |       70 | 44.09%     | ok               |

## GE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 44.86%   | 240.19%            | -22.29% |     0.81 |       66 | 40.60%     | ok               |
|          45 | 33.93%   | 240.19%            | -25.68% |     0.65 |       74 | 43.43%     | ok               |
|          20 | 32.94%   | 240.19%            | -26.63% |     0.59 |       69 | 57.24%     | ok               |
|          35 | 26.97%   | 240.19%            | -27.11% |     0.54 |       80 | 48.75%     | ok               |
|          40 | 26.01%   | 240.19%            | -26.97% |     0.53 |       76 | 44.93%     | ok               |

## GLD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 31.49%   | 100.78%            | -14.61% |     0.76 |       46 | 47.42%     | ok               |
|          20 | 29.53%   | 100.78%            | -14.61% |     0.72 |       48 | 48.75%     | ok               |
|          30 | 25.23%   | 100.78%            | -16.63% |     0.64 |       48 | 46.26%     | ok               |
|          15 | 21.60%   | 100.78%            | -17.54% |     0.54 |       50 | 52.91%     | ok               |
|          35 | 19.12%   | 100.78%            | -17.29% |     0.52 |       50 | 45.59%     | ok               |

## GOOGL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 80.52%   | 146.67%            | -19.76% |     1.18 |       57 | 55.91%     | ok               |
|          30 | 75.66%   | 146.67%            | -20.41% |     1.14 |       63 | 53.41%     | ok               |
|          20 | 66.89%   | 146.67%            | -20.57% |     1.02 |       68 | 58.24%     | ok               |
|          35 | 58.56%   | 146.67%            | -22.85% |     1.01 |       71 | 48.25%     | ok               |
|          15 | 68.71%   | 146.67%            | -13.81% |     1.01 |       71 | 63.39%     | ok               |

## GRT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 39.95%   | -88.60%            | -34.47% |     0.64 |       44 | 21.84%     | ok               |
|          45 | 21.41%   | -88.60%            | -46.59% |     0.44 |       50 | 27.39%     | ok               |
|          35 | 16.47%   | -88.60%            | -48.22% |     0.39 |       60 | 36.21%     | ok               |
|          15 | 14.49%   | -88.60%            | -49.67% |     0.39 |       75 | 61.88%     | ok               |
|          40 | 16.36%   | -88.60%            | -46.38% |     0.38 |       48 | 30.46%     | ok               |

## GS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 21.11%   | 165.17%            | -20.56% |     0.47 |       74 | 61.06%     | ok               |
|          20 | 4.59%    | 165.17%            | -23.19% |     0.19 |       74 | 57.07%     | ok               |
|          40 | 0.08%    | 165.17%            | -17.88% |     0.09 |       72 | 45.26%     | ok               |
|          25 | -0.70%   | 165.17%            | -23.32% |     0.09 |       74 | 54.58%     | ok               |
|          30 | -2.38%   | 165.17%            | -22.13% |     0.05 |       76 | 52.08%     | ok               |

## HD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -2.60%   | -1.60%             | -18.58% |     0.01 |       73 | 43.93%     | ok               |
|          25 | -3.36%   | -1.60%             | -19.40% |    -0.01 |       72 | 45.92%     | ok               |
|          15 | -12.50%  | -1.60%             | -27.26% |    -0.23 |      107 | 54.58%     | ok               |
|          45 | -9.11%   | -1.60%             | -20.74% |    -0.25 |       60 | 28.29%     | ok               |
|          35 | -12.94%  | -1.60%             | -23.81% |    -0.31 |       82 | 39.93%     | ok               |

## HON Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -13.43%  | 26.06%             | -21.17% |    -0.4  |       72 | 31.78%     | ok               |
|          45 | -15.16%  | 26.06%             | -19.99% |    -0.43 |       74 | 36.77%     | ok               |
|          40 | -23.52%  | 26.06%             | -26.29% |    -0.66 |       76 | 41.10%     | ok               |
|          35 | -24.98%  | 26.06%             | -27.37% |    -0.69 |       91 | 47.42%     | ok               |
|          30 | -26.82%  | 26.06%             | -29.80% |    -0.72 |       93 | 52.41%     | ok               |

## HYG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -7.49%   | 3.25%              | -7.49%  |    -0.9  |       70 | 29.62%     | ok               |
|          45 | -8.18%   | 3.25%              | -8.21%  |    -1.02 |       66 | 26.46%     | ok               |
|          30 | -9.05%   | 3.25%              | -9.59%  |    -1.05 |       79 | 34.44%     | ok               |
|          15 | -9.75%   | 3.25%              | -10.10% |    -1.06 |       88 | 41.60%     | ok               |
|          20 | -9.79%   | 3.25%              | -10.39% |    -1.09 |       88 | 39.27%     | ok               |

## IBIT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 67.59%   | -8.26%             | -19.20% |     1.08 |       38 | 39.90%     | ok               |
|          50 | 53.73%   | -8.26%             | -17.37% |     1.08 |       22 | 22.80%     | ok               |
|          45 | 44.27%   | -8.26%             | -17.37% |     0.91 |       26 | 24.23%     | ok               |
|          40 | 38.04%   | -8.26%             | -17.78% |     0.81 |       26 | 26.13%     | ok               |
|          30 | 38.08%   | -8.26%             | -18.95% |     0.78 |       32 | 32.30%     | ok               |

## IBM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 17.26%   | 57.04%             | -28.20% |     0.4  |       92 | 62.06%     | ok               |
|          30 | 4.04%    | 57.04%             | -27.54% |     0.18 |       78 | 49.75%     | ok               |
|          20 | -0.54%   | 57.04%             | -34.12% |     0.1  |       76 | 54.41%     | ok               |
|          35 | -0.50%   | 57.04%             | -27.54% |     0.09 |       74 | 45.26%     | ok               |
|          50 | -2.68%   | 57.04%             | -22.50% |     0.03 |       56 | 32.45%     | ok               |

## ICP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 14.78%   | -74.11%            | -32.85% |     0.36 |       58 | 26.25%     | ok               |
|          35 | 3.27%    | -74.11%            | -46.24% |     0.25 |       68 | 31.23%     | ok               |
|          30 | -6.90%   | -74.11%            | -55.89% |     0.2  |       83 | 37.55%     | ok               |
|          50 | -0.01%   | -74.11%            | -43.65% |     0.19 |       40 | 16.09%     | ok               |
|          45 | -13.01%  | -74.11%            | -40.57% |     0.02 |       58 | 20.31%     | ok               |

## IEF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.92%   | -0.57%             | -9.79%  |    -0.82 |       70 | 42.26%     | ok               |
|          15 | -7.48%   | -0.57%             | -10.52% |    -0.88 |       69 | 43.76%     | ok               |
|          40 | -8.39%   | -0.57%             | -9.67%  |    -1.31 |       60 | 24.79%     | ok               |
|          45 | -8.07%   | -0.57%             | -9.73%  |    -1.33 |       50 | 22.80%     | ok               |
|          25 | -10.50%  | -0.57%             | -11.19% |    -1.34 |       76 | 39.43%     | ok               |

## IEMG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -2.20%   | 60.87%             | -23.59% |    -0.01 |       65 | 42.43%     | ok               |
|          25 | -4.72%   | 60.87%             | -25.58% |    -0.09 |       59 | 45.42%     | ok               |
|          40 | -4.82%   | 60.87%             | -20.42% |    -0.12 |       64 | 39.60%     | ok               |
|          50 | -4.52%   | 60.87%             | -16.01% |    -0.12 |       58 | 33.78%     | ok               |
|          30 | -5.52%   | 60.87%             | -26.84% |    -0.12 |       58 | 43.59%     | ok               |

## INJ-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -9.97%   | -72.99%            | -53.80% |     0.06 |       42 | 22.61%     | ok               |
|          35 | -18.70%  | -72.99%            | -60.42% |     0.01 |       62 | 32.76%     | ok               |
|          50 | -19.76%  | -72.99%            | -49.35% |    -0.1  |       46 | 19.54%     | ok               |
|          40 | -27.04%  | -72.99%            | -57.21% |    -0.15 |       52 | 28.93%     | ok               |
|          25 | -53.83%  | -72.99%            | -81.57% |    -0.46 |       77 | 43.30%     | ok               |

## INTC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 76.11%   | 183.18%            | -49.32% |     0.74 |       60 | 34.28%     | ok               |
|          15 | 83.79%   | 183.18%            | -53.65% |     0.74 |       82 | 61.06%     | ok               |
|          25 | 75.50%   | 183.18%            | -56.41% |     0.72 |       75 | 51.58%     | ok               |
|          40 | 70.33%   | 183.18%            | -55.86% |     0.7  |       68 | 38.60%     | ok               |
|          20 | 72.70%   | 183.18%            | -52.47% |     0.7  |       82 | 56.57%     | ok               |

## INTU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -2.37%   | -57.84%            | -42.41% |     0.07 |       73 | 28.79%     | ok               |
|          45 | -5.71%   | -57.84%            | -44.25% |     0.02 |       71 | 32.95%     | ok               |
|          40 | -13.28%  | -57.84%            | -48.32% |    -0.13 |       71 | 35.77%     | ok               |
|          25 | -17.13%  | -57.84%            | -42.24% |    -0.17 |       66 | 45.26%     | ok               |
|          15 | -18.73%  | -57.84%            | -47.30% |    -0.19 |       83 | 50.58%     | ok               |

## ITA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 4.45%    | 99.43%             | -21.48% |     0.21 |       76 | 37.77%     | ok               |
|          15 | 0.89%    | 99.43%             | -28.17% |     0.11 |       84 | 59.40%     | ok               |
|          30 | 0.83%    | 99.43%             | -23.75% |     0.1  |       72 | 47.75%     | ok               |
|          35 | -1.32%   | 99.43%             | -23.16% |     0.03 |       76 | 46.09%     | ok               |
|          40 | -2.46%   | 99.43%             | -20.58% |    -0.01 |       78 | 42.60%     | ok               |

## IWM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 8.60%    | 51.71%             | -14.08% |     0.39 |       42 | 31.28%     | ok               |
|          30 | 9.40%    | 51.71%             | -12.83% |     0.39 |       48 | 35.77%     | ok               |
|          25 | 9.50%    | 51.71%             | -13.55% |     0.39 |       50 | 36.94%     | ok               |
|          35 | 8.35%    | 51.71%             | -14.11% |     0.36 |       48 | 33.61%     | ok               |
|          20 | 5.19%    | 51.71%             | -14.08% |     0.24 |       60 | 37.94%     | ok               |

## JNJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 25.34%   | 68.18%             | -10.57% |     1.01 |       56 | 37.44%     | ok               |
|          45 | 15.35%   | 68.18%             | -13.35% |     0.63 |       58 | 42.43%     | ok               |
|          15 | 18.08%   | 68.18%             | -18.02% |     0.62 |       67 | 57.07%     | ok               |
|          40 | 12.83%   | 68.18%             | -14.77% |     0.52 |       64 | 46.59%     | ok               |
|          20 | 14.08%   | 68.18%             | -17.61% |     0.52 |       71 | 53.74%     | ok               |

## JPM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 22.39%   | 91.34%             | -15.90% |     0.72 |       52 | 41.60%     | ok               |
|          45 | 10.76%   | 91.34%             | -21.91% |     0.37 |       54 | 44.59%     | ok               |
|          40 | -3.86%   | 91.34%             | -28.47% |    -0.03 |       66 | 47.09%     | ok               |
|          20 | -11.04%  | 91.34%             | -33.59% |    -0.16 |       84 | 58.40%     | ok               |
|          35 | -9.23%   | 91.34%             | -27.43% |    -0.18 |       72 | 50.75%     | ok               |

## KO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 28.93%   | 40.63%             | -8.07%  |     1.03 |       49 | 37.77%     | ok               |
|          35 | 24.98%   | 40.63%             | -8.07%  |     0.93 |       52 | 36.44%     | ok               |
|          40 | 22.37%   | 40.63%             | -9.28%  |     0.9  |       54 | 33.28%     | ok               |
|          25 | 23.60%   | 40.63%             | -9.37%  |     0.86 |       55 | 40.43%     | ok               |
|          50 | 14.81%   | 40.63%             | -11.40% |     0.68 |       36 | 26.79%     | ok               |

## LDO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 24.99%   | -85.37%            | -46.95% |     0.48 |       81 | 51.92%     | ok               |
|          20 | 13.39%   | -85.37%            | -44.97% |     0.4  |       85 | 47.32%     | ok               |
|          50 | 15.22%   | -85.37%            | -48.04% |     0.37 |       46 | 16.86%     | ok               |
|          30 | -1.03%   | -85.37%            | -60.93% |     0.26 |       76 | 38.12%     | ok               |
|          35 | -3.23%   | -85.37%            | -62.61% |     0.22 |       74 | 31.23%     | ok               |

## LIN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 5.16%    | 32.04%             | -23.68% |     0.23 |       62 | 49.42%     | ok               |
|          25 | 4.87%    | 32.04%             | -22.01% |     0.23 |       61 | 41.43%     | ok               |
|          20 | 2.62%    | 32.04%             | -23.00% |     0.15 |       60 | 44.59%     | ok               |
|          35 | 1.08%    | 32.04%             | -21.18% |     0.1  |       60 | 32.11%     | ok               |
|          30 | 0.44%    | 32.04%             | -21.53% |     0.08 |       64 | 38.60%     | ok               |

## LINK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -16.15%  | -65.70%            | -49.35% |     0.07 |       71 | 41.76%     | ok               |
|          45 | -13.28%  | -65.70%            | -38.11% |     0.05 |       50 | 26.63%     | ok               |
|          50 | -12.86%  | -65.70%            | -36.52% |     0.03 |       40 | 21.26%     | ok               |
|          35 | -24.33%  | -65.70%            | -49.18% |    -0.05 |       59 | 36.78%     | ok               |
|          40 | -28.49%  | -65.70%            | -50.55% |    -0.14 |       55 | 31.03%     | ok               |

## LLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 7.21%    | 65.01%             | -38.23% |     0.25 |       46 | 37.94%     | ok               |
|          15 | 0.12%    | 65.01%             | -48.12% |     0.15 |       63 | 61.73%     | ok               |
|          45 | -4.85%   | 65.01%             | -42.66% |     0.03 |       54 | 41.43%     | ok               |
|          20 | -16.00%  | 65.01%             | -51.34% |    -0.13 |       72 | 56.74%     | ok               |
|          25 | -17.39%  | 65.01%             | -53.47% |    -0.16 |       68 | 54.08%     | ok               |

## LRCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -2.47%   | 306.56%            | -60.45% |     0.17 |       83 | 55.57%     | ok               |
|          50 | -8.09%   | 306.56%            | -50.39% |     0.07 |       80 | 37.44%     | ok               |
|          40 | -10.85%  | 306.56%            | -56.86% |     0.05 |       72 | 43.26%     | ok               |
|          35 | -16.64%  | 306.56%            | -61.76% |    -0.02 |       80 | 45.26%     | ok               |
|          20 | -19.05%  | 306.56%            | -67.64% |    -0.04 |       87 | 51.25%     | ok               |

## LTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -12.22%  | -60.74%            | -44.78% |    -0    |       56 | 31.80%     | ok               |
|          35 | -22.47%  | -60.74%            | -54.86% |    -0.13 |       66 | 42.91%     | ok               |
|          30 | -34.00%  | -60.74%            | -53.76% |    -0.29 |       66 | 48.47%     | ok               |
|          40 | -31.40%  | -60.74%            | -56.10% |    -0.3  |       58 | 38.12%     | ok               |
|          25 | -36.79%  | -60.74%            | -54.26% |    -0.33 |       74 | 50.96%     | ok               |

## MCD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 2.85%    | -3.87%             | -9.22%  |     0.19 |       42 | 20.63%     | ok               |
|          30 | -2.55%   | -3.87%             | -18.81% |    -0.05 |       75 | 38.10%     | ok               |
|          25 | -3.59%   | -3.87%             | -20.47% |    -0.09 |       75 | 40.77%     | ok               |
|          35 | -7.68%   | -3.87%             | -15.45% |    -0.29 |       67 | 34.44%     | ok               |
|          40 | -7.95%   | -3.87%             | -16.86% |    -0.33 |       71 | 28.79%     | ok               |

## META Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -8.61%   | 24.02%             | -31.03% |    -0.07 |       66 | 38.60%     | ok               |
|          40 | -18.65%  | 24.02%             | -35.11% |    -0.28 |       66 | 41.60%     | ok               |
|          25 | -26.68%  | 24.02%             | -39.84% |    -0.41 |       67 | 52.25%     | ok               |
|          50 | -22.56%  | 24.02%             | -34.00% |    -0.42 |       70 | 34.78%     | ok               |
|          30 | -28.65%  | 24.02%             | -38.96% |    -0.48 |       72 | 49.08%     | ok               |

## MPC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 12.46%   | 56.97%             | -23.96% |     0.34 |       52 | 38.27%     | ok               |
|          45 | 5.33%    | 56.97%             | -25.09% |     0.21 |       58 | 41.93%     | ok               |
|          40 | 3.73%    | 56.97%             | -25.70% |     0.18 |       60 | 44.26%     | ok               |
|          35 | 0.52%    | 56.97%             | -35.90% |     0.13 |       68 | 46.76%     | ok               |
|          30 | -15.29%  | 56.97%             | -44.76% |    -0.17 |       71 | 49.58%     | ok               |

## MRK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -21.32%  | 2.33%              | -30.12% |    -0.4  |       87 | 56.07%     | ok               |
|          25 | -20.94%  | 2.33%              | -31.07% |    -0.43 |       72 | 48.09%     | ok               |
|          20 | -24.81%  | 2.33%              | -29.59% |    -0.53 |       77 | 51.41%     | ok               |
|          45 | -23.75%  | 2.33%              | -26.02% |    -0.64 |       57 | 34.28%     | ok               |
|          50 | -23.40%  | 2.33%              | -25.69% |    -0.67 |       56 | 31.28%     | ok               |

## MS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -4.22%   | 149.77%            | -19.99% |    -0.02 |       70 | 41.10%     | ok               |
|          35 | -10.89%  | 149.77%            | -25.26% |    -0.19 |       74 | 45.76%     | ok               |
|          15 | -14.62%  | 149.77%            | -23.25% |    -0.23 |       78 | 58.57%     | ok               |
|          20 | -14.73%  | 149.77%            | -25.68% |    -0.26 |       82 | 54.74%     | ok               |
|          30 | -16.46%  | 149.77%            | -27.79% |    -0.34 |       81 | 49.75%     | ok               |

## MSFT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -22.75%  | -5.70%             | -25.28% |    -0.64 |       64 | 35.11%     | ok               |
|          50 | -25.88%  | -5.70%             | -28.69% |    -0.77 |       62 | 30.45%     | ok               |
|          35 | -33.83%  | -5.70%             | -34.82% |    -0.9  |       73 | 43.43%     | ok               |
|          40 | -34.62%  | -5.70%             | -35.60% |    -0.97 |       69 | 38.44%     | ok               |
|          25 | -37.89%  | -5.70%             | -38.82% |    -0.98 |       87 | 51.25%     | ok               |

## MU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 421.65%  | 1049.34%           | -61.96% |     1.55 |       48 | 68.05%     | ok               |
|          25 | 334.60%  | 1049.34%           | -67.90% |     1.46 |       49 | 61.73%     | ok               |
|          40 | 287.64%  | 1049.34%           | -64.36% |     1.39 |       56 | 55.41%     | ok               |
|          20 | 297.89%  | 1049.34%           | -67.25% |     1.37 |       55 | 63.89%     | ok               |
|          30 | 270.20%  | 1049.34%           | -68.76% |     1.34 |       51 | 59.90%     | ok               |

## NEAR-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 103.12%  | -54.24%            | -48.01% |     0.99 |       44 | 23.37%     | ok               |
|          50 | 70.90%   | -54.24%            | -53.13% |     0.82 |       38 | 18.39%     | ok               |
|          40 | 60.91%   | -54.24%            | -56.35% |     0.73 |       48 | 27.78%     | ok               |
|          35 | 33.68%   | -54.24%            | -60.50% |     0.53 |       70 | 33.14%     | ok               |
|          15 | 2.00%    | -54.24%            | -54.94% |     0.31 |       89 | 56.13%     | ok               |

## NEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 2.42%    | 191.06%            | -29.41% |     0.2  |       64 | 61.73%     | ok               |
|          20 | -8.55%   | 191.06%            | -30.47% |     0.06 |       74 | 57.24%     | ok               |
|          25 | -21.89%  | 191.06%            | -37.89% |    -0.15 |       70 | 55.07%     | ok               |
|          50 | -25.02%  | 191.06%            | -33.36% |    -0.27 |       58 | 40.43%     | ok               |
|          30 | -31.68%  | 191.06%            | -38.49% |    -0.34 |       74 | 53.41%     | ok               |

## NFLX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 54.62%   | 39.03%             | -11.94% |     1.08 |       46 | 47.25%     | ok               |
|          50 | 48.36%   | 39.03%             | -16.28% |     1.05 |       48 | 39.60%     | ok               |
|          35 | 46.68%   | 39.03%             | -18.30% |     0.92 |       60 | 50.75%     | ok               |
|          45 | 37.90%   | 39.03%             | -15.48% |     0.83 |       52 | 43.59%     | ok               |
|          25 | 36.29%   | 39.03%             | -21.09% |     0.74 |       60 | 57.24%     | ok               |

## NKE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -33.86%  | -57.51%            | -50.44% |    -0.42 |       93 | 52.58%     | ok               |
|          40 | -26.46%  | -57.51%            | -31.19% |    -0.5  |       63 | 30.12%     | ok               |
|          15 | -38.38%  | -57.51%            | -55.52% |    -0.51 |       91 | 56.91%     | ok               |
|          25 | -45.09%  | -57.51%            | -52.84% |    -0.79 |       91 | 48.59%     | ok               |
|          35 | -39.10%  | -57.51%            | -43.08% |    -0.8  |       75 | 37.10%     | ok               |

## NOW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 8.42%    | -33.50%            | -26.36% |     0.27 |       79 | 51.75%     | ok               |
|          30 | 6.62%    | -33.50%            | -30.25% |     0.24 |       80 | 45.76%     | ok               |
|          15 | 1.21%    | -33.50%            | -26.36% |     0.19 |       88 | 54.91%     | ok               |
|          25 | 0.09%    | -33.50%            | -25.74% |     0.17 |       74 | 49.25%     | ok               |
|          35 | -0.27%   | -33.50%            | -29.30% |     0.14 |       81 | 40.43%     | ok               |

## NVDA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -1.32%   | 123.60%            | -35.26% |     0.14 |       70 | 47.59%     | ok               |
|          25 | -2.29%   | 123.60%            | -33.22% |     0.14 |       66 | 50.09%     | ok               |
|          20 | -6.31%   | 123.60%            | -40.59% |     0.09 |       69 | 54.90%     | ok               |
|          35 | -14.66%  | 123.60%            | -41.25% |    -0.08 |       78 | 44.74%     | ok               |
|          50 | -14.29%  | 123.60%            | -40.84% |    -0.11 |       56 | 32.09%     | ok               |

## OP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 50.84%   | -92.62%            | -36.11% |     0.73 |       32 | 12.07%     | ok               |
|          45 | 49.75%   | -92.62%            | -45.76% |     0.68 |       34 | 16.67%     | ok               |
|          40 | 27.95%   | -92.62%            | -53.61% |     0.49 |       48 | 25.10%     | ok               |
|          35 | 6.49%    | -92.62%            | -58.33% |     0.29 |       56 | 28.16%     | ok               |
|          30 | -12.93%  | -92.62%            | -70.27% |     0.11 |       72 | 34.67%     | ok               |

## ORCL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 200.86%  | 20.22%             | -29.32% |     1.26 |       74 | 65.22%     | ok               |
|          25 | 125.70%  | 20.22%             | -27.76% |     1    |       75 | 57.74%     | ok               |
|          20 | 121.82%  | 20.22%             | -29.32% |     0.97 |       77 | 60.90%     | ok               |
|          35 | 93.51%   | 20.22%             | -31.95% |     0.87 |       68 | 49.42%     | ok               |
|          30 | 93.68%   | 20.22%             | -29.47% |     0.86 |       74 | 53.58%     | ok               |

## OXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 8.55%    | -15.75%            | -31.37% |     0.26 |       67 | 43.26%     | ok               |
|          35 | 4.08%    | -15.75%            | -31.78% |     0.19 |       68 | 38.77%     | ok               |
|          40 | 1.53%    | -15.75%            | -33.45% |     0.14 |       56 | 34.78%     | ok               |
|          50 | 0.86%    | -15.75%            | -30.54% |     0.12 |       36 | 27.79%     | ok               |
|          25 | -5.18%   | -15.75%            | -40.06% |     0.03 |       73 | 47.25%     | ok               |

## PEP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 13.45%   | -17.04%            | -11.62% |     0.6  |       44 | 26.79%     | ok               |
|          45 | 4.86%    | -17.04%            | -14.22% |     0.25 |       64 | 31.28%     | ok               |
|          40 | -3.61%   | -17.04%            | -18.04% |    -0.08 |       80 | 37.44%     | ok               |
|          35 | -4.69%   | -17.04%            | -21.42% |    -0.09 |       87 | 42.43%     | ok               |
|          30 | -10.20%  | -17.04%            | -21.35% |    -0.24 |       83 | 49.08%     | ok               |

## PEPE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 14.96%   | -78.50%            | -61.96% |     0.43 |       78 | 60.34%     | ok               |
|          30 | 14.92%   | -78.50%            | -57.66% |     0.4  |       79 | 44.83%     | ok               |
|          35 | 8.37%    | -78.50%            | -51.35% |     0.33 |       64 | 39.46%     | ok               |
|          25 | -5.95%   | -78.50%            | -53.88% |     0.23 |       85 | 50.00%     | ok               |
|          20 | -10.37%  | -78.50%            | -61.13% |     0.21 |       84 | 56.70%     | ok               |

## PFE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -24.42%  | -11.79%            | -25.27% |    -0.9  |       50 | 18.64%     | ok               |
|          50 | -25.58%  | -11.79%            | -26.42% |    -1.04 |       38 | 15.14%     | ok               |
|          35 | -32.80%  | -11.79%            | -34.05% |    -1.07 |       84 | 30.95%     | ok               |
|          40 | -31.49%  | -11.79%            | -32.26% |    -1.12 |       74 | 23.63%     | ok               |
|          30 | -39.75%  | -11.79%            | -40.87% |    -1.29 |       77 | 34.94%     | ok               |

## PG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -3.25%   | -4.56%             | -20.08% |    -0.09 |       54 | 34.61%     | ok               |
|          35 | -6.55%   | -4.56%             | -18.99% |    -0.22 |       62 | 38.10%     | ok               |
|          45 | -12.71%  | -4.56%             | -20.75% |    -0.53 |       54 | 32.11%     | ok               |
|          30 | -15.05%  | -4.56%             | -21.96% |    -0.55 |       64 | 41.26%     | ok               |
|          25 | -16.07%  | -4.56%             | -22.86% |    -0.59 |       74 | 42.43%     | ok               |

## PM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -2.02%   | 104.77%            | -32.20% |     0.05 |       90 | 52.91%     | ok               |
|          20 | -4.75%   | 104.77%            | -31.89% |    -0    |       87 | 61.90%     | ok               |
|          30 | -5.17%   | 104.77%            | -33.68% |    -0.02 |       83 | 56.91%     | ok               |
|          50 | -6.95%   | 104.77%            | -35.70% |    -0.09 |       74 | 42.10%     | ok               |
|          40 | -9.40%   | 104.77%            | -37.94% |    -0.14 |       82 | 48.59%     | ok               |

## POL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 66.27%   | -81.22%            | -46.45% |     0.77 |       79 | 50.77%     | ok               |
|          25 | 69.33%   | -81.22%            | -46.72% |     0.77 |       64 | 58.62%     | ok               |
|          20 | 56.30%   | -81.22%            | -52.88% |     0.68 |       70 | 62.84%     | ok               |
|          15 | 39.48%   | -81.22%            | -58.42% |     0.57 |       72 | 67.62%     | ok               |
|          50 | 18.38%   | -81.22%            | -22.86% |     0.42 |       52 | 20.88%     | ok               |

## QCOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -0.20%   | 18.94%             | -54.50% |     0.17 |       73 | 48.42%     | ok               |
|          35 | -0.76%   | 18.94%             | -50.58% |     0.15 |       79 | 44.26%     | ok               |
|          20 | -4.25%   | 18.94%             | -54.38% |     0.12 |       69 | 51.25%     | ok               |
|          30 | -12.01%  | 18.94%             | -56.59% |     0.01 |       75 | 46.76%     | ok               |
|          15 | -20.16%  | 18.94%             | -57.94% |    -0.09 |       73 | 54.41%     | ok               |

## QQQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 20.70%   | 64.65%             | -12.88% |     0.57 |       61 | 47.92%     | ok               |
|          15 | 21.22%   | 64.65%             | -14.17% |     0.55 |       65 | 53.41%     | ok               |
|          30 | 16.76%   | 64.65%             | -12.88% |     0.5  |       64 | 45.09%     | ok               |
|          20 | 17.79%   | 64.65%             | -12.98% |     0.49 |       69 | 50.58%     | ok               |
|          35 | 4.82%    | 64.65%             | -19.00% |     0.21 |       70 | 41.43%     | ok               |

## RENDER-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 46.52%   | -61.66%            | -43.43% |     0.62 |       86 | 54.22%     | ok               |
|          15 | 29.51%   | -61.66%            | -44.59% |     0.52 |       86 | 57.23%     | ok               |
|          25 | 17.48%   | -61.66%            | -40.60% |     0.44 |       90 | 50.40%     | ok               |
|          30 | -19.07%  | -61.66%            | -45.00% |     0.1  |       98 | 43.98%     | ok               |
|          35 | -31.74%  | -61.66%            | -41.33% |    -0.12 |       84 | 35.54%     | ok               |

## RTX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 34.63%   | 118.86%            | -18.66% |     0.79 |       78 | 56.24%     | ok               |
|          25 | 29.85%   | 118.86%            | -18.59% |     0.71 |       64 | 52.75%     | ok               |
|          50 | 23.78%   | 118.86%            | -18.42% |     0.71 |       60 | 41.93%     | ok               |
|          35 | 25.18%   | 118.86%            | -18.00% |     0.7  |       56 | 49.75%     | ok               |
|          30 | 27.88%   | 118.86%            | -16.99% |     0.68 |       58 | 51.58%     | ok               |

## SBUX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -15.38%  | 7.95%              | -23.55% |    -0.25 |       65 | 42.10%     | ok               |
|          45 | -18.16%  | 7.95%              | -27.26% |    -0.41 |       70 | 29.95%     | ok               |
|          40 | -20.11%  | 7.95%              | -26.97% |    -0.43 |       62 | 34.28%     | ok               |
|          30 | -22.61%  | 7.95%              | -29.22% |    -0.45 |       64 | 39.77%     | ok               |
|          35 | -24.12%  | 7.95%              | -29.75% |    -0.51 |       60 | 37.10%     | ok               |

## SCHW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 1.82%    | 55.27%             | -16.53% |     0.12 |       58 | 33.78%     | ok               |
|          50 | -2.16%   | 55.27%             | -13.28% |    -0.01 |       54 | 31.28%     | ok               |
|          25 | -8.37%   | 55.27%             | -28.76% |    -0.11 |       65 | 48.59%     | ok               |
|          20 | -10.08%  | 55.27%             | -29.24% |    -0.15 |       73 | 51.25%     | ok               |
|          40 | -8.74%   | 55.27%             | -23.35% |    -0.17 |       66 | 36.77%     | ok               |

## SHIB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 0.07%    | -76.32%            | -49.21% |     0.25 |       80 | 69.54%     | ok               |
|          25 | -12.55%  | -76.32%            | -43.85% |     0.1  |       77 | 59.96%     | ok               |
|          20 | -13.84%  | -76.32%            | -46.92% |     0.09 |       79 | 64.56%     | ok               |
|          35 | -16.32%  | -76.32%            | -53.32% |     0.01 |       66 | 46.93%     | ok               |
|          40 | -19.26%  | -76.32%            | -50.74% |    -0.05 |       56 | 39.46%     | ok               |

## SHY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          30 | -2.24%   | 0.12%              | -2.85% |    -0.79 |       48 | 34.28%     | ok               |
|          35 | -2.36%   | 0.12%              | -3.27% |    -0.84 |       50 | 32.45%     | ok               |
|          40 | -2.47%   | 0.12%              | -3.33% |    -0.89 |       50 | 30.62%     | ok               |
|          45 | -2.45%   | 0.12%              | -3.23% |    -0.9  |       48 | 27.45%     | ok               |
|          50 | -2.62%   | 0.12%              | -3.40% |    -1.01 |       44 | 24.63%     | ok               |

## SKY-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -28.56%  | 3.75%              | -43.98% |    -0.35 |       70 | 41.04%     | ok               |
|          15 | -32.92%  | 3.75%              | -56.39% |    -0.35 |       60 | 51.25%     | ok               |
|          25 | -32.22%  | 3.75%              | -48.09% |    -0.4  |       65 | 44.67%     | ok               |
|          20 | -42.55%  | 3.75%              | -58.40% |    -0.59 |       62 | 48.30%     | ok               |
|          35 | -39.77%  | 3.75%              | -49.68% |    -0.7  |       64 | 34.69%     | ok               |

## SLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 25.38%   | -5.57%             | -23.07% |     0.58 |       46 | 36.27%     | ok               |
|          45 | 22.37%   | -5.57%             | -20.46% |     0.54 |       54 | 32.78%     | ok               |
|          35 | -6.10%   | -5.57%             | -41.81% |    -0.02 |       74 | 44.26%     | ok               |
|          50 | -4.32%   | -5.57%             | -30.82% |    -0.02 |       52 | 28.45%     | ok               |
|          30 | -20.81%  | -5.57%             | -54.13% |    -0.32 |       77 | 50.92%     | ok               |

## SLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 70.89%   | 166.44%            | -34.10% |     0.88 |       52 | 34.61%     | ok               |
|          45 | 68.18%   | 166.44%            | -31.82% |     0.86 |       56 | 35.44%     | ok               |
|          40 | 66.17%   | 166.44%            | -31.93% |     0.84 |       62 | 37.60%     | ok               |
|          35 | 53.02%   | 166.44%            | -36.89% |     0.73 |       64 | 39.77%     | ok               |
|          30 | 44.14%   | 166.44%            | -42.66% |     0.64 |       58 | 41.93%     | ok               |

## SMH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 112.10%  | 196.99%            | -30.17% |     1.29 |       47 | 52.08%     | ok               |
|          35 | 89.82%   | 196.99%            | -34.36% |     1.16 |       54 | 47.92%     | ok               |
|          25 | 89.68%   | 196.99%            | -32.94% |     1.15 |       46 | 50.92%     | ok               |
|          30 | 87.45%   | 196.99%            | -33.99% |     1.13 |       48 | 49.25%     | ok               |
|          45 | 73.81%   | 196.99%            | -32.75% |     1.09 |       52 | 42.10%     | ok               |

## SNX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -0.15%   | -83.31%            | -43.20% |     0.28 |       73 | 48.66%     | ok               |
|          35 | -7.07%   | -83.31%            | -30.08% |     0.17 |       66 | 31.61%     | ok               |
|          30 | -16.00%  | -83.31%            | -34.76% |     0.08 |       62 | 38.70%     | ok               |
|          15 | -32.75%  | -83.31%            | -47.56% |    -0.05 |       83 | 53.26%     | ok               |
|          25 | -29.34%  | -83.31%            | -38.88% |    -0.07 |       74 | 43.10%     | ok               |

## SOL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -9.04%   | -64.48%            | -54.68% |     0.14 |       62 | 38.31%     | ok               |
|          25 | -24.96%  | -64.48%            | -53.21% |     0    |       72 | 56.70%     | ok               |
|          35 | -26.03%  | -64.48%            | -61.96% |    -0.03 |       72 | 45.79%     | ok               |
|          15 | -30.85%  | -64.48%            | -59.14% |    -0.05 |       74 | 63.79%     | ok               |
|          20 | -35.74%  | -64.48%            | -56.90% |    -0.13 |       68 | 59.20%     | ok               |

## SOXX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 89.78%   | 175.30%            | -40.27% |     1.09 |       55 | 50.58%     | ok               |
|          35 | 85.80%   | 175.30%            | -38.63% |     1.08 |       59 | 45.76%     | ok               |
|          25 | 86.15%   | 175.30%            | -41.42% |     1.07 |       53 | 50.25%     | ok               |
|          15 | 85.02%   | 175.30%            | -39.35% |     1.02 |       68 | 53.41%     | ok               |
|          30 | 75.69%   | 175.30%            | -41.89% |     0.99 |       57 | 48.09%     | ok               |

## SPY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 14.64%   | 49.46%             | -14.25% |     0.52 |       61 | 53.91%     | ok               |
|          15 | 13.07%   | 49.46%             | -16.80% |     0.46 |       70 | 57.07%     | ok               |
|          25 | 7.50%    | 49.46%             | -15.22% |     0.31 |       61 | 52.91%     | ok               |
|          30 | 2.96%    | 49.46%             | -16.47% |     0.16 |       64 | 50.08%     | ok               |
|          35 | 2.38%    | 49.46%             | -16.72% |     0.14 |       58 | 47.09%     | ok               |

## SUSHI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -23.49%  | -86.13%            | -40.08% |    -0.19 |       52 | 14.75%     | ok               |
|          45 | -58.58%  | -86.13%            | -64.27% |    -0.77 |       56 | 18.20%     | ok               |
|          40 | -61.52%  | -86.13%            | -68.16% |    -0.77 |       63 | 24.71%     | ok               |
|          15 | -78.36%  | -86.13%            | -79.45% |    -0.94 |       89 | 47.32%     | ok               |
|          35 | -73.65%  | -86.13%            | -79.42% |    -1.03 |       78 | 30.27%     | ok               |

## T Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 67.38%   | 22.35%             | -18.13% |     1.26 |       58 | 56.07%     | ok               |
|          25 | 62.19%   | 22.35%             | -17.66% |     1.2  |       60 | 53.91%     | ok               |
|          15 | 58.24%   | 22.35%             | -15.08% |     1.11 |       67 | 59.90%     | ok               |
|          30 | 44.42%   | 22.35%             | -17.01% |     0.96 |       64 | 51.91%     | ok               |
|          35 | 29.57%   | 22.35%             | -14.49% |     0.73 |       66 | 48.42%     | ok               |

## TGT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -12.29%  | -11.66%            | -42.86% |    -0.13 |       81 | 46.76%     | ok               |
|          45 | -10.91%  | -11.66%            | -29.07% |    -0.18 |       52 | 29.12%     | ok               |
|          25 | -13.17%  | -11.66%            | -43.36% |    -0.18 |       63 | 41.76%     | ok               |
|          15 | -15.16%  | -11.66%            | -40.77% |    -0.18 |       71 | 51.25%     | ok               |
|          30 | -12.54%  | -11.66%            | -40.57% |    -0.18 |       58 | 38.94%     | ok               |

## TIA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 15.64%   | -90.31%            | -36.58% |     0.37 |       68 | 26.25%     | ok               |
|          35 | 15.16%   | -90.31%            | -44.72% |     0.37 |       66 | 31.03%     | ok               |
|          50 | 11.42%   | -90.31%            | -46.02% |     0.32 |       34 | 11.69%     | ok               |
|          45 | 10.81%   | -90.31%            | -46.58% |     0.32 |       54 | 18.97%     | ok               |
|          30 | -28.18%  | -90.31%            | -60.92% |    -0.06 |       90 | 36.02%     | ok               |

## TLT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -13.40%  | -9.07%             | -14.14% |    -1.57 |       32 | 14.14%     | ok               |
|          30 | -21.58%  | -9.07%             | -21.75% |    -1.68 |       68 | 31.61%     | ok               |
|          40 | -18.63%  | -9.07%             | -18.63% |    -1.85 |       58 | 20.63%     | ok               |
|          35 | -21.08%  | -9.07%             | -21.08% |    -1.9  |       66 | 25.62%     | ok               |
|          15 | -27.20%  | -9.07%             | -27.62% |    -1.92 |       75 | 39.77%     | ok               |

## TMO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 45.64%   | -4.98%             | -8.17%  |     1.04 |       40 | 30.62%     | ok               |
|          45 | 41.41%   | -4.98%             | -10.13% |     0.91 |       46 | 35.44%     | ok               |
|          40 | 39.32%   | -4.98%             | -9.91%  |     0.86 |       49 | 39.93%     | ok               |
|          35 | 21.59%   | -4.98%             | -14.06% |     0.53 |       61 | 44.43%     | ok               |
|          30 | 13.93%   | -4.98%             | -18.85% |     0.38 |       61 | 49.08%     | ok               |

## TMUS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 13.98%   | 10.31%             | -26.87% |     0.37 |       69 | 60.07%     | ok               |
|          30 | 12.74%   | 10.31%             | -24.50% |     0.36 |       70 | 48.09%     | ok               |
|          20 | 4.77%    | 10.31%             | -26.83% |     0.2  |       73 | 54.24%     | ok               |
|          25 | 3.83%    | 10.31%             | -28.01% |     0.18 |       75 | 50.58%     | ok               |
|          35 | 0.14%    | 10.31%             | -30.93% |     0.1  |       68 | 44.76%     | ok               |

## TRX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 6.87%    | 32.26%             | -18.79% |     0.28 |       52 | 37.16%     | ok               |
|          30 | 0.99%    | 32.26%             | -22.90% |     0.12 |       72 | 49.04%     | ok               |
|          50 | 0.66%    | 32.26%             | -18.49% |     0.1  |       44 | 31.99%     | ok               |
|          35 | 0.16%    | 32.26%             | -21.77% |     0.09 |       68 | 45.79%     | ok               |
|          45 | -0.23%   | 32.26%             | -18.27% |     0.07 |       44 | 33.52%     | ok               |

## TSLA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 72.03%   | 107.56%            | -31.33% |     0.82 |       62 | 34.28%     | ok               |
|          50 | 48.84%   | 107.56%            | -33.23% |     0.67 |       64 | 29.78%     | ok               |
|          45 | 45.74%   | 107.56%            | -32.54% |     0.63 |       66 | 31.61%     | ok               |
|          35 | 35.59%   | 107.56%            | -37.58% |     0.53 |       71 | 36.94%     | ok               |
|          30 | 9.97%    | 107.56%            | -42.22% |     0.29 |       69 | 41.43%     | ok               |

## TXN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 11.70%   | 82.93%             | -45.45% |     0.31 |       70 | 35.44%     | ok               |
|          20 | 2.52%    | 82.93%             | -38.49% |     0.19 |       62 | 60.07%     | ok               |
|          15 | -0.42%   | 82.93%             | -38.99% |     0.15 |       65 | 64.06%     | ok               |
|          35 | -3.89%   | 82.93%             | -43.28% |     0.07 |       80 | 50.75%     | ok               |
|          40 | -6.50%   | 82.93%             | -45.67% |     0.03 |       76 | 48.42%     | ok               |

## UNH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 33.25%   | -18.21%            | -36.82% |     0.58 |       52 | 30.62%     | ok               |
|          30 | 33.82%   | -18.21%            | -26.96% |     0.56 |       74 | 52.41%     | ok               |
|          15 | 34.32%   | -18.21%            | -32.14% |     0.55 |       74 | 67.22%     | ok               |
|          35 | 30.18%   | -18.21%            | -28.32% |     0.53 |       66 | 47.25%     | ok               |
|          40 | 22.09%   | -18.21%            | -35.73% |     0.44 |       60 | 42.76%     | ok               |

## UNI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -29.92%  | -71.20%            | -58.49% |    -0.16 |       56 | 26.05%     | ok               |
|          40 | -34.51%  | -71.20%            | -63.75% |    -0.2  |       58 | 31.03%     | ok               |
|          50 | -36.00%  | -71.20%            | -57.60% |    -0.3  |       54 | 21.26%     | ok               |
|          35 | -45.03%  | -71.20%            | -68.71% |    -0.32 |       72 | 36.02%     | ok               |
|          20 | -77.25%  | -71.20%            | -83.06% |    -0.87 |      105 | 52.87%     | ok               |

## UPS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -33.13%  | -25.19%            | -43.74% |    -0.6  |       84 | 48.75%     | ok               |
|          35 | -32.12%  | -25.19%            | -38.06% |    -0.63 |       63 | 34.28%     | ok               |
|          25 | -34.19%  | -25.19%            | -40.09% |    -0.65 |       80 | 45.26%     | ok               |
|          15 | -37.19%  | -25.19%            | -45.98% |    -0.69 |       92 | 53.58%     | ok               |
|          30 | -35.75%  | -25.19%            | -38.75% |    -0.71 |       70 | 40.27%     | ok               |

## USO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 15.47%   | 45.39%             | -33.25% |     0.37 |       50 | 26.79%     | ok               |
|          30 | 7.65%    | 45.39%             | -43.35% |     0.25 |       68 | 34.28%     | ok               |
|          15 | 5.70%    | 45.39%             | -46.93% |     0.22 |       73 | 42.26%     | ok               |
|          50 | 3.92%    | 45.39%             | -31.13% |     0.18 |       52 | 24.13%     | ok               |
|          40 | 3.66%    | 45.39%             | -41.14% |     0.18 |       61 | 29.45%     | ok               |

## VEA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 5.44%    | 49.17%             | -16.28% |     0.25 |       60 | 50.58%     | ok               |
|          20 | 1.19%    | 49.17%             | -17.70% |     0.1  |       61 | 47.92%     | ok               |
|          25 | -0.82%   | 49.17%             | -17.79% |     0.02 |       57 | 46.26%     | ok               |
|          30 | -0.98%   | 49.17%             | -17.93% |     0.01 |       58 | 44.09%     | ok               |
|          35 | -2.09%   | 49.17%             | -16.79% |    -0.03 |       56 | 43.09%     | ok               |

## VIXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -46.17%  | -61.73%            | -68.69% |    -0.39 |       44 | 10.32%     | ok               |
|          45 | -56.13%  | -61.73%            | -74.13% |    -0.55 |       56 | 16.31%     | ok               |
|          40 | -64.45%  | -61.73%            | -80.03% |    -0.66 |       70 | 20.63%     | ok               |
|          35 | -68.17%  | -61.73%            | -83.81% |    -0.7  |       86 | 25.79%     | ok               |
|          15 | -79.12%  | -61.73%            | -89.47% |    -0.84 |      102 | 44.59%     | ok               |

## VNQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -8.60%   | 16.34%             | -19.07% |    -0.37 |       60 | 28.62%     | ok               |
|          50 | -9.03%   | 16.34%             | -17.13% |    -0.41 |       56 | 26.12%     | ok               |
|          25 | -13.12%  | 16.34%             | -22.34% |    -0.51 |       69 | 40.77%     | ok               |
|          40 | -14.13%  | 16.34%             | -24.84% |    -0.62 |       74 | 32.11%     | ok               |
|          20 | -16.52%  | 16.34%             | -23.79% |    -0.64 |       74 | 43.59%     | ok               |

## VTI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 18.30%   | 49.06%             | -13.96% |     0.62 |       64 | 54.91%     | ok               |
|          15 | 12.24%   | 49.06%             | -15.70% |     0.44 |       67 | 57.40%     | ok               |
|          25 | 4.62%    | 49.06%             | -16.10% |     0.22 |       60 | 52.91%     | ok               |
|          30 | -2.68%   | 49.06%             | -18.77% |    -0.04 |       70 | 50.92%     | ok               |
|          40 | -4.51%   | 49.06%             | -20.73% |    -0.12 |       70 | 43.93%     | ok               |

## VWO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -7.30%   | 45.89%             | -21.18% |    -0.25 |       60 | 32.61%     | ok               |
|          15 | -9.03%   | 45.89%             | -24.01% |    -0.26 |       69 | 49.42%     | ok               |
|          20 | -10.06%  | 45.89%             | -26.14% |    -0.31 |       67 | 47.25%     | ok               |
|          40 | -8.98%   | 45.89%             | -23.57% |    -0.31 |       70 | 37.94%     | ok               |
|          45 | -9.11%   | 45.89%             | -23.26% |    -0.33 |       62 | 35.11%     | ok               |

## VZ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -6.80%   | 6.64%              | -12.71% |    -0.19 |       50 | 24.29%     | ok               |
|          45 | -16.34%  | 6.64%              | -19.43% |    -0.53 |       60 | 27.45%     | ok               |
|          35 | -19.63%  | 6.64%              | -19.89% |    -0.63 |       63 | 32.95%     | ok               |
|          25 | -22.05%  | 6.64%              | -24.92% |    -0.64 |       83 | 41.26%     | ok               |
|          40 | -23.39%  | 6.64%              | -23.39% |    -0.81 |       66 | 30.12%     | ok               |

## WFC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -1.92%   | 76.86%             | -18.29% |     0.01 |       60 | 34.28%     | ok               |
|          35 | -7.91%   | 76.86%             | -22.53% |    -0.1  |       81 | 46.26%     | ok               |
|          20 | -15.15%  | 76.86%             | -29.87% |    -0.2  |       79 | 55.41%     | ok               |
|          45 | -10.80%  | 76.86%             | -24.02% |    -0.25 |       68 | 39.27%     | ok               |
|          30 | -17.50%  | 76.86%             | -29.78% |    -0.29 |       84 | 49.42%     | ok               |

## WIF-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 60.65%   | -83.71%            | -46.21% |     0.66 |       71 | 41.38%     | ok               |
|          20 | 54.98%   | -83.71%            | -40.67% |     0.64 |       65 | 38.70%     | ok               |
|          25 | -11.37%  | -83.71%            | -52.41% |     0.2  |       67 | 36.21%     | ok               |
|          50 | -20.06%  | -83.71%            | -37.87% |    -0.14 |       40 | 12.07%     | ok               |
|          30 | -43.81%  | -83.71%            | -57.06% |    -0.24 |       68 | 32.18%     | ok               |

## WMT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 56.95%   | 98.10%             | -9.18%  |     1.5  |       36 | 42.60%     | ok               |
|          50 | 50.57%   | 98.10%             | -12.19% |     1.43 |       30 | 40.43%     | ok               |
|          40 | 47.13%   | 98.10%             | -9.18%  |     1.26 |       40 | 43.76%     | ok               |
|          35 | 44.36%   | 98.10%             | -10.48% |     1.17 |       52 | 47.92%     | ok               |
|          30 | 20.12%   | 98.10%             | -21.31% |     0.58 |       59 | 50.58%     | ok               |

## XBI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 10.20%   | 79.85%             | -16.56% |     0.33 |       62 | 35.61%     | ok               |
|          45 | 9.36%    | 79.85%             | -16.74% |     0.31 |       54 | 32.45%     | ok               |
|          35 | 6.83%    | 79.85%             | -20.36% |     0.25 |       62 | 39.10%     | ok               |
|          30 | 5.64%    | 79.85%             | -20.73% |     0.22 |       62 | 40.77%     | ok               |
|          25 | 0.78%    | 79.85%             | -24.31% |     0.11 |       70 | 42.76%     | ok               |

## XLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -1.53%   | 25.39%             | -20.68% |    -0    |       56 | 31.78%     | ok               |
|          50 | -1.59%   | 25.39%             | -17.59% |    -0.01 |       44 | 27.45%     | ok               |
|          35 | -4.77%   | 25.39%             | -23.62% |    -0.12 |       58 | 35.11%     | ok               |
|          45 | -4.50%   | 25.39%             | -20.79% |    -0.13 |       44 | 28.95%     | ok               |
|          25 | -8.23%   | 25.39%             | -23.87% |    -0.24 |       64 | 40.60%     | ok               |

## XLC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 13.24%   | 38.59%             | -12.33% |     0.48 |       65 | 55.24%     | ok               |
|          25 | 11.11%   | 38.59%             | -12.31% |     0.41 |       62 | 57.07%     | ok               |
|          40 | 7.58%    | 38.59%             | -13.38% |     0.32 |       68 | 47.92%     | ok               |
|          35 | 7.56%    | 38.59%             | -13.38% |     0.32 |       64 | 52.41%     | ok               |
|          20 | 3.46%    | 38.59%             | -13.37% |     0.17 |       70 | 59.90%     | ok               |

## XLE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -1.04%   | 25.80%             | -25.98% |     0.04 |       54 | 36.77%     | ok               |
|          35 | -4.77%   | 25.80%             | -32.17% |    -0.04 |       65 | 44.43%     | ok               |
|          45 | -6.14%   | 25.80%             | -30.88% |    -0.1  |       62 | 39.43%     | ok               |
|          25 | -12.25%  | 25.80%             | -37.50% |    -0.23 |       81 | 49.75%     | ok               |
|          30 | -12.28%  | 25.80%             | -37.51% |    -0.24 |       73 | 46.59%     | ok               |

## XLF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -2.64%   | 42.73%             | -18.01% |    -0.03 |       68 | 53.91%     | ok               |
|          15 | -6.67%   | 42.73%             | -19.58% |    -0.16 |       76 | 56.74%     | ok               |
|          30 | -8.64%   | 42.73%             | -23.61% |    -0.26 |       76 | 48.25%     | ok               |
|          25 | -9.43%   | 42.73%             | -23.22% |    -0.28 |       77 | 50.42%     | ok               |
|          35 | -16.02%  | 42.73%             | -26.29% |    -0.61 |       68 | 44.09%     | ok               |

## XLI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 8.59%    | 57.50%             | -10.36% |     0.35 |       72 | 51.91%     | ok               |
|          20 | 4.47%    | 57.50%             | -12.74% |     0.22 |       63 | 47.25%     | ok               |
|          50 | 2.66%    | 57.50%             | -9.25%  |     0.17 |       58 | 34.11%     | ok               |
|          30 | 2.18%    | 57.50%             | -11.38% |     0.14 |       64 | 44.76%     | ok               |
|          45 | 1.72%    | 57.50%             | -12.27% |     0.12 |       64 | 36.27%     | ok               |

## XLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 81.82%   | 76.12%             | -14.75% |     1.32 |       41 | 52.25%     | ok               |
|          20 | 67.59%   | 76.12%             | -14.75% |     1.18 |       48 | 50.08%     | ok               |
|          25 | 64.18%   | 76.12%             | -14.75% |     1.18 |       42 | 47.92%     | ok               |
|          30 | 57.41%   | 76.12%             | -14.75% |     1.11 |       44 | 46.59%     | ok               |
|          35 | 39.93%   | 76.12%             | -16.03% |     0.87 |       54 | 43.93%     | ok               |

## XLM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 26.14%   | -49.75%            | -38.97% |     0.48 |       44 | 27.39%     | ok               |
|          45 | 22.34%   | -49.75%            | -43.99% |     0.44 |       50 | 31.03%     | ok               |
|          30 | 5.21%    | -49.75%            | -50.36% |     0.28 |       69 | 45.79%     | ok               |
|          40 | 1.75%    | -49.75%            | -43.80% |     0.23 |       49 | 35.44%     | ok               |
|          35 | -4.00%   | -49.75%            | -50.42% |     0.17 |       69 | 41.76%     | ok               |

## XLP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 10.15%   | 15.18%             | -6.85%  |     0.63 |       56 | 34.11%     | ok               |
|          40 | 9.44%    | 15.18%             | -7.77%  |     0.57 |       70 | 38.44%     | ok               |
|          50 | 8.23%    | 15.18%             | -7.01%  |     0.53 |       58 | 31.61%     | ok               |
|          35 | 8.49%    | 15.18%             | -9.73%  |     0.51 |       66 | 41.43%     | ok               |
|          30 | 6.56%    | 15.18%             | -11.16% |     0.4  |       68 | 42.93%     | ok               |

## XLU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 7.91%    | 52.43%             | -11.28% |     0.42 |       48 | 30.12%     | ok               |
|          45 | 5.76%    | 52.43%             | -13.05% |     0.32 |       52 | 30.95%     | ok               |
|          40 | 2.84%    | 52.43%             | -14.38% |     0.18 |       56 | 32.45%     | ok               |
|          35 | -3.15%   | 52.43%             | -18.56% |    -0.11 |       60 | 34.61%     | ok               |
|          30 | -4.08%   | 52.43%             | -20.40% |    -0.14 |       67 | 37.77%     | ok               |

## XLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -12.12%  | 13.61%             | -16.83% |    -0.59 |       66 | 35.61%     | ok               |
|          25 | -13.41%  | 13.61%             | -18.06% |    -0.66 |       68 | 36.94%     | ok               |
|          15 | -17.34%  | 13.61%             | -21.47% |    -0.84 |       79 | 41.76%     | ok               |
|          20 | -17.27%  | 13.61%             | -21.56% |    -0.86 |       73 | 38.60%     | ok               |
|          50 | -14.45%  | 13.61%             | -18.24% |    -0.87 |       54 | 24.29%     | ok               |

## XLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 4.62%    | 31.13%             | -12.94% |     0.21 |       72 | 41.26%     | ok               |
|          30 | 2.75%    | 31.13%             | -14.01% |     0.15 |       72 | 44.26%     | ok               |
|          15 | 1.20%    | 31.13%             | -15.77% |     0.11 |       74 | 51.25%     | ok               |
|          50 | 1.30%    | 31.13%             | -11.79% |     0.1  |       50 | 29.62%     | ok               |
|          40 | -1.91%   | 31.13%             | -16.99% |    -0.01 |       68 | 37.10%     | ok               |

## XOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 3.38%    | 31.86%             | -19.90% |     0.17 |       58 | 37.60%     | ok               |
|          30 | 2.35%    | 31.86%             | -20.29% |     0.14 |       58 | 36.94%     | ok               |
|          50 | 0.21%    | 31.86%             | -21.35% |     0.08 |       46 | 29.78%     | ok               |
|          20 | -0.45%   | 31.86%             | -25.56% |     0.06 |       63 | 40.10%     | ok               |
|          35 | -2.00%   | 31.86%             | -20.93% |     0.01 |       60 | 35.77%     | ok               |

## XRP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -24.90%  | -64.36%            | -46.89% |    -0.14 |       70 | 40.04%     | ok               |
|          40 | -31.84%  | -64.36%            | -44.89% |    -0.29 |       60 | 33.91%     | ok               |
|          30 | -38.99%  | -64.36%            | -56.11% |    -0.36 |       74 | 44.44%     | ok               |
|          45 | -39.45%  | -64.36%            | -46.83% |    -0.45 |       60 | 29.69%     | ok               |
|          50 | -36.16%  | -64.36%            | -39.26% |    -0.49 |       62 | 22.22%     | ok               |

## YFI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -32.83%  | -73.98%            | -52.37% |    -0.46 |       62 | 27.20%     | ok               |
|          45 | -38.27%  | -73.98%            | -54.04% |    -0.66 |       64 | 22.61%     | ok               |
|          35 | -49.34%  | -73.98%            | -64.08% |    -0.73 |       73 | 34.67%     | ok               |
|          30 | -52.55%  | -73.98%            | -67.78% |    -0.75 |       81 | 40.80%     | ok               |
|          50 | -41.48%  | -73.98%            | -51.80% |    -0.84 |       52 | 17.43%     | ok               |

## ZEC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 136.96%  | 923.33%            | -24.66% |     0.94 |       46 | 23.18%     | ok               |
|          35 | 102.61%  | 923.33%            | -44.34% |     0.81 |       52 | 30.08%     | ok               |
|          25 | 80.38%   | 923.33%            | -48.59% |     0.72 |       58 | 39.27%     | ok               |
|          50 | 62.89%   | 923.33%            | -34.39% |     0.65 |       48 | 20.69%     | ok               |
|          30 | 62.53%   | 923.33%            | -47.68% |     0.64 |       62 | 35.82%     | ok               |
