# Market Tracker Backtest Report

_Generated: 2026-11-13T06:30:50+00:00_

## Data Sources

- Crypto: Kraken -> Coinbase -> CoinGecko OHLC -> CoinPaprika fallback chain.
- Stocks / ETFs / indices: Stooq -> Yahoo Finance fallback chain.
- Data rows are generated from real market APIs. Mock OHLCV rows are not generated.

## Data Freshness

- Rows: **92,791**
- Symbols: **161**
- Date range: **2024-06-24** to **2026-11-13**

## Latest Signals

| symbol     | date                |         close |   composite_score | signal   | data_source   |
|:-----------|:--------------------|--------------:|------------------:|:---------|:--------------|
| AMD        | 2026-11-12 00:00:00 |   585.3       |         67.4167   | LONG     | Yahoo Finance |
| AMGN       | 2026-11-12 00:00:00 |   467.06      |         55.75     | LONG     | Yahoo Finance |
| AVGO       | 2026-11-12 00:00:00 |   364.36      |         51.4167   | LONG     | Yahoo Finance |
| BLK        | 2026-11-12 00:00:00 |  1216.61      |         74.4167   | LONG     | Yahoo Finance |
| CL         | 2026-11-12 00:00:00 |    97.9       |         51.0833   | LONG     | Yahoo Finance |
| CMCSA      | 2026-11-12 00:00:00 |    24.8       |         34.4167   | LONG     | Yahoo Finance |
| COST       | 2026-11-12 00:00:00 |  1092.21      |         58.75     | LONG     | Yahoo Finance |
| DE         | 2026-11-12 00:00:00 |   678.79      |         51.9167   | LONG     | Yahoo Finance |
| DIS        | 2026-11-12 00:00:00 |   118.23      |         71.0833   | LONG     | Yahoo Finance |
| DXY-INDEX  | 2026-11-13 00:00:00 |   103.201     |         72.8495   | LONG     | Yahoo Finance |
| EOG        | 2026-11-12 00:00:00 |   155.62      |         40.4167   | LONG     | Yahoo Finance |
| GE         | 2026-11-12 00:00:00 |   330.86      |         66.3333   | LONG     | Yahoo Finance |
| HD         | 2026-11-12 00:00:00 |   348.26      |         56.4167   | LONG     | Yahoo Finance |
| JNJ        | 2026-11-12 00:00:00 |   283.52      |         60.5833   | LONG     | Yahoo Finance |
| JPM        | 2026-11-12 00:00:00 |   342.82      |         70.4167   | LONG     | Yahoo Finance |
| KO         | 2026-11-12 00:00:00 |    97.44      |         72.75     | LONG     | Yahoo Finance |
| LIN        | 2026-11-12 00:00:00 |   522.49      |         49.4167   | LONG     | Yahoo Finance |
| LLY        | 2026-11-12 00:00:00 |  1427.28      |         71.5833   | LONG     | Yahoo Finance |
| MCD        | 2026-11-12 00:00:00 |   273.63      |         31.5      | LONG     | Yahoo Finance |
| MRK        | 2026-11-12 00:00:00 |   146.95      |         69.0833   | LONG     | Yahoo Finance |
| PEP        | 2026-11-12 00:00:00 |   142.26      |         61.8333   | LONG     | Yahoo Finance |
| PG         | 2026-11-12 00:00:00 |   168.03      |         72.75     | LONG     | Yahoo Finance |
| RTX        | 2026-11-12 00:00:00 |   198.36      |         52.3333   | LONG     | Yahoo Finance |
| SBUX       | 2026-11-12 00:00:00 |   107.26      |         55.9167   | LONG     | Yahoo Finance |
| UNH        | 2026-11-12 00:00:00 |   405.13      |         36.4167   | LONG     | Yahoo Finance |
| UPS        | 2026-11-12 00:00:00 |   110.38      |         55.9167   | LONG     | Yahoo Finance |
| VNQ        | 2026-11-12 00:00:00 |    96.44      |         59.5833   | LONG     | Yahoo Finance |
| WFC        | 2026-11-12 00:00:00 |    85.76      |         76.9167   | LONG     | Yahoo Finance |
| WMT        | 2026-11-12 00:00:00 |   126.19      |         36.0833   | LONG     | Yahoo Finance |
| XLB        | 2026-11-12 00:00:00 |    52.34      |         35.5833   | LONG     | Yahoo Finance |
| XLF        | 2026-11-12 00:00:00 |    58.21      |         71.4167   | LONG     | Yahoo Finance |
| XLP        | 2026-11-12 00:00:00 |    91.06      |         53.0833   | LONG     | Yahoo Finance |
| XLU        | 2026-11-12 00:00:00 |    43.81      |         65.8333   | LONG     | Yahoo Finance |
| XLV        | 2026-11-12 00:00:00 |   187.83      |         73.5833   | LONG     | Yahoo Finance |
| XLY        | 2026-11-12 00:00:00 |   120.46      |         61.4167   | LONG     | Yahoo Finance |
| AAPL       | 2026-11-12 00:00:00 |   354.88      |         57.8333   | NEUTRAL  | Yahoo Finance |
| ABBV       | 2026-11-12 00:00:00 |   294.45      |         44.5      | NEUTRAL  | Yahoo Finance |
| ADBE       | 2026-11-12 00:00:00 |   238.54      |        -44.0833   | NEUTRAL  | Yahoo Finance |
| AMZN       | 2026-11-12 00:00:00 |   267.44      |         65.3333   | NEUTRAL  | Yahoo Finance |
| ARB-USD    | 2026-11-13 00:00:00 |     0.1453    |        -43.75     | NEUTRAL  | Kraken API    |
| ATOM-USD   | 2026-11-13 00:00:00 |     1.3891    |        -20.9167   | NEUTRAL  | Kraken API    |
| AVAX-USD   | 2026-11-13 00:00:00 |     8.168     |         -9.41667  | NEUTRAL  | Kraken API    |
| BAC        | 2026-11-12 00:00:00 |    50.51      |        -23.75     | NEUTRAL  | Yahoo Finance |
| BONK-USD   | 2026-11-13 00:00:00 |     2.645e-06 |        -59.25     | NEUTRAL  | Kraken API    |
| C          | 2026-11-12 00:00:00 |   124.06      |         -3.08333  | NEUTRAL  | Yahoo Finance |
| COMP-USD   | 2026-11-13 00:00:00 |    19.59      |        -22.5      | NEUTRAL  | Kraken API    |
| COP        | 2026-11-12 00:00:00 |   140.06      |          3.25     | NEUTRAL  | Yahoo Finance |
| CRM        | 2026-11-12 00:00:00 |   217.57      |        -14.8333   | NEUTRAL  | Yahoo Finance |
| CSCO       | 2026-11-12 00:00:00 |   102.01      |        -22.8333   | NEUTRAL  | Yahoo Finance |
| CVX        | 2026-11-12 00:00:00 |   216.35      |        -14.75     | NEUTRAL  | Yahoo Finance |
| DBC        | 2026-11-12 00:00:00 |    30.91      |        -18.3333   | NEUTRAL  | Yahoo Finance |
| DIA        | 2026-11-12 00:00:00 |   522.47      |         58.0833   | NEUTRAL  | Yahoo Finance |
| DOT-USD    | 2026-11-13 00:00:00 |     0.8149    |        -55.5833   | NEUTRAL  | Kraken API    |
| EFA        | 2026-11-12 00:00:00 |   104.01      |         20        | NEUTRAL  | Yahoo Finance |
| FET-USD    | 2026-11-13 00:00:00 |     0.1441    |        -22.6667   | NEUTRAL  | Kraken API    |
| FXI        | 2026-11-12 00:00:00 |    33.48      |         -1.91667  | NEUTRAL  | Yahoo Finance |
| GDX        | 2026-11-12 00:00:00 |    81.84      |        -30.8333   | NEUTRAL  | Yahoo Finance |
| GDXJ       | 2026-11-12 00:00:00 |    99.62      |        -32.8333   | NEUTRAL  | Yahoo Finance |
| GLD        | 2026-11-12 00:00:00 |   354.89      |        -60        | NEUTRAL  | Yahoo Finance |
| GS         | 2026-11-12 00:00:00 |   913.6       |         -2        | NEUTRAL  | Yahoo Finance |
| HON        | 2026-11-12 00:00:00 |   223.45      |         48.4167   | NEUTRAL  | Yahoo Finance |
| HYG        | 2026-11-12 00:00:00 |    76.98      |        -19.9167   | NEUTRAL  | Yahoo Finance |
| IBM        | 2026-11-12 00:00:00 |   244.67      |        -10.5833   | NEUTRAL  | Yahoo Finance |
| ICP-USD    | 2026-11-13 00:00:00 |     2.566     |         17        | NEUTRAL  | Kraken API    |
| INJ-USD    | 2026-11-13 00:00:00 |     7.303     |          1.33333  | NEUTRAL  | Kraken API    |
| INTU       | 2026-11-12 00:00:00 |   340.17      |         14.9167   | NEUTRAL  | Yahoo Finance |
| ITA        | 2026-11-12 00:00:00 |    71.73      |         22.6667   | NEUTRAL  | Yahoo Finance |
| IWM        | 2026-11-12 00:00:00 |   278.44      |         12.75     | NEUTRAL  | Yahoo Finance |
| LINK-USD   | 2026-11-13 00:00:00 |     9.77945   |        -61.3333   | NEUTRAL  | Kraken API    |
| LRCX       | 2026-11-12 00:00:00 |   233.78      |        -27.0833   | NEUTRAL  | Yahoo Finance |
| META       | 2026-11-12 00:00:00 |   623.61      |        -13.25     | NEUTRAL  | Yahoo Finance |
| MPC        | 2026-11-12 00:00:00 |   412.85      |          0.916667 | NEUTRAL  | Yahoo Finance |
| MS         | 2026-11-12 00:00:00 |   189.17      |         -5.08333  | NEUTRAL  | Yahoo Finance |
| MSFT       | 2026-11-12 00:00:00 |   523         |         -2.16667  | NEUTRAL  | Yahoo Finance |
| MU         | 2026-11-12 00:00:00 |   798.44      |        -14.8333   | NEUTRAL  | Yahoo Finance |
| NEAR-USD   | 2026-11-13 00:00:00 |     3.4017    |        -24.8333   | NEUTRAL  | Kraken API    |
| NEM        | 2026-11-12 00:00:00 |   112.64      |          4.91667  | NEUTRAL  | Yahoo Finance |
| NKE        | 2026-11-12 00:00:00 |    37.76      |        -14.9167   | NEUTRAL  | Yahoo Finance |
| ORCL       | 2026-11-12 00:00:00 |   127.11      |        -12.5      | NEUTRAL  | Yahoo Finance |
| PEPE-USD   | 2026-11-13 00:00:00 |     4.532e-06 |         14.4167   | NEUTRAL  | Kraken API    |
| PFE        | 2026-11-12 00:00:00 |    28.83      |          5.41667  | NEUTRAL  | Yahoo Finance |
| PM         | 2026-11-12 00:00:00 |   196.66      |         -3.33333  | NEUTRAL  | Yahoo Finance |
| QCOM       | 2026-11-12 00:00:00 |   177.14      |         54.25     | NEUTRAL  | Yahoo Finance |
| QQQ        | 2026-11-12 00:00:00 |   688.17      |        -10.5833   | NEUTRAL  | Yahoo Finance |
| RENDER-USD | 2026-11-13 00:00:00 |     1.491     |        -20.6667   | NEUTRAL  | Kraken API    |
| SCHW       | 2026-11-12 00:00:00 |    91.72      |        -16.0833   | NEUTRAL  | Yahoo Finance |
| SLB        | 2026-11-12 00:00:00 |    50.91      |        -40.75     | NEUTRAL  | Yahoo Finance |
| SNX-USD    | 2026-11-13 00:00:00 |     0.1579    |        -29.8333   | NEUTRAL  | Kraken API    |
| SPY        | 2026-11-12 00:00:00 |   757.12      |         -1.08333  | NEUTRAL  | Yahoo Finance |
| T          | 2026-11-12 00:00:00 |    22.18      |          1.08333  | NEUTRAL  | Yahoo Finance |
| TGT        | 2026-11-12 00:00:00 |   160.9       |         60.3333   | NEUTRAL  | Yahoo Finance |
| TMO        | 2026-11-12 00:00:00 |   699.44      |         28.8333   | NEUTRAL  | Yahoo Finance |
| TMUS       | 2026-11-12 00:00:00 |   171.03      |         23.5      | NEUTRAL  | Yahoo Finance |
| TSLA       | 2026-11-12 00:00:00 |   397.45      |         30.3333   | NEUTRAL  | Yahoo Finance |
| TXN        | 2026-11-12 00:00:00 |   312.48      |         52.1667   | NEUTRAL  | Yahoo Finance |
| USO        | 2026-11-12 00:00:00 |   146.07      |        -20.0833   | NEUTRAL  | Yahoo Finance |
| VEA        | 2026-11-12 00:00:00 |    69.43      |         -1.5      | NEUTRAL  | Yahoo Finance |
| VTI        | 2026-11-12 00:00:00 |   372.62      |          2.41667  | NEUTRAL  | Yahoo Finance |
| VWO        | 2026-11-12 00:00:00 |    56.43      |        -24.5      | NEUTRAL  | Yahoo Finance |
| VZ         | 2026-11-12 00:00:00 |    46.55      |         48.5833   | NEUTRAL  | Yahoo Finance |
| XBI        | 2026-11-12 00:00:00 |   151.2       |         17.5      | NEUTRAL  | Yahoo Finance |
| XLC        | 2026-11-12 00:00:00 |   107.56      |          5.66667  | NEUTRAL  | Yahoo Finance |
| XLI        | 2026-11-12 00:00:00 |   169.44      |          5.41667  | NEUTRAL  | Yahoo Finance |
| XLK        | 2026-11-12 00:00:00 |   173.77      |         -6.83333  | NEUTRAL  | Yahoo Finance |
| XOM        | 2026-11-12 00:00:00 |   169.78      |         -5.75     | NEUTRAL  | Yahoo Finance |
| ZEC-USD    | 2026-11-13 00:00:00 |   939.27      |        -37.8333   | NEUTRAL  | Kraken API    |
| AAVE-USD   | 2026-11-13 00:00:00 |   111.14      |        -30.25     | SHORT    | Kraken API    |
| ADA-USD    | 2026-11-13 00:00:00 |     0.169262  |        -37.5833   | SHORT    | Kraken API    |
| AGG        | 2026-11-12 00:00:00 |    95.22      |        -43.0833   | SHORT    | Yahoo Finance |
| ALGO-USD   | 2026-11-13 00:00:00 |     0.08614   |        -34        | SHORT    | Kraken API    |
| AMAT       | 2026-11-12 00:00:00 |   380.95      |        -31.0833   | SHORT    | Yahoo Finance |
| APT-USD    | 2026-11-13 00:00:00 |     0.5371    |        -43.1667   | SHORT    | Kraken API    |
| ARKK       | 2026-11-12 00:00:00 |    76.5       |        -36        | SHORT    | Yahoo Finance |
| BA         | 2026-11-12 00:00:00 |   171.55      |        -43.25     | SHORT    | Yahoo Finance |
| BCH-USD    | 2026-11-13 00:00:00 |   217.35      |        -53.8333   | SHORT    | Kraken API    |
| BITO       | 2026-11-12 00:00:00 |     9.49      |        -44.3333   | SHORT    | Yahoo Finance |
| BND        | 2026-11-12 00:00:00 |    70.65      |        -43.0833   | SHORT    | Yahoo Finance |
| BTC-USD    | 2026-11-13 00:00:00 | 68430.6       |        -48.0833   | SHORT    | Kraken API    |
| CAT        | 2026-11-12 00:00:00 |   605.28      |        -53.0833   | SHORT    | Yahoo Finance |
| CRV-USD    | 2026-11-13 00:00:00 |     0.23201   |        -50.5      | SHORT    | Kraken API    |
| DASH-USD   | 2026-11-13 00:00:00 |    39.7       |        -54.5      | SHORT    | Kraken API    |
| DOGE-USD   | 2026-11-13 00:00:00 |     0.0641695 |        -50.0833   | SHORT    | Kraken API    |
| EEM        | 2026-11-12 00:00:00 |    61.14      |        -30        | SHORT    | Yahoo Finance |
| ETC-USD    | 2026-11-13 00:00:00 |     6.394     |        -41.4167   | SHORT    | Kraken API    |
| ETH-USD    | 2026-11-13 00:00:00 |  1923.72      |        -57.25     | SHORT    | Kraken API    |
| EWJ        | 2026-11-12 00:00:00 |    91.47      |        -45.8333   | SHORT    | Yahoo Finance |
| FCX        | 2026-11-12 00:00:00 |    60.45      |        -51.5833   | SHORT    | Yahoo Finance |
| FIL-USD    | 2026-11-13 00:00:00 |     0.722     |        -50.5      | SHORT    | Kraken API    |
| GOOGL      | 2026-11-12 00:00:00 |   298.7       |        -37.25     | SHORT    | Yahoo Finance |
| GRT-USD    | 2026-11-13 00:00:00 |     0.0172    |        -51.6667   | SHORT    | Kraken API    |
| HBAR-USD   | 2026-11-13 00:00:00 |     0.06153   |        -35.6667   | SHORT    | Kraken API    |
| IBIT       | 2026-11-12 00:00:00 |    40.36      |        -44.3333   | SHORT    | Yahoo Finance |
| IEF        | 2026-11-12 00:00:00 |    90.21      |        -43.0833   | SHORT    | Yahoo Finance |
| IEMG       | 2026-11-12 00:00:00 |    74.45      |        -30        | SHORT    | Yahoo Finance |
| INTC       | 2026-11-12 00:00:00 |    61.2       |        -60.75     | SHORT    | Yahoo Finance |
| LDO-USD    | 2026-11-13 00:00:00 |     0.299     |        -36        | SHORT    | Kraken API    |
| LTC-USD    | 2026-11-13 00:00:00 |    48.52      |        -51.8333   | SHORT    | Kraken API    |
| NFLX       | 2026-11-12 00:00:00 |    62.69      |        -38.75     | SHORT    | Yahoo Finance |
| NOW        | 2026-11-12 00:00:00 |   100.66      |        -52.0833   | SHORT    | Yahoo Finance |
| NVDA       | 2026-11-12 00:00:00 |   166.19      |        -62.3333   | SHORT    | Yahoo Finance |
| OP-USD     | 2026-11-13 00:00:00 |     0.0924    |        -56.0833   | SHORT    | Kraken API    |
| OXY        | 2026-11-12 00:00:00 |    58.4       |        -37.8333   | SHORT    | Yahoo Finance |
| POL-USD    | 2026-11-13 00:00:00 |     0.08651   |        -39        | SHORT    | Kraken API    |
| SHIB-USD   | 2026-11-13 00:00:00 |     4.237e-06 |        -49.8333   | SHORT    | Kraken API    |
| SHY        | 2026-11-12 00:00:00 |    81.14      |        -44.8333   | SHORT    | Yahoo Finance |
| SKY-USD    | 2026-11-13 00:00:00 |     0.05709   |        -47.9167   | SHORT    | Kraken API    |
| SLV        | 2026-11-12 00:00:00 |    45.12      |        -33.75     | SHORT    | Yahoo Finance |
| SMH        | 2026-11-12 00:00:00 |   501.73      |        -51.3333   | SHORT    | Yahoo Finance |
| SOL-USD    | 2026-11-13 00:00:00 |    79.05      |        -52.0833   | SHORT    | Kraken API    |
| SOXX       | 2026-11-12 00:00:00 |   154.99      |        -31.5      | SHORT    | Yahoo Finance |
| SUSHI-USD  | 2026-11-13 00:00:00 |     0.1688    |        -51.5833   | SHORT    | Kraken API    |
| TIA-USD    | 2026-11-13 00:00:00 |     0.4144    |        -47.3333   | SHORT    | Kraken API    |
| TLT        | 2026-11-12 00:00:00 |    79.72      |        -43.0833   | SHORT    | Yahoo Finance |
| TRX-USD    | 2026-11-13 00:00:00 |     0.310983  |        -58.3333   | SHORT    | Kraken API    |
| UNI-USD    | 2026-11-13 00:00:00 |     5.7514    |        -49        | SHORT    | Kraken API    |
| VIXY       | 2026-11-12 00:00:00 |    17.51      |        -37.8333   | SHORT    | Yahoo Finance |
| WIF-USD    | 2026-11-13 00:00:00 |     0.1479    |        -43.0833   | SHORT    | Kraken API    |
| XLE        | 2026-11-12 00:00:00 |    64.33      |        -32.75     | SHORT    | Yahoo Finance |
| XLM-USD    | 2026-11-13 00:00:00 |     0.14335   |        -53.8333   | SHORT    | Kraken API    |
| XRP-USD    | 2026-11-13 00:00:00 |     1.01847   |        -51.5833   | SHORT    | Kraken API    |
| YFI-USD    | 2026-11-13 00:00:00 |  1791.9       |        -32.8333   | SHORT    | Kraken API    |

## Edge Summary

- Symbols with trades: **161** of 161
- Beat buy-and-hold: **36.65%** of traded symbols
- Positive return: **32.30%** of traded symbols
- Median strategy return: **-7.10%** (benchmark **16.88%**)
- Median excess vs benchmark: **-24.83%**
- Median Sharpe: **-0.06**
- Median exposure: **44.43%**

> Edge is real only if both _beat buy-and-hold_ and _median excess_ are convincingly positive across many symbols. Treat a single high-return symbol as noise.

## Portfolio Backtest

Actual capital-allocation books (not per-symbol averages). Benchmarks: `equal_weight_buyhold` (whole tracked universe), `spy_buyhold` (100% SPY), and `sixty_forty` (60% SPY / 40% AGG). `high_conf_voltarget` inverse-vol-weights the HIGH-confidence book; `conviction_long_short` is market-neutral. Judge on **Sharpe** and **max_drawdown** out-of-sample, not raw return: a fully-invested long book wins on return in a bull market but carries all the risk.

| strategy              | scope         | ann_return   | ann_vol   |   sharpe | max_drawdown   | total_return   |   avg_gross_exposure |
|:----------------------|:--------------|:-------------|:----------|---------:|:---------------|:---------------|---------------------:|
| equal_weight_buyhold  | full          | 3.87%        | 28.37%    |     0.14 | -39.53%        | -0.45%         |                 1    |
| equal_weight_buyhold  | out_of_sample | 15.53%       | 26.35%    |     0.59 | -18.44%        | 13.70%         |                 1    |
| all_signals_ew        | full          | -11.04%      | 24.14%    |    -0.46 | -51.97%        | -34.56%        |                 1    |
| all_signals_ew        | out_of_sample | -4.61%       | 21.43%    |    -0.22 | -23.76%        | -7.08%         |                 1    |
| high_conf_ew          | full          | -7.93%       | 29.94%    |    -0.26 | -44.69%        | -31.32%        |                 0.89 |
| high_conf_ew          | out_of_sample | -9.19%       | 27.61%    |    -0.33 | -26.39%        | -12.98%        |                 0.89 |
| high_conf_voltarget   | full          | -9.10%       | 26.68%    |    -0.34 | -39.70%        | -31.82%        |                 0.89 |
| high_conf_voltarget   | out_of_sample | -11.63%      | 23.35%    |    -0.5  | -21.18%        | -14.24%        |                 0.89 |
| conviction_long_short | full          | -14.53%      | 22.01%    |    -0.66 | -49.74%        | -40.26%        |                 0.96 |
| conviction_long_short | out_of_sample | -16.09%      | 17.40%    |    -0.92 | -27.86%        | -17.08%        |                 0.96 |
| spy_buyhold           | full          | 2.87%        | 14.00%    |     0.21 | -19.00%        | 5.92%          |                 0.79 |
| spy_buyhold           | out_of_sample | -2.18%       | 10.92%    |    -0.2  | -11.45%        | -2.91%         |                 0.79 |
| sixty_forty           | full          | 1.10%        | 8.79%     |     0.13 | -11.86%        | 2.19%          |                 0.79 |
| sixty_forty           | out_of_sample | -3.69%       | 7.22%     |    -0.51 | -8.19%         | -4.11%         |                 0.79 |

## Walk-Forward Robustness

Each book measured across contiguous time folds (each a different regime). A book has durable edge only if `mean_sharpe` is positive, `min_sharpe` isn't deeply negative, and `pct_positive_folds` is high — a single great fold doesn't count. `fold_sharpes` lists each fold oldest-to-newest.

| strategy              |   n_folds |   mean_sharpe |   median_sharpe |   min_sharpe | pct_positive_folds   | mean_return   | fold_sharpes                 |
|:----------------------|----------:|--------------:|----------------:|-------------:|:---------------------|:--------------|:-----------------------------|
| equal_weight_buyhold  |         5 |          0.33 |            0.29 |        -0.54 | 60.00%               | 0.75%         | 1.23;1.18;-0.51;-0.54;0.29   |
| all_signals_ew        |         5 |         -0.49 |           -0.18 |        -2.05 | 20.00%               | -6.58%        | -1.24;-0.18;-2.05;1.14;-0.12 |
| high_conf_ew          |         5 |         -0.14 |           -0.58 |        -1.4  | 40.00%               | -5.78%        | 0.77;-1.40;-0.58;1.29;-0.77  |
| high_conf_voltarget   |         5 |         -0.27 |           -0.31 |        -1.79 | 40.00%               | -6.55%        | 0.86;-1.79;-0.31;0.76;-0.89  |
| conviction_long_short |         5 |         -0.63 |           -0.24 |        -1.93 | 40.00%               | -9.17%        | -1.93;0.21;-1.28;0.06;-0.24  |
| spy_buyhold           |         5 |          0.13 |            0.19 |        -0.92 | 60.00%               | 1.30%         | 1.30;0.19;-0.22;0.29;-0.92   |
| sixty_forty           |         5 |          0.04 |            0.06 |        -1.16 | 60.00%               | 0.50%         | 1.19;0.19;-0.10;0.06;-1.16   |

## Strategy Comparison

Each decision rule backtested over the same data. `out_of_sample` is the most recent ~35% of each symbol's history (unseen tail). A rule has real edge only if `median_excess` and `beat_benchmark_pct` stay positive out-of-sample, not just full-sample.

| strategy        | scope         |   symbols | beat_benchmark_pct   | positive_pct   | median_return   | median_benchmark   | median_excess   |   median_sharpe |   total_trades |
|:----------------|:--------------|----------:|:---------------------|:---------------|:----------------|:-------------------|:----------------|----------------:|---------------:|
| trend           | full          |       161 | 36.65%               | 32.30%         | -7.10%          | 16.88%             | -24.83%         |           -0.06 |          11308 |
| trend           | out_of_sample |       161 | 40.99%               | 47.20%         | -0.99%          | 0.17%              | -4.32%          |            0.09 |           3862 |
| mean_reversion  | full          |       159 | 41.51%               | 49.06%         | -0.13%          | 16.88%             | -18.51%         |           -0.02 |           1286 |
| mean_reversion  | out_of_sample |       131 | 50.38%               | 58.02%         | 0.34%           | -1.40%             | 0.50%           |            0.5  |            446 |
| regime_adaptive | full          |       161 | 36.65%               | 32.92%         | -7.50%          | 16.88%             | -24.09%         |           -0.06 |          11570 |
| regime_adaptive | out_of_sample |       161 | 40.99%               | 47.20%         | -1.03%          | 0.17%              | -4.57%          |            0.09 |           3963 |

## Signal Calibration

Realized forward return in the signal's direction, grouped by confidence. HIGH should outrank LOW for the confidence score to be meaningful.

| confidence_level   |   horizon |     n | mean_return   | median_return   | win_rate   |
|:-------------------|----------:|------:|:--------------|:----------------|:-----------|
| HIGH               |         5 |  7821 | 0.21%         | 0.08%           | 51.40%     |
| MEDIUM             |         5 | 29249 | 0.09%         | 0.07%           | 50.74%     |
| LOW                |         5 |  3649 | -0.22%        | -0.26%          | 47.44%     |
| ALL                |         5 | 40719 | 0.08%         | 0.05%           | 50.57%     |
| HIGH               |        10 |  7695 | 0.48%         | 0.09%           | 51.02%     |
| MEDIUM             |        10 | 28924 | 0.19%         | 0.07%           | 50.52%     |
| LOW                |        10 |  3614 | -0.39%        | -0.23%          | 48.26%     |
| ALL                |        10 | 40233 | 0.19%         | 0.05%           | 50.41%     |
| HIGH               |        20 |  7571 | 0.92%         | 0.19%           | 51.49%     |
| MEDIUM             |        20 | 28374 | 0.71%         | 0.45%           | 52.48%     |
| LOW                |        20 |  3518 | -0.31%        | -0.48%          | 47.73%     |
| ALL                |        20 | 39463 | 0.66%         | 0.32%           | 51.87%     |

## Backtest Summary

### Data Quality / Signal Availability

- **ok**: 161 symbols

| symbol     |   trades | return   | benchmark_return   | mdd     |   sharpe | exposure   | skipped_reason   |
|:-----------|---------:|:---------|:-------------------|:--------|---------:|:-----------|:-----------------|
| AAPL       |       67 | -5.25%   | 70.50%             | -20.65% |    -0    | 48.25%     | ok               |
| AAVE-USD   |       67 | -40.29%  | -63.95%            | -64.31% |    -0.29 | 38.89%     | ok               |
| ABBV       |       68 | -17.32%  | 70.46%             | -30.52% |    -0.32 | 50.42%     | ok               |
| ADA-USD    |       74 | -13.97%  | -76.36%            | -52.70% |     0.06 | 49.81%     | ok               |
| ADBE       |       74 | 1.74%    | -54.49%            | -31.20% |     0.16 | 53.41%     | ok               |
| AGG        |       65 | -6.50%   | -2.68%             | -10.74% |    -0.99 | 34.11%     | ok               |
| ALGO-USD   |       80 | -16.21%  | -58.56%            | -42.04% |     0.02 | 41.95%     | ok               |
| AMAT       |       73 | -41.24%  | 65.75%             | -57.56% |    -0.36 | 51.58%     | ok               |
| AMD        |       54 | 29.71%   | 265.24%            | -38.64% |     0.47 | 36.11%     | ok               |
| AMGN       |       63 | -3.42%   | 46.80%             | -34.19% |     0.02 | 53.08%     | ok               |
| AMZN       |       82 | -58.15%  | 44.12%             | -58.58% |    -1.7  | 41.43%     | ok               |
| APT-USD    |       76 | -34.52%  | -89.54%            | -56.73% |    -0.16 | 39.85%     | ok               |
| ARB-USD    |       75 | -2.51%   | -64.90%            | -47.30% |     0.26 | 42.34%     | ok               |
| ARKK       |       85 | -28.48%  | 76.92%             | -35.78% |    -0.41 | 43.93%     | ok               |
| ATOM-USD   |       78 | -52.39%  | -69.77%            | -61.74% |    -0.72 | 46.17%     | ok               |
| AVAX-USD   |       68 | -32.12%  | -63.81%            | -46.76% |    -0.23 | 41.76%     | ok               |
| AVGO       |       66 | -1.94%   | 128.84%            | -42.02% |     0.15 | 40.10%     | ok               |
| BA         |       65 | 14.33%   | -4.22%             | -24.47% |     0.35 | 52.41%     | ok               |
| BAC        |       78 | -5.89%   | 26.21%             | -21.87% |    -0.08 | 48.75%     | ok               |
| BCH-USD    |       84 | -9.12%   | -50.41%            | -54.04% |     0.11 | 48.47%     | ok               |
| BITO       |       85 | -23.70%  | -57.39%            | -43.13% |    -0.16 | 41.60%     | ok               |
| BLK        |       79 | -5.14%   | 52.28%             | -26.90% |    -0.06 | 47.09%     | ok               |
| BND        |       68 | -6.67%   | -2.63%             | -10.80% |    -1.01 | 35.11%     | ok               |
| BONK-USD   |       70 | 64.23%   | -85.27%            | -53.32% |     0.7  | 45.02%     | ok               |
| BTC-USD    |       81 | -7.10%   | -37.94%            | -25.52% |     0.01 | 51.92%     | ok               |
| C          |       81 | -35.20%  | 102.25%            | -39.84% |    -0.76 | 47.42%     | ok               |
| CAT        |       70 | 25.51%   | 83.42%             | -21.87% |     0.48 | 51.25%     | ok               |
| CL         |       60 | 4.41%    | -1.10%             | -14.32% |     0.2  | 40.43%     | ok               |
| CMCSA      |       82 | -35.28%  | -31.23%            | -45.88% |    -0.84 | 43.76%     | ok               |
| COMP-USD   |       95 | -57.22%  | -67.65%            | -57.54% |    -0.62 | 48.47%     | ok               |
| COP        |       64 | -13.14%  | 21.61%             | -37.99% |    -0.14 | 43.76%     | ok               |
| COST       |       60 | 3.94%    | 28.77%             | -31.32% |     0.19 | 40.93%     | ok               |
| CRM        |       67 | -29.12%  | -9.32%             | -39.41% |    -0.39 | 46.26%     | ok               |
| CRV-USD    |       62 | 50.38%   | -68.46%            | -39.89% |     0.64 | 37.16%     | ok               |
| CSCO       |       65 | 1.70%    | 115.76%            | -28.14% |     0.15 | 51.75%     | ok               |
| CVX        |       69 | -13.63%  | 35.80%             | -26.75% |    -0.28 | 43.59%     | ok               |
| DASH-USD   |       59 | -11.08%  | 74.97%             | -64.43% |     0.31 | 30.46%     | ok               |
| DBC        |       68 | -11.81%  | 32.15%             | -24.10% |    -0.34 | 36.11%     | ok               |
| DE         |       72 | -6.01%   | 79.49%             | -22.44% |    -0.03 | 44.43%     | ok               |
| DIA        |       72 | -10.04%  | 32.61%             | -16.20% |    -0.51 | 44.43%     | ok               |
| DIS        |       62 | 2.92%    | 15.93%             | -27.81% |     0.16 | 46.76%     | ok               |
| DOGE-USD   |       68 | -5.38%   | -67.68%            | -61.52% |     0.16 | 47.13%     | ok               |
| DOT-USD    |       74 | -49.61%  | -81.01%            | -67.54% |    -0.44 | 42.15%     | ok               |
| DXY-INDEX  |       42 | -2.18%   | -5.55%             | -5.53%  |    -0.36 | 30.67%     | ok               |
| EEM        |       66 | -8.86%   | 43.29%             | -22.68% |    -0.21 | 41.43%     | ok               |
| EFA        |       64 | -11.02%  | 32.38%             | -13.32% |    -0.45 | 38.77%     | ok               |
| EOG        |       78 | -28.27%  | 24.20%             | -47.50% |    -0.58 | 44.43%     | ok               |
| ETC-USD    |       56 | -3.03%   | -65.41%            | -46.79% |     0.13 | 35.63%     | ok               |
| ETH-USD    |       61 | 130.19%  | -31.69%            | -30.11% |     1.23 | 47.32%     | ok               |
| EWJ        |       66 | -25.60%  | 37.53%             | -29.40% |    -0.88 | 37.94%     | ok               |
| FCX        |       69 | -28.54%  | 19.99%             | -46.84% |    -0.29 | 45.59%     | ok               |
| FET-USD    |       77 | -29.67%  | -82.38%            | -66.52% |    -0.04 | 44.44%     | ok               |
| FIL-USD    |       69 | -23.33%  | -73.51%            | -58.54% |    -0.06 | 38.89%     | ok               |
| FXI        |       46 | -4.25%   | 25.30%             | -23.91% |    -0.02 | 30.45%     | ok               |
| GDX        |       68 | -6.36%   | 138.95%            | -34.29% |     0.04 | 45.09%     | ok               |
| GDXJ       |       70 | -30.10%  | 134.23%            | -36.01% |    -0.32 | 44.43%     | ok               |
| GE         |       78 | -13.14%  | 106.09%            | -27.82% |    -0.14 | 48.42%     | ok               |
| GLD        |       52 | 11.67%   | 64.58%             | -14.15% |     0.35 | 46.09%     | ok               |
| GOOGL      |       57 | 67.76%   | 66.67%             | -16.84% |     1.07 | 48.92%     | ok               |
| GRT-USD    |       73 | 85.77%   | -83.15%            | -43.87% |     0.85 | 47.89%     | ok               |
| GS         |       68 | -2.77%   | 97.71%             | -21.94% |     0.04 | 47.42%     | ok               |
| HBAR-USD   |       40 | -29.16%  | -40.34%            | -56.47% |    -0.42 | 42.66%     | ok               |
| HD         |       71 | 6.07%    | -0.75%             | -17.15% |     0.23 | 44.76%     | ok               |
| HON        |       88 | -29.36%  | 4.71%              | -33.27% |    -0.76 | 53.58%     | ok               |
| HYG        |       89 | -7.38%   | -0.43%             | -10.59% |    -0.83 | 39.10%     | ok               |
| IBIT       |       46 | 36.57%   | 6.18%              | -18.95% |     0.65 | 35.60%     | ok               |
| IBM        |       71 | -21.10%  | 39.80%             | -48.94% |    -0.21 | 50.92%     | ok               |
| ICP-USD    |       71 | 9.52%    | -58.35%            | -40.56% |     0.35 | 40.42%     | ok               |
| IEF        |       78 | -10.13%  | -4.47%             | -12.66% |    -1.34 | 34.61%     | ok               |
| IEMG       |       62 | -7.40%   | 38.93%             | -24.73% |    -0.17 | 41.43%     | ok               |
| INJ-USD    |       55 | -12.40%  | -48.00%            | -61.35% |     0.13 | 38.70%     | ok               |
| INTC       |       72 | 50.17%   | 100.20%            | -60.60% |     0.58 | 49.58%     | ok               |
| INTU       |       71 | 3.97%    | -45.48%            | -36.67% |     0.2  | 47.92%     | ok               |
| ITA        |       72 | -1.32%   | 61.47%             | -23.75% |     0.04 | 47.42%     | ok               |
| IWM        |       56 | 10.39%   | 38.38%             | -8.62%  |     0.42 | 34.44%     | ok               |
| JNJ        |       60 | 14.49%   | 90.13%             | -17.51% |     0.54 | 47.09%     | ok               |
| JPM        |       75 | -25.99%  | 72.38%             | -32.74% |    -0.75 | 44.43%     | ok               |
| KO         |       54 | 27.16%   | 52.32%             | -8.64%  |     0.92 | 39.27%     | ok               |
| LDO-USD    |       68 | 68.59%   | -69.58%            | -50.17% |     0.73 | 48.28%     | ok               |
| LIN        |       70 | -3.70%   | 17.91%             | -20.61% |    -0.06 | 41.76%     | ok               |
| LINK-USD   |       70 | 50.52%   | -36.66%            | -35.01% |     0.66 | 43.10%     | ok               |
| LLY        |       80 | -29.73%  | 60.35%             | -52.47% |    -0.42 | 49.58%     | ok               |
| LRCX       |       82 | -25.33%  | 128.21%            | -60.58% |    -0.1  | 45.26%     | ok               |
| LTC-USD    |       67 | 22.96%   | -47.98%            | -30.78% |     0.45 | 50.77%     | ok               |
| MCD        |       75 | 8.02%    | 5.09%              | -22.20% |     0.33 | 40.77%     | ok               |
| META       |       72 | -31.59%  | 24.99%             | -44.90% |    -0.46 | 50.42%     | ok               |
| MPC        |       70 | 11.57%   | 137.28%            | -33.74% |     0.31 | 53.41%     | ok               |
| MRK        |       67 | -23.47%  | 10.52%             | -35.95% |    -0.45 | 43.26%     | ok               |
| MS         |       75 | -6.28%   | 94.82%             | -27.79% |    -0.06 | 47.92%     | ok               |
| MSFT       |       83 | -28.52%  | 16.83%             | -39.07% |    -0.63 | 50.92%     | ok               |
| MU         |       53 | 74.50%   | 474.38%            | -66.33% |     0.72 | 49.75%     | ok               |
| NEAR-USD   |       65 | 174.64%  | 27.79%             | -46.60% |     1.12 | 43.30%     | ok               |
| NEM        |       72 | -28.27%  | 164.41%            | -41.53% |    -0.29 | 49.58%     | ok               |
| NFLX       |       84 | -5.41%   | -6.30%             | -27.17% |    -0.01 | 50.92%     | ok               |
| NKE        |       89 | -35.53%  | -61.14%            | -55.35% |    -0.45 | 47.75%     | ok               |
| NOW        |       81 | -11.63%  | -31.95%            | -42.66% |     0.08 | 52.08%     | ok               |
| NVDA       |       82 | -39.11%  | 30.60%             | -51.27% |    -0.5  | 55.79%     | ok               |
| OP-USD     |       74 | -28.63%  | -87.26%            | -57.83% |    -0.11 | 35.44%     | ok               |
| ORCL       |       60 | 61.58%   | -9.14%             | -31.06% |     0.67 | 50.58%     | ok               |
| OXY        |       67 | -0.31%   | -7.67%             | -28.48% |     0.12 | 43.43%     | ok               |
| PEP        |       70 | 3.30%    | -15.36%            | -21.35% |     0.17 | 45.42%     | ok               |
| PEPE-USD   |       72 | -38.57%  | -65.43%            | -60.19% |    -0.14 | 46.55%     | ok               |
| PFE        |       79 | -33.58%  | 1.66%              | -42.77% |    -1.02 | 37.60%     | ok               |
| PG         |       62 | -18.21%  | -0.25%             | -24.55% |    -0.63 | 36.77%     | ok               |
| PM         |       79 | -7.00%   | 93.05%             | -38.30% |    -0.07 | 48.09%     | ok               |
| POL-USD    |       83 | 4.48%    | -61.65%            | -46.25% |     0.26 | 49.04%     | ok               |
| QCOM       |       77 | -35.78%  | -11.80%            | -50.90% |    -0.37 | 40.10%     | ok               |
| QQQ        |       70 | -5.29%   | 45.20%             | -15.84% |    -0.06 | 43.43%     | ok               |
| RENDER-USD |       88 | -37.94%  | -64.18%            | -54.16% |    -0.17 | 47.89%     | ok               |
| RTX        |       71 | 19.58%   | 94.55%             | -16.99% |     0.49 | 52.41%     | ok               |
| SBUX       |       66 | -8.54%   | 34.53%             | -29.22% |    -0.08 | 40.60%     | ok               |
| SCHW       |       84 | -20.31%  | 23.06%             | -31.92% |    -0.44 | 48.25%     | ok               |
| SHIB-USD   |       79 | -26.51%  | -68.31%            | -52.76% |    -0.19 | 51.92%     | ok               |
| SHY        |       56 | -2.23%   | -0.62%             | -3.30%  |    -0.72 | 38.77%     | ok               |
| SKY-USD    |       87 | -54.17%  | -38.65%            | -63.60% |    -0.78 | 45.21%     | ok               |
| SLB        |       75 | -43.45%  | 7.22%              | -55.41% |    -0.89 | 47.75%     | ok               |
| SLV        |       66 | 33.80%   | 67.11%             | -37.05% |     0.54 | 41.76%     | ok               |
| SMH        |       50 | 48.21%   | 96.16%             | -34.29% |     0.76 | 42.10%     | ok               |
| SNX-USD    |       60 | 16.58%   | -78.69%            | -50.74% |     0.39 | 37.16%     | ok               |
| SOL-USD    |       71 | 20.12%   | -52.13%            | -41.09% |     0.42 | 58.05%     | ok               |
| SOXX       |       58 | 50.45%   | 91.62%             | -40.14% |     0.74 | 41.10%     | ok               |
| SPY        |       63 | -4.93%   | 39.50%             | -15.53% |    -0.11 | 47.59%     | ok               |
| SUSHI-USD  |       89 | -61.22%  | -78.31%            | -78.31% |    -0.72 | 43.30%     | ok               |
| T          |       68 | 52.21%   | 18.93%             | -17.01% |     0.94 | 57.57%     | ok               |
| TGT        |       58 | -8.89%   | 7.49%              | -32.83% |    -0.11 | 37.27%     | ok               |
| TIA-USD    |       85 | -40.80%  | -81.23%            | -75.44% |    -0.14 | 44.44%     | ok               |
| TLT        |       66 | -20.96%  | -15.50%            | -22.01% |    -1.59 | 34.28%     | ok               |
| TMO        |       67 | 38.81%   | 23.59%             | -18.85% |     0.74 | 56.41%     | ok               |
| TMUS       |       74 | -7.44%   | -3.89%             | -33.05% |    -0.06 | 46.59%     | ok               |
| TRX-USD    |       62 | 2.69%    | 6.30%              | -22.90% |     0.16 | 48.28%     | ok               |
| TSLA       |       76 | -32.71%  | 117.69%            | -59.64% |    -0.19 | 42.26%     | ok               |
| TXN        |       83 | -30.18%  | 61.15%             | -46.56% |    -0.35 | 48.75%     | ok               |
| UNH        |       75 | 39.01%   | -17.32%            | -26.31% |     0.61 | 48.75%     | ok               |
| UNI-USD    |       82 | -24.50%  | -33.65%            | -59.93% |     0.04 | 49.23%     | ok               |
| UPS        |       71 | -34.15%  | -20.36%            | -40.15% |    -0.63 | 43.26%     | ok               |
| USO        |       65 | -13.28%  | 83.27%             | -43.70% |    -0.06 | 34.11%     | ok               |
| VEA        |       64 | -7.02%   | 40.21%             | -18.84% |    -0.25 | 41.26%     | ok               |
| VIXY       |       94 | -83.33%  | -60.67%            | -90.81% |    -1.12 | 31.45%     | ok               |
| VNQ        |       71 | -11.13%  | 13.97%             | -24.92% |    -0.41 | 40.43%     | ok               |
| VTI        |       67 | -11.75%  | 39.11%             | -17.64% |    -0.37 | 47.59%     | ok               |
| VWO        |       78 | -15.96%  | 28.48%             | -25.20% |    -0.55 | 41.60%     | ok               |
| VZ         |       86 | -27.73%  | 13.07%             | -31.67% |    -0.84 | 43.26%     | ok               |
| WFC        |       82 | -21.39%  | 45.33%             | -30.87% |    -0.38 | 46.09%     | ok               |
| WIF-USD    |       64 | 3.01%    | -85.60%            | -48.32% |     0.29 | 42.72%     | ok               |
| WMT        |       71 | 4.89%    | 83.15%             | -25.96% |     0.21 | 48.42%     | ok               |
| XBI        |       60 | 1.08%    | 61.30%             | -17.66% |     0.11 | 37.60%     | ok               |
| XLB        |       64 | -9.79%   | 16.58%             | -24.18% |    -0.3  | 34.44%     | ok               |
| XLC        |       61 | 4.90%    | 26.54%             | -12.33% |     0.22 | 49.25%     | ok               |
| XLE        |       68 | -7.50%   | 40.95%             | -34.77% |    -0.11 | 47.25%     | ok               |
| XLF        |       78 | -2.16%   | 39.96%             | -23.61% |    -0.01 | 49.08%     | ok               |
| XLI        |       82 | -9.35%   | 37.68%             | -18.27% |    -0.32 | 42.76%     | ok               |
| XLK        |       42 | 32.12%   | 56.25%             | -19.09% |     0.71 | 44.09%     | ok               |
| XLM-USD    |       77 | -1.53%   | -48.90%            | -56.32% |     0.2  | 48.85%     | ok               |
| XLP        |       63 | 14.51%   | 16.88%             | -8.96%  |     0.71 | 40.60%     | ok               |
| XLU        |       69 | 0.02%    | 25.64%             | -20.40% |     0.05 | 40.60%     | ok               |
| XLV        |       74 | -18.08%  | 27.70%             | -22.82% |    -0.8  | 37.27%     | ok               |
| XLY        |       77 | -2.45%   | 32.78%             | -18.44% |    -0    | 47.75%     | ok               |
| XOM        |       55 | 2.46%    | 48.86%             | -20.29% |     0.14 | 36.27%     | ok               |
| XRP-USD    |       74 | 3.58%    | -55.84%            | -32.16% |     0.23 | 36.02%     | ok               |
| YFI-USD    |       74 | -49.30%  | -68.18%            | -58.28% |    -0.74 | 39.66%     | ok               |
| ZEC-USD    |       54 | 126.43%  | 1711.51%           | -56.50% |     0.87 | 36.97%     | ok               |

## AAPL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 0.67%    | 70.50%             | -21.71% |     0.12 |       76 | 53.08%     | ok               |
|          15 | -3.78%   | 70.50%             | -23.86% |     0.04 |       85 | 60.57%     | ok               |
|          30 | -5.25%   | 70.50%             | -20.65% |    -0    |       67 | 48.25%     | ok               |
|          35 | -6.61%   | 70.50%             | -22.04% |    -0.04 |       67 | 46.92%     | ok               |
|          25 | -9.09%   | 70.50%             | -22.37% |    -0.08 |       77 | 50.42%     | ok               |

## AAVE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 4.68%    | -63.95%            | -43.61% |     0.27 |       43 | 33.52%     | ok               |
|          35 | -9.10%   | -63.95%            | -48.79% |     0.12 |       53 | 36.78%     | ok               |
|          45 | -10.37%  | -63.95%            | -49.19% |     0.07 |       48 | 28.54%     | ok               |
|          50 | -11.28%  | -63.95%            | -45.07% |     0.04 |       44 | 21.26%     | ok               |
|          15 | -41.67%  | -63.95%            | -61.33% |    -0.2  |       80 | 53.26%     | ok               |

## ABBV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -8.70%   | 70.46%             | -27.91% |    -0.14 |       54 | 38.27%     | ok               |
|          20 | -14.08%  | 70.46%             | -28.73% |    -0.23 |       64 | 53.74%     | ok               |
|          25 | -14.17%  | 70.46%             | -30.04% |    -0.24 |       67 | 52.25%     | ok               |
|          30 | -17.32%  | 70.46%             | -30.52% |    -0.32 |       68 | 50.42%     | ok               |
|          40 | -17.37%  | 70.46%             | -27.36% |    -0.36 |       70 | 43.43%     | ok               |

## ADA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 8.66%    | -76.36%            | -46.50% |     0.35 |       67 | 64.56%     | ok               |
|          40 | -0.08%   | -76.36%            | -41.68% |     0.21 |       56 | 39.08%     | ok               |
|          50 | 2.25%    | -76.36%            | -32.89% |     0.2  |       48 | 24.90%     | ok               |
|          35 | -1.19%   | -76.36%            | -44.07% |     0.2  |       62 | 43.68%     | ok               |
|          45 | -5.29%   | -76.36%            | -38.00% |     0.13 |       56 | 31.80%     | ok               |

## ADBE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 13.92%   | -54.49%            | -29.07% |     0.34 |       61 | 57.74%     | ok               |
|          30 | 1.74%    | -54.49%            | -31.20% |     0.16 |       74 | 53.41%     | ok               |
|          20 | 0.74%    | -54.49%            | -31.52% |     0.16 |       69 | 61.40%     | ok               |
|          35 | -1.61%   | -54.49%            | -32.89% |     0.1  |       75 | 44.93%     | ok               |
|          15 | -6.10%   | -54.49%            | -34.98% |     0.06 |       69 | 64.06%     | ok               |

## AGG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -6.50%   | -2.68%             | -10.74% |    -0.99 |       65 | 34.11%     | ok               |
|          45 | -5.94%   | -2.68%             | -9.39%  |    -1.09 |       58 | 23.79%     | ok               |
|          20 | -8.37%   | -2.68%             | -11.89% |    -1.18 |       70 | 39.77%     | ok               |
|          25 | -8.13%   | -2.68%             | -12.28% |    -1.19 |       71 | 37.60%     | ok               |
|          35 | -7.75%   | -2.68%             | -11.53% |    -1.24 |       64 | 30.78%     | ok               |

## ALGO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -16.21%  | -58.56%            | -42.04% |     0.02 |       80 | 41.95%     | ok               |
|          25 | -18.56%  | -58.56%            | -50.24% |     0.01 |       84 | 46.55%     | ok               |
|          15 | -30.86%  | -58.56%            | -54.18% |    -0.13 |       84 | 53.26%     | ok               |
|          35 | -30.79%  | -58.56%            | -52.80% |    -0.24 |       68 | 36.78%     | ok               |
|          20 | -37.20%  | -58.56%            | -56.25% |    -0.25 |       83 | 49.43%     | ok               |

## AMAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -21.15%  | 65.75%             | -38.30% |    -0.1  |       50 | 35.94%     | ok               |
|          15 | -35.30%  | 65.75%             | -53.90% |    -0.23 |       74 | 60.40%     | ok               |
|          35 | -36.88%  | 65.75%             | -52.00% |    -0.3  |       73 | 48.92%     | ok               |
|          30 | -41.24%  | 65.75%             | -57.56% |    -0.36 |       73 | 51.58%     | ok               |
|          40 | -42.02%  | 65.75%             | -54.64% |    -0.41 |       71 | 44.09%     | ok               |

## AMD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 47.05%   | 265.24%            | -37.12% |     0.61 |       52 | 31.28%     | ok               |
|          40 | 29.71%   | 265.24%            | -38.64% |     0.47 |       54 | 36.11%     | ok               |
|          35 | 24.14%   | 265.24%            | -40.22% |     0.43 |       62 | 37.77%     | ok               |
|          45 | 17.37%   | 265.24%            | -45.23% |     0.37 |       58 | 34.11%     | ok               |
|          30 | 5.47%    | 265.24%            | -47.20% |     0.27 |       65 | 40.43%     | ok               |

## AMGN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 1.68%    | 46.80%             | -26.65% |     0.14 |       62 | 58.40%     | ok               |
|          35 | -0.99%   | 46.80%             | -31.29% |     0.08 |       65 | 49.75%     | ok               |
|          30 | -3.42%   | 46.80%             | -34.19% |     0.02 |       63 | 53.08%     | ok               |
|          15 | -5.85%   | 46.80%             | -27.98% |    -0.01 |       61 | 62.40%     | ok               |
|          25 | -5.40%   | 46.80%             | -33.47% |    -0.01 |       59 | 55.24%     | ok               |

## AMZN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -32.85%  | 44.12%             | -33.72% |    -1.02 |       60 | 30.28%     | ok               |
|          50 | -34.90%  | 44.12%             | -35.58% |    -1.27 |       52 | 22.96%     | ok               |
|          45 | -40.35%  | 44.12%             | -40.97% |    -1.45 |       60 | 26.62%     | ok               |
|          35 | -55.29%  | 44.12%             | -55.76% |    -1.66 |       81 | 35.61%     | ok               |
|          30 | -58.15%  | 44.12%             | -58.58% |    -1.7  |       82 | 41.43%     | ok               |

## APT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 49.09%   | -89.54%            | -25.96% |     0.82 |       42 | 15.90%     | ok               |
|          45 | 11.44%   | -89.54%            | -52.49% |     0.33 |       62 | 23.37%     | ok               |
|          20 | -4.11%   | -89.54%            | -56.22% |     0.24 |       84 | 50.57%     | ok               |
|          15 | -23.80%  | -89.54%            | -58.22% |     0.07 |       79 | 56.90%     | ok               |
|          25 | -28.11%  | -89.54%            | -55.69% |    -0.04 |       76 | 45.02%     | ok               |

## ARB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 83.97%   | -64.90%            | -33.86% |     0.82 |       58 | 26.05%     | ok               |
|          40 | 49.52%   | -64.90%            | -38.69% |     0.62 |       55 | 33.52%     | ok               |
|          35 | 39.78%   | -64.90%            | -41.77% |     0.56 |       69 | 37.36%     | ok               |
|          50 | 38.21%   | -64.90%            | -33.86% |     0.55 |       46 | 18.39%     | ok               |
|          15 | 23.76%   | -64.90%            | -55.99% |     0.47 |       95 | 58.05%     | ok               |

## ARKK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -13.10%  | 76.92%             | -37.76% |    -0.05 |       87 | 54.91%     | ok               |
|          20 | -21.79%  | 76.92%             | -35.06% |    -0.22 |       87 | 50.25%     | ok               |
|          30 | -28.48%  | 76.92%             | -35.78% |    -0.41 |       85 | 43.93%     | ok               |
|          35 | -34.97%  | 76.92%             | -40.36% |    -0.6  |       88 | 40.93%     | ok               |
|          25 | -38.78%  | 76.92%             | -45.03% |    -0.63 |       95 | 46.42%     | ok               |

## ATOM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -38.65%  | -69.77%            | -54.33% |    -0.36 |       80 | 52.49%     | ok               |
|          15 | -43.58%  | -69.77%            | -57.59% |    -0.4  |       82 | 65.52%     | ok               |
|          20 | -47.99%  | -69.77%            | -61.00% |    -0.52 |       88 | 57.47%     | ok               |
|          45 | -45.06%  | -69.77%            | -53.91% |    -0.64 |       68 | 31.80%     | ok               |
|          30 | -52.39%  | -69.77%            | -61.74% |    -0.72 |       78 | 46.17%     | ok               |

## AVAX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 65.25%   | -63.81%            | -22.06% |     0.94 |       34 | 19.73%     | ok               |
|          40 | 41.79%   | -63.81%            | -26.27% |     0.66 |       40 | 30.08%     | ok               |
|          45 | 31.19%   | -63.81%            | -24.48% |     0.57 |       36 | 25.67%     | ok               |
|          35 | 11.79%   | -63.81%            | -33.05% |     0.33 |       52 | 36.21%     | ok               |
|          15 | -6.26%   | -63.81%            | -43.71% |     0.16 |       75 | 53.45%     | ok               |

## AVGO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 0.88%    | 128.84%            | -40.32% |     0.19 |       70 | 42.76%     | ok               |
|          30 | -1.94%   | 128.84%            | -42.02% |     0.15 |       66 | 40.10%     | ok               |
|          20 | -4.56%   | 128.84%            | -42.52% |     0.13 |       80 | 46.42%     | ok               |
|          15 | -12.87%  | 128.84%            | -41.86% |     0.05 |       80 | 51.25%     | ok               |
|          50 | -9.36%   | 128.84%            | -41.40% |     0.03 |       60 | 27.95%     | ok               |

## BA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 29.55%   | -4.22%             | -13.34% |     0.7  |       46 | 35.77%     | ok               |
|          35 | 28.33%   | -4.22%             | -18.09% |     0.56 |       68 | 49.08%     | ok               |
|          40 | 23.63%   | -4.22%             | -23.87% |     0.51 |       48 | 43.76%     | ok               |
|          25 | 23.91%   | -4.22%             | -26.02% |     0.48 |       66 | 55.74%     | ok               |
|          30 | 14.33%   | -4.22%             | -24.47% |     0.35 |       65 | 52.41%     | ok               |

## BAC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 1.17%    | 26.21%             | -13.90% |     0.1  |       54 | 34.11%     | ok               |
|          35 | 0.65%    | 26.21%             | -22.58% |     0.09 |       70 | 44.09%     | ok               |
|          20 | -0.56%   | 26.21%             | -17.27% |     0.07 |       82 | 54.24%     | ok               |
|          50 | -2.10%   | 26.21%             | -12.71% |    -0.01 |       52 | 31.11%     | ok               |
|          40 | -3.01%   | 26.21%             | -17.78% |    -0.03 |       64 | 37.60%     | ok               |

## BCH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 11.68%   | -50.41%            | -45.64% |     0.34 |       81 | 57.28%     | ok               |
|          20 | 8.77%    | -50.41%            | -45.52% |     0.31 |       76 | 54.02%     | ok               |
|          35 | -3.66%   | -50.41%            | -57.75% |     0.17 |       74 | 44.64%     | ok               |
|          25 | -6.61%   | -50.41%            | -48.42% |     0.15 |       80 | 50.38%     | ok               |
|          30 | -9.12%   | -50.41%            | -54.04% |     0.11 |       84 | 48.47%     | ok               |

## BITO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -1.54%   | -57.39%            | -31.98% |     0.11 |       52 | 24.13%     | ok               |
|          45 | -15.11%  | -57.39%            | -32.05% |    -0.09 |       58 | 27.62%     | ok               |
|          30 | -23.70%  | -57.39%            | -43.13% |    -0.16 |       85 | 41.60%     | ok               |
|          35 | -25.08%  | -57.39%            | -42.80% |    -0.21 |       76 | 37.27%     | ok               |
|          15 | -31.23%  | -57.39%            | -53.24% |    -0.22 |       83 | 49.92%     | ok               |

## BLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 4.58%    | 52.28%             | -20.79% |     0.2  |       86 | 43.59%     | ok               |
|          40 | 0.03%    | 52.28%             | -22.83% |     0.07 |       78 | 39.10%     | ok               |
|          20 | -1.20%   | 52.28%             | -21.48% |     0.06 |       82 | 51.91%     | ok               |
|          25 | -2.61%   | 52.28%             | -24.62% |     0.02 |       75 | 49.75%     | ok               |
|          30 | -5.14%   | 52.28%             | -26.90% |    -0.06 |       79 | 47.09%     | ok               |

## BND Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -7.10%   | -2.63%             | -10.72% |    -1    |       65 | 40.93%     | ok               |
|          25 | -6.89%   | -2.63%             | -11.16% |    -1    |       70 | 38.77%     | ok               |
|          30 | -6.67%   | -2.63%             | -10.80% |    -1.01 |       68 | 35.11%     | ok               |
|          40 | -6.73%   | -2.63%             | -11.24% |    -1.13 |       60 | 28.79%     | ok               |
|          15 | -8.47%   | -2.63%             | -12.04% |    -1.18 |       77 | 43.26%     | ok               |

## BONK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 149.39%  | -85.27%            | -23.92% |     1.26 |       36 | 17.24%     | ok               |
|          40 | 159.66%  | -85.27%            | -41.42% |     1.16 |       62 | 34.48%     | ok               |
|          45 | 123.03%  | -85.27%            | -30.84% |     1.07 |       62 | 23.75%     | ok               |
|          35 | 113.01%  | -85.27%            | -47.15% |     0.94 |       60 | 40.42%     | ok               |
|          15 | 88.21%   | -85.27%            | -55.03% |     0.78 |       63 | 61.11%     | ok               |

## BTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 41.67%   | -37.94%            | -21.37% |     0.81 |       62 | 41.38%     | ok               |
|          45 | 34.06%   | -37.94%            | -12.58% |     0.76 |       38 | 29.69%     | ok               |
|          40 | 35.42%   | -37.94%            | -18.10% |     0.75 |       50 | 34.87%     | ok               |
|          50 | 17.82%   | -37.94%            | -20.16% |     0.49 |       34 | 25.10%     | ok               |
|          30 | 9.82%    | -37.94%            | -22.58% |     0.3  |       74 | 47.13%     | ok               |

## C Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -12.29%  | 102.25%            | -22.75% |    -0.29 |       68 | 30.78%     | ok               |
|          45 | -21.49%  | 102.25%            | -29.81% |    -0.54 |       78 | 36.11%     | ok               |
|          40 | -26.43%  | 102.25%            | -34.23% |    -0.64 |       74 | 38.60%     | ok               |
|          25 | -34.24%  | 102.25%            | -37.53% |    -0.72 |       71 | 50.08%     | ok               |
|          20 | -36.29%  | 102.25%            | -39.30% |    -0.76 |       77 | 52.75%     | ok               |

## CAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 40.33%   | 83.42%             | -21.80% |     0.64 |       71 | 61.90%     | ok               |
|          25 | 34.43%   | 83.42%             | -21.79% |     0.59 |       66 | 53.58%     | ok               |
|          45 | 26.27%   | 83.42%             | -23.56% |     0.51 |       54 | 39.77%     | ok               |
|          30 | 25.51%   | 83.42%             | -21.87% |     0.48 |       70 | 51.25%     | ok               |
|          20 | 22.52%   | 83.42%             | -24.56% |     0.44 |       70 | 55.91%     | ok               |

## CL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 10.28%   | -1.10%             | -10.72% |     0.41 |       42 | 24.96%     | ok               |
|          45 | 6.06%    | -1.10%             | -10.96% |     0.26 |       46 | 28.12%     | ok               |
|          30 | 4.41%    | -1.10%             | -14.32% |     0.2  |       60 | 40.43%     | ok               |
|          40 | 0.98%    | -1.10%             | -15.09% |     0.1  |       54 | 31.61%     | ok               |
|          35 | 0.25%    | -1.10%             | -15.39% |     0.07 |       60 | 36.61%     | ok               |

## CMCSA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -17.90%  | -31.23%            | -28.74% |    -0.59 |       48 | 16.47%     | ok               |
|          45 | -23.19%  | -31.23%            | -35.43% |    -0.73 |       62 | 21.13%     | ok               |
|          15 | -35.83%  | -31.23%            | -43.53% |    -0.74 |       90 | 58.40%     | ok               |
|          40 | -31.05%  | -31.23%            | -42.78% |    -0.83 |       89 | 28.62%     | ok               |
|          30 | -35.28%  | -31.23%            | -45.88% |    -0.84 |       82 | 43.76%     | ok               |

## COMP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -40.66%  | -67.65%            | -42.64% |    -0.49 |       48 | 22.99%     | ok               |
|          30 | -57.22%  | -67.65%            | -57.54% |    -0.62 |       95 | 48.47%     | ok               |
|          15 | -68.51%  | -67.65%            | -70.55% |    -0.79 |      104 | 67.82%     | ok               |
|          20 | -66.39%  | -67.65%            | -67.24% |    -0.8  |      106 | 63.03%     | ok               |
|          25 | -66.48%  | -67.65%            | -66.74% |    -0.83 |      102 | 56.51%     | ok               |

## COP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -13.14%  | 21.61%             | -37.99% |    -0.14 |       64 | 43.76%     | ok               |
|          35 | -13.00%  | 21.61%             | -40.42% |    -0.15 |       65 | 40.93%     | ok               |
|          50 | -12.17%  | 21.61%             | -35.99% |    -0.17 |       50 | 31.28%     | ok               |
|          45 | -17.00%  | 21.61%             | -41.02% |    -0.27 |       60 | 34.78%     | ok               |
|          40 | -22.24%  | 21.61%             | -46.75% |    -0.38 |       66 | 37.94%     | ok               |

## COST Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 20.30%   | 28.77%             | -24.32% |     0.61 |       62 | 47.25%     | ok               |
|          25 | 16.36%   | 28.77%             | -24.93% |     0.52 |       59 | 44.26%     | ok               |
|          35 | 8.53%    | 28.77%             | -30.16% |     0.33 |       58 | 38.44%     | ok               |
|          30 | 3.94%    | 28.77%             | -31.32% |     0.19 |       60 | 40.93%     | ok               |
|          15 | 4.00%    | 28.77%             | -27.30% |     0.18 |       67 | 50.92%     | ok               |

## CRM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -17.85%  | -9.32%             | -26.69% |    -0.19 |       64 | 41.43%     | ok               |
|          40 | -20.92%  | -9.32%             | -32.67% |    -0.27 |       70 | 37.27%     | ok               |
|          15 | -27.85%  | -9.32%             | -47.54% |    -0.29 |       92 | 58.57%     | ok               |
|          30 | -29.12%  | -9.32%             | -39.41% |    -0.39 |       67 | 46.26%     | ok               |
|          20 | -32.99%  | -9.32%             | -45.97% |    -0.42 |       74 | 52.08%     | ok               |

## CRV-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 99.81%   | -68.46%            | -37.78% |     0.94 |       60 | 32.95%     | ok               |
|          40 | 79.15%   | -68.46%            | -38.86% |     0.83 |       52 | 29.12%     | ok               |
|          45 | 52.35%   | -68.46%            | -42.29% |     0.68 |       56 | 22.80%     | ok               |
|          30 | 50.38%   | -68.46%            | -39.89% |     0.64 |       62 | 37.16%     | ok               |
|          50 | 39.34%   | -68.46%            | -30.73% |     0.59 |       50 | 18.58%     | ok               |

## CSCO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 27.70%   | 115.76%            | -21.30% |     0.59 |       54 | 41.60%     | ok               |
|          50 | 26.90%   | 115.76%            | -19.34% |     0.59 |       54 | 39.77%     | ok               |
|          40 | 11.78%   | 115.76%            | -27.46% |     0.32 |       58 | 44.76%     | ok               |
|          35 | 8.28%    | 115.76%            | -26.94% |     0.26 |       60 | 48.42%     | ok               |
|          25 | 1.98%    | 115.76%            | -28.73% |     0.15 |       65 | 52.75%     | ok               |

## CVX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -8.74%   | 35.80%             | -27.82% |    -0.17 |       63 | 35.94%     | ok               |
|          40 | -9.92%   | 35.80%             | -25.79% |    -0.19 |       73 | 39.60%     | ok               |
|          25 | -11.05%  | 35.80%             | -23.25% |    -0.2  |       73 | 46.42%     | ok               |
|          50 | -8.62%   | 35.80%             | -29.71% |    -0.2  |       56 | 31.45%     | ok               |
|          30 | -13.63%  | 35.80%             | -26.75% |    -0.28 |       69 | 43.59%     | ok               |

## DASH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 99.47%   | 74.97%             | -43.46% |     0.82 |       42 | 17.24%     | ok               |
|          40 | 81.38%   | 74.97%             | -42.64% |     0.73 |       50 | 23.75%     | ok               |
|          45 | 47.55%   | 74.97%             | -46.93% |     0.58 |       46 | 19.92%     | ok               |
|          25 | -6.69%   | 74.97%             | -64.14% |     0.34 |       69 | 32.76%     | ok               |
|          30 | -11.08%  | 74.97%             | -64.43% |     0.31 |       59 | 30.46%     | ok               |

## DBC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -2.90%   | 32.15%             | -26.01% |    -0.02 |       81 | 43.26%     | ok               |
|          20 | -8.86%   | 32.15%             | -25.69% |    -0.22 |       73 | 40.60%     | ok               |
|          25 | -9.03%   | 32.15%             | -24.84% |    -0.23 |       68 | 38.44%     | ok               |
|          50 | -8.86%   | 32.15%             | -18.84% |    -0.28 |       48 | 25.29%     | ok               |
|          45 | -10.62%  | 32.15%             | -20.02% |    -0.32 |       60 | 28.62%     | ok               |

## DE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 2.45%    | 79.49%             | -17.97% |     0.14 |       58 | 30.62%     | ok               |
|          45 | 0.02%    | 79.49%             | -18.05% |     0.09 |       58 | 34.61%     | ok               |
|          20 | -3.41%   | 79.49%             | -20.02% |     0.03 |       64 | 48.59%     | ok               |
|          25 | -4.81%   | 79.49%             | -20.21% |    -0    |       71 | 46.59%     | ok               |
|          30 | -6.01%   | 79.49%             | -22.44% |    -0.03 |       72 | 44.43%     | ok               |

## DIA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -7.96%   | 32.61%             | -13.58% |    -0.39 |       66 | 45.59%     | ok               |
|          20 | -10.06%  | 32.61%             | -15.48% |    -0.49 |       68 | 47.92%     | ok               |
|          35 | -9.64%   | 32.61%             | -16.94% |    -0.51 |       74 | 41.26%     | ok               |
|          30 | -10.04%  | 32.61%             | -16.20% |    -0.51 |       72 | 44.43%     | ok               |
|          40 | -12.21%  | 32.61%             | -18.41% |    -0.69 |       76 | 37.77%     | ok               |

## DIS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 44.49%   | 15.93%             | -10.17% |     1.23 |       52 | 29.28%     | ok               |
|          40 | 14.53%   | 15.93%             | -18.75% |     0.41 |       67 | 37.44%     | ok               |
|          45 | 11.87%   | 15.93%             | -16.54% |     0.37 |       53 | 32.95%     | ok               |
|          35 | 8.88%    | 15.93%             | -25.30% |     0.28 |       73 | 43.59%     | ok               |
|          15 | 4.86%    | 15.93%             | -32.73% |     0.2  |       79 | 56.07%     | ok               |

## DOGE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -1.42%   | -67.68%            | -60.29% |     0.24 |       81 | 62.45%     | ok               |
|          50 | 1.27%    | -67.68%            | -52.24% |     0.2  |       56 | 20.88%     | ok               |
|          20 | -3.94%   | -67.68%            | -60.01% |     0.2  |       79 | 56.51%     | ok               |
|          30 | -5.38%   | -67.68%            | -61.52% |     0.16 |       68 | 47.13%     | ok               |
|          40 | -4.72%   | -67.68%            | -63.82% |     0.15 |       60 | 34.67%     | ok               |

## DOT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -48.19%  | -81.01%            | -70.04% |    -0.34 |       88 | 53.26%     | ok               |
|          50 | -30.56%  | -81.01%            | -53.14% |    -0.35 |       56 | 21.07%     | ok               |
|          15 | -55.85%  | -81.01%            | -76.85% |    -0.4  |       79 | 57.66%     | ok               |
|          30 | -49.61%  | -81.01%            | -67.54% |    -0.44 |       74 | 42.15%     | ok               |
|          35 | -48.81%  | -81.01%            | -63.75% |    -0.44 |       68 | 38.31%     | ok               |

## DXY-INDEX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -2.18%   | -5.55%             | -5.53%  |    -0.36 |       42 | 30.67%     | ok               |
|          40 | -4.09%   | -5.55%             | -6.38%  |    -0.56 |       68 | 46.22%     | ok               |
|          45 | -4.49%   | -5.55%             | -7.61%  |    -0.66 |       64 | 37.37%     | ok               |
|          30 | -6.38%   | -5.55%             | -9.65%  |    -0.77 |       80 | 56.59%     | ok               |
|          15 | -7.89%   | -5.55%             | -11.87% |    -0.77 |       99 | 72.57%     | ok               |

## EEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.74%   | 43.29%             | -25.47% |    -0.13 |       66 | 44.76%     | ok               |
|          35 | -7.38%   | 43.29%             | -22.40% |    -0.16 |       70 | 39.60%     | ok               |
|          25 | -7.76%   | 43.29%             | -23.98% |    -0.17 |       66 | 43.09%     | ok               |
|          30 | -8.86%   | 43.29%             | -22.68% |    -0.21 |       66 | 41.43%     | ok               |
|          40 | -9.09%   | 43.29%             | -19.08% |    -0.24 |       70 | 37.77%     | ok               |

## EFA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -3.40%   | 32.38%             | -10.29% |    -0.07 |       62 | 49.08%     | ok               |
|          20 | -10.35%  | 32.38%             | -13.88% |    -0.38 |       67 | 46.26%     | ok               |
|          30 | -11.02%  | 32.38%             | -13.32% |    -0.45 |       64 | 38.77%     | ok               |
|          25 | -11.46%  | 32.38%             | -15.57% |    -0.45 |       68 | 42.43%     | ok               |
|          40 | -10.91%  | 32.38%             | -15.01% |    -0.49 |       60 | 34.28%     | ok               |

## EOG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -13.51%  | 24.20%             | -34.41% |    -0.24 |       48 | 32.45%     | ok               |
|          40 | -17.89%  | 24.20%             | -36.53% |    -0.35 |       62 | 35.61%     | ok               |
|          35 | -20.78%  | 24.20%             | -39.26% |    -0.41 |       77 | 39.77%     | ok               |
|          50 | -21.07%  | 24.20%             | -35.63% |    -0.47 |       52 | 29.95%     | ok               |
|          30 | -28.27%  | 24.20%             | -47.50% |    -0.58 |       78 | 44.43%     | ok               |

## ETC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 0.17%    | -65.41%            | -43.95% |     0.17 |       48 | 32.38%     | ok               |
|          30 | -3.03%   | -65.41%            | -46.79% |     0.13 |       56 | 35.63%     | ok               |
|          50 | -2.30%   | -65.41%            | -28.33% |     0.1  |       28 | 18.20%     | ok               |
|          45 | -7.56%   | -65.41%            | -35.44% |     0.02 |       34 | 21.46%     | ok               |
|          40 | -8.96%   | -65.41%            | -41.85% |     0.01 |       50 | 26.44%     | ok               |

## ETH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 130.19%  | -31.69%            | -30.11% |     1.23 |       61 | 47.32%     | ok               |
|          30 | 90.45%   | -31.69%            | -32.89% |     0.96 |       65 | 55.17%     | ok               |
|          40 | 72.11%   | -31.69%            | -33.11% |     0.91 |       62 | 39.46%     | ok               |
|          25 | 67.63%   | -31.69%            | -40.90% |     0.8  |       63 | 59.00%     | ok               |
|          45 | 48.92%   | -31.69%            | -34.50% |     0.73 |       64 | 36.02%     | ok               |

## EWJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -21.53%  | 37.53%             | -30.00% |    -0.65 |       58 | 40.27%     | ok               |
|          15 | -25.30%  | 37.53%             | -31.15% |    -0.75 |       69 | 43.59%     | ok               |
|          25 | -24.02%  | 37.53%             | -29.85% |    -0.76 |       58 | 39.27%     | ok               |
|          30 | -25.60%  | 37.53%             | -29.40% |    -0.88 |       66 | 37.94%     | ok               |
|          45 | -26.32%  | 37.53%             | -28.64% |    -1.06 |       62 | 29.28%     | ok               |

## FCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -1.49%   | 19.99%             | -30.39% |     0.12 |       54 | 33.28%     | ok               |
|          50 | -7.07%   | 19.99%             | -26.57% |     0.02 |       58 | 29.45%     | ok               |
|          40 | -13.73%  | 19.99%             | -42.89% |    -0.07 |       66 | 38.10%     | ok               |
|          30 | -28.54%  | 19.99%             | -46.84% |    -0.29 |       69 | 45.59%     | ok               |
|          35 | -32.14%  | 19.99%             | -50.12% |    -0.38 |       71 | 43.26%     | ok               |

## FET-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 22.74%   | -82.38%            | -59.58% |     0.46 |       71 | 57.66%     | ok               |
|          20 | -11.74%  | -82.38%            | -66.17% |     0.19 |       82 | 54.02%     | ok               |
|          25 | -14.25%  | -82.38%            | -65.31% |     0.16 |       77 | 48.66%     | ok               |
|          30 | -29.67%  | -82.38%            | -66.52% |    -0.04 |       77 | 44.44%     | ok               |
|          45 | -32.05%  | -82.38%            | -51.19% |    -0.29 |       52 | 22.41%     | ok               |

## FIL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -23.33%  | -73.51%            | -58.54% |    -0.06 |       69 | 38.89%     | ok               |
|          40 | -32.95%  | -73.51%            | -57.60% |    -0.27 |       48 | 29.69%     | ok               |
|          15 | -44.90%  | -73.51%            | -72.01% |    -0.28 |       91 | 52.11%     | ok               |
|          35 | -38.86%  | -73.51%            | -65.39% |    -0.34 |       60 | 33.33%     | ok               |
|          20 | -50.76%  | -73.51%            | -74.98% |    -0.42 |       94 | 48.47%     | ok               |

## FXI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -2.11%   | 25.30%             | -22.57% |     0.03 |       48 | 31.78%     | ok               |
|          15 | -4.19%   | 25.30%             | -21.68% |    -0.01 |       51 | 35.27%     | ok               |
|          30 | -4.25%   | 25.30%             | -23.91% |    -0.02 |       46 | 30.45%     | ok               |
|          35 | -6.68%   | 25.30%             | -27.53% |    -0.09 |       48 | 27.79%     | ok               |
|          20 | -7.27%   | 25.30%             | -24.53% |    -0.1  |       48 | 33.11%     | ok               |

## GDX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -2.80%   | 138.95%            | -31.05% |     0.12 |       82 | 51.25%     | ok               |
|          40 | -4.94%   | 138.95%            | -34.42% |     0.05 |       66 | 38.94%     | ok               |
|          30 | -6.36%   | 138.95%            | -34.29% |     0.04 |       68 | 45.09%     | ok               |
|          35 | -10.44%  | 138.95%            | -38.67% |    -0.03 |       74 | 41.60%     | ok               |
|          25 | -15.19%  | 138.95%            | -42.42% |    -0.09 |       72 | 46.92%     | ok               |

## GDXJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -16.79%  | 134.23%            | -34.84% |    -0.05 |       72 | 51.58%     | ok               |
|          35 | -28.11%  | 134.23%            | -38.09% |    -0.29 |       70 | 41.76%     | ok               |
|          30 | -30.10%  | 134.23%            | -36.01% |    -0.32 |       70 | 44.43%     | ok               |
|          25 | -34.34%  | 134.23%            | -39.67% |    -0.37 |       75 | 47.59%     | ok               |
|          40 | -30.85%  | 134.23%            | -46.16% |    -0.38 |       64 | 39.27%     | ok               |

## GE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 4.89%    | 106.09%            | -21.25% |     0.2  |       60 | 33.78%     | ok               |
|          45 | -7.35%   | 106.09%            | -21.88% |    -0.05 |       72 | 36.77%     | ok               |
|          20 | -13.05%  | 106.09%            | -25.05% |    -0.12 |       73 | 52.75%     | ok               |
|          30 | -13.14%  | 106.09%            | -27.82% |    -0.14 |       78 | 48.42%     | ok               |
|          25 | -13.54%  | 106.09%            | -29.91% |    -0.14 |       74 | 50.25%     | ok               |

## GLD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 21.05%   | 64.58%             | -13.87% |     0.54 |       48 | 47.59%     | ok               |
|          20 | 19.41%   | 64.58%             | -13.87% |     0.51 |       49 | 49.25%     | ok               |
|          30 | 11.67%   | 64.58%             | -14.15% |     0.35 |       52 | 46.09%     | ok               |
|          35 | 8.96%    | 64.58%             | -15.57% |     0.3  |       52 | 43.43%     | ok               |
|          15 | 9.15%    | 64.58%             | -18.05% |     0.29 |       55 | 52.75%     | ok               |

## GOOGL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 70.46%   | 66.67%             | -17.38% |     1.12 |       59 | 45.09%     | ok               |
|          30 | 67.76%   | 66.67%             | -16.84% |     1.07 |       57 | 48.92%     | ok               |
|          45 | 58.34%   | 66.67%             | -11.66% |     1.04 |       52 | 38.60%     | ok               |
|          25 | 65.20%   | 66.67%             | -16.16% |     1.03 |       57 | 51.41%     | ok               |
|          50 | 53.67%   | 66.67%             | -11.52% |     1    |       44 | 33.78%     | ok               |

## GRT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 118.76%  | -83.15%            | -36.70% |     0.97 |       68 | 62.26%     | ok               |
|          45 | 86.46%   | -83.15%            | -39.68% |     0.93 |       48 | 29.12%     | ok               |
|          35 | 83.12%   | -83.15%            | -37.94% |     0.85 |       64 | 42.53%     | ok               |
|          30 | 85.77%   | -83.15%            | -43.87% |     0.85 |       73 | 47.89%     | ok               |
|          25 | 85.43%   | -83.15%            | -37.25% |     0.83 |       76 | 52.87%     | ok               |

## GS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 22.58%   | 97.71%             | -20.56% |     0.5  |       66 | 55.24%     | ok               |
|          40 | 7.27%    | 97.71%             | -16.16% |     0.25 |       64 | 40.93%     | ok               |
|          20 | 7.49%    | 97.71%             | -23.19% |     0.25 |       64 | 51.91%     | ok               |
|          25 | -0.60%   | 97.71%             | -23.32% |     0.09 |       66 | 49.92%     | ok               |
|          35 | -1.92%   | 97.71%             | -19.95% |     0.06 |       68 | 44.59%     | ok               |

## HBAR-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -22.53%  | -40.34%            | -49.09% |    -0.3  |       28 | 27.65%     | ok               |
|          40 | -24.21%  | -40.34%            | -51.16% |    -0.32 |       32 | 33.45%     | ok               |
|          15 | -27.07%  | -40.34%            | -58.64% |    -0.33 |       52 | 57.00%     | ok               |
|          50 | -24.56%  | -40.34%            | -39.47% |    -0.41 |       32 | 18.77%     | ok               |
|          35 | -28.42%  | -40.34%            | -56.01% |    -0.41 |       30 | 38.57%     | ok               |

## HD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 6.07%    | -0.75%             | -17.15% |     0.23 |       71 | 44.76%     | ok               |
|          35 | 4.67%    | -0.75%             | -15.36% |     0.2  |       72 | 40.10%     | ok               |
|          25 | 2.45%    | -0.75%             | -16.67% |     0.15 |       72 | 47.25%     | ok               |
|          40 | 1.15%    | -0.75%             | -14.18% |     0.11 |       74 | 34.94%     | ok               |
|          45 | 0.36%    | -0.75%             | -13.70% |     0.08 |       50 | 30.12%     | ok               |

## HON Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -11.78%  | 4.71%              | -20.43% |    -0.31 |       64 | 31.28%     | ok               |
|          45 | -15.68%  | 4.71%              | -22.88% |    -0.41 |       66 | 36.61%     | ok               |
|          35 | -27.78%  | 4.71%              | -31.65% |    -0.75 |       88 | 48.59%     | ok               |
|          30 | -29.36%  | 4.71%              | -33.27% |    -0.76 |       88 | 53.58%     | ok               |
|          40 | -28.78%  | 4.71%              | -32.19% |    -0.81 |       78 | 41.26%     | ok               |

## HYG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -4.90%   | -0.43%             | -8.00%  |    -0.56 |       70 | 33.78%     | ok               |
|          45 | -6.66%   | -0.43%             | -9.14%  |    -0.81 |       70 | 30.12%     | ok               |
|          20 | -7.57%   | -0.43%             | -11.59% |    -0.81 |       94 | 45.09%     | ok               |
|          25 | -7.56%   | -0.43%             | -11.22% |    -0.82 |       89 | 42.43%     | ok               |
|          35 | -7.10%   | -0.43%             | -9.76%  |    -0.82 |       79 | 35.61%     | ok               |

## IBIT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 66.77%   | 6.18%              | -19.20% |     0.93 |       48 | 43.00%     | ok               |
|          50 | 52.34%   | 6.18%              | -17.37% |     0.92 |       26 | 24.51%     | ok               |
|          45 | 42.91%   | 6.18%              | -17.37% |     0.78 |       32 | 25.88%     | ok               |
|          30 | 36.57%   | 6.18%              | -18.95% |     0.65 |       46 | 35.60%     | ok               |
|          40 | 27.20%   | 6.18%              | -22.57% |     0.56 |       40 | 28.79%     | ok               |

## IBM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -15.87%  | 39.80%             | -49.43% |    -0.08 |       87 | 62.73%     | ok               |
|          35 | -19.41%  | 39.80%             | -47.10% |    -0.19 |       65 | 47.75%     | ok               |
|          30 | -21.10%  | 39.80%             | -48.94% |    -0.21 |       71 | 50.92%     | ok               |
|          20 | -27.94%  | 39.80%             | -53.45% |    -0.32 |       73 | 55.74%     | ok               |
|          50 | -27.41%  | 39.80%             | -45.97% |    -0.39 |       46 | 36.61%     | ok               |

## ICP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 9.52%    | -58.35%            | -40.56% |     0.35 |       71 | 40.42%     | ok               |
|          35 | -4.59%   | -58.35%            | -52.30% |     0.18 |       68 | 35.25%     | ok               |
|          40 | -4.71%   | -58.35%            | -46.01% |     0.17 |       62 | 31.03%     | ok               |
|          15 | -30.09%  | -58.35%            | -59.32% |     0.04 |       76 | 52.11%     | ok               |
|          20 | -29.41%  | -58.35%            | -62.99% |     0.04 |       82 | 48.85%     | ok               |

## IEF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -5.35%   | -4.47%             | -10.18% |    -0.61 |       74 | 42.93%     | ok               |
|          15 | -6.59%   | -4.47%             | -10.91% |    -0.74 |       73 | 44.59%     | ok               |
|          40 | -8.15%   | -4.47%             | -10.75% |    -1.18 |       62 | 26.62%     | ok               |
|          25 | -9.59%   | -4.47%             | -11.95% |    -1.2  |       76 | 39.77%     | ok               |
|          45 | -8.34%   | -4.47%             | -10.86% |    -1.24 |       60 | 24.79%     | ok               |

## IEMG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -4.29%   | 38.93%             | -23.73% |    -0.06 |       61 | 43.76%     | ok               |
|          20 | -5.90%   | 38.93%             | -25.26% |    -0.11 |       59 | 45.42%     | ok               |
|          35 | -6.02%   | 38.93%             | -23.28% |    -0.13 |       69 | 40.27%     | ok               |
|          30 | -7.40%   | 38.93%             | -24.73% |    -0.17 |       62 | 41.43%     | ok               |
|          40 | -8.14%   | 38.93%             | -20.42% |    -0.22 |       70 | 37.77%     | ok               |

## INJ-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 33.68%   | -48.00%            | -42.48% |     0.53 |       52 | 35.63%     | ok               |
|          40 | 30.28%   | -48.00%            | -34.03% |     0.5  |       44 | 32.57%     | ok               |
|          45 | 8.30%    | -48.00%            | -42.40% |     0.3  |       50 | 26.44%     | ok               |
|          25 | -9.09%   | -48.00%            | -56.45% |     0.18 |       59 | 41.76%     | ok               |
|          15 | -11.08%  | -48.00%            | -64.35% |     0.18 |       68 | 46.74%     | ok               |

## INTC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 90.86%   | 100.20%            | -49.32% |     0.8  |       60 | 35.11%     | ok               |
|          50 | 84.93%   | 100.20%            | -48.35% |     0.78 |       64 | 31.28%     | ok               |
|          40 | 69.93%   | 100.20%            | -55.86% |     0.69 |       68 | 39.27%     | ok               |
|          15 | 72.70%   | 100.20%            | -53.65% |     0.68 |       78 | 60.07%     | ok               |
|          20 | 63.45%   | 100.20%            | -52.47% |     0.65 |       82 | 56.41%     | ok               |

## INTU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 15.24%   | -45.48%            | -33.65% |     0.37 |       67 | 29.62%     | ok               |
|          35 | 11.35%   | -45.48%            | -40.91% |     0.3  |       69 | 42.10%     | ok               |
|          45 | 9.34%    | -45.48%            | -35.63% |     0.28 |       65 | 33.78%     | ok               |
|          25 | 8.49%    | -45.48%            | -35.24% |     0.26 |       69 | 50.58%     | ok               |
|          40 | 7.59%    | -45.48%            | -37.97% |     0.25 |       69 | 37.27%     | ok               |

## ITA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 0.84%    | 61.47%             | -25.76% |     0.11 |       73 | 59.73%     | ok               |
|          50 | -0.12%   | 61.47%             | -21.48% |     0.06 |       68 | 34.94%     | ok               |
|          30 | -1.32%   | 61.47%             | -23.75% |     0.04 |       72 | 47.42%     | ok               |
|          40 | -4.89%   | 61.47%             | -20.54% |    -0.08 |       70 | 39.93%     | ok               |
|          35 | -5.60%   | 61.47%             | -23.12% |    -0.09 |       72 | 43.59%     | ok               |

## IWM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          25 | 17.32%   | 38.38%             | -8.02% |     0.64 |       52 | 35.77%     | ok               |
|          20 | 12.69%   | 38.38%             | -9.67% |     0.49 |       62 | 36.77%     | ok               |
|          30 | 10.39%   | 38.38%             | -8.62% |     0.42 |       56 | 34.44%     | ok               |
|          40 | 8.67%    | 38.38%             | -9.21% |     0.4  |       44 | 29.28%     | ok               |
|          35 | 8.33%    | 38.38%             | -9.25% |     0.36 |       52 | 31.95%     | ok               |

## JNJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 20.73%   | 90.13%             | -10.97% |     0.8  |       44 | 35.77%     | ok               |
|          15 | 19.65%   | 90.13%             | -18.02% |     0.65 |       58 | 53.58%     | ok               |
|          30 | 14.49%   | 90.13%             | -17.51% |     0.54 |       60 | 47.09%     | ok               |
|          20 | 14.12%   | 90.13%             | -17.61% |     0.51 |       64 | 50.08%     | ok               |
|          45 | 10.40%   | 90.13%             | -13.35% |     0.44 |       50 | 39.43%     | ok               |

## JPM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 1.50%    | 72.38%             | -15.90% |     0.11 |       50 | 31.78%     | ok               |
|          45 | -8.97%   | 72.38%             | -21.91% |    -0.23 |       54 | 34.44%     | ok               |
|          20 | -20.43%  | 72.38%             | -33.59% |    -0.44 |       84 | 48.75%     | ok               |
|          40 | -21.46%  | 72.38%             | -28.47% |    -0.65 |       66 | 37.10%     | ok               |
|          35 | -22.15%  | 72.38%             | -27.43% |    -0.66 |       76 | 40.60%     | ok               |

## KO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 27.16%   | 52.32%             | -8.64%  |     0.92 |       54 | 39.27%     | ok               |
|          40 | 22.33%   | 52.32%             | -9.28%  |     0.82 |       58 | 34.78%     | ok               |
|          35 | 22.84%   | 52.32%             | -8.73%  |     0.8  |       58 | 37.77%     | ok               |
|          25 | 20.97%   | 52.32%             | -10.61% |     0.73 |       60 | 41.93%     | ok               |
|          50 | 9.32%    | 52.32%             | -16.13% |     0.41 |       44 | 28.95%     | ok               |

## LDO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 154.88%  | -69.58%            | -39.01% |     1.04 |       73 | 60.34%     | ok               |
|          20 | 94.21%   | -69.58%            | -41.55% |     0.83 |       78 | 55.56%     | ok               |
|          30 | 68.59%   | -69.58%            | -50.17% |     0.73 |       68 | 48.28%     | ok               |
|          25 | 53.31%   | -69.58%            | -45.81% |     0.64 |       74 | 52.87%     | ok               |
|          35 | 31.75%   | -69.58%            | -58.88% |     0.51 |       76 | 41.00%     | ok               |

## LIN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -0.38%   | 17.91%             | -22.01% |     0.05 |       69 | 44.59%     | ok               |
|          20 | -1.16%   | 17.91%             | -23.00% |     0.03 |       64 | 47.42%     | ok               |
|          15 | -3.06%   | 17.91%             | -23.68% |    -0.03 |       70 | 50.42%     | ok               |
|          30 | -3.70%   | 17.91%             | -20.61% |    -0.06 |       70 | 41.76%     | ok               |
|          45 | -3.98%   | 17.91%             | -17.04% |    -0.11 |       48 | 25.46%     | ok               |

## LINK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 50.52%   | -36.66%            | -35.01% |     0.66 |       70 | 43.10%     | ok               |
|          35 | 47.33%   | -36.66%            | -34.21% |     0.65 |       62 | 38.31%     | ok               |
|          40 | 36.76%   | -36.66%            | -34.00% |     0.58 |       54 | 32.57%     | ok               |
|          50 | 33.28%   | -36.66%            | -27.70% |     0.56 |       42 | 23.95%     | ok               |
|          45 | 33.76%   | -36.66%            | -33.71% |     0.55 |       50 | 29.12%     | ok               |

## LLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 3.89%    | 60.35%             | -38.23% |     0.19 |       50 | 35.44%     | ok               |
|          15 | -10.77%  | 60.35%             | -48.12% |    -0.02 |       70 | 60.23%     | ok               |
|          45 | -10.18%  | 60.35%             | -42.99% |    -0.07 |       60 | 39.27%     | ok               |
|          40 | -19.66%  | 60.35%             | -45.23% |    -0.24 |       70 | 42.43%     | ok               |
|          20 | -23.18%  | 60.35%             | -51.14% |    -0.26 |       77 | 55.41%     | ok               |

## LRCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -7.67%   | 128.21%            | -48.71% |     0.1  |       76 | 36.44%     | ok               |
|          15 | -18.18%  | 128.21%            | -55.17% |     0.04 |       79 | 53.74%     | ok               |
|          40 | -19.56%  | 128.21%            | -55.33% |    -0.03 |       72 | 42.60%     | ok               |
|          35 | -21.10%  | 128.21%            | -58.47% |    -0.05 |       80 | 44.76%     | ok               |
|          20 | -25.26%  | 128.21%            | -61.61% |    -0.07 |       84 | 49.58%     | ok               |

## LTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 29.10%   | -47.98%            | -34.94% |     0.52 |       66 | 44.25%     | ok               |
|          30 | 22.96%   | -47.98%            | -30.78% |     0.45 |       67 | 50.77%     | ok               |
|          25 | 21.53%   | -47.98%            | -34.22% |     0.44 |       67 | 53.45%     | ok               |
|          45 | 19.17%   | -47.98%            | -36.44% |     0.42 |       56 | 33.14%     | ok               |
|          50 | 6.22%    | -47.98%            | -34.89% |     0.25 |       50 | 25.29%     | ok               |

## MCD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 8.21%    | 5.09%              | -9.22%  |     0.39 |       48 | 25.79%     | ok               |
|          30 | 8.02%    | 5.09%              | -22.20% |     0.33 |       75 | 40.77%     | ok               |
|          35 | 5.90%    | 5.09%              | -16.97% |     0.27 |       67 | 38.10%     | ok               |
|          25 | 4.67%    | 5.09%              | -23.93% |     0.22 |       75 | 43.26%     | ok               |
|          20 | 0.40%    | 5.09%              | -24.58% |     0.08 |       77 | 46.42%     | ok               |

## META Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -17.49%  | 24.99%             | -37.54% |    -0.22 |       68 | 39.10%     | ok               |
|          40 | -20.97%  | 24.99%             | -40.90% |    -0.27 |       68 | 42.43%     | ok               |
|          50 | -22.02%  | 24.99%             | -39.33% |    -0.33 |       68 | 34.61%     | ok               |
|          30 | -31.59%  | 24.99%             | -44.90% |    -0.46 |       72 | 50.42%     | ok               |
|          25 | -33.65%  | 24.99%             | -45.70% |    -0.5  |       73 | 53.08%     | ok               |

## MPC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 19.12%   | 137.28%            | -19.02% |     0.43 |       54 | 41.60%     | ok               |
|          40 | 17.16%   | 137.28%            | -20.88% |     0.39 |       64 | 48.25%     | ok               |
|          35 | 16.33%   | 137.28%            | -31.08% |     0.38 |       70 | 50.92%     | ok               |
|          45 | 15.10%   | 137.28%            | -20.23% |     0.37 |       60 | 45.59%     | ok               |
|          30 | 11.57%   | 137.28%            | -33.74% |     0.31 |       70 | 53.41%     | ok               |

## MRK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -13.11%  | 10.52%             | -28.39% |    -0.16 |       85 | 52.75%     | ok               |
|          25 | -13.87%  | 10.52%             | -31.07% |    -0.2  |       72 | 44.93%     | ok               |
|          20 | -18.09%  | 10.52%             | -29.34% |    -0.29 |       77 | 48.25%     | ok               |
|          50 | -14.56%  | 10.52%             | -23.01% |    -0.3  |       58 | 29.28%     | ok               |
|          45 | -16.68%  | 10.52%             | -25.38% |    -0.33 |       59 | 32.61%     | ok               |

## MS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 1.94%    | 94.82%             | -19.99% |     0.13 |       68 | 38.77%     | ok               |
|          15 | -0.04%   | 94.82%             | -22.02% |     0.1  |       74 | 57.07%     | ok               |
|          20 | -2.26%   | 94.82%             | -25.68% |     0.04 |       73 | 52.91%     | ok               |
|          30 | -6.28%   | 94.82%             | -27.79% |    -0.06 |       75 | 47.92%     | ok               |
|          25 | -7.75%   | 94.82%             | -28.36% |    -0.1  |       73 | 50.08%     | ok               |

## MSFT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -15.96%  | 16.83%             | -24.64% |    -0.37 |       70 | 36.94%     | ok               |
|          50 | -19.36%  | 16.83%             | -25.48% |    -0.5  |       60 | 31.78%     | ok               |
|          35 | -25.42%  | 16.83%             | -35.38% |    -0.57 |       73 | 46.26%     | ok               |
|          40 | -25.20%  | 16.83%             | -34.92% |    -0.59 |       69 | 40.60%     | ok               |
|          30 | -28.52%  | 16.83%             | -39.07% |    -0.63 |       83 | 50.92%     | ok               |

## MU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 93.97%   | 474.38%            | -61.15% |     0.82 |       60 | 45.09%     | ok               |
|          45 | 84.23%   | 474.38%            | -62.31% |     0.79 |       62 | 42.43%     | ok               |
|          30 | 74.50%   | 474.38%            | -66.33% |     0.72 |       53 | 49.75%     | ok               |
|          15 | 76.89%   | 474.38%            | -61.96% |     0.71 |       56 | 58.24%     | ok               |
|          35 | 69.68%   | 474.38%            | -66.69% |     0.7  |       65 | 47.42%     | ok               |

## NEAR-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 223.63%  | 27.79%             | -40.07% |     1.41 |       30 | 22.41%     | ok               |
|          40 | 257.67%  | 27.79%             | -41.76% |     1.41 |       40 | 32.38%     | ok               |
|          45 | 200.17%  | 27.79%             | -38.08% |     1.26 |       42 | 28.35%     | ok               |
|          30 | 174.64%  | 27.79%             | -46.60% |     1.12 |       65 | 43.30%     | ok               |
|          35 | 161.03%  | 27.79%             | -52.15% |     1.11 |       60 | 36.21%     | ok               |

## NEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -7.46%   | 164.41%            | -35.45% |     0.08 |       66 | 58.90%     | ok               |
|          20 | -7.68%   | 164.41%            | -32.74% |     0.06 |       73 | 53.91%     | ok               |
|          50 | -12.51%  | 164.41%            | -33.03% |    -0.06 |       48 | 37.77%     | ok               |
|          25 | -21.78%  | 164.41%            | -39.51% |    -0.17 |       70 | 51.58%     | ok               |
|          30 | -28.27%  | 164.41%            | -41.53% |    -0.29 |       72 | 49.58%     | ok               |

## NFLX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 19.92%   | -6.30%             | -20.78% |     0.52 |       54 | 38.77%     | ok               |
|          50 | 17.25%   | -6.30%             | -16.28% |     0.5  |       44 | 30.45%     | ok               |
|          35 | 13.49%   | -6.30%             | -18.30% |     0.38 |       78 | 43.59%     | ok               |
|          45 | 5.54%    | -6.30%             | -18.06% |     0.22 |       58 | 34.78%     | ok               |
|          15 | 3.02%    | -6.30%             | -26.59% |     0.17 |       76 | 63.89%     | ok               |

## NKE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -21.40%  | -61.14%            | -42.13% |    -0.25 |       75 | 39.93%     | ok               |
|          20 | -28.23%  | -61.14%            | -49.34% |    -0.29 |       87 | 55.24%     | ok               |
|          25 | -31.21%  | -61.14%            | -51.20% |    -0.35 |       87 | 52.58%     | ok               |
|          15 | -34.48%  | -61.14%            | -55.79% |    -0.41 |       90 | 59.07%     | ok               |
|          40 | -24.27%  | -61.14%            | -33.81% |    -0.44 |       69 | 32.61%     | ok               |

## NOW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -10.52%  | -31.95%            | -49.77% |     0.1  |       73 | 57.57%     | ok               |
|          30 | -11.63%  | -31.95%            | -42.66% |     0.08 |       81 | 52.08%     | ok               |
|          15 | -17.15%  | -31.95%            | -52.56% |     0.02 |       81 | 60.23%     | ok               |
|          25 | -17.96%  | -31.95%            | -47.93% |     0.01 |       73 | 55.41%     | ok               |
|          35 | -23.63%  | -31.95%            | -48.24% |    -0.11 |       84 | 47.25%     | ok               |

## NVDA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -26.86%  | 30.60%             | -39.21% |    -0.27 |       76 | 51.52%     | ok               |
|          25 | -32.03%  | 30.60%             | -44.52% |    -0.4  |       81 | 47.59%     | ok               |
|          30 | -31.81%  | 30.60%             | -43.72% |    -0.42 |       82 | 44.74%     | ok               |
|          15 | -39.11%  | 30.60%             | -51.27% |    -0.5  |       82 | 55.79%     | ok               |
|          35 | -42.07%  | 30.60%             | -51.85% |    -0.69 |       92 | 41.89%     | ok               |

## OP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 36.28%   | -87.26%            | -30.63% |     0.66 |       38 | 10.34%     | ok               |
|          45 | 26.69%   | -87.26%            | -28.24% |     0.49 |       40 | 16.48%     | ok               |
|          40 | 0.95%    | -87.26%            | -43.68% |     0.21 |       48 | 24.71%     | ok               |
|          15 | -24.82%  | -87.26%            | -55.83% |     0    |       75 | 46.93%     | ok               |
|          30 | -28.63%  | -87.26%            | -57.83% |    -0.11 |       74 | 35.44%     | ok               |

## ORCL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 130.35%  | -9.14%             | -37.59% |     0.99 |       67 | 60.23%     | ok               |
|          45 | 95.21%   | -9.14%             | -32.35% |     0.91 |       54 | 37.77%     | ok               |
|          25 | 85.20%   | -9.14%             | -31.06% |     0.8  |       59 | 52.75%     | ok               |
|          35 | 76.44%   | -9.14%             | -31.95% |     0.77 |       60 | 46.92%     | ok               |
|          20 | 80.04%   | -9.14%             | -32.60% |     0.77 |       68 | 55.91%     | ok               |

## OXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 1.89%    | -7.67%             | -26.37% |     0.15 |       68 | 38.94%     | ok               |
|          30 | -0.31%   | -7.67%             | -28.48% |     0.12 |       67 | 43.43%     | ok               |
|          40 | -2.37%   | -7.67%             | -28.30% |     0.07 |       58 | 35.77%     | ok               |
|          50 | -2.93%   | -7.67%             | -26.34% |     0.05 |       48 | 29.12%     | ok               |
|          25 | -14.21%  | -7.67%             | -38.51% |    -0.12 |       75 | 47.09%     | ok               |

## PEP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 17.47%   | -15.36%            | -11.62% |     0.73 |       40 | 26.29%     | ok               |
|          45 | 5.62%    | -15.36%            | -14.22% |     0.27 |       52 | 29.95%     | ok               |
|          30 | 3.30%    | -15.36%            | -21.35% |     0.17 |       70 | 45.42%     | ok               |
|          35 | 1.69%    | -15.36%            | -21.42% |     0.12 |       73 | 39.77%     | ok               |
|          40 | -1.19%   | -15.36%            | -18.04% |     0.01 |       68 | 35.11%     | ok               |

## PEPE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -40.40%  | -65.43%            | -64.58% |    -0.05 |       79 | 61.11%     | ok               |
|          30 | -38.57%  | -65.43%            | -60.19% |    -0.14 |       72 | 46.55%     | ok               |
|          20 | -43.42%  | -65.43%            | -63.48% |    -0.16 |       85 | 56.70%     | ok               |
|          35 | -44.12%  | -65.43%            | -60.83% |    -0.3  |       64 | 42.72%     | ok               |
|          25 | -54.17%  | -65.43%            | -64.37% |    -0.37 |       86 | 51.53%     | ok               |

## PFE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -15.07%  | 1.66%              | -25.81% |    -0.45 |       52 | 22.96%     | ok               |
|          50 | -14.14%  | 1.66%              | -27.79% |    -0.46 |       40 | 19.63%     | ok               |
|          40 | -18.08%  | 1.66%              | -30.60% |    -0.53 |       74 | 28.12%     | ok               |
|          35 | -25.97%  | 1.66%              | -36.12% |    -0.78 |       84 | 34.61%     | ok               |
|          30 | -33.58%  | 1.66%              | -42.77% |    -1.02 |       79 | 37.60%     | ok               |

## PG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -6.86%   | -0.25%             | -20.08% |    -0.21 |       52 | 30.12%     | ok               |
|          35 | -10.04%  | -0.25%             | -18.99% |    -0.32 |       60 | 33.61%     | ok               |
|          45 | -14.75%  | -0.25%             | -22.00% |    -0.56 |       52 | 27.79%     | ok               |
|          30 | -18.21%  | -0.25%             | -24.55% |    -0.63 |       62 | 36.77%     | ok               |
|          25 | -20.08%  | -0.25%             | -25.84% |    -0.7  |       74 | 38.27%     | ok               |

## PM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -3.98%   | 93.05%             | -35.28% |    -0    |       84 | 44.59%     | ok               |
|          20 | -6.49%   | 93.05%             | -36.74% |    -0.05 |       83 | 53.24%     | ok               |
|          30 | -7.00%   | 93.05%             | -38.30% |    -0.07 |       79 | 48.09%     | ok               |
|          50 | -9.22%   | 93.05%             | -36.94% |    -0.16 |       66 | 35.44%     | ok               |
|          40 | -11.50%  | 93.05%             | -39.92% |    -0.21 |       78 | 41.10%     | ok               |

## POL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 9.99%    | -61.65%            | -46.25% |     0.33 |       75 | 54.02%     | ok               |
|          20 | 9.52%    | -61.65%            | -48.58% |     0.33 |       85 | 57.85%     | ok               |
|          50 | 10.04%   | -61.65%            | -30.34% |     0.3  |       52 | 20.88%     | ok               |
|          30 | 4.48%    | -61.65%            | -46.25% |     0.26 |       83 | 49.04%     | ok               |
|          40 | 2.01%    | -61.65%            | -32.62% |     0.21 |       58 | 32.18%     | ok               |

## QCOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -21.87%  | -11.80%            | -39.94% |    -0.14 |       77 | 37.44%     | ok               |
|          25 | -23.83%  | -11.80%            | -50.64% |    -0.14 |       75 | 41.60%     | ok               |
|          20 | -29.43%  | -11.80%            | -50.50% |    -0.22 |       71 | 44.93%     | ok               |
|          15 | -37.95%  | -11.80%            | -54.37% |    -0.36 |       73 | 47.59%     | ok               |
|          30 | -35.78%  | -11.80%            | -50.90% |    -0.37 |       77 | 40.10%     | ok               |

## QQQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 5.02%    | 45.20%             | -17.16% |     0.21 |       71 | 52.58%     | ok               |
|          25 | 1.57%    | 45.20%             | -14.05% |     0.12 |       65 | 45.42%     | ok               |
|          20 | 0.35%    | 45.20%             | -14.88% |     0.1  |       77 | 48.59%     | ok               |
|          30 | -5.29%   | 45.20%             | -15.84% |    -0.06 |       70 | 43.43%     | ok               |
|          50 | -13.19%  | 45.20%             | -22.73% |    -0.38 |       62 | 27.95%     | ok               |

## RENDER-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 36.24%   | -64.18%            | -44.75% |     0.55 |       86 | 63.22%     | ok               |
|          20 | 21.49%   | -64.18%            | -43.37% |     0.45 |       89 | 58.43%     | ok               |
|          25 | 8.09%    | -64.18%            | -43.13% |     0.35 |       85 | 53.64%     | ok               |
|          30 | -37.94%  | -64.18%            | -54.16% |    -0.17 |       88 | 47.89%     | ok               |
|          35 | -39.98%  | -64.18%            | -55.67% |    -0.24 |       80 | 42.53%     | ok               |

## RTX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 32.83%   | 94.55%             | -18.66% |     0.7  |       74 | 57.90%     | ok               |
|          25 | 28.29%   | 94.55%             | -18.59% |     0.63 |       62 | 55.24%     | ok               |
|          15 | 24.80%   | 94.55%             | -19.55% |     0.56 |       67 | 62.40%     | ok               |
|          30 | 19.58%   | 94.55%             | -16.99% |     0.49 |       71 | 52.41%     | ok               |
|          50 | 13.21%   | 94.55%             | -18.42% |     0.43 |       62 | 39.60%     | ok               |

## SBUX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 2.96%    | 34.53%             | -23.55% |     0.16 |       61 | 42.43%     | ok               |
|          40 | 1.03%    | 34.53%             | -25.43% |     0.12 |       60 | 34.11%     | ok               |
|          45 | -0.89%   | 34.53%             | -27.26% |     0.07 |       66 | 29.28%     | ok               |
|          35 | -2.45%   | 34.53%             | -26.54% |     0.05 |       64 | 37.44%     | ok               |
|          20 | -9.32%   | 34.53%             | -30.94% |    -0.07 |       64 | 44.43%     | ok               |

## SCHW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -3.45%   | 23.06%             | -16.53% |    -0.04 |       62 | 31.28%     | ok               |
|          20 | -5.99%   | 23.06%             | -29.24% |    -0.04 |       71 | 52.75%     | ok               |
|          50 | -3.90%   | 23.06%             | -13.28% |    -0.08 |       54 | 28.12%     | ok               |
|          25 | -7.72%   | 23.06%             | -28.76% |    -0.09 |       67 | 51.08%     | ok               |
|          15 | -11.16%  | 23.06%             | -31.37% |    -0.16 |       78 | 56.74%     | ok               |

## SHIB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -7.88%   | -68.31%            | -32.18% |     0.02 |       48 | 21.65%     | ok               |
|          15 | -16.09%  | -68.31%            | -47.25% |     0.01 |       85 | 65.71%     | ok               |
|          35 | -12.81%  | -68.31%            | -43.57% |     0.01 |       75 | 45.98%     | ok               |
|          20 | -19.62%  | -68.31%            | -49.90% |    -0.05 |       78 | 61.11%     | ok               |
|          25 | -26.10%  | -68.31%            | -50.56% |    -0.16 |       78 | 57.66%     | ok               |

## SHY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          30 | -2.23%   | -0.62%             | -3.30% |    -0.72 |       56 | 38.77%     | ok               |
|          40 | -2.46%   | -0.62%             | -3.58% |    -0.83 |       60 | 35.11%     | ok               |
|          35 | -2.76%   | -0.62%             | -3.61% |    -0.91 |       58 | 36.61%     | ok               |
|          45 | -2.54%   | -0.62%             | -3.43% |    -0.93 |       56 | 28.62%     | ok               |
|          50 | -2.67%   | -0.62%             | -3.40% |    -1.03 |       48 | 24.79%     | ok               |

## SKY-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -54.26%  | -38.65%            | -65.72% |    -0.67 |       79 | 55.75%     | ok               |
|          35 | -50.82%  | -38.65%            | -60.94% |    -0.75 |       78 | 37.16%     | ok               |
|          30 | -54.17%  | -38.65%            | -63.60% |    -0.78 |       87 | 45.21%     | ok               |
|          25 | -59.36%  | -38.65%            | -66.89% |    -0.89 |       80 | 48.47%     | ok               |
|          40 | -55.25%  | -38.65%            | -63.28% |    -0.93 |       66 | 33.72%     | ok               |

## SLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -11.47%  | 7.22%              | -27.99% |    -0.14 |       50 | 33.78%     | ok               |
|          45 | -11.64%  | 7.22%              | -26.23% |    -0.15 |       56 | 31.11%     | ok               |
|          50 | -10.06%  | 7.22%              | -27.89% |    -0.16 |       44 | 24.46%     | ok               |
|          35 | -34.42%  | 7.22%              | -46.57% |    -0.68 |       74 | 41.76%     | ok               |
|          25 | -40.10%  | 7.22%              | -52.31% |    -0.76 |       86 | 51.75%     | ok               |

## SLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 66.55%   | 67.11%             | -28.72% |     0.86 |       50 | 31.45%     | ok               |
|          45 | 52.41%   | 67.11%             | -31.33% |     0.73 |       61 | 32.95%     | ok               |
|          40 | 51.20%   | 67.11%             | -34.28% |     0.72 |       65 | 34.94%     | ok               |
|          20 | 45.68%   | 67.11%             | -37.05% |     0.64 |       70 | 45.59%     | ok               |
|          15 | 43.24%   | 67.11%             | -47.98% |     0.6  |       71 | 50.25%     | ok               |

## SMH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 67.51%   | 96.16%             | -31.66% |     0.92 |       49 | 44.93%     | ok               |
|          25 | 52.36%   | 96.16%             | -33.57% |     0.8  |       46 | 43.43%     | ok               |
|          30 | 48.21%   | 96.16%             | -34.29% |     0.76 |       50 | 42.10%     | ok               |
|          35 | 37.18%   | 96.16%             | -34.65% |     0.64 |       56 | 40.10%     | ok               |
|          45 | 25.13%   | 96.16%             | -32.84% |     0.52 |       54 | 34.28%     | ok               |

## SNX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 43.12%   | -78.69%            | -29.01% |     0.67 |       44 | 26.63%     | ok               |
|          35 | 43.05%   | -78.69%            | -42.92% |     0.63 |       50 | 30.84%     | ok               |
|          20 | 31.30%   | -78.69%            | -53.03% |     0.52 |       71 | 46.36%     | ok               |
|          15 | 16.79%   | -78.69%            | -54.74% |     0.4  |       72 | 50.38%     | ok               |
|          30 | 16.58%   | -78.69%            | -50.74% |     0.39 |       60 | 37.16%     | ok               |

## SOL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 73.36%   | -52.13%            | -39.12% |     0.87 |       54 | 38.70%     | ok               |
|          35 | 44.68%   | -52.13%            | -43.12% |     0.63 |       66 | 44.83%     | ok               |
|          45 | 24.76%   | -52.13%            | -46.28% |     0.48 |       48 | 32.57%     | ok               |
|          25 | 24.88%   | -52.13%            | -37.29% |     0.46 |       67 | 55.56%     | ok               |
|          15 | 21.08%   | -52.13%            | -46.18% |     0.43 |       73 | 63.22%     | ok               |

## SOXX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 54.74%   | 91.62%             | -39.65% |     0.78 |       56 | 43.26%     | ok               |
|          35 | 52.08%   | 91.62%             | -38.76% |     0.76 |       58 | 38.60%     | ok               |
|          30 | 50.45%   | 91.62%             | -40.14% |     0.74 |       58 | 41.10%     | ok               |
|          20 | 43.06%   | 91.62%             | -38.67% |     0.66 |       61 | 44.09%     | ok               |
|          40 | 33.56%   | 91.62%             | -41.03% |     0.58 |       58 | 36.44%     | ok               |

## SPY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 4.26%    | 39.50%             | -14.25% |     0.2  |       62 | 51.25%     | ok               |
|          15 | 1.73%    | 39.50%             | -16.80% |     0.12 |       68 | 54.24%     | ok               |
|          25 | -0.05%   | 39.50%             | -14.25% |     0.06 |       60 | 50.08%     | ok               |
|          30 | -4.93%   | 39.50%             | -15.53% |    -0.11 |       63 | 47.59%     | ok               |
|          35 | -5.85%   | 39.50%             | -15.58% |    -0.15 |       61 | 44.43%     | ok               |

## SUSHI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -30.90%  | -78.31%            | -41.02% |    -0.39 |       60 | 17.05%     | ok               |
|          15 | -58.95%  | -78.31%            | -77.32% |    -0.52 |       83 | 53.64%     | ok               |
|          20 | -58.27%  | -78.31%            | -76.66% |    -0.56 |       84 | 49.81%     | ok               |
|          35 | -54.17%  | -78.31%            | -70.88% |    -0.65 |       75 | 36.78%     | ok               |
|          45 | -46.99%  | -78.31%            | -58.64% |    -0.66 |       62 | 23.18%     | ok               |

## T Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 66.55%   | 18.93%             | -15.08% |     1.06 |       71 | 66.39%     | ok               |
|          25 | 62.97%   | 18.93%             | -17.66% |     1.06 |       66 | 59.57%     | ok               |
|          20 | 62.44%   | 18.93%             | -18.13% |     1.04 |       66 | 61.90%     | ok               |
|          30 | 52.21%   | 18.93%             | -17.01% |     0.94 |       68 | 57.57%     | ok               |
|          35 | 34.31%   | 18.93%             | -14.49% |     0.71 |       76 | 52.91%     | ok               |

## TGT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -8.89%   | 7.49%              | -32.83% |    -0.11 |       58 | 37.27%     | ok               |
|          25 | -10.70%  | 7.49%              | -34.49% |    -0.14 |       66 | 40.27%     | ok               |
|          20 | -13.69%  | 7.49%              | -36.76% |    -0.18 |       84 | 44.76%     | ok               |
|          45 | -12.30%  | 7.49%              | -26.12% |    -0.24 |       48 | 28.79%     | ok               |
|          15 | -19.64%  | 7.49%              | -36.20% |    -0.3  |       70 | 49.58%     | ok               |

## TIA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -26.20%  | -81.23%            | -66.94% |     0.12 |       93 | 60.54%     | ok               |
|          25 | -30.19%  | -81.23%            | -69.36% |     0.02 |       90 | 49.43%     | ok               |
|          20 | -32.26%  | -81.23%            | -68.67% |     0.02 |       87 | 54.60%     | ok               |
|          35 | -23.92%  | -81.23%            | -66.58% |    -0    |       76 | 38.12%     | ok               |
|          30 | -40.80%  | -81.23%            | -75.44% |    -0.14 |       85 | 44.44%     | ok               |

## TLT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -7.83%   | -15.50%            | -12.51% |    -0.87 |       32 | 16.81%     | ok               |
|          40 | -13.43%  | -15.50%            | -17.65% |    -1.19 |       48 | 24.79%     | ok               |
|          45 | -11.96%  | -15.50%            | -15.17% |    -1.25 |       42 | 20.13%     | ok               |
|          30 | -20.96%  | -15.50%            | -22.01% |    -1.59 |       66 | 34.28%     | ok               |
|          35 | -19.97%  | -15.50%            | -21.03% |    -1.67 |       66 | 29.28%     | ok               |

## TMO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 50.73%   | 23.59%             | -8.17%  |     1.07 |       50 | 35.27%     | ok               |
|          45 | 49.68%   | 23.59%             | -9.69%  |     1    |       54 | 40.27%     | ok               |
|          40 | 42.51%   | 23.59%             | -11.54% |     0.87 |       59 | 45.42%     | ok               |
|          35 | 45.43%   | 23.59%             | -13.84% |     0.86 |       67 | 50.75%     | ok               |
|          20 | 42.89%   | 23.59%             | -22.89% |     0.77 |       74 | 62.56%     | ok               |

## TMUS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -6.17%   | -3.89%             | -41.04% |    -0.01 |       68 | 59.40%     | ok               |
|          30 | -7.44%   | -3.89%             | -33.05% |    -0.06 |       74 | 46.59%     | ok               |
|          25 | -10.06%  | -3.89%             | -39.29% |    -0.11 |       75 | 49.58%     | ok               |
|          20 | -11.59%  | -3.89%             | -39.79% |    -0.14 |       74 | 53.74%     | ok               |
|          50 | -10.37%  | -3.89%             | -32.38% |    -0.22 |       60 | 32.11%     | ok               |

## TRX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 11.03%   | 6.30%              | -18.79% |     0.41 |       54 | 38.89%     | ok               |
|          50 | 6.26%    | 6.30%              | -19.79% |     0.28 |       44 | 32.95%     | ok               |
|          35 | 3.58%    | 6.30%              | -21.77% |     0.19 |       60 | 45.98%     | ok               |
|          45 | 2.67%    | 6.30%              | -24.19% |     0.16 |       48 | 35.25%     | ok               |
|          30 | 2.69%    | 6.30%              | -22.90% |     0.16 |       62 | 48.28%     | ok               |

## TSLA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 47.27%   | 117.69%            | -30.57% |     0.66 |       62 | 29.95%     | ok               |
|          40 | 18.38%   | 117.69%            | -50.11% |     0.38 |       61 | 35.44%     | ok               |
|          45 | -6.85%   | 117.69%            | -52.01% |     0.11 |       67 | 32.45%     | ok               |
|          35 | -17.25%  | 117.69%            | -60.12% |     0.01 |       74 | 37.94%     | ok               |
|          25 | -32.27%  | 117.69%            | -56.97% |    -0.17 |       72 | 45.09%     | ok               |

## TXN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -2.53%   | 61.15%             | -43.95% |     0.09 |       70 | 31.61%     | ok               |
|          35 | -17.67%  | 61.15%             | -42.08% |    -0.15 |       84 | 45.42%     | ok               |
|          20 | -23.53%  | 61.15%             | -37.19% |    -0.19 |       74 | 55.24%     | ok               |
|          15 | -25.27%  | 61.15%             | -38.02% |    -0.21 |       79 | 59.57%     | ok               |
|          40 | -22.70%  | 61.15%             | -44.52% |    -0.25 |       78 | 42.93%     | ok               |

## UNH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 39.01%   | -17.32%            | -26.31% |     0.61 |       75 | 48.75%     | ok               |
|          35 | 34.62%   | -17.32%            | -27.21% |     0.57 |       68 | 43.76%     | ok               |
|          50 | 32.27%   | -17.32%            | -37.02% |     0.57 |       54 | 29.95%     | ok               |
|          15 | 33.88%   | -17.32%            | -26.07% |     0.54 |       82 | 63.89%     | ok               |
|          20 | 31.44%   | -17.32%            | -26.96% |     0.52 |       77 | 57.57%     | ok               |

## UNI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 74.50%   | -33.65%            | -22.21% |     0.84 |       48 | 25.67%     | ok               |
|          45 | 58.67%   | -33.65%            | -30.17% |     0.71 |       54 | 32.76%     | ok               |
|          40 | 43.22%   | -33.65%            | -43.84% |     0.6  |       60 | 38.89%     | ok               |
|          35 | 31.49%   | -33.65%            | -48.64% |     0.51 |       64 | 44.06%     | ok               |
|          30 | -24.50%  | -33.65%            | -59.93% |     0.04 |       82 | 49.23%     | ok               |

## UPS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -18.14%  | -20.36%            | -25.52% |    -0.3  |       60 | 34.11%     | ok               |
|          50 | -16.70%  | -20.36%            | -24.11% |    -0.31 |       44 | 24.79%     | ok               |
|          20 | -27.36%  | -20.36%            | -34.46% |    -0.44 |       80 | 50.42%     | ok               |
|          15 | -29.75%  | -20.36%            | -36.61% |    -0.48 |       82 | 53.91%     | ok               |
|          35 | -28.96%  | -20.36%            | -32.02% |    -0.53 |       65 | 38.10%     | ok               |

## USO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 4.56%    | 83.27%             | -37.82% |     0.22 |       64 | 41.76%     | ok               |
|          20 | 3.09%    | 83.27%             | -41.14% |     0.19 |       68 | 38.10%     | ok               |
|          45 | 2.33%    | 83.27%             | -35.01% |     0.17 |       50 | 26.62%     | ok               |
|          25 | -5.62%   | 83.27%             | -42.94% |     0.07 |       66 | 36.27%     | ok               |
|          50 | -4.73%   | 83.27%             | -29.83% |     0.05 |       52 | 24.79%     | ok               |

## VEA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 2.64%    | 40.21%             | -16.89% |     0.15 |       56 | 49.75%     | ok               |
|          20 | -1.00%   | 40.21%             | -17.40% |     0.01 |       57 | 47.25%     | ok               |
|          25 | -5.88%   | 40.21%             | -18.46% |    -0.19 |       59 | 45.26%     | ok               |
|          30 | -7.02%   | 40.21%             | -18.84% |    -0.25 |       64 | 41.26%     | ok               |
|          35 | -7.67%   | 40.21%             | -17.88% |    -0.29 |       50 | 38.77%     | ok               |

## VIXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -54.55%  | -60.67%            | -69.78% |    -0.63 |       34 | 8.65%      | ok               |
|          45 | -64.29%  | -60.67%            | -75.03% |    -0.84 |       54 | 13.64%     | ok               |
|          40 | -71.97%  | -60.67%            | -80.72% |    -0.97 |       68 | 17.64%     | ok               |
|          35 | -78.91%  | -60.67%            | -84.48% |    -1.11 |       92 | 24.29%     | ok               |
|          30 | -83.33%  | -60.67%            | -90.81% |    -1.12 |       94 | 31.45%     | ok               |

## VNQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -7.39%   | 13.97%             | -22.34% |    -0.24 |       70 | 43.26%     | ok               |
|          45 | -7.50%   | 13.97%             | -19.07% |    -0.31 |       60 | 28.62%     | ok               |
|          50 | -8.42%   | 13.97%             | -17.13% |    -0.37 |       52 | 25.29%     | ok               |
|          30 | -11.13%  | 13.97%             | -24.92% |    -0.41 |       71 | 40.43%     | ok               |
|          20 | -12.12%  | 13.97%             | -24.00% |    -0.43 |       75 | 45.92%     | ok               |

## VTI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 5.92%    | 39.11%             | -13.96% |     0.25 |       63 | 51.58%     | ok               |
|          15 | -1.79%   | 39.11%             | -15.70% |     0.01 |       64 | 54.41%     | ok               |
|          25 | -4.60%   | 39.11%             | -15.00% |    -0.09 |       57 | 49.58%     | ok               |
|          40 | -8.79%   | 39.11%             | -19.77% |    -0.3  |       70 | 39.93%     | ok               |
|          35 | -10.79%  | 39.11%             | -20.22% |    -0.36 |       64 | 44.26%     | ok               |

## VWO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -7.41%   | 28.48%             | -21.18% |    -0.24 |       56 | 29.95%     | ok               |
|          45 | -9.22%   | 28.48%             | -23.26% |    -0.32 |       58 | 32.45%     | ok               |
|          15 | -11.37%  | 28.48%             | -24.01% |    -0.34 |       72 | 47.09%     | ok               |
|          40 | -10.07%  | 28.48%             | -23.57% |    -0.34 |       68 | 35.27%     | ok               |
|          20 | -11.39%  | 28.48%             | -26.14% |    -0.34 |       67 | 45.09%     | ok               |

## VZ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -3.10%   | 13.07%             | -12.96% |    -0.04 |       56 | 28.62%     | ok               |
|          20 | -22.26%  | 13.07%             | -35.02% |    -0.43 |       80 | 52.75%     | ok               |
|          25 | -19.09%  | 13.07%             | -26.32% |    -0.47 |       83 | 47.75%     | ok               |
|          35 | -18.88%  | 13.07%             | -26.97% |    -0.55 |       64 | 39.10%     | ok               |
|          45 | -18.61%  | 13.07%             | -26.23% |    -0.57 |       72 | 32.95%     | ok               |

## WFC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -9.85%   | 45.33%             | -23.64% |    -0.15 |       77 | 42.60%     | ok               |
|          50 | -8.46%   | 45.33%             | -18.29% |    -0.21 |       58 | 32.28%     | ok               |
|          45 | -12.64%  | 45.33%             | -23.40% |    -0.31 |       62 | 35.94%     | ok               |
|          40 | -13.50%  | 45.33%             | -24.26% |    -0.32 |       70 | 39.10%     | ok               |
|          20 | -21.51%  | 45.33%             | -29.43% |    -0.34 |       80 | 52.58%     | ok               |

## WIF-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 53.48%   | -85.60%            | -40.67% |     0.64 |       67 | 49.43%     | ok               |
|          25 | 30.90%   | -85.60%            | -44.74% |     0.5  |       63 | 45.40%     | ok               |
|          15 | 19.94%   | -85.60%            | -46.21% |     0.44 |       77 | 52.68%     | ok               |
|          30 | 3.01%    | -85.60%            | -48.32% |     0.29 |       64 | 42.72%     | ok               |
|          35 | -4.42%   | -85.60%            | -52.54% |     0.18 |       60 | 36.59%     | ok               |

## WMT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 35.85%   | 83.15%             | -12.87% |     1.05 |       38 | 36.27%     | ok               |
|          45 | 34.84%   | 83.15%             | -14.82% |     0.98 |       44 | 38.77%     | ok               |
|          35 | 25.55%   | 83.15%             | -18.90% |     0.73 |       60 | 45.26%     | ok               |
|          40 | 23.39%   | 83.15%             | -19.17% |     0.69 |       52 | 40.43%     | ok               |
|          15 | 7.12%    | 83.15%             | -26.82% |     0.25 |       84 | 59.23%     | ok               |

## XBI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 13.75%   | 61.30%             | -16.08% |     0.41 |       50 | 33.44%     | ok               |
|          45 | 9.43%    | 61.30%             | -15.46% |     0.32 |       48 | 30.95%     | ok               |
|          35 | 3.24%    | 61.30%             | -17.66% |     0.16 |       58 | 36.11%     | ok               |
|          30 | 1.08%    | 61.30%             | -17.66% |     0.11 |       60 | 37.60%     | ok               |
|          50 | 0.20%    | 61.30%             | -15.41% |     0.08 |       48 | 27.95%     | ok               |

## XLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 0.82%    | 16.58%             | -17.29% |     0.09 |       54 | 29.12%     | ok               |
|          50 | -0.07%   | 16.58%             | -16.22% |     0.05 |       38 | 24.29%     | ok               |
|          35 | -2.87%   | 16.58%             | -20.65% |    -0.05 |       54 | 32.28%     | ok               |
|          45 | -3.06%   | 16.58%             | -17.93% |    -0.07 |       40 | 26.12%     | ok               |
|          25 | -6.36%   | 16.58%             | -21.62% |    -0.17 |       62 | 38.27%     | ok               |

## XLC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 4.90%    | 26.54%             | -12.33% |     0.22 |       61 | 49.25%     | ok               |
|          25 | 3.35%    | 26.54%             | -12.31% |     0.17 |       62 | 51.58%     | ok               |
|          50 | 2.39%    | 26.54%             | -12.48% |     0.15 |       64 | 37.27%     | ok               |
|          20 | 2.78%    | 26.54%             | -11.04% |     0.15 |       65 | 54.08%     | ok               |
|          40 | 0.41%    | 26.54%             | -13.38% |     0.07 |       62 | 42.93%     | ok               |

## XLE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.76%   | 40.95%             | -25.98% |     0.06 |       58 | 38.60%     | ok               |
|          45 | -2.44%   | 40.95%             | -28.46% |     0.01 |       60 | 41.10%     | ok               |
|          30 | -7.50%   | 40.95%             | -34.77% |    -0.11 |       68 | 47.25%     | ok               |
|          20 | -11.17%  | 40.95%             | -34.45% |    -0.18 |       79 | 52.58%     | ok               |
|          40 | -9.79%   | 40.95%             | -31.71% |    -0.18 |       62 | 43.43%     | ok               |

## XLF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 6.53%    | 39.96%             | -20.19% |     0.27 |       70 | 56.91%     | ok               |
|          20 | 5.87%    | 39.96%             | -18.63% |     0.25 |       70 | 54.24%     | ok               |
|          25 | -1.51%   | 39.96%             | -23.22% |     0.01 |       77 | 51.08%     | ok               |
|          30 | -2.16%   | 39.96%             | -23.61% |    -0.01 |       78 | 49.08%     | ok               |
|          35 | -10.17%  | 39.96%             | -24.48% |    -0.33 |       70 | 45.59%     | ok               |

## XLI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 5.38%    | 37.68%             | -11.06% |     0.24 |       85 | 51.58%     | ok               |
|          20 | 0.03%    | 37.68%             | -12.74% |     0.06 |       77 | 46.59%     | ok               |
|          45 | -5.55%   | 37.68%             | -16.29% |    -0.2  |       70 | 33.78%     | ok               |
|          50 | -6.76%   | 37.68%             | -14.94% |    -0.28 |       62 | 31.28%     | ok               |
|          25 | -8.77%   | 37.68%             | -17.60% |    -0.29 |       78 | 44.43%     | ok               |

## XLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 47.97%   | 56.25%             | -18.51% |     0.87 |       53 | 50.75%     | ok               |
|          25 | 40.53%   | 56.25%             | -15.06% |     0.83 |       42 | 45.42%     | ok               |
|          20 | 41.07%   | 56.25%             | -19.61% |     0.81 |       52 | 47.92%     | ok               |
|          30 | 32.12%   | 56.25%             | -19.09% |     0.71 |       42 | 44.09%     | ok               |
|          35 | 14.38%   | 56.25%             | -21.79% |     0.4  |       58 | 41.10%     | ok               |

## XLM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 19.06%   | -48.90%            | -61.51% |     0.41 |       74 | 60.73%     | ok               |
|          25 | 17.71%   | -48.90%            | -53.31% |     0.4  |       77 | 51.72%     | ok               |
|          40 | 4.53%    | -48.90%            | -53.91% |     0.25 |       70 | 35.63%     | ok               |
|          45 | 4.83%    | -48.90%            | -49.94% |     0.25 |       60 | 27.59%     | ok               |
|          20 | -2.09%   | -48.90%            | -63.17% |     0.21 |       78 | 54.79%     | ok               |

## XLP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          45 | 21.66%   | 16.88%             | -5.66% |     1.07 |       48 | 32.61%     | ok               |
|          50 | 18.79%   | 16.88%             | -6.08% |     0.96 |       54 | 30.78%     | ok               |
|          40 | 19.40%   | 16.88%             | -7.32% |     0.95 |       64 | 35.94%     | ok               |
|          35 | 17.93%   | 16.88%             | -8.39% |     0.88 |       62 | 38.77%     | ok               |
|          30 | 14.51%   | 16.88%             | -8.96% |     0.71 |       63 | 40.60%     | ok               |

## XLU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 5.78%    | 25.64%             | -14.03% |     0.33 |       56 | 29.95%     | ok               |
|          45 | 4.62%    | 25.64%             | -14.97% |     0.27 |       60 | 31.11%     | ok               |
|          35 | 4.54%    | 25.64%             | -19.71% |     0.25 |       64 | 37.10%     | ok               |
|          40 | 2.08%    | 25.64%             | -16.41% |     0.14 |       70 | 33.78%     | ok               |
|          30 | 0.02%    | 25.64%             | -20.40% |     0.05 |       69 | 40.60%     | ok               |

## XLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -17.70%  | 27.70%             | -22.46% |    -0.77 |       74 | 38.94%     | ok               |
|          30 | -18.08%  | 27.70%             | -22.82% |    -0.8  |       74 | 37.27%     | ok               |
|          15 | -20.48%  | 27.70%             | -24.77% |    -0.87 |       81 | 42.93%     | ok               |
|          20 | -20.31%  | 27.70%             | -24.61% |    -0.89 |       77 | 40.43%     | ok               |
|          35 | -22.16%  | 27.70%             | -26.64% |    -1.05 |       68 | 34.28%     | ok               |

## XLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 1.06%    | 32.78%             | -16.52% |     0.11 |       78 | 54.41%     | ok               |
|          30 | -2.45%   | 32.78%             | -18.44% |    -0    |       77 | 47.75%     | ok               |
|          20 | -4.29%   | 32.78%             | -20.14% |    -0.04 |       74 | 51.08%     | ok               |
|          25 | -6.42%   | 32.78%             | -21.01% |    -0.11 |       71 | 49.58%     | ok               |
|          50 | -5.60%   | 32.78%             | -17.00% |    -0.16 |       66 | 32.45%     | ok               |

## XOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 3.48%    | 48.86%             | -21.35% |     0.17 |       40 | 29.28%     | ok               |
|          25 | 3.49%    | 48.86%             | -19.90% |     0.17 |       55 | 36.94%     | ok               |
|          30 | 2.46%    | 48.86%             | -20.29% |     0.14 |       55 | 36.27%     | ok               |
|          45 | -1.68%   | 48.86%             | -23.33% |     0.03 |       44 | 30.45%     | ok               |
|          40 | -3.14%   | 48.86%             | -21.45% |    -0.01 |       54 | 33.78%     | ok               |

## XRP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 11.75%   | -55.84%            | -33.31% |     0.33 |       82 | 43.87%     | ok               |
|          40 | 3.58%    | -55.84%            | -32.16% |     0.23 |       74 | 36.02%     | ok               |
|          30 | -7.04%   | -55.84%            | -34.07% |     0.12 |       72 | 49.23%     | ok               |
|          45 | -6.31%   | -55.84%            | -33.74% |     0.1  |       66 | 29.89%     | ok               |
|          20 | -13.08%  | -55.84%            | -37.79% |     0.05 |       75 | 55.94%     | ok               |

## YFI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -41.47%  | -68.18%            | -44.76% |    -0.64 |       58 | 27.59%     | ok               |
|          35 | -45.79%  | -68.18%            | -52.87% |    -0.68 |       60 | 35.63%     | ok               |
|          30 | -49.30%  | -68.18%            | -58.28% |    -0.74 |       74 | 39.66%     | ok               |
|          25 | -52.24%  | -68.18%            | -60.71% |    -0.78 |       73 | 44.06%     | ok               |
|          15 | -59.64%  | -68.18%            | -67.95% |    -0.9  |       81 | 52.49%     | ok               |

## ZEC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 211.96%  | 1711.51%           | -30.64% |     1.11 |       46 | 28.74%     | ok               |
|          35 | 162.09%  | 1711.51%           | -50.84% |     0.97 |       52 | 34.10%     | ok               |
|          40 | 138.59%  | 1711.51%           | -54.22% |     0.91 |       52 | 32.38%     | ok               |
|          50 | 127.49%  | 1711.51%           | -41.34% |     0.89 |       42 | 25.29%     | ok               |
|          30 | 126.43%  | 1711.51%           | -56.50% |     0.87 |       54 | 36.97%     | ok               |
