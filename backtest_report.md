# Market Tracker Backtest Report

_Generated: 2026-11-11T06:04:09+00:00_

## Data Sources

- Crypto: Kraken -> Coinbase -> CoinGecko OHLC -> CoinPaprika fallback chain.
- Stocks / ETFs / indices: Stooq -> Yahoo Finance fallback chain.
- Data rows are generated from real market APIs. Mock OHLCV rows are not generated.

## Data Freshness

- Rows: **92,786**
- Symbols: **161**
- Date range: **2024-06-20** to **2026-11-11**

## Latest Signals

| symbol     | date                |         close |   composite_score | signal   | data_source   |
|:-----------|:--------------------|--------------:|------------------:|:---------|:--------------|
| ABBV       | 2026-11-10 00:00:00 |   293.89      |          55.75    | LONG     | Yahoo Finance |
| AMGN       | 2026-11-10 00:00:00 |   465.23      |          71.9167  | LONG     | Yahoo Finance |
| BLK        | 2026-11-10 00:00:00 |  1222.15      |          73.5833  | LONG     | Yahoo Finance |
| CL         | 2026-11-10 00:00:00 |    98.09      |          49.4167  | LONG     | Yahoo Finance |
| CMCSA      | 2026-11-10 00:00:00 |    24.75      |          36.9167  | LONG     | Yahoo Finance |
| COST       | 2026-11-10 00:00:00 |  1066.14      |          58.4167  | LONG     | Yahoo Finance |
| DE         | 2026-11-10 00:00:00 |   687.64      |          50.75    | LONG     | Yahoo Finance |
| DIA        | 2026-11-10 00:00:00 |   521.73      |          41.9167  | LONG     | Yahoo Finance |
| DIS        | 2026-11-10 00:00:00 |   119.21      |          73.5833  | LONG     | Yahoo Finance |
| DXY-INDEX  | 2026-11-11 00:00:00 |   102.275     |          56.7204  | LONG     | Yahoo Finance |
| FXI        | 2026-11-10 00:00:00 |    34.41      |          32.3333  | LONG     | Yahoo Finance |
| HD         | 2026-11-10 00:00:00 |   351         |          56.4167  | LONG     | Yahoo Finance |
| JNJ        | 2026-11-10 00:00:00 |   280.78      |          54.4167  | LONG     | Yahoo Finance |
| KO         | 2026-11-10 00:00:00 |    96.91      |          69.5833  | LONG     | Yahoo Finance |
| LIN        | 2026-11-10 00:00:00 |   521.78      |          53.0833  | LONG     | Yahoo Finance |
| LLY        | 2026-11-10 00:00:00 |  1432.29      |          70.25    | LONG     | Yahoo Finance |
| MCD        | 2026-11-10 00:00:00 |   282.17      |          60.5     | LONG     | Yahoo Finance |
| MRK        | 2026-11-10 00:00:00 |   148.05      |          60.75    | LONG     | Yahoo Finance |
| PEP        | 2026-11-10 00:00:00 |   143.61      |          64.3333  | LONG     | Yahoo Finance |
| PEPE-USD   | 2026-11-11 00:00:00 |     5.332e-06 |          62.1667  | LONG     | Kraken API    |
| PG         | 2026-11-10 00:00:00 |   168.66      |          69.0833  | LONG     | Yahoo Finance |
| RTX        | 2026-11-10 00:00:00 |   200.27      |          64.3333  | LONG     | Yahoo Finance |
| SBUX       | 2026-11-10 00:00:00 |   109.95      |          60.0833  | LONG     | Yahoo Finance |
| UNH        | 2026-11-10 00:00:00 |   405.12      |          36.9167  | LONG     | Yahoo Finance |
| UPS        | 2026-11-10 00:00:00 |   111.05      |          55.0833  | LONG     | Yahoo Finance |
| VNQ        | 2026-11-10 00:00:00 |    97.08      |          60.0833  | LONG     | Yahoo Finance |
| WMT        | 2026-11-10 00:00:00 |   125.55      |          49.4167  | LONG     | Yahoo Finance |
| XLB        | 2026-11-10 00:00:00 |    52.85      |          58.4167  | LONG     | Yahoo Finance |
| XLF        | 2026-11-10 00:00:00 |    58.29      |          73.9167  | LONG     | Yahoo Finance |
| XLP        | 2026-11-10 00:00:00 |    91.03      |          51.4167  | LONG     | Yahoo Finance |
| XLU        | 2026-11-10 00:00:00 |    43.73      |          65.8333  | LONG     | Yahoo Finance |
| XLV        | 2026-11-10 00:00:00 |   188.88      |          73.5833  | LONG     | Yahoo Finance |
| XLY        | 2026-11-10 00:00:00 |   121.05      |          60.0833  | LONG     | Yahoo Finance |
| AAPL       | 2026-11-10 00:00:00 |   348.51      |          33.5     | NEUTRAL  | Yahoo Finance |
| AAVE-USD   | 2026-11-11 00:00:00 |   123.87      |         -15.25    | NEUTRAL  | Kraken API    |
| ADBE       | 2026-11-10 00:00:00 |   236.7       |         -51.75    | NEUTRAL  | Yahoo Finance |
| AGG        | 2026-11-10 00:00:00 |    95.88      |          -6.58333 | NEUTRAL  | Yahoo Finance |
| AMD        | 2026-11-10 00:00:00 |   515.21      |         -14.8333  | NEUTRAL  | Yahoo Finance |
| AMZN       | 2026-11-10 00:00:00 |   270.87      |          56.5     | NEUTRAL  | Yahoo Finance |
| ARB-USD    | 2026-11-11 00:00:00 |     0.1621    |          -3.41667 | NEUTRAL  | Kraken API    |
| AVAX-USD   | 2026-11-11 00:00:00 |     8.462     |         -13.25    | NEUTRAL  | Kraken API    |
| AVGO       | 2026-11-10 00:00:00 |   331.98      |         -24.5833  | NEUTRAL  | Yahoo Finance |
| BAC        | 2026-11-10 00:00:00 |    50.68      |         -23.75    | NEUTRAL  | Yahoo Finance |
| BND        | 2026-11-10 00:00:00 |    71.13      |          -6.58333 | NEUTRAL  | Yahoo Finance |
| BONK-USD   | 2026-11-11 00:00:00 |     2.829e-06 |         -43.9167  | NEUTRAL  | Kraken API    |
| C          | 2026-11-10 00:00:00 |   122.27      |         -40.4167  | NEUTRAL  | Yahoo Finance |
| COP        | 2026-11-10 00:00:00 |   135.59      |          -8.58333 | NEUTRAL  | Yahoo Finance |
| DBC        | 2026-11-10 00:00:00 |    30.76      |         -18.5833  | NEUTRAL  | Yahoo Finance |
| DOT-USD    | 2026-11-11 00:00:00 |     0.8432    |         -62.9167  | NEUTRAL  | Kraken API    |
| EFA        | 2026-11-10 00:00:00 |   104.36      |          27.6667  | NEUTRAL  | Yahoo Finance |
| EOG        | 2026-11-10 00:00:00 |   151.51      |          12.25    | NEUTRAL  | Yahoo Finance |
| GDX        | 2026-11-10 00:00:00 |    86.49      |           9.75    | NEUTRAL  | Yahoo Finance |
| GDXJ       | 2026-11-10 00:00:00 |   106.3       |         -15.9167  | NEUTRAL  | Yahoo Finance |
| GE         | 2026-11-10 00:00:00 |   337.91      |          57.5833  | NEUTRAL  | Yahoo Finance |
| GLD        | 2026-11-10 00:00:00 |   369.36      |         -50       | NEUTRAL  | Yahoo Finance |
| GS         | 2026-11-10 00:00:00 |   910.19      |         -11.8333  | NEUTRAL  | Yahoo Finance |
| HBAR-USD   | 2026-11-11 00:00:00 |     0.06575   |         -24.8333  | NEUTRAL  | Kraken API    |
| HON        | 2026-11-10 00:00:00 |   228.22      |          55.9167  | NEUTRAL  | Yahoo Finance |
| HYG        | 2026-11-10 00:00:00 |    77.18      |          -4.75    | NEUTRAL  | Yahoo Finance |
| IBM        | 2026-11-10 00:00:00 |   244.53      |         -11.0833  | NEUTRAL  | Yahoo Finance |
| ICP-USD    | 2026-11-11 00:00:00 |     2.581     |           4.5     | NEUTRAL  | Kraken API    |
| IEF        | 2026-11-10 00:00:00 |    91.01      |          -6.58333 | NEUTRAL  | Yahoo Finance |
| INJ-USD    | 2026-11-11 00:00:00 |     8.246     |          54.0833  | NEUTRAL  | Kraken API    |
| INTU       | 2026-11-10 00:00:00 |   340.44      |          27.0833  | NEUTRAL  | Yahoo Finance |
| ITA        | 2026-11-10 00:00:00 |    72.35      |          25.1667  | NEUTRAL  | Yahoo Finance |
| IWM        | 2026-11-10 00:00:00 |   280.58      |          27.5     | NEUTRAL  | Yahoo Finance |
| JPM        | 2026-11-10 00:00:00 |   342.07      |          61.1667  | NEUTRAL  | Yahoo Finance |
| LDO-USD    | 2026-11-11 00:00:00 |     0.328     |         -22.3333  | NEUTRAL  | Kraken API    |
| MPC        | 2026-11-10 00:00:00 |   389.55      |         -22.5833  | NEUTRAL  | Yahoo Finance |
| MS         | 2026-11-10 00:00:00 |   187.56      |          -4.75    | NEUTRAL  | Yahoo Finance |
| MSFT       | 2026-11-10 00:00:00 |   533.16      |          25.5     | NEUTRAL  | Yahoo Finance |
| NEAR-USD   | 2026-11-11 00:00:00 |     3.6582    |         -24.5833  | NEUTRAL  | Kraken API    |
| NEM        | 2026-11-10 00:00:00 |   119.96      |          37.3333  | NEUTRAL  | Yahoo Finance |
| NKE        | 2026-11-10 00:00:00 |    38.67      |          28.9167  | NEUTRAL  | Yahoo Finance |
| PFE        | 2026-11-10 00:00:00 |    29.36      |          25.9167  | NEUTRAL  | Yahoo Finance |
| PM         | 2026-11-10 00:00:00 |   194.25      |          -5.33333 | NEUTRAL  | Yahoo Finance |
| POL-USD    | 2026-11-11 00:00:00 |     0.0888    |         -18.6667  | NEUTRAL  | Kraken API    |
| QCOM       | 2026-11-10 00:00:00 |   173.53      |          -2       | NEUTRAL  | Yahoo Finance |
| RENDER-USD | 2026-11-11 00:00:00 |     1.59      |         -17       | NEUTRAL  | Kraken API    |
| SCHW       | 2026-11-10 00:00:00 |    93.03      |           4.41667 | NEUTRAL  | Yahoo Finance |
| SHY        | 2026-11-10 00:00:00 |    81.32      |          -4.33333 | NEUTRAL  | Yahoo Finance |
| SLB        | 2026-11-10 00:00:00 |    49.9       |         -46.5     | NEUTRAL  | Yahoo Finance |
| SPY        | 2026-11-10 00:00:00 |   749.92      |         -11.5833  | NEUTRAL  | Yahoo Finance |
| T          | 2026-11-10 00:00:00 |    21.94      |         -20.5833  | NEUTRAL  | Yahoo Finance |
| TGT        | 2026-11-10 00:00:00 |   161.78      |          60.8333  | NEUTRAL  | Yahoo Finance |
| TLT        | 2026-11-10 00:00:00 |    80.88      |         -15.5833  | NEUTRAL  | Yahoo Finance |
| TMO        | 2026-11-10 00:00:00 |   718.2       |          48.8333  | NEUTRAL  | Yahoo Finance |
| TMUS       | 2026-11-10 00:00:00 |   169.08      |          17.8333  | NEUTRAL  | Yahoo Finance |
| TSLA       | 2026-11-10 00:00:00 |   379.78      |          10.6667  | NEUTRAL  | Yahoo Finance |
| TXN        | 2026-11-10 00:00:00 |   300.52      |          38.8333  | NEUTRAL  | Yahoo Finance |
| UNI-USD    | 2026-11-11 00:00:00 |     6.6729    |         -10.5833  | NEUTRAL  | Kraken API    |
| USO        | 2026-11-10 00:00:00 |   141.45      |         -17.25    | NEUTRAL  | Yahoo Finance |
| VEA        | 2026-11-10 00:00:00 |    69.36      |         -18.5     | NEUTRAL  | Yahoo Finance |
| VIXY       | 2026-11-10 00:00:00 |    18.16      |          21.1667  | NEUTRAL  | Yahoo Finance |
| VTI        | 2026-11-10 00:00:00 |   369.55      |         -11.5833  | NEUTRAL  | Yahoo Finance |
| VZ         | 2026-11-10 00:00:00 |    46.31      |          48.5833  | NEUTRAL  | Yahoo Finance |
| WFC        | 2026-11-10 00:00:00 |    85.76      |          61.1667  | NEUTRAL  | Yahoo Finance |
| XBI        | 2026-11-10 00:00:00 |   155.06      |          59.1667  | NEUTRAL  | Yahoo Finance |
| XLC        | 2026-11-10 00:00:00 |   107.76      |          -6       | NEUTRAL  | Yahoo Finance |
| XLE        | 2026-11-10 00:00:00 |    62.21      |         -29.5     | NEUTRAL  | Yahoo Finance |
| XLI        | 2026-11-10 00:00:00 |   168.73      |          -3.25    | NEUTRAL  | Yahoo Finance |
| XOM        | 2026-11-10 00:00:00 |   164.47      |         -20.5     | NEUTRAL  | Yahoo Finance |
| YFI-USD    | 2026-11-11 00:00:00 |  1949.3       |         -19       | NEUTRAL  | Kraken API    |
| ZEC-USD    | 2026-11-11 00:00:00 |  1019.46      |         -34.5     | NEUTRAL  | Kraken API    |
| ADA-USD    | 2026-11-11 00:00:00 |     0.175169  |         -44.6667  | SHORT    | Kraken API    |
| ALGO-USD   | 2026-11-11 00:00:00 |     0.0904    |         -34       | SHORT    | Kraken API    |
| AMAT       | 2026-11-10 00:00:00 |   372.53      |         -48.5833  | SHORT    | Yahoo Finance |
| APT-USD    | 2026-11-11 00:00:00 |     0.5715    |         -35.9167  | SHORT    | Kraken API    |
| ARKK       | 2026-11-10 00:00:00 |    77.1       |         -38.8333  | SHORT    | Yahoo Finance |
| ATOM-USD   | 2026-11-11 00:00:00 |     1.4133    |         -41.3333  | SHORT    | Kraken API    |
| BA         | 2026-11-10 00:00:00 |   173.38      |         -40.75    | SHORT    | Yahoo Finance |
| BCH-USD    | 2026-11-11 00:00:00 |   230.6       |         -53.3333  | SHORT    | Kraken API    |
| BITO       | 2026-11-10 00:00:00 |     9.79      |         -44.3333  | SHORT    | Yahoo Finance |
| BTC-USD    | 2026-11-11 00:00:00 | 73771.8       |         -45.5833  | SHORT    | Kraken API    |
| CAT        | 2026-11-10 00:00:00 |   584.57      |         -63.4167  | SHORT    | Yahoo Finance |
| COMP-USD   | 2026-11-11 00:00:00 |    19.86      |         -46.3333  | SHORT    | Kraken API    |
| CRM        | 2026-11-10 00:00:00 |   213.48      |         -43.8333  | SHORT    | Yahoo Finance |
| CRV-USD    | 2026-11-11 00:00:00 |     0.24976   |         -55.6667  | SHORT    | Kraken API    |
| CSCO       | 2026-11-10 00:00:00 |    98.15      |         -50.3333  | SHORT    | Yahoo Finance |
| CVX        | 2026-11-10 00:00:00 |   211.22      |         -33.25    | SHORT    | Yahoo Finance |
| DASH-USD   | 2026-11-11 00:00:00 |    45.233     |         -50.3333  | SHORT    | Kraken API    |
| DOGE-USD   | 2026-11-11 00:00:00 |     0.0681955 |         -51.3333  | SHORT    | Kraken API    |
| EEM        | 2026-11-10 00:00:00 |    60.57      |         -46.5833  | SHORT    | Yahoo Finance |
| ETC-USD    | 2026-11-11 00:00:00 |     6.73      |         -44.3333  | SHORT    | Kraken API    |
| ETH-USD    | 2026-11-11 00:00:00 |  2066.66      |         -45.1667  | SHORT    | Kraken API    |
| EWJ        | 2026-11-10 00:00:00 |    90.39      |         -50.8333  | SHORT    | Yahoo Finance |
| FCX        | 2026-11-10 00:00:00 |    60.31      |         -56.9167  | SHORT    | Yahoo Finance |
| FET-USD    | 2026-11-11 00:00:00 |     0.1476    |         -49.6667  | SHORT    | Kraken API    |
| FIL-USD    | 2026-11-11 00:00:00 |     0.758     |         -41.3333  | SHORT    | Kraken API    |
| GOOGL      | 2026-11-10 00:00:00 |   287.38      |         -61.4167  | SHORT    | Yahoo Finance |
| GRT-USD    | 2026-11-11 00:00:00 |     0.01761   |         -51.6667  | SHORT    | Kraken API    |
| IBIT       | 2026-11-10 00:00:00 |    41.68      |         -44.3333  | SHORT    | Yahoo Finance |
| IEMG       | 2026-11-10 00:00:00 |    73.77      |         -46.5833  | SHORT    | Yahoo Finance |
| INTC       | 2026-11-10 00:00:00 |    58.13      |         -64.0833  | SHORT    | Yahoo Finance |
| LINK-USD   | 2026-11-11 00:00:00 |    10.385     |         -31.5833  | SHORT    | Kraken API    |
| LRCX       | 2026-11-10 00:00:00 |   222.39      |         -48.5833  | SHORT    | Yahoo Finance |
| LTC-USD    | 2026-11-11 00:00:00 |    51         |         -44.3333  | SHORT    | Kraken API    |
| META       | 2026-11-10 00:00:00 |   641.39      |         -37.1667  | SHORT    | Yahoo Finance |
| MU         | 2026-11-10 00:00:00 |   725.11      |         -41.5     | SHORT    | Yahoo Finance |
| NFLX       | 2026-11-10 00:00:00 |    63.26      |         -39.4167  | SHORT    | Yahoo Finance |
| NOW        | 2026-11-10 00:00:00 |    99.61      |         -52.0833  | SHORT    | Yahoo Finance |
| NVDA       | 2026-11-10 00:00:00 |   168.89      |         -67.3333  | SHORT    | Yahoo Finance |
| OP-USD     | 2026-11-11 00:00:00 |     0.0998    |         -34.3333  | SHORT    | Kraken API    |
| ORCL       | 2026-11-10 00:00:00 |   117.98      |         -44.5833  | SHORT    | Yahoo Finance |
| OXY        | 2026-11-10 00:00:00 |    56.9       |         -34.0833  | SHORT    | Yahoo Finance |
| QQQ        | 2026-11-10 00:00:00 |   674.76      |         -36.8333  | SHORT    | Yahoo Finance |
| SHIB-USD   | 2026-11-11 00:00:00 |     4.452e-06 |         -42.3333  | SHORT    | Kraken API    |
| SKY-USD    | 2026-11-11 00:00:00 |     0.05982   |         -43       | SHORT    | Kraken API    |
| SLV        | 2026-11-10 00:00:00 |    46.48      |         -38.75    | SHORT    | Yahoo Finance |
| SMH        | 2026-11-10 00:00:00 |   483.63      |         -49.3333  | SHORT    | Yahoo Finance |
| SNX-USD    | 2026-11-11 00:00:00 |     0.1643    |         -40.6667  | SHORT    | Kraken API    |
| SOL-USD    | 2026-11-11 00:00:00 |    83.2       |         -53.3333  | SHORT    | Kraken API    |
| SOXX       | 2026-11-10 00:00:00 |   146.59      |         -53.0833  | SHORT    | Yahoo Finance |
| SUSHI-USD  | 2026-11-11 00:00:00 |     0.1757    |         -40.6667  | SHORT    | Kraken API    |
| TIA-USD    | 2026-11-11 00:00:00 |     0.4296    |         -53.6667  | SHORT    | Kraken API    |
| TRX-USD    | 2026-11-11 00:00:00 |     0.317425  |         -47       | SHORT    | Kraken API    |
| VWO        | 2026-11-10 00:00:00 |    56.49      |         -35.0833  | SHORT    | Yahoo Finance |
| WIF-USD    | 2026-11-11 00:00:00 |     0.1577    |         -35.3333  | SHORT    | Kraken API    |
| XLK        | 2026-11-10 00:00:00 |   168.91      |         -38.8333  | SHORT    | Yahoo Finance |
| XLM-USD    | 2026-11-11 00:00:00 |     0.14491   |         -53.3333  | SHORT    | Kraken API    |
| XRP-USD    | 2026-11-11 00:00:00 |     1.06011   |         -53.3333  | SHORT    | Kraken API    |

## Edge Summary

- Symbols with trades: **161** of 161
- Beat buy-and-hold: **35.40%** of traded symbols
- Positive return: **30.43%** of traded symbols
- Median strategy return: **-8.23%** (benchmark **17.93%**)
- Median excess vs benchmark: **-25.47%**
- Median Sharpe: **-0.07**
- Median exposure: **44.43%**

> Edge is real only if both _beat buy-and-hold_ and _median excess_ are convincingly positive across many symbols. Treat a single high-return symbol as noise.

## Portfolio Backtest

Actual capital-allocation books (not per-symbol averages). Benchmarks: `equal_weight_buyhold` (whole tracked universe), `spy_buyhold` (100% SPY), and `sixty_forty` (60% SPY / 40% AGG). `high_conf_voltarget` inverse-vol-weights the HIGH-confidence book; `conviction_long_short` is market-neutral. Judge on **Sharpe** and **max_drawdown** out-of-sample, not raw return: a fully-invested long book wins on return in a bull market but carries all the risk.

| strategy              | scope         | ann_return   | ann_vol   |   sharpe | max_drawdown   | total_return   |   avg_gross_exposure |
|:----------------------|:--------------|:-------------|:----------|---------:|:---------------|:---------------|---------------------:|
| equal_weight_buyhold  | full          | 6.51%        | 28.57%    |     0.23 | -39.53%        | 7.66%          |                 1    |
| equal_weight_buyhold  | out_of_sample | 16.15%       | 26.33%    |     0.61 | -18.44%        | 14.46%         |                 1    |
| all_signals_ew        | full          | -12.69%      | 24.25%    |    -0.52 | -54.47%        | -37.84%        |                 1    |
| all_signals_ew        | out_of_sample | -3.22%       | 21.35%    |    -0.15 | -23.52%        | -5.68%         |                 1    |
| high_conf_ew          | full          | -9.55%       | 29.99%    |    -0.32 | -45.79%        | -34.69%        |                 0.89 |
| high_conf_ew          | out_of_sample | -8.51%       | 27.60%    |    -0.31 | -26.01%        | -12.34%        |                 0.89 |
| high_conf_voltarget   | full          | -9.78%       | 26.69%    |    -0.37 | -40.26%        | -33.26%        |                 0.89 |
| high_conf_voltarget   | out_of_sample | -11.19%      | 23.34%    |    -0.48 | -21.00%        | -13.84%        |                 0.89 |
| conviction_long_short | full          | -14.69%      | 21.93%    |    -0.67 | -49.44%        | -40.56%        |                 0.96 |
| conviction_long_short | out_of_sample | -14.73%      | 17.26%    |    -0.85 | -27.59%        | -15.85%        |                 0.96 |
| spy_buyhold           | full          | 2.24%        | 13.98%    |     0.16 | -19.00%        | 3.94%          |                 0.79 |
| spy_buyhold           | out_of_sample | -2.89%       | 10.85%    |    -0.27 | -11.45%        | -3.63%         |                 0.79 |
| sixty_forty           | full          | 0.80%        | 8.77%     |     0.09 | -11.86%        | 1.28%          |                 0.79 |
| sixty_forty           | out_of_sample | -3.91%       | 7.17%     |    -0.54 | -8.19%         | -4.33%         |                 0.79 |

## Walk-Forward Robustness

Each book measured across contiguous time folds (each a different regime). A book has durable edge only if `mean_sharpe` is positive, `min_sharpe` isn't deeply negative, and `pct_positive_folds` is high — a single great fold doesn't count. `fold_sharpes` lists each fold oldest-to-newest.

| strategy              |   n_folds |   mean_sharpe |   median_sharpe |   min_sharpe | pct_positive_folds   | mean_return   | fold_sharpes                 |
|:----------------------|----------:|--------------:|----------------:|-------------:|:---------------------|:--------------|:-----------------------------|
| equal_weight_buyhold  |         5 |          0.44 |            0.56 |        -0.8  | 60.00%               | 2.87%         | 1.34;1.59;-0.49;-0.80;0.56   |
| all_signals_ew        |         5 |         -0.58 |           -0.45 |        -1.79 | 20.00%               | -7.85%        | -1.32;-0.45;-1.79;1.06;-0.39 |
| high_conf_ew          |         5 |         -0.2  |           -0.59 |        -1.63 | 40.00%               | -6.44%        | 0.67;-1.63;-0.59;1.42;-0.89  |
| high_conf_voltarget   |         5 |         -0.3  |           -0.39 |        -1.8  | 40.00%               | -6.83%        | 0.85;-1.80;-0.39;0.89;-1.03  |
| conviction_long_short |         5 |         -0.69 |           -0.6  |        -1.99 | 40.00%               | -9.40%        | -1.99;0.13;-1.05;0.07;-0.60  |
| spy_buyhold           |         5 |          0.11 |            0.06 |        -1.1  | 80.00%               | 0.93%         | 1.26;0.06;0.01;0.29;-1.10    |
| sixty_forty           |         5 |          0.03 |            0.06 |        -1.27 | 80.00%               | 0.32%         | 1.18;0.05;0.11;0.06;-1.27    |

## Strategy Comparison

Each decision rule backtested over the same data. `out_of_sample` is the most recent ~35% of each symbol's history (unseen tail). A rule has real edge only if `median_excess` and `beat_benchmark_pct` stay positive out-of-sample, not just full-sample.

| strategy        | scope         |   symbols | beat_benchmark_pct   | positive_pct   | median_return   | median_benchmark   | median_excess   |   median_sharpe |   total_trades |
|:----------------|:--------------|----------:|:---------------------|:---------------|:----------------|:-------------------|:----------------|----------------:|---------------:|
| trend           | full          |       161 | 35.40%               | 30.43%         | -8.23%          | 17.93%             | -25.47%         |           -0.07 |          11343 |
| trend           | out_of_sample |       161 | 44.72%               | 46.58%         | -0.70%          | 1.67%              | -2.79%          |            0.03 |           3884 |
| mean_reversion  | full          |       159 | 38.99%               | 47.80%         | -0.23%          | 17.93%             | -19.18%         |           -0.02 |           1286 |
| mean_reversion  | out_of_sample |       132 | 47.73%               | 58.33%         | 0.38%           | 0.44%              | -1.39%          |            0.52 |            448 |
| regime_adaptive | full          |       161 | 35.40%               | 31.68%         | -8.12%          | 17.93%             | -24.97%         |           -0.06 |          11611 |
| regime_adaptive | out_of_sample |       161 | 43.48%               | 47.83%         | -0.52%          | 1.67%              | -3.65%          |            0.04 |           3987 |

## Signal Calibration

Realized forward return in the signal's direction, grouped by confidence. HIGH should outrank LOW for the confidence score to be meaningful.

| confidence_level   |   horizon |     n | mean_return   | median_return   | win_rate   |
|:-------------------|----------:|------:|:--------------|:----------------|:-----------|
| HIGH               |         5 |  7817 | 0.21%         | 0.08%           | 51.30%     |
| MEDIUM             |         5 | 29230 | 0.10%         | 0.07%           | 50.78%     |
| LOW                |         5 |  3634 | -0.21%        | -0.24%          | 47.58%     |
| ALL                |         5 | 40681 | 0.09%         | 0.05%           | 50.60%     |
| HIGH               |        10 |  7709 | 0.46%         | 0.08%           | 50.95%     |
| MEDIUM             |        10 | 28908 | 0.19%         | 0.07%           | 50.54%     |
| LOW                |        10 |  3586 | -0.45%        | -0.23%          | 48.33%     |
| ALL                |        10 | 40203 | 0.18%         | 0.05%           | 50.42%     |
| HIGH               |        20 |  7603 | 0.84%         | 0.18%           | 51.33%     |
| MEDIUM             |        20 | 28390 | 0.69%         | 0.45%           | 52.50%     |
| LOW                |        20 |  3493 | -0.39%        | -0.48%          | 47.81%     |
| ALL                |        20 | 39486 | 0.63%         | 0.32%           | 51.86%     |

## Backtest Summary

### Data Quality / Signal Availability

- **ok**: 161 symbols

| symbol     |   trades | return   | benchmark_return   | mdd     |   sharpe | exposure   | skipped_reason   |
|:-----------|---------:|:---------|:-------------------|:--------|---------:|:-----------|:-----------------|
| AAPL       |       68 | -8.82%   | 66.21%             | -23.09% |    -0.08 | 48.42%     | ok               |
| AAVE-USD   |       65 | -43.38%  | -51.24%            | -64.31% |    -0.34 | 38.70%     | ok               |
| ABBV       |       68 | -17.18%  | 70.74%             | -30.52% |    -0.32 | 50.42%     | ok               |
| ADA-USD    |       76 | -15.90%  | -73.83%            | -52.70% |     0.03 | 49.04%     | ok               |
| ADBE       |       74 | 1.98%    | -54.74%            | -31.20% |     0.17 | 53.74%     | ok               |
| AGG        |       63 | -7.05%   | -1.91%             | -10.74% |    -1.09 | 33.94%     | ok               |
| ALGO-USD   |       82 | -29.20%  | -52.50%            | -43.23% |    -0.16 | 42.15%     | ok               |
| AMAT       |       73 | -40.09%  | 55.23%             | -57.56% |    -0.34 | 51.75%     | ok               |
| AMD        |       54 | 22.07%   | 218.46%            | -38.64% |     0.41 | 36.11%     | ok               |
| AMGN       |       63 | -3.80%   | 50.13%             | -34.19% |     0.02 | 52.75%     | ok               |
| AMZN       |       82 | -58.15%  | 45.55%             | -58.58% |    -1.7  | 41.43%     | ok               |
| APT-USD    |       74 | -29.46%  | -87.87%            | -56.73% |    -0.09 | 40.04%     | ok               |
| ARB-USD    |       77 | -8.33%   | -52.63%            | -44.34% |     0.2  | 42.72%     | ok               |
| ARKK       |       85 | -28.97%  | 77.77%             | -35.78% |    -0.42 | 43.59%     | ok               |
| ATOM-USD   |       84 | -58.77%  | -66.90%            | -64.83% |    -0.88 | 47.70%     | ok               |
| AVAX-USD   |       68 | -35.04%  | -59.76%            | -47.41% |    -0.28 | 41.95%     | ok               |
| AVGO       |       66 | -9.96%   | 91.39%             | -42.01% |     0.05 | 40.43%     | ok               |
| BA         |       65 | 13.16%   | -1.66%             | -24.47% |     0.33 | 52.08%     | ok               |
| BAC        |       78 | -6.49%   | 26.73%             | -22.37% |    -0.1  | 48.92%     | ok               |
| BCH-USD    |       84 | -14.21%  | -43.94%            | -54.04% |     0.04 | 48.08%     | ok               |
| BITO       |       85 | -25.89%  | -60.01%            | -43.13% |    -0.2  | 41.26%     | ok               |
| BLK        |       79 | -4.79%   | 56.12%             | -26.90% |    -0.05 | 47.25%     | ok               |
| BND        |       66 | -7.21%   | -1.89%             | -10.80% |    -1.1  | 34.94%     | ok               |
| BONK-USD   |       77 | 37.32%   | -82.04%            | -56.14% |     0.55 | 45.21%     | ok               |
| BTC-USD    |       81 | -9.89%   | -30.24%            | -25.52% |    -0.05 | 51.92%     | ok               |
| C          |       81 | -35.20%  | 101.70%            | -39.84% |    -0.76 | 47.42%     | ok               |
| CAT        |       70 | 30.07%   | 77.61%             | -21.87% |     0.54 | 50.92%     | ok               |
| CL         |       60 | 6.40%    | 1.18%              | -14.32% |     0.26 | 40.10%     | ok               |
| CMCSA      |       82 | -35.42%  | -30.23%            | -45.88% |    -0.84 | 43.43%     | ok               |
| COMP-USD   |       99 | -47.01%  | -56.54%            | -61.00% |    -0.36 | 49.04%     | ok               |
| COP        |       64 | -14.28%  | 21.79%             | -38.80% |    -0.17 | 43.59%     | ok               |
| COST       |       60 | -0.22%   | 23.62%             | -31.32% |     0.06 | 40.93%     | ok               |
| CRM        |       67 | -27.57%  | -11.71%            | -39.41% |    -0.36 | 46.09%     | ok               |
| CRV-USD    |       64 | 28.97%   | -61.27%            | -39.89% |     0.49 | 36.97%     | ok               |
| CSCO       |       65 | 6.08%    | 110.08%            | -25.62% |     0.22 | 51.08%     | ok               |
| CVX        |       67 | -11.48%  | 34.84%             | -26.75% |    -0.22 | 43.26%     | ok               |
| DASH-USD   |       57 | -15.19%  | 110.62%            | -64.43% |     0.28 | 30.27%     | ok               |
| DBC        |       68 | -11.81%  | 31.51%             | -24.10% |    -0.34 | 36.11%     | ok               |
| DE         |       72 | -4.78%   | 80.23%             | -22.44% |    -0    | 44.09%     | ok               |
| DIA        |       72 | -9.73%   | 33.07%             | -16.20% |    -0.49 | 44.43%     | ok               |
| DIS        |       62 | 3.78%    | 17.06%             | -27.81% |     0.18 | 46.42%     | ok               |
| DOGE-USD   |       68 | -16.17%  | -62.98%            | -60.39% |     0.03 | 47.70%     | ok               |
| DOT-USD    |       80 | -48.62%  | -79.04%            | -63.40% |    -0.39 | 45.02%     | ok               |
| DXY-INDEX  |       40 | -3.04%   | -6.99%             | -5.53%  |    -0.5  | 30.52%     | ok               |
| EEM        |       66 | -8.34%   | 41.45%             | -24.14% |    -0.19 | 41.43%     | ok               |
| EFA        |       64 | -9.07%   | 32.94%             | -12.63% |    -0.35 | 38.94%     | ok               |
| EOG        |       76 | -29.30%  | 24.20%             | -47.65% |    -0.62 | 43.93%     | ok               |
| ETC-USD    |       56 | -7.71%   | -60.37%            | -46.79% |     0.06 | 35.25%     | ok               |
| ETH-USD    |       61 | 114.78%  | -17.70%            | -30.11% |     1.14 | 46.93%     | ok               |
| EWJ        |       66 | -24.12%  | 35.97%             | -29.40% |    -0.82 | 37.77%     | ok               |
| FCX        |       69 | -26.53%  | 22.18%             | -46.84% |    -0.25 | 45.42%     | ok               |
| FET-USD    |       79 | -32.83%  | -80.14%            | -66.52% |    -0.07 | 44.83%     | ok               |
| FIL-USD    |       71 | -38.14%  | -69.50%            | -60.64% |    -0.29 | 39.08%     | ok               |
| FXI        |       48 | -4.56%   | 28.01%             | -23.91% |    -0.03 | 30.45%     | ok               |
| GDX        |       68 | -6.33%   | 150.33%            | -34.27% |     0.04 | 45.09%     | ok               |
| GDXJ       |       70 | -30.08%  | 145.33%            | -35.99% |    -0.32 | 44.43%     | ok               |
| GE         |       78 | -13.14%  | 104.79%            | -27.82% |    -0.14 | 48.42%     | ok               |
| GLD        |       52 | 11.67%   | 69.31%             | -14.15% |     0.35 | 46.09%     | ok               |
| GOOGL      |       57 | 74.51%   | 63.01%             | -16.84% |     1.14 | 48.59%     | ok               |
| GRT-USD    |       75 | 61.62%   | -80.76%            | -43.87% |     0.71 | 47.89%     | ok               |
| GS         |       68 | -2.77%   | 98.71%             | -21.94% |     0.04 | 47.42%     | ok               |
| HBAR-USD   |       40 | -29.16%  | -36.25%            | -56.47% |    -0.42 | 42.96%     | ok               |
| HD         |       71 | 6.13%    | -0.69%             | -17.15% |     0.23 | 44.76%     | ok               |
| HON        |       89 | -29.30%  | 7.82%              | -34.06% |    -0.76 | 53.74%     | ok               |
| HYG        |       89 | -7.38%   | -0.16%             | -10.59% |    -0.83 | 39.10%     | ok               |
| IBIT       |       46 | 32.53%   | 9.66%              | -18.95% |     0.61 | 35.35%     | ok               |
| IBM        |       69 | -19.93%  | 40.60%             | -48.94% |    -0.19 | 50.75%     | ok               |
| ICP-USD    |       72 | 2.49%    | -53.52%            | -40.43% |     0.29 | 39.66%     | ok               |
| IEF        |       76 | -9.64%   | -3.52%             | -12.21% |    -1.26 | 34.78%     | ok               |
| IEMG       |       62 | -5.19%   | 37.22%             | -24.73% |    -0.1  | 41.26%     | ok               |
| INJ-USD    |       57 | -18.95%  | -37.81%            | -64.24% |     0.06 | 39.08%     | ok               |
| INTC       |       72 | 59.06%   | 89.84%             | -60.60% |     0.63 | 49.25%     | ok               |
| INTU       |       71 | 5.32%    | -44.74%            | -36.67% |     0.22 | 48.25%     | ok               |
| ITA        |       72 | -1.32%   | 61.88%             | -23.75% |     0.04 | 47.42%     | ok               |
| IWM        |       58 | 10.62%   | 40.36%             | -8.62%  |     0.43 | 34.78%     | ok               |
| JNJ        |       60 | 13.39%   | 90.00%             | -17.51% |     0.5  | 46.76%     | ok               |
| JPM        |       75 | -25.99%  | 72.18%             | -32.74% |    -0.75 | 44.43%     | ok               |
| KO         |       52 | 29.78%   | 55.85%             | -8.64%  |     0.98 | 39.10%     | ok               |
| LDO-USD    |       66 | 61.79%   | -59.61%            | -53.44% |     0.69 | 48.28%     | ok               |
| LIN        |       72 | -4.51%   | 17.88%             | -20.61% |    -0.09 | 41.26%     | ok               |
| LINK-USD   |       68 | 31.72%   | -24.35%            | -35.01% |     0.52 | 43.10%     | ok               |
| LLY        |       80 | -29.16%  | 61.66%             | -52.47% |    -0.41 | 49.58%     | ok               |
| LRCX       |       82 | -20.02%  | 109.54%            | -58.92% |    -0.03 | 45.59%     | ok               |
| LTC-USD    |       69 | 9.23%    | -41.56%            | -30.78% |     0.31 | 50.77%     | ok               |
| MCD        |       75 | 11.39%   | 11.18%             | -22.20% |     0.43 | 40.43%     | ok               |
| META       |       72 | -33.27%  | 27.84%             | -44.90% |    -0.5  | 50.58%     | ok               |
| MPC        |       70 | 11.57%   | 124.32%            | -33.74% |     0.31 | 53.41%     | ok               |
| MRK        |       67 | -22.90%  | 14.17%             | -35.95% |    -0.43 | 42.93%     | ok               |
| MS         |       77 | -7.56%   | 92.49%             | -27.79% |    -0.1  | 48.09%     | ok               |
| MSFT       |       81 | -27.33%  | 19.62%             | -38.06% |    -0.6  | 50.92%     | ok               |
| MU         |       53 | 90.98%   | 402.89%            | -66.33% |     0.8  | 49.92%     | ok               |
| NEAR-USD   |       63 | 169.55%  | 51.04%             | -47.35% |     1.11 | 42.91%     | ok               |
| NEM        |       70 | -25.86%  | 180.21%            | -39.56% |    -0.25 | 49.75%     | ok               |
| NFLX       |       84 | -7.53%   | -6.84%             | -27.17% |    -0.05 | 50.92%     | ok               |
| NKE        |       87 | -33.44%  | -59.54%            | -55.35% |    -0.41 | 47.92%     | ok               |
| NOW        |       81 | -9.93%   | -32.17%            | -42.66% |     0.1  | 52.08%     | ok               |
| NVDA       |       82 | -38.63%  | 35.57%             | -51.51% |    -0.49 | 55.79%     | ok               |
| OP-USD     |       72 | -35.08%  | -83.60%            | -58.87% |    -0.21 | 35.06%     | ok               |
| ORCL       |       60 | 75.24%   | -17.44%            | -30.61% |     0.75 | 50.58%     | ok               |
| OXY        |       69 | -0.19%   | -8.87%             | -28.48% |     0.12 | 43.26%     | ok               |
| PEP        |       72 | 3.72%    | -13.84%            | -21.35% |     0.18 | 45.26%     | ok               |
| PEPE-USD   |       74 | -33.64%  | -54.34%            | -57.70% |    -0.09 | 46.74%     | ok               |
| PFE        |       77 | -32.42%  | 5.84%              | -41.77% |    -0.98 | 37.44%     | ok               |
| PG         |       62 | -17.91%  | 0.59%              | -24.55% |    -0.61 | 36.44%     | ok               |
| PM         |       81 | -8.23%   | 91.95%             | -38.30% |    -0.1  | 48.25%     | ok               |
| POL-USD    |       83 | 5.09%    | -57.78%            | -44.63% |     0.27 | 50.00%     | ok               |
| QCOM       |       79 | -40.18%  | -19.46%            | -53.61% |    -0.45 | 40.43%     | ok               |
| QQQ        |       70 | -4.53%   | 40.15%             | -14.40% |    -0.04 | 43.59%     | ok               |
| RENDER-USD |       92 | -43.06%  | -58.81%            | -54.46% |    -0.25 | 48.47%     | ok               |
| RTX        |       71 | 20.73%   | 90.61%             | -16.99% |     0.51 | 52.08%     | ok               |
| SBUX       |       66 | -6.25%   | 37.92%             | -29.22% |    -0.03 | 40.27%     | ok               |
| SCHW       |       84 | -16.47%  | 27.96%             | -31.92% |    -0.34 | 48.09%     | ok               |
| SHIB-USD   |       81 | -34.84%  | -64.41%            | -52.52% |    -0.34 | 52.49%     | ok               |
| SHY        |       54 | -2.37%   | -0.36%             | -3.30%  |    -0.77 | 38.60%     | ok               |
| SKY-USD    |       87 | -56.20%  | -18.50%            | -63.60% |    -0.84 | 44.83%     | ok               |
| SLB        |       76 | -43.91%  | 9.77%              | -55.78% |    -0.9  | 47.92%     | ok               |
| SLV        |       66 | 30.03%   | 66.00%             | -37.05% |     0.51 | 41.43%     | ok               |
| SMH        |       50 | 46.60%   | 79.84%             | -34.29% |     0.74 | 42.10%     | ok               |
| SNX-USD    |       62 | 5.24%    | -75.11%            | -50.74% |     0.28 | 36.97%     | ok               |
| SOL-USD    |       73 | 5.09%    | -45.45%            | -41.09% |     0.28 | 58.05%     | ok               |
| SOXX       |       56 | 54.41%   | 74.35%             | -39.81% |     0.78 | 40.93%     | ok               |
| SPY        |       63 | -5.24%   | 37.10%             | -15.53% |    -0.12 | 47.75%     | ok               |
| SUSHI-USD  |       91 | -60.20%  | -72.76%            | -76.86% |    -0.69 | 43.30%     | ok               |
| T          |       68 | 52.26%   | 21.15%             | -17.01% |     0.94 | 57.57%     | ok               |
| TGT        |       58 | -8.89%   | 12.83%             | -32.83% |    -0.11 | 37.27%     | ok               |
| TIA-USD    |       91 | -45.91%  | -78.60%            | -75.93% |    -0.21 | 43.49%     | ok               |
| TLT        |       66 | -20.93%  | -13.92%            | -22.01% |    -1.58 | 34.28%     | ok               |
| TMO        |       67 | 36.18%   | 28.89%             | -18.85% |     0.7  | 55.91%     | ok               |
| TMUS       |       74 | -6.64%   | -4.17%             | -33.05% |    -0.04 | 46.92%     | ok               |
| TRX-USD    |       62 | 2.55%    | 12.60%             | -22.90% |     0.16 | 48.08%     | ok               |
| TSLA       |       74 | -30.19%  | 109.16%            | -58.36% |    -0.15 | 42.76%     | ok               |
| TXN        |       83 | -30.16%  | 55.90%             | -46.56% |    -0.35 | 48.75%     | ok               |
| UNH        |       73 | 37.46%   | -16.39%            | -26.31% |     0.6  | 48.75%     | ok               |
| UNI-USD    |       82 | -24.50%  | 5.53%              | -59.93% |     0.04 | 49.23%     | ok               |
| UPS        |       71 | -33.75%  | -18.86%            | -40.15% |    -0.63 | 42.93%     | ok               |
| USO        |       65 | -13.28%  | 78.13%             | -43.70% |    -0.06 | 34.11%     | ok               |
| VEA        |       64 | -7.02%   | 39.05%             | -18.84% |    -0.25 | 41.26%     | ok               |
| VIXY       |       96 | -84.10%  | -60.14%            | -91.23% |    -1.16 | 31.61%     | ok               |
| VNQ        |       71 | -9.84%   | 15.90%             | -24.92% |    -0.35 | 40.27%     | ok               |
| VTI        |       67 | -11.90%  | 37.52%             | -17.64% |    -0.38 | 47.75%     | ok               |
| VWO        |       78 | -14.84%  | 27.60%             | -25.20% |    -0.51 | 41.43%     | ok               |
| VZ         |       86 | -27.73%  | 15.08%             | -31.67% |    -0.84 | 43.26%     | ok               |
| WFC        |       84 | -21.97%  | 45.45%             | -29.78% |    -0.4  | 46.42%     | ok               |
| WIF-USD    |       64 | -3.27%   | -82.28%            | -48.32% |     0.24 | 42.34%     | ok               |
| WMT        |       71 | 5.72%    | 84.61%             | -25.96% |     0.23 | 48.42%     | ok               |
| XBI        |       60 | 0.63%    | 72.50%             | -17.66% |     0.1  | 37.77%     | ok               |
| XLB        |       64 | -8.92%   | 17.93%             | -24.18% |    -0.27 | 34.11%     | ok               |
| XLC        |       61 | 5.66%    | 27.69%             | -12.33% |     0.25 | 49.58%     | ok               |
| XLE        |       68 | -7.47%   | 37.83%             | -34.77% |    -0.11 | 47.25%     | ok               |
| XLF        |       78 | -2.02%   | 40.49%             | -23.61% |    -0.01 | 48.75%     | ok               |
| XLI        |       82 | -9.35%   | 36.92%             | -18.27% |    -0.32 | 42.76%     | ok               |
| XLK        |       42 | 33.34%   | 47.64%             | -17.32% |     0.73 | 44.26%     | ok               |
| XLM-USD    |       73 | 7.07%    | -45.88%            | -54.58% |     0.29 | 49.23%     | ok               |
| XLP        |       63 | 14.47%   | 17.29%             | -8.96%  |     0.71 | 40.27%     | ok               |
| XLU        |       69 | -0.17%   | 25.30%             | -20.40% |     0.04 | 40.27%     | ok               |
| XLV        |       74 | -17.62%  | 29.02%             | -22.82% |    -0.77 | 36.94%     | ok               |
| XLY        |       77 | -1.78%   | 33.70%             | -18.44% |     0.02 | 47.75%     | ok               |
| XOM        |       55 | 2.46%    | 47.19%             | -20.29% |     0.14 | 36.27%     | ok               |
| XRP-USD    |       74 | -5.56%   | -53.25%            | -33.91% |     0.11 | 35.63%     | ok               |
| YFI-USD    |       74 | -51.63%  | -62.63%            | -58.28% |    -0.8  | 39.66%     | ok               |
| ZEC-USD    |       54 | 126.43%  | 1991.63%           | -56.50% |     0.87 | 36.97%     | ok               |

## AAPL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -3.12%   | 66.21%             | -22.53% |     0.05 |       77 | 53.24%     | ok               |
|          15 | -7.40%   | 66.21%             | -24.50% |    -0.03 |       86 | 60.73%     | ok               |
|          30 | -8.82%   | 66.21%             | -23.09% |    -0.08 |       68 | 48.42%     | ok               |
|          35 | -10.13%  | 66.21%             | -24.45% |    -0.12 |       68 | 47.09%     | ok               |
|          25 | -12.51%  | 66.21%             | -24.77% |    -0.16 |       78 | 50.58%     | ok               |

## AAVE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 4.68%    | -51.24%            | -43.61% |     0.27 |       43 | 33.52%     | ok               |
|          35 | -9.10%   | -51.24%            | -48.79% |     0.12 |       53 | 36.78%     | ok               |
|          45 | -10.37%  | -51.24%            | -49.19% |     0.07 |       48 | 28.54%     | ok               |
|          50 | -11.28%  | -51.24%            | -45.07% |     0.04 |       44 | 21.26%     | ok               |
|          15 | -46.14%  | -51.24%            | -60.36% |    -0.27 |       78 | 53.07%     | ok               |

## ABBV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -9.20%   | 70.74%             | -28.42% |    -0.15 |       54 | 38.44%     | ok               |
|          20 | -13.94%  | 70.74%             | -28.73% |    -0.23 |       64 | 53.74%     | ok               |
|          25 | -14.03%  | 70.74%             | -30.04% |    -0.23 |       67 | 52.25%     | ok               |
|          30 | -17.18%  | 70.74%             | -30.52% |    -0.32 |       68 | 50.42%     | ok               |
|          40 | -17.24%  | 70.74%             | -27.36% |    -0.36 |       70 | 43.43%     | ok               |

## ADA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 13.22%   | -73.83%            | -32.15% |     0.35 |       46 | 25.48%     | ok               |
|          15 | 2.62%    | -73.83%            | -47.27% |     0.3  |       69 | 63.79%     | ok               |
|          45 | 6.55%    | -73.83%            | -37.32% |     0.27 |       54 | 32.18%     | ok               |
|          40 | 5.52%    | -73.83%            | -40.39% |     0.27 |       58 | 38.89%     | ok               |
|          35 | 4.34%    | -73.83%            | -44.07% |     0.26 |       64 | 43.49%     | ok               |

## ADBE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 14.18%   | -54.74%            | -29.07% |     0.34 |       61 | 58.07%     | ok               |
|          30 | 1.98%    | -54.74%            | -31.20% |     0.17 |       74 | 53.74%     | ok               |
|          20 | 0.98%    | -54.74%            | -31.52% |     0.16 |       69 | 61.73%     | ok               |
|          35 | -1.92%   | -54.74%            | -32.89% |     0.1  |       79 | 45.09%     | ok               |
|          15 | -5.88%   | -54.74%            | -34.98% |     0.06 |       69 | 64.39%     | ok               |

## AGG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -5.94%   | -1.91%             | -9.39%  |    -1.09 |       58 | 23.79%     | ok               |
|          30 | -7.05%   | -1.91%             | -10.74% |    -1.09 |       63 | 33.94%     | ok               |
|          35 | -7.72%   | -1.91%             | -11.53% |    -1.23 |       64 | 30.78%     | ok               |
|          20 | -8.90%   | -1.91%             | -11.89% |    -1.27 |       68 | 39.60%     | ok               |
|          25 | -8.66%   | -1.91%             | -12.28% |    -1.29 |       69 | 37.44%     | ok               |

## ALGO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -29.20%  | -52.50%            | -43.23% |    -0.16 |       82 | 42.15%     | ok               |
|          25 | -32.94%  | -52.50%            | -51.61% |    -0.19 |       84 | 46.55%     | ok               |
|          15 | -39.78%  | -52.50%            | -54.11% |    -0.27 |       79 | 52.49%     | ok               |
|          35 | -36.94%  | -52.50%            | -52.80% |    -0.35 |       70 | 37.16%     | ok               |
|          20 | -46.06%  | -52.50%            | -56.75% |    -0.4  |       83 | 49.23%     | ok               |

## AMAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -26.70%  | 55.23%             | -40.12% |    -0.18 |       52 | 35.94%     | ok               |
|          15 | -34.03%  | 55.23%             | -53.90% |    -0.21 |       74 | 60.57%     | ok               |
|          35 | -35.64%  | 55.23%             | -52.00% |    -0.29 |       73 | 49.08%     | ok               |
|          30 | -40.09%  | 55.23%             | -57.56% |    -0.34 |       73 | 51.75%     | ok               |
|          40 | -41.77%  | 55.23%             | -55.32% |    -0.41 |       73 | 44.09%     | ok               |

## AMD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 38.38%   | 218.46%            | -37.12% |     0.55 |       52 | 31.28%     | ok               |
|          40 | 22.07%   | 218.46%            | -38.64% |     0.41 |       54 | 36.11%     | ok               |
|          35 | 16.82%   | 218.46%            | -40.46% |     0.37 |       62 | 37.77%     | ok               |
|          45 | 10.46%   | 218.46%            | -45.45% |     0.31 |       58 | 34.11%     | ok               |
|          30 | -0.75%   | 218.46%            | -47.41% |     0.21 |       65 | 40.43%     | ok               |

## AMGN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 1.28%    | 50.13%             | -26.65% |     0.13 |       62 | 58.07%     | ok               |
|          35 | -1.37%   | 50.13%             | -31.29% |     0.07 |       65 | 49.42%     | ok               |
|          30 | -3.80%   | 50.13%             | -34.19% |     0.02 |       63 | 52.75%     | ok               |
|          15 | -6.22%   | 50.13%             | -27.98% |    -0.02 |       61 | 62.06%     | ok               |
|          25 | -5.77%   | 50.13%             | -33.47% |    -0.02 |       59 | 54.91%     | ok               |

## AMZN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -32.85%  | 45.55%             | -33.72% |    -1.02 |       60 | 30.28%     | ok               |
|          50 | -34.90%  | 45.55%             | -35.58% |    -1.27 |       52 | 22.96%     | ok               |
|          45 | -40.35%  | 45.55%             | -40.97% |    -1.45 |       60 | 26.62%     | ok               |
|          35 | -55.29%  | 45.55%             | -55.76% |    -1.66 |       81 | 35.61%     | ok               |
|          30 | -58.15%  | 45.55%             | -58.58% |    -1.7  |       82 | 41.43%     | ok               |

## APT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 47.37%   | -87.87%            | -25.96% |     0.8  |       40 | 15.71%     | ok               |
|          45 | 14.91%   | -87.87%            | -52.49% |     0.37 |       62 | 23.37%     | ok               |
|          20 | -5.46%   | -87.87%            | -56.22% |     0.23 |       82 | 50.38%     | ok               |
|          35 | -14.94%  | -87.87%            | -49.10% |     0.06 |       72 | 35.63%     | ok               |
|          15 | -28.30%  | -87.87%            | -58.22% |     0.02 |       79 | 56.51%     | ok               |

## ARB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 68.31%   | -52.63%            | -33.86% |     0.73 |       56 | 26.05%     | ok               |
|          50 | 38.21%   | -52.63%            | -33.86% |     0.55 |       46 | 18.39%     | ok               |
|          40 | 36.71%   | -52.63%            | -38.69% |     0.54 |       55 | 33.52%     | ok               |
|          35 | 31.43%   | -52.63%            | -39.59% |     0.5  |       71 | 37.74%     | ok               |
|          15 | 25.21%   | -52.63%            | -55.99% |     0.48 |       94 | 58.62%     | ok               |

## ARKK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -13.70%  | 77.77%             | -37.76% |    -0.06 |       87 | 54.58%     | ok               |
|          20 | -22.33%  | 77.77%             | -35.06% |    -0.23 |       87 | 49.92%     | ok               |
|          30 | -28.97%  | 77.77%             | -35.78% |    -0.42 |       85 | 43.59%     | ok               |
|          35 | -33.75%  | 77.77%             | -39.24% |    -0.57 |       86 | 40.77%     | ok               |
|          25 | -39.20%  | 77.77%             | -45.03% |    -0.64 |       95 | 46.09%     | ok               |

## ATOM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -44.72%  | -66.90%            | -56.26% |    -0.42 |       82 | 65.52%     | ok               |
|          25 | -47.57%  | -66.90%            | -58.01% |    -0.54 |       86 | 53.64%     | ok               |
|          20 | -51.91%  | -66.90%            | -62.05% |    -0.61 |       90 | 57.85%     | ok               |
|          45 | -48.30%  | -66.90%            | -55.84% |    -0.71 |       74 | 32.76%     | ok               |
|          40 | -53.87%  | -66.90%            | -62.66% |    -0.82 |       72 | 38.12%     | ok               |

## AVAX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 62.56%   | -59.76%            | -22.06% |     0.92 |       34 | 19.73%     | ok               |
|          40 | 28.44%   | -59.76%            | -26.27% |     0.52 |       40 | 30.08%     | ok               |
|          45 | 18.84%   | -59.76%            | -24.48% |     0.42 |       36 | 25.67%     | ok               |
|          35 | 6.97%    | -59.76%            | -33.05% |     0.28 |       52 | 36.40%     | ok               |
|          15 | 2.18%    | -59.76%            | -43.71% |     0.26 |       73 | 54.02%     | ok               |

## AVGO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -7.37%   | 91.39%             | -40.31% |     0.09 |       70 | 43.09%     | ok               |
|          30 | -9.96%   | 91.39%             | -42.01% |     0.05 |       66 | 40.43%     | ok               |
|          20 | -13.50%  | 91.39%             | -40.93% |     0.02 |       79 | 46.42%     | ok               |
|          15 | -21.03%  | 91.39%             | -41.62% |    -0.06 |       79 | 51.25%     | ok               |
|          50 | -16.77%  | 91.39%             | -41.39% |    -0.08 |       60 | 28.29%     | ok               |

## BA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 32.48%   | -1.66%             | -13.34% |     0.75 |       46 | 36.11%     | ok               |
|          35 | 27.01%   | -1.66%             | -18.09% |     0.54 |       68 | 48.75%     | ok               |
|          40 | 23.76%   | -1.66%             | -23.87% |     0.51 |       46 | 43.59%     | ok               |
|          25 | 22.65%   | -1.66%             | -26.02% |     0.46 |       66 | 55.41%     | ok               |
|          30 | 13.16%   | -1.66%             | -24.47% |     0.33 |       65 | 52.08%     | ok               |

## BAC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 1.58%    | 26.73%             | -16.89% |     0.12 |       82 | 54.24%     | ok               |
|          35 | 0.65%    | 26.73%             | -22.58% |     0.09 |       70 | 44.09%     | ok               |
|          45 | -0.38%   | 26.73%             | -15.21% |     0.05 |       56 | 34.28%     | ok               |
|          15 | -4.20%   | 26.73%             | -21.05% |    -0.01 |       88 | 60.23%     | ok               |
|          25 | -3.71%   | 26.73%             | -22.01% |    -0.02 |       80 | 52.08%     | ok               |

## BCH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 17.05%   | -43.94%            | -45.51% |     0.39 |       82 | 56.70%     | ok               |
|          20 | 2.68%    | -43.94%            | -45.52% |     0.25 |       76 | 53.64%     | ok               |
|          35 | -9.06%   | -43.94%            | -57.75% |     0.1  |       74 | 44.25%     | ok               |
|          25 | -11.84%  | -43.94%            | -48.42% |     0.08 |       80 | 50.00%     | ok               |
|          30 | -14.21%  | -43.94%            | -54.04% |     0.04 |       84 | 48.08%     | ok               |

## BITO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -11.29%  | -60.01%            | -31.98% |    -0.04 |       54 | 24.29%     | ok               |
|          45 | -15.11%  | -60.01%            | -32.05% |    -0.09 |       58 | 27.62%     | ok               |
|          15 | -27.87%  | -60.01%            | -53.24% |    -0.17 |       83 | 49.75%     | ok               |
|          30 | -25.89%  | -60.01%            | -43.13% |    -0.2  |       85 | 41.26%     | ok               |
|          40 | -23.78%  | -60.01%            | -40.13% |    -0.21 |       68 | 32.45%     | ok               |

## BLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 4.97%    | 56.12%             | -20.79% |     0.21 |       86 | 43.76%     | ok               |
|          20 | 1.30%    | 56.12%             | -21.48% |     0.12 |       82 | 51.91%     | ok               |
|          40 | 0.40%    | 56.12%             | -22.83% |     0.09 |       78 | 39.27%     | ok               |
|          25 | -0.15%   | 56.12%             | -24.62% |     0.08 |       75 | 49.75%     | ok               |
|          30 | -4.79%   | 56.12%             | -26.90% |    -0.05 |       79 | 47.25%     | ok               |

## BND Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -7.62%   | -1.89%             | -10.72% |    -1.08 |       63 | 40.77%     | ok               |
|          25 | -7.42%   | -1.89%             | -11.16% |    -1.09 |       68 | 38.60%     | ok               |
|          30 | -7.21%   | -1.89%             | -10.80% |    -1.1  |       66 | 34.94%     | ok               |
|          40 | -7.39%   | -1.89%             | -11.34% |    -1.26 |       58 | 28.79%     | ok               |
|          15 | -8.99%   | -1.89%             | -12.04% |    -1.27 |       75 | 43.09%     | ok               |

## BONK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 97.75%   | -82.04%            | -29.38% |     1.01 |       36 | 16.28%     | ok               |
|          40 | 117.13%  | -82.04%            | -46.44% |     0.99 |       65 | 34.10%     | ok               |
|          45 | 96.77%   | -82.04%            | -35.81% |     0.94 |       60 | 22.80%     | ok               |
|          15 | 77.30%   | -82.04%            | -56.25% |     0.74 |       65 | 61.49%     | ok               |
|          35 | 66.39%   | -82.04%            | -52.83% |     0.72 |       65 | 40.23%     | ok               |

## BTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 34.06%   | -30.24%            | -12.58% |     0.76 |       38 | 29.69%     | ok               |
|          40 | 30.42%   | -30.24%            | -19.29% |     0.67 |       48 | 34.67%     | ok               |
|          35 | 31.80%   | -30.24%            | -22.51% |     0.67 |       62 | 41.00%     | ok               |
|          50 | 17.82%   | -30.24%            | -20.16% |     0.49 |       34 | 25.10%     | ok               |
|          30 | 2.17%    | -30.24%            | -23.71% |     0.17 |       74 | 46.74%     | ok               |

## C Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -12.24%  | 101.70%            | -22.72% |    -0.29 |       68 | 30.95%     | ok               |
|          45 | -22.47%  | 101.70%            | -30.69% |    -0.57 |       78 | 36.27%     | ok               |
|          40 | -27.35%  | 101.70%            | -35.05% |    -0.67 |       74 | 38.77%     | ok               |
|          25 | -34.24%  | 101.70%            | -37.53% |    -0.72 |       71 | 50.08%     | ok               |
|          20 | -36.29%  | 101.70%            | -39.30% |    -0.76 |       77 | 52.75%     | ok               |

## CAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 45.44%   | 77.61%             | -21.80% |     0.69 |       71 | 61.56%     | ok               |
|          25 | 39.32%   | 77.61%             | -21.79% |     0.64 |       66 | 53.24%     | ok               |
|          45 | 30.86%   | 77.61%             | -23.56% |     0.57 |       54 | 39.43%     | ok               |
|          30 | 30.07%   | 77.61%             | -21.87% |     0.54 |       70 | 50.92%     | ok               |
|          20 | 26.97%   | 77.61%             | -24.56% |     0.5  |       70 | 55.57%     | ok               |

## CL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 12.23%   | 1.18%              | -10.72% |     0.47 |       42 | 25.12%     | ok               |
|          45 | 8.14%    | 1.18%              | -10.96% |     0.33 |       46 | 27.95%     | ok               |
|          30 | 6.40%    | 1.18%              | -14.32% |     0.26 |       60 | 40.10%     | ok               |
|          40 | 2.96%    | 1.18%              | -15.09% |     0.16 |       52 | 31.28%     | ok               |
|          35 | 2.16%    | 1.18%              | -15.39% |     0.13 |       60 | 36.27%     | ok               |

## CMCSA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -17.90%  | -30.23%            | -28.74% |    -0.59 |       48 | 16.47%     | ok               |
|          45 | -23.19%  | -30.23%            | -35.43% |    -0.73 |       62 | 21.13%     | ok               |
|          15 | -35.96%  | -30.23%            | -43.53% |    -0.74 |       90 | 58.07%     | ok               |
|          40 | -31.05%  | -30.23%            | -42.78% |    -0.83 |       89 | 28.62%     | ok               |
|          30 | -35.42%  | -30.23%            | -45.88% |    -0.84 |       82 | 43.43%     | ok               |

## COMP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -29.57%  | -56.54%            | -43.08% |    -0.24 |       50 | 23.37%     | ok               |
|          30 | -47.01%  | -56.54%            | -61.00% |    -0.36 |       99 | 49.04%     | ok               |
|          25 | -56.75%  | -56.54%            | -68.16% |    -0.53 |      102 | 57.09%     | ok               |
|          20 | -58.31%  | -56.54%            | -69.31% |    -0.54 |      108 | 63.22%     | ok               |
|          15 | -60.94%  | -56.54%            | -72.41% |    -0.55 |      105 | 68.01%     | ok               |

## COP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -14.28%  | 21.79%             | -38.80% |    -0.17 |       64 | 43.59%     | ok               |
|          50 | -12.17%  | 21.79%             | -35.99% |    -0.17 |       50 | 31.28%     | ok               |
|          35 | -14.14%  | 21.79%             | -41.20% |    -0.17 |       65 | 40.77%     | ok               |
|          45 | -17.00%  | 21.79%             | -41.02% |    -0.27 |       60 | 34.78%     | ok               |
|          25 | -25.22%  | 21.79%             | -44.40% |    -0.39 |       75 | 46.76%     | ok               |

## COST Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 15.48%   | 23.62%             | -24.32% |     0.49 |       62 | 47.25%     | ok               |
|          25 | 11.70%   | 23.62%             | -24.93% |     0.4  |       59 | 44.26%     | ok               |
|          35 | 4.19%    | 23.62%             | -30.16% |     0.2  |       58 | 38.44%     | ok               |
|          15 | -0.17%   | 23.62%             | -27.30% |     0.07 |       67 | 50.92%     | ok               |
|          30 | -0.22%   | 23.62%             | -31.32% |     0.06 |       60 | 40.93%     | ok               |

## CRM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -16.04%  | -11.71%            | -26.69% |    -0.15 |       64 | 41.26%     | ok               |
|          40 | -19.19%  | -11.71%            | -32.67% |    -0.23 |       70 | 37.10%     | ok               |
|          15 | -25.94%  | -11.71%            | -47.54% |    -0.26 |       92 | 58.24%     | ok               |
|          30 | -27.57%  | -11.71%            | -39.41% |    -0.36 |       67 | 46.09%     | ok               |
|          20 | -31.21%  | -11.71%            | -45.74% |    -0.38 |       74 | 51.75%     | ok               |

## CRV-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 71.36%   | -61.27%            | -37.78% |     0.78 |       62 | 32.76%     | ok               |
|          40 | 66.71%   | -61.27%            | -38.86% |     0.76 |       52 | 28.74%     | ok               |
|          45 | 41.78%   | -61.27%            | -42.29% |     0.6  |       56 | 22.41%     | ok               |
|          50 | 29.67%   | -61.27%            | -30.73% |     0.5  |       50 | 18.20%     | ok               |
|          30 | 28.97%   | -61.27%            | -39.89% |     0.49 |       64 | 36.97%     | ok               |

## CSCO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 31.26%   | 110.08%            | -19.54% |     0.65 |       54 | 41.60%     | ok               |
|          50 | 30.48%   | 110.08%            | -19.34% |     0.64 |       52 | 39.77%     | ok               |
|          40 | 16.69%   | 110.08%            | -24.92% |     0.4  |       56 | 44.26%     | ok               |
|          35 | 12.95%   | 110.08%            | -24.39% |     0.34 |       60 | 47.75%     | ok               |
|          25 | 6.38%    | 110.08%            | -26.24% |     0.23 |       65 | 52.08%     | ok               |

## CVX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -8.87%   | 34.84%             | -23.25% |    -0.14 |       73 | 46.09%     | ok               |
|          45 | -8.74%   | 34.84%             | -27.82% |    -0.17 |       63 | 35.94%     | ok               |
|          40 | -9.92%   | 34.84%             | -25.79% |    -0.19 |       73 | 39.60%     | ok               |
|          50 | -8.62%   | 34.84%             | -29.71% |    -0.2  |       56 | 31.45%     | ok               |
|          30 | -11.48%  | 34.84%             | -26.75% |    -0.22 |       67 | 43.26%     | ok               |

## DASH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 117.37%  | 110.62%            | -43.46% |     0.88 |       42 | 17.43%     | ok               |
|          40 | 72.73%   | 110.62%            | -42.64% |     0.69 |       48 | 23.75%     | ok               |
|          45 | 64.47%   | 110.62%            | -46.93% |     0.66 |       46 | 19.92%     | ok               |
|          30 | -15.19%  | 110.62%            | -64.43% |     0.28 |       57 | 30.27%     | ok               |
|          25 | -16.00%  | 110.62%            | -64.14% |     0.28 |       67 | 32.57%     | ok               |

## DBC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -2.43%   | 31.51%             | -26.01% |    -0.01 |       81 | 42.93%     | ok               |
|          20 | -8.86%   | 31.51%             | -25.69% |    -0.22 |       73 | 40.60%     | ok               |
|          25 | -9.03%   | 31.51%             | -24.84% |    -0.23 |       68 | 38.44%     | ok               |
|          50 | -8.86%   | 31.51%             | -18.84% |    -0.28 |       48 | 25.29%     | ok               |
|          45 | -10.62%  | 31.51%             | -20.02% |    -0.32 |       60 | 28.62%     | ok               |

## DE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 3.78%    | 80.23%             | -17.97% |     0.18 |       58 | 30.28%     | ok               |
|          45 | 1.32%    | 80.23%             | -18.05% |     0.12 |       58 | 34.28%     | ok               |
|          20 | -3.87%   | 80.23%             | -20.60% |     0.02 |       66 | 48.42%     | ok               |
|          30 | -4.78%   | 80.23%             | -22.44% |    -0    |       72 | 44.09%     | ok               |
|          25 | -5.27%   | 80.23%             | -20.79% |    -0.01 |       73 | 46.42%     | ok               |

## DIA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -7.64%   | 33.07%             | -13.58% |    -0.37 |       66 | 45.59%     | ok               |
|          20 | -9.75%   | 33.07%             | -15.48% |    -0.47 |       68 | 47.92%     | ok               |
|          35 | -9.33%   | 33.07%             | -16.94% |    -0.49 |       74 | 41.26%     | ok               |
|          30 | -9.73%   | 33.07%             | -16.20% |    -0.49 |       72 | 44.43%     | ok               |
|          40 | -11.91%  | 33.07%             | -18.41% |    -0.67 |       76 | 37.77%     | ok               |

## DIS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 49.09%   | 17.06%             | -10.17% |     1.34 |       50 | 28.79%     | ok               |
|          40 | 18.18%   | 17.06%             | -18.75% |     0.48 |       65 | 36.94%     | ok               |
|          45 | 15.44%   | 17.06%             | -16.54% |     0.45 |       51 | 32.45%     | ok               |
|          35 | 9.78%    | 17.06%             | -25.30% |     0.3  |       73 | 43.26%     | ok               |
|          15 | 5.73%    | 17.06%             | -32.73% |     0.22 |       79 | 55.74%     | ok               |

## DOGE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -12.52%  | -62.98%            | -59.12% |     0.12 |       80 | 63.22%     | ok               |
|          50 | -5.66%   | -62.98%            | -51.01% |     0.11 |       58 | 21.84%     | ok               |
|          20 | -12.89%  | -62.98%            | -58.83% |     0.1  |       79 | 57.47%     | ok               |
|          25 | -15.18%  | -62.98%            | -59.36% |     0.06 |       72 | 53.07%     | ok               |
|          30 | -16.17%  | -62.98%            | -60.39% |     0.03 |       68 | 47.70%     | ok               |

## DOT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -47.79%  | -79.04%            | -65.96% |    -0.32 |       83 | 55.56%     | ok               |
|          15 | -52.84%  | -79.04%            | -72.35% |    -0.34 |       72 | 59.39%     | ok               |
|          30 | -48.62%  | -79.04%            | -63.40% |    -0.39 |       80 | 45.02%     | ok               |
|          25 | -55.91%  | -79.04%            | -71.03% |    -0.49 |       74 | 50.57%     | ok               |
|          50 | -42.01%  | -79.04%            | -51.97% |    -0.59 |       58 | 22.03%     | ok               |

## DXY-INDEX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -3.04%   | -6.99%             | -5.53%  |    -0.5  |       40 | 30.52%     | ok               |
|          40 | -5.96%   | -6.99%             | -6.78%  |    -0.83 |       70 | 46.32%     | ok               |
|          45 | -5.94%   | -6.99%             | -7.61%  |    -0.89 |       64 | 37.23%     | ok               |
|          15 | -10.71%  | -6.99%             | -11.87% |    -1.1  |       99 | 72.08%     | ok               |
|          30 | -9.58%   | -6.99%             | -10.01% |    -1.24 |       80 | 56.28%     | ok               |

## EEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -4.02%   | 41.45%             | -25.18% |    -0.05 |       65 | 44.93%     | ok               |
|          25 | -5.07%   | 41.45%             | -23.69% |    -0.08 |       65 | 43.26%     | ok               |
|          35 | -6.85%   | 41.45%             | -23.88% |    -0.15 |       70 | 39.60%     | ok               |
|          15 | -8.17%   | 41.45%             | -26.83% |    -0.16 |       73 | 48.59%     | ok               |
|          40 | -7.31%   | 41.45%             | -19.52% |    -0.18 |       70 | 37.77%     | ok               |

## EFA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -0.91%   | 32.94%             | -10.10% |     0.03 |       60 | 49.08%     | ok               |
|          20 | -8.09%   | 32.94%             | -12.23% |    -0.28 |       67 | 46.26%     | ok               |
|          30 | -9.07%   | 32.94%             | -12.63% |    -0.35 |       64 | 38.94%     | ok               |
|          25 | -9.53%   | 32.94%             | -13.73% |    -0.36 |       68 | 42.60%     | ok               |
|          40 | -8.96%   | 32.94%             | -14.83% |    -0.38 |       60 | 34.44%     | ok               |

## EOG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -13.51%  | 24.20%             | -34.41% |    -0.24 |       48 | 32.45%     | ok               |
|          40 | -17.44%  | 24.20%             | -36.18% |    -0.34 |       60 | 35.44%     | ok               |
|          35 | -21.27%  | 24.20%             | -38.93% |    -0.43 |       73 | 39.43%     | ok               |
|          50 | -21.22%  | 24.20%             | -35.63% |    -0.48 |       52 | 29.78%     | ok               |
|          30 | -29.30%  | 24.20%             | -47.65% |    -0.62 |       76 | 43.93%     | ok               |

## ETC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -4.66%   | -60.37%            | -43.95% |     0.1  |       48 | 31.99%     | ok               |
|          50 | -2.30%   | -60.37%            | -28.33% |     0.1  |       28 | 18.20%     | ok               |
|          30 | -7.71%   | -60.37%            | -46.79% |     0.06 |       56 | 35.25%     | ok               |
|          45 | -6.54%   | -60.37%            | -35.44% |     0.03 |       32 | 21.26%     | ok               |
|          40 | -10.07%  | -60.37%            | -41.85% |    -0.01 |       50 | 26.25%     | ok               |

## ETH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 114.78%  | -17.70%            | -30.11% |     1.14 |       61 | 46.93%     | ok               |
|          30 | 77.70%   | -17.70%            | -32.89% |     0.88 |       65 | 54.79%     | ok               |
|          40 | 60.59%   | -17.70%            | -33.11% |     0.82 |       62 | 39.08%     | ok               |
|          25 | 56.41%   | -17.70%            | -40.90% |     0.72 |       63 | 58.62%     | ok               |
|          45 | 45.44%   | -17.70%            | -34.50% |     0.69 |       64 | 35.82%     | ok               |

## EWJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -20.56%  | 35.97%             | -30.00% |    -0.62 |       58 | 39.93%     | ok               |
|          25 | -22.51%  | 35.97%             | -29.85% |    -0.7  |       58 | 39.10%     | ok               |
|          15 | -24.37%  | 35.97%             | -31.15% |    -0.72 |       69 | 43.26%     | ok               |
|          30 | -24.12%  | 35.97%             | -29.40% |    -0.82 |       66 | 37.77%     | ok               |
|          45 | -25.74%  | 35.97%             | -28.08% |    -1.04 |       62 | 28.95%     | ok               |

## FCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 2.85%    | 22.18%             | -29.52% |     0.18 |       54 | 32.95%     | ok               |
|          50 | -2.93%   | 22.18%             | -26.57% |     0.09 |       56 | 29.12%     | ok               |
|          40 | -11.30%  | 22.18%             | -42.89% |    -0.03 |       66 | 37.94%     | ok               |
|          30 | -26.53%  | 22.18%             | -46.84% |    -0.25 |       69 | 45.42%     | ok               |
|          35 | -30.23%  | 22.18%             | -50.12% |    -0.34 |       71 | 43.09%     | ok               |

## FET-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 8.42%    | -80.14%            | -59.58% |     0.36 |       71 | 57.66%     | ok               |
|          25 | -18.10%  | -80.14%            | -65.31% |     0.12 |       79 | 49.04%     | ok               |
|          20 | -19.85%  | -80.14%            | -66.17% |     0.12 |       82 | 54.21%     | ok               |
|          30 | -32.83%  | -80.14%            | -66.52% |    -0.07 |       79 | 44.83%     | ok               |
|          45 | -36.32%  | -80.14%            | -51.19% |    -0.36 |       54 | 22.61%     | ok               |

## FIL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -38.14%  | -69.50%            | -60.64% |    -0.29 |       71 | 39.08%     | ok               |
|          40 | -38.70%  | -69.50%            | -57.60% |    -0.38 |       48 | 28.35%     | ok               |
|          15 | -53.23%  | -69.50%            | -72.54% |    -0.43 |       95 | 52.30%     | ok               |
|          35 | -46.39%  | -69.50%            | -65.88% |    -0.49 |       62 | 32.57%     | ok               |
|          20 | -60.93%  | -69.50%            | -77.06% |    -0.63 |       94 | 48.85%     | ok               |

## FXI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -2.30%   | 28.01%             | -21.68% |     0.03 |       52 | 34.94%     | ok               |
|          25 | -2.42%   | 28.01%             | -22.57% |     0.02 |       50 | 31.78%     | ok               |
|          30 | -4.56%   | 28.01%             | -23.91% |    -0.03 |       48 | 30.45%     | ok               |
|          35 | -6.68%   | 28.01%             | -27.53% |    -0.09 |       48 | 27.79%     | ok               |
|          20 | -7.57%   | 28.01%             | -24.53% |    -0.11 |       50 | 33.11%     | ok               |

## GDX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -2.77%   | 150.33%            | -31.05% |     0.12 |       82 | 51.25%     | ok               |
|          40 | -4.91%   | 150.33%            | -34.40% |     0.05 |       66 | 38.94%     | ok               |
|          30 | -6.33%   | 150.33%            | -34.27% |     0.04 |       68 | 45.09%     | ok               |
|          35 | -10.41%  | 150.33%            | -38.65% |    -0.03 |       74 | 41.60%     | ok               |
|          25 | -15.17%  | 150.33%            | -42.40% |    -0.09 |       72 | 46.92%     | ok               |

## GDXJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -16.76%  | 145.33%            | -34.84% |    -0.05 |       72 | 51.58%     | ok               |
|          35 | -28.09%  | 145.33%            | -38.07% |    -0.29 |       70 | 41.76%     | ok               |
|          30 | -30.08%  | 145.33%            | -35.99% |    -0.32 |       70 | 44.43%     | ok               |
|          25 | -34.32%  | 145.33%            | -39.65% |    -0.37 |       75 | 47.59%     | ok               |
|          40 | -30.83%  | 145.33%            | -46.14% |    -0.38 |       64 | 39.27%     | ok               |

## GE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 4.89%    | 104.79%            | -21.25% |     0.2  |       60 | 33.78%     | ok               |
|          45 | -7.35%   | 104.79%            | -21.88% |    -0.05 |       72 | 36.77%     | ok               |
|          20 | -13.05%  | 104.79%            | -25.05% |    -0.12 |       73 | 52.75%     | ok               |
|          30 | -13.14%  | 104.79%            | -27.82% |    -0.14 |       78 | 48.42%     | ok               |
|          25 | -13.54%  | 104.79%            | -29.91% |    -0.14 |       74 | 50.25%     | ok               |

## GLD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 21.05%   | 69.31%             | -13.87% |     0.54 |       48 | 47.59%     | ok               |
|          20 | 19.41%   | 69.31%             | -13.87% |     0.51 |       49 | 49.25%     | ok               |
|          30 | 11.67%   | 69.31%             | -14.15% |     0.35 |       52 | 46.09%     | ok               |
|          35 | 8.96%    | 69.31%             | -15.57% |     0.3  |       52 | 43.43%     | ok               |
|          15 | 9.15%    | 69.31%             | -18.05% |     0.29 |       55 | 52.75%     | ok               |

## GOOGL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 77.31%   | 63.01%             | -17.38% |     1.2  |       59 | 44.76%     | ok               |
|          30 | 74.51%   | 63.01%             | -16.84% |     1.14 |       57 | 48.59%     | ok               |
|          45 | 64.70%   | 63.01%             | -11.66% |     1.12 |       52 | 38.27%     | ok               |
|          25 | 71.84%   | 63.01%             | -16.16% |     1.1  |       57 | 51.08%     | ok               |
|          50 | 59.85%   | 63.01%             | -11.52% |     1.09 |       44 | 33.44%     | ok               |

## GRT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 90.43%   | -80.76%            | -36.70% |     0.84 |       70 | 62.45%     | ok               |
|          45 | 63.08%   | -80.76%            | -39.68% |     0.77 |       50 | 29.50%     | ok               |
|          30 | 61.62%   | -80.76%            | -43.87% |     0.71 |       75 | 47.89%     | ok               |
|          35 | 59.31%   | -80.76%            | -37.94% |     0.71 |       66 | 42.53%     | ok               |
|          25 | 61.33%   | -80.76%            | -37.25% |     0.7  |       80 | 53.07%     | ok               |

## GS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 22.58%   | 98.71%             | -20.56% |     0.5  |       66 | 55.24%     | ok               |
|          40 | 7.27%    | 98.71%             | -16.16% |     0.25 |       64 | 40.93%     | ok               |
|          20 | 7.49%    | 98.71%             | -23.19% |     0.25 |       64 | 51.91%     | ok               |
|          25 | -0.60%   | 98.71%             | -23.32% |     0.09 |       66 | 49.92%     | ok               |
|          35 | -1.92%   | 98.71%             | -19.95% |     0.06 |       68 | 44.59%     | ok               |

## HBAR-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -22.53%  | -36.25%            | -49.09% |    -0.3  |       28 | 27.84%     | ok               |
|          40 | -24.21%  | -36.25%            | -51.16% |    -0.32 |       32 | 33.68%     | ok               |
|          50 | -24.56%  | -36.25%            | -39.47% |    -0.41 |       32 | 18.90%     | ok               |
|          35 | -28.42%  | -36.25%            | -56.01% |    -0.41 |       30 | 38.83%     | ok               |
|          30 | -29.16%  | -36.25%            | -56.47% |    -0.42 |       40 | 42.96%     | ok               |

## HD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 6.13%    | -0.69%             | -17.15% |     0.23 |       71 | 44.76%     | ok               |
|          35 | 4.73%    | -0.69%             | -17.81% |     0.2  |       72 | 40.10%     | ok               |
|          25 | 2.51%    | -0.69%             | -18.17% |     0.15 |       72 | 47.25%     | ok               |
|          40 | 1.21%    | -0.69%             | -16.74% |     0.11 |       74 | 34.94%     | ok               |
|          45 | 0.42%    | -0.69%             | -17.41% |     0.08 |       50 | 30.12%     | ok               |

## HON Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -11.06%  | 7.82%              | -20.54% |    -0.28 |       64 | 31.61%     | ok               |
|          45 | -14.99%  | 7.82%              | -22.88% |    -0.39 |       66 | 36.94%     | ok               |
|          35 | -27.72%  | 7.82%              | -31.86% |    -0.74 |       89 | 48.75%     | ok               |
|          30 | -29.30%  | 7.82%              | -34.06% |    -0.76 |       89 | 53.74%     | ok               |
|          40 | -27.52%  | 7.82%              | -31.84% |    -0.76 |       76 | 41.26%     | ok               |

## HYG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -4.90%   | -0.16%             | -8.00%  |    -0.56 |       70 | 33.78%     | ok               |
|          45 | -6.66%   | -0.16%             | -9.14%  |    -0.81 |       70 | 30.12%     | ok               |
|          20 | -7.57%   | -0.16%             | -11.59% |    -0.81 |       94 | 45.09%     | ok               |
|          25 | -7.56%   | -0.16%             | -11.22% |    -0.82 |       89 | 42.43%     | ok               |
|          35 | -7.10%   | -0.16%             | -9.76%  |    -0.82 |       79 | 35.61%     | ok               |

## IBIT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 52.34%   | 9.66%              | -17.37% |     0.92 |       26 | 24.61%     | ok               |
|          15 | 61.83%   | 9.66%              | -19.20% |     0.89 |       48 | 42.77%     | ok               |
|          45 | 42.91%   | 9.66%              | -17.37% |     0.78 |       32 | 25.98%     | ok               |
|          30 | 32.53%   | 9.66%              | -18.95% |     0.61 |       46 | 35.35%     | ok               |
|          40 | 28.97%   | 9.66%              | -22.57% |     0.59 |       40 | 28.71%     | ok               |

## IBM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -14.59%  | 40.60%             | -49.43% |    -0.06 |       85 | 62.56%     | ok               |
|          35 | -18.22%  | 40.60%             | -47.10% |    -0.16 |       63 | 47.59%     | ok               |
|          30 | -19.93%  | 40.60%             | -48.94% |    -0.19 |       69 | 50.75%     | ok               |
|          20 | -26.85%  | 40.60%             | -53.45% |    -0.29 |       71 | 55.57%     | ok               |
|          50 | -27.41%  | 40.60%             | -45.97% |    -0.39 |       46 | 36.61%     | ok               |

## ICP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 2.49%    | -53.52%            | -40.43% |     0.29 |       72 | 39.66%     | ok               |
|          40 | -13.27%  | -53.52%            | -46.21% |     0.06 |       62 | 29.89%     | ok               |
|          35 | -14.64%  | -53.52%            | -52.13% |     0.06 |       70 | 34.29%     | ok               |
|          15 | -30.73%  | -53.52%            | -59.70% |     0.04 |       72 | 51.53%     | ok               |
|          20 | -30.08%  | -53.52%            | -63.34% |     0.03 |       80 | 48.47%     | ok               |

## IEF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.05%   | -3.52%             | -10.18% |    -0.71 |       72 | 42.76%     | ok               |
|          15 | -7.28%   | -3.52%             | -10.91% |    -0.83 |       71 | 44.43%     | ok               |
|          40 | -7.75%   | -3.52%             | -10.34% |    -1.11 |       64 | 26.62%     | ok               |
|          45 | -7.77%   | -3.52%             | -10.45% |    -1.15 |       60 | 24.63%     | ok               |
|          25 | -9.56%   | -3.52%             | -11.95% |    -1.19 |       76 | 39.77%     | ok               |

## IEMG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -2.00%   | 37.22%             | -23.73% |     0.01 |       61 | 43.59%     | ok               |
|          35 | -1.92%   | 37.22%             | -21.81% |     0    |       67 | 40.27%     | ok               |
|          20 | -3.65%   | 37.22%             | -25.26% |    -0.04 |       59 | 45.26%     | ok               |
|          40 | -3.59%   | 37.22%             | -18.43% |    -0.06 |       66 | 37.94%     | ok               |
|          30 | -5.19%   | 37.22%             | -24.73% |    -0.1  |       62 | 41.26%     | ok               |

## INJ-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 26.67%   | -37.81%            | -35.85% |     0.47 |       44 | 32.76%     | ok               |
|          35 | 23.68%   | -37.81%            | -46.78% |     0.45 |       54 | 36.02%     | ok               |
|          45 | 12.80%   | -37.81%            | -38.47% |     0.35 |       50 | 27.01%     | ok               |
|          15 | -15.39%  | -37.81%            | -66.08% |     0.14 |       69 | 46.93%     | ok               |
|          25 | -15.89%  | -37.81%            | -59.70% |     0.11 |       61 | 42.15%     | ok               |

## INTC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 102.17%  | 89.84%             | -49.32% |     0.85 |       60 | 34.78%     | ok               |
|          50 | 95.89%   | 89.84%             | -48.35% |     0.83 |       64 | 30.95%     | ok               |
|          40 | 79.99%   | 89.84%             | -55.86% |     0.74 |       68 | 38.94%     | ok               |
|          15 | 79.77%   | 89.84%             | -53.65% |     0.71 |       80 | 59.90%     | ok               |
|          20 | 73.14%   | 89.84%             | -52.47% |     0.69 |       82 | 56.07%     | ok               |

## INTU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 16.70%   | -44.74%            | -33.65% |     0.39 |       67 | 29.95%     | ok               |
|          35 | 12.80%   | -44.74%            | -40.91% |     0.32 |       69 | 42.43%     | ok               |
|          45 | 10.73%   | -44.74%            | -35.63% |     0.3  |       65 | 34.11%     | ok               |
|          25 | 9.19%    | -44.74%            | -35.24% |     0.27 |       69 | 50.75%     | ok               |
|          40 | 8.96%    | -44.74%            | -37.97% |     0.27 |       69 | 37.60%     | ok               |

## ITA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.12%   | 61.88%             | -21.48% |     0.06 |       68 | 34.94%     | ok               |
|          30 | -1.32%   | 61.88%             | -23.75% |     0.04 |       72 | 47.42%     | ok               |
|          15 | -2.43%   | 61.88%             | -28.17% |     0.03 |       72 | 60.07%     | ok               |
|          40 | -4.89%   | 61.88%             | -20.54% |    -0.08 |       70 | 39.93%     | ok               |
|          35 | -5.60%   | 61.88%             | -23.12% |    -0.09 |       72 | 43.59%     | ok               |

## IWM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          25 | 17.01%   | 40.36%             | -8.02% |     0.63 |       54 | 36.11%     | ok               |
|          20 | 15.47%   | 40.36%             | -9.67% |     0.57 |       60 | 37.10%     | ok               |
|          15 | 11.92%   | 40.36%             | -8.91% |     0.44 |       78 | 42.93%     | ok               |
|          30 | 10.62%   | 40.36%             | -8.62% |     0.43 |       58 | 34.78%     | ok               |
|          40 | 8.85%    | 40.36%             | -9.06% |     0.4  |       48 | 29.78%     | ok               |

## JNJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 20.50%   | 90.00%             | -10.97% |     0.8  |       44 | 35.61%     | ok               |
|          15 | 18.49%   | 90.00%             | -18.02% |     0.62 |       58 | 53.24%     | ok               |
|          30 | 13.39%   | 90.00%             | -17.51% |     0.5  |       60 | 46.76%     | ok               |
|          20 | 13.01%   | 90.00%             | -17.61% |     0.48 |       64 | 49.75%     | ok               |
|          45 | 10.19%   | 90.00%             | -13.35% |     0.43 |       50 | 39.27%     | ok               |

## JPM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 1.50%    | 72.18%             | -15.90% |     0.11 |       50 | 31.78%     | ok               |
|          45 | -8.97%   | 72.18%             | -21.91% |    -0.23 |       54 | 34.44%     | ok               |
|          20 | -24.26%  | 72.18%             | -35.58% |    -0.55 |       86 | 48.75%     | ok               |
|          40 | -21.46%  | 72.18%             | -28.47% |    -0.65 |       66 | 37.10%     | ok               |
|          35 | -22.15%  | 72.18%             | -27.43% |    -0.66 |       76 | 40.60%     | ok               |

## KO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 29.78%   | 55.85%             | -8.64%  |     0.98 |       52 | 39.10%     | ok               |
|          35 | 25.37%   | 55.85%             | -8.73%  |     0.87 |       56 | 37.60%     | ok               |
|          40 | 21.66%   | 55.85%             | -9.28%  |     0.8  |       58 | 34.44%     | ok               |
|          25 | 23.46%   | 55.85%             | -10.61% |     0.8  |       58 | 41.76%     | ok               |
|          50 | 8.73%    | 55.85%             | -16.13% |     0.39 |       44 | 28.62%     | ok               |

## LDO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 127.43%  | -59.61%            | -39.01% |     0.95 |       72 | 60.15%     | ok               |
|          20 | 81.77%   | -59.61%            | -44.07% |     0.78 |       75 | 55.36%     | ok               |
|          30 | 61.79%   | -59.61%            | -53.44% |     0.69 |       66 | 48.28%     | ok               |
|          25 | 47.04%   | -59.61%            | -48.17% |     0.61 |       74 | 52.87%     | ok               |
|          35 | 35.08%   | -59.61%            | -60.70% |     0.53 |       76 | 41.19%     | ok               |

## LIN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -1.22%   | 17.88%             | -22.01% |     0.02 |       71 | 44.09%     | ok               |
|          20 | -1.29%   | 17.88%             | -23.00% |     0.02 |       64 | 47.09%     | ok               |
|          15 | -3.20%   | 17.88%             | -23.68% |    -0.04 |       70 | 50.08%     | ok               |
|          30 | -4.51%   | 17.88%             | -20.61% |    -0.09 |       72 | 41.26%     | ok               |
|          45 | -4.85%   | 17.88%             | -17.04% |    -0.14 |       46 | 24.63%     | ok               |

## LINK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 31.72%   | -24.35%            | -35.01% |     0.52 |       68 | 43.10%     | ok               |
|          35 | 16.84%   | -24.35%            | -34.21% |     0.39 |       62 | 38.89%     | ok               |
|          45 | 12.72%   | -24.35%            | -33.71% |     0.34 |       54 | 29.69%     | ok               |
|          40 | 12.26%   | -24.35%            | -34.00% |     0.34 |       56 | 33.33%     | ok               |
|          50 | 12.32%   | -24.35%            | -27.70% |     0.33 |       46 | 24.52%     | ok               |

## LLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 4.74%    | 61.66%             | -38.23% |     0.2  |       50 | 35.44%     | ok               |
|          15 | -10.05%  | 61.66%             | -48.12% |    -0.01 |       70 | 60.23%     | ok               |
|          45 | -9.44%   | 61.66%             | -42.99% |    -0.06 |       60 | 39.27%     | ok               |
|          40 | -19.00%  | 61.66%             | -45.23% |    -0.23 |       70 | 42.43%     | ok               |
|          20 | -22.55%  | 61.66%             | -51.14% |    -0.25 |       77 | 55.41%     | ok               |

## LRCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 0.11%    | 109.54%            | -42.40% |     0.18 |       74 | 36.61%     | ok               |
|          40 | -3.24%   | 109.54%            | -47.73% |     0.16 |       70 | 42.76%     | ok               |
|          45 | -11.80%  | 109.54%            | -47.62% |     0.06 |       74 | 40.43%     | ok               |
|          35 | -15.50%  | 109.54%            | -56.72% |     0.03 |       80 | 45.09%     | ok               |
|          15 | -20.31%  | 109.54%            | -57.13% |     0.01 |       80 | 53.91%     | ok               |

## LTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 17.96%   | -41.56%            | -34.94% |     0.4  |       68 | 44.06%     | ok               |
|          45 | 13.98%   | -41.56%            | -36.44% |     0.36 |       56 | 33.14%     | ok               |
|          30 | 9.23%    | -41.56%            | -30.78% |     0.31 |       69 | 50.77%     | ok               |
|          25 | 7.96%    | -41.56%            | -34.22% |     0.29 |       69 | 53.45%     | ok               |
|          50 | 1.89%    | -41.56%            | -35.25% |     0.19 |       50 | 25.10%     | ok               |

## MCD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 11.59%   | 11.18%             | -9.22%  |     0.53 |       48 | 25.46%     | ok               |
|          30 | 11.39%   | 11.18%             | -22.20% |     0.43 |       75 | 40.43%     | ok               |
|          35 | 9.21%    | 11.18%             | -16.97% |     0.39 |       67 | 37.77%     | ok               |
|          25 | 7.94%    | 11.18%             | -23.93% |     0.32 |       75 | 42.93%     | ok               |
|          20 | 3.54%    | 11.18%             | -24.58% |     0.18 |       77 | 46.09%     | ok               |

## META Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -17.95%  | 27.84%             | -37.54% |    -0.22 |       68 | 39.43%     | ok               |
|          40 | -21.41%  | 27.84%             | -40.90% |    -0.28 |       68 | 42.76%     | ok               |
|          50 | -22.46%  | 27.84%             | -39.33% |    -0.34 |       68 | 34.94%     | ok               |
|          30 | -33.27%  | 27.84%             | -44.90% |    -0.5  |       72 | 50.58%     | ok               |
|          25 | -35.27%  | 27.84%             | -45.70% |    -0.54 |       73 | 53.24%     | ok               |

## MPC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 19.12%   | 124.32%            | -19.02% |     0.43 |       54 | 41.60%     | ok               |
|          40 | 17.16%   | 124.32%            | -20.88% |     0.39 |       64 | 48.25%     | ok               |
|          35 | 16.33%   | 124.32%            | -31.08% |     0.38 |       70 | 50.92%     | ok               |
|          45 | 15.10%   | 124.32%            | -20.23% |     0.37 |       60 | 45.59%     | ok               |
|          30 | 11.57%   | 124.32%            | -33.74% |     0.31 |       70 | 53.41%     | ok               |

## MRK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -12.46%  | 14.17%             | -28.39% |    -0.15 |       85 | 52.41%     | ok               |
|          25 | -13.23%  | 14.17%             | -31.07% |    -0.18 |       72 | 44.59%     | ok               |
|          20 | -17.48%  | 14.17%             | -29.34% |    -0.28 |       77 | 47.92%     | ok               |
|          50 | -13.92%  | 14.17%             | -23.01% |    -0.28 |       58 | 28.95%     | ok               |
|          45 | -16.06%  | 14.17%             | -25.38% |    -0.31 |       59 | 32.28%     | ok               |

## MS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 0.54%    | 92.49%             | -19.99% |     0.09 |       70 | 38.94%     | ok               |
|          15 | -0.39%   | 92.49%             | -22.02% |     0.09 |       74 | 57.40%     | ok               |
|          20 | -3.61%   | 92.49%             | -25.68% |     0.01 |       75 | 53.08%     | ok               |
|          30 | -7.56%   | 92.49%             | -27.79% |    -0.1  |       77 | 48.09%     | ok               |
|          25 | -9.02%   | 92.49%             | -28.36% |    -0.13 |       75 | 50.25%     | ok               |

## MSFT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -16.97%  | 19.62%             | -25.54% |    -0.4  |       72 | 37.10%     | ok               |
|          50 | -20.33%  | 19.62%             | -26.37% |    -0.53 |       62 | 31.95%     | ok               |
|          30 | -27.33%  | 19.62%             | -38.06% |    -0.6  |       81 | 50.92%     | ok               |
|          35 | -26.45%  | 19.62%             | -36.28% |    -0.6  |       75 | 46.59%     | ok               |
|          40 | -26.10%  | 19.62%             | -35.70% |    -0.62 |       71 | 40.77%     | ok               |

## MU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 112.29%  | 402.89%            | -61.15% |     0.9  |       60 | 45.26%     | ok               |
|          30 | 90.98%   | 402.89%            | -66.33% |     0.8  |       53 | 49.92%     | ok               |
|          35 | 85.70%   | 402.89%            | -66.69% |     0.78 |       65 | 47.59%     | ok               |
|          15 | 93.59%   | 402.89%            | -61.96% |     0.78 |       56 | 58.40%     | ok               |
|          45 | 77.60%   | 402.89%            | -62.31% |     0.75 |       62 | 42.76%     | ok               |

## NEAR-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 235.36%  | 51.04%             | -37.89% |     1.45 |       28 | 22.61%     | ok               |
|          40 | 257.67%  | 51.04%             | -41.76% |     1.41 |       40 | 32.38%     | ok               |
|          45 | 200.17%  | 51.04%             | -38.08% |     1.26 |       42 | 28.35%     | ok               |
|          30 | 169.55%  | 51.04%             | -47.35% |     1.11 |       63 | 42.91%     | ok               |
|          35 | 158.28%  | 51.04%             | -52.65% |     1.1  |       58 | 36.02%     | ok               |

## NEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -4.57%   | 180.21%            | -30.50% |     0.1  |       71 | 54.08%     | ok               |
|          15 | -7.30%   | 180.21%            | -35.45% |     0.08 |       66 | 58.74%     | ok               |
|          50 | -12.51%  | 180.21%            | -33.03% |    -0.06 |       48 | 37.77%     | ok               |
|          25 | -19.14%  | 180.21%            | -39.51% |    -0.12 |       68 | 51.75%     | ok               |
|          30 | -25.86%  | 180.21%            | -39.56% |    -0.25 |       70 | 49.75%     | ok               |

## NFLX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 18.18%   | -6.84%             | -20.78% |     0.49 |       54 | 39.10%     | ok               |
|          50 | 15.52%   | -6.84%             | -16.28% |     0.46 |       44 | 30.78%     | ok               |
|          35 | 14.16%   | -6.84%             | -18.30% |     0.39 |       78 | 43.76%     | ok               |
|          45 | 3.98%    | -6.84%             | -18.06% |     0.18 |       58 | 35.11%     | ok               |
|          15 | 0.71%    | -6.84%             | -26.59% |     0.13 |       76 | 63.89%     | ok               |

## NKE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -18.88%  | -59.54%            | -42.13% |    -0.2  |       73 | 40.10%     | ok               |
|          20 | -25.27%  | -59.54%            | -49.34% |    -0.24 |       87 | 55.24%     | ok               |
|          25 | -28.37%  | -59.54%            | -51.20% |    -0.3  |       87 | 52.58%     | ok               |
|          15 | -31.77%  | -59.54%            | -55.79% |    -0.35 |       90 | 59.07%     | ok               |
|          30 | -33.44%  | -59.54%            | -55.35% |    -0.41 |       87 | 47.92%     | ok               |

## NOW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -8.80%   | -32.17%            | -49.77% |     0.12 |       73 | 57.57%     | ok               |
|          30 | -9.93%   | -32.17%            | -42.66% |     0.1  |       81 | 52.08%     | ok               |
|          15 | -15.56%  | -32.17%            | -52.56% |     0.04 |       81 | 60.23%     | ok               |
|          25 | -16.39%  | -32.17%            | -47.93% |     0.03 |       73 | 55.41%     | ok               |
|          35 | -22.16%  | -32.17%            | -48.24% |    -0.09 |       84 | 47.25%     | ok               |

## NVDA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -26.29%  | 35.57%             | -39.50% |    -0.26 |       76 | 51.52%     | ok               |
|          25 | -31.50%  | 35.57%             | -44.52% |    -0.39 |       81 | 47.59%     | ok               |
|          30 | -31.28%  | 35.57%             | -43.72% |    -0.41 |       82 | 44.74%     | ok               |
|          15 | -38.63%  | 35.57%             | -51.51% |    -0.49 |       82 | 55.79%     | ok               |
|          35 | -41.61%  | 35.57%             | -52.08% |    -0.67 |       92 | 41.89%     | ok               |

## OP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 36.28%   | -83.60%            | -30.63% |     0.66 |       38 | 10.34%     | ok               |
|          45 | 26.69%   | -83.60%            | -28.24% |     0.49 |       40 | 16.48%     | ok               |
|          40 | 1.44%    | -83.60%            | -43.68% |     0.22 |       50 | 24.90%     | ok               |
|          15 | -34.47%  | -83.60%            | -55.83% |    -0.12 |       75 | 46.17%     | ok               |
|          35 | -30.75%  | -83.60%            | -56.85% |    -0.19 |       60 | 29.89%     | ok               |

## ORCL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 149.82%  | -17.44%            | -32.54% |     1.07 |       67 | 60.23%     | ok               |
|          45 | 92.99%   | -17.44%            | -32.35% |     0.9  |       54 | 37.94%     | ok               |
|          25 | 100.86%  | -17.44%            | -27.76% |     0.88 |       59 | 52.75%     | ok               |
|          35 | 91.35%   | -17.44%            | -31.95% |     0.85 |       60 | 46.92%     | ok               |
|          20 | 95.26%   | -17.44%            | -29.32% |     0.84 |       68 | 55.91%     | ok               |

## OXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -0.19%   | -8.87%             | -28.48% |     0.12 |       69 | 43.26%     | ok               |
|          35 | -0.62%   | -8.87%             | -26.37% |     0.11 |       70 | 39.10%     | ok               |
|          50 | -4.00%   | -8.87%             | -26.34% |     0.03 |       52 | 28.79%     | ok               |
|          40 | -4.78%   | -8.87%             | -28.30% |     0.02 |       60 | 35.94%     | ok               |
|          25 | -14.11%  | -8.87%             | -38.51% |    -0.12 |       77 | 46.92%     | ok               |

## PEP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 22.66%   | -13.84%            | -11.62% |     0.88 |       40 | 26.46%     | ok               |
|          45 | 10.30%   | -13.84%            | -14.22% |     0.44 |       52 | 30.12%     | ok               |
|          30 | 3.72%    | -13.84%            | -21.35% |     0.18 |       72 | 45.26%     | ok               |
|          35 | 2.10%    | -13.84%            | -21.42% |     0.13 |       75 | 39.60%     | ok               |
|          40 | -0.25%   | -13.84%            | -18.04% |     0.05 |       68 | 34.78%     | ok               |

## PEPE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -35.75%  | -54.34%            | -62.24% |    -0    |       79 | 61.11%     | ok               |
|          30 | -33.64%  | -54.34%            | -57.70% |    -0.09 |       74 | 46.74%     | ok               |
|          20 | -38.88%  | -54.34%            | -61.07% |    -0.1  |       87 | 56.90%     | ok               |
|          35 | -39.64%  | -54.34%            | -58.37% |    -0.24 |       66 | 42.91%     | ok               |
|          25 | -50.50%  | -54.34%            | -62.02% |    -0.32 |       88 | 51.72%     | ok               |

## PFE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -12.28%  | 5.84%              | -23.37% |    -0.35 |       50 | 22.63%     | ok               |
|          50 | -11.32%  | 5.84%              | -25.42% |    -0.35 |       38 | 19.30%     | ok               |
|          40 | -13.92%  | 5.84%              | -27.08% |    -0.39 |       70 | 27.62%     | ok               |
|          35 | -22.21%  | 5.84%              | -32.87% |    -0.65 |       80 | 34.11%     | ok               |
|          30 | -32.42%  | 5.84%              | -41.77% |    -0.98 |       77 | 37.44%     | ok               |

## PG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -6.51%   | 0.59%              | -20.08% |    -0.2  |       52 | 29.78%     | ok               |
|          35 | -9.70%   | 0.59%              | -18.99% |    -0.31 |       60 | 33.28%     | ok               |
|          45 | -14.44%  | 0.59%              | -22.00% |    -0.54 |       52 | 27.45%     | ok               |
|          30 | -17.91%  | 0.59%              | -24.55% |    -0.61 |       62 | 36.44%     | ok               |
|          25 | -19.78%  | 0.59%              | -25.84% |    -0.69 |       74 | 37.94%     | ok               |

## PM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -5.25%   | 91.95%             | -35.28% |    -0.03 |       86 | 44.76%     | ok               |
|          20 | -7.73%   | 91.95%             | -36.74% |    -0.08 |       85 | 53.41%     | ok               |
|          30 | -8.23%   | 91.95%             | -38.30% |    -0.1  |       81 | 48.25%     | ok               |
|          50 | -9.22%   | 91.95%             | -36.94% |    -0.16 |       66 | 35.44%     | ok               |
|          40 | -11.50%  | 91.95%             | -39.92% |    -0.21 |       78 | 41.10%     | ok               |

## POL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 5.09%    | -57.78%            | -44.63% |     0.27 |       83 | 50.00%     | ok               |
|          25 | -1.96%   | -57.78%            | -44.63% |     0.21 |       73 | 54.79%     | ok               |
|          20 | -6.66%   | -57.78%            | -47.73% |     0.16 |       84 | 58.62%     | ok               |
|          40 | -3.57%   | -57.78%            | -31.71% |     0.14 |       60 | 32.18%     | ok               |
|          50 | -4.33%   | -57.78%            | -29.40% |     0.09 |       52 | 21.07%     | ok               |

## QCOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -26.03%  | -19.46%            | -51.39% |    -0.17 |       73 | 42.26%     | ok               |
|          20 | -31.47%  | -19.46%            | -51.25% |    -0.25 |       69 | 45.59%     | ok               |
|          35 | -32.27%  | -19.46%            | -47.20% |    -0.31 |       81 | 37.94%     | ok               |
|          15 | -39.75%  | -19.46%            | -55.06% |    -0.39 |       71 | 48.25%     | ok               |
|          30 | -40.18%  | -19.46%            | -53.61% |    -0.45 |       79 | 40.43%     | ok               |

## QQQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 5.86%    | 40.15%             | -15.74% |     0.22 |       71 | 52.75%     | ok               |
|          25 | 2.38%    | 40.15%             | -12.88% |     0.14 |       65 | 45.59%     | ok               |
|          20 | 1.15%    | 40.15%             | -13.42% |     0.11 |       77 | 48.75%     | ok               |
|          30 | -4.53%   | 40.15%             | -14.40% |    -0.04 |       70 | 43.59%     | ok               |
|          35 | -14.94%  | 40.15%             | -20.59% |    -0.37 |       76 | 39.60%     | ok               |

## RENDER-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 21.21%   | -58.81%            | -44.59% |     0.45 |       84 | 63.60%     | ok               |
|          20 | 11.52%   | -58.81%            | -43.43% |     0.38 |       91 | 59.00%     | ok               |
|          25 | -0.83%   | -58.81%            | -43.13% |     0.28 |       89 | 54.21%     | ok               |
|          30 | -43.06%  | -58.81%            | -54.46% |    -0.25 |       92 | 48.47%     | ok               |
|          35 | -42.93%  | -58.81%            | -54.35% |    -0.29 |       84 | 42.72%     | ok               |

## RTX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 34.11%   | 90.61%             | -18.66% |     0.72 |       74 | 57.57%     | ok               |
|          25 | 29.53%   | 90.61%             | -18.59% |     0.65 |       62 | 54.91%     | ok               |
|          15 | 26.01%   | 90.61%             | -19.55% |     0.58 |       67 | 62.06%     | ok               |
|          30 | 20.73%   | 90.61%             | -16.99% |     0.51 |       71 | 52.08%     | ok               |
|          50 | 14.34%   | 90.61%             | -18.42% |     0.46 |       60 | 39.27%     | ok               |

## SBUX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 5.78%    | 37.92%             | -23.55% |     0.22 |       61 | 42.26%     | ok               |
|          40 | 3.57%    | 37.92%             | -25.43% |     0.17 |       60 | 33.78%     | ok               |
|          45 | 1.60%    | 37.92%             | -27.26% |     0.13 |       66 | 28.95%     | ok               |
|          35 | 0.00%    | 37.92%             | -26.54% |     0.1  |       64 | 37.10%     | ok               |
|          50 | -3.76%   | 37.92%             | -25.13% |    -0.01 |       52 | 24.46%     | ok               |

## SCHW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -1.47%   | 27.96%             | -29.24% |     0.06 |       71 | 52.58%     | ok               |
|          25 | -3.28%   | 27.96%             | -28.76% |     0.02 |       67 | 50.92%     | ok               |
|          45 | -3.45%   | 27.96%             | -16.53% |    -0.04 |       62 | 31.28%     | ok               |
|          15 | -6.89%   | 27.96%             | -31.37% |    -0.06 |       78 | 56.57%     | ok               |
|          50 | -3.90%   | 27.96%             | -13.28% |    -0.08 |       54 | 28.12%     | ok               |

## SHIB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -20.46%  | -64.41%            | -43.76% |    -0.05 |       85 | 66.48%     | ok               |
|          50 | -14.09%  | -64.41%            | -32.18% |    -0.09 |       50 | 22.03%     | ok               |
|          20 | -23.85%  | -64.41%            | -47.65% |    -0.11 |       80 | 61.88%     | ok               |
|          35 | -24.17%  | -64.41%            | -43.57% |    -0.17 |       75 | 46.36%     | ok               |
|          40 | -27.18%  | -64.41%            | -41.51% |    -0.26 |       60 | 37.55%     | ok               |

## SHY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          30 | -2.37%   | -0.36%             | -3.30% |    -0.77 |       54 | 38.60%     | ok               |
|          40 | -2.63%   | -0.36%             | -3.58% |    -0.89 |       58 | 34.94%     | ok               |
|          45 | -2.54%   | -0.36%             | -3.43% |    -0.93 |       56 | 28.62%     | ok               |
|          35 | -2.90%   | -0.36%             | -3.61% |    -0.96 |       56 | 36.44%     | ok               |
|          50 | -2.67%   | -0.36%             | -3.40% |    -1.03 |       48 | 24.79%     | ok               |

## SKY-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -56.28%  | -18.50%            | -65.72% |    -0.72 |       79 | 55.36%     | ok               |
|          35 | -53.00%  | -18.50%            | -60.94% |    -0.81 |       78 | 36.78%     | ok               |
|          30 | -56.20%  | -18.50%            | -63.60% |    -0.84 |       87 | 44.83%     | ok               |
|          25 | -61.15%  | -18.50%            | -66.89% |    -0.95 |       80 | 48.08%     | ok               |
|          40 | -57.23%  | -18.50%            | -63.28% |    -0.99 |       66 | 33.33%     | ok               |

## SLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -6.18%   | 9.77%              | -25.01% |    -0.03 |       56 | 31.11%     | ok               |
|          40 | -7.15%   | 9.77%              | -26.80% |    -0.04 |       50 | 33.94%     | ok               |
|          50 | -10.06%  | 9.77%              | -27.89% |    -0.16 |       44 | 24.46%     | ok               |
|          35 | -31.70%  | 9.77%              | -44.36% |    -0.61 |       74 | 41.76%     | ok               |
|          25 | -41.25%  | 9.77%              | -53.22% |    -0.8  |       85 | 51.75%     | ok               |

## SLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 66.55%   | 66.00%             | -28.72% |     0.86 |       50 | 31.45%     | ok               |
|          45 | 52.41%   | 66.00%             | -31.33% |     0.73 |       61 | 32.95%     | ok               |
|          40 | 51.20%   | 66.00%             | -34.28% |     0.72 |       65 | 34.94%     | ok               |
|          20 | 41.57%   | 66.00%             | -37.05% |     0.61 |       70 | 45.26%     | ok               |
|          15 | 39.20%   | 66.00%             | -47.98% |     0.57 |       71 | 49.92%     | ok               |

## SMH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 65.69%   | 79.84%             | -31.66% |     0.91 |       49 | 44.93%     | ok               |
|          25 | 50.71%   | 79.84%             | -33.57% |     0.78 |       46 | 43.43%     | ok               |
|          30 | 46.60%   | 79.84%             | -34.29% |     0.74 |       50 | 42.10%     | ok               |
|          35 | 35.69%   | 79.84%             | -34.65% |     0.63 |       56 | 40.10%     | ok               |
|          45 | 23.70%   | 79.84%             | -32.84% |     0.5  |       56 | 34.28%     | ok               |

## SNX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 28.14%   | -75.11%            | -29.01% |     0.51 |       46 | 26.63%     | ok               |
|          35 | 28.07%   | -75.11%            | -41.29% |     0.5  |       52 | 30.84%     | ok               |
|          20 | 18.60%   | -75.11%            | -53.03% |     0.42 |       71 | 46.17%     | ok               |
|          15 | 5.49%    | -75.11%            | -54.74% |     0.3  |       72 | 50.19%     | ok               |
|          30 | 5.24%    | -75.11%            | -50.74% |     0.28 |       62 | 36.97%     | ok               |

## SOL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 55.44%   | -45.45%            | -39.12% |     0.74 |       56 | 38.51%     | ok               |
|          35 | 29.72%   | -45.45%            | -43.12% |     0.51 |       68 | 44.64%     | ok               |
|          45 | 11.87%   | -45.45%            | -46.28% |     0.33 |       50 | 32.38%     | ok               |
|          25 | 9.26%    | -45.45%            | -37.29% |     0.32 |       69 | 55.56%     | ok               |
|          30 | 8.28%    | -45.45%            | -41.75% |     0.31 |       75 | 51.15%     | ok               |

## SOXX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 58.82%   | 74.35%             | -39.32% |     0.82 |       55 | 43.09%     | ok               |
|          35 | 55.25%   | 74.35%             | -38.76% |     0.8  |       58 | 38.60%     | ok               |
|          30 | 54.41%   | 74.35%             | -39.81% |     0.78 |       56 | 40.93%     | ok               |
|          20 | 44.80%   | 74.35%             | -39.19% |     0.68 |       61 | 44.09%     | ok               |
|          40 | 36.26%   | 74.35%             | -41.03% |     0.61 |       60 | 36.44%     | ok               |

## SPY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 4.32%    | 37.10%             | -14.25% |     0.2  |       60 | 51.25%     | ok               |
|          15 | 1.79%    | 37.10%             | -16.80% |     0.12 |       66 | 54.24%     | ok               |
|          25 | -0.37%   | 37.10%             | -14.25% |     0.05 |       60 | 50.25%     | ok               |
|          30 | -5.24%   | 37.10%             | -15.53% |    -0.12 |       63 | 47.75%     | ok               |
|          35 | -6.16%   | 37.10%             | -15.58% |    -0.17 |       61 | 44.59%     | ok               |

## SUSHI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -8.82%   | -72.76%            | -34.86% |     0.04 |       60 | 17.05%     | ok               |
|          45 | -35.78%  | -72.76%            | -58.06% |    -0.36 |       64 | 23.37%     | ok               |
|          35 | -42.79%  | -72.76%            | -68.76% |    -0.37 |       79 | 37.36%     | ok               |
|          40 | -40.37%  | -72.76%            | -62.11% |    -0.39 |       66 | 31.61%     | ok               |
|          15 | -62.45%  | -72.76%            | -78.43% |    -0.6  |       85 | 53.07%     | ok               |

## T Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 69.07%   | 21.15%             | -15.08% |     1.09 |       71 | 66.22%     | ok               |
|          20 | 64.90%   | 21.15%             | -18.13% |     1.07 |       66 | 61.73%     | ok               |
|          25 | 63.02%   | 21.15%             | -17.66% |     1.06 |       66 | 59.57%     | ok               |
|          30 | 52.26%   | 21.15%             | -17.01% |     0.94 |       68 | 57.57%     | ok               |
|          35 | 34.35%   | 21.15%             | -14.49% |     0.71 |       76 | 52.91%     | ok               |

## TGT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -8.89%   | 12.83%             | -32.83% |    -0.11 |       58 | 37.27%     | ok               |
|          25 | -10.70%  | 12.83%             | -34.49% |    -0.14 |       66 | 40.27%     | ok               |
|          20 | -13.69%  | 12.83%             | -36.76% |    -0.18 |       84 | 44.76%     | ok               |
|          45 | -12.30%  | 12.83%             | -26.12% |    -0.24 |       48 | 28.79%     | ok               |
|          15 | -19.64%  | 12.83%             | -36.20% |    -0.3  |       70 | 49.58%     | ok               |

## TIA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -23.70%  | -78.60%            | -66.82% |     0.14 |       95 | 59.77%     | ok               |
|          25 | -34.03%  | -78.60%            | -69.36% |    -0.02 |       94 | 49.04%     | ok               |
|          35 | -27.60%  | -78.60%            | -66.58% |    -0.07 |       74 | 36.40%     | ok               |
|          20 | -40.66%  | -78.60%            | -70.15% |    -0.07 |       91 | 54.21%     | ok               |
|          30 | -45.91%  | -78.60%            | -75.93% |    -0.21 |       91 | 43.49%     | ok               |

## TLT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -6.80%   | -13.92%            | -12.00% |    -0.75 |       32 | 16.81%     | ok               |
|          40 | -12.96%  | -13.92%            | -17.65% |    -1.14 |       48 | 24.96%     | ok               |
|          45 | -10.98%  | -13.92%            | -14.68% |    -1.14 |       42 | 20.13%     | ok               |
|          30 | -20.93%  | -13.92%            | -22.01% |    -1.58 |       66 | 34.28%     | ok               |
|          35 | -19.47%  | -13.92%            | -20.56% |    -1.62 |       64 | 29.45%     | ok               |

## TMO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 50.73%   | 28.89%             | -8.17%  |     1.07 |       50 | 35.27%     | ok               |
|          45 | 49.68%   | 28.89%             | -9.69%  |     1    |       54 | 40.27%     | ok               |
|          40 | 42.51%   | 28.89%             | -11.54% |     0.87 |       59 | 45.42%     | ok               |
|          35 | 45.43%   | 28.89%             | -13.84% |     0.86 |       67 | 50.75%     | ok               |
|          20 | 40.10%   | 28.89%             | -22.89% |     0.73 |       76 | 62.06%     | ok               |

## TMUS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -5.37%   | -4.17%             | -41.04% |     0    |       68 | 59.73%     | ok               |
|          30 | -6.64%   | -4.17%             | -33.05% |    -0.04 |       74 | 46.92%     | ok               |
|          25 | -9.29%   | -4.17%             | -39.29% |    -0.09 |       75 | 49.92%     | ok               |
|          20 | -10.83%  | -4.17%             | -39.79% |    -0.12 |       74 | 54.08%     | ok               |
|          50 | -9.60%   | -4.17%             | -32.38% |    -0.2  |       60 | 32.45%     | ok               |

## TRX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 11.16%   | 12.60%             | -18.79% |     0.41 |       54 | 38.51%     | ok               |
|          50 | 3.84%    | 12.60%             | -22.22% |     0.2  |       44 | 32.95%     | ok               |
|          35 | 3.63%    | 12.60%             | -21.77% |     0.19 |       62 | 45.59%     | ok               |
|          45 | 2.78%    | 12.60%             | -24.19% |     0.16 |       48 | 34.87%     | ok               |
|          30 | 2.55%    | 12.60%             | -22.90% |     0.16 |       62 | 48.08%     | ok               |

## TSLA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 47.27%   | 109.16%            | -30.57% |     0.66 |       62 | 29.95%     | ok               |
|          40 | 18.38%   | 109.16%            | -50.11% |     0.38 |       61 | 35.44%     | ok               |
|          45 | -6.85%   | 109.16%            | -52.01% |     0.11 |       67 | 32.45%     | ok               |
|          35 | -14.63%  | 109.16%            | -58.86% |     0.04 |       72 | 38.10%     | ok               |
|          25 | -29.74%  | 109.16%            | -55.60% |    -0.14 |       70 | 45.59%     | ok               |

## TXN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -2.50%   | 55.90%             | -43.95% |     0.09 |       70 | 31.61%     | ok               |
|          35 | -17.64%  | 55.90%             | -42.08% |    -0.15 |       84 | 45.42%     | ok               |
|          20 | -23.51%  | 55.90%             | -37.19% |    -0.19 |       74 | 55.24%     | ok               |
|          15 | -25.25%  | 55.90%             | -38.02% |    -0.21 |       79 | 59.57%     | ok               |
|          40 | -22.68%  | 55.90%             | -44.52% |    -0.25 |       78 | 42.93%     | ok               |

## UNH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 37.46%   | -16.39%            | -26.31% |     0.6  |       73 | 48.75%     | ok               |
|          50 | 31.88%   | -16.39%            | -36.71% |     0.56 |       52 | 29.95%     | ok               |
|          35 | 33.36%   | -16.39%            | -27.21% |     0.56 |       66 | 43.76%     | ok               |
|          15 | 32.35%   | -16.39%            | -26.07% |     0.53 |       82 | 63.89%     | ok               |
|          20 | 29.98%   | -16.39%            | -26.96% |     0.51 |       75 | 57.57%     | ok               |

## UNI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 80.67%   | 5.53%              | -22.21% |     0.87 |       46 | 25.48%     | ok               |
|          45 | 64.28%   | 5.53%              | -30.17% |     0.74 |       52 | 32.57%     | ok               |
|          40 | 48.20%   | 5.53%              | -43.84% |     0.63 |       60 | 38.70%     | ok               |
|          35 | 36.05%   | 5.53%              | -48.64% |     0.54 |       64 | 43.87%     | ok               |
|          20 | -17.07%  | 5.53%              | -68.99% |     0.15 |       86 | 58.05%     | ok               |

## UPS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -17.36%  | -18.86%            | -25.27% |    -0.28 |       58 | 33.44%     | ok               |
|          50 | -16.20%  | -18.86%            | -24.11% |    -0.3  |       42 | 24.29%     | ok               |
|          20 | -28.03%  | -18.86%            | -35.46% |    -0.45 |       82 | 50.25%     | ok               |
|          15 | -30.40%  | -18.86%            | -37.58% |    -0.5  |       84 | 53.74%     | ok               |
|          35 | -28.29%  | -18.86%            | -31.79% |    -0.51 |       63 | 37.44%     | ok               |

## USO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 7.92%    | 78.13%             | -37.92% |     0.26 |       66 | 41.60%     | ok               |
|          20 | 2.94%    | 78.13%             | -41.23% |     0.19 |       70 | 38.27%     | ok               |
|          45 | 2.33%    | 78.13%             | -35.01% |     0.17 |       50 | 26.62%     | ok               |
|          25 | -5.62%   | 78.13%             | -42.94% |     0.07 |       66 | 36.27%     | ok               |
|          50 | -4.73%   | 78.13%             | -29.83% |     0.05 |       52 | 24.79%     | ok               |

## VEA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 2.76%    | 39.05%             | -16.79% |     0.16 |       58 | 50.08%     | ok               |
|          20 | -1.45%   | 39.05%             | -17.78% |    -0    |       59 | 47.42%     | ok               |
|          25 | -5.88%   | 39.05%             | -18.46% |    -0.19 |       59 | 45.26%     | ok               |
|          30 | -7.02%   | 39.05%             | -18.84% |    -0.25 |       64 | 41.26%     | ok               |
|          35 | -7.67%   | 39.05%             | -17.88% |    -0.29 |       50 | 38.77%     | ok               |

## VIXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -54.55%  | -60.14%            | -69.78% |    -0.63 |       34 | 8.65%      | ok               |
|          45 | -64.29%  | -60.14%            | -75.03% |    -0.84 |       54 | 13.64%     | ok               |
|          40 | -73.26%  | -60.14%            | -81.61% |    -1.01 |       70 | 17.80%     | ok               |
|          35 | -79.88%  | -60.14%            | -85.20% |    -1.15 |       94 | 24.46%     | ok               |
|          30 | -84.10%  | -60.14%            | -91.23% |    -1.16 |       96 | 31.61%     | ok               |

## VNQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -5.83%   | 15.90%             | -22.16% |    -0.18 |       69 | 43.26%     | ok               |
|          45 | -6.17%   | 15.90%             | -19.07% |    -0.24 |       60 | 28.45%     | ok               |
|          50 | -7.09%   | 15.90%             | -17.13% |    -0.3  |       52 | 25.12%     | ok               |
|          30 | -9.84%   | 15.90%             | -24.92% |    -0.35 |       71 | 40.27%     | ok               |
|          20 | -10.64%  | 15.90%             | -23.83% |    -0.37 |       74 | 45.92%     | ok               |

## VTI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 5.74%    | 37.52%             | -13.96% |     0.25 |       63 | 51.75%     | ok               |
|          15 | -1.50%   | 37.52%             | -15.70% |     0.02 |       62 | 54.41%     | ok               |
|          25 | -4.76%   | 37.52%             | -15.00% |    -0.1  |       57 | 49.75%     | ok               |
|          40 | -8.94%   | 37.52%             | -19.77% |    -0.3  |       70 | 40.10%     | ok               |
|          35 | -10.94%  | 37.52%             | -20.22% |    -0.37 |       64 | 44.43%     | ok               |

## VWO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -8.00%   | 27.60%             | -21.68% |    -0.27 |       56 | 29.78%     | ok               |
|          15 | -10.18%  | 27.60%             | -24.01% |    -0.29 |       72 | 46.92%     | ok               |
|          20 | -10.20%  | 27.60%             | -26.14% |    -0.3  |       67 | 44.93%     | ok               |
|          45 | -9.79%   | 27.60%             | -23.75% |    -0.34 |       58 | 32.28%     | ok               |
|          40 | -10.04%  | 27.60%             | -23.57% |    -0.34 |       68 | 35.27%     | ok               |

## VZ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -2.64%   | 15.08%             | -12.55% |    -0.02 |       56 | 28.45%     | ok               |
|          20 | -21.86%  | 15.08%             | -35.02% |    -0.42 |       79 | 52.91%     | ok               |
|          25 | -18.67%  | 15.08%             | -26.32% |    -0.46 |       82 | 47.92%     | ok               |
|          35 | -18.88%  | 15.08%             | -26.97% |    -0.55 |       64 | 39.10%     | ok               |
|          45 | -18.61%  | 15.08%             | -26.23% |    -0.57 |       72 | 32.95%     | ok               |

## WFC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -10.63%  | 45.45%             | -22.54% |    -0.17 |       79 | 43.09%     | ok               |
|          50 | -8.46%   | 45.45%             | -18.29% |    -0.21 |       58 | 32.28%     | ok               |
|          20 | -23.18%  | 45.45%             | -29.87% |    -0.38 |       82 | 52.75%     | ok               |
|          45 | -15.33%  | 45.45%             | -24.02% |    -0.39 |       66 | 36.61%     | ok               |
|          30 | -21.97%  | 45.45%             | -29.78% |    -0.4  |       84 | 46.42%     | ok               |

## WIF-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 44.12%   | -82.28%            | -40.67% |     0.58 |       67 | 49.04%     | ok               |
|          25 | 22.92%   | -82.28%            | -44.74% |     0.45 |       63 | 45.02%     | ok               |
|          15 | 12.63%   | -82.28%            | -46.21% |     0.39 |       77 | 52.30%     | ok               |
|          30 | -3.27%   | -82.28%            | -48.32% |     0.24 |       64 | 42.34%     | ok               |
|          35 | -7.86%   | -82.28%            | -52.54% |     0.14 |       60 | 36.40%     | ok               |

## WMT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 37.67%   | 84.61%             | -12.87% |     1.09 |       38 | 36.61%     | ok               |
|          45 | 36.51%   | 84.61%             | -14.82% |     1.02 |       44 | 38.94%     | ok               |
|          35 | 26.55%   | 84.61%             | -18.90% |     0.75 |       60 | 45.26%     | ok               |
|          40 | 24.92%   | 84.61%             | -19.17% |     0.73 |       52 | 40.60%     | ok               |
|          15 | 7.98%    | 84.61%             | -26.82% |     0.27 |       84 | 59.23%     | ok               |

## XBI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 13.75%   | 72.50%             | -16.08% |     0.41 |       50 | 33.44%     | ok               |
|          45 | 9.43%    | 72.50%             | -15.46% |     0.32 |       48 | 30.95%     | ok               |
|          35 | 2.78%    | 72.50%             | -17.66% |     0.15 |       58 | 36.27%     | ok               |
|          30 | 0.63%    | 72.50%             | -17.66% |     0.1  |       60 | 37.77%     | ok               |
|          50 | 0.20%    | 72.50%             | -15.41% |     0.08 |       48 | 27.95%     | ok               |

## XLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 2.12%    | 17.93%             | -15.73% |     0.14 |       40 | 24.46%     | ok               |
|          40 | 1.80%    | 17.93%             | -17.29% |     0.12 |       54 | 28.79%     | ok               |
|          45 | -0.93%   | 17.93%             | -17.09% |     0.02 |       42 | 26.29%     | ok               |
|          35 | -1.93%   | 17.93%             | -20.65% |    -0.01 |       54 | 31.95%     | ok               |
|          25 | -5.44%   | 17.93%             | -21.62% |    -0.13 |       62 | 37.94%     | ok               |

## XLC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 5.66%    | 27.69%             | -12.33% |     0.25 |       61 | 49.58%     | ok               |
|          25 | 5.14%    | 27.69%             | -12.31% |     0.23 |       60 | 51.75%     | ok               |
|          20 | 4.55%    | 27.69%             | -11.04% |     0.21 |       63 | 54.24%     | ok               |
|          50 | 3.13%    | 27.69%             | -12.48% |     0.19 |       64 | 37.60%     | ok               |
|          40 | 1.14%    | 27.69%             | -13.38% |     0.1  |       62 | 43.26%     | ok               |

## XLE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.76%   | 37.83%             | -25.98% |     0.06 |       58 | 38.60%     | ok               |
|          45 | -2.44%   | 37.83%             | -28.46% |     0.01 |       60 | 41.10%     | ok               |
|          20 | -8.09%   | 37.83%             | -34.45% |    -0.1  |       79 | 52.25%     | ok               |
|          30 | -7.47%   | 37.83%             | -34.77% |    -0.11 |       68 | 47.25%     | ok               |
|          15 | -9.28%   | 37.83%             | -36.62% |    -0.12 |       95 | 56.24%     | ok               |

## XLF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 6.68%    | 40.49%             | -20.19% |     0.27 |       70 | 56.57%     | ok               |
|          20 | 6.02%    | 40.49%             | -18.63% |     0.25 |       70 | 53.91%     | ok               |
|          25 | -1.38%   | 40.49%             | -23.22% |     0.02 |       77 | 50.75%     | ok               |
|          30 | -2.02%   | 40.49%             | -23.61% |    -0.01 |       78 | 48.75%     | ok               |
|          35 | -10.05%  | 40.49%             | -24.48% |    -0.33 |       70 | 45.26%     | ok               |

## XLI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 5.38%    | 36.92%             | -11.06% |     0.24 |       85 | 51.58%     | ok               |
|          20 | 0.03%    | 36.92%             | -12.74% |     0.06 |       77 | 46.59%     | ok               |
|          45 | -4.05%   | 36.92%             | -16.29% |    -0.13 |       68 | 34.11%     | ok               |
|          50 | -5.33%   | 36.92%             | -14.94% |    -0.21 |       62 | 31.61%     | ok               |
|          40 | -7.57%   | 36.92%             | -14.16% |    -0.28 |       76 | 36.27%     | ok               |

## XLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 41.82%   | 47.64%             | -14.75% |     0.84 |       42 | 45.59%     | ok               |
|          20 | 42.16%   | 47.64%             | -17.85% |     0.82 |       52 | 47.92%     | ok               |
|          15 | 44.30%   | 47.64%             | -17.54% |     0.82 |       53 | 50.58%     | ok               |
|          30 | 33.34%   | 47.64%             | -17.32% |     0.73 |       42 | 44.26%     | ok               |
|          35 | 18.46%   | 47.64%             | -19.14% |     0.48 |       56 | 41.43%     | ok               |

## XLM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 13.14%   | -45.88%            | -49.86% |     0.35 |       73 | 51.92%     | ok               |
|          40 | 10.25%   | -45.88%            | -48.91% |     0.32 |       56 | 35.82%     | ok               |
|          50 | 9.82%    | -45.88%            | -47.56% |     0.3  |       40 | 23.95%     | ok               |
|          15 | 5.29%    | -45.88%            | -61.51% |     0.29 |       76 | 60.73%     | ok               |
|          30 | 7.07%    | -45.88%            | -54.58% |     0.29 |       73 | 49.23%     | ok               |

## XLP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          45 | 21.62%   | 17.29%             | -5.66% |     1.07 |       48 | 32.28%     | ok               |
|          50 | 18.75%   | 17.29%             | -6.08% |     0.96 |       54 | 30.45%     | ok               |
|          40 | 19.36%   | 17.29%             | -7.32% |     0.95 |       64 | 35.61%     | ok               |
|          35 | 17.89%   | 17.29%             | -8.39% |     0.87 |       62 | 38.44%     | ok               |
|          30 | 14.47%   | 17.29%             | -8.96% |     0.71 |       63 | 40.27%     | ok               |

## XLU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 5.59%    | 25.30%             | -14.03% |     0.32 |       56 | 29.62%     | ok               |
|          45 | 4.43%    | 25.30%             | -14.97% |     0.26 |       60 | 30.78%     | ok               |
|          35 | 4.35%    | 25.30%             | -19.71% |     0.24 |       64 | 36.77%     | ok               |
|          40 | 1.89%    | 25.30%             | -16.41% |     0.13 |       70 | 33.44%     | ok               |
|          30 | -0.17%   | 25.30%             | -20.40% |     0.04 |       69 | 40.27%     | ok               |

## XLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -17.24%  | 29.02%             | -22.46% |    -0.74 |       74 | 38.60%     | ok               |
|          30 | -17.62%  | 29.02%             | -22.82% |    -0.77 |       74 | 36.94%     | ok               |
|          15 | -20.04%  | 29.02%             | -24.77% |    -0.85 |       81 | 42.60%     | ok               |
|          20 | -19.87%  | 29.02%             | -24.61% |    -0.86 |       77 | 40.10%     | ok               |
|          35 | -21.72%  | 29.02%             | -26.64% |    -1.03 |       68 | 33.94%     | ok               |

## XLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 1.76%    | 33.70%             | -16.52% |     0.13 |       78 | 54.41%     | ok               |
|          30 | -1.78%   | 33.70%             | -18.44% |     0.02 |       77 | 47.75%     | ok               |
|          20 | -3.63%   | 33.70%             | -20.14% |    -0.02 |       74 | 51.08%     | ok               |
|          25 | -5.78%   | 33.70%             | -21.01% |    -0.09 |       71 | 49.58%     | ok               |
|          50 | -4.95%   | 33.70%             | -17.00% |    -0.14 |       66 | 32.45%     | ok               |

## XOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 3.48%    | 47.19%             | -21.35% |     0.17 |       40 | 29.28%     | ok               |
|          25 | 3.49%    | 47.19%             | -19.90% |     0.17 |       55 | 36.94%     | ok               |
|          30 | 2.46%    | 47.19%             | -20.29% |     0.14 |       55 | 36.27%     | ok               |
|          45 | -1.68%   | 47.19%             | -23.33% |     0.03 |       44 | 30.45%     | ok               |
|          40 | -3.14%   | 47.19%             | -21.45% |    -0.01 |       54 | 33.78%     | ok               |

## XRP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 1.88%    | -53.25%            | -34.36% |     0.22 |       82 | 43.49%     | ok               |
|          40 | -5.56%   | -53.25%            | -33.91% |     0.11 |       74 | 35.63%     | ok               |
|          30 | -13.81%  | -53.25%            | -34.78% |     0.02 |       73 | 49.04%     | ok               |
|          45 | -12.26%  | -53.25%            | -36.27% |     0.01 |       66 | 29.50%     | ok               |
|          20 | -19.40%  | -53.25%            | -38.46% |    -0.04 |       76 | 55.75%     | ok               |

## YFI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -42.67%  | -62.63%            | -44.76% |    -0.67 |       60 | 27.78%     | ok               |
|          35 | -46.91%  | -62.63%            | -52.87% |    -0.71 |       62 | 35.82%     | ok               |
|          30 | -51.63%  | -62.63%            | -58.28% |    -0.8  |       74 | 39.66%     | ok               |
|          25 | -54.43%  | -62.63%            | -60.71% |    -0.84 |       73 | 44.06%     | ok               |
|          15 | -63.56%  | -62.63%            | -67.95% |    -1.03 |       83 | 52.30%     | ok               |

## ZEC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 222.23%  | 1991.63%           | -30.64% |     1.13 |       44 | 28.93%     | ok               |
|          35 | 162.09%  | 1991.63%           | -50.84% |     0.97 |       52 | 34.10%     | ok               |
|          50 | 146.25%  | 1991.63%           | -41.34% |     0.95 |       44 | 26.05%     | ok               |
|          40 | 138.59%  | 1991.63%           | -54.22% |     0.91 |       52 | 32.38%     | ok               |
|          30 | 126.43%  | 1991.63%           | -56.50% |     0.87 |       54 | 36.97%     | ok               |
