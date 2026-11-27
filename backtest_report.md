# Market Tracker Backtest Report

_Generated: 2026-11-27T08:12:15+00:00_

## Data Sources

- Crypto: Kraken -> Coinbase -> CoinGecko OHLC -> CoinPaprika fallback chain.
- Stocks / ETFs / indices: Stooq -> Yahoo Finance fallback chain.
- Data rows are generated from real market APIs. Mock OHLCV rows are not generated.

## Data Freshness

- Rows: **92,814**
- Symbols: **161**
- Date range: **2024-07-08** to **2026-11-27**

## Latest Signals

| symbol     | date                |         close |   composite_score | signal   | data_source   |
|:-----------|:--------------------|--------------:|------------------:|:---------|:--------------|
| AMGN       | 2026-11-25 00:00:00 |   469.24      |          55.75    | LONG     | Yahoo Finance |
| CMCSA      | 2026-11-25 00:00:00 |    25.73      |          53.1667  | LONG     | Yahoo Finance |
| COST       | 2026-11-25 00:00:00 |  1086.81      |          38.0833  | LONG     | Yahoo Finance |
| DIS        | 2026-11-25 00:00:00 |   125.6       |          80.9167  | LONG     | Yahoo Finance |
| DXY-INDEX  | 2026-11-27 00:00:00 |   103.718     |          80.3763  | LONG     | Yahoo Finance |
| HD         | 2026-11-25 00:00:00 |   361.26      |          56.25    | LONG     | Yahoo Finance |
| LLY        | 2026-11-25 00:00:00 |  1392.22      |          50.25    | LONG     | Yahoo Finance |
| MCD        | 2026-11-25 00:00:00 |   283.5       |          42       | LONG     | Yahoo Finance |
| PG         | 2026-11-25 00:00:00 |   173.23      |          61.0833  | LONG     | Yahoo Finance |
| SBUX       | 2026-11-25 00:00:00 |   107.74      |          30.75    | LONG     | Yahoo Finance |
| TGT        | 2026-11-25 00:00:00 |   172.22      |          76.5833  | LONG     | Yahoo Finance |
| TLT        | 2026-11-25 00:00:00 |    82.24      |          32.3333  | LONG     | Yahoo Finance |
| TMUS       | 2026-11-25 00:00:00 |   166.25      |          32.75    | LONG     | Yahoo Finance |
| UPS        | 2026-11-25 00:00:00 |   111.47      |          30.25    | LONG     | Yahoo Finance |
| VIXY       | 2026-11-25 00:00:00 |    23.28      |          52.0833  | LONG     | Yahoo Finance |
| WMT        | 2026-11-25 00:00:00 |   131.94      |          43.5833  | LONG     | Yahoo Finance |
| XLU        | 2026-11-25 00:00:00 |    43.61      |          38       | LONG     | Yahoo Finance |
| XLV        | 2026-11-25 00:00:00 |   183.68      |          40.0833  | LONG     | Yahoo Finance |
| XLY        | 2026-11-25 00:00:00 |   117.49      |          38.0833  | LONG     | Yahoo Finance |
| AAPL       | 2026-11-25 00:00:00 |   355.58      |          42       | NEUTRAL  | Yahoo Finance |
| ABBV       | 2026-11-25 00:00:00 |   294.48      |          47.5     | NEUTRAL  | Yahoo Finance |
| ADA-USD    | 2026-11-27 00:00:00 |     0.152975  |         -18.5     | NEUTRAL  | Kraken API    |
| ADBE       | 2026-11-25 00:00:00 |   232.83      |         -39.0833  | NEUTRAL  | Yahoo Finance |
| AGG        | 2026-11-25 00:00:00 |    96.55      |          14.4167  | NEUTRAL  | Yahoo Finance |
| ALGO-USD   | 2026-11-27 00:00:00 |     0.0822    |          -8       | NEUTRAL  | Kraken API    |
| AMD        | 2026-11-25 00:00:00 |   406.03      |         -48.0833  | NEUTRAL  | Yahoo Finance |
| AMZN       | 2026-11-25 00:00:00 |   244.43      |         -43.25    | NEUTRAL  | Yahoo Finance |
| ATOM-USD   | 2026-11-27 00:00:00 |     1.2405    |         -18.6667  | NEUTRAL  | Kraken API    |
| AVGO       | 2026-11-25 00:00:00 |   300.86      |         -56.8333  | NEUTRAL  | Yahoo Finance |
| BAC        | 2026-11-25 00:00:00 |    48.54      |         -44.1667  | NEUTRAL  | Yahoo Finance |
| BCH-USD    | 2026-11-27 00:00:00 |   213.32      |         -13.25    | NEUTRAL  | Kraken API    |
| BLK        | 2026-11-25 00:00:00 |  1141.86      |          18.0833  | NEUTRAL  | Yahoo Finance |
| BND        | 2026-11-25 00:00:00 |    71.6       |          14.4167  | NEUTRAL  | Yahoo Finance |
| C          | 2026-11-25 00:00:00 |   113.33      |         -64       | NEUTRAL  | Yahoo Finance |
| CL         | 2026-11-25 00:00:00 |    99.66      |          35.3333  | NEUTRAL  | Yahoo Finance |
| COMP-USD   | 2026-11-27 00:00:00 |    18.15      |         -15       | NEUTRAL  | Kraken API    |
| COP        | 2026-11-25 00:00:00 |   135.02      |         -26.5833  | NEUTRAL  | Yahoo Finance |
| CVX        | 2026-11-25 00:00:00 |   210.95      |         -26.0833  | NEUTRAL  | Yahoo Finance |
| DASH-USD   | 2026-11-27 00:00:00 |    36.555     |         -19       | NEUTRAL  | Kraken API    |
| DE         | 2026-11-25 00:00:00 |   641.02      |         -29.0833  | NEUTRAL  | Yahoo Finance |
| DIA        | 2026-11-25 00:00:00 |   501.27      |         -59.5833  | NEUTRAL  | Yahoo Finance |
| DOGE-USD   | 2026-11-27 00:00:00 |     0.0581104 |         -18.5     | NEUTRAL  | Kraken API    |
| DOT-USD    | 2026-11-27 00:00:00 |     0.6842    |         -20.0833  | NEUTRAL  | Kraken API    |
| EFA        | 2026-11-25 00:00:00 |    99.18      |         -59.5833  | NEUTRAL  | Yahoo Finance |
| EOG        | 2026-11-25 00:00:00 |   148.31      |          -6.66667 | NEUTRAL  | Yahoo Finance |
| ETC-USD    | 2026-11-27 00:00:00 |     5.996     |         -17.5     | NEUTRAL  | Kraken API    |
| ETH-USD    | 2026-11-27 00:00:00 |  1732.19      |         -15.25    | NEUTRAL  | Kraken API    |
| FET-USD    | 2026-11-27 00:00:00 |     0.1249    |         -26.3333  | NEUTRAL  | Kraken API    |
| FIL-USD    | 2026-11-27 00:00:00 |     0.548     |         -29.6667  | NEUTRAL  | Kraken API    |
| GDX        | 2026-11-25 00:00:00 |    73.89      |         -72.25    | NEUTRAL  | Yahoo Finance |
| GDXJ       | 2026-11-25 00:00:00 |    87.66      |         -70.5     | NEUTRAL  | Yahoo Finance |
| GOOGL      | 2026-11-25 00:00:00 |   273.1       |         -46.6667  | NEUTRAL  | Yahoo Finance |
| GRT-USD    | 2026-11-27 00:00:00 |     0.01686   |         -17       | NEUTRAL  | Kraken API    |
| GS         | 2026-11-25 00:00:00 |   801.03      |         -62.8333  | NEUTRAL  | Yahoo Finance |
| HBAR-USD   | 2026-11-27 00:00:00 |     0.0555    |         -18.5     | NEUTRAL  | Kraken API    |
| HON        | 2026-11-25 00:00:00 |   225.1       |          26.0833  | NEUTRAL  | Yahoo Finance |
| HYG        | 2026-11-25 00:00:00 |    76.52      |         -58.5     | NEUTRAL  | Yahoo Finance |
| IBM        | 2026-11-25 00:00:00 |   243.47      |           8.41667 | NEUTRAL  | Yahoo Finance |
| ICP-USD    | 2026-11-27 00:00:00 |     2.033     |         -63.25    | NEUTRAL  | Kraken API    |
| IEF        | 2026-11-25 00:00:00 |    92.06      |          21.0833  | NEUTRAL  | Yahoo Finance |
| INJ-USD    | 2026-11-27 00:00:00 |     6.434     |         -30.3333  | NEUTRAL  | Kraken API    |
| ITA        | 2026-11-25 00:00:00 |    68.77      |         -50.3333  | NEUTRAL  | Yahoo Finance |
| IWM        | 2026-11-25 00:00:00 |   268.87      |         -57.0833  | NEUTRAL  | Yahoo Finance |
| JNJ        | 2026-11-25 00:00:00 |   273.94      |          26.75    | NEUTRAL  | Yahoo Finance |
| KO         | 2026-11-25 00:00:00 |    97.59      |          40.6667  | NEUTRAL  | Yahoo Finance |
| LIN        | 2026-11-25 00:00:00 |   524.61      |          21.5     | NEUTRAL  | Yahoo Finance |
| LINK-USD   | 2026-11-27 00:00:00 |     9.58835   |           3       | NEUTRAL  | Kraken API    |
| LTC-USD    | 2026-11-27 00:00:00 |    44.38      |         -15.5     | NEUTRAL  | Kraken API    |
| META       | 2026-11-25 00:00:00 |   609.89      |         -19.4167  | NEUTRAL  | Yahoo Finance |
| MPC        | 2026-11-25 00:00:00 |   346.27      |          -9.33333 | NEUTRAL  | Yahoo Finance |
| MRK        | 2026-11-25 00:00:00 |   140.29      |         -24.8333  | NEUTRAL  | Yahoo Finance |
| MS         | 2026-11-25 00:00:00 |   167.55      |         -64.5     | NEUTRAL  | Yahoo Finance |
| MSFT       | 2026-11-25 00:00:00 |   489.93      |         -31.8333  | NEUTRAL  | Yahoo Finance |
| NEAR-USD   | 2026-11-27 00:00:00 |     3.0843    |           4       | NEUTRAL  | Kraken API    |
| NEM        | 2026-11-25 00:00:00 |   101.44      |         -71       | NEUTRAL  | Yahoo Finance |
| NFLX       | 2026-11-25 00:00:00 |    59.41      |         -65.3333  | NEUTRAL  | Yahoo Finance |
| NKE        | 2026-11-25 00:00:00 |    36.66      |         -24.3333  | NEUTRAL  | Yahoo Finance |
| NOW        | 2026-11-25 00:00:00 |    92.16      |         -15.25    | NEUTRAL  | Yahoo Finance |
| ORCL       | 2026-11-25 00:00:00 |   103.88      |         -59       | NEUTRAL  | Yahoo Finance |
| PEP        | 2026-11-25 00:00:00 |   143.93      |          21.0833  | NEUTRAL  | Yahoo Finance |
| PFE        | 2026-11-25 00:00:00 |    28.46      |         -24.8333  | NEUTRAL  | Yahoo Finance |
| POL-USD    | 2026-11-27 00:00:00 |     0.07839   |         -26       | NEUTRAL  | Kraken API    |
| QCOM       | 2026-11-25 00:00:00 |   168.66      |         -11.1667  | NEUTRAL  | Yahoo Finance |
| RTX        | 2026-11-25 00:00:00 |   196.19      |          31.75    | NEUTRAL  | Yahoo Finance |
| SCHW       | 2026-11-25 00:00:00 |    93.45      |           9.33333 | NEUTRAL  | Yahoo Finance |
| SHY        | 2026-11-25 00:00:00 |    81.64      |          14.4167  | NEUTRAL  | Yahoo Finance |
| SKY-USD    | 2026-11-27 00:00:00 |     0.04687   |         -26.75    | NEUTRAL  | Kraken API    |
| SNX-USD    | 2026-11-27 00:00:00 |     0.146     |         -26.4167  | NEUTRAL  | Kraken API    |
| SOL-USD    | 2026-11-27 00:00:00 |    73.19      |         -18.5     | NEUTRAL  | Kraken API    |
| SPY        | 2026-11-25 00:00:00 |   716.7       |         -46.75    | NEUTRAL  | Yahoo Finance |
| SUSHI-USD  | 2026-11-27 00:00:00 |     0.1552    |         -19       | NEUTRAL  | Kraken API    |
| T          | 2026-11-25 00:00:00 |    22.97      |          21.1667  | NEUTRAL  | Yahoo Finance |
| TIA-USD    | 2026-11-27 00:00:00 |     0.3458    |         -19       | NEUTRAL  | Kraken API    |
| TMO        | 2026-11-25 00:00:00 |   685.52      |           7.33333 | NEUTRAL  | Yahoo Finance |
| TSLA       | 2026-11-25 00:00:00 |   380.14      |          11.8333  | NEUTRAL  | Yahoo Finance |
| TXN        | 2026-11-25 00:00:00 |   270.19      |         -41.0833  | NEUTRAL  | Yahoo Finance |
| USO        | 2026-11-25 00:00:00 |   139.89      |         -26.0833  | NEUTRAL  | Yahoo Finance |
| VEA        | 2026-11-25 00:00:00 |    65.67      |         -63.3333  | NEUTRAL  | Yahoo Finance |
| VNQ        | 2026-11-25 00:00:00 |    95.66      |          29.8333  | NEUTRAL  | Yahoo Finance |
| VZ         | 2026-11-25 00:00:00 |    47.28      |          55.9167  | NEUTRAL  | Yahoo Finance |
| WFC        | 2026-11-25 00:00:00 |    80.94      |         -27.8333  | NEUTRAL  | Yahoo Finance |
| WIF-USD    | 2026-11-27 00:00:00 |     0.1375    |         -13.75    | NEUTRAL  | Kraken API    |
| XBI        | 2026-11-25 00:00:00 |   156.6       |          29.1667  | NEUTRAL  | Yahoo Finance |
| XLB        | 2026-11-25 00:00:00 |    51.21      |          17.6667  | NEUTRAL  | Yahoo Finance |
| XLC        | 2026-11-25 00:00:00 |   105.38      |         -16       | NEUTRAL  | Yahoo Finance |
| XLE        | 2026-11-25 00:00:00 |    60.9       |         -22.8333  | NEUTRAL  | Yahoo Finance |
| XLF        | 2026-11-25 00:00:00 |    56.51      |          15.4167  | NEUTRAL  | Yahoo Finance |
| XLI        | 2026-11-25 00:00:00 |   162.95      |         -50.3333  | NEUTRAL  | Yahoo Finance |
| XLP        | 2026-11-25 00:00:00 |    92.3       |          28.5     | NEUTRAL  | Yahoo Finance |
| XOM        | 2026-11-25 00:00:00 |   158.08      |         -24.8333  | NEUTRAL  | Yahoo Finance |
| XRP-USD    | 2026-11-27 00:00:00 |     0.97539   |         -13       | NEUTRAL  | Kraken API    |
| ZEC-USD    | 2026-11-27 00:00:00 |   741         |         -43.5833  | NEUTRAL  | Kraken API    |
| AAVE-USD   | 2026-11-27 00:00:00 |    96.04      |         -50.3333  | SHORT    | Kraken API    |
| AMAT       | 2026-11-25 00:00:00 |   311.18      |         -56.75    | SHORT    | Yahoo Finance |
| APT-USD    | 2026-11-27 00:00:00 |     0.3911    |         -38.6667  | SHORT    | Kraken API    |
| ARB-USD    | 2026-11-27 00:00:00 |     0.1173    |         -53.1667  | SHORT    | Kraken API    |
| ARKK       | 2026-11-25 00:00:00 |    67.36      |         -43.25    | SHORT    | Yahoo Finance |
| AVAX-USD   | 2026-11-27 00:00:00 |     6.748     |         -35.8333  | SHORT    | Kraken API    |
| BA         | 2026-11-25 00:00:00 |   164.53      |         -32.9167  | SHORT    | Yahoo Finance |
| BITO       | 2026-11-25 00:00:00 |    16         |         -47.5833  | SHORT    | Yahoo Finance |
| BONK-USD   | 2026-11-27 00:00:00 |     2.188e-06 |         -37       | SHORT    | Kraken API    |
| BTC-USD    | 2026-11-27 00:00:00 | 61577.6       |         -27.5     | SHORT    | Kraken API    |
| CAT        | 2026-11-25 00:00:00 |   543.69      |         -33.25    | SHORT    | Yahoo Finance |
| CRM        | 2026-11-25 00:00:00 |   197.21      |         -33.8333  | SHORT    | Yahoo Finance |
| CRV-USD    | 2026-11-27 00:00:00 |     0.17829   |         -31.3333  | SHORT    | Kraken API    |
| CSCO       | 2026-11-25 00:00:00 |    94.2       |         -46.5833  | SHORT    | Yahoo Finance |
| DBC        | 2026-11-25 00:00:00 |    29.27      |         -54.9167  | SHORT    | Yahoo Finance |
| EEM        | 2026-11-25 00:00:00 |    56.4       |         -52.75    | SHORT    | Yahoo Finance |
| EWJ        | 2026-11-25 00:00:00 |    87.25      |         -49.0833  | SHORT    | Yahoo Finance |
| FCX        | 2026-11-25 00:00:00 |    48.55      |         -54.25    | SHORT    | Yahoo Finance |
| FXI        | 2026-11-25 00:00:00 |    31.3       |         -59.0833  | SHORT    | Yahoo Finance |
| GE         | 2026-11-25 00:00:00 |   316.98      |         -31.1667  | SHORT    | Yahoo Finance |
| GLD        | 2026-11-25 00:00:00 |   327.45      |         -62.8333  | SHORT    | Yahoo Finance |
| IBIT       | 2026-11-25 00:00:00 |    34.07      |         -47.5833  | SHORT    | Yahoo Finance |
| IEMG       | 2026-11-25 00:00:00 |    68.78      |         -52.75    | SHORT    | Yahoo Finance |
| INTC       | 2026-11-25 00:00:00 |    54.47      |         -34.5833  | SHORT    | Yahoo Finance |
| INTU       | 2026-11-25 00:00:00 |   271.72      |         -42.5833  | SHORT    | Yahoo Finance |
| JPM        | 2026-11-25 00:00:00 |   316.74      |         -38.5     | SHORT    | Yahoo Finance |
| LDO-USD    | 2026-11-27 00:00:00 |     0.243     |         -35.8333  | SHORT    | Kraken API    |
| LRCX       | 2026-11-25 00:00:00 |   185.01      |         -55.0833  | SHORT    | Yahoo Finance |
| MU         | 2026-11-25 00:00:00 |   601.25      |         -59.5833  | SHORT    | Yahoo Finance |
| NVDA       | 2026-11-25 00:00:00 |   149.3       |         -59.5833  | SHORT    | Yahoo Finance |
| OP-USD     | 2026-11-27 00:00:00 |     0.0719    |         -34.1667  | SHORT    | Kraken API    |
| OXY        | 2026-11-25 00:00:00 |    53.95      |         -48.5833  | SHORT    | Yahoo Finance |
| PEPE-USD   | 2026-11-27 00:00:00 |     3.604e-06 |         -53.1667  | SHORT    | Kraken API    |
| PM         | 2026-11-25 00:00:00 |   184.32      |         -40.1667  | SHORT    | Yahoo Finance |
| QQQ        | 2026-11-25 00:00:00 |   633.93      |         -51.0833  | SHORT    | Yahoo Finance |
| RENDER-USD | 2026-11-27 00:00:00 |     1.361     |         -32.5     | SHORT    | Kraken API    |
| SHIB-USD   | 2026-11-27 00:00:00 |     3.695e-06 |         -30.8333  | SHORT    | Kraken API    |
| SLB        | 2026-11-25 00:00:00 |    48.52      |         -49.0833  | SHORT    | Yahoo Finance |
| SLV        | 2026-11-25 00:00:00 |    37.1       |         -64.8333  | SHORT    | Yahoo Finance |
| SMH        | 2026-11-25 00:00:00 |   422.46      |         -55.0833  | SHORT    | Yahoo Finance |
| SOXX       | 2026-11-25 00:00:00 |   127.98      |         -59.0833  | SHORT    | Yahoo Finance |
| TRX-USD    | 2026-11-27 00:00:00 |     0.305079  |         -32.1667  | SHORT    | Kraken API    |
| UNH        | 2026-11-25 00:00:00 |   346.19      |         -38.8333  | SHORT    | Yahoo Finance |
| UNI-USD    | 2026-11-27 00:00:00 |     4.8786    |         -31.5     | SHORT    | Kraken API    |
| VTI        | 2026-11-25 00:00:00 |   353.2       |         -47       | SHORT    | Yahoo Finance |
| VWO        | 2026-11-25 00:00:00 |    52.78      |         -52.75    | SHORT    | Yahoo Finance |
| XLK        | 2026-11-25 00:00:00 |   155.79      |         -37.5833  | SHORT    | Yahoo Finance |
| XLM-USD    | 2026-11-27 00:00:00 |     0.129735  |         -35       | SHORT    | Kraken API    |
| YFI-USD    | 2026-11-27 00:00:00 |  1633.2       |         -30.8333  | SHORT    | Kraken API    |

## Edge Summary

- Symbols with trades: **161** of 161
- Beat buy-and-hold: **40.37%** of traded symbols
- Positive return: **32.30%** of traded symbols
- Median strategy return: **-7.08%** (benchmark **16.18%**)
- Median excess vs benchmark: **-20.18%**
- Median Sharpe: **-0.06**
- Median exposure: **44.83%**

> Edge is real only if both _beat buy-and-hold_ and _median excess_ are convincingly positive across many symbols. Treat a single high-return symbol as noise.

## Portfolio Backtest

Actual capital-allocation books (not per-symbol averages). Benchmarks: `equal_weight_buyhold` (whole tracked universe), `spy_buyhold` (100% SPY), and `sixty_forty` (60% SPY / 40% AGG). `high_conf_voltarget` inverse-vol-weights the HIGH-confidence book; `conviction_long_short` is market-neutral. Judge on **Sharpe** and **max_drawdown** out-of-sample, not raw return: a fully-invested long book wins on return in a bull market but carries all the risk.

| strategy              | scope         | ann_return   | ann_vol   |   sharpe | max_drawdown   | total_return   |   avg_gross_exposure |
|:----------------------|:--------------|:-------------|:----------|---------:|:---------------|:---------------|---------------------:|
| equal_weight_buyhold  | full          | 3.53%        | 27.92%    |     0.13 | -39.53%        | -1.14%         |                 1    |
| equal_weight_buyhold  | out_of_sample | 17.05%       | 26.29%    |     0.65 | -24.61%        | 15.57%         |                 1    |
| all_signals_ew        | full          | -10.37%      | 23.60%    |    -0.44 | -50.49%        | -32.94%        |                 1    |
| all_signals_ew        | out_of_sample | -2.08%       | 21.94%    |    -0.1  | -22.66%        | -4.66%         |                 1    |
| high_conf_ew          | full          | -8.19%       | 29.47%    |    -0.28 | -45.07%        | -31.55%        |                 0.89 |
| high_conf_ew          | out_of_sample | 8.31%        | 25.44%    |     0.33 | -27.61%        | 5.55%          |                 0.89 |
| high_conf_voltarget   | full          | -11.04%      | 26.11%    |    -0.42 | -40.80%        | -35.41%        |                 0.89 |
| high_conf_voltarget   | out_of_sample | 0.64%        | 20.26%    |     0.03 | -23.45%        | -1.51%         |                 0.89 |
| conviction_long_short | full          | -15.22%      | 21.67%    |    -0.7  | -51.23%        | -41.36%        |                 0.96 |
| conviction_long_short | out_of_sample | -2.82%       | 17.42%    |    -0.16 | -22.70%        | -4.50%         |                 0.96 |
| spy_buyhold           | full          | -0.06%       | 14.23%    |    -0    | -19.00%        | -3.18%         |                 0.79 |
| spy_buyhold           | out_of_sample | -10.25%      | 11.53%    |    -0.89 | -15.61%        | -10.97%        |                 0.79 |
| sixty_forty           | full          | -0.45%       | 8.89%     |    -0.05 | -11.86%        | -2.51%         |                 0.79 |
| sixty_forty           | out_of_sample | -8.02%       | 7.48%     |    -1.07 | -10.28%        | -8.45%         |                 0.79 |

## Walk-Forward Robustness

Each book measured across contiguous time folds (each a different regime). A book has durable edge only if `mean_sharpe` is positive, `min_sharpe` isn't deeply negative, and `pct_positive_folds` is high — a single great fold doesn't count. `fold_sharpes` lists each fold oldest-to-newest.

| strategy              |   n_folds |   mean_sharpe |   median_sharpe |   min_sharpe | pct_positive_folds   | mean_return   | fold_sharpes                 |
|:----------------------|----------:|--------------:|----------------:|-------------:|:---------------------|:--------------|:-----------------------------|
| equal_weight_buyhold  |         5 |          0.32 |            0.39 |        -0.54 | 60.00%               | 0.26%         | 1.33;0.65;-0.54;-0.22;0.39   |
| all_signals_ew        |         5 |         -0.56 |           -0.72 |        -1.64 | 40.00%               | -7.07%        | -1.64;-0.72;-1.30;0.54;0.32  |
| high_conf_ew          |         5 |         -0.19 |            0.03 |        -2.3  | 60.00%               | -5.86%        | 1.00;-2.30;0.03;0.62;-0.28   |
| high_conf_voltarget   |         5 |         -0.41 |            0.12 |        -2.6  | 60.00%               | -7.32%        | 1.09;-2.60;0.12;0.23;-0.87   |
| conviction_long_short |         5 |         -0.68 |           -0.49 |        -2.4  | 20.00%               | -9.50%        | -2.40;-0.49;-0.89;-0.34;0.73 |
| spy_buyhold           |         5 |         -0.12 |           -0.14 |        -1.56 | 40.00%               | -0.43%        | 1.17;0.26;-0.14;-0.35;-1.56  |
| sixty_forty           |         5 |         -0.18 |           -0.07 |        -1.75 | 40.00%               | -0.41%        | 1.08;0.31;-0.07;-0.48;-1.75  |

## Strategy Comparison

Each decision rule backtested over the same data. `out_of_sample` is the most recent ~35% of each symbol's history (unseen tail). A rule has real edge only if `median_excess` and `beat_benchmark_pct` stay positive out-of-sample, not just full-sample.

| strategy        | scope         |   symbols | beat_benchmark_pct   | positive_pct   | median_return   | median_benchmark   | median_excess   |   median_sharpe |   total_trades |
|:----------------|:--------------|----------:|:---------------------|:---------------|:----------------|:-------------------|:----------------|----------------:|---------------:|
| trend           | full          |       161 | 40.37%               | 32.30%         | -7.08%          | 16.18%             | -20.18%         |           -0.06 |          11374 |
| trend           | out_of_sample |       161 | 52.17%               | 52.17%         | 0.46%           | -3.74%             | 2.20%           |            0.16 |           3887 |
| mean_reversion  | full          |       159 | 40.25%               | 47.80%         | -0.23%          | 16.18%             | -15.09%         |           -0.02 |           1298 |
| mean_reversion  | out_of_sample |       132 | 61.36%               | 58.33%         | 0.38%           | -3.87%             | 3.53%           |            0.52 |            446 |
| regime_adaptive | full          |       161 | 40.37%               | 32.30%         | -7.38%          | 16.18%             | -20.59%         |           -0.05 |          11644 |
| regime_adaptive | out_of_sample |       161 | 52.80%               | 52.80%         | 0.61%           | -3.74%             | 2.53%           |            0.18 |           3996 |

## Signal Calibration

Realized forward return in the signal's direction, grouped by confidence. HIGH should outrank LOW for the confidence score to be meaningful.

| confidence_level   |   horizon |     n | mean_return   | median_return   | win_rate   |
|:-------------------|----------:|------:|:--------------|:----------------|:-----------|
| HIGH               |         5 |  7642 | 0.19%         | 0.06%           | 51.06%     |
| MEDIUM             |         5 | 29611 | 0.14%         | 0.07%           | 50.85%     |
| LOW                |         5 |  3729 | -0.15%        | -0.24%          | 47.68%     |
| ALL                |         5 | 40982 | 0.13%         | 0.05%           | 50.60%     |
| HIGH               |        10 |  7578 | 0.50%         | 0.09%           | 51.07%     |
| MEDIUM             |        10 | 29230 | 0.36%         | 0.11%           | 50.90%     |
| LOW                |        10 |  3693 | -0.25%        | -0.21%          | 48.42%     |
| ALL                |        10 | 40501 | 0.33%         | 0.08%           | 50.71%     |
| HIGH               |        20 |  7366 | 1.15%         | 0.28%           | 52.23%     |
| MEDIUM             |        20 | 28548 | 0.96%         | 0.54%           | 52.99%     |
| LOW                |        20 |  3614 | 0.07%         | -0.30%          | 48.56%     |
| ALL                |        20 | 39528 | 0.91%         | 0.43%           | 52.44%     |

## Backtest Summary

### Data Quality / Signal Availability

- **ok**: 161 symbols

| symbol     |   trades | return   | benchmark_return   | mdd     |   sharpe | exposure   | skipped_reason   |
|:-----------|---------:|:---------|:-------------------|:--------|---------:|:-----------|:-----------------|
| AAPL       |       67 | -13.44%  | 56.08%             | -20.65% |    -0.19 | 46.76%     | ok               |
| AAVE-USD   |       75 | -46.08%  | -63.55%            | -68.22% |    -0.36 | 42.15%     | ok               |
| ABBV       |       66 | -13.91%  | 76.84%             | -30.52% |    -0.24 | 49.42%     | ok               |
| ADA-USD    |       72 | -6.23%   | -73.97%            | -52.70% |     0.15 | 49.62%     | ok               |
| ADBE       |       74 | -2.85%   | -59.54%            | -31.20% |     0.09 | 53.58%     | ok               |
| AGG        |       65 | -7.17%   | -1.09%             | -10.37% |    -1.08 | 35.44%     | ok               |
| ALGO-USD   |       80 | -27.79%  | -55.01%            | -48.16% |    -0.15 | 39.85%     | ok               |
| AMAT       |       73 | -35.08%  | 26.35%             | -57.08% |    -0.23 | 51.25%     | ok               |
| AMD        |       54 | 23.48%   | 127.23%            | -38.64% |     0.42 | 36.44%     | ok               |
| AMGN       |       67 | -9.55%   | 50.66%             | -34.19% |    -0.11 | 52.91%     | ok               |
| AMZN       |       84 | -59.46%  | 22.65%             | -59.55% |    -1.76 | 40.27%     | ok               |
| APT-USD    |       76 | -11.99%  | -92.12%            | -56.73% |     0.13 | 41.38%     | ok               |
| ARB-USD    |       75 | 15.74%   | -62.63%            | -44.51% |     0.4  | 43.68%     | ok               |
| ARKK       |       89 | -23.61%  | 46.79%             | -38.67% |    -0.28 | 45.59%     | ok               |
| ATOM-USD   |       78 | -59.81%  | -69.56%            | -65.09% |    -0.94 | 44.44%     | ok               |
| AVAX-USD   |       66 | -34.13%  | -62.96%            | -48.46% |    -0.29 | 39.85%     | ok               |
| AVGO       |       68 | -14.88%  | 72.33%             | -44.82% |    -0.02 | 38.77%     | ok               |
| BA         |       63 | 22.43%   | -11.47%            | -24.47% |     0.46 | 53.91%     | ok               |
| BAC        |       78 | -6.49%   | 19.50%             | -22.37% |    -0.1  | 48.92%     | ok               |
| BCH-USD    |       80 | -3.78%   | -52.98%            | -54.04% |     0.17 | 50.00%     | ok               |
| BITO       |       83 | -18.50%  | -59.53%            | -42.14% |    -0.08 | 41.76%     | ok               |
| BLK        |       77 | -6.99%   | 44.50%             | -26.90% |    -0.11 | 46.42%     | ok               |
| BND        |       68 | -7.27%   | -1.10%             | -10.43% |    -1.09 | 36.44%     | ok               |
| BONK-USD   |       72 | 51.20%   | -84.60%            | -53.32% |     0.63 | 44.64%     | ok               |
| BTC-USD    |       75 | 9.23%    | -41.96%            | -25.52% |     0.29 | 53.83%     | ok               |
| C          |       79 | -37.30%  | 75.05%             | -39.84% |    -0.83 | 46.59%     | ok               |
| CAT        |       66 | 39.33%   | 65.23%             | -21.87% |     0.63 | 52.08%     | ok               |
| CL         |       60 | 7.34%    | 2.13%              | -14.32% |     0.28 | 40.27%     | ok               |
| CMCSA      |       88 | -34.64%  | -26.46%            | -45.76% |    -0.81 | 45.09%     | ok               |
| COMP-USD   |       91 | -37.88%  | -60.88%            | -52.17% |    -0.26 | 49.62%     | ok               |
| COP        |       68 | -13.48%  | 20.31%             | -37.99% |    -0.15 | 44.26%     | ok               |
| COST       |       58 | 2.79%    | 23.38%             | -31.32% |     0.15 | 41.43%     | ok               |
| CRM        |       67 | -22.78%  | -23.37%            | -38.02% |    -0.24 | 47.09%     | ok               |
| CRV-USD    |       66 | 84.89%   | -68.71%            | -46.63% |     0.84 | 38.51%     | ok               |
| CSCO       |       67 | 1.79%    | 104.52%            | -29.59% |     0.15 | 52.08%     | ok               |
| CVX        |       71 | -14.92%  | 36.69%             | -26.75% |    -0.31 | 44.26%     | ok               |
| DASH-USD   |       59 | -5.75%   | 82.12%             | -64.43% |     0.35 | 29.12%     | ok               |
| DBC        |       70 | -7.71%   | 24.77%             | -24.10% |    -0.19 | 37.10%     | ok               |
| DE         |       76 | -12.44%  | 80.57%             | -21.16% |    -0.17 | 44.93%     | ok               |
| DIA        |       74 | -9.14%   | 27.40%             | -16.20% |    -0.46 | 42.60%     | ok               |
| DIS        |       62 | 6.38%    | 28.99%             | -27.81% |     0.23 | 47.92%     | ok               |
| DOGE-USD   |       70 | -21.90%  | -64.95%            | -65.42% |    -0.05 | 47.32%     | ok               |
| DOT-USD    |       76 | -56.80%  | -80.12%            | -68.61% |    -0.61 | 41.00%     | ok               |
| DXY-INDEX  |       40 | -0.53%   | -3.85%             | -5.13%  |    -0.08 | 31.75%     | ok               |
| EEM        |       68 | -2.66%   | 29.24%             | -22.68% |     0    | 42.60%     | ok               |
| EFA        |       64 | -9.07%   | 24.46%             | -12.63% |    -0.35 | 38.94%     | ok               |
| EOG        |       77 | -31.84%  | 18.05%             | -48.55% |    -0.68 | 44.09%     | ok               |
| ETC-USD    |       53 | 3.43%    | -63.48%            | -46.78% |     0.22 | 37.36%     | ok               |
| ETH-USD    |       59 | 153.77%  | -29.25%            | -30.11% |     1.32 | 49.23%     | ok               |
| EWJ        |       70 | -23.99%  | 25.32%             | -29.40% |    -0.77 | 39.27%     | ok               |
| FCX        |       67 | -12.40%  | -5.05%             | -46.84% |    -0    | 46.92%     | ok               |
| FET-USD    |       77 | -48.08%  | -81.58%            | -66.52% |    -0.32 | 45.21%     | ok               |
| FIL-USD    |       61 | -6.15%   | -76.15%            | -58.54% |     0.16 | 40.23%     | ok               |
| FXI        |       48 | -1.03%   | 19.33%             | -23.91% |     0.06 | 31.28%     | ok               |
| GDX        |       68 | -4.93%   | 104.68%            | -34.29% |     0.07 | 45.26%     | ok               |
| GDXJ       |       70 | -30.10%  | 94.76%             | -36.01% |    -0.32 | 44.43%     | ok               |
| GE         |       84 | -20.14%  | 93.84%             | -32.12% |    -0.28 | 49.75%     | ok               |
| GLD        |       52 | 11.67%   | 50.08%             | -14.15% |     0.35 | 46.09%     | ok               |
| GOOGL      |       59 | 61.00%   | 44.47%             | -17.54% |     0.97 | 48.92%     | ok               |
| GRT-USD    |       71 | 66.70%   | -79.94%            | -35.55% |     0.76 | 44.25%     | ok               |
| GS         |       68 | -2.77%   | 72.33%             | -21.94% |     0.04 | 47.42%     | ok               |
| HBAR-USD   |       44 | -26.98%  | -46.18%            | -56.47% |    -0.33 | 42.67%     | ok               |
| HD         |       67 | 14.47%   | 6.38%              | -17.15% |     0.41 | 45.59%     | ok               |
| HON        |       87 | -27.34%  | 7.61%              | -32.93% |    -0.69 | 51.25%     | ok               |
| HYG        |       91 | -7.33%   | -1.15%             | -10.59% |    -0.82 | 39.43%     | ok               |
| IBIT       |       46 | 59.91%   | -10.37%            | -18.95% |     0.89 | 36.71%     | ok               |
| IBM        |       73 | -28.31%  | 37.06%             | -50.84% |    -0.36 | 50.42%     | ok               |
| ICP-USD    |       70 | 15.46%   | -59.04%            | -42.66% |     0.4  | 41.76%     | ok               |
| IEF        |       78 | -10.33%  | -2.26%             | -12.21% |    -1.35 | 35.61%     | ok               |
| IEMG       |       64 | -0.79%   | 25.51%             | -24.73% |     0.05 | 42.76%     | ok               |
| INJ-USD    |       56 | -2.07%   | -44.48%            | -56.80% |     0.23 | 38.51%     | ok               |
| INTC       |       72 | 61.10%   | 60.25%             | -60.60% |     0.64 | 51.08%     | ok               |
| INTU       |       77 | -11.71%  | -58.80%            | -38.09% |    -0.05 | 46.59%     | ok               |
| ITA        |       72 | 0.52%    | 54.85%             | -22.33% |     0.09 | 47.09%     | ok               |
| IWM        |       56 | 10.39%   | 32.92%             | -8.62%  |     0.42 | 34.44%     | ok               |
| JNJ        |       62 | 9.85%    | 88.30%             | -17.51% |     0.39 | 48.09%     | ok               |
| JPM        |       79 | -28.75%  | 54.38%             | -32.74% |    -0.85 | 45.09%     | ok               |
| KO         |       54 | 25.09%   | 55.00%             | -8.64%  |     0.85 | 40.43%     | ok               |
| LDO-USD    |       66 | 92.80%   | -66.39%            | -51.13% |     0.84 | 49.43%     | ok               |
| LIN        |       72 | -6.30%   | 20.40%             | -20.61% |    -0.15 | 42.26%     | ok               |
| LINK-USD   |       70 | 25.67%   | -28.50%            | -35.01% |     0.47 | 43.49%     | ok               |
| LLY        |       82 | -36.25%  | 51.66%             | -52.47% |    -0.58 | 49.08%     | ok               |
| LRCX       |       84 | -18.17%  | 67.95%             | -60.21% |     0.02 | 45.09%     | ok               |
| LTC-USD    |       71 | 47.29%   | -47.67%            | -29.27% |     0.67 | 52.11%     | ok               |
| MCD        |       79 | 9.07%    | 14.38%             | -22.20% |     0.36 | 41.76%     | ok               |
| META       |       76 | -41.85%  | 15.22%             | -45.06% |    -0.72 | 49.25%     | ok               |
| MPC        |       70 | 11.57%   | 106.77%            | -33.74% |     0.31 | 53.41%     | ok               |
| MRK        |       67 | -24.79%  | 11.54%             | -35.95% |    -0.48 | 43.59%     | ok               |
| MS         |       69 | -6.30%   | 66.57%             | -27.79% |    -0.06 | 47.25%     | ok               |
| MSFT       |       81 | -30.95%  | 5.08%              | -38.98% |    -0.71 | 49.75%     | ok               |
| MU         |       51 | 113.71%  | 360.06%            | -64.76% |     0.88 | 50.08%     | ok               |
| NEAR-USD   |       67 | 156.41%  | 40.77%             | -47.64% |     1.06 | 44.83%     | ok               |
| NEM        |       70 | -27.00%  | 129.87%            | -39.56% |    -0.27 | 49.42%     | ok               |
| NFLX       |       86 | -9.30%   | -13.36%            | -27.17% |    -0.09 | 49.42%     | ok               |
| NKE        |       89 | -51.13%  | -49.82%            | -55.62% |    -0.94 | 46.92%     | ok               |
| NOW        |       79 | -4.34%   | -39.86%            | -42.66% |     0.16 | 51.75%     | ok               |
| NVDA       |       80 | -30.06%  | 38.24%             | -47.95% |    -0.18 | 55.79%     | ok               |
| OP-USD     |       72 | -9.13%   | -87.05%            | -57.23% |     0.14 | 37.36%     | ok               |
| ORCL       |       60 | 55.85%   | -28.37%            | -31.06% |     0.64 | 49.08%     | ok               |
| OXY        |       63 | 10.08%   | -11.48%            | -28.48% |     0.29 | 43.76%     | ok               |
| PEP        |       72 | 1.75%    | -11.22%            | -21.35% |     0.12 | 46.42%     | ok               |
| PEPE-USD   |       76 | -36.29%  | -64.16%            | -60.19% |    -0.12 | 47.13%     | ok               |
| PFE        |       81 | -38.60%  | 1.90%              | -46.24% |    -1.19 | 37.94%     | ok               |
| PG         |       62 | -15.68%  | 4.03%              | -24.55% |    -0.51 | 38.27%     | ok               |
| PM         |       75 | -6.01%   | 79.67%             | -37.61% |    -0.04 | 47.59%     | ok               |
| POL-USD    |       83 | 5.57%    | -57.47%            | -46.25% |     0.27 | 48.28%     | ok               |
| QCOM       |       77 | -35.78%  | -18.87%            | -50.90% |    -0.37 | 40.10%     | ok               |
| QQQ        |       72 | -3.38%   | 27.46%             | -15.84% |     0    | 42.76%     | ok               |
| RENDER-USD |       88 | -52.22%  | -57.43%            | -59.91% |    -0.45 | 45.40%     | ok               |
| RTX        |       73 | 16.35%   | 95.99%             | -16.99% |     0.43 | 52.91%     | ok               |
| SBUX       |       66 | -13.00%  | 44.48%             | -29.22% |    -0.18 | 40.93%     | ok               |
| SCHW       |       84 | -20.31%  | 27.59%             | -31.92% |    -0.44 | 48.25%     | ok               |
| SHIB-USD   |       81 | -28.78%  | -68.45%            | -55.32% |    -0.23 | 51.34%     | ok               |
| SHY        |       54 | -1.90%   | 0.00%              | -3.30%  |    -0.63 | 38.94%     | ok               |
| SKY-USD    |       89 | -40.33%  | -43.35%            | -65.07% |    -0.41 | 46.36%     | ok               |
| SLB        |       74 | -40.59%  | 4.93%              | -54.27% |    -0.78 | 48.42%     | ok               |
| SLV        |       66 | 60.30%   | 31.89%             | -37.05% |     0.76 | 43.26%     | ok               |
| SMH        |       52 | 57.87%   | 54.06%             | -33.99% |     0.8  | 41.76%     | ok               |
| SNX-USD    |       62 | -8.03%   | -75.21%            | -50.74% |     0.11 | 35.25%     | ok               |
| SOL-USD    |       71 | 5.09%    | -49.86%            | -44.96% |     0.28 | 59.00%     | ok               |
| SOXX       |       57 | 62.79%   | 47.90%             | -40.34% |     0.81 | 41.26%     | ok               |
| SPY        |       63 | -7.08%   | 29.07%             | -15.53% |    -0.19 | 46.09%     | ok               |
| SUSHI-USD  |       87 | -58.93%  | -74.52%            | -78.97% |    -0.64 | 44.64%     | ok               |
| T          |       68 | 52.29%   | 22.12%             | -17.01% |     0.94 | 57.07%     | ok               |
| TGT        |       60 | -2.84%   | 15.80%             | -32.83% |     0.04 | 38.60%     | ok               |
| TIA-USD    |       85 | -43.41%  | -79.49%            | -74.75% |    -0.19 | 44.25%     | ok               |
| TLT        |       70 | -22.94%  | -11.34%            | -23.57% |    -1.73 | 35.44%     | ok               |
| TMO        |       67 | 39.00%   | 27.83%             | -18.85% |     0.74 | 56.07%     | ok               |
| TMUS       |       74 | -7.71%   | -7.21%             | -33.05% |    -0.07 | 45.76%     | ok               |
| TRX-USD    |       60 | 15.38%   | 11.41%             | -22.96% |     0.51 | 50.38%     | ok               |
| TSLA       |       74 | -49.89%  | 50.29%             | -58.36% |    -0.51 | 40.93%     | ok               |
| TXN        |       83 | -30.18%  | 34.11%             | -46.56% |    -0.35 | 48.75%     | ok               |
| UNH        |       72 | 47.68%   | -29.25%            | -26.31% |     0.7  | 48.09%     | ok               |
| UNI-USD    |       80 | 9.96%    | -30.84%            | -61.11% |     0.37 | 51.15%     | ok               |
| UPS        |       71 | -37.94%  | -17.75%            | -41.37% |    -0.74 | 44.59%     | ok               |
| USO        |       70 | -10.76%  | 73.95%             | -42.32% |    -0.02 | 33.61%     | ok               |
| VEA        |       64 | -7.02%   | 30.66%             | -18.84% |    -0.25 | 41.26%     | ok               |
| VIXY       |      104 | -84.51%  | -42.94%            | -91.82% |    -1.13 | 32.45%     | ok               |
| VNQ        |       68 | -13.27%  | 14.18%             | -24.66% |    -0.5  | 40.77%     | ok               |
| VTI        |       69 | -15.48%  | 29.62%             | -18.77% |    -0.53 | 46.09%     | ok               |
| VWO        |       80 | -15.13%  | 18.18%             | -25.20% |    -0.47 | 41.76%     | ok               |
| VZ         |       86 | -27.73%  | 13.85%             | -31.67% |    -0.84 | 43.26%     | ok               |
| WFC        |       80 | -21.76%  | 37.16%             | -30.70% |    -0.39 | 47.09%     | ok               |
| WIF-USD    |       64 | 8.22%    | -84.18%            | -48.32% |     0.34 | 45.21%     | ok               |
| WMT        |       69 | 11.96%   | 89.35%             | -25.96% |     0.38 | 49.25%     | ok               |
| XBI        |       60 | -3.53%   | 67.97%             | -19.01% |    -0.01 | 37.27%     | ok               |
| XLB        |       66 | -11.18%  | 16.18%             | -22.72% |    -0.35 | 35.11%     | ok               |
| XLC        |       63 | -1.20%   | 21.17%             | -12.33% |     0.02 | 47.92%     | ok               |
| XLE        |       72 | -3.75%   | 36.01%             | -34.77% |    -0.01 | 48.42%     | ok               |
| XLF        |       78 | -5.19%   | 36.40%             | -23.61% |    -0.12 | 49.75%     | ok               |
| XLI        |       82 | -11.88%  | 34.26%             | -18.27% |    -0.45 | 42.43%     | ok               |
| XLK        |       46 | 32.92%   | 32.89%             | -19.09% |     0.68 | 43.76%     | ok               |
| XLM-USD    |       75 | 1.26%    | -47.85%            | -56.32% |     0.23 | 50.38%     | ok               |
| XLP        |       65 | 15.23%   | 19.47%             | -8.96%  |     0.73 | 41.93%     | ok               |
| XLU        |       73 | -2.91%   | 27.11%             | -20.40% |    -0.08 | 41.76%     | ok               |
| XLV        |       74 | -20.03%  | 27.33%             | -21.39% |    -0.89 | 37.77%     | ok               |
| XLY        |       83 | -15.52%  | 24.07%             | -22.28% |    -0.41 | 47.25%     | ok               |
| XOM        |       59 | 4.26%    | 40.92%             | -20.29% |     0.19 | 37.44%     | ok               |
| XRP-USD    |       68 | -0.60%   | -55.47%            | -36.92% |     0.18 | 37.36%     | ok               |
| YFI-USD    |       72 | -42.82%  | -68.49%            | -56.38% |    -0.56 | 40.42%     | ok               |
| ZEC-USD    |       54 | 134.89%  | 1635.36%           | -56.50% |     0.89 | 36.02%     | ok               |

## AAPL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -8.02%   | 56.08%             | -21.71% |    -0.05 |       76 | 51.58%     | ok               |
|          15 | -12.09%  | 56.08%             | -23.86% |    -0.13 |       85 | 59.07%     | ok               |
|          30 | -13.44%  | 56.08%             | -20.65% |    -0.19 |       67 | 46.76%     | ok               |
|          35 | -14.68%  | 56.08%             | -22.04% |    -0.23 |       67 | 45.42%     | ok               |
|          25 | -16.94%  | 56.08%             | -22.37% |    -0.26 |       77 | 48.92%     | ok               |

## AAVE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -8.43%   | -63.55%            | -47.84% |     0.13 |       51 | 36.02%     | ok               |
|          50 | -11.76%  | -63.55%            | -47.89% |     0.03 |       46 | 23.37%     | ok               |
|          35 | -17.92%  | -63.55%            | -52.63% |     0.02 |       61 | 40.04%     | ok               |
|          45 | -15.78%  | -63.55%            | -51.44% |     0.01 |       54 | 30.46%     | ok               |
|          15 | -28.95%  | -63.55%            | -58.12% |    -0.03 |       78 | 55.36%     | ok               |

## ABBV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 2.91%    | 76.84%             | -21.96% |     0.16 |       50 | 36.61%     | ok               |
|          20 | -9.78%   | 76.84%             | -28.48% |    -0.13 |       59 | 53.08%     | ok               |
|          25 | -10.20%  | 76.84%             | -30.04% |    -0.14 |       63 | 51.08%     | ok               |
|          30 | -13.91%  | 76.84%             | -30.52% |    -0.24 |       66 | 49.42%     | ok               |
|          40 | -14.56%  | 76.84%             | -27.87% |    -0.28 |       70 | 42.60%     | ok               |

## ADA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 24.88%   | -73.97%            | -46.50% |     0.47 |       68 | 64.18%     | ok               |
|          35 | 10.14%   | -73.97%            | -44.07% |     0.32 |       62 | 43.87%     | ok               |
|          20 | 3.54%    | -73.97%            | -53.45% |     0.3  |       77 | 58.81%     | ok               |
|          40 | -3.88%   | -73.97%            | -41.68% |     0.16 |       60 | 38.89%     | ok               |
|          30 | -6.23%   | -73.97%            | -52.70% |     0.15 |       72 | 49.62%     | ok               |

## ADBE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 13.51%   | -59.54%            | -29.07% |     0.33 |       59 | 58.07%     | ok               |
|          20 | -2.11%   | -59.54%            | -31.52% |     0.12 |       65 | 61.40%     | ok               |
|          30 | -2.85%   | -59.54%            | -31.20% |     0.09 |       74 | 53.58%     | ok               |
|          15 | -9.91%   | -59.54%            | -34.98% |     0    |       67 | 63.56%     | ok               |
|          35 | -10.47%  | -59.54%            | -32.89% |    -0.05 |       77 | 45.26%     | ok               |

## AGG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -7.17%   | -1.09%             | -10.37% |    -1.08 |       65 | 35.44%     | ok               |
|          45 | -6.65%   | -1.09%             | -9.07%  |    -1.2  |       60 | 24.63%     | ok               |
|          20 | -9.39%   | -1.09%             | -11.89% |    -1.32 |       72 | 40.93%     | ok               |
|          35 | -8.38%   | -1.09%             | -11.22% |    -1.32 |       66 | 31.95%     | ok               |
|          25 | -9.16%   | -1.09%             | -12.28% |    -1.33 |       73 | 38.77%     | ok               |

## ALGO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -24.17%  | -55.01%            | -45.13% |    -0.07 |       82 | 44.64%     | ok               |
|          30 | -27.79%  | -55.01%            | -48.16% |    -0.15 |       80 | 39.85%     | ok               |
|          15 | -40.72%  | -55.01%            | -54.19% |    -0.29 |       86 | 53.07%     | ok               |
|          20 | -41.45%  | -55.01%            | -58.45% |    -0.33 |       81 | 47.70%     | ok               |
|          35 | -51.13%  | -55.01%            | -58.39% |    -0.69 |       68 | 34.48%     | ok               |

## AMAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -29.48%  | 26.35%             | -54.01% |    -0.11 |       76 | 60.57%     | ok               |
|          30 | -35.08%  | 26.35%             | -57.08% |    -0.23 |       73 | 51.25%     | ok               |
|          35 | -37.26%  | 26.35%             | -55.13% |    -0.28 |       75 | 48.75%     | ok               |
|          20 | -43.89%  | 26.35%             | -60.13% |    -0.35 |       80 | 56.57%     | ok               |
|          25 | -44.41%  | 26.35%             | -59.69% |    -0.38 |       75 | 54.08%     | ok               |

## AMD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 39.99%   | 127.23%            | -37.12% |     0.56 |       52 | 31.61%     | ok               |
|          40 | 23.48%   | 127.23%            | -38.64% |     0.42 |       54 | 36.44%     | ok               |
|          35 | 13.24%   | 127.23%            | -40.22% |     0.34 |       62 | 37.94%     | ok               |
|          45 | 11.74%   | 127.23%            | -42.84% |     0.32 |       58 | 34.44%     | ok               |
|          30 | -3.80%   | 127.23%            | -47.20% |     0.19 |       65 | 40.60%     | ok               |

## AMGN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 0.93%    | 50.66%             | -26.89% |     0.12 |       64 | 58.40%     | ok               |
|          15 | -8.29%   | 50.66%             | -28.21% |    -0.06 |       63 | 62.73%     | ok               |
|          35 | -7.86%   | 50.66%             | -31.29% |    -0.08 |       69 | 49.42%     | ok               |
|          50 | -5.89%   | 50.66%             | -23.70% |    -0.08 |       52 | 33.44%     | ok               |
|          30 | -9.55%   | 50.66%             | -34.19% |    -0.11 |       67 | 52.91%     | ok               |

## AMZN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -32.71%  | 22.65%             | -33.10% |    -1.04 |       58 | 29.12%     | ok               |
|          50 | -35.37%  | 22.65%             | -35.51% |    -1.32 |       52 | 21.96%     | ok               |
|          45 | -40.23%  | 22.65%             | -40.36% |    -1.47 |       58 | 25.46%     | ok               |
|          35 | -54.68%  | 22.65%             | -54.78% |    -1.65 |       77 | 34.28%     | ok               |
|          30 | -59.46%  | 22.65%             | -59.55% |    -1.76 |       84 | 40.27%     | ok               |

## APT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 72.82%   | -92.12%            | -25.96% |     1.03 |       44 | 18.20%     | ok               |
|          45 | 42.95%   | -92.12%            | -52.49% |     0.65 |       62 | 25.10%     | ok               |
|          20 | 25.75%   | -92.12%            | -56.22% |     0.48 |       84 | 53.26%     | ok               |
|          40 | 13.48%   | -92.12%            | -53.58% |     0.37 |       58 | 31.61%     | ok               |
|          15 | -0.07%   | -92.12%            | -58.22% |     0.3  |       79 | 59.58%     | ok               |

## ARB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 108.67%  | -62.63%            | -36.31% |     0.93 |       62 | 27.20%     | ok               |
|          40 | 83.59%   | -62.63%            | -38.69% |     0.79 |       57 | 34.87%     | ok               |
|          35 | 65.55%   | -62.63%            | -37.63% |     0.7  |       69 | 39.08%     | ok               |
|          50 | 25.83%   | -62.63%            | -36.31% |     0.46 |       56 | 19.16%     | ok               |
|          15 | 15.79%   | -62.63%            | -57.62% |     0.42 |       99 | 58.24%     | ok               |

## ARKK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -5.98%   | 46.79%             | -37.76% |     0.07 |       88 | 56.41%     | ok               |
|          20 | -16.46%  | 46.79%             | -35.06% |    -0.11 |       91 | 51.91%     | ok               |
|          30 | -23.61%  | 46.79%             | -38.67% |    -0.28 |       89 | 45.59%     | ok               |
|          35 | -29.07%  | 46.79%             | -41.28% |    -0.43 |       94 | 42.26%     | ok               |
|          25 | -34.61%  | 46.79%             | -47.50% |    -0.5  |       99 | 48.09%     | ok               |

## ATOM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -42.06%  | -69.56%            | -55.32% |    -0.36 |       80 | 65.71%     | ok               |
|          20 | -49.89%  | -69.56%            | -58.91% |    -0.56 |       92 | 56.90%     | ok               |
|          25 | -48.35%  | -69.56%            | -55.57% |    -0.57 |       80 | 50.57%     | ok               |
|          50 | -34.51%  | -69.56%            | -39.10% |    -0.62 |       62 | 18.97%     | ok               |
|          45 | -45.20%  | -69.56%            | -53.91% |    -0.66 |       62 | 30.08%     | ok               |

## AVAX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 50.74%   | -62.96%            | -22.06% |     0.82 |       38 | 17.43%     | ok               |
|          40 | 25.55%   | -62.96%            | -26.27% |     0.49 |       42 | 28.93%     | ok               |
|          45 | 24.13%   | -62.96%            | -26.90% |     0.49 |       38 | 24.52%     | ok               |
|          35 | 7.54%    | -62.96%            | -33.05% |     0.28 |       52 | 34.48%     | ok               |
|          15 | -19.07%  | -62.96%            | -43.91% |     0    |       76 | 51.92%     | ok               |

## AVGO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -14.88%  | 72.33%             | -44.82% |    -0.02 |       68 | 38.77%     | ok               |
|          25 | -15.87%  | 72.33%             | -45.43% |    -0.03 |       72 | 41.60%     | ok               |
|          20 | -22.38%  | 72.33%             | -45.94% |    -0.1  |       81 | 45.42%     | ok               |
|          50 | -21.32%  | 72.33%             | -44.23% |    -0.15 |       62 | 26.62%     | ok               |
|          35 | -23.12%  | 72.33%             | -48.57% |    -0.15 |       78 | 35.94%     | ok               |

## BA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 37.42%   | -11.47%            | -18.09% |     0.67 |       66 | 50.58%     | ok               |
|          50 | 24.33%   | -11.47%            | -13.34% |     0.6  |       50 | 35.94%     | ok               |
|          25 | 32.69%   | -11.47%            | -26.02% |     0.59 |       64 | 57.24%     | ok               |
|          40 | 23.28%   | -11.47%            | -23.87% |     0.5  |       50 | 44.76%     | ok               |
|          30 | 22.43%   | -11.47%            | -24.47% |     0.46 |       63 | 53.91%     | ok               |

## BAC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 3.18%    | 19.50%             | -16.89% |     0.16 |       84 | 55.07%     | ok               |
|          45 | 1.17%    | 19.50%             | -13.90% |     0.1  |       54 | 34.11%     | ok               |
|          35 | 0.65%    | 19.50%             | -22.58% |     0.09 |       70 | 44.09%     | ok               |
|          15 | -2.69%   | 19.50%             | -21.05% |     0.03 |       90 | 61.06%     | ok               |
|          25 | -2.48%   | 19.50%             | -22.01% |     0.02 |       84 | 52.41%     | ok               |

## BCH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 15.16%   | -52.98%            | -45.52% |     0.37 |       72 | 55.56%     | ok               |
|          15 | 13.88%   | -52.98%            | -45.64% |     0.36 |       77 | 59.20%     | ok               |
|          35 | 2.00%    | -52.98%            | -57.75% |     0.23 |       70 | 46.17%     | ok               |
|          25 | -1.12%   | -52.98%            | -48.42% |     0.21 |       76 | 51.92%     | ok               |
|          30 | -3.78%   | -52.98%            | -54.04% |     0.17 |       80 | 50.00%     | ok               |

## BITO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -1.02%   | -59.53%            | -31.98% |     0.12 |       52 | 24.96%     | ok               |
|          45 | -7.22%   | -59.53%            | -32.05% |     0.04 |       56 | 28.29%     | ok               |
|          30 | -18.50%  | -59.53%            | -42.14% |    -0.08 |       83 | 41.76%     | ok               |
|          35 | -19.97%  | -59.53%            | -41.80% |    -0.12 |       74 | 37.44%     | ok               |
|          15 | -25.64%  | -59.53%            | -51.02% |    -0.14 |       83 | 49.75%     | ok               |

## BLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 2.37%    | 44.50%             | -20.79% |     0.14 |       84 | 42.76%     | ok               |
|          40 | -2.08%   | 44.50%             | -22.83% |     0.02 |       76 | 38.27%     | ok               |
|          25 | -4.51%   | 44.50%             | -24.62% |    -0.03 |       73 | 49.08%     | ok               |
|          20 | -5.89%   | 44.50%             | -21.48% |    -0.06 |       80 | 51.41%     | ok               |
|          30 | -6.99%   | 44.50%             | -26.90% |    -0.11 |       77 | 46.42%     | ok               |

## BND Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -7.73%   | -1.10%             | -10.72% |    -1.08 |       67 | 42.26%     | ok               |
|          30 | -7.27%   | -1.10%             | -10.43% |    -1.09 |       68 | 36.44%     | ok               |
|          25 | -7.87%   | -1.10%             | -11.16% |    -1.13 |       72 | 39.93%     | ok               |
|          40 | -7.43%   | -1.10%             | -11.03% |    -1.23 |       60 | 30.12%     | ok               |
|          15 | -9.09%   | -1.10%             | -12.04% |    -1.26 |       79 | 44.59%     | ok               |

## BONK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 154.86%  | -84.60%            | -23.92% |     1.27 |       40 | 19.16%     | ok               |
|          40 | 123.58%  | -84.60%            | -43.89% |     1.02 |       60 | 35.25%     | ok               |
|          45 | 102.12%  | -84.60%            | -33.76% |     0.96 |       64 | 25.29%     | ok               |
|          35 | 97.28%   | -84.60%            | -48.16% |     0.88 |       60 | 40.42%     | ok               |
|          15 | 73.28%   | -84.60%            | -55.03% |     0.72 |       65 | 60.73%     | ok               |

## BTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 66.15%   | -41.96%            | -21.12% |     1.09 |       58 | 43.49%     | ok               |
|          40 | 58.81%   | -41.96%            | -17.26% |     1.05 |       46 | 36.97%     | ok               |
|          45 | 50.26%   | -41.96%            | -12.58% |     0.98 |       38 | 32.18%     | ok               |
|          30 | 28.79%   | -41.96%            | -22.34% |     0.58 |       70 | 49.23%     | ok               |
|          50 | 19.58%   | -41.96%            | -20.16% |     0.52 |       36 | 25.29%     | ok               |

## C Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -14.90%  | 75.05%             | -22.85% |    -0.38 |       66 | 30.45%     | ok               |
|          45 | -24.68%  | 75.05%             | -30.69% |    -0.65 |       76 | 35.61%     | ok               |
|          40 | -29.42%  | 75.05%             | -35.05% |    -0.75 |       72 | 38.10%     | ok               |
|          25 | -36.37%  | 75.05%             | -37.53% |    -0.79 |       69 | 49.25%     | ok               |
|          20 | -38.36%  | 75.05%             | -39.30% |    -0.83 |       75 | 51.91%     | ok               |

## CAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 53.03%   | 65.23%             | -21.99% |     0.75 |       67 | 62.23%     | ok               |
|          25 | 49.74%   | 65.23%             | -21.79% |     0.74 |       64 | 54.24%     | ok               |
|          30 | 39.33%   | 65.23%             | -21.87% |     0.63 |       66 | 52.08%     | ok               |
|          20 | 36.13%   | 65.23%             | -24.75% |     0.59 |       68 | 56.74%     | ok               |
|          35 | 32.94%   | 65.23%             | -25.22% |     0.57 |       66 | 46.26%     | ok               |

## CL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 8.16%    | 2.13%              | -13.51% |     0.34 |       40 | 24.46%     | ok               |
|          30 | 7.34%    | 2.13%              | -14.32% |     0.28 |       60 | 40.27%     | ok               |
|          45 | 3.16%    | 2.13%              | -13.13% |     0.17 |       44 | 27.79%     | ok               |
|          35 | 3.06%    | 2.13%              | -15.39% |     0.16 |       60 | 36.44%     | ok               |
|          15 | -1.96%   | 2.13%              | -19.00% |     0.02 |       62 | 48.09%     | ok               |

## CMCSA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -17.43%  | -26.46%            | -27.57% |    -0.57 |       48 | 16.81%     | ok               |
|          15 | -33.28%  | -26.46%            | -43.40% |    -0.66 |       92 | 60.07%     | ok               |
|          45 | -22.75%  | -26.46%            | -34.36% |    -0.71 |       62 | 21.46%     | ok               |
|          40 | -29.72%  | -26.46%            | -41.83% |    -0.78 |       91 | 29.12%     | ok               |
|          35 | -32.51%  | -26.46%            | -46.34% |    -0.8  |       95 | 39.60%     | ok               |

## COMP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -14.38%  | -60.88%            | -36.92% |    -0.05 |       44 | 18.58%     | ok               |
|          30 | -37.88%  | -60.88%            | -52.17% |    -0.26 |       91 | 49.62%     | ok               |
|          45 | -38.46%  | -60.88%            | -41.19% |    -0.41 |       66 | 28.54%     | ok               |
|          35 | -47.59%  | -60.88%            | -54.86% |    -0.47 |       83 | 43.30%     | ok               |
|          20 | -57.21%  | -60.88%            | -65.80% |    -0.56 |      101 | 64.18%     | ok               |

## COP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -13.48%  | 20.31%             | -37.99% |    -0.15 |       68 | 44.26%     | ok               |
|          50 | -12.17%  | 20.31%             | -35.99% |    -0.17 |       50 | 31.28%     | ok               |
|          35 | -14.12%  | 20.31%             | -40.42% |    -0.17 |       67 | 41.10%     | ok               |
|          45 | -17.00%  | 20.31%             | -41.02% |    -0.27 |       60 | 34.78%     | ok               |
|          40 | -22.24%  | 20.31%             | -46.75% |    -0.38 |       66 | 37.94%     | ok               |

## COST Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 17.29%   | 23.38%             | -24.32% |     0.53 |       60 | 47.42%     | ok               |
|          25 | 13.90%   | 23.38%             | -24.93% |     0.46 |       57 | 44.59%     | ok               |
|          35 | 7.33%    | 23.38%             | -30.16% |     0.3  |       56 | 38.94%     | ok               |
|          30 | 2.79%    | 23.38%             | -31.32% |     0.15 |       58 | 41.43%     | ok               |
|          40 | 2.25%    | 23.38%             | -31.90% |     0.14 |       54 | 36.44%     | ok               |

## CRM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -10.49%  | -23.37%            | -25.68% |    -0.04 |       64 | 42.26%     | ok               |
|          40 | -13.84%  | -23.37%            | -31.13% |    -0.11 |       70 | 38.10%     | ok               |
|          15 | -21.59%  | -23.37%            | -47.54% |    -0.17 |       92 | 58.07%     | ok               |
|          30 | -22.78%  | -23.37%            | -38.02% |    -0.24 |       67 | 47.09%     | ok               |
|          25 | -23.94%  | -23.37%            | -40.58% |    -0.26 |       68 | 49.08%     | ok               |

## CRV-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 96.97%   | -68.71%            | -45.78% |     0.92 |       64 | 34.48%     | ok               |
|          30 | 84.89%   | -68.71%            | -46.63% |     0.84 |       66 | 38.51%     | ok               |
|          45 | 69.95%   | -68.71%            | -42.88% |     0.8  |       58 | 24.14%     | ok               |
|          40 | 71.29%   | -68.71%            | -45.11% |     0.78 |       58 | 31.03%     | ok               |
|          20 | 70.55%   | -68.71%            | -57.57% |     0.75 |       71 | 45.79%     | ok               |

## CSCO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 25.96%   | 104.52%            | -22.87% |     0.55 |       54 | 41.76%     | ok               |
|          50 | 21.35%   | 104.52%            | -22.15% |     0.49 |       56 | 39.93%     | ok               |
|          40 | 11.98%   | 104.52%            | -28.93% |     0.32 |       58 | 45.09%     | ok               |
|          35 | 8.45%    | 104.52%            | -28.42% |     0.26 |       60 | 48.59%     | ok               |
|          20 | 7.77%    | 104.52%            | -29.33% |     0.25 |       73 | 55.74%     | ok               |

## CVX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -8.74%   | 36.69%             | -27.82% |    -0.17 |       63 | 35.94%     | ok               |
|          40 | -9.92%   | 36.69%             | -25.79% |    -0.19 |       73 | 39.60%     | ok               |
|          50 | -8.62%   | 36.69%             | -29.71% |    -0.2  |       56 | 31.45%     | ok               |
|          25 | -13.28%  | 36.69%             | -23.25% |    -0.25 |       75 | 47.25%     | ok               |
|          35 | -13.87%  | 36.69%             | -27.83% |    -0.29 |       69 | 41.43%     | ok               |

## DASH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 122.18%  | 82.12%             | -43.46% |     0.9  |       40 | 17.82%     | ok               |
|          40 | 91.67%   | 82.12%             | -42.64% |     0.77 |       46 | 24.14%     | ok               |
|          45 | 62.77%   | 82.12%             | -46.93% |     0.65 |       44 | 20.88%     | ok               |
|          25 | -4.19%   | 82.12%             | -64.14% |     0.36 |       69 | 31.61%     | ok               |
|          30 | -5.75%   | 82.12%             | -64.43% |     0.35 |       59 | 29.12%     | ok               |

## DBC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 1.97%    | 24.77%             | -26.01% |     0.13 |       83 | 44.43%     | ok               |
|          20 | -4.62%   | 24.77%             | -25.69% |    -0.08 |       75 | 41.60%     | ok               |
|          25 | -4.80%   | 24.77%             | -24.84% |    -0.09 |       70 | 39.43%     | ok               |
|          30 | -7.71%   | 24.77%             | -24.10% |    -0.19 |       70 | 37.10%     | ok               |
|          50 | -7.90%   | 24.77%             | -18.84% |    -0.24 |       52 | 25.79%     | ok               |

## DE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -5.11%   | 80.57%             | -19.95% |    -0    |       65 | 49.25%     | ok               |
|          25 | -6.49%   | 80.57%             | -20.14% |    -0.03 |       72 | 47.25%     | ok               |
|          30 | -12.44%  | 80.57%             | -21.16% |    -0.17 |       76 | 44.93%     | ok               |
|          15 | -14.31%  | 80.57%             | -23.06% |    -0.19 |       72 | 52.41%     | ok               |
|          45 | -12.02%  | 80.57%             | -22.07% |    -0.21 |       64 | 34.28%     | ok               |

## DIA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -7.04%   | 27.40%             | -13.58% |    -0.34 |       68 | 43.76%     | ok               |
|          20 | -9.46%   | 27.40%             | -15.48% |    -0.46 |       70 | 46.26%     | ok               |
|          30 | -9.14%   | 27.40%             | -16.20% |    -0.46 |       74 | 42.60%     | ok               |
|          35 | -9.25%   | 27.40%             | -16.94% |    -0.48 |       74 | 39.60%     | ok               |
|          40 | -12.12%  | 27.40%             | -18.41% |    -0.69 |       76 | 36.27%     | ok               |

## DIS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 57.09%   | 28.99%             | -10.17% |     1.43 |       50 | 30.62%     | ok               |
|          40 | 24.51%   | 28.99%             | -18.75% |     0.59 |       65 | 38.77%     | ok               |
|          45 | 21.63%   | 28.99%             | -16.54% |     0.57 |       51 | 34.28%     | ok               |
|          35 | 12.53%   | 28.99%             | -25.30% |     0.35 |       73 | 44.76%     | ok               |
|          15 | 11.40%   | 28.99%             | -32.73% |     0.32 |       79 | 57.57%     | ok               |

## DOGE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -11.16%  | -64.95%            | -64.54% |     0.06 |       62 | 34.29%     | ok               |
|          15 | -18.59%  | -64.95%            | -64.29% |     0.06 |       80 | 62.64%     | ok               |
|          50 | -10.00%  | -64.95%            | -55.20% |     0.04 |       62 | 19.16%     | ok               |
|          20 | -20.67%  | -64.95%            | -64.04% |     0    |       78 | 56.70%     | ok               |
|          35 | -17.50%  | -64.95%            | -65.74% |    -0.01 |       66 | 40.80%     | ok               |

## DOT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -32.04%  | -80.12%            | -46.40% |    -0.44 |       54 | 18.01%     | ok               |
|          40 | -39.05%  | -80.12%            | -50.99% |    -0.46 |       58 | 31.42%     | ok               |
|          35 | -49.80%  | -80.12%            | -59.91% |    -0.49 |       68 | 36.97%     | ok               |
|          20 | -56.91%  | -80.12%            | -71.39% |    -0.52 |       92 | 52.49%     | ok               |
|          15 | -61.54%  | -80.12%            | -76.85% |    -0.53 |       81 | 57.28%     | ok               |

## DXY-INDEX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.53%   | -3.85%             | -5.13%  |    -0.08 |       40 | 31.75%     | ok               |
|          40 | -2.47%   | -3.85%             | -6.15%  |    -0.33 |       66 | 47.30%     | ok               |
|          45 | -2.88%   | -3.85%             | -6.67%  |    -0.42 |       62 | 38.44%     | ok               |
|          15 | -4.55%   | -3.85%             | -10.68% |    -0.42 |       97 | 73.87%     | ok               |
|          30 | -3.75%   | -3.85%             | -8.65%  |    -0.45 |       76 | 57.45%     | ok               |

## EEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -0.39%   | 29.24%             | -25.47% |     0.07 |       68 | 45.92%     | ok               |
|          25 | -1.48%   | 29.24%             | -23.98% |     0.04 |       68 | 44.26%     | ok               |
|          30 | -2.66%   | 29.24%             | -22.68% |     0    |       68 | 42.60%     | ok               |
|          15 | -5.10%   | 29.24%             | -28.49% |    -0.05 |       74 | 49.92%     | ok               |
|          35 | -4.61%   | 29.24%             | -22.40% |    -0.05 |       72 | 40.43%     | ok               |

## EFA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -0.91%   | 24.46%             | -10.10% |     0.03 |       60 | 49.08%     | ok               |
|          20 | -8.09%   | 24.46%             | -12.23% |    -0.28 |       67 | 46.26%     | ok               |
|          30 | -9.07%   | 24.46%             | -12.63% |    -0.35 |       64 | 38.94%     | ok               |
|          25 | -9.53%   | 24.46%             | -13.73% |    -0.36 |       68 | 42.60%     | ok               |
|          40 | -8.96%   | 24.46%             | -14.83% |    -0.38 |       60 | 34.44%     | ok               |

## EOG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -20.81%  | 18.05%             | -38.89% |    -0.44 |       54 | 31.61%     | ok               |
|          40 | -23.77%  | 18.05%             | -40.83% |    -0.52 |       66 | 35.11%     | ok               |
|          50 | -24.39%  | 18.05%             | -37.65% |    -0.57 |       54 | 29.28%     | ok               |
|          35 | -29.23%  | 18.05%             | -44.04% |    -0.65 |       77 | 39.43%     | ok               |
|          30 | -31.84%  | 18.05%             | -48.55% |    -0.68 |       77 | 44.09%     | ok               |

## ETC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 3.43%    | -63.48%            | -46.78% |     0.22 |       53 | 37.36%     | ok               |
|          35 | 3.38%    | -63.48%            | -47.01% |     0.22 |       47 | 33.52%     | ok               |
|          50 | 1.48%    | -63.48%            | -30.03% |     0.16 |       30 | 18.58%     | ok               |
|          45 | -3.86%   | -63.48%            | -32.70% |     0.08 |       36 | 22.22%     | ok               |
|          40 | -5.51%   | -63.48%            | -39.64% |     0.07 |       46 | 27.39%     | ok               |

## ETH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 153.77%  | -29.25%            | -30.11% |     1.32 |       59 | 49.23%     | ok               |
|          40 | 91.73%   | -29.25%            | -33.11% |     1.04 |       60 | 41.38%     | ok               |
|          30 | 97.74%   | -29.25%            | -32.89% |     0.99 |       65 | 57.09%     | ok               |
|          45 | 66.76%   | -29.25%            | -33.73% |     0.87 |       64 | 37.74%     | ok               |
|          50 | 55.94%   | -29.25%            | -33.16% |     0.81 |       66 | 30.27%     | ok               |

## EWJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -18.08%  | 25.32%             | -30.00% |    -0.5  |       58 | 41.76%     | ok               |
|          15 | -22.02%  | 25.32%             | -31.15% |    -0.6  |       69 | 45.09%     | ok               |
|          25 | -22.37%  | 25.32%             | -29.85% |    -0.66 |       62 | 40.60%     | ok               |
|          30 | -23.99%  | 25.32%             | -29.40% |    -0.77 |       70 | 39.27%     | ok               |
|          45 | -24.72%  | 25.32%             | -28.91% |    -0.92 |       66 | 30.62%     | ok               |

## FCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 18.02%   | -5.05%             | -31.94% |     0.38 |       54 | 34.94%     | ok               |
|          50 | 10.50%   | -5.05%             | -26.57% |     0.29 |       58 | 30.95%     | ok               |
|          40 | 5.75%    | -5.05%             | -42.89% |     0.23 |       64 | 39.43%     | ok               |
|          30 | -12.40%  | -5.05%             | -46.84% |    -0    |       67 | 46.92%     | ok               |
|          35 | -16.81%  | -5.05%             | -50.12% |    -0.08 |       69 | 44.59%     | ok               |

## FET-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 19.95%   | -81.58%            | -59.58% |     0.45 |       69 | 59.96%     | ok               |
|          20 | -26.16%  | -81.58%            | -66.17% |     0.06 |       84 | 55.94%     | ok               |
|          25 | -41.61%  | -81.58%            | -65.31% |    -0.16 |       81 | 49.81%     | ok               |
|          30 | -48.08%  | -81.58%            | -66.52% |    -0.32 |       77 | 45.21%     | ok               |
|          45 | -39.38%  | -81.58%            | -51.19% |    -0.41 |       54 | 23.56%     | ok               |

## FIL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -6.15%   | -76.15%            | -58.54% |     0.16 |       61 | 40.23%     | ok               |
|          25 | -26.88%  | -76.15%            | -70.65% |    -0.06 |       68 | 44.06%     | ok               |
|          40 | -27.38%  | -76.15%            | -62.90% |    -0.15 |       52 | 31.42%     | ok               |
|          15 | -37.64%  | -76.15%            | -71.31% |    -0.15 |       87 | 53.26%     | ok               |
|          35 | -33.76%  | -76.15%            | -70.22% |    -0.23 |       62 | 35.44%     | ok               |

## FXI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 2.95%    | 19.33%             | -21.68% |     0.16 |       51 | 35.94%     | ok               |
|          25 | 1.18%    | 19.33%             | -22.57% |     0.11 |       50 | 32.61%     | ok               |
|          20 | -0.30%   | 19.33%             | -24.53% |     0.08 |       48 | 33.94%     | ok               |
|          30 | -1.03%   | 19.33%             | -23.91% |     0.06 |       48 | 31.28%     | ok               |
|          35 | -5.30%   | 19.33%             | -27.53% |    -0.06 |       50 | 28.45%     | ok               |

## GDX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -1.32%   | 104.68%            | -30.00% |     0.14 |       82 | 51.41%     | ok               |
|          40 | -3.49%   | 104.68%            | -34.42% |     0.07 |       66 | 39.10%     | ok               |
|          30 | -4.93%   | 104.68%            | -34.29% |     0.07 |       68 | 45.26%     | ok               |
|          35 | -9.07%   | 104.68%            | -38.67% |    -0.01 |       74 | 41.76%     | ok               |
|          25 | -13.90%  | 104.68%            | -42.42% |    -0.07 |       72 | 47.09%     | ok               |

## GDXJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -16.79%  | 94.76%             | -34.84% |    -0.05 |       72 | 51.58%     | ok               |
|          35 | -28.11%  | 94.76%             | -38.09% |    -0.29 |       70 | 41.76%     | ok               |
|          30 | -30.10%  | 94.76%             | -36.01% |    -0.32 |       70 | 44.43%     | ok               |
|          25 | -34.34%  | 94.76%             | -39.67% |    -0.37 |       75 | 47.59%     | ok               |
|          40 | -30.85%  | 94.76%             | -46.16% |    -0.38 |       64 | 39.27%     | ok               |

## GE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 1.03%    | 93.84%             | -21.25% |     0.12 |       62 | 34.61%     | ok               |
|          45 | -10.76%  | 93.84%             | -21.88% |    -0.13 |       74 | 37.60%     | ok               |
|          30 | -20.14%  | 93.84%             | -32.12% |    -0.28 |       84 | 49.75%     | ok               |
|          20 | -20.96%  | 93.84%             | -30.37% |    -0.29 |       80 | 54.24%     | ok               |
|          25 | -20.52%  | 93.84%             | -32.30% |    -0.29 |       80 | 51.58%     | ok               |

## GLD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 21.05%   | 50.08%             | -13.87% |     0.54 |       48 | 47.59%     | ok               |
|          20 | 19.41%   | 50.08%             | -13.87% |     0.51 |       49 | 49.25%     | ok               |
|          30 | 11.67%   | 50.08%             | -14.15% |     0.35 |       52 | 46.09%     | ok               |
|          35 | 8.96%    | 50.08%             | -15.57% |     0.3  |       52 | 43.43%     | ok               |
|          15 | 9.21%    | 50.08%             | -18.05% |     0.29 |       53 | 52.58%     | ok               |

## GOOGL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 64.99%   | 44.47%             | -17.38% |     1.04 |       61 | 45.42%     | ok               |
|          25 | 66.26%   | 44.47%             | -16.87% |     1.02 |       61 | 51.75%     | ok               |
|          45 | 55.11%   | 44.47%             | -11.66% |     1    |       52 | 38.10%     | ok               |
|          15 | 66.28%   | 44.47%             | -15.62% |     0.98 |       68 | 58.90%     | ok               |
|          30 | 61.00%   | 44.47%             | -17.54% |     0.97 |       59 | 48.92%     | ok               |

## GRT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 105.80%  | -79.94%            | -34.35% |     0.92 |       68 | 61.49%     | ok               |
|          35 | 85.19%   | -79.94%            | -28.74% |     0.89 |       64 | 38.51%     | ok               |
|          45 | 67.74%   | -79.94%            | -36.59% |     0.82 |       48 | 25.10%     | ok               |
|          20 | 75.02%   | -79.94%            | -40.51% |     0.78 |       82 | 53.83%     | ok               |
|          30 | 66.70%   | -79.94%            | -35.55% |     0.76 |       71 | 44.25%     | ok               |

## GS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 22.58%   | 72.33%             | -20.56% |     0.5  |       66 | 55.24%     | ok               |
|          40 | 7.27%    | 72.33%             | -16.16% |     0.25 |       64 | 40.93%     | ok               |
|          20 | 7.49%    | 72.33%             | -23.19% |     0.25 |       64 | 51.91%     | ok               |
|          25 | -0.60%   | 72.33%             | -23.32% |     0.09 |       66 | 49.92%     | ok               |
|          35 | -1.92%   | 72.33%             | -19.95% |     0.06 |       68 | 44.59%     | ok               |

## HBAR-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -26.95%  | -46.18%            | -58.64% |    -0.3  |       54 | 56.68%     | ok               |
|          30 | -26.98%  | -46.18%            | -56.47% |    -0.33 |       44 | 42.67%     | ok               |
|          45 | -26.35%  | -46.18%            | -49.09% |    -0.38 |       30 | 28.01%     | ok               |
|          40 | -27.95%  | -46.18%            | -51.16% |    -0.4  |       34 | 33.55%     | ok               |
|          35 | -31.95%  | -46.18%            | -56.01% |    -0.49 |       32 | 38.44%     | ok               |

## HD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 14.47%   | 6.38%              | -17.15% |     0.41 |       67 | 45.59%     | ok               |
|          25 | 13.40%   | 6.38%              | -16.67% |     0.39 |       68 | 47.59%     | ok               |
|          40 | 11.46%   | 6.38%              | -14.18% |     0.38 |       72 | 35.27%     | ok               |
|          35 | 11.73%   | 6.38%              | -16.37% |     0.37 |       72 | 40.93%     | ok               |
|          45 | 9.87%    | 6.38%              | -13.34% |     0.35 |       48 | 30.28%     | ok               |

## HON Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -10.34%  | 7.61%              | -20.43% |    -0.26 |       64 | 29.95%     | ok               |
|          45 | -13.98%  | 7.61%              | -22.88% |    -0.35 |       66 | 35.11%     | ok               |
|          35 | -26.22%  | 7.61%              | -31.30% |    -0.69 |       87 | 46.42%     | ok               |
|          30 | -27.34%  | 7.61%              | -32.93% |    -0.69 |       87 | 51.25%     | ok               |
|          40 | -26.41%  | 7.61%              | -31.84% |    -0.73 |       74 | 39.27%     | ok               |

## HYG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -4.79%   | -1.15%             | -7.93%  |    -0.55 |       70 | 33.94%     | ok               |
|          45 | -6.55%   | -1.15%             | -9.07%  |    -0.79 |       70 | 30.28%     | ok               |
|          20 | -7.50%   | -1.15%             | -11.56% |    -0.8  |       94 | 45.09%     | ok               |
|          25 | -7.52%   | -1.15%             | -11.22% |    -0.81 |       91 | 42.76%     | ok               |
|          35 | -7.06%   | -1.15%             | -9.76%  |    -0.81 |       81 | 35.94%     | ok               |

## IBIT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 95.27%   | -10.37%            | -19.20% |     1.14 |       48 | 43.98%     | ok               |
|          50 | 59.20%   | -10.37%            | -17.37% |     0.97 |       30 | 25.24%     | ok               |
|          45 | 61.60%   | -10.37%            | -17.37% |     0.97 |       34 | 26.96%     | ok               |
|          30 | 59.91%   | -10.37%            | -18.95% |     0.89 |       46 | 36.71%     | ok               |
|          40 | 48.89%   | -10.37%            | -22.57% |     0.82 |       42 | 30.02%     | ok               |

## IBM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -21.19%  | 37.06%             | -50.66% |    -0.17 |       87 | 62.56%     | ok               |
|          35 | -23.41%  | 37.06%             | -47.10% |    -0.26 |       67 | 46.92%     | ok               |
|          30 | -28.31%  | 37.06%             | -50.84% |    -0.36 |       73 | 50.42%     | ok               |
|          20 | -32.50%  | 37.06%             | -55.39% |    -0.4  |       73 | 55.57%     | ok               |
|          50 | -29.47%  | 37.06%             | -45.97% |    -0.44 |       46 | 35.27%     | ok               |

## ICP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 15.46%   | -59.04%            | -42.66% |     0.4  |       70 | 41.76%     | ok               |
|          35 | 3.04%    | -59.04%            | -49.65% |     0.28 |       68 | 36.59%     | ok               |
|          40 | -8.65%   | -59.04%            | -47.74% |     0.15 |       64 | 32.18%     | ok               |
|          20 | -26.75%  | -59.04%            | -63.83% |     0.07 |       81 | 49.23%     | ok               |
|          25 | -28.34%  | -59.04%            | -58.19% |     0.03 |       70 | 45.21%     | ok               |

## IEF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.88%   | -2.26%             | -10.18% |    -0.79 |       74 | 43.93%     | ok               |
|          15 | -8.16%   | -2.26%             | -11.03% |    -0.92 |       74 | 45.76%     | ok               |
|          40 | -8.35%   | -2.26%             | -10.25% |    -1.21 |       68 | 27.12%     | ok               |
|          45 | -8.71%   | -2.26%             | -10.37% |    -1.31 |       64 | 24.46%     | ok               |
|          30 | -10.33%  | -2.26%             | -12.21% |    -1.35 |       78 | 35.61%     | ok               |

## IEMG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 2.55%    | 25.51%             | -23.73% |     0.15 |       63 | 45.09%     | ok               |
|          20 | 0.82%    | 25.51%             | -25.26% |     0.1  |       61 | 46.76%     | ok               |
|          30 | -0.79%   | 25.51%             | -24.73% |     0.05 |       64 | 42.76%     | ok               |
|          35 | -2.82%   | 25.51%             | -23.28% |    -0.01 |       71 | 41.26%     | ok               |
|          40 | -5.92%   | 25.51%             | -20.42% |    -0.11 |       72 | 38.60%     | ok               |

## INJ-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 33.68%   | -44.48%            | -42.48% |     0.53 |       52 | 35.63%     | ok               |
|          40 | 31.33%   | -44.48%            | -33.49% |     0.51 |       42 | 32.38%     | ok               |
|          45 | 17.42%   | -44.48%            | -37.55% |     0.39 |       48 | 25.86%     | ok               |
|          25 | 1.63%    | -44.48%            | -51.31% |     0.28 |       60 | 41.57%     | ok               |
|          15 | -0.59%   | -44.48%            | -60.14% |     0.27 |       69 | 46.55%     | ok               |

## INTC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 108.30%  | 60.25%             | -49.32% |     0.88 |       60 | 35.94%     | ok               |
|          50 | 101.83%  | 60.25%             | -48.35% |     0.86 |       64 | 32.11%     | ok               |
|          20 | 75.36%   | 60.25%             | -52.47% |     0.7  |       82 | 57.90%     | ok               |
|          25 | 71.90%   | 60.25%             | -56.41% |     0.69 |       81 | 53.58%     | ok               |
|          15 | 70.62%   | 60.25%             | -53.65% |     0.67 |       76 | 61.06%     | ok               |

## INTU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 8.13%    | -58.80%            | -32.57% |     0.26 |       67 | 27.95%     | ok               |
|          35 | 1.92%    | -58.80%            | -42.23% |     0.16 |       73 | 40.60%     | ok               |
|          45 | 2.17%    | -58.80%            | -34.86% |     0.16 |       65 | 31.95%     | ok               |
|          40 | -0.10%   | -58.80%            | -38.48% |     0.12 |       71 | 35.94%     | ok               |
|          25 | -5.33%   | -58.80%            | -35.66% |     0.06 |       74 | 49.58%     | ok               |

## ITA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 0.31%    | 54.85%             | -26.15% |     0.1  |       73 | 59.40%     | ok               |
|          30 | 0.52%    | 54.85%             | -22.33% |     0.09 |       72 | 47.09%     | ok               |
|          50 | -0.54%   | 54.85%             | -21.48% |     0.05 |       68 | 34.78%     | ok               |
|          35 | -4.77%   | 54.85%             | -22.44% |    -0.07 |       72 | 43.43%     | ok               |
|          20 | -5.79%   | 54.85%             | -26.56% |    -0.07 |       72 | 53.74%     | ok               |

## IWM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          25 | 15.49%   | 32.92%             | -8.59% |     0.58 |       54 | 36.27%     | ok               |
|          20 | 10.94%   | 32.92%             | -9.67% |     0.43 |       64 | 37.27%     | ok               |
|          30 | 10.39%   | 32.92%             | -8.62% |     0.42 |       56 | 34.44%     | ok               |
|          40 | 8.67%    | 32.92%             | -9.21% |     0.4  |       44 | 29.28%     | ok               |
|          35 | 8.33%    | 32.92%             | -9.25% |     0.36 |       52 | 31.95%     | ok               |

## JNJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 16.70%   | 88.30%             | -10.97% |     0.66 |       44 | 36.77%     | ok               |
|          15 | 13.29%   | 88.30%             | -18.02% |     0.47 |       62 | 54.74%     | ok               |
|          30 | 9.85%    | 88.30%             | -17.51% |     0.39 |       62 | 48.09%     | ok               |
|          20 | 8.06%    | 88.30%             | -17.61% |     0.32 |       68 | 51.25%     | ok               |
|          45 | 6.71%    | 88.30%             | -13.35% |     0.3  |       50 | 40.43%     | ok               |

## JPM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 0.07%    | 54.38%             | -15.90% |     0.06 |       52 | 32.11%     | ok               |
|          45 | -10.24%  | 54.38%             | -21.91% |    -0.27 |       56 | 34.78%     | ok               |
|          20 | -27.08%  | 54.38%             | -35.58% |    -0.63 |       90 | 49.42%     | ok               |
|          40 | -22.56%  | 54.38%             | -28.47% |    -0.69 |       68 | 37.44%     | ok               |
|          35 | -25.11%  | 54.38%             | -29.39% |    -0.77 |       78 | 41.10%     | ok               |

## KO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 25.09%   | 55.00%             | -8.64%  |     0.85 |       54 | 40.43%     | ok               |
|          40 | 20.33%   | 55.00%             | -9.28%  |     0.75 |       58 | 35.94%     | ok               |
|          35 | 20.84%   | 55.00%             | -8.73%  |     0.73 |       58 | 38.94%     | ok               |
|          25 | 19.00%   | 55.00%             | -10.61% |     0.66 |       60 | 43.09%     | ok               |
|          50 | 7.54%    | 55.00%             | -16.13% |     0.34 |       44 | 30.12%     | ok               |

## LDO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 163.67%  | -66.39%            | -47.13% |     1.07 |       78 | 61.30%     | ok               |
|          30 | 92.80%   | -66.39%            | -51.13% |     0.84 |       66 | 49.43%     | ok               |
|          20 | 82.35%   | -66.39%            | -49.09% |     0.78 |       81 | 55.75%     | ok               |
|          25 | 66.14%   | -66.39%            | -52.80% |     0.71 |       76 | 53.26%     | ok               |
|          35 | 23.51%   | -66.39%            | -58.29% |     0.45 |       80 | 42.15%     | ok               |

## LIN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -3.14%   | 20.40%             | -23.00% |    -0.04 |       64 | 48.09%     | ok               |
|          25 | -3.07%   | 20.40%             | -22.01% |    -0.04 |       71 | 45.09%     | ok               |
|          45 | -4.57%   | 20.40%             | -17.04% |    -0.13 |       46 | 25.29%     | ok               |
|          30 | -6.30%   | 20.40%             | -20.61% |    -0.15 |       72 | 42.26%     | ok               |
|          15 | -7.74%   | 20.40%             | -23.68% |    -0.18 |       72 | 51.25%     | ok               |

## LINK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 38.50%   | -28.50%            | -34.21% |     0.58 |       60 | 38.89%     | ok               |
|          45 | 34.26%   | -28.50%            | -34.16% |     0.55 |       52 | 31.03%     | ok               |
|          40 | 32.99%   | -28.50%            | -36.88% |     0.54 |       52 | 34.10%     | ok               |
|          50 | 28.12%   | -28.50%            | -28.65% |     0.5  |       48 | 25.10%     | ok               |
|          30 | 25.67%   | -28.50%            | -35.01% |     0.47 |       70 | 43.49%     | ok               |

## LLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -2.44%   | 51.66%             | -38.23% |     0.07 |       50 | 34.61%     | ok               |
|          15 | -15.61%  | 51.66%             | -48.12% |    -0.1  |       70 | 60.23%     | ok               |
|          45 | -17.58%  | 51.66%             | -42.99% |    -0.22 |       60 | 38.60%     | ok               |
|          40 | -27.11%  | 51.66%             | -45.23% |    -0.4  |       72 | 41.93%     | ok               |
|          20 | -30.30%  | 51.66%             | -51.14% |    -0.41 |       79 | 54.91%     | ok               |

## LRCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -11.28%  | 67.95%             | -56.69% |     0.13 |       82 | 54.08%     | ok               |
|          35 | -12.42%  | 67.95%             | -57.54% |     0.08 |       80 | 44.43%     | ok               |
|          20 | -17.14%  | 67.95%             | -62.08% |     0.05 |       85 | 49.75%     | ok               |
|          30 | -18.17%  | 67.95%             | -60.21% |     0.02 |       84 | 45.09%     | ok               |
|          40 | -18.13%  | 67.95%             | -55.33% |     0.01 |       74 | 42.26%     | ok               |

## LTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 45.41%   | -47.67%            | -30.75% |     0.67 |       68 | 45.79%     | ok               |
|          30 | 47.29%   | -47.67%            | -29.27% |     0.67 |       71 | 52.11%     | ok               |
|          25 | 46.10%   | -47.67%            | -32.32% |     0.66 |       71 | 54.79%     | ok               |
|          45 | 36.66%   | -47.67%            | -35.29% |     0.61 |       56 | 34.29%     | ok               |
|          50 | 21.18%   | -47.67%            | -35.78% |     0.45 |       50 | 25.67%     | ok               |

## MCD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 9.07%    | 14.38%             | -22.20% |     0.36 |       79 | 41.76%     | ok               |
|          50 | 6.19%    | 14.38%             | -9.22%  |     0.31 |       50 | 25.96%     | ok               |
|          35 | 6.49%    | 14.38%             | -16.97% |     0.29 |       71 | 38.77%     | ok               |
|          25 | 6.80%    | 14.38%             | -23.93% |     0.28 |       77 | 44.43%     | ok               |
|          20 | 2.45%    | 14.38%             | -24.58% |     0.14 |       79 | 47.59%     | ok               |

## META Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -21.44%  | 15.22%             | -37.54% |    -0.31 |       66 | 37.77%     | ok               |
|          50 | -21.33%  | 15.22%             | -39.33% |    -0.32 |       66 | 33.61%     | ok               |
|          40 | -25.51%  | 15.22%             | -40.90% |    -0.38 |       68 | 40.93%     | ok               |
|          35 | -36.12%  | 15.22%             | -41.21% |    -0.61 |       81 | 46.42%     | ok               |
|          30 | -41.85%  | 15.22%             | -45.06% |    -0.72 |       76 | 49.25%     | ok               |

## MPC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 20.28%   | 106.77%            | -18.24% |     0.45 |       52 | 41.43%     | ok               |
|          40 | 18.30%   | 106.77%            | -20.11% |     0.41 |       62 | 48.09%     | ok               |
|          35 | 17.46%   | 106.77%            | -30.41% |     0.39 |       68 | 50.75%     | ok               |
|          45 | 16.22%   | 106.77%            | -19.46% |     0.38 |       58 | 45.42%     | ok               |
|          30 | 11.57%   | 106.77%            | -33.74% |     0.31 |       70 | 53.41%     | ok               |

## MRK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -14.78%  | 11.54%             | -27.83% |    -0.2  |       85 | 53.08%     | ok               |
|          25 | -15.36%  | 11.54%             | -31.07% |    -0.23 |       72 | 45.26%     | ok               |
|          20 | -19.51%  | 11.54%             | -29.34% |    -0.33 |       77 | 48.59%     | ok               |
|          50 | -16.04%  | 11.54%             | -23.01% |    -0.34 |       58 | 29.62%     | ok               |
|          45 | -18.12%  | 11.54%             | -25.38% |    -0.37 |       59 | 32.95%     | ok               |

## MS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 0.68%    | 66.57%             | -19.99% |     0.1  |       64 | 38.27%     | ok               |
|          15 | -1.58%   | 66.57%             | -22.02% |     0.07 |       70 | 56.24%     | ok               |
|          20 | -3.77%   | 66.57%             | -25.68% |     0.01 |       69 | 52.08%     | ok               |
|          30 | -6.30%   | 66.57%             | -27.79% |    -0.06 |       69 | 47.25%     | ok               |
|          25 | -7.77%   | 66.57%             | -28.36% |    -0.1  |       67 | 49.42%     | ok               |

## MSFT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -19.20%  | 5.08%              | -25.05% |    -0.48 |       70 | 35.61%     | ok               |
|          50 | -22.52%  | 5.08%              | -25.93% |    -0.61 |       62 | 30.45%     | ok               |
|          35 | -27.86%  | 5.08%              | -35.20% |    -0.65 |       73 | 44.93%     | ok               |
|          40 | -27.49%  | 5.08%              | -34.58% |    -0.67 |       69 | 39.10%     | ok               |
|          30 | -30.95%  | 5.08%              | -38.98% |    -0.71 |       81 | 49.75%     | ok               |

## MU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 127.15%  | 360.06%            | -61.12% |     0.93 |       60 | 45.76%     | ok               |
|          45 | 113.77%  | 360.06%            | -62.28% |     0.9  |       62 | 42.93%     | ok               |
|          15 | 125.55%  | 360.06%            | -61.96% |     0.88 |       56 | 58.07%     | ok               |
|          30 | 113.71%  | 360.06%            | -64.76% |     0.88 |       51 | 50.08%     | ok               |
|          35 | 107.80%  | 360.06%            | -65.13% |     0.86 |       63 | 47.75%     | ok               |

## NEAR-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 242.24%  | 40.77%             | -36.62% |     1.47 |       32 | 22.22%     | ok               |
|          40 | 260.70%  | 40.77%             | -36.30% |     1.41 |       44 | 32.95%     | ok               |
|          45 | 213.02%  | 40.77%             | -39.04% |     1.3  |       46 | 28.74%     | ok               |
|          35 | 148.21%  | 40.77%             | -52.16% |     1.07 |       62 | 37.55%     | ok               |
|          30 | 156.41%  | 40.77%             | -47.64% |     1.06 |       67 | 44.83%     | ok               |

## NEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -6.37%   | 129.87%            | -35.45% |     0.09 |       67 | 58.24%     | ok               |
|          20 | -6.04%   | 129.87%            | -30.50% |     0.08 |       71 | 53.74%     | ok               |
|          50 | -14.13%  | 129.87%            | -33.24% |    -0.09 |       48 | 37.27%     | ok               |
|          25 | -20.39%  | 129.87%            | -39.51% |    -0.14 |       68 | 51.41%     | ok               |
|          30 | -27.00%  | 129.87%            | -39.56% |    -0.27 |       70 | 49.42%     | ok               |

## NFLX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 14.88%   | -13.36%            | -16.28% |     0.45 |       42 | 28.62%     | ok               |
|          40 | 13.66%   | -13.36%            | -20.78% |     0.4  |       54 | 36.77%     | ok               |
|          35 | 7.27%    | -13.36%            | -18.30% |     0.25 |       82 | 41.76%     | ok               |
|          15 | 3.93%    | -13.36%            | -26.59% |     0.19 |       78 | 62.90%     | ok               |
|          45 | 1.96%    | -13.36%            | -18.06% |     0.13 |       56 | 32.61%     | ok               |

## NKE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -29.57%  | -49.82%            | -35.00% |    -0.59 |       67 | 31.61%     | ok               |
|          25 | -44.97%  | -49.82%            | -51.50% |    -0.73 |       85 | 51.91%     | ok               |
|          35 | -38.05%  | -49.82%            | -42.49% |    -0.74 |       73 | 38.77%     | ok               |
|          20 | -47.86%  | -49.82%            | -51.16% |    -0.79 |       92 | 55.07%     | ok               |
|          15 | -52.53%  | -49.82%            | -57.49% |    -0.91 |       93 | 59.07%     | ok               |

## NOW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -4.34%   | -39.86%            | -42.66% |     0.16 |       79 | 51.75%     | ok               |
|          20 | -5.54%   | -39.86%            | -49.77% |     0.16 |       74 | 57.74%     | ok               |
|          25 | -8.85%   | -39.86%            | -47.93% |     0.12 |       71 | 55.24%     | ok               |
|          15 | -13.60%  | -39.86%            | -52.56% |     0.07 |       82 | 60.57%     | ok               |
|          35 | -17.33%  | -39.86%            | -48.24% |    -0.02 |       82 | 46.92%     | ok               |

## NVDA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -15.99%  | 38.24%             | -38.53% |     0.01 |       74 | 51.52%     | ok               |
|          25 | -21.93%  | 38.24%             | -44.52% |    -0.08 |       79 | 47.59%     | ok               |
|          30 | -21.68%  | 38.24%             | -43.72% |    -0.09 |       80 | 44.74%     | ok               |
|          15 | -30.06%  | 38.24%             | -47.95% |    -0.18 |       80 | 55.79%     | ok               |
|          35 | -32.41%  | 38.24%             | -51.29% |    -0.28 |       88 | 42.07%     | ok               |

## OP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 59.43%   | -87.05%            | -33.09% |     0.87 |       42 | 13.03%     | ok               |
|          45 | 67.76%   | -87.05%            | -30.78% |     0.84 |       46 | 18.97%     | ok               |
|          40 | 50.16%   | -87.05%            | -43.68% |     0.67 |       48 | 26.63%     | ok               |
|          35 | 2.55%    | -87.05%            | -56.85% |     0.24 |       58 | 31.61%     | ok               |
|          15 | -12.48%  | -87.05%            | -57.22% |     0.15 |       75 | 50.00%     | ok               |

## ORCL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 122.18%  | -28.37%            | -37.59% |     0.96 |       67 | 58.74%     | ok               |
|          45 | 79.52%   | -28.37%            | -32.35% |     0.82 |       54 | 36.44%     | ok               |
|          25 | 78.64%   | -28.37%            | -31.06% |     0.76 |       59 | 51.25%     | ok               |
|          20 | 73.66%   | -28.37%            | -32.60% |     0.73 |       68 | 54.41%     | ok               |
|          35 | 70.18%   | -28.37%            | -31.95% |     0.73 |       60 | 45.42%     | ok               |

## OXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 10.08%   | -11.48%            | -28.48% |     0.29 |       63 | 43.76%     | ok               |
|          35 | 7.25%    | -11.48%            | -26.37% |     0.24 |       70 | 39.10%     | ok               |
|          40 | -1.38%   | -11.48%            | -28.30% |     0.09 |       58 | 35.61%     | ok               |
|          50 | -2.05%   | -11.48%            | -26.34% |     0.07 |       48 | 29.12%     | ok               |
|          25 | -5.26%   | -11.48%            | -38.51% |     0.04 |       73 | 47.25%     | ok               |

## PEP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 14.53%   | -11.22%            | -11.62% |     0.6  |       40 | 26.96%     | ok               |
|          45 | 3.17%    | -11.22%            | -14.22% |     0.17 |       52 | 30.78%     | ok               |
|          30 | 1.75%    | -11.22%            | -21.35% |     0.12 |       72 | 46.42%     | ok               |
|          35 | -0.67%   | -11.22%            | -21.42% |     0.05 |       73 | 40.60%     | ok               |
|          40 | -3.48%   | -11.22%            | -18.04% |    -0.07 |       68 | 35.94%     | ok               |

## PEPE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -40.06%  | -64.16%            | -64.84% |    -0.04 |       89 | 62.45%     | ok               |
|          30 | -36.29%  | -64.16%            | -60.19% |    -0.12 |       76 | 47.13%     | ok               |
|          20 | -50.67%  | -64.16%            | -64.77% |    -0.27 |       97 | 57.66%     | ok               |
|          35 | -42.05%  | -64.16%            | -60.83% |    -0.28 |       68 | 43.30%     | ok               |
|          25 | -54.16%  | -64.16%            | -65.63% |    -0.39 |       92 | 52.49%     | ok               |

## PFE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -16.29%  | 1.90%              | -29.60% |    -0.54 |       42 | 19.80%     | ok               |
|          45 | -21.49%  | 1.90%              | -30.53% |    -0.67 |       54 | 23.29%     | ok               |
|          40 | -24.28%  | 1.90%              | -34.20% |    -0.74 |       76 | 28.45%     | ok               |
|          35 | -31.57%  | 1.90%              | -40.11% |    -0.97 |       86 | 34.94%     | ok               |
|          30 | -38.60%  | 1.90%              | -46.24% |    -1.19 |       81 | 37.94%     | ok               |

## PG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -3.98%   | 4.03%              | -20.08% |    -0.09 |       52 | 31.61%     | ok               |
|          35 | -7.25%   | 4.03%              | -18.99% |    -0.21 |       60 | 35.11%     | ok               |
|          45 | -12.12%  | 4.03%              | -22.00% |    -0.43 |       52 | 29.28%     | ok               |
|          30 | -15.68%  | 4.03%              | -24.55% |    -0.51 |       62 | 38.27%     | ok               |
|          50 | -14.59%  | 4.03%              | -24.20% |    -0.58 |       56 | 25.29%     | ok               |

## PM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -2.96%   | 79.67%             | -34.56% |     0.02 |       80 | 44.09%     | ok               |
|          20 | -5.23%   | 79.67%             | -36.03% |    -0.02 |       77 | 52.58%     | ok               |
|          30 | -6.01%   | 79.67%             | -37.61% |    -0.04 |       75 | 47.59%     | ok               |
|          50 | -9.22%   | 79.67%             | -36.94% |    -0.16 |       66 | 35.44%     | ok               |
|          25 | -12.85%  | 79.67%             | -41.68% |    -0.21 |       73 | 49.42%     | ok               |

## POL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 15.72%   | -57.47%            | -25.31% |     0.38 |       54 | 19.16%     | ok               |
|          45 | 12.51%   | -57.47%            | -30.67% |     0.33 |       54 | 27.20%     | ok               |
|          25 | 6.22%    | -57.47%            | -46.25% |     0.29 |       79 | 53.83%     | ok               |
|          30 | 5.57%    | -57.47%            | -46.25% |     0.27 |       83 | 48.28%     | ok               |
|          20 | 2.77%    | -57.47%            | -48.58% |     0.26 |       89 | 58.24%     | ok               |

## QCOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -21.17%  | -18.87%            | -48.91% |    -0.1  |       73 | 41.76%     | ok               |
|          35 | -21.87%  | -18.87%            | -39.94% |    -0.14 |       77 | 37.44%     | ok               |
|          20 | -26.96%  | -18.87%            | -48.77% |    -0.18 |       69 | 45.09%     | ok               |
|          15 | -35.79%  | -18.87%            | -52.77% |    -0.32 |       71 | 47.75%     | ok               |
|          30 | -35.78%  | -18.87%            | -50.90% |    -0.37 |       77 | 40.10%     | ok               |

## QQQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 6.26%    | 27.46%             | -17.16% |     0.23 |       73 | 52.41%     | ok               |
|          25 | 3.16%    | 27.46%             | -14.05% |     0.16 |       69 | 45.09%     | ok               |
|          20 | 1.53%    | 27.46%             | -14.88% |     0.13 |       79 | 48.42%     | ok               |
|          30 | -3.38%   | 27.46%             | -15.84% |     0    |       72 | 42.76%     | ok               |
|          35 | -15.84%  | 27.46%             | -19.93% |    -0.36 |       82 | 38.60%     | ok               |

## RENDER-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -22.17%  | -57.43%            | -43.75% |     0.08 |       92 | 60.15%     | ok               |
|          20 | -27.63%  | -57.43%            | -50.73% |    -0.01 |       93 | 54.79%     | ok               |
|          25 | -26.77%  | -57.43%            | -50.52% |    -0.01 |       85 | 50.00%     | ok               |
|          50 | -16.84%  | -57.43%            | -42.88% |    -0.15 |       56 | 16.28%     | ok               |
|          30 | -52.22%  | -57.43%            | -59.91% |    -0.45 |       88 | 45.40%     | ok               |

## RTX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 26.32%   | 95.99%             | -18.66% |     0.59 |       72 | 58.57%     | ok               |
|          25 | 23.72%   | 95.99%             | -18.59% |     0.55 |       64 | 55.91%     | ok               |
|          15 | 17.83%   | 95.99%             | -19.55% |     0.44 |       69 | 61.90%     | ok               |
|          50 | 13.31%   | 95.99%             | -18.42% |     0.43 |       62 | 39.77%     | ok               |
|          30 | 16.35%   | 95.99%             | -16.99% |     0.43 |       73 | 52.91%     | ok               |

## SBUX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -0.52%   | 44.48%             | -25.43% |     0.08 |       58 | 34.11%     | ok               |
|          25 | -2.06%   | 44.48%             | -23.55% |     0.06 |       61 | 42.76%     | ok               |
|          45 | -2.46%   | 44.48%             | -27.26% |     0.03 |       62 | 29.45%     | ok               |
|          50 | -4.97%   | 44.48%             | -25.13% |    -0.04 |       50 | 24.96%     | ok               |
|          35 | -8.12%   | 44.48%             | -26.54% |    -0.08 |       66 | 37.77%     | ok               |

## SCHW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.50%   | 27.59%             | -29.24% |    -0.06 |       73 | 52.91%     | ok               |
|          45 | -4.63%   | 27.59%             | -16.53% |    -0.07 |       64 | 31.45%     | ok               |
|          50 | -3.90%   | 27.59%             | -13.28% |    -0.08 |       54 | 28.12%     | ok               |
|          25 | -7.72%   | 27.59%             | -28.76% |    -0.09 |       67 | 51.08%     | ok               |
|          15 | -12.90%  | 27.59%             | -31.37% |    -0.21 |       82 | 57.07%     | ok               |

## SHIB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -15.74%  | -68.45%            | -44.71% |     0.01 |       85 | 65.71%     | ok               |
|          50 | -8.65%   | -68.45%            | -27.01% |    -0.02 |       50 | 18.20%     | ok               |
|          20 | -19.29%  | -68.45%            | -49.90% |    -0.05 |       78 | 61.11%     | ok               |
|          35 | -20.97%  | -68.45%            | -48.59% |    -0.13 |       77 | 44.64%     | ok               |
|          25 | -25.80%  | -68.45%            | -50.56% |    -0.16 |       78 | 57.66%     | ok               |

## SHY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          30 | -1.90%   | 0.00%              | -3.30% |    -0.63 |       54 | 38.94%     | ok               |
|          40 | -2.07%   | 0.00%              | -3.52% |    -0.71 |       58 | 35.44%     | ok               |
|          45 | -2.14%   | 0.00%              | -3.37% |    -0.81 |       56 | 28.79%     | ok               |
|          35 | -2.43%   | 0.00%              | -3.61% |    -0.82 |       56 | 36.77%     | ok               |
|          50 | -2.14%   | 0.00%              | -3.34% |    -0.86 |       46 | 24.79%     | ok               |

## SKY-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -34.57%  | -43.35%            | -63.86% |    -0.24 |       78 | 57.28%     | ok               |
|          30 | -40.33%  | -43.35%            | -65.07% |    -0.41 |       89 | 46.36%     | ok               |
|          35 | -40.15%  | -43.35%            | -64.96% |    -0.45 |       82 | 38.31%     | ok               |
|          25 | -47.08%  | -43.35%            | -68.23% |    -0.53 |       82 | 49.62%     | ok               |
|          20 | -52.13%  | -43.35%            | -71.26% |    -0.61 |       82 | 53.26%     | ok               |

## SLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -4.50%   | 4.93%              | -24.05% |     0.01 |       60 | 32.11%     | ok               |
|          50 | -4.90%   | 4.93%              | -26.59% |    -0.02 |       48 | 25.46%     | ok               |
|          40 | -7.16%   | 4.93%              | -27.18% |    -0.04 |       52 | 34.78%     | ok               |
|          35 | -27.39%  | 4.93%              | -42.45% |    -0.49 |       72 | 42.43%     | ok               |
|          25 | -37.44%  | 4.93%              | -52.28% |    -0.68 |       83 | 52.41%     | ok               |

## SLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 74.96%   | 31.89%             | -28.72% |     0.91 |       54 | 32.28%     | ok               |
|          45 | 71.84%   | 31.89%             | -31.33% |     0.88 |       63 | 34.11%     | ok               |
|          40 | 70.48%   | 31.89%             | -34.28% |     0.86 |       67 | 36.11%     | ok               |
|          20 | 74.53%   | 31.89%             | -37.05% |     0.85 |       70 | 47.09%     | ok               |
|          15 | 71.61%   | 31.89%             | -47.98% |     0.8  |       71 | 51.75%     | ok               |

## SMH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 79.32%   | 54.06%             | -31.01% |     0.96 |       49 | 44.76%     | ok               |
|          25 | 63.11%   | 54.06%             | -32.94% |     0.84 |       46 | 43.26%     | ok               |
|          30 | 57.87%   | 54.06%             | -33.99% |     0.8  |       52 | 41.76%     | ok               |
|          35 | 46.13%   | 54.06%             | -34.36% |     0.7  |       58 | 39.77%     | ok               |
|          45 | 37.02%   | 54.06%             | -32.24% |     0.62 |       54 | 34.11%     | ok               |

## SNX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 15.57%   | -75.21%            | -44.08% |     0.38 |       50 | 28.74%     | ok               |
|          40 | 14.24%   | -75.21%            | -29.01% |     0.36 |       48 | 24.14%     | ok               |
|          20 | 3.73%    | -75.21%            | -53.03% |     0.28 |       75 | 45.02%     | ok               |
|          30 | -8.03%   | -75.21%            | -50.74% |     0.11 |       62 | 35.25%     | ok               |
|          15 | -12.77%  | -75.21%            | -54.74% |     0.11 |       78 | 49.81%     | ok               |

## SOL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 72.70%   | -49.86%            | -40.41% |     0.85 |       52 | 40.04%     | ok               |
|          45 | 34.88%   | -49.86%            | -47.42% |     0.58 |       50 | 33.52%     | ok               |
|          35 | 32.74%   | -49.86%            | -44.32% |     0.53 |       66 | 45.79%     | ok               |
|          25 | 16.65%   | -49.86%            | -39.39% |     0.39 |       65 | 56.51%     | ok               |
|          50 | 11.79%   | -49.86%            | -46.56% |     0.33 |       54 | 27.59%     | ok               |

## SOXX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 67.44%   | 47.90%             | -39.85% |     0.84 |       55 | 43.43%     | ok               |
|          30 | 62.79%   | 47.90%             | -40.34% |     0.81 |       57 | 41.26%     | ok               |
|          35 | 61.20%   | 47.90%             | -38.63% |     0.8  |       57 | 38.94%     | ok               |
|          20 | 55.30%   | 47.90%             | -38.67% |     0.73 |       61 | 44.09%     | ok               |
|          15 | 41.01%   | 47.90%             | -37.72% |     0.59 |       79 | 47.75%     | ok               |

## SPY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 1.87%    | 29.07%             | -14.25% |     0.13 |       62 | 49.75%     | ok               |
|          15 | -0.60%   | 29.07%             | -16.80% |     0.05 |       68 | 52.75%     | ok               |
|          25 | -2.30%   | 29.07%             | -14.25% |    -0.01 |       60 | 48.59%     | ok               |
|          30 | -7.08%   | 29.07%             | -15.53% |    -0.19 |       63 | 46.09%     | ok               |
|          35 | -7.98%   | 29.07%             | -15.58% |    -0.24 |       61 | 42.93%     | ok               |

## SUSHI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -44.00%  | -74.52%            | -73.16% |    -0.38 |       75 | 38.51%     | ok               |
|          40 | -43.08%  | -74.52%            | -67.47% |    -0.43 |       70 | 32.76%     | ok               |
|          15 | -61.61%  | -74.52%            | -80.08% |    -0.57 |       83 | 55.36%     | ok               |
|          25 | -59.26%  | -74.52%            | -79.14% |    -0.62 |       80 | 48.28%     | ok               |
|          20 | -61.27%  | -74.52%            | -79.50% |    -0.62 |       86 | 51.53%     | ok               |

## T Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 63.65%   | 22.12%             | -17.66% |     1.07 |       68 | 59.23%     | ok               |
|          20 | 63.77%   | 22.12%             | -18.13% |     1.06 |       70 | 61.73%     | ok               |
|          15 | 64.37%   | 22.12%             | -15.08% |     1.04 |       75 | 66.39%     | ok               |
|          30 | 52.29%   | 22.12%             | -17.01% |     0.94 |       68 | 57.07%     | ok               |
|          35 | 34.38%   | 22.12%             | -14.49% |     0.71 |       76 | 52.41%     | ok               |

## TGT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -3.11%   | 15.80%             | -33.35% |     0.04 |       68 | 41.93%     | ok               |
|          30 | -2.84%   | 15.80%             | -32.83% |     0.04 |       60 | 38.60%     | ok               |
|          20 | -6.30%   | 15.80%             | -35.62% |    -0.01 |       84 | 46.42%     | ok               |
|          45 | -6.48%   | 15.80%             | -26.12% |    -0.07 |       50 | 30.12%     | ok               |
|          15 | -12.76%  | 15.80%             | -35.05% |    -0.13 |       70 | 51.25%     | ok               |

## TIA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -31.55%  | -79.49%            | -66.82% |     0.06 |       93 | 60.54%     | ok               |
|          35 | -25.07%  | -79.49%            | -65.55% |    -0.03 |       76 | 37.55%     | ok               |
|          20 | -37.18%  | -79.49%            | -68.67% |    -0.05 |       87 | 54.60%     | ok               |
|          25 | -35.26%  | -79.49%            | -69.36% |    -0.05 |       90 | 49.43%     | ok               |
|          30 | -43.41%  | -79.49%            | -74.75% |    -0.19 |       85 | 44.25%     | ok               |

## TLT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -6.80%   | -11.34%            | -12.00% |    -0.75 |       32 | 16.81%     | ok               |
|          40 | -14.89%  | -11.34%            | -18.39% |    -1.3  |       50 | 25.96%     | ok               |
|          45 | -13.31%  | -11.34%            | -15.44% |    -1.36 |       44 | 20.80%     | ok               |
|          30 | -22.94%  | -11.34%            | -23.57% |    -1.73 |       70 | 35.44%     | ok               |
|          35 | -21.28%  | -11.34%            | -21.92% |    -1.76 |       66 | 30.45%     | ok               |

## TMO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 45.90%   | 27.83%             | -8.17%  |     0.99 |       50 | 35.11%     | ok               |
|          45 | 46.19%   | 27.83%             | -9.69%  |     0.95 |       52 | 39.93%     | ok               |
|          40 | 38.13%   | 27.83%             | -11.54% |     0.81 |       59 | 44.93%     | ok               |
|          35 | 40.96%   | 27.83%             | -13.84% |     0.8  |       67 | 50.25%     | ok               |
|          30 | 39.00%   | 27.83%             | -18.85% |     0.74 |       67 | 56.07%     | ok               |

## TMUS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -7.36%   | -7.21%             | -41.04% |    -0.04 |       70 | 58.74%     | ok               |
|          30 | -7.71%   | -7.21%             | -33.05% |    -0.07 |       74 | 45.76%     | ok               |
|          25 | -10.33%  | -7.21%             | -39.29% |    -0.12 |       75 | 48.75%     | ok               |
|          20 | -11.85%  | -7.21%             | -39.79% |    -0.14 |       74 | 52.91%     | ok               |
|          50 | -9.72%   | -7.21%             | -32.38% |    -0.2  |       56 | 31.61%     | ok               |

## TRX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 16.98%   | 11.41%             | -20.10% |     0.58 |       52 | 41.00%     | ok               |
|          35 | 17.45%   | 11.41%             | -21.45% |     0.58 |       60 | 48.08%     | ok               |
|          30 | 15.38%   | 11.41%             | -22.96% |     0.51 |       60 | 50.38%     | ok               |
|          50 | 11.60%   | 11.41%             | -19.79% |     0.46 |       46 | 34.48%     | ok               |
|          20 | 14.09%   | 11.41%             | -26.11% |     0.45 |       60 | 56.32%     | ok               |

## TSLA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 22.19%   | 50.29%             | -30.57% |     0.42 |       62 | 29.28%     | ok               |
|          40 | -8.09%   | 50.29%             | -50.11% |     0.1  |       61 | 34.28%     | ok               |
|          45 | -22.72%  | 50.29%             | -52.01% |    -0.1  |       67 | 31.78%     | ok               |
|          35 | -38.38%  | 50.29%             | -58.86% |    -0.32 |       72 | 36.61%     | ok               |
|          25 | -48.71%  | 50.29%             | -54.86% |    -0.47 |       70 | 43.59%     | ok               |

## TXN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -3.96%   | 34.11%             | -43.95% |     0.06 |       70 | 31.78%     | ok               |
|          35 | -17.67%  | 34.11%             | -42.08% |    -0.15 |       84 | 45.42%     | ok               |
|          20 | -23.53%  | 34.11%             | -37.19% |    -0.19 |       74 | 55.24%     | ok               |
|          15 | -25.27%  | 34.11%             | -38.02% |    -0.21 |       79 | 59.57%     | ok               |
|          40 | -22.70%  | 34.11%             | -44.52% |    -0.25 |       78 | 42.93%     | ok               |

## UNH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 47.68%   | -29.25%            | -26.31% |     0.7  |       72 | 48.09%     | ok               |
|          35 | 45.31%   | -29.25%            | -27.21% |     0.68 |       67 | 43.09%     | ok               |
|          15 | 45.14%   | -29.25%            | -26.07% |     0.65 |       78 | 62.90%     | ok               |
|          20 | 42.49%   | -29.25%            | -26.96% |     0.63 |       73 | 56.57%     | ok               |
|          25 | 38.41%   | -29.25%            | -24.25% |     0.61 |       72 | 52.91%     | ok               |

## UNI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 161.21%  | -30.84%            | -22.21% |     1.25 |       54 | 27.01%     | ok               |
|          45 | 145.39%  | -30.84%            | -29.39% |     1.13 |       60 | 35.25%     | ok               |
|          40 | 106.92%  | -30.84%            | -44.76% |     0.94 |       64 | 42.34%     | ok               |
|          35 | 79.27%   | -30.84%            | -49.23% |     0.79 |       62 | 46.93%     | ok               |
|          30 | 9.96%    | -30.84%            | -61.11% |     0.37 |       80 | 51.15%     | ok               |

## UPS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -16.78%  | -17.75%            | -24.11% |    -0.31 |       44 | 25.29%     | ok               |
|          40 | -18.72%  | -17.75%            | -25.98% |    -0.31 |       60 | 34.78%     | ok               |
|          20 | -27.16%  | -17.75%            | -33.47% |    -0.43 |       80 | 51.75%     | ok               |
|          15 | -29.56%  | -17.75%            | -35.66% |    -0.48 |       82 | 55.24%     | ok               |
|          35 | -30.72%  | -17.75%            | -32.44% |    -0.57 |       67 | 38.94%     | ok               |

## USO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 6.75%    | 73.95%             | -37.20% |     0.24 |       67 | 42.43%     | ok               |
|          20 | 5.22%    | 73.95%             | -40.55% |     0.22 |       73 | 38.77%     | ok               |
|          45 | 1.99%    | 73.95%             | -33.48% |     0.17 |       48 | 24.96%     | ok               |
|          25 | -6.38%   | 73.95%             | -41.74% |     0.06 |       73 | 36.11%     | ok               |
|          50 | -5.04%   | 73.95%             | -28.71% |     0.04 |       50 | 23.13%     | ok               |

## VEA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 2.64%    | 30.66%             | -16.89% |     0.15 |       56 | 49.75%     | ok               |
|          20 | -1.00%   | 30.66%             | -17.40% |     0.01 |       57 | 47.25%     | ok               |
|          25 | -5.88%   | 30.66%             | -18.46% |    -0.19 |       59 | 45.26%     | ok               |
|          30 | -7.02%   | 30.66%             | -18.84% |    -0.25 |       64 | 41.26%     | ok               |
|          35 | -7.67%   | 30.66%             | -17.88% |    -0.29 |       50 | 38.77%     | ok               |

## VIXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -55.17%  | -42.94%            | -69.78% |    -0.6  |       36 | 8.99%      | ok               |
|          45 | -64.78%  | -42.94%            | -75.37% |    -0.8  |       56 | 13.98%     | ok               |
|          40 | -73.62%  | -42.94%            | -81.61% |    -0.97 |       72 | 18.14%     | ok               |
|          35 | -80.65%  | -42.94%            | -85.76% |    -1.13 |       98 | 24.96%     | ok               |
|          30 | -84.51%  | -42.94%            | -91.82% |    -1.13 |      104 | 32.45%     | ok               |

## VNQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -10.02%  | 14.18%             | -22.16% |    -0.35 |       68 | 43.43%     | ok               |
|          50 | -9.28%   | 14.18%             | -19.06% |    -0.4  |       48 | 25.46%     | ok               |
|          45 | -9.60%   | 14.18%             | -20.96% |    -0.4  |       58 | 28.45%     | ok               |
|          30 | -13.27%  | 14.18%             | -24.66% |    -0.5  |       68 | 40.77%     | ok               |
|          20 | -13.85%  | 14.18%             | -23.83% |    -0.5  |       74 | 46.26%     | ok               |

## VTI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 2.91%    | 29.62%             | -13.96% |     0.16 |       67 | 50.08%     | ok               |
|          15 | -4.61%   | 29.62%             | -15.70% |    -0.08 |       68 | 52.91%     | ok               |
|          25 | -8.63%   | 29.62%             | -16.10% |    -0.24 |       59 | 48.09%     | ok               |
|          40 | -12.31%  | 29.62%             | -20.44% |    -0.46 |       68 | 38.10%     | ok               |
|          35 | -14.11%  | 29.62%             | -20.89% |    -0.51 |       64 | 42.60%     | ok               |

## VWO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -8.00%   | 18.18%             | -24.01% |    -0.19 |       74 | 47.59%     | ok               |
|          20 | -8.02%   | 18.18%             | -26.14% |    -0.19 |       69 | 45.59%     | ok               |
|          45 | -9.18%   | 18.18%             | -23.20% |    -0.28 |       58 | 32.61%     | ok               |
|          40 | -10.02%  | 18.18%             | -23.50% |    -0.3  |       68 | 35.44%     | ok               |
|          50 | -13.31%  | 18.18%             | -23.66% |    -0.46 |       58 | 29.78%     | ok               |

## VZ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -3.10%   | 13.85%             | -12.96% |    -0.04 |       56 | 28.62%     | ok               |
|          20 | -22.26%  | 13.85%             | -35.02% |    -0.43 |       80 | 52.75%     | ok               |
|          25 | -19.09%  | 13.85%             | -26.32% |    -0.47 |       83 | 47.75%     | ok               |
|          35 | -18.88%  | 13.85%             | -26.97% |    -0.55 |       64 | 39.10%     | ok               |
|          45 | -18.61%  | 13.85%             | -26.23% |    -0.57 |       72 | 32.95%     | ok               |

## WFC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -11.23%  | 37.16%             | -25.34% |    -0.18 |       75 | 43.43%     | ok               |
|          50 | -10.87%  | 37.16%             | -20.08% |    -0.29 |       58 | 32.45%     | ok               |
|          40 | -15.18%  | 37.16%             | -24.30% |    -0.38 |       68 | 39.93%     | ok               |
|          30 | -21.76%  | 37.16%             | -30.70% |    -0.39 |       80 | 47.09%     | ok               |
|          20 | -24.50%  | 37.16%             | -32.64% |    -0.41 |       80 | 53.41%     | ok               |

## WIF-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 61.24%   | -84.18%            | -40.67% |     0.67 |       67 | 51.92%     | ok               |
|          25 | 37.52%   | -84.18%            | -44.74% |     0.55 |       63 | 47.89%     | ok               |
|          15 | 26.01%   | -84.18%            | -46.21% |     0.48 |       77 | 55.17%     | ok               |
|          30 | 8.22%    | -84.18%            | -48.32% |     0.34 |       64 | 45.21%     | ok               |
|          35 | 8.25%    | -84.18%            | -52.54% |     0.32 |       62 | 38.89%     | ok               |

## WMT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 38.69%   | 89.35%             | -12.87% |     1.12 |       36 | 35.61%     | ok               |
|          45 | 37.65%   | 89.35%             | -14.82% |     1.05 |       42 | 38.10%     | ok               |
|          35 | 33.65%   | 89.35%             | -18.90% |     0.91 |       60 | 45.59%     | ok               |
|          40 | 27.50%   | 89.35%             | -19.17% |     0.8  |       52 | 39.93%     | ok               |
|          15 | 14.35%   | 89.35%             | -26.82% |     0.39 |       82 | 60.07%     | ok               |

## XBI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 8.56%    | 67.97%             | -16.08% |     0.3  |       50 | 33.11%     | ok               |
|          45 | 4.44%    | 67.97%             | -17.35% |     0.19 |       48 | 30.62%     | ok               |
|          35 | -1.47%   | 67.97%             | -17.82% |     0.04 |       58 | 35.77%     | ok               |
|          30 | -3.53%   | 67.97%             | -19.01% |    -0.01 |       60 | 37.27%     | ok               |
|          25 | -5.00%   | 67.97%             | -24.31% |    -0.04 |       70 | 39.77%     | ok               |

## XLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -1.61%   | 16.18%             | -17.65% |     0    |       54 | 29.62%     | ok               |
|          50 | -1.50%   | 16.18%             | -16.42% |    -0    |       42 | 24.79%     | ok               |
|          35 | -5.31%   | 16.18%             | -20.92% |    -0.13 |       56 | 32.78%     | ok               |
|          45 | -6.51%   | 16.18%             | -17.76% |    -0.2  |       42 | 26.62%     | ok               |
|          25 | -8.22%   | 16.18%             | -20.49% |    -0.22 |       60 | 39.10%     | ok               |

## XLC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 0.07%    | 21.17%             | -12.48% |     0.05 |       64 | 35.77%     | ok               |
|          30 | -1.20%   | 21.17%             | -12.33% |     0.02 |       63 | 47.92%     | ok               |
|          45 | -2.74%   | 21.17%             | -13.21% |    -0.05 |       60 | 38.60%     | ok               |
|          25 | -4.41%   | 21.17%             | -15.42% |    -0.08 |       66 | 50.42%     | ok               |
|          20 | -4.95%   | 21.17%             | -15.26% |    -0.09 |       69 | 52.91%     | ok               |

## XLE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.76%   | 36.01%             | -25.98% |     0.06 |       58 | 38.60%     | ok               |
|          45 | -2.44%   | 36.01%             | -28.46% |     0.01 |       60 | 41.10%     | ok               |
|          30 | -3.75%   | 36.01%             | -34.77% |    -0.01 |       72 | 48.42%     | ok               |
|          20 | -8.20%   | 36.01%             | -34.45% |    -0.1  |       81 | 53.91%     | ok               |
|          15 | -9.38%   | 36.01%             | -36.62% |    -0.12 |       97 | 57.90%     | ok               |

## XLF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 1.12%    | 36.40%             | -20.19% |     0.1  |       72 | 57.74%     | ok               |
|          20 | 0.50%    | 36.40%             | -18.63% |     0.08 |       72 | 55.07%     | ok               |
|          30 | -5.19%   | 36.40%             | -23.61% |    -0.12 |       78 | 49.75%     | ok               |
|          25 | -6.52%   | 36.40%             | -23.22% |    -0.16 |       79 | 51.91%     | ok               |
|          35 | -12.96%  | 36.40%             | -24.48% |    -0.44 |       70 | 46.26%     | ok               |

## XLI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 3.56%    | 34.26%             | -9.33%  |     0.18 |       83 | 51.41%     | ok               |
|          20 | -3.75%   | 34.26%             | -12.74% |    -0.08 |       77 | 46.42%     | ok               |
|          45 | -8.73%   | 34.26%             | -16.29% |    -0.36 |       72 | 32.95%     | ok               |
|          40 | -9.90%   | 34.26%             | -14.16% |    -0.39 |       80 | 35.44%     | ok               |
|          25 | -11.31%  | 34.26%             | -17.60% |    -0.41 |       78 | 44.09%     | ok               |

## XLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 51.33%   | 32.89%             | -18.51% |     0.87 |       54 | 50.75%     | ok               |
|          25 | 41.38%   | 32.89%             | -15.06% |     0.79 |       46 | 45.09%     | ok               |
|          20 | 41.93%   | 32.89%             | -19.61% |     0.78 |       56 | 47.59%     | ok               |
|          30 | 32.92%   | 32.89%             | -19.09% |     0.68 |       46 | 43.76%     | ok               |
|          35 | 12.92%   | 32.89%             | -21.79% |     0.36 |       62 | 40.77%     | ok               |

## XLM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 17.60%   | -47.85%            | -61.51% |     0.4  |       72 | 61.88%     | ok               |
|          25 | 16.26%   | -47.85%            | -53.31% |     0.38 |       75 | 52.87%     | ok               |
|          45 | 14.81%   | -47.85%            | -49.94% |     0.36 |       62 | 29.12%     | ok               |
|          40 | 9.03%    | -47.85%            | -53.91% |     0.31 |       70 | 37.16%     | ok               |
|          30 | 1.26%    | -47.85%            | -56.32% |     0.23 |       75 | 50.38%     | ok               |

## XLP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          45 | 21.78%   | 19.47%             | -5.66% |     1.06 |       48 | 33.28%     | ok               |
|          50 | 18.91%   | 19.47%             | -6.08% |     0.96 |       54 | 31.45%     | ok               |
|          40 | 19.52%   | 19.47%             | -7.32% |     0.95 |       64 | 36.61%     | ok               |
|          35 | 16.34%   | 19.47%             | -8.39% |     0.79 |       62 | 39.60%     | ok               |
|          30 | 15.23%   | 19.47%             | -8.96% |     0.73 |       65 | 41.93%     | ok               |

## XLU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 4.81%    | 27.11%             | -14.03% |     0.28 |       56 | 30.45%     | ok               |
|          45 | 3.66%    | 27.11%             | -14.97% |     0.22 |       60 | 31.61%     | ok               |
|          35 | 1.48%    | 27.11%             | -19.71% |     0.11 |       68 | 38.27%     | ok               |
|          40 | -0.17%   | 27.11%             | -16.41% |     0.03 |       72 | 34.44%     | ok               |
|          30 | -2.91%   | 27.11%             | -20.40% |    -0.08 |       73 | 41.76%     | ok               |

## XLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -20.03%  | 27.33%             | -21.39% |    -0.89 |       74 | 37.77%     | ok               |
|          25 | -21.11%  | 27.33%             | -22.46% |    -0.93 |       76 | 39.77%     | ok               |
|          15 | -23.55%  | 27.33%             | -25.92% |    -0.99 |       85 | 43.93%     | ok               |
|          20 | -25.18%  | 27.33%             | -25.80% |    -1.12 |       79 | 41.43%     | ok               |
|          35 | -24.01%  | 27.33%             | -25.29% |    -1.14 |       68 | 34.78%     | ok               |

## XLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -10.85%  | 24.07%             | -18.98% |    -0.21 |       82 | 54.08%     | ok               |
|          20 | -15.57%  | 24.07%             | -22.50% |    -0.37 |       78 | 50.75%     | ok               |
|          30 | -15.52%  | 24.07%             | -22.28% |    -0.41 |       83 | 47.25%     | ok               |
|          50 | -12.11%  | 24.07%             | -17.00% |    -0.44 |       66 | 31.45%     | ok               |
|          25 | -18.95%  | 24.07%             | -24.73% |    -0.5  |       77 | 49.08%     | ok               |

## XOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 5.44%    | 40.92%             | -19.90% |     0.22 |       59 | 38.27%     | ok               |
|          30 | 4.26%    | 40.92%             | -20.29% |     0.19 |       59 | 37.44%     | ok               |
|          50 | 3.48%    | 40.92%             | -21.35% |     0.17 |       40 | 29.28%     | ok               |
|          45 | -1.68%   | 40.92%             | -23.33% |     0.03 |       44 | 30.45%     | ok               |
|          40 | -3.14%   | 40.92%             | -21.45% |    -0.01 |       54 | 33.78%     | ok               |

## XRP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 6.85%    | -55.47%            | -36.96% |     0.28 |       74 | 44.44%     | ok               |
|          45 | 7.22%    | -55.47%            | -32.85% |     0.28 |       58 | 31.42%     | ok               |
|          20 | 2.71%    | -55.47%            | -37.30% |     0.24 |       72 | 56.13%     | ok               |
|          40 | -0.60%   | -55.47%            | -36.92% |     0.18 |       68 | 37.36%     | ok               |
|          30 | -5.42%   | -55.47%            | -39.26% |     0.14 |       69 | 50.00%     | ok               |

## YFI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -42.82%  | -68.49%            | -56.38% |    -0.56 |       72 | 40.42%     | ok               |
|          25 | -46.60%  | -68.49%            | -59.28% |    -0.62 |       77 | 45.02%     | ok               |
|          35 | -44.18%  | -68.49%            | -52.46% |    -0.66 |       68 | 35.44%     | ok               |
|          40 | -42.87%  | -68.49%            | -48.77% |    -0.69 |       64 | 27.78%     | ok               |
|          15 | -53.83%  | -68.49%            | -66.02% |    -0.71 |       82 | 54.98%     | ok               |

## ZEC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 268.42%  | 1635.36%           | -30.64% |     1.23 |       42 | 27.20%     | ok               |
|          35 | 171.88%  | 1635.36%           | -50.84% |     1    |       52 | 33.14%     | ok               |
|          50 | 155.04%  | 1635.36%           | -41.34% |     0.98 |       40 | 23.18%     | ok               |
|          40 | 160.53%  | 1635.36%           | -54.22% |     0.97 |       50 | 31.23%     | ok               |
|          30 | 134.89%  | 1635.36%           | -56.50% |     0.89 |       54 | 36.02%     | ok               |
