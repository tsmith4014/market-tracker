# Market Tracker Backtest Report

_Generated: 2026-07-01T01:34:59+00:00_

## Data Sources

- Crypto: Kraken -> Coinbase -> CoinGecko OHLC -> CoinPaprika fallback chain.
- Stocks / ETFs / indices: Stooq -> Yahoo Finance fallback chain.
- Data rows are generated from real market APIs. Mock OHLCV rows are not generated.

## Data Freshness

- Rows: **92,450**
- Symbols: **161**
- Date range: **2024-02-06** to **2026-07-01**

## Latest Signals

| symbol     | date                |         close |   composite_score | signal   | data_source   |
|:-----------|:--------------------|--------------:|------------------:|:---------|:--------------|
| AAVE-USD   | 2026-07-01 00:00:00 |    85.01      |          46.6667  | LONG     | Kraken API    |
| AMAT       | 2026-06-30 00:00:00 |   723         |          69.5833  | LONG     | Yahoo Finance |
| BAC        | 2026-06-30 00:00:00 |    56.98      |          55.9167  | LONG     | Yahoo Finance |
| C          | 2026-06-30 00:00:00 |   139.96      |          51.5833  | LONG     | Yahoo Finance |
| CAT        | 2026-06-30 00:00:00 |  1064.9       |          77.4167  | LONG     | Yahoo Finance |
| DE         | 2026-06-30 00:00:00 |   634.33      |          79.0833  | LONG     | Yahoo Finance |
| DXY-INDEX  | 2026-06-30 00:00:00 |   101.293     |          80.914   | LONG     | Yahoo Finance |
| GE         | 2026-06-30 00:00:00 |   373.73      |          58.4167  | LONG     | Yahoo Finance |
| HD         | 2026-06-30 00:00:00 |   352.68      |          65.5     | LONG     | Yahoo Finance |
| IBM        | 2026-06-30 00:00:00 |   281.21      |          38.25    | LONG     | Yahoo Finance |
| ITA        | 2026-06-30 00:00:00 |   242.42      |          62.25    | LONG     | Yahoo Finance |
| JNJ        | 2026-06-30 00:00:00 |   253.97      |          74.4167  | LONG     | Yahoo Finance |
| JPM        | 2026-06-30 00:00:00 |   327.33      |          54.6667  | LONG     | Yahoo Finance |
| LLY        | 2026-06-30 00:00:00 |  1199.43      |          48.5833  | LONG     | Yahoo Finance |
| LRCX       | 2026-06-30 00:00:00 |   433.33      |          75.0833  | LONG     | Yahoo Finance |
| QQQ        | 2026-06-30 00:00:00 |   736.4       |          52.25    | LONG     | Yahoo Finance |
| RTX        | 2026-06-30 00:00:00 |   189.73      |          64.3333  | LONG     | Yahoo Finance |
| SBUX       | 2026-06-30 00:00:00 |   102.19      |          69.9167  | LONG     | Yahoo Finance |
| SCHW       | 2026-06-30 00:00:00 |    92.27      |          36.9167  | LONG     | Yahoo Finance |
| TGT        | 2026-06-30 00:00:00 |   130.61      |          48.4167  | LONG     | Yahoo Finance |
| TLT        | 2026-06-30 00:00:00 |    86.42      |          38.3333  | LONG     | Yahoo Finance |
| TMO        | 2026-06-30 00:00:00 |   501.36      |          31.0833  | LONG     | Yahoo Finance |
| TSLA       | 2026-06-30 00:00:00 |   420.6       |          49.4167  | LONG     | Yahoo Finance |
| UNH        | 2026-06-30 00:00:00 |   415.63      |          52.0833  | LONG     | Yahoo Finance |
| VTI        | 2026-06-30 00:00:00 |   370.04      |          38.25    | LONG     | Yahoo Finance |
| WFC        | 2026-06-30 00:00:00 |    82.64      |          30.0833  | LONG     | Yahoo Finance |
| XBI        | 2026-06-30 00:00:00 |   158.25      |          73.25    | LONG     | Yahoo Finance |
| XLF        | 2026-06-30 00:00:00 |    53.61      |          46.75    | LONG     | Yahoo Finance |
| XLU        | 2026-06-30 00:00:00 |    45.34      |          66.6667  | LONG     | Yahoo Finance |
| AAPL       | 2026-06-30 00:00:00 |   289.36      |         -26.0833  | NEUTRAL  | Yahoo Finance |
| ABBV       | 2026-06-30 00:00:00 |   251.64      |          48.5     | NEUTRAL  | Yahoo Finance |
| ADA-USD    | 2026-07-01 00:00:00 |     0.142951  |         -29.3333  | NEUTRAL  | Kraken API    |
| AGG        | 2026-06-30 00:00:00 |    98.98      |          29.0833  | NEUTRAL  | Yahoo Finance |
| ALGO-USD   | 2026-07-01 00:00:00 |     0.08222   |         -62.5833  | NEUTRAL  | Kraken API    |
| AMD        | 2026-06-30 00:00:00 |   580.91      |          48       | NEUTRAL  | Yahoo Finance |
| AMGN       | 2026-06-30 00:00:00 |   362.12      |          64       | NEUTRAL  | Yahoo Finance |
| AMZN       | 2026-06-30 00:00:00 |   238.34      |           9.66667 | NEUTRAL  | Yahoo Finance |
| ARB-USD    | 2026-07-01 00:00:00 |     0.0757    |         -47.25    | NEUTRAL  | Kraken API    |
| ARKK       | 2026-06-30 00:00:00 |    80.82      |          48.5833  | NEUTRAL  | Yahoo Finance |
| AVAX-USD   | 2026-07-01 00:00:00 |     6.504     |         -28.4167  | NEUTRAL  | Kraken API    |
| AVGO       | 2026-06-30 00:00:00 |   377.75      |         -24.8333  | NEUTRAL  | Yahoo Finance |
| BA         | 2026-06-30 00:00:00 |   216.47      |         -39.5833  | NEUTRAL  | Yahoo Finance |
| BCH-USD    | 2026-07-01 00:00:00 |   197.31      |         -53.25    | NEUTRAL  | Kraken API    |
| BLK        | 2026-06-30 00:00:00 |   961.56      |         -67       | NEUTRAL  | Yahoo Finance |
| BND        | 2026-06-30 00:00:00 |    73.41      |          25.5833  | NEUTRAL  | Yahoo Finance |
| BONK-USD   | 2026-07-01 00:00:00 |     4.028e-06 |         -49.25    | NEUTRAL  | Kraken API    |
| CL         | 2026-06-30 00:00:00 |    91.68      |          63.9167  | NEUTRAL  | Yahoo Finance |
| CMCSA      | 2026-06-30 00:00:00 |    24.55      |          20.4167  | NEUTRAL  | Yahoo Finance |
| COST       | 2026-06-30 00:00:00 |   935.47      |         -40       | NEUTRAL  | Yahoo Finance |
| CSCO       | 2026-06-30 00:00:00 |   117.46      |          20.0833  | NEUTRAL  | Yahoo Finance |
| DASH-USD   | 2026-07-01 00:00:00 |    31.972     |         -73.25    | NEUTRAL  | Kraken API    |
| DBC        | 2026-06-30 00:00:00 |    26.66      |         -12.4167  | NEUTRAL  | Yahoo Finance |
| DIA        | 2026-06-30 00:00:00 |   522.39      |          45.5     | NEUTRAL  | Yahoo Finance |
| DIS        | 2026-06-30 00:00:00 |    96.25      |         -60       | NEUTRAL  | Yahoo Finance |
| EEM        | 2026-06-30 00:00:00 |    68.41      |          41       | NEUTRAL  | Yahoo Finance |
| EFA        | 2026-06-30 00:00:00 |   103.88      |          28.25    | NEUTRAL  | Yahoo Finance |
| EOG        | 2026-06-30 00:00:00 |   129.73      |         -25.25    | NEUTRAL  | Yahoo Finance |
| ETC-USD    | 2026-07-01 00:00:00 |     6.786     |         -37.4167  | NEUTRAL  | Kraken API    |
| EWJ        | 2026-06-30 00:00:00 |    93.27      |          49.8333  | NEUTRAL  | Yahoo Finance |
| FCX        | 2026-06-30 00:00:00 |    62.89      |         -15.3333  | NEUTRAL  | Yahoo Finance |
| GDX        | 2026-06-30 00:00:00 |    75.45      |         -52       | NEUTRAL  | Yahoo Finance |
| GDXJ       | 2026-06-30 00:00:00 |    98.25      |         -52.3333  | NEUTRAL  | Yahoo Finance |
| GOOGL      | 2026-06-30 00:00:00 |   357.37      |         -25.3333  | NEUTRAL  | Yahoo Finance |
| GRT-USD    | 2026-07-01 00:00:00 |     0.01779   |         -38.25    | NEUTRAL  | Kraken API    |
| GS         | 2026-06-30 00:00:00 |  1011.37      |          -5.83333 | NEUTRAL  | Yahoo Finance |
| HON        | 2026-06-30 00:00:00 |   223.9       |          32.4167  | NEUTRAL  | Yahoo Finance |
| HYG        | 2026-06-30 00:00:00 |    79.97      |          25.5833  | NEUTRAL  | Yahoo Finance |
| ICP-USD    | 2026-07-01 00:00:00 |     2.065     |         -57.5833  | NEUTRAL  | Kraken API    |
| IEF        | 2026-06-30 00:00:00 |    94.57      |          25.5833  | NEUTRAL  | Yahoo Finance |
| IEMG       | 2026-06-30 00:00:00 |    82.84      |          39.25    | NEUTRAL  | Yahoo Finance |
| INJ-USD    | 2026-07-01 00:00:00 |     4.531     |         -55.8333  | NEUTRAL  | Kraken API    |
| INTC       | 2026-06-30 00:00:00 |   139.63      |          59.3333  | NEUTRAL  | Yahoo Finance |
| IWM        | 2026-06-30 00:00:00 |   300.45      |          61.5     | NEUTRAL  | Yahoo Finance |
| KO         | 2026-06-30 00:00:00 |    81.27      |          58.5     | NEUTRAL  | Yahoo Finance |
| LDO-USD    | 2026-07-01 00:00:00 |     0.238     |         -47.5     | NEUTRAL  | Kraken API    |
| LIN        | 2026-06-30 00:00:00 |   518.94      |          43.3333  | NEUTRAL  | Yahoo Finance |
| MCD        | 2026-06-30 00:00:00 |   270.31      |         -62.5     | NEUTRAL  | Yahoo Finance |
| META       | 2026-06-30 00:00:00 |   563.29      |         -65.6667  | NEUTRAL  | Yahoo Finance |
| MPC        | 2026-06-30 00:00:00 |   255.67      |          22.6667  | NEUTRAL  | Yahoo Finance |
| MRK        | 2026-06-30 00:00:00 |   128.5       |          65.3333  | NEUTRAL  | Yahoo Finance |
| MS         | 2026-06-30 00:00:00 |   209.04      |          23.4167  | NEUTRAL  | Yahoo Finance |
| MU         | 2026-06-30 00:00:00 |  1154.29      |          38.1667  | NEUTRAL  | Yahoo Finance |
| NEAR-USD   | 2026-07-01 00:00:00 |     1.7516    |         -60.8333  | NEUTRAL  | Kraken API    |
| NEM        | 2026-06-30 00:00:00 |    93.4       |         -64.5     | NEUTRAL  | Yahoo Finance |
| NKE        | 2026-06-30 00:00:00 |    41.05      |         -66.25    | NEUTRAL  | Yahoo Finance |
| OP-USD     | 2026-07-01 00:00:00 |     0.0951    |         -62.5833  | NEUTRAL  | Kraken API    |
| PEP        | 2026-06-30 00:00:00 |   135.4       |         -61.6667  | NEUTRAL  | Yahoo Finance |
| PG         | 2026-06-30 00:00:00 |   146.64      |         -18.0833  | NEUTRAL  | Yahoo Finance |
| PM         | 2026-06-30 00:00:00 |   180.91      |          50.3333  | NEUTRAL  | Yahoo Finance |
| POL-USD    | 2026-07-01 00:00:00 |     0.06837   |         -62.5833  | NEUTRAL  | Kraken API    |
| QCOM       | 2026-06-30 00:00:00 |   184.79      |         -23.5833  | NEUTRAL  | Yahoo Finance |
| SHY        | 2026-06-30 00:00:00 |    82.11      |          -4.75    | NEUTRAL  | Yahoo Finance |
| SKY-USD    | 2026-07-01 00:00:00 |     0.05204   |         -52.4167  | NEUTRAL  | Kraken API    |
| SMH        | 2026-06-30 00:00:00 |   655.89      |          37.6667  | NEUTRAL  | Yahoo Finance |
| SNX-USD    | 2026-07-01 00:00:00 |     0.2048    |         -65.25    | NEUTRAL  | Kraken API    |
| SOL-USD    | 2026-07-01 00:00:00 |    72.85      |           2.08333 | NEUTRAL  | Kraken API    |
| SOXX       | 2026-06-30 00:00:00 |   640.76      |          44.6667  | NEUTRAL  | Yahoo Finance |
| SPY        | 2026-06-30 00:00:00 |   746.77      |          28.75    | NEUTRAL  | Yahoo Finance |
| TRX-USD    | 2026-07-01 00:00:00 |     0.314029  |         -39.1667  | NEUTRAL  | Kraken API    |
| TXN        | 2026-06-30 00:00:00 |   298.07      |          15.8333  | NEUTRAL  | Yahoo Finance |
| UPS        | 2026-06-30 00:00:00 |   107.5       |          23.1667  | NEUTRAL  | Yahoo Finance |
| USO        | 2026-06-30 00:00:00 |   106.44      |         -17.1667  | NEUTRAL  | Yahoo Finance |
| VEA        | 2026-06-30 00:00:00 |    71.25      |          41.25    | NEUTRAL  | Yahoo Finance |
| VIXY       | 2026-06-30 00:00:00 |    21.29      |         -34.0833  | NEUTRAL  | Yahoo Finance |
| VNQ        | 2026-06-30 00:00:00 |    96.43      |           6.66667 | NEUTRAL  | Yahoo Finance |
| VWO        | 2026-06-30 00:00:00 |    59.69      |          25       | NEUTRAL  | Yahoo Finance |
| WIF-USD    | 2026-07-01 00:00:00 |     0.1622    |         -28.4167  | NEUTRAL  | Kraken API    |
| WMT        | 2026-06-30 00:00:00 |   113.26      |         -57.9167  | NEUTRAL  | Yahoo Finance |
| XLB        | 2026-06-30 00:00:00 |    50.83      |          -9.5     | NEUTRAL  | Yahoo Finance |
| XLE        | 2026-06-30 00:00:00 |    53.11      |         -17.3333  | NEUTRAL  | Yahoo Finance |
| XLI        | 2026-06-30 00:00:00 |   185.23      |          66.5     | NEUTRAL  | Yahoo Finance |
| XLK        | 2026-06-30 00:00:00 |   190.52      |          41       | NEUTRAL  | Yahoo Finance |
| XLM-USD    | 2026-07-01 00:00:00 |     0.193614  |         -14.25    | NEUTRAL  | Kraken API    |
| XLP        | 2026-06-30 00:00:00 |    83.07      |          -4.25    | NEUTRAL  | Yahoo Finance |
| XLV        | 2026-06-30 00:00:00 |   158.66      |          48.3333  | NEUTRAL  | Yahoo Finance |
| XLY        | 2026-06-30 00:00:00 |   117.28      |          38.1667  | NEUTRAL  | Yahoo Finance |
| XRP-USD    | 2026-07-01 00:00:00 |     1.02999   |         -60.5833  | NEUTRAL  | Kraken API    |
| ZEC-USD    | 2026-07-01 00:00:00 |   392.23      |         -23.25    | NEUTRAL  | Kraken API    |
| ADBE       | 2026-06-30 00:00:00 |   205.02      |         -61.4167  | SHORT    | Yahoo Finance |
| APT-USD    | 2026-07-01 00:00:00 |     0.5641    |         -31       | SHORT    | Kraken API    |
| ATOM-USD   | 2026-07-01 00:00:00 |     1.4954    |         -51.3333  | SHORT    | Kraken API    |
| BITO       | 2026-06-30 00:00:00 |     7.98      |         -48.75    | SHORT    | Yahoo Finance |
| BTC-USD    | 2026-07-01 00:00:00 | 58144.9       |         -49.3333  | SHORT    | Kraken API    |
| COMP-USD   | 2026-07-01 00:00:00 |    15.03      |         -51.3333  | SHORT    | Kraken API    |
| COP        | 2026-06-30 00:00:00 |   103.96      |         -47.5833  | SHORT    | Yahoo Finance |
| CRM        | 2026-06-30 00:00:00 |   156.66      |         -61.4167  | SHORT    | Yahoo Finance |
| CRV-USD    | 2026-07-01 00:00:00 |     0.18322   |         -53.3333  | SHORT    | Kraken API    |
| CVX        | 2026-06-30 00:00:00 |   165.76      |         -48.0833  | SHORT    | Yahoo Finance |
| DOGE-USD   | 2026-07-01 00:00:00 |     0.0711729 |         -51.3333  | SHORT    | Kraken API    |
| DOT-USD    | 2026-07-01 00:00:00 |     0.8162    |         -51.3333  | SHORT    | Kraken API    |
| ETH-USD    | 2026-07-01 00:00:00 |  1562.59      |         -57.25    | SHORT    | Kraken API    |
| FET-USD    | 2026-07-01 00:00:00 |     0.1705    |         -53.3333  | SHORT    | Kraken API    |
| FIL-USD    | 2026-07-01 00:00:00 |     0.708     |         -51.3333  | SHORT    | Kraken API    |
| FXI        | 2026-06-30 00:00:00 |    31.59      |         -59.5833  | SHORT    | Yahoo Finance |
| GLD        | 2026-06-30 00:00:00 |   368.38      |         -52.75    | SHORT    | Yahoo Finance |
| HBAR-USD   | 2026-07-01 00:00:00 |     0.06897   |         -49.3333  | SHORT    | Kraken API    |
| IBIT       | 2026-06-30 00:00:00 |    33.29      |         -48.75    | SHORT    | Yahoo Finance |
| INTU       | 2026-06-30 00:00:00 |   261         |         -40.75    | SHORT    | Yahoo Finance |
| LINK-USD   | 2026-07-01 00:00:00 |     7.14316   |         -49.3333  | SHORT    | Kraken API    |
| LTC-USD    | 2026-07-01 00:00:00 |    41.76      |         -32.6667  | SHORT    | Kraken API    |
| MSFT       | 2026-06-30 00:00:00 |   373.02      |         -54.0833  | SHORT    | Yahoo Finance |
| NFLX       | 2026-06-30 00:00:00 |    71.4       |         -56.5833  | SHORT    | Yahoo Finance |
| NOW        | 2026-06-30 00:00:00 |    99.28      |         -55.5833  | SHORT    | Yahoo Finance |
| NVDA       | 2026-06-30 00:00:00 |   200.09      |         -24       | SHORT    | Yahoo Finance |
| ORCL       | 2026-06-30 00:00:00 |   146.55      |         -65.0833  | SHORT    | Yahoo Finance |
| OXY        | 2026-06-30 00:00:00 |    48.57      |         -50.0833  | SHORT    | Yahoo Finance |
| PEPE-USD   | 2026-07-01 00:00:00 |     2.293e-06 |         -53.3333  | SHORT    | Kraken API    |
| PFE        | 2026-06-30 00:00:00 |    24.08      |         -44.75    | SHORT    | Yahoo Finance |
| RENDER-USD | 2026-07-01 00:00:00 |     1.487     |         -51.3333  | SHORT    | Kraken API    |
| SHIB-USD   | 2026-07-01 00:00:00 |     4.166e-06 |         -51.3333  | SHORT    | Kraken API    |
| SLB        | 2026-06-30 00:00:00 |    46.49      |         -47.5833  | SHORT    | Yahoo Finance |
| SLV        | 2026-06-30 00:00:00 |    53.47      |         -50.5833  | SHORT    | Yahoo Finance |
| SUSHI-USD  | 2026-07-01 00:00:00 |     0.1465    |         -53.3333  | SHORT    | Kraken API    |
| T          | 2026-06-30 00:00:00 |    20.7       |         -50.5     | SHORT    | Yahoo Finance |
| TIA-USD    | 2026-07-01 00:00:00 |     0.3517    |         -52       | SHORT    | Kraken API    |
| TMUS       | 2026-06-30 00:00:00 |   167.73      |         -50.4167  | SHORT    | Yahoo Finance |
| UNI-USD    | 2026-07-01 00:00:00 |     2.7734    |         -53.3333  | SHORT    | Kraken API    |
| VZ         | 2026-06-30 00:00:00 |    42.34      |         -43.1667  | SHORT    | Yahoo Finance |
| XLC        | 2026-06-30 00:00:00 |   107.13      |         -51.25    | SHORT    | Yahoo Finance |
| XOM        | 2026-06-30 00:00:00 |   136.72      |         -40.1667  | SHORT    | Yahoo Finance |
| YFI-USD    | 2026-07-01 00:00:00 |  1595.6       |         -53.8333  | SHORT    | Kraken API    |

## Edge Summary

- Symbols with trades: **160** of 160
- Beat buy-and-hold: **36.25%** of traded symbols
- Positive return: **34.38%** of traded symbols
- Median strategy return: **-8.12%** (benchmark **13.50%**)
- Median excess vs benchmark: **-24.29%**
- Median Sharpe: **-0.05**
- Median exposure: **44.60%**

> Edge is real only if both _beat buy-and-hold_ and _median excess_ are convincingly positive across many symbols. Treat a single high-return symbol as noise.

## Portfolio Backtest

Actual capital-allocation books (not per-symbol averages). Benchmarks: `equal_weight_buyhold` (whole tracked universe), `spy_buyhold` (100% SPY), and `sixty_forty` (60% SPY / 40% AGG). `high_conf_voltarget` inverse-vol-weights the HIGH-confidence book; `conviction_long_short` is market-neutral. Judge on **Sharpe** and **max_drawdown** out-of-sample, not raw return: a fully-invested long book wins on return in a bull market but carries all the risk.

| strategy              | scope         | ann_return   | ann_vol   |   sharpe | max_drawdown   | total_return   |   avg_gross_exposure |
|:----------------------|:--------------|:-------------|:----------|---------:|:---------------|:---------------|---------------------:|
| equal_weight_buyhold  | full          | -8.45%       | 33.36%    |    -0.25 | -53.38%        | -34.84%        |                 1    |
| equal_weight_buyhold  | out_of_sample | -16.31%      | 34.07%    |    -0.48 | -39.63%        | -21.02%        |                 1    |
| all_signals_ew        | full          | -9.20%       | 28.18%    |    -0.33 | -59.74%        | -33.04%        |                 1    |
| all_signals_ew        | out_of_sample | 8.95%        | 28.54%    |     0.31 | -21.47%        | 5.38%          |                 1    |
| high_conf_ew          | full          | 6.23%        | 32.22%    |     0.19 | -44.22%        | 3.43%          |                 0.89 |
| high_conf_ew          | out_of_sample | 10.54%       | 35.06%    |     0.3  | -19.36%        | 4.97%          |                 0.89 |
| high_conf_voltarget   | full          | 6.75%        | 29.80%    |     0.23 | -36.20%        | 7.56%          |                 0.89 |
| high_conf_voltarget   | out_of_sample | 5.55%        | 32.74%    |     0.17 | -16.94%        | 0.35%          |                 0.89 |
| conviction_long_short | full          | -11.42%      | 23.49%    |    -0.49 | -40.29%        | -35.09%        |                 0.97 |
| conviction_long_short | out_of_sample | -9.91%       | 26.77%    |    -0.37 | -21.16%        | -13.43%        |                 0.97 |
| spy_buyhold           | full          | 7.44%        | 13.37%    |     0.56 | -17.81%        | 22.06%         |                 0.79 |
| spy_buyhold           | out_of_sample | -4.59%       | 10.12%    |    -0.45 | -14.83%        | -5.30%         |                 0.79 |
| sixty_forty           | full          | 4.35%        | 8.47%     |     0.51 | -10.80%        | 12.90%         |                 0.79 |
| sixty_forty           | out_of_sample | -3.63%       | 6.57%     |    -0.55 | -10.06%        | -4.02%         |                 0.79 |

## Walk-Forward Robustness

Each book measured across contiguous time folds (each a different regime). A book has durable edge only if `mean_sharpe` is positive, `min_sharpe` isn't deeply negative, and `pct_positive_folds` is high — a single great fold doesn't count. `fold_sharpes` lists each fold oldest-to-newest.

| strategy              |   n_folds |   mean_sharpe |   median_sharpe |   min_sharpe | pct_positive_folds   | mean_return   | fold_sharpes                  |
|:----------------------|----------:|--------------:|----------------:|-------------:|:---------------------|:--------------|:------------------------------|
| equal_weight_buyhold  |         5 |          0.03 |           -0.1  |        -1.44 | 40.00%               | -6.59%        | 1.66;-1.44;0.56;-0.55;-0.10   |
| all_signals_ew        |         5 |         -0.21 |            0.2  |        -1.3  | 60.00%               | -6.93%        | 0.27;0.20;-1.30;-0.62;0.40    |
| high_conf_ew          |         5 |          0.4  |            0.6  |        -1    | 80.00%               | 1.70%         | 1.29;0.60;-1.00;0.39;0.70     |
| high_conf_voltarget   |         5 |          0.53 |            0.52 |        -1.13 | 80.00%               | 2.57%         | 2.19;0.85;-1.13;0.52;0.21     |
| conviction_long_short |         5 |         -0.54 |           -0.31 |        -1.49 | 0.00%                | -8.17%        | -1.49;-0.31;-0.30;-0.36;-0.23 |
| spy_buyhold           |         5 |          0.5  |            0.5  |        -0.26 | 60.00%               | 4.22%         | 1.71;0.50;0.64;-0.11;-0.26    |
| sixty_forty           |         5 |          0.44 |            0.17 |        -0.43 | 60.00%               | 2.54%         | 1.87;0.17;0.66;-0.07;-0.43    |

## Strategy Comparison

Each decision rule backtested over the same data. `out_of_sample` is the most recent ~35% of each symbol's history (unseen tail). A rule has real edge only if `median_excess` and `beat_benchmark_pct` stay positive out-of-sample, not just full-sample.

| strategy        | scope         |   symbols | beat_benchmark_pct   | positive_pct   | median_return   | median_benchmark   | median_excess   |   median_sharpe |   total_trades |
|:----------------|:--------------|----------:|:---------------------|:---------------|:----------------|:-------------------|:----------------|----------------:|---------------:|
| trend           | full          |       160 | 36.25%               | 34.38%         | -8.12%          | 13.50%             | -24.29%         |           -0.05 |          11239 |
| trend           | out_of_sample |       160 | 43.12%               | 53.75%         | 2.60%           | 2.64%              | -4.89%          |            0.31 |           3902 |
| mean_reversion  | full          |       157 | 42.04%               | 49.68%         | -0.03%          | 12.44%             | -14.43%         |            0.01 |           1254 |
| mean_reversion  | out_of_sample |       127 | 48.82%               | 58.27%         | 0.33%           | -0.45%             | -1.50%          |            0.65 |            478 |
| regime_adaptive | full          |       160 | 36.88%               | 35.62%         | -8.37%          | 13.50%             | -23.64%         |           -0.06 |          11504 |
| regime_adaptive | out_of_sample |       160 | 43.75%               | 54.37%         | 2.60%           | 2.64%              | -5.78%          |            0.3  |           3997 |

## Signal Calibration

Realized forward return in the signal's direction, grouped by confidence. HIGH should outrank LOW for the confidence score to be meaningful.

| confidence_level   |   horizon |     n | mean_return   | median_return   | win_rate   |
|:-------------------|----------:|------:|:--------------|:----------------|:-----------|
| HIGH               |         5 |  8057 | 0.18%         | 0.13%           | 52.18%     |
| MEDIUM             |         5 | 29275 | 0.08%         | 0.11%           | 51.21%     |
| LOW                |         5 |  3282 | -0.60%        | -0.51%          | 44.94%     |
| ALL                |         5 | 40614 | 0.05%         | 0.07%           | 50.89%     |
| HIGH               |        10 |  8013 | 0.49%         | 0.18%           | 52.10%     |
| MEDIUM             |        10 | 29098 | 0.26%         | 0.17%           | 51.43%     |
| LOW                |        10 |  3268 | -0.90%        | -0.73%          | 45.26%     |
| ALL                |        10 | 40379 | 0.22%         | 0.12%           | 51.06%     |
| HIGH               |        20 |  7947 | 0.87%         | 0.43%           | 53.42%     |
| MEDIUM             |        20 | 28678 | 0.94%         | 0.66%           | 53.83%     |
| LOW                |        20 |  3228 | -0.62%        | -0.48%          | 47.30%     |
| ALL                |        20 | 39853 | 0.80%         | 0.54%           | 53.22%     |

## Backtest Summary

### Data Quality / Signal Availability

- **ok**: 160 symbols

| symbol     |   trades | return   | benchmark_return   | mdd     |   sharpe | exposure   | skipped_reason   |
|:-----------|---------:|:---------|:-------------------|:--------|---------:|:-----------|:-----------------|
| AAPL       |       63 | 11.48%   | 52.86%             | -20.65% |     0.33 | 48.42%     | ok               |
| AAVE-USD   |       74 | -54.03%  | -73.13%            | -68.26% |    -0.54 | 36.59%     | ok               |
| ABBV       |       64 | -18.51%  | 45.21%             | -30.55% |    -0.39 | 47.42%     | ok               |
| ADA-USD    |       88 | -82.30%  | -85.00%            | -89.12% |    -0.64 | 46.55%     | ok               |
| ADBE       |       68 | -23.71%  | -66.23%            | -37.27% |    -0.25 | 57.40%     | ok               |
| AGG        |       67 | -6.37%   | 0.84%              | -9.93%  |    -1.06 | 30.95%     | ok               |
| ALGO-USD   |       86 | -50.43%  | -78.45%            | -53.13% |    -0.57 | 38.12%     | ok               |
| AMAT       |       69 | -0.98%   | 328.57%            | -57.21% |     0.17 | 53.41%     | ok               |
| AMD        |       56 | 6.87%    | 246.03%            | -44.76% |     0.28 | 36.77%     | ok               |
| AMGN       |       71 | -20.87%  | 14.57%             | -34.14% |    -0.42 | 46.42%     | ok               |
| AMZN       |       78 | -37.01%  | 40.90%             | -42.48% |    -1.1  | 38.44%     | ok               |
| APT-USD    |       76 | -29.03%  | -92.79%            | -69.96% |    -0.04 | 44.06%     | ok               |
| ARB-USD    |       68 | -0.31%   | -88.78%            | -62.67% |     0.24 | 39.27%     | ok               |
| ARKK       |       79 | -30.02%  | 73.06%             | -32.63% |    -0.5  | 38.94%     | ok               |
| ATOM-USD   |       90 | -65.53%  | -75.43%            | -73.34% |    -1.04 | 45.40%     | ok               |
| AVAX-USD   |       74 | -32.75%  | -81.79%            | -60.43% |    -0.21 | 39.85%     | ok               |
| AVGO       |       62 | 27.56%   | 208.96%            | -35.76% |     0.46 | 44.26%     | ok               |
| BA         |       67 | 7.60%    | 3.78%              | -30.56% |     0.25 | 49.25%     | ok               |
| BAC        |       78 | -12.28%  | 72.46%             | -26.30% |    -0.27 | 47.92%     | ok               |
| BCH-USD    |       78 | -3.13%   | -53.61%            | -54.26% |     0.18 | 49.62%     | ok               |
| BITO       |       78 | 14.25%   | -60.92%            | -42.82% |     0.33 | 41.76%     | ok               |
| BLK        |       75 | -9.61%   | 22.03%             | -24.29% |    -0.22 | 43.26%     | ok               |
| BND        |       65 | -7.32%   | 0.89%              | -9.89%  |    -1.18 | 32.28%     | ok               |
| BONK-USD   |       68 | 69.11%   | -85.19%            | -43.77% |     0.72 | 41.95%     | ok               |
| BTC-USD    |       74 | 11.63%   | -43.33%            | -23.38% |     0.33 | 51.92%     | ok               |
| C          |       83 | -27.46%  | 157.52%            | -38.66% |    -0.53 | 51.75%     | ok               |
| CAT        |       72 | 38.52%   | 229.98%            | -21.02% |     0.66 | 57.07%     | ok               |
| CL         |       60 | 13.77%   | 9.48%              | -14.32% |     0.49 | 46.76%     | ok               |
| CMCSA      |       80 | -38.29%  | -41.03%            | -38.49% |    -0.99 | 43.93%     | ok               |
| COMP-USD   |       91 | -34.33%  | -79.36%            | -58.43% |    -0.17 | 46.17%     | ok               |
| COP        |       73 | -20.81%  | -6.78%             | -43.96% |    -0.36 | 40.60%     | ok               |
| COST       |       60 | 2.07%    | 31.61%             | -29.73% |     0.13 | 45.42%     | ok               |
| CRM        |       67 | -36.76%  | -45.19%            | -40.31% |    -0.75 | 43.59%     | ok               |
| CRV-USD    |       64 | 5.48%    | -76.11%            | -39.89% |     0.28 | 35.63%     | ok               |
| CSCO       |       59 | 26.60%   | 135.01%            | -21.79% |     0.56 | 50.25%     | ok               |
| CVX        |       71 | -12.12%  | 8.80%              | -26.75% |    -0.28 | 41.60%     | ok               |
| DASH-USD   |       63 | -37.83%  | -5.42%             | -64.43% |     0.03 | 31.61%     | ok               |
| DBC        |       56 | -12.95%  | 21.29%             | -25.67% |    -0.45 | 32.95%     | ok               |
| DE         |       72 | -1.11%   | 63.11%             | -25.24% |     0.07 | 46.42%     | ok               |
| DIA        |       60 | -2.08%   | 35.66%             | -12.94% |    -0.07 | 45.59%     | ok               |
| DIS        |       68 | -14.47%  | -3.06%             | -28.17% |    -0.2  | 47.59%     | ok               |
| DOGE-USD   |       78 | -17.34%  | -78.81%            | -62.31% |     0.08 | 50.19%     | ok               |
| DOT-USD    |       92 | -45.70%  | -86.78%            | -61.52% |    -0.32 | 49.23%     | ok               |
| DXY-INDEX  |       44 | -1.98%   | -0.05%             | -6.06%  |    -0.3  | 30.59%     | ok               |
| EEM        |       64 | -9.40%   | 72.84%             | -25.67% |    -0.25 | 43.43%     | ok               |
| EFA        |       62 | -9.68%   | 38.12%             | -15.14% |    -0.36 | 44.76%     | ok               |
| EOG        |       77 | -24.73%  | 15.95%             | -48.13% |    -0.54 | 46.09%     | ok               |
| ETC-USD    |       64 | -35.69%  | -74.08%            | -48.16% |    -0.51 | 31.23%     | ok               |
| ETH-USD    |       64 | 167.50%  | -51.67%            | -30.11% |     1.32 | 45.21%     | ok               |
| EWJ        |       64 | -17.65%  | 40.93%             | -30.73% |    -0.57 | 39.60%     | ok               |
| FCX        |       65 | -30.42%  | 56.56%             | -48.09% |    -0.37 | 45.26%     | ok               |
| FET-USD    |       83 | -14.01%  | -85.53%            | -54.02% |     0.16 | 40.80%     | ok               |
| FIL-USD    |       72 | -33.03%  | -85.42%            | -49.05% |    -0.28 | 33.33%     | ok               |
| FXI        |       44 | -1.22%   | 36.58%             | -23.91% |     0.06 | 29.28%     | ok               |
| GDX        |       60 | 11.28%   | 172.19%            | -34.99% |     0.3  | 48.09%     | ok               |
| GDXJ       |       68 | -23.13%  | 191.02%            | -44.93% |    -0.22 | 46.42%     | ok               |
| GE         |       74 | 25.41%   | 240.37%            | -27.82% |     0.5  | 53.41%     | ok               |
| GLD        |       48 | 28.60%   | 95.38%             | -16.63% |     0.71 | 45.92%     | ok               |
| GOOGL      |       63 | 77.86%   | 148.00%            | -20.41% |     1.16 | 53.74%     | ok               |
| GRT-USD    |       85 | -3.45%   | -90.15%            | -54.83% |     0.19 | 42.72%     | ok               |
| GS         |       76 | -2.38%   | 162.70%            | -22.13% |     0.05 | 52.08%     | ok               |
| HD         |       73 | -4.02%   | -1.00%             | -18.58% |    -0.03 | 43.59%     | ok               |
| HON        |       93 | -26.82%  | 22.68%             | -29.80% |    -0.72 | 52.41%     | ok               |
| HYG        |       81 | -9.52%   | 3.71%              | -9.59%  |    -1.11 | 34.28%     | ok               |
| IBIT       |       32 | 44.80%   | -12.42%            | -18.95% |     0.87 | 31.98%     | ok               |
| IBM        |       76 | 3.41%    | 53.32%             | -27.54% |     0.17 | 49.58%     | ok               |
| ICP-USD    |       83 | -3.73%   | -76.53%            | -55.67% |     0.23 | 38.51%     | ok               |
| IEF        |       76 | -10.90%  | -0.60%             | -11.70% |    -1.54 | 32.78%     | ok               |
| IEMG       |       58 | -5.52%   | 66.05%             | -26.84% |    -0.12 | 43.59%     | ok               |
| INJ-USD    |       77 | -51.80%  | -77.49%            | -76.97% |    -0.47 | 38.70%     | ok               |
| INTC       |       70 | 55.82%   | 226.70%            | -60.60% |     0.62 | 49.25%     | ok               |
| INTU       |       67 | -13.13%  | -58.92%            | -43.77% |    -0.1  | 42.60%     | ok               |
| ITA        |       74 | -0.85%   | 95.33%             | -23.75% |     0.05 | 47.59%     | ok               |
| IWM        |       48 | 9.40%    | 55.14%             | -12.83% |     0.39 | 35.77%     | ok               |
| JNJ        |       72 | 5.11%    | 60.68%             | -17.51% |     0.24 | 50.25%     | ok               |
| JPM        |       73 | -19.22%  | 86.94%             | -33.16% |    -0.46 | 53.74%     | ok               |
| KO         |       49 | 28.93%   | 35.59%             | -8.07%  |     1.03 | 37.77%     | ok               |
| LDO-USD    |       76 | -2.99%   | -88.57%            | -60.93% |     0.24 | 38.31%     | ok               |
| LIN        |       64 | 0.44%    | 24.88%             | -21.53% |     0.08 | 38.60%     | ok               |
| LINK-USD   |       69 | -11.40%  | -71.26%            | -49.35% |     0.12 | 41.57%     | ok               |
| LLY        |       71 | -21.38%  | 70.12%             | -53.34% |    -0.26 | 51.25%     | ok               |
| LRCX       |       80 | 1.15%    | 419.19%            | -63.56% |     0.19 | 46.26%     | ok               |
| LTC-USD    |       66 | -34.00%  | -64.31%            | -53.76% |    -0.29 | 48.47%     | ok               |
| MCD        |       75 | -2.55%   | -5.04%             | -18.81% |    -0.05 | 38.10%     | ok               |
| META       |       72 | -26.25%  | 23.88%             | -38.96% |    -0.42 | 49.42%     | ok               |
| MPC        |       71 | -13.74%  | 53.43%             | -44.76% |    -0.14 | 49.92%     | ok               |
| MRK        |       67 | -30.49%  | 1.28%              | -34.46% |    -0.74 | 45.42%     | ok               |
| MS         |       80 | -17.40%  | 142.79%            | -27.79% |    -0.36 | 49.75%     | ok               |
| MSFT       |       83 | -33.98%  | -8.01%             | -38.02% |    -0.86 | 48.09%     | ok               |
| MU         |       51 | 270.20%  | 1264.41%           | -68.76% |     1.34 | 59.90%     | ok               |
| NEAR-USD   |       87 | 4.05%    | -63.19%            | -59.86% |     0.29 | 42.15%     | ok               |
| NEM        |       74 | -31.03%  | 177.48%            | -38.49% |    -0.33 | 53.74%     | ok               |
| NFLX       |       62 | 43.68%   | 28.44%             | -21.09% |     0.86 | 54.74%     | ok               |
| NKE        |       91 | -48.19%  | -59.99%            | -57.25% |    -0.9  | 43.59%     | ok               |
| NOW        |       80 | 17.37%   | -36.15%            | -30.25% |     0.37 | 45.92%     | ok               |
| NVDA       |       76 | -25.32%  | 132.92%            | -45.02% |    -0.17 | 58.29%     | ok               |
| OP-USD     |       74 | -5.33%   | -93.91%            | -70.27% |     0.2  | 35.25%     | ok               |
| ORCL       |       74 | 87.79%   | 27.10%             | -29.47% |     0.83 | 53.58%     | ok               |
| OXY        |       65 | 10.88%   | -15.63%            | -30.43% |     0.3  | 43.43%     | ok               |
| PEP        |       83 | -7.99%   | -21.01%            | -21.35% |    -0.17 | 49.75%     | ok               |
| PEPE-USD   |       79 | 23.59%   | -83.63%            | -57.66% |     0.46 | 44.44%     | ok               |
| PFE        |       77 | -39.30%  | -12.44%            | -40.87% |    -1.27 | 34.94%     | ok               |
| PG         |       64 | -15.19%  | -7.75%             | -21.96% |    -0.56 | 41.60%     | ok               |
| PM         |       85 | -2.21%   | 97.37%             | -33.68% |     0.05 | 57.40%     | ok               |
| POL-USD    |       81 | 83.81%   | -84.25%            | -46.45% |     0.88 | 51.15%     | ok               |
| QCOM       |       75 | -10.63%  | 28.24%             | -56.59% |     0.03 | 46.92%     | ok               |
| QQQ        |       64 | 20.05%   | 72.22%             | -12.88% |     0.57 | 45.26%     | ok               |
| RENDER-USD |       98 | -13.20%  | -64.25%            | -45.00% |     0.16 | 43.95%     | ok               |
| RTX        |       58 | 20.13%   | 105.60%            | -16.99% |     0.53 | 51.58%     | ok               |
| SBUX       |       64 | -22.96%  | 6.82%              | -29.34% |    -0.46 | 39.93%     | ok               |
| SCHW       |       76 | -24.21%  | 49.09%             | -31.92% |    -0.58 | 45.92%     | ok               |
| SHIB-USD   |       78 | -21.74%  | -78.14%            | -47.96% |    -0.05 | 53.26%     | ok               |
| SHY        |       48 | -2.24%   | 0.27%              | -2.85%  |    -0.79 | 34.28%     | ok               |
| SKY-USD    |       70 | -28.56%  | -10.01%            | -43.98% |    -0.35 | 41.23%     | ok               |
| SLB        |       75 | -24.42%  | -3.17%             | -54.95% |    -0.41 | 50.42%     | ok               |
| SLV        |       58 | 48.42%   | 160.70%            | -42.66% |     0.68 | 41.60%     | ok               |
| SMH        |       48 | 93.95%   | 240.30%            | -33.99% |     1.19 | 49.58%     | ok               |
| SNX-USD    |       62 | -8.25%   | -86.83%            | -34.76% |     0.17 | 39.08%     | ok               |
| SOL-USD    |       68 | -37.42%  | -69.72%            | -55.52% |    -0.15 | 59.39%     | ok               |
| SOXX       |       55 | 86.31%   | 221.68%            | -40.34% |     1.07 | 48.59%     | ok               |
| SPY        |       62 | 4.03%    | 51.17%             | -16.47% |     0.2  | 50.25%     | ok               |
| SUSHI-USD  |       90 | -79.45%  | -88.54%            | -84.18% |    -1.18 | 35.63%     | ok               |
| T          |       62 | 45.43%   | 17.55%             | -17.01% |     0.98 | 51.75%     | ok               |
| TGT        |       58 | -12.27%  | -9.57%             | -40.57% |    -0.17 | 38.60%     | ok               |
| TIA-USD    |       88 | -34.83%  | -91.91%            | -64.54% |    -0.15 | 35.82%     | ok               |
| TLT        |       72 | -20.23%  | -9.08%             | -20.97% |    -1.57 | 31.61%     | ok               |
| TMO        |       57 | 8.05%    | -10.52%            | -18.85% |     0.26 | 48.09%     | ok               |
| TMUS       |       70 | 19.52%   | 4.18%              | -24.50% |     0.49 | 47.75%     | ok               |
| TRX-USD    |       74 | -1.66%   | 27.55%             | -22.90% |     0.05 | 49.43%     | ok               |
| TSLA       |       67 | 19.34%   | 127.23%            | -42.22% |     0.38 | 41.60%     | ok               |
| TXN        |       77 | -15.83%  | 88.21%             | -46.98% |    -0.1  | 53.41%     | ok               |
| UNH        |       74 | 27.08%   | -18.61%            | -27.86% |     0.49 | 52.41%     | ok               |
| UNI-USD    |       88 | -72.12%  | -75.71%            | -80.61% |    -0.87 | 41.76%     | ok               |
| UPS        |       72 | -36.62%  | -26.33%            | -38.76% |    -0.73 | 40.27%     | ok               |
| USO        |       66 | 8.43%    | 54.69%             | -43.35% |     0.26 | 34.11%     | ok               |
| VEA        |       58 | -0.98%   | 49.94%             | -17.93% |     0.01 | 44.09%     | ok               |
| VIXY       |       96 | -80.86%  | -62.01%            | -88.16% |    -1.03 | 32.78%     | ok               |
| VNQ        |       75 | -16.77%  | 15.22%             | -24.92% |    -0.7  | 37.60%     | ok               |
| VTI        |       66 | -0.94%   | 51.13%             | -18.77% |     0.03 | 51.08%     | ok               |
| VWO        |       76 | -13.41%  | 46.62%             | -25.20% |    -0.47 | 44.09%     | ok               |
| VZ         |       87 | -29.21%  | 3.02%              | -28.39% |    -1    | 36.94%     | ok               |
| WFC        |       84 | -20.27%  | 71.13%             | -29.78% |    -0.36 | 49.08%     | ok               |
| WIF-USD    |       68 | -43.81%  | -86.61%            | -57.06% |    -0.24 | 32.18%     | ok               |
| WMT        |       59 | 19.81%   | 100.09%            | -21.31% |     0.57 | 50.92%     | ok               |
| XBI        |       62 | 6.18%    | 76.30%             | -19.80% |     0.23 | 40.43%     | ok               |
| XLB        |       66 | -10.84%  | 23.36%             | -26.57% |    -0.36 | 37.10%     | ok               |
| XLC        |       65 | 16.58%   | 36.68%             | -12.33% |     0.58 | 55.57%     | ok               |
| XLE        |       73 | -11.37%  | 27.09%             | -37.51% |    -0.22 | 46.76%     | ok               |
| XLF        |       76 | -11.63%  | 38.06%             | -23.61% |    -0.38 | 48.25%     | ok               |
| XLI        |       64 | 2.77%    | 59.71%             | -11.38% |     0.16 | 45.59%     | ok               |
| XLK        |       42 | 64.69%   | 88.85%             | -14.75% |     1.2  | 47.09%     | ok               |
| XLM-USD    |       69 | 0.26%    | -52.34%            | -50.36% |     0.22 | 45.59%     | ok               |
| XLP        |       68 | 6.56%    | 12.44%             | -11.16% |     0.4  | 42.93%     | ok               |
| XLU        |       69 | -5.08%   | 50.06%             | -19.39% |    -0.19 | 37.60%     | ok               |
| XLV        |       66 | -12.12%  | 10.20%             | -16.83% |    -0.59 | 35.61%     | ok               |
| XLY        |       70 | 3.26%    | 33.36%             | -14.01% |     0.17 | 44.43%     | ok               |
| XOM        |       58 | 4.39%    | 33.71%             | -20.29% |     0.2  | 36.77%     | ok               |
| XRP-USD    |       62 | -31.08%  | -65.92%            | -44.90% |    -0.27 | 34.29%     | ok               |
| YFI-USD    |       81 | -52.55%  | -77.82%            | -67.78% |    -0.75 | 40.80%     | ok               |
| ZEC-USD    |       64 | 56.52%   | 776.88%            | -47.68% |     0.62 | 36.21%     | ok               |

## AAPL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 19.89%   | 52.86%             | -21.71% |     0.47 |       67 | 52.75%     | ok               |
|          15 | 16.20%   | 52.86%             | -23.86% |     0.4  |       74 | 59.90%     | ok               |
|          25 | 14.16%   | 52.86%             | -20.03% |     0.37 |       65 | 50.58%     | ok               |
|          30 | 11.48%   | 52.86%             | -20.65% |     0.33 |       63 | 48.42%     | ok               |
|          35 | 6.37%    | 52.86%             | -22.04% |     0.23 |       63 | 46.26%     | ok               |

## AAVE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 6.43%    | -73.13%            | -43.61% |     0.29 |       38 | 29.89%     | ok               |
|          45 | -1.41%   | -73.13%            | -46.87% |     0.19 |       38 | 25.67%     | ok               |
|          35 | -12.47%  | -73.13%            | -51.96% |     0.08 |       50 | 32.57%     | ok               |
|          50 | -29.26%  | -73.13%            | -43.73% |    -0.28 |       42 | 19.54%     | ok               |
|          15 | -54.95%  | -73.13%            | -61.76% |    -0.39 |       80 | 50.77%     | ok               |

## ABBV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -3.06%   | 45.21%             | -23.85% |     0    |       50 | 36.94%     | ok               |
|          40 | -15.13%  | 45.21%             | -26.61% |    -0.32 |       64 | 41.76%     | ok               |
|          35 | -16.34%  | 45.21%             | -27.83% |    -0.35 |       66 | 44.59%     | ok               |
|          30 | -18.51%  | 45.21%             | -30.55% |    -0.39 |       64 | 47.42%     | ok               |
|          45 | -17.78%  | 45.21%             | -29.59% |    -0.41 |       54 | 39.10%     | ok               |

## ADA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -80.74%  | -85.00%            | -91.37% |    -0.47 |       80 | 63.41%     | ok               |
|          20 | -82.26%  | -85.00%            | -91.89% |    -0.54 |       90 | 57.66%     | ok               |
|          50 | -77.92%  | -85.00%            | -85.97% |    -0.59 |       55 | 26.82%     | ok               |
|          45 | -80.28%  | -85.00%            | -88.02% |    -0.62 |       58 | 31.61%     | ok               |
|          25 | -83.78%  | -85.00%            | -91.94% |    -0.62 |       83 | 53.83%     | ok               |

## ADBE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 9.17%    | -66.23%            | -21.34% |     0.27 |       78 | 49.75%     | ok               |
|          40 | -4.92%   | -66.23%            | -20.88% |     0.03 |       74 | 42.76%     | ok               |
|          25 | -8.57%   | -66.23%            | -30.47% |     0.02 |       52 | 61.56%     | ok               |
|          15 | -18.32%  | -66.23%            | -31.45% |    -0.13 |       63 | 66.22%     | ok               |
|          20 | -19.92%  | -66.23%            | -33.63% |    -0.16 |       52 | 63.73%     | ok               |

## AGG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -6.37%   | 0.84%              | -9.93%  |    -1.06 |       67 | 30.95%     | ok               |
|          20 | -7.76%   | 0.84%              | -10.85% |    -1.14 |       71 | 36.44%     | ok               |
|          45 | -5.75%   | 0.84%              | -7.89%  |    -1.16 |       52 | 20.47%     | ok               |
|          25 | -7.94%   | 0.84%              | -11.38% |    -1.22 |       71 | 34.78%     | ok               |
|          50 | -5.57%   | 0.84%              | -7.92%  |    -1.25 |       46 | 16.97%     | ok               |

## ALGO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -50.43%  | -78.45%            | -53.13% |    -0.57 |       86 | 38.12%     | ok               |
|          15 | -61.64%  | -78.45%            | -68.50% |    -0.67 |       84 | 50.38%     | ok               |
|          25 | -61.89%  | -78.45%            | -72.48% |    -0.74 |       84 | 45.02%     | ok               |
|          20 | -65.54%  | -78.45%            | -71.20% |    -0.8  |       86 | 48.08%     | ok               |
|          50 | -45.64%  | -78.45%            | -48.43% |    -0.81 |       42 | 16.86%     | ok               |

## AMAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 18.31%   | 328.57%            | -54.05% |     0.38 |       66 | 62.06%     | ok               |
|          30 | -0.98%   | 328.57%            | -57.21% |     0.17 |       69 | 53.41%     | ok               |
|          50 | -5.71%   | 328.57%            | -48.72% |     0.09 |       52 | 39.27%     | ok               |
|          20 | -8.22%   | 328.57%            | -60.16% |     0.09 |       72 | 58.57%     | ok               |
|          35 | -8.03%   | 328.57%            | -55.26% |     0.08 |       71 | 51.25%     | ok               |

## AMD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 6.87%    | 246.03%            | -44.76% |     0.28 |       56 | 36.77%     | ok               |
|          50 | 5.05%    | 246.03%            | -44.97% |     0.25 |       58 | 31.11%     | ok               |
|          35 | -6.75%   | 246.03%            | -54.16% |     0.14 |       62 | 38.77%     | ok               |
|          45 | -14.62%  | 246.03%            | -53.82% |     0.04 |       64 | 34.11%     | ok               |
|          30 | -19.05%  | 246.03%            | -59.51% |     0.01 |       63 | 41.26%     | ok               |

## AMGN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -15.64%  | 14.57%             | -26.64% |    -0.26 |       73 | 52.58%     | ok               |
|          15 | -18.78%  | 14.57%             | -27.92% |    -0.32 |       71 | 58.40%     | ok               |
|          35 | -16.99%  | 14.57%             | -31.23% |    -0.32 |       67 | 42.60%     | ok               |
|          30 | -20.87%  | 14.57%             | -34.14% |    -0.42 |       71 | 46.42%     | ok               |
|          25 | -24.09%  | 14.57%             | -33.41% |    -0.5  |       67 | 48.75%     | ok               |

## AMZN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -16.92%  | 40.90%             | -27.15% |    -0.48 |       50 | 29.45%     | ok               |
|          50 | -22.21%  | 40.90%             | -34.08% |    -0.76 |       46 | 23.63%     | ok               |
|          45 | -25.07%  | 40.90%             | -34.08% |    -0.85 |       50 | 26.62%     | ok               |
|          35 | -30.86%  | 40.90%             | -38.29% |    -0.96 |       66 | 32.95%     | ok               |
|          30 | -37.01%  | 40.90%             | -42.48% |    -1.1  |       78 | 38.44%     | ok               |

## APT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 46.14%   | -92.79%            | -46.73% |     0.68 |       44 | 20.50%     | ok               |
|          45 | 11.11%   | -92.79%            | -63.86% |     0.33 |       60 | 26.63%     | ok               |
|          20 | -15.91%  | -92.79%            | -70.51% |     0.14 |       73 | 52.87%     | ok               |
|          40 | -10.23%  | -92.79%            | -63.33% |     0.13 |       66 | 32.18%     | ok               |
|          35 | -16.81%  | -92.79%            | -64.45% |     0.07 |       70 | 37.93%     | ok               |

## ARB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 72.02%   | -88.78%            | -53.74% |     0.72 |       87 | 56.70%     | ok               |
|          40 | 45.76%   | -88.78%            | -47.60% |     0.62 |       50 | 30.27%     | ok               |
|          35 | 31.50%   | -88.78%            | -56.00% |     0.51 |       60 | 33.72%     | ok               |
|          20 | 29.27%   | -88.78%            | -60.40% |     0.5  |       75 | 50.19%     | ok               |
|          45 | 24.86%   | -88.78%            | -50.83% |     0.46 |       56 | 23.37%     | ok               |

## ARKK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -24.32%  | 73.06%             | -34.75% |    -0.28 |       90 | 50.25%     | ok               |
|          20 | -28.79%  | 73.06%             | -34.66% |    -0.4  |       85 | 45.59%     | ok               |
|          30 | -30.02%  | 73.06%             | -32.63% |    -0.5  |       79 | 38.94%     | ok               |
|          35 | -31.21%  | 73.06%             | -33.79% |    -0.56 |       78 | 36.61%     | ok               |
|          40 | -32.66%  | 73.06%             | -34.78% |    -0.64 |       70 | 31.78%     | ok               |

## ATOM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -61.38%  | -75.43%            | -69.81% |    -0.84 |       93 | 51.72%     | ok               |
|          15 | -66.68%  | -75.43%            | -71.82% |    -0.92 |       93 | 61.11%     | ok               |
|          45 | -55.54%  | -75.43%            | -63.84% |    -0.96 |       76 | 29.69%     | ok               |
|          30 | -65.53%  | -75.43%            | -73.34% |    -1.04 |       90 | 45.40%     | ok               |
|          20 | -70.18%  | -75.43%            | -74.51% |    -1.08 |      101 | 55.36%     | ok               |

## AVAX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 15.04%   | -81.79%            | -34.50% |     0.37 |       38 | 19.54%     | ok               |
|          45 | 6.34%    | -81.79%            | -41.07% |     0.26 |       42 | 23.75%     | ok               |
|          15 | -3.05%   | -81.79%            | -52.46% |     0.23 |       67 | 54.02%     | ok               |
|          40 | -8.53%   | -81.79%            | -46.84% |     0.07 |       46 | 26.82%     | ok               |
|          25 | -16.70%  | -81.79%            | -52.93% |     0.04 |       73 | 44.44%     | ok               |

## AVGO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 27.56%   | 208.96%            | -35.76% |     0.46 |       62 | 44.26%     | ok               |
|          35 | 21.43%   | 208.96%            | -36.19% |     0.4  |       70 | 41.43%     | ok               |
|          25 | 21.32%   | 208.96%            | -38.01% |     0.4  |       66 | 45.09%     | ok               |
|          40 | 21.02%   | 208.96%            | -40.70% |     0.4  |       60 | 38.27%     | ok               |
|          50 | 15.03%   | 208.96%            | -35.84% |     0.34 |       62 | 32.11%     | ok               |

## BA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 26.03%   | 3.78%              | -13.34% |     0.67 |       42 | 31.45%     | ok               |
|          35 | 30.46%   | 3.78%              | -23.77% |     0.59 |       72 | 44.59%     | ok               |
|          40 | 20.11%   | 3.78%              | -23.90% |     0.47 |       46 | 38.60%     | ok               |
|          25 | 10.59%   | 3.78%              | -32.48% |     0.29 |       70 | 52.58%     | ok               |
|          30 | 7.60%    | 3.78%              | -30.56% |     0.25 |       67 | 49.25%     | ok               |

## BAC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -5.91%   | 72.46%             | -22.31% |    -0.12 |       60 | 36.94%     | ok               |
|          20 | -8.46%   | 72.46%             | -21.70% |    -0.12 |       80 | 52.58%     | ok               |
|          35 | -7.63%   | 72.46%             | -27.81% |    -0.15 |       70 | 44.09%     | ok               |
|          50 | -7.44%   | 72.46%             | -20.84% |    -0.19 |       58 | 33.78%     | ok               |
|          25 | -11.11%  | 72.46%             | -25.79% |    -0.22 |       80 | 50.58%     | ok               |

## BCH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -3.13%   | -53.61%            | -54.26% |     0.18 |       78 | 49.62%     | ok               |
|          15 | -14.50%  | -53.61%            | -58.01% |     0.09 |       76 | 60.34%     | ok               |
|          20 | -14.38%  | -53.61%            | -56.98% |     0.09 |       74 | 56.13%     | ok               |
|          25 | -24.18%  | -53.61%            | -61.90% |    -0.05 |       73 | 51.92%     | ok               |
|          40 | -20.29%  | -53.61%            | -61.24% |    -0.07 |       69 | 40.61%     | ok               |

## BITO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 26.14%   | -60.92%            | -31.98% |     0.47 |       54 | 25.79%     | ok               |
|          30 | 14.25%   | -60.92%            | -42.82% |     0.33 |       78 | 41.76%     | ok               |
|          15 | 7.08%    | -60.92%            | -48.38% |     0.27 |       87 | 50.58%     | ok               |
|          45 | 8.18%    | -60.92%            | -41.16% |     0.26 |       62 | 29.28%     | ok               |
|          25 | 5.21%    | -60.92%            | -41.73% |     0.24 |       82 | 44.76%     | ok               |

## BLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -3.39%   | 22.03%             | -17.97% |    -0.04 |       82 | 39.60%     | ok               |
|          20 | -5.80%   | 22.03%             | -21.48% |    -0.09 |       80 | 47.59%     | ok               |
|          40 | -5.22%   | 22.03%             | -20.08% |    -0.11 |       74 | 35.27%     | ok               |
|          30 | -9.61%   | 22.03%             | -24.29% |    -0.22 |       75 | 43.26%     | ok               |
|          25 | -10.52%  | 22.03%             | -23.36% |    -0.24 |       75 | 45.59%     | ok               |

## BND Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.45%   | 0.89%              | -9.32%  |    -0.94 |       63 | 37.94%     | ok               |
|          25 | -7.14%   | 0.89%              | -10.40% |    -1.09 |       67 | 35.94%     | ok               |
|          30 | -7.32%   | 0.89%              | -9.89%  |    -1.18 |       65 | 32.28%     | ok               |
|          15 | -8.65%   | 0.89%              | -10.85% |    -1.25 |       73 | 40.77%     | ok               |
|          45 | -7.22%   | 0.89%              | -9.57%  |    -1.39 |       50 | 22.13%     | ok               |

## BONK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 170.82%  | -85.19%            | -35.57% |     1.24 |       46 | 22.22%     | ok               |
|          25 | 186.54%  | -85.19%            | -46.61% |     1.08 |       65 | 48.28%     | ok               |
|          20 | 170.36%  | -85.19%            | -54.25% |     1.03 |       66 | 52.87%     | ok               |
|          15 | 176.55%  | -85.19%            | -62.48% |     1.02 |       69 | 57.85%     | ok               |
|          45 | 82.77%   | -85.19%            | -42.36% |     0.83 |       56 | 26.82%     | ok               |

## BTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 62.19%   | -43.33%            | -14.50% |     1.08 |       46 | 34.29%     | ok               |
|          45 | 46.76%   | -43.33%            | -13.36% |     0.89 |       46 | 30.65%     | ok               |
|          35 | 40.57%   | -43.33%            | -22.12% |     0.76 |       70 | 41.38%     | ok               |
|          30 | 23.69%   | -43.33%            | -21.75% |     0.5  |       74 | 48.08%     | ok               |
|          50 | 18.84%   | -43.33%            | -16.15% |     0.49 |       42 | 25.29%     | ok               |

## C Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -8.19%   | 157.52%            | -22.28% |    -0.15 |       66 | 36.61%     | ok               |
|          45 | -15.03%  | 157.52%            | -28.12% |    -0.33 |       78 | 40.60%     | ok               |
|          15 | -24.15%  | 157.52%            | -35.02% |    -0.4  |       74 | 60.23%     | ok               |
|          25 | -24.14%  | 157.52%            | -35.86% |    -0.44 |       73 | 53.74%     | ok               |
|          40 | -21.04%  | 157.52%            | -33.20% |    -0.47 |       82 | 43.09%     | ok               |

## CAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 38.52%   | 229.98%            | -21.02% |     0.66 |       72 | 57.07%     | ok               |
|          25 | 38.64%   | 229.98%            | -26.37% |     0.66 |       68 | 59.90%     | ok               |
|          20 | 35.83%   | 229.98%            | -25.65% |     0.62 |       78 | 63.23%     | ok               |
|          45 | 26.55%   | 229.98%            | -28.85% |     0.53 |       58 | 45.92%     | ok               |
|          15 | 25.30%   | 229.98%            | -30.60% |     0.49 |       71 | 69.22%     | ok               |

## CL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 14.26%   | 9.48%              | -12.98% |     0.61 |       42 | 30.78%     | ok               |
|          30 | 13.77%   | 9.48%              | -14.32% |     0.49 |       60 | 46.76%     | ok               |
|          45 | 9.04%    | 9.48%              | -13.51% |     0.4  |       46 | 33.78%     | ok               |
|          35 | 8.35%    | 9.48%              | -13.83% |     0.34 |       62 | 43.09%     | ok               |
|          40 | 5.21%    | 9.48%              | -12.70% |     0.25 |       56 | 37.77%     | ok               |

## CMCSA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -36.10%  | -41.03%            | -44.43% |    -0.79 |       88 | 58.74%     | ok               |
|          30 | -38.29%  | -41.03%            | -38.49% |    -0.99 |       80 | 43.93%     | ok               |
|          25 | -43.66%  | -41.03%            | -41.59% |    -1.16 |       89 | 49.25%     | ok               |
|          50 | -30.21%  | -41.03%            | -31.36% |    -1.17 |       48 | 15.47%     | ok               |
|          20 | -47.06%  | -41.03%            | -45.83% |    -1.24 |       94 | 54.74%     | ok               |

## COMP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 0.93%    | -79.36%            | -38.71% |     0.21 |       52 | 21.26%     | ok               |
|          25 | -35.52%  | -79.36%            | -60.58% |    -0.15 |       89 | 51.15%     | ok               |
|          30 | -34.33%  | -79.36%            | -58.43% |    -0.17 |       91 | 46.17%     | ok               |
|          15 | -44.08%  | -79.36%            | -65.55% |    -0.24 |      103 | 62.64%     | ok               |
|          40 | -38.92%  | -79.36%            | -47.89% |    -0.33 |       76 | 34.29%     | ok               |

## COP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -11.98%  | -6.78%             | -35.08% |    -0.2  |       50 | 27.45%     | ok               |
|          45 | -17.86%  | -6.78%             | -41.35% |    -0.35 |       62 | 30.28%     | ok               |
|          35 | -20.27%  | -6.78%             | -43.58% |    -0.36 |       75 | 37.44%     | ok               |
|          30 | -20.81%  | -6.78%             | -43.96% |    -0.36 |       73 | 40.60%     | ok               |
|          40 | -23.93%  | -6.78%             | -47.05% |    -0.51 |       70 | 33.28%     | ok               |

## COST Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 13.87%   | 31.61%             | -24.32% |     0.44 |       66 | 51.91%     | ok               |
|          25 | 12.19%   | 31.61%             | -24.73% |     0.4  |       63 | 49.08%     | ok               |
|          35 | 6.97%    | 31.61%             | -26.58% |     0.28 |       54 | 42.43%     | ok               |
|          30 | 2.07%    | 31.61%             | -29.73% |     0.13 |       60 | 45.42%     | ok               |
|          40 | 0.40%    | 31.61%             | -28.41% |     0.08 |       56 | 39.43%     | ok               |

## CRM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -31.97%  | -45.19%            | -41.65% |    -0.48 |       92 | 55.41%     | ok               |
|          35 | -26.37%  | -45.19%            | -35.48% |    -0.5  |       64 | 38.77%     | ok               |
|          40 | -33.02%  | -45.19%            | -41.30% |    -0.75 |       70 | 34.94%     | ok               |
|          30 | -36.76%  | -45.19%            | -40.31% |    -0.75 |       67 | 43.59%     | ok               |
|          20 | -42.01%  | -45.19%            | -43.99% |    -0.79 |       80 | 49.08%     | ok               |

## CRV-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 32.82%   | -76.11%            | -37.78% |     0.53 |       66 | 31.03%     | ok               |
|          45 | 12.02%   | -76.11%            | -42.29% |     0.33 |       54 | 20.69%     | ok               |
|          50 | 12.26%   | -76.11%            | -29.30% |     0.33 |       46 | 17.43%     | ok               |
|          30 | 5.48%    | -76.11%            | -39.89% |     0.28 |       64 | 35.63%     | ok               |
|          40 | 5.77%    | -76.11%            | -38.86% |     0.27 |       58 | 27.01%     | ok               |

## CSCO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 33.52%   | 135.01%            | -19.34% |     0.72 |       56 | 38.77%     | ok               |
|          45 | 32.58%   | 135.01%            | -19.34% |     0.69 |       51 | 41.26%     | ok               |
|          25 | 27.19%   | 135.01%            | -23.28% |     0.57 |       63 | 52.25%     | ok               |
|          35 | 26.59%   | 135.01%            | -23.68% |     0.57 |       51 | 47.75%     | ok               |
|          30 | 26.60%   | 135.01%            | -21.79% |     0.56 |       59 | 50.25%     | ok               |

## CVX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -7.26%   | 8.80%              | -23.25% |    -0.12 |       72 | 44.09%     | ok               |
|          20 | -8.24%   | 8.80%              | -25.18% |    -0.15 |       72 | 45.26%     | ok               |
|          30 | -12.12%  | 8.80%              | -26.75% |    -0.28 |       71 | 41.60%     | ok               |
|          45 | -10.56%  | 8.80%              | -28.32% |    -0.28 |       63 | 30.28%     | ok               |
|          35 | -11.86%  | 8.80%              | -27.83% |    -0.28 |       71 | 38.60%     | ok               |

## DASH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 129.69%  | -5.42%             | -31.38% |     0.96 |       40 | 17.05%     | ok               |
|          40 | 75.62%   | -5.42%             | -34.44% |     0.72 |       46 | 23.75%     | ok               |
|          45 | 65.87%   | -5.42%             | -39.58% |     0.68 |       44 | 19.35%     | ok               |
|          25 | -32.35%  | -5.42%             | -64.14% |     0.1  |       69 | 34.48%     | ok               |
|          35 | -32.14%  | -5.42%             | -63.23% |     0.09 |       69 | 28.16%     | ok               |

## DBC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -10.12%  | 21.29%             | -27.30% |    -0.31 |       71 | 37.60%     | ok               |
|          35 | -10.07%  | 21.29%             | -23.71% |    -0.33 |       58 | 31.78%     | ok               |
|          50 | -8.98%   | 21.29%             | -20.31% |    -0.34 |       42 | 21.13%     | ok               |
|          45 | -10.35%  | 21.29%             | -21.46% |    -0.37 |       54 | 24.46%     | ok               |
|          30 | -12.95%  | 21.29%             | -25.67% |    -0.45 |       56 | 32.95%     | ok               |

## DE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -0.18%   | 63.11%             | -28.94% |     0.1  |       72 | 51.75%     | ok               |
|          30 | -1.11%   | 63.11%             | -25.24% |     0.07 |       72 | 46.42%     | ok               |
|          25 | -2.66%   | 63.11%             | -26.67% |     0.04 |       74 | 49.08%     | ok               |
|          50 | -3.24%   | 63.11%             | -24.57% |    -0.01 |       72 | 31.28%     | ok               |
|          45 | -5.17%   | 63.11%             | -28.13% |    -0.04 |       70 | 35.77%     | ok               |

## DIA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -0.01%   | 35.66%             | -13.15% |     0.04 |       60 | 43.43%     | ok               |
|          25 | -0.55%   | 35.66%             | -11.28% |     0.01 |       60 | 46.76%     | ok               |
|          30 | -2.08%   | 35.66%             | -12.94% |    -0.07 |       60 | 45.59%     | ok               |
|          20 | -3.96%   | 35.66%             | -13.85% |    -0.16 |       64 | 49.08%     | ok               |
|          40 | -4.05%   | 35.66%             | -15.06% |    -0.2  |       66 | 40.77%     | ok               |

## DIS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 29.88%   | -3.06%             | -14.24% |     0.77 |       50 | 29.45%     | ok               |
|          45 | 2.74%    | -3.06%             | -16.54% |     0.16 |       53 | 33.11%     | ok               |
|          40 | 1.81%    | -3.06%             | -22.77% |     0.14 |       65 | 38.27%     | ok               |
|          15 | -9.37%   | -3.06%             | -31.15% |    -0.06 |       88 | 58.90%     | ok               |
|          35 | -8.37%   | -3.06%             | -25.70% |    -0.07 |       75 | 44.26%     | ok               |

## DOGE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 21.11%   | -78.81%            | -59.36% |     0.45 |       82 | 65.52%     | ok               |
|          20 | 3.41%    | -78.81%            | -57.37% |     0.31 |       85 | 60.73%     | ok               |
|          25 | -0.88%   | -78.81%            | -55.33% |     0.26 |       75 | 55.36%     | ok               |
|          30 | -17.34%  | -78.81%            | -62.31% |     0.08 |       78 | 50.19%     | ok               |
|          35 | -41.83%  | -78.81%            | -61.79% |    -0.31 |       74 | 43.87%     | ok               |

## DOT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -19.97%  | -86.78%            | -45.72% |    -0.12 |       60 | 26.63%     | ok               |
|          45 | -25.67%  | -86.78%            | -51.57% |    -0.19 |       54 | 31.61%     | ok               |
|          40 | -33.51%  | -86.78%            | -51.23% |    -0.29 |       58 | 35.25%     | ok               |
|          20 | -47.27%  | -86.78%            | -65.30% |    -0.29 |       94 | 61.30%     | ok               |
|          35 | -42.80%  | -86.78%            | -61.83% |    -0.29 |       82 | 42.72%     | ok               |

## DXY-INDEX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -1.98%   | -0.05%             | -6.06%  |    -0.3  |       44 | 30.59%     | ok               |
|          40 | -3.81%   | -0.05%             | -7.30%  |    -0.48 |       68 | 48.16%     | ok               |
|          15 | -5.35%   | -0.05%             | -11.57% |    -0.49 |       90 | 75.70%     | ok               |
|          30 | -4.74%   | -0.05%             | -9.98%  |    -0.54 |       70 | 58.79%     | ok               |
|          35 | -5.19%   | -0.05%             | -10.12% |    -0.63 |       73 | 54.23%     | ok               |

## EEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -4.96%   | 72.84%             | -19.52% |    -0.11 |       64 | 39.77%     | ok               |
|          35 | -5.62%   | 72.84%             | -23.88% |    -0.12 |       66 | 41.76%     | ok               |
|          50 | -4.94%   | 72.84%             | -15.88% |    -0.12 |       52 | 35.77%     | ok               |
|          45 | -6.04%   | 72.84%             | -17.36% |    -0.16 |       54 | 37.44%     | ok               |
|          30 | -9.40%   | 72.84%             | -25.67% |    -0.25 |       64 | 43.43%     | ok               |

## EFA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -2.18%   | 38.12%             | -10.80% |    -0.02 |       60 | 52.25%     | ok               |
|          20 | -8.97%   | 38.12%             | -12.49% |    -0.3  |       67 | 49.25%     | ok               |
|          30 | -9.68%   | 38.12%             | -15.14% |    -0.36 |       62 | 44.76%     | ok               |
|          50 | -9.07%   | 38.12%             | -17.56% |    -0.4  |       54 | 36.27%     | ok               |
|          25 | -11.12%  | 38.12%             | -16.37% |    -0.41 |       62 | 46.59%     | ok               |

## EOG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -20.10%  | 15.95%             | -39.69% |    -0.48 |       54 | 32.28%     | ok               |
|          50 | -21.27%  | 15.95%             | -40.57% |    -0.53 |       58 | 29.45%     | ok               |
|          30 | -24.73%  | 15.95%             | -48.13% |    -0.54 |       77 | 46.09%     | ok               |
|          35 | -25.56%  | 15.95%             | -46.26% |    -0.61 |       75 | 40.77%     | ok               |
|          40 | -24.83%  | 15.95%             | -43.26% |    -0.61 |       62 | 35.61%     | ok               |

## ETC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -7.93%   | -74.08%            | -27.89% |    -0.02 |       28 | 17.05%     | ok               |
|          35 | -15.03%  | -74.08%            | -42.62% |    -0.11 |       44 | 27.01%     | ok               |
|          45 | -16.07%  | -74.08%            | -35.44% |    -0.17 |       26 | 18.97%     | ok               |
|          40 | -21.04%  | -74.08%            | -40.48% |    -0.26 |       42 | 22.80%     | ok               |
|          30 | -35.69%  | -74.08%            | -48.16% |    -0.51 |       64 | 31.23%     | ok               |

## ETH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 167.50%  | -51.67%            | -30.11% |     1.32 |       64 | 45.21%     | ok               |
|          30 | 147.34%  | -51.67%            | -32.89% |     1.18 |       66 | 54.02%     | ok               |
|          40 | 63.83%   | -51.67%            | -33.11% |     0.8  |       60 | 37.74%     | ok               |
|          15 | 51.67%   | -51.67%            | -42.74% |     0.65 |       78 | 69.16%     | ok               |
|          20 | 45.06%   | -51.67%            | -39.10% |     0.61 |       83 | 63.79%     | ok               |

## EWJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -17.65%  | 40.93%             | -30.73% |    -0.57 |       64 | 39.60%     | ok               |
|          20 | -19.05%  | 40.93%             | -31.32% |    -0.6  |       60 | 41.60%     | ok               |
|          45 | -18.44%  | 40.93%             | -27.68% |    -0.69 |       60 | 31.78%     | ok               |
|          25 | -21.38%  | 40.93%             | -31.18% |    -0.7  |       60 | 40.60%     | ok               |
|          35 | -21.60%  | 40.93%             | -32.54% |    -0.73 |       70 | 37.94%     | ok               |

## FCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -6.11%   | 56.56%             | -27.80% |     0.03 |       54 | 29.62%     | ok               |
|          45 | -10.84%  | 56.56%             | -35.28% |    -0.04 |       54 | 33.94%     | ok               |
|          40 | -22.27%  | 56.56%             | -44.23% |    -0.24 |       64 | 38.60%     | ok               |
|          30 | -30.42%  | 56.56%             | -48.09% |    -0.37 |       65 | 45.26%     | ok               |
|          20 | -35.76%  | 56.56%             | -57.65% |    -0.42 |       72 | 52.08%     | ok               |

## FET-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 39.30%   | -85.53%            | -57.24% |     0.57 |       90 | 50.96%     | ok               |
|          15 | 4.18%    | -85.53%            | -59.58% |     0.35 |       86 | 54.02%     | ok               |
|          25 | -8.86%   | -85.53%            | -57.82% |     0.22 |       93 | 44.64%     | ok               |
|          30 | -14.01%  | -85.53%            | -54.02% |     0.16 |       83 | 40.80%     | ok               |
|          35 | -36.66%  | -85.53%            | -62.73% |    -0.18 |       71 | 34.29%     | ok               |

## FIL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -5.46%   | -85.42%            | -39.40% |     0.1  |       50 | 23.56%     | ok               |
|          35 | -29.70%  | -85.42%            | -45.88% |    -0.25 |       60 | 27.78%     | ok               |
|          30 | -33.03%  | -85.42%            | -49.05% |    -0.28 |       72 | 33.33%     | ok               |
|          45 | -27.58%  | -85.42%            | -43.98% |    -0.29 |       44 | 17.62%     | ok               |
|          50 | -26.52%  | -85.42%            | -44.97% |    -0.32 |       38 | 13.03%     | ok               |

## FXI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -0.65%   | 36.58%             | -22.57% |     0.07 |       44 | 30.45%     | ok               |
|          30 | -1.22%   | 36.58%             | -23.91% |     0.06 |       44 | 29.28%     | ok               |
|          15 | -3.60%   | 36.58%             | -21.68% |     0.01 |       52 | 33.78%     | ok               |
|          45 | -3.75%   | 36.58%             | -26.75% |    -0.02 |       44 | 23.96%     | ok               |
|          20 | -4.66%   | 36.58%             | -24.53% |    -0.03 |       50 | 31.61%     | ok               |

## GDX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 18.06%   | 172.19%            | -35.59% |     0.39 |       73 | 52.91%     | ok               |
|          40 | 13.85%   | 172.19%            | -31.87% |     0.35 |       64 | 42.93%     | ok               |
|          30 | 11.28%   | 172.19%            | -34.99% |     0.3  |       60 | 48.09%     | ok               |
|          35 | 8.95%    | 172.19%            | -32.37% |     0.27 |       68 | 45.26%     | ok               |
|          25 | 6.77%    | 172.19%            | -38.90% |     0.24 |       63 | 49.75%     | ok               |

## GDXJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -7.90%   | 191.02%            | -45.05% |     0.06 |       67 | 53.24%     | ok               |
|          30 | -23.13%  | 191.02%            | -44.93% |    -0.22 |       68 | 46.42%     | ok               |
|          50 | -20.22%  | 191.02%            | -44.94% |    -0.22 |       58 | 37.77%     | ok               |
|          25 | -26.54%  | 191.02%            | -47.26% |    -0.25 |       72 | 49.92%     | ok               |
|          35 | -26.76%  | 191.02%            | -43.49% |    -0.3  |       70 | 44.09%     | ok               |

## GE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 43.41%   | 240.37%            | -22.29% |     0.8  |       66 | 40.27%     | ok               |
|          45 | 32.58%   | 240.37%            | -25.68% |     0.64 |       74 | 43.09%     | ok               |
|          20 | 31.61%   | 240.37%            | -26.63% |     0.58 |       69 | 56.91%     | ok               |
|          35 | 25.70%   | 240.37%            | -27.11% |     0.52 |       80 | 48.42%     | ok               |
|          40 | 24.75%   | 240.37%            | -26.97% |     0.52 |       76 | 44.59%     | ok               |

## GLD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 35.03%   | 95.38%             | -14.61% |     0.82 |       46 | 47.09%     | ok               |
|          20 | 33.02%   | 95.38%             | -14.61% |     0.78 |       48 | 48.42%     | ok               |
|          30 | 28.60%   | 95.38%             | -16.63% |     0.71 |       48 | 45.92%     | ok               |
|          15 | 24.87%   | 95.38%             | -17.54% |     0.61 |       50 | 52.58%     | ok               |
|          35 | 22.33%   | 95.38%             | -17.29% |     0.59 |       50 | 45.26%     | ok               |

## GOOGL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 82.79%   | 148.00%            | -19.76% |     1.2  |       57 | 56.24%     | ok               |
|          30 | 77.86%   | 148.00%            | -20.41% |     1.16 |       63 | 53.74%     | ok               |
|          20 | 68.98%   | 148.00%            | -20.57% |     1.05 |       68 | 58.57%     | ok               |
|          35 | 60.55%   | 148.00%            | -22.85% |     1.04 |       71 | 48.59%     | ok               |
|          15 | 70.83%   | 148.00%            | -13.81% |     1.03 |       71 | 63.73%     | ok               |

## GRT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 37.41%   | -90.15%            | -35.66% |     0.62 |       44 | 22.03%     | ok               |
|          15 | 14.49%   | -90.15%            | -49.67% |     0.39 |       75 | 61.88%     | ok               |
|          20 | 10.52%   | -90.15%            | -46.47% |     0.35 |       83 | 56.32%     | ok               |
|          45 | 10.67%   | -90.15%            | -46.59% |     0.32 |       52 | 27.59%     | ok               |
|          35 | 6.17%    | -90.15%            | -48.22% |     0.28 |       62 | 36.40%     | ok               |

## GS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 21.11%   | 162.70%            | -20.56% |     0.47 |       74 | 61.06%     | ok               |
|          20 | 4.59%    | 162.70%            | -23.19% |     0.19 |       74 | 57.07%     | ok               |
|          40 | 0.08%    | 162.70%            | -17.88% |     0.09 |       72 | 45.26%     | ok               |
|          25 | -0.70%   | 162.70%            | -23.32% |     0.09 |       74 | 54.58%     | ok               |
|          30 | -2.38%   | 162.70%            | -22.13% |     0.05 |       76 | 52.08%     | ok               |

## HD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -4.02%   | -1.00%             | -18.58% |    -0.03 |       73 | 43.59%     | ok               |
|          25 | -4.77%   | -1.00%             | -19.40% |    -0.05 |       72 | 45.59%     | ok               |
|          45 | -8.80%   | -1.00%             | -19.30% |    -0.24 |       58 | 28.12%     | ok               |
|          15 | -13.77%  | -1.00%             | -27.26% |    -0.27 |      107 | 54.24%     | ok               |
|          35 | -12.64%  | -1.00%             | -22.43% |    -0.3  |       80 | 39.77%     | ok               |

## HON Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -13.43%  | 22.68%             | -21.17% |    -0.4  |       72 | 31.78%     | ok               |
|          45 | -15.16%  | 22.68%             | -19.99% |    -0.43 |       74 | 36.77%     | ok               |
|          40 | -23.52%  | 22.68%             | -26.29% |    -0.66 |       76 | 41.10%     | ok               |
|          35 | -24.98%  | 22.68%             | -27.37% |    -0.69 |       91 | 47.42%     | ok               |
|          30 | -26.82%  | 22.68%             | -29.80% |    -0.72 |       93 | 52.41%     | ok               |

## HYG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -7.92%   | 3.71%              | -7.92%  |    -0.96 |       70 | 29.45%     | ok               |
|          15 | -9.71%   | 3.71%              | -10.06% |    -1.05 |       88 | 41.43%     | ok               |
|          20 | -9.69%   | 3.71%              | -10.29% |    -1.08 |       86 | 39.10%     | ok               |
|          45 | -8.60%   | 3.71%              | -8.60%  |    -1.08 |       66 | 26.29%     | ok               |
|          30 | -9.52%   | 3.71%              | -9.59%  |    -1.11 |       81 | 34.28%     | ok               |

## IBIT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 75.73%   | -12.42%            | -19.20% |     1.17 |       38 | 39.62%     | ok               |
|          50 | 53.73%   | -12.42%            | -17.37% |     1.08 |       22 | 22.91%     | ok               |
|          45 | 47.46%   | -12.42%            | -17.37% |     0.96 |       26 | 24.11%     | ok               |
|          30 | 44.80%   | -12.42%            | -18.95% |     0.87 |       32 | 31.98%     | ok               |
|          40 | 41.09%   | -12.42%            | -17.78% |     0.86 |       26 | 26.01%     | ok               |

## IBM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 16.52%   | 53.32%             | -28.20% |     0.39 |       92 | 61.90%     | ok               |
|          30 | 3.41%    | 53.32%             | -27.54% |     0.17 |       76 | 49.58%     | ok               |
|          20 | -1.17%   | 53.32%             | -34.12% |     0.09 |       76 | 54.24%     | ok               |
|          35 | -1.09%   | 53.32%             | -27.54% |     0.08 |       72 | 45.09%     | ok               |
|          50 | -3.25%   | 53.32%             | -22.50% |     0.01 |       54 | 32.61%     | ok               |

## ICP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 17.53%   | -76.53%            | -32.85% |     0.39 |       60 | 26.82%     | ok               |
|          35 | 6.37%    | -76.53%            | -46.18% |     0.29 |       70 | 32.38%     | ok               |
|          30 | -3.73%   | -76.53%            | -55.67% |     0.23 |       83 | 38.51%     | ok               |
|          50 | 2.38%    | -76.53%            | -43.65% |     0.22 |       42 | 16.67%     | ok               |
|          45 | -10.93%  | -76.53%            | -40.57% |     0.05 |       60 | 20.88%     | ok               |

## IEF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -7.23%   | -0.60%             | -10.09% |    -0.87 |       70 | 42.10%     | ok               |
|          15 | -7.78%   | -0.60%             | -10.82% |    -0.92 |       69 | 43.59%     | ok               |
|          40 | -8.39%   | -0.60%             | -9.67%  |    -1.31 |       60 | 24.79%     | ok               |
|          45 | -8.07%   | -0.60%             | -9.73%  |    -1.33 |       50 | 22.80%     | ok               |
|          25 | -10.80%  | -0.60%             | -11.49% |    -1.38 |       76 | 39.27%     | ok               |

## IEMG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -0.32%   | 66.05%             | -22.13% |     0.05 |       63 | 42.60%     | ok               |
|          50 | -2.14%   | 66.05%             | -13.91% |    -0.03 |       54 | 34.11%     | ok               |
|          40 | -2.44%   | 66.05%             | -18.43% |    -0.03 |       60 | 39.93%     | ok               |
|          45 | -2.35%   | 66.05%             | -14.92% |    -0.03 |       50 | 36.77%     | ok               |
|          25 | -4.72%   | 66.05%             | -25.58% |    -0.09 |       59 | 45.42%     | ok               |

## INJ-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -9.97%   | -77.49%            | -53.80% |     0.06 |       42 | 22.61%     | ok               |
|          35 | -18.70%  | -77.49%            | -60.42% |     0.01 |       62 | 32.76%     | ok               |
|          50 | -19.76%  | -77.49%            | -49.35% |    -0.1  |       46 | 19.54%     | ok               |
|          40 | -27.04%  | -77.49%            | -57.21% |    -0.15 |       52 | 28.93%     | ok               |
|          25 | -53.83%  | -77.49%            | -81.57% |    -0.46 |       77 | 43.30%     | ok               |

## INTC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 76.11%   | 226.70%            | -49.32% |     0.74 |       60 | 34.28%     | ok               |
|          15 | 83.79%   | 226.70%            | -53.65% |     0.74 |       82 | 61.06%     | ok               |
|          25 | 75.50%   | 226.70%            | -56.41% |     0.72 |       75 | 51.58%     | ok               |
|          40 | 70.33%   | 226.70%            | -55.86% |     0.7  |       68 | 38.60%     | ok               |
|          20 | 72.70%   | 226.70%            | -52.47% |     0.7  |       82 | 56.57%     | ok               |

## INTU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 0.02%    | -58.92%            | -42.60% |     0.12 |       73 | 28.62%     | ok               |
|          45 | -3.40%   | -58.92%            | -44.44% |     0.06 |       71 | 32.78%     | ok               |
|          40 | -8.40%   | -58.92%            | -48.15% |    -0.03 |       73 | 35.77%     | ok               |
|          25 | -9.99%   | -58.92%            | -42.24% |    -0.04 |       66 | 45.26%     | ok               |
|          15 | -11.06%  | -58.92%            | -46.90% |    -0.05 |       81 | 50.75%     | ok               |

## ITA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 2.71%    | 95.33%             | -21.48% |     0.15 |       78 | 37.60%     | ok               |
|          15 | -0.78%   | 95.33%             | -28.17% |     0.07 |       86 | 59.23%     | ok               |
|          30 | -0.85%   | 95.33%             | -23.75% |     0.05 |       74 | 47.59%     | ok               |
|          35 | -2.96%   | 95.33%             | -23.16% |    -0.02 |       78 | 45.92%     | ok               |
|          40 | -4.08%   | 95.33%             | -20.58% |    -0.06 |       80 | 42.43%     | ok               |

## IWM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 9.83%    | 55.14%             | -13.30% |     0.4  |       50 | 36.77%     | ok               |
|          40 | 8.60%    | 55.14%             | -14.08% |     0.39 |       42 | 31.28%     | ok               |
|          30 | 9.40%    | 55.14%             | -12.83% |     0.39 |       48 | 35.77%     | ok               |
|          35 | 8.35%    | 55.14%             | -14.11% |     0.36 |       48 | 33.61%     | ok               |
|          20 | 5.50%    | 55.14%             | -13.83% |     0.25 |       60 | 37.77%     | ok               |

## JNJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 20.07%   | 60.68%             | -10.57% |     0.85 |       58 | 36.94%     | ok               |
|          15 | 14.47%   | 60.68%             | -18.02% |     0.52 |       68 | 56.91%     | ok               |
|          45 | 10.50%   | 60.68%             | -13.35% |     0.47 |       60 | 41.93%     | ok               |
|          20 | 10.59%   | 60.68%             | -17.61% |     0.42 |       72 | 53.58%     | ok               |
|          40 | 8.08%    | 60.68%             | -14.77% |     0.36 |       66 | 46.09%     | ok               |

## JPM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 19.35%   | 86.94%             | -15.90% |     0.64 |       52 | 41.43%     | ok               |
|          45 | 8.01%    | 86.94%             | -21.91% |     0.3  |       54 | 44.43%     | ok               |
|          40 | -6.26%   | 86.94%             | -28.47% |    -0.11 |       66 | 46.92%     | ok               |
|          20 | -13.25%  | 86.94%             | -33.59% |    -0.21 |       84 | 58.24%     | ok               |
|          35 | -11.49%  | 86.94%             | -27.43% |    -0.25 |       72 | 50.58%     | ok               |

## KO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 28.93%   | 35.59%             | -8.07%  |     1.03 |       49 | 37.77%     | ok               |
|          35 | 24.98%   | 35.59%             | -8.07%  |     0.93 |       52 | 36.44%     | ok               |
|          40 | 22.37%   | 35.59%             | -9.28%  |     0.9  |       54 | 33.28%     | ok               |
|          25 | 23.60%   | 35.59%             | -9.37%  |     0.86 |       55 | 40.43%     | ok               |
|          50 | 14.81%   | 35.59%             | -11.40% |     0.68 |       36 | 26.79%     | ok               |

## LDO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 24.99%   | -88.57%            | -46.95% |     0.48 |       81 | 51.92%     | ok               |
|          20 | 13.39%   | -88.57%            | -44.97% |     0.4  |       85 | 47.32%     | ok               |
|          50 | 15.22%   | -88.57%            | -48.04% |     0.37 |       46 | 16.86%     | ok               |
|          30 | -2.99%   | -88.57%            | -60.93% |     0.24 |       76 | 38.31%     | ok               |
|          35 | -5.15%   | -88.57%            | -62.61% |     0.2  |       74 | 31.42%     | ok               |

## LIN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 5.16%    | 24.88%             | -23.68% |     0.23 |       62 | 49.42%     | ok               |
|          25 | 4.87%    | 24.88%             | -22.01% |     0.23 |       61 | 41.43%     | ok               |
|          20 | 2.62%    | 24.88%             | -23.00% |     0.15 |       60 | 44.59%     | ok               |
|          35 | 1.08%    | 24.88%             | -21.18% |     0.1  |       60 | 32.11%     | ok               |
|          30 | 0.44%    | 24.88%             | -21.53% |     0.08 |       64 | 38.60%     | ok               |

## LINK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -11.40%  | -71.26%            | -49.35% |     0.12 |       69 | 41.57%     | ok               |
|          45 | -13.28%  | -71.26%            | -38.11% |     0.05 |       50 | 26.63%     | ok               |
|          50 | -12.86%  | -71.26%            | -36.52% |     0.03 |       40 | 21.26%     | ok               |
|          35 | -24.33%  | -71.26%            | -49.18% |    -0.05 |       59 | 36.78%     | ok               |
|          25 | -34.06%  | -71.26%            | -46.32% |    -0.12 |       68 | 47.13%     | ok               |

## LLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 11.91%   | 70.12%             | -38.23% |     0.33 |       46 | 38.27%     | ok               |
|          15 | 5.18%    | 70.12%             | -48.12% |     0.22 |       63 | 61.90%     | ok               |
|          45 | -0.04%   | 70.12%             | -42.66% |     0.12 |       54 | 41.60%     | ok               |
|          20 | -11.75%  | 70.12%             | -51.34% |    -0.05 |       72 | 56.91%     | ok               |
|          25 | -13.21%  | 70.12%             | -53.47% |    -0.09 |       68 | 54.24%     | ok               |

## LRCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 24.55%   | 419.19%            | -60.45% |     0.43 |       83 | 55.57%     | ok               |
|          50 | 17.37%   | 419.19%            | -50.39% |     0.37 |       80 | 37.44%     | ok               |
|          40 | 13.85%   | 419.19%            | -56.86% |     0.33 |       72 | 43.26%     | ok               |
|          35 | 6.46%    | 419.19%            | -61.76% |     0.25 |       80 | 45.26%     | ok               |
|          20 | 3.37%    | 419.19%            | -67.64% |     0.22 |       87 | 51.25%     | ok               |

## LTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -12.22%  | -64.31%            | -44.78% |    -0    |       56 | 31.80%     | ok               |
|          35 | -22.47%  | -64.31%            | -54.86% |    -0.13 |       66 | 42.91%     | ok               |
|          30 | -34.00%  | -64.31%            | -53.76% |    -0.29 |       66 | 48.47%     | ok               |
|          40 | -31.40%  | -64.31%            | -56.10% |    -0.3  |       58 | 38.12%     | ok               |
|          25 | -36.79%  | -64.31%            | -54.26% |    -0.33 |       74 | 50.96%     | ok               |

## MCD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 2.85%    | -5.04%             | -9.22%  |     0.19 |       42 | 20.63%     | ok               |
|          30 | -2.55%   | -5.04%             | -18.81% |    -0.05 |       75 | 38.10%     | ok               |
|          25 | -3.59%   | -5.04%             | -20.47% |    -0.09 |       75 | 40.77%     | ok               |
|          35 | -7.68%   | -5.04%             | -15.45% |    -0.29 |       67 | 34.44%     | ok               |
|          40 | -7.95%   | -5.04%             | -16.86% |    -0.33 |       71 | 28.79%     | ok               |

## META Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -5.54%   | 23.88%             | -31.03% |    -0    |       66 | 38.94%     | ok               |
|          40 | -15.92%  | 23.88%             | -35.11% |    -0.22 |       66 | 41.93%     | ok               |
|          50 | -19.96%  | 23.88%             | -34.00% |    -0.35 |       70 | 35.11%     | ok               |
|          25 | -24.22%  | 23.88%             | -39.84% |    -0.35 |       67 | 52.58%     | ok               |
|          30 | -26.25%  | 23.88%             | -38.96% |    -0.42 |       72 | 49.42%     | ok               |

## MPC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 14.51%   | 53.43%             | -23.96% |     0.37 |       52 | 38.60%     | ok               |
|          45 | 7.25%    | 53.43%             | -25.09% |     0.24 |       58 | 42.26%     | ok               |
|          40 | 5.62%    | 53.43%             | -25.70% |     0.22 |       60 | 44.59%     | ok               |
|          35 | 2.36%    | 53.43%             | -35.90% |     0.16 |       68 | 47.09%     | ok               |
|          30 | -13.74%  | 53.43%             | -44.76% |    -0.14 |       71 | 49.92%     | ok               |

## MRK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -21.48%  | 1.28%              | -30.12% |    -0.4  |       87 | 56.41%     | ok               |
|          25 | -21.11%  | 1.28%              | -31.07% |    -0.43 |       72 | 48.42%     | ok               |
|          20 | -24.97%  | 1.28%              | -29.59% |    -0.53 |       77 | 51.75%     | ok               |
|          45 | -23.91%  | 1.28%              | -26.02% |    -0.64 |       57 | 34.61%     | ok               |
|          50 | -23.57%  | 1.28%              | -25.69% |    -0.68 |       56 | 31.61%     | ok               |

## MS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -4.22%   | 142.79%            | -19.99% |    -0.02 |       70 | 41.10%     | ok               |
|          35 | -11.06%  | 142.79%            | -25.26% |    -0.2  |       76 | 45.92%     | ok               |
|          15 | -16.73%  | 142.79%            | -23.39% |    -0.29 |       79 | 58.40%     | ok               |
|          20 | -16.83%  | 142.79%            | -25.68% |    -0.32 |       83 | 54.58%     | ok               |
|          30 | -17.40%  | 142.79%            | -27.79% |    -0.36 |       80 | 49.75%     | ok               |

## MSFT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -18.41%  | -8.01%             | -26.27% |    -0.49 |       66 | 35.27%     | ok               |
|          50 | -22.08%  | -8.01%             | -28.83% |    -0.63 |       64 | 30.62%     | ok               |
|          35 | -30.11%  | -8.01%             | -33.68% |    -0.77 |       75 | 43.59%     | ok               |
|          25 | -33.52%  | -8.01%             | -37.59% |    -0.83 |       87 | 51.25%     | ok               |
|          40 | -30.94%  | -8.01%             | -34.46% |    -0.84 |       71 | 38.60%     | ok               |

## MU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 421.65%  | 1264.41%           | -61.96% |     1.55 |       48 | 68.05%     | ok               |
|          25 | 334.60%  | 1264.41%           | -67.90% |     1.46 |       49 | 61.73%     | ok               |
|          40 | 290.77%  | 1264.41%           | -64.07% |     1.4  |       56 | 55.24%     | ok               |
|          20 | 297.89%  | 1264.41%           | -67.25% |     1.37 |       55 | 63.89%     | ok               |
|          30 | 270.20%  | 1264.41%           | -68.76% |     1.34 |       51 | 59.90%     | ok               |

## NEAR-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 99.44%   | -63.19%            | -48.95% |     0.97 |       44 | 23.18%     | ok               |
|          50 | 70.90%   | -63.19%            | -53.13% |     0.82 |       38 | 18.39%     | ok               |
|          40 | 57.99%   | -63.19%            | -57.15% |     0.71 |       48 | 27.59%     | ok               |
|          35 | 31.48%   | -63.19%            | -61.02% |     0.51 |       70 | 32.95%     | ok               |
|          15 | 14.09%   | -63.19%            | -54.94% |     0.41 |       89 | 56.51%     | ok               |

## NEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 3.39%    | 177.48%            | -29.41% |     0.22 |       64 | 62.06%     | ok               |
|          20 | -7.68%   | 177.48%            | -30.47% |     0.07 |       74 | 57.57%     | ok               |
|          25 | -21.15%  | 177.48%            | -37.89% |    -0.14 |       70 | 55.41%     | ok               |
|          50 | -24.59%  | 177.48%            | -32.97% |    -0.26 |       58 | 40.60%     | ok               |
|          30 | -31.03%  | 177.48%            | -38.49% |    -0.33 |       74 | 53.74%     | ok               |

## NFLX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 69.59%   | 28.44%             | -11.94% |     1.32 |       46 | 47.25%     | ok               |
|          50 | 55.17%   | 28.44%             | -16.28% |     1.17 |       48 | 39.77%     | ok               |
|          35 | 60.87%   | 28.44%             | -18.30% |     1.14 |       60 | 50.75%     | ok               |
|          45 | 51.25%   | 28.44%             | -15.48% |     1.07 |       52 | 43.59%     | ok               |
|          25 | 49.48%   | 28.44%             | -21.09% |     0.94 |       60 | 57.24%     | ok               |

## NKE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -33.86%  | -59.99%            | -50.44% |    -0.42 |       93 | 52.58%     | ok               |
|          40 | -26.46%  | -59.99%            | -31.19% |    -0.5  |       63 | 30.12%     | ok               |
|          15 | -38.38%  | -59.99%            | -55.52% |    -0.51 |       91 | 56.91%     | ok               |
|          25 | -45.09%  | -59.99%            | -52.84% |    -0.79 |       91 | 48.59%     | ok               |
|          35 | -39.10%  | -59.99%            | -43.08% |    -0.8  |       75 | 37.10%     | ok               |

## NOW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 17.89%   | -36.15%            | -26.36% |     0.37 |       79 | 51.91%     | ok               |
|          30 | 17.37%   | -36.15%            | -30.25% |     0.37 |       80 | 45.92%     | ok               |
|          15 | 11.51%   | -36.15%            | -26.36% |     0.3  |       87 | 55.24%     | ok               |
|          25 | 10.70%   | -36.15%            | -25.70% |     0.29 |       72 | 49.25%     | ok               |
|          35 | 9.79%    | -36.15%            | -29.30% |     0.28 |       81 | 40.60%     | ok               |

## NVDA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -1.32%   | 132.92%            | -35.26% |     0.14 |       70 | 47.59%     | ok               |
|          25 | -3.29%   | 132.92%            | -33.22% |     0.12 |       68 | 50.27%     | ok               |
|          20 | -9.71%   | 132.92%            | -40.59% |     0.05 |       71 | 54.72%     | ok               |
|          35 | -14.66%  | 132.92%            | -41.25% |    -0.08 |       78 | 44.74%     | ok               |
|          50 | -14.29%  | 132.92%            | -40.84% |    -0.11 |       56 | 32.09%     | ok               |

## OP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 59.93%   | -93.91%            | -36.11% |     0.81 |       32 | 12.26%     | ok               |
|          45 | 58.78%   | -93.91%            | -45.76% |     0.75 |       34 | 16.86%     | ok               |
|          40 | 39.12%   | -93.91%            | -53.61% |     0.58 |       50 | 25.67%     | ok               |
|          35 | 15.79%   | -93.91%            | -58.33% |     0.38 |       58 | 28.74%     | ok               |
|          30 | -5.33%   | -93.91%            | -70.27% |     0.2  |       74 | 35.25%     | ok               |

## ORCL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 191.71%  | 27.10%             | -29.32% |     1.23 |       74 | 65.22%     | ok               |
|          25 | 118.83%  | 27.10%             | -27.76% |     0.97 |       75 | 57.74%     | ok               |
|          20 | 115.07%  | 27.10%             | -29.32% |     0.95 |       77 | 60.90%     | ok               |
|          35 | 87.62%   | 27.10%             | -31.95% |     0.84 |       68 | 49.42%     | ok               |
|          30 | 87.79%   | 27.10%             | -29.47% |     0.83 |       74 | 53.58%     | ok               |

## OXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 10.88%   | -15.63%            | -30.43% |     0.3  |       65 | 43.43%     | ok               |
|          35 | 6.25%    | -15.63%            | -30.89% |     0.23 |       68 | 38.94%     | ok               |
|          40 | 3.65%    | -15.63%            | -32.58% |     0.18 |       56 | 34.94%     | ok               |
|          50 | 1.65%    | -15.63%            | -30.54% |     0.14 |       34 | 27.45%     | ok               |
|          25 | -4.47%   | -15.63%            | -40.06% |     0.04 |       73 | 46.92%     | ok               |

## PEP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 12.74%   | -21.01%            | -11.62% |     0.57 |       48 | 27.29%     | ok               |
|          45 | 4.48%    | -21.01%            | -14.22% |     0.23 |       72 | 32.11%     | ok               |
|          40 | -1.62%   | -21.01%            | -18.04% |    -0    |       82 | 38.27%     | ok               |
|          35 | -2.35%   | -21.01%            | -21.42% |    -0.01 |       87 | 43.09%     | ok               |
|          30 | -7.99%   | -21.01%            | -21.35% |    -0.17 |       83 | 49.75%     | ok               |

## PEPE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 23.63%   | -83.63%            | -61.96% |     0.49 |       78 | 59.96%     | ok               |
|          30 | 23.59%   | -83.63%            | -57.66% |     0.46 |       79 | 44.44%     | ok               |
|          35 | 16.54%   | -83.63%            | -51.35% |     0.4  |       64 | 39.08%     | ok               |
|          25 | 1.14%    | -83.63%            | -53.88% |     0.29 |       85 | 49.62%     | ok               |
|          20 | -3.62%   | -83.63%            | -61.13% |     0.27 |       84 | 56.32%     | ok               |

## PFE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -25.36%  | -12.44%            | -26.20% |    -0.94 |       50 | 19.13%     | ok               |
|          35 | -33.10%  | -12.44%            | -34.83% |    -1.09 |       82 | 31.45%     | ok               |
|          50 | -26.63%  | -12.44%            | -27.45% |    -1.09 |       40 | 15.47%     | ok               |
|          40 | -31.68%  | -12.44%            | -32.39% |    -1.13 |       74 | 23.96%     | ok               |
|          30 | -39.30%  | -12.44%            | -40.87% |    -1.27 |       77 | 34.94%     | ok               |

## PG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -3.45%   | -7.75%             | -20.08% |    -0.09 |       54 | 34.94%     | ok               |
|          35 | -6.71%   | -7.75%             | -18.99% |    -0.22 |       62 | 38.44%     | ok               |
|          45 | -12.88%  | -7.75%             | -20.75% |    -0.54 |       54 | 32.45%     | ok               |
|          30 | -15.19%  | -7.75%             | -21.96% |    -0.56 |       64 | 41.60%     | ok               |
|          25 | -16.21%  | -7.75%             | -22.86% |    -0.6  |       74 | 42.76%     | ok               |

## PM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 0.75%    | 97.37%             | -32.20% |     0.11 |       88 | 53.74%     | ok               |
|          30 | -2.21%   | 97.37%             | -33.68% |     0.05 |       85 | 57.40%     | ok               |
|          20 | -2.46%   | 97.37%             | -31.89% |     0.05 |       89 | 62.56%     | ok               |
|          50 | -5.36%   | 97.37%             | -35.70% |    -0.05 |       76 | 42.76%     | ok               |
|          40 | -7.38%   | 97.37%             | -37.94% |    -0.09 |       82 | 49.92%     | ok               |

## POL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 83.81%   | -84.25%            | -46.45% |     0.88 |       81 | 51.15%     | ok               |
|          25 | 87.19%   | -84.25%            | -46.72% |     0.87 |       66 | 59.00%     | ok               |
|          20 | 72.79%   | -84.25%            | -52.88% |     0.78 |       72 | 63.22%     | ok               |
|          15 | 54.20%   | -84.25%            | -58.42% |     0.66 |       74 | 68.01%     | ok               |
|          50 | 18.38%   | -84.25%            | -22.86% |     0.42 |       52 | 20.88%     | ok               |

## QCOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 2.63%    | 28.24%             | -54.50% |     0.2  |       73 | 48.75%     | ok               |
|          35 | 0.80%    | 28.24%             | -50.58% |     0.17 |       79 | 44.43%     | ok               |
|          20 | -1.54%   | 28.24%             | -54.38% |     0.16 |       69 | 51.58%     | ok               |
|          30 | -10.63%  | 28.24%             | -56.59% |     0.03 |       75 | 46.92%     | ok               |
|          15 | -17.90%  | 28.24%             | -57.94% |    -0.06 |       73 | 54.74%     | ok               |

## QQQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 25.18%   | 72.22%             | -12.88% |     0.67 |       59 | 48.25%     | ok               |
|          15 | 25.72%   | 72.22%             | -14.17% |     0.63 |       63 | 53.74%     | ok               |
|          20 | 22.16%   | 72.22%             | -12.98% |     0.58 |       67 | 50.92%     | ok               |
|          30 | 20.05%   | 72.22%             | -12.88% |     0.57 |       64 | 45.26%     | ok               |
|          35 | 7.77%    | 72.22%             | -19.00% |     0.29 |       70 | 41.60%     | ok               |

## RENDER-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 57.70%   | -64.25%            | -43.43% |     0.69 |       86 | 54.03%     | ok               |
|          15 | 39.40%   | -64.25%            | -44.59% |     0.58 |       86 | 57.06%     | ok               |
|          25 | 26.45%   | -64.25%            | -40.60% |     0.5  |       90 | 50.20%     | ok               |
|          30 | -13.20%  | -64.25%            | -45.00% |     0.16 |       98 | 43.95%     | ok               |
|          35 | -26.78%  | -64.25%            | -41.33% |    -0.06 |       84 | 35.48%     | ok               |

## RTX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 26.48%   | 105.60%            | -18.66% |     0.65 |       78 | 56.24%     | ok               |
|          25 | 21.98%   | 105.60%            | -18.59% |     0.57 |       64 | 52.75%     | ok               |
|          30 | 20.13%   | 105.60%            | -16.99% |     0.53 |       58 | 51.58%     | ok               |
|          35 | 17.59%   | 105.60%            | -18.00% |     0.53 |       56 | 49.75%     | ok               |
|          50 | 16.28%   | 105.60%            | -18.42% |     0.53 |       60 | 41.93%     | ok               |

## SBUX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -15.77%  | 6.82%              | -23.55% |    -0.26 |       65 | 42.26%     | ok               |
|          40 | -19.95%  | 6.82%              | -26.97% |    -0.43 |       62 | 34.28%     | ok               |
|          30 | -22.96%  | 6.82%              | -29.34% |    -0.46 |       64 | 39.93%     | ok               |
|          45 | -20.39%  | 6.82%              | -27.26% |    -0.48 |       70 | 30.12%     | ok               |
|          35 | -24.47%  | 6.82%              | -30.20% |    -0.52 |       60 | 37.27%     | ok               |

## SCHW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -0.45%   | 49.09%             | -16.53% |     0.06 |       56 | 33.44%     | ok               |
|          50 | -4.29%   | 49.09%             | -13.28% |    -0.09 |       50 | 30.95%     | ok               |
|          25 | -12.81%  | 49.09%             | -28.76% |    -0.23 |       63 | 48.25%     | ok               |
|          40 | -10.77%  | 49.09%             | -23.35% |    -0.23 |       64 | 36.44%     | ok               |
|          20 | -14.44%  | 49.09%             | -29.24% |    -0.26 |       71 | 50.92%     | ok               |

## SHIB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 2.20%    | -78.14%            | -49.21% |     0.27 |       80 | 69.16%     | ok               |
|          25 | -5.59%   | -78.14%            | -43.85% |     0.18 |       77 | 59.96%     | ok               |
|          20 | -10.15%  | -78.14%            | -46.38% |     0.13 |       79 | 64.37%     | ok               |
|          35 | -8.92%   | -78.14%            | -53.32% |     0.11 |       66 | 47.13%     | ok               |
|          40 | -15.54%  | -78.14%            | -49.96% |     0.01 |       56 | 39.46%     | ok               |

## SHY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          30 | -2.24%   | 0.27%              | -2.85% |    -0.79 |       48 | 34.28%     | ok               |
|          35 | -2.36%   | 0.27%              | -3.27% |    -0.84 |       50 | 32.45%     | ok               |
|          40 | -2.47%   | 0.27%              | -3.33% |    -0.89 |       50 | 30.62%     | ok               |
|          45 | -2.45%   | 0.27%              | -3.23% |    -0.9  |       48 | 27.45%     | ok               |
|          50 | -2.62%   | 0.27%              | -3.40% |    -1.01 |       44 | 24.63%     | ok               |

## SKY-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -28.56%  | -10.01%            | -43.98% |    -0.35 |       70 | 41.23%     | ok               |
|          15 | -32.92%  | -10.01%            | -56.39% |    -0.35 |       60 | 51.48%     | ok               |
|          25 | -32.22%  | -10.01%            | -48.09% |    -0.4  |       65 | 44.87%     | ok               |
|          20 | -42.55%  | -10.01%            | -58.40% |    -0.59 |       62 | 48.52%     | ok               |
|          35 | -39.77%  | -10.01%            | -49.68% |    -0.7  |       64 | 34.85%     | ok               |

## SLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 21.82%   | -3.17%             | -23.07% |     0.52 |       46 | 35.94%     | ok               |
|          45 | 18.90%   | -3.17%             | -20.46% |     0.48 |       54 | 32.45%     | ok               |
|          50 | -4.32%   | -3.17%             | -30.82% |    -0.02 |       52 | 28.45%     | ok               |
|          35 | -8.77%   | -3.17%             | -41.81% |    -0.08 |       74 | 43.93%     | ok               |
|          30 | -24.42%  | -3.17%             | -54.95% |    -0.41 |       75 | 50.42%     | ok               |

## SLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 75.97%   | 160.70%            | -34.10% |     0.92 |       52 | 34.28%     | ok               |
|          45 | 73.18%   | 160.70%            | -31.82% |     0.9  |       56 | 35.11%     | ok               |
|          40 | 71.11%   | 160.70%            | -31.93% |     0.88 |       62 | 37.27%     | ok               |
|          35 | 57.57%   | 160.70%            | -36.89% |     0.77 |       64 | 39.43%     | ok               |
|          30 | 48.42%   | 160.70%            | -42.66% |     0.68 |       58 | 41.60%     | ok               |

## SMH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 119.46%  | 240.30%            | -30.17% |     1.34 |       47 | 52.41%     | ok               |
|          35 | 96.41%   | 240.30%            | -34.36% |     1.22 |       54 | 48.25%     | ok               |
|          25 | 96.27%   | 240.30%            | -32.94% |     1.2  |       46 | 51.25%     | ok               |
|          30 | 93.95%   | 240.30%            | -33.99% |     1.19 |       48 | 49.58%     | ok               |
|          45 | 79.84%   | 240.30%            | -32.75% |     1.15 |       52 | 42.43%     | ok               |

## SNX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 24.60%   | -86.83%            | -43.20% |     0.47 |       73 | 49.43%     | ok               |
|          35 | 1.49%    | -86.83%            | -30.08% |     0.26 |       66 | 31.99%     | ok               |
|          30 | -8.25%   | -86.83%            | -34.76% |     0.17 |       62 | 39.08%     | ok               |
|          25 | -11.82%  | -86.83%            | -38.88% |     0.15 |       74 | 43.87%     | ok               |
|          15 | -16.03%  | -86.83%            | -44.00% |     0.14 |       81 | 54.02%     | ok               |

## SOL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -7.64%   | -69.72%            | -51.20% |     0.16 |       64 | 38.89%     | ok               |
|          35 | -24.84%  | -69.72%            | -59.05% |    -0.01 |       72 | 46.36%     | ok               |
|          25 | -26.91%  | -69.72%            | -51.71% |    -0.02 |       72 | 56.90%     | ok               |
|          15 | -32.70%  | -69.72%            | -57.85% |    -0.07 |       76 | 63.98%     | ok               |
|          30 | -34.38%  | -69.72%            | -58.80% |    -0.13 |       80 | 52.49%     | ok               |

## SOXX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 101.25%  | 221.68%            | -38.67% |     1.18 |       53 | 51.08%     | ok               |
|          25 | 97.40%   | 221.68%            | -39.85% |     1.15 |       51 | 50.75%     | ok               |
|          35 | 91.88%   | 221.68%            | -38.63% |     1.13 |       59 | 46.09%     | ok               |
|          15 | 96.19%   | 221.68%            | -37.72% |     1.1  |       66 | 53.91%     | ok               |
|          30 | 86.31%   | 221.68%            | -40.34% |     1.07 |       55 | 48.59%     | ok               |

## SPY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 15.95%   | 51.17%             | -14.25% |     0.56 |       61 | 53.91%     | ok               |
|          15 | 14.37%   | 51.17%             | -16.80% |     0.5  |       70 | 57.07%     | ok               |
|          25 | 8.74%    | 51.17%             | -15.22% |     0.35 |       61 | 52.91%     | ok               |
|          30 | 4.03%    | 51.17%             | -16.47% |     0.2  |       62 | 50.25%     | ok               |
|          35 | 3.28%    | 51.17%             | -16.72% |     0.18 |       58 | 47.42%     | ok               |

## SUSHI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -23.49%  | -88.54%            | -40.08% |    -0.19 |       52 | 14.75%     | ok               |
|          45 | -55.77%  | -88.54%            | -64.27% |    -0.7  |       54 | 18.01%     | ok               |
|          40 | -58.91%  | -88.54%            | -66.57% |    -0.7  |       61 | 24.52%     | ok               |
|          15 | -76.99%  | -88.54%            | -78.98% |    -0.89 |       87 | 46.93%     | ok               |
|          35 | -71.87%  | -88.54%            | -78.94% |    -0.97 |       76 | 30.08%     | ok               |

## T Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 68.55%   | 17.55%             | -18.13% |     1.28 |       56 | 55.91%     | ok               |
|          25 | 63.32%   | 17.55%             | -17.66% |     1.22 |       58 | 53.74%     | ok               |
|          15 | 59.35%   | 17.55%             | -15.08% |     1.12 |       65 | 59.73%     | ok               |
|          30 | 45.43%   | 17.55%             | -17.01% |     0.98 |       62 | 51.75%     | ok               |
|          35 | 30.51%   | 17.55%             | -14.49% |     0.75 |       62 | 48.25%     | ok               |

## TGT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -10.52%  | -9.57%             | -41.89% |    -0.09 |       81 | 46.26%     | ok               |
|          25 | -11.41%  | -9.57%             | -42.39% |    -0.14 |       63 | 41.26%     | ok               |
|          15 | -13.45%  | -9.57%             | -39.76% |    -0.14 |       71 | 50.75%     | ok               |
|          45 | -10.66%  | -9.57%             | -29.07% |    -0.17 |       52 | 28.95%     | ok               |
|          30 | -12.27%  | -9.57%             | -40.57% |    -0.17 |       58 | 38.60%     | ok               |

## TIA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 13.81%   | -91.91%            | -44.86% |     0.36 |       32 | 11.49%     | ok               |
|          45 | 13.19%   | -91.91%            | -45.43% |     0.34 |       52 | 18.77%     | ok               |
|          35 | 4.43%    | -91.91%            | -42.77% |     0.27 |       66 | 30.84%     | ok               |
|          40 | 4.87%    | -91.91%            | -41.47% |     0.27 |       68 | 26.05%     | ok               |
|          15 | -44.86%  | -91.91%            | -53.14% |    -0.14 |       98 | 51.92%     | ok               |

## TLT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -20.23%  | -9.08%             | -20.97% |    -1.57 |       72 | 31.61%     | ok               |
|          50 | -14.98%  | -9.08%             | -15.73% |    -1.78 |       32 | 14.14%     | ok               |
|          15 | -26.04%  | -9.08%             | -27.29% |    -1.83 |       76 | 39.43%     | ok               |
|          35 | -21.46%  | -9.08%             | -21.60% |    -1.91 |       66 | 25.62%     | ok               |
|          40 | -20.01%  | -9.08%             | -20.01% |    -1.95 |       58 | 20.80%     | ok               |

## TMO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 42.91%   | -10.52%            | -8.17%  |     0.99 |       38 | 30.45%     | ok               |
|          45 | 33.33%   | -10.52%            | -10.13% |     0.78 |       44 | 35.11%     | ok               |
|          40 | 31.36%   | -10.52%            | -9.91%  |     0.73 |       47 | 39.60%     | ok               |
|          35 | 16.22%   | -10.52%            | -14.06% |     0.43 |       57 | 43.93%     | ok               |
|          30 | 8.05%    | -10.52%            | -18.85% |     0.26 |       57 | 48.09%     | ok               |

## TMUS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 20.83%   | 4.18%              | -26.87% |     0.5  |       69 | 59.73%     | ok               |
|          30 | 19.52%   | 4.18%              | -24.50% |     0.49 |       70 | 47.75%     | ok               |
|          20 | 11.07%   | 4.18%              | -25.10% |     0.32 |       73 | 53.91%     | ok               |
|          25 | 10.08%   | 4.18%              | -26.30% |     0.31 |       75 | 50.25%     | ok               |
|          35 | 6.17%    | 4.18%              | -30.40% |     0.23 |       68 | 44.43%     | ok               |

## TRX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 4.06%    | 27.55%             | -18.79% |     0.2  |       54 | 37.55%     | ok               |
|          50 | 0.66%    | 27.55%             | -18.49% |     0.1  |       44 | 31.99%     | ok               |
|          30 | -1.66%   | 27.55%             | -22.90% |     0.05 |       74 | 49.43%     | ok               |
|          35 | -2.48%   | 27.55%             | -21.77% |     0.02 |       70 | 46.17%     | ok               |
|          25 | -3.43%   | 27.55%             | -26.84% |     0    |       70 | 52.68%     | ok               |

## TSLA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 88.36%   | 127.23%            | -30.67% |     0.93 |       60 | 34.28%     | ok               |
|          45 | 59.58%   | 127.23%            | -31.89% |     0.74 |       64 | 31.61%     | ok               |
|          50 | 52.31%   | 127.23%            | -32.60% |     0.69 |       66 | 30.12%     | ok               |
|          35 | 47.06%   | 127.23%            | -37.58% |     0.62 |       71 | 37.10%     | ok               |
|          30 | 19.34%   | 127.23%            | -42.22% |     0.38 |       67 | 41.60%     | ok               |

## TXN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 13.38%   | 88.21%             | -45.45% |     0.33 |       72 | 35.77%     | ok               |
|          20 | 2.88%    | 88.21%             | -38.98% |     0.19 |       62 | 59.90%     | ok               |
|          15 | 0.75%    | 88.21%             | -39.48% |     0.17 |       65 | 64.06%     | ok               |
|          35 | -5.44%   | 88.21%             | -43.38% |     0.05 |       78 | 50.42%     | ok               |
|          40 | -6.08%   | 88.21%             | -45.67% |     0.04 |       76 | 48.25%     | ok               |

## UNH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 30.37%   | -18.61%            | -37.02% |     0.55 |       52 | 30.28%     | ok               |
|          30 | 27.08%   | -18.61%            | -27.86% |     0.49 |       74 | 52.41%     | ok               |
|          35 | 23.62%   | -18.61%            | -29.20% |     0.45 |       66 | 47.25%     | ok               |
|          15 | 21.33%   | -18.61%            | -33.62% |     0.42 |       75 | 67.39%     | ok               |
|          40 | 19.08%   | -18.61%            | -35.94% |     0.4  |       60 | 42.43%     | ok               |

## UNI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -18.00%  | -75.71%            | -58.49% |    -0    |       56 | 25.86%     | ok               |
|          40 | -23.38%  | -75.71%            | -63.75% |    -0.05 |       58 | 30.84%     | ok               |
|          50 | -25.51%  | -75.71%            | -57.60% |    -0.14 |       52 | 21.07%     | ok               |
|          35 | -35.69%  | -75.71%            | -68.71% |    -0.18 |       72 | 35.82%     | ok               |
|          20 | -72.95%  | -75.71%            | -80.75% |    -0.75 |      103 | 52.30%     | ok               |

## UPS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -34.94%  | -26.33%            | -44.52% |    -0.65 |       84 | 48.25%     | ok               |
|          35 | -34.22%  | -26.33%            | -38.61% |    -0.69 |       61 | 34.28%     | ok               |
|          25 | -35.97%  | -26.33%            | -40.93% |    -0.7  |       80 | 44.76%     | ok               |
|          40 | -34.67%  | -26.33%            | -39.56% |    -0.72 |       53 | 28.79%     | ok               |
|          30 | -36.62%  | -26.33%            | -38.76% |    -0.73 |       72 | 40.27%     | ok               |

## USO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 16.31%   | 54.69%             | -33.25% |     0.38 |       48 | 26.62%     | ok               |
|          30 | 8.43%    | 54.69%             | -43.35% |     0.26 |       66 | 34.11%     | ok               |
|          40 | 4.41%    | 54.69%             | -41.14% |     0.2  |       59 | 29.28%     | ok               |
|          15 | 3.35%    | 54.69%             | -46.93% |     0.18 |       73 | 41.93%     | ok               |
|          50 | 3.92%    | 54.69%             | -31.13% |     0.18 |       52 | 24.13%     | ok               |

## VEA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 5.44%    | 49.94%             | -16.28% |     0.25 |       60 | 50.58%     | ok               |
|          20 | 1.19%    | 49.94%             | -17.70% |     0.1  |       61 | 47.92%     | ok               |
|          25 | -0.82%   | 49.94%             | -17.79% |     0.02 |       57 | 46.26%     | ok               |
|          30 | -0.98%   | 49.94%             | -17.93% |     0.01 |       58 | 44.09%     | ok               |
|          35 | -2.09%   | 49.94%             | -16.79% |    -0.03 |       56 | 43.09%     | ok               |

## VIXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -48.04%  | -62.01%            | -69.78% |    -0.43 |       46 | 10.48%     | ok               |
|          45 | -59.37%  | -62.01%            | -75.03% |    -0.61 |       60 | 16.64%     | ok               |
|          40 | -67.66%  | -62.01%            | -80.72% |    -0.74 |       76 | 21.46%     | ok               |
|          35 | -70.62%  | -62.01%            | -84.37% |    -0.76 |       90 | 26.79%     | ok               |
|          15 | -77.15%  | -62.01%            | -89.47% |    -0.77 |      101 | 44.76%     | ok               |

## VNQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -8.60%   | 15.22%             | -19.07% |    -0.37 |       60 | 28.62%     | ok               |
|          50 | -9.03%   | 15.22%             | -17.13% |    -0.41 |       56 | 26.12%     | ok               |
|          25 | -13.12%  | 15.22%             | -22.34% |    -0.51 |       69 | 40.77%     | ok               |
|          40 | -14.13%  | 15.22%             | -24.84% |    -0.62 |       74 | 32.11%     | ok               |
|          20 | -16.52%  | 15.22%             | -23.79% |    -0.64 |       74 | 43.59%     | ok               |

## VTI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 19.94%   | 51.13%             | -13.96% |     0.66 |       64 | 54.91%     | ok               |
|          15 | 13.80%   | 51.13%             | -15.70% |     0.48 |       67 | 57.40%     | ok               |
|          25 | 6.11%    | 51.13%             | -16.10% |     0.27 |       58 | 52.91%     | ok               |
|          30 | -0.94%   | 51.13%             | -18.77% |     0.03 |       66 | 51.08%     | ok               |
|          40 | -3.16%   | 51.13%             | -20.44% |    -0.06 |       68 | 44.43%     | ok               |

## VWO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -7.30%   | 46.62%             | -21.18% |    -0.25 |       60 | 32.61%     | ok               |
|          15 | -9.03%   | 46.62%             | -24.01% |    -0.26 |       69 | 49.42%     | ok               |
|          20 | -10.06%  | 46.62%             | -26.14% |    -0.31 |       67 | 47.25%     | ok               |
|          40 | -8.98%   | 46.62%             | -23.57% |    -0.31 |       70 | 37.94%     | ok               |
|          45 | -9.11%   | 46.62%             | -23.26% |    -0.33 |       62 | 35.11%     | ok               |

## VZ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -8.40%   | 3.02%              | -12.73% |    -0.25 |       52 | 24.46%     | ok               |
|          45 | -16.62%  | 3.02%              | -19.37% |    -0.54 |       60 | 27.45%     | ok               |
|          25 | -23.89%  | 3.02%              | -25.51% |    -0.71 |       83 | 41.26%     | ok               |
|          35 | -21.55%  | 3.02%              | -20.82% |    -0.71 |       63 | 32.95%     | ok               |
|          40 | -24.27%  | 3.02%              | -22.97% |    -0.85 |       66 | 29.95%     | ok               |

## WFC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -1.40%   | 71.13%             | -18.29% |     0.02 |       58 | 34.11%     | ok               |
|          35 | -7.39%   | 71.13%             | -22.53% |    -0.09 |       79 | 46.09%     | ok               |
|          45 | -10.30%  | 71.13%             | -24.02% |    -0.23 |       66 | 39.10%     | ok               |
|          20 | -18.00%  | 71.13%             | -29.87% |    -0.26 |       79 | 55.07%     | ok               |
|          40 | -13.89%  | 71.13%             | -24.88% |    -0.34 |       76 | 42.43%     | ok               |

## WIF-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 60.65%   | -86.61%            | -46.21% |     0.66 |       71 | 41.38%     | ok               |
|          20 | 54.98%   | -86.61%            | -40.67% |     0.64 |       65 | 38.70%     | ok               |
|          25 | -11.37%  | -86.61%            | -52.41% |     0.2  |       67 | 36.21%     | ok               |
|          50 | -24.32%  | -86.61%            | -41.18% |    -0.22 |       42 | 12.26%     | ok               |
|          30 | -43.81%  | -86.61%            | -57.06% |    -0.24 |       68 | 32.18%     | ok               |

## WMT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 56.54%   | 100.09%            | -9.18%  |     1.49 |       36 | 42.93%     | ok               |
|          50 | 50.18%   | 100.09%            | -12.19% |     1.42 |       30 | 40.77%     | ok               |
|          40 | 46.75%   | 100.09%            | -9.18%  |     1.25 |       40 | 44.09%     | ok               |
|          35 | 43.99%   | 100.09%            | -10.48% |     1.16 |       52 | 48.25%     | ok               |
|          30 | 19.81%   | 100.09%            | -21.31% |     0.57 |       59 | 50.92%     | ok               |

## XBI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 8.68%    | 76.30%             | -16.56% |     0.29 |       62 | 35.27%     | ok               |
|          45 | 7.85%    | 76.30%             | -16.74% |     0.28 |       54 | 32.11%     | ok               |
|          35 | 7.37%    | 76.30%             | -18.84% |     0.26 |       62 | 38.77%     | ok               |
|          30 | 6.18%    | 76.30%             | -19.80% |     0.23 |       62 | 40.43%     | ok               |
|          25 | 1.29%    | 76.30%             | -23.66% |     0.12 |       70 | 42.43%     | ok               |

## XLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -1.55%   | 23.36%             | -20.60% |    -0    |       58 | 31.78%     | ok               |
|          50 | -1.49%   | 23.36%             | -17.40% |    -0.01 |       42 | 27.45%     | ok               |
|          45 | -4.40%   | 23.36%             | -20.61% |    -0.13 |       42 | 28.95%     | ok               |
|          35 | -4.89%   | 23.36%             | -23.62% |    -0.13 |       58 | 35.27%     | ok               |
|          25 | -8.18%   | 23.36%             | -23.73% |    -0.24 |       66 | 40.93%     | ok               |

## XLC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 16.58%   | 36.68%             | -12.33% |     0.58 |       65 | 55.57%     | ok               |
|          25 | 14.39%   | 36.68%             | -12.31% |     0.51 |       62 | 57.40%     | ok               |
|          40 | 11.29%   | 36.68%             | -13.38% |     0.45 |       68 | 48.09%     | ok               |
|          35 | 11.26%   | 36.68%             | -13.38% |     0.44 |       64 | 52.58%     | ok               |
|          20 | 6.34%    | 36.68%             | -13.78% |     0.26 |       70 | 60.07%     | ok               |

## XLE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.02%   | 27.09%             | -25.98% |     0.07 |       54 | 36.94%     | ok               |
|          35 | -3.79%   | 27.09%             | -32.17% |    -0.02 |       65 | 44.59%     | ok               |
|          45 | -5.17%   | 27.09%             | -30.88% |    -0.07 |       62 | 39.60%     | ok               |
|          25 | -11.35%  | 27.09%             | -37.50% |    -0.2  |       81 | 49.92%     | ok               |
|          30 | -11.37%  | 27.09%             | -37.51% |    -0.22 |       73 | 46.76%     | ok               |

## XLF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -5.82%   | 38.06%             | -18.01% |    -0.14 |       68 | 53.91%     | ok               |
|          15 | -9.72%   | 38.06%             | -19.58% |    -0.27 |       76 | 56.74%     | ok               |
|          30 | -11.63%  | 38.06%             | -23.61% |    -0.38 |       76 | 48.25%     | ok               |
|          25 | -12.39%  | 38.06%             | -23.22% |    -0.4  |       77 | 50.42%     | ok               |
|          35 | -17.69%  | 38.06%             | -25.31% |    -0.7  |       66 | 44.76%     | ok               |

## XLI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 9.15%    | 59.71%             | -10.36% |     0.37 |       72 | 52.41%     | ok               |
|          20 | 5.07%    | 59.71%             | -12.74% |     0.24 |       63 | 48.09%     | ok               |
|          30 | 2.77%    | 59.71%             | -11.38% |     0.16 |       64 | 45.59%     | ok               |
|          50 | 2.18%    | 59.71%             | -9.25%  |     0.15 |       56 | 34.94%     | ok               |
|          45 | 2.18%    | 59.71%             | -12.27% |     0.14 |       62 | 36.77%     | ok               |

## XLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 84.80%   | 88.85%             | -14.75% |     1.35 |       41 | 52.58%     | ok               |
|          20 | 70.34%   | 88.85%             | -14.75% |     1.21 |       48 | 50.42%     | ok               |
|          25 | 66.87%   | 88.85%             | -14.75% |     1.21 |       42 | 48.25%     | ok               |
|          30 | 64.69%   | 88.85%             | -14.75% |     1.2  |       42 | 47.09%     | ok               |
|          35 | 46.32%   | 88.85%             | -13.61% |     0.97 |       54 | 44.43%     | ok               |

## XLM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 26.14%   | -52.34%            | -38.97% |     0.48 |       44 | 27.39%     | ok               |
|          45 | 22.34%   | -52.34%            | -43.99% |     0.44 |       50 | 31.03%     | ok               |
|          30 | 0.26%    | -52.34%            | -50.36% |     0.22 |       69 | 45.59%     | ok               |
|          40 | -3.03%   | -52.34%            | -43.80% |     0.17 |       49 | 35.25%     | ok               |
|          35 | -8.51%   | -52.34%            | -50.42% |     0.12 |       69 | 41.57%     | ok               |

## XLP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 11.69%   | 12.44%             | -5.66%  |     0.71 |       54 | 34.28%     | ok               |
|          50 | 9.69%    | 12.44%             | -6.08%  |     0.61 |       58 | 31.78%     | ok               |
|          40 | 9.44%    | 12.44%             | -7.77%  |     0.57 |       70 | 38.44%     | ok               |
|          35 | 8.49%    | 12.44%             | -9.73%  |     0.51 |       66 | 41.43%     | ok               |
|          30 | 6.56%    | 12.44%             | -11.16% |     0.4  |       68 | 42.93%     | ok               |

## XLU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 9.32%    | 50.06%             | -10.12% |     0.49 |       48 | 29.95%     | ok               |
|          45 | 7.00%    | 50.06%             | -11.91% |     0.38 |       54 | 30.95%     | ok               |
|          40 | 4.05%    | 50.06%             | -13.27% |     0.24 |       58 | 32.45%     | ok               |
|          35 | -2.01%   | 50.06%             | -17.50% |    -0.05 |       62 | 34.61%     | ok               |
|          30 | -5.08%   | 50.06%             | -19.39% |    -0.19 |       69 | 37.60%     | ok               |

## XLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -12.12%  | 10.20%             | -16.83% |    -0.59 |       66 | 35.61%     | ok               |
|          25 | -13.41%  | 10.20%             | -18.06% |    -0.66 |       68 | 36.94%     | ok               |
|          15 | -17.34%  | 10.20%             | -21.47% |    -0.84 |       79 | 41.76%     | ok               |
|          20 | -17.27%  | 10.20%             | -21.56% |    -0.86 |       73 | 38.60%     | ok               |
|          50 | -14.45%  | 10.20%             | -18.24% |    -0.87 |       54 | 24.29%     | ok               |

## XLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 5.14%    | 33.36%             | -12.94% |     0.23 |       70 | 41.43%     | ok               |
|          30 | 3.26%    | 33.36%             | -14.01% |     0.17 |       70 | 44.43%     | ok               |
|          15 | 1.20%    | 33.36%             | -15.77% |     0.11 |       74 | 51.25%     | ok               |
|          50 | 1.30%    | 33.36%             | -11.79% |     0.1  |       50 | 29.62%     | ok               |
|          40 | -1.91%   | 33.36%             | -16.99% |    -0.01 |       68 | 37.10%     | ok               |

## XOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 5.44%    | 33.71%             | -19.90% |     0.22 |       58 | 37.44%     | ok               |
|          30 | 4.39%    | 33.71%             | -20.29% |     0.2  |       58 | 36.77%     | ok               |
|          50 | 1.92%    | 33.71%             | -21.35% |     0.13 |       46 | 29.95%     | ok               |
|          20 | 1.54%    | 33.71%             | -25.56% |     0.12 |       63 | 39.93%     | ok               |
|          35 | -0.05%   | 33.71%             | -20.93% |     0.07 |       60 | 35.61%     | ok               |

## XRP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -24.02%  | -65.92%            | -46.89% |    -0.12 |       70 | 40.42%     | ok               |
|          40 | -31.08%  | -65.92%            | -44.90% |    -0.27 |       62 | 34.29%     | ok               |
|          30 | -38.27%  | -65.92%            | -56.11% |    -0.35 |       74 | 44.83%     | ok               |
|          45 | -38.84%  | -65.92%            | -46.85% |    -0.44 |       62 | 29.89%     | ok               |
|          50 | -36.16%  | -65.92%            | -39.26% |    -0.49 |       62 | 22.22%     | ok               |

## YFI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -32.83%  | -77.82%            | -52.37% |    -0.46 |       62 | 27.20%     | ok               |
|          45 | -38.27%  | -77.82%            | -54.04% |    -0.66 |       64 | 22.61%     | ok               |
|          35 | -49.34%  | -77.82%            | -64.08% |    -0.73 |       73 | 34.67%     | ok               |
|          30 | -52.55%  | -77.82%            | -67.78% |    -0.75 |       81 | 40.80%     | ok               |
|          50 | -41.48%  | -77.82%            | -51.80% |    -0.84 |       52 | 17.43%     | ok               |

## ZEC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 134.63%  | 776.88%            | -24.66% |     0.94 |       46 | 23.18%     | ok               |
|          35 | 103.21%  | 776.88%            | -44.34% |     0.81 |       54 | 30.65%     | ok               |
|          25 | 75.32%   | 776.88%            | -48.59% |     0.7  |       58 | 39.66%     | ok               |
|          50 | 61.29%   | 776.88%            | -37.62% |     0.64 |       48 | 20.69%     | ok               |
|          30 | 56.52%   | 776.88%            | -47.68% |     0.62 |       64 | 36.21%     | ok               |
