# Market Tracker Backtest Report

_Generated: 2026-06-22T01:41:18+00:00_

## Data Sources

- Crypto: Kraken -> Coinbase -> CoinGecko OHLC -> CoinPaprika fallback chain.
- Stocks / ETFs / indices: Stooq -> Yahoo Finance fallback chain.
- Data rows are generated from real market APIs. Mock OHLCV rows are not generated.

## Data Freshness

- Rows: **92,416**
- Symbols: **161**
- Date range: **2024-01-26** to **2026-06-22**

## Latest Signals

| symbol     | date                |         close |   composite_score | signal   | data_source   |
|:-----------|:--------------------|--------------:|------------------:|:---------|:--------------|
| AMAT       | 2026-06-18 00:00:00 |   617.11      |         75.25     | LONG     | Yahoo Finance |
| BAC        | 2026-06-18 00:00:00 |    56.2       |         63.25     | LONG     | Yahoo Finance |
| BLK        | 2026-06-18 00:00:00 |  1050.09      |         51.1667   | LONG     | Yahoo Finance |
| C          | 2026-06-18 00:00:00 |   143.06      |         72.25     | LONG     | Yahoo Finance |
| CSCO       | 2026-06-18 00:00:00 |   119.54      |         35.1667   | LONG     | Yahoo Finance |
| DIS        | 2026-06-18 00:00:00 |   103.89      |         30.1667   | LONG     | Yahoo Finance |
| DXY-INDEX  | 2026-06-21 00:00:00 |   100.808     |         82.2581   | LONG     | Yahoo Finance |
| GE         | 2026-06-18 00:00:00 |   357.64      |         63.5833   | LONG     | Yahoo Finance |
| GS         | 2026-06-18 00:00:00 |  1096.56      |         52.5833   | LONG     | Yahoo Finance |
| HD         | 2026-06-18 00:00:00 |   334.28      |         43.6667   | LONG     | Yahoo Finance |
| ITA        | 2026-06-18 00:00:00 |   238.99      |         57.5833   | LONG     | Yahoo Finance |
| JPM        | 2026-06-18 00:00:00 |   325.22      |         52.0833   | LONG     | Yahoo Finance |
| LLY        | 2026-06-18 00:00:00 |  1098.57      |         41.4167   | LONG     | Yahoo Finance |
| LRCX       | 2026-06-18 00:00:00 |   389.04      |         76.4167   | LONG     | Yahoo Finance |
| MS         | 2026-06-18 00:00:00 |   223.17      |         73.4167   | LONG     | Yahoo Finance |
| PG         | 2026-06-18 00:00:00 |   150.38      |         83.8333   | LONG     | Yahoo Finance |
| PM         | 2026-06-18 00:00:00 |   178.4       |         37.4167   | LONG     | Yahoo Finance |
| RTX        | 2026-06-18 00:00:00 |   185.6       |         64.8333   | LONG     | Yahoo Finance |
| SBUX       | 2026-06-18 00:00:00 |   100.65      |         67.4167   | LONG     | Yahoo Finance |
| TIA-USD    | 2026-06-22 00:00:00 |     0.3753    |         38.4167   | LONG     | Kraken API    |
| TRX-USD    | 2026-06-22 00:00:00 |     0.328026  |         45.9167   | LONG     | Kraken API    |
| UNH        | 2026-06-18 00:00:00 |   400.96      |         65.0833   | LONG     | Yahoo Finance |
| UNI-USD    | 2026-06-22 00:00:00 |     3.066     |         41.3333   | LONG     | Kraken API    |
| WFC        | 2026-06-18 00:00:00 |    82.2       |         62.75     | LONG     | Yahoo Finance |
| XLM-USD    | 2026-06-22 00:00:00 |     0.214691  |         58.25     | LONG     | Kraken API    |
| AAPL       | 2026-06-18 00:00:00 |   298.01      |         -1.33333  | NEUTRAL  | Yahoo Finance |
| AAVE-USD   | 2026-06-22 00:00:00 |    75.88      |         13.3333   | NEUTRAL  | Kraken API    |
| ABBV       | 2026-06-18 00:00:00 |   216.49      |        -11.3333   | NEUTRAL  | Yahoo Finance |
| ADA-USD    | 2026-06-22 00:00:00 |     0.160835  |        -20.6667   | NEUTRAL  | Kraken API    |
| AGG        | 2026-06-18 00:00:00 |    98.9       |         -1.75     | NEUTRAL  | Yahoo Finance |
| ALGO-USD   | 2026-06-22 00:00:00 |     0.09086   |        -11.5      | NEUTRAL  | Kraken API    |
| AMD        | 2026-06-18 00:00:00 |   537.37      |         33.8333   | NEUTRAL  | Yahoo Finance |
| AMGN       | 2026-06-18 00:00:00 |   337.6       |         19.8333   | NEUTRAL  | Yahoo Finance |
| AMZN       | 2026-06-18 00:00:00 |   244.39      |        -11.0833   | NEUTRAL  | Yahoo Finance |
| APT-USD    | 2026-06-22 00:00:00 |     0.6773    |        -11.8333   | NEUTRAL  | Kraken API    |
| ARB-USD    | 2026-06-22 00:00:00 |     0.085     |         -6.33333  | NEUTRAL  | Kraken API    |
| ARKK       | 2026-06-18 00:00:00 |    80.19      |         20.4167   | NEUTRAL  | Yahoo Finance |
| ATOM-USD   | 2026-06-22 00:00:00 |     1.782     |        -31.0833   | NEUTRAL  | Kraken API    |
| AVAX-USD   | 2026-06-22 00:00:00 |     6.279     |        -21        | NEUTRAL  | Kraken API    |
| AVGO       | 2026-06-18 00:00:00 |   411.35      |         -8.25     | NEUTRAL  | Yahoo Finance |
| BA         | 2026-06-18 00:00:00 |   222.72      |         20.25     | NEUTRAL  | Yahoo Finance |
| BND        | 2026-06-18 00:00:00 |    73.34      |         -1.75     | NEUTRAL  | Yahoo Finance |
| BONK-USD   | 2026-06-22 00:00:00 |     4.628e-06 |          1.16667  | NEUTRAL  | Kraken API    |
| BTC-USD    | 2026-06-22 00:00:00 | 64327         |          3.16667  | NEUTRAL  | Kraken API    |
| CAT        | 2026-06-18 00:00:00 |   985.82      |         66.8333   | NEUTRAL  | Yahoo Finance |
| CL         | 2026-06-18 00:00:00 |    89.48      |         55.9167   | NEUTRAL  | Yahoo Finance |
| COMP-USD   | 2026-06-22 00:00:00 |    17.79      |         -9.33333  | NEUTRAL  | Kraken API    |
| COP        | 2026-06-18 00:00:00 |   107.74      |        -52.3333   | NEUTRAL  | Yahoo Finance |
| COST       | 2026-06-18 00:00:00 |   951.45      |        -17.8333   | NEUTRAL  | Yahoo Finance |
| CRM        | 2026-06-18 00:00:00 |   151.78      |        -74.0833   | NEUTRAL  | Yahoo Finance |
| CRV-USD    | 2026-06-22 00:00:00 |     0.21103   |        -23.8333   | NEUTRAL  | Kraken API    |
| CVX        | 2026-06-18 00:00:00 |   173.63      |        -52.3333   | NEUTRAL  | Yahoo Finance |
| DASH-USD   | 2026-06-22 00:00:00 |    35.627     |        -44.4167   | NEUTRAL  | Kraken API    |
| DBC        | 2026-06-18 00:00:00 |    27.63      |        -14.8333   | NEUTRAL  | Yahoo Finance |
| DE         | 2026-06-18 00:00:00 |   589.24      |         60.8333   | NEUTRAL  | Yahoo Finance |
| DIA        | 2026-06-18 00:00:00 |   515.52      |         40.1667   | NEUTRAL  | Yahoo Finance |
| DOGE-USD   | 2026-06-22 00:00:00 |     0.0839511 |         -8.66667  | NEUTRAL  | Kraken API    |
| DOT-USD    | 2026-06-22 00:00:00 |     0.9638    |        -14.5      | NEUTRAL  | Kraken API    |
| EEM        | 2026-06-18 00:00:00 |    70.79      |         45.1667   | NEUTRAL  | Yahoo Finance |
| EFA        | 2026-06-18 00:00:00 |   104.41      |          7.33333  | NEUTRAL  | Yahoo Finance |
| EOG        | 2026-06-18 00:00:00 |   129.98      |        -25.3333   | NEUTRAL  | Yahoo Finance |
| ETC-USD    | 2026-06-22 00:00:00 |     7.419     |          1.5      | NEUTRAL  | Kraken API    |
| ETH-USD    | 2026-06-22 00:00:00 |  1740.12      |        -10.75     | NEUTRAL  | Kraken API    |
| EWJ        | 2026-06-18 00:00:00 |    96.26      |         56.3333   | NEUTRAL  | Yahoo Finance |
| FCX        | 2026-06-18 00:00:00 |    68.68      |         53.8333   | NEUTRAL  | Yahoo Finance |
| FIL-USD    | 2026-06-22 00:00:00 |     0.819     |         19.1667   | NEUTRAL  | Kraken API    |
| GOOGL      | 2026-06-18 00:00:00 |   368.03      |         -8.58333  | NEUTRAL  | Yahoo Finance |
| GRT-USD    | 2026-06-22 00:00:00 |     0.01991   |         -7.5      | NEUTRAL  | Kraken API    |
| HBAR-USD   | 2026-06-22 00:00:00 |     0.07942   |        -27.9167   | NEUTRAL  | Kraken API    |
| HON        | 2026-06-18 00:00:00 |   229.01      |         40        | NEUTRAL  | Yahoo Finance |
| HYG        | 2026-06-18 00:00:00 |    80.01      |         -8.75     | NEUTRAL  | Yahoo Finance |
| ICP-USD    | 2026-06-22 00:00:00 |     2.281     |        -35.5833   | NEUTRAL  | Kraken API    |
| IEF        | 2026-06-18 00:00:00 |    94.36      |        -20.3333   | NEUTRAL  | Yahoo Finance |
| IEMG       | 2026-06-18 00:00:00 |    85.63      |         45.1667   | NEUTRAL  | Yahoo Finance |
| INJ-USD    | 2026-06-22 00:00:00 |     5.016     |        -57.8333   | NEUTRAL  | Kraken API    |
| INTC       | 2026-06-18 00:00:00 |   133.99      |         62.8333   | NEUTRAL  | Yahoo Finance |
| INTU       | 2026-06-18 00:00:00 |   267         |        -71.8333   | NEUTRAL  | Yahoo Finance |
| IWM        | 2026-06-18 00:00:00 |   295.59      |         41.8333   | NEUTRAL  | Yahoo Finance |
| JNJ        | 2026-06-18 00:00:00 |   228.39      |         28.3333   | NEUTRAL  | Yahoo Finance |
| KO         | 2026-06-18 00:00:00 |    79.39      |         17        | NEUTRAL  | Yahoo Finance |
| LDO-USD    | 2026-06-22 00:00:00 |     0.275     |          0.666667 | NEUTRAL  | Kraken API    |
| LIN        | 2026-06-18 00:00:00 |   512.15      |         64.3333   | NEUTRAL  | Yahoo Finance |
| LINK-USD   | 2026-06-22 00:00:00 |     7.94438   |         -5.16667  | NEUTRAL  | Kraken API    |
| LTC-USD    | 2026-06-22 00:00:00 |    45.21      |          2.66667  | NEUTRAL  | Kraken API    |
| MCD        | 2026-06-18 00:00:00 |   278.61      |        -28        | NEUTRAL  | Yahoo Finance |
| META       | 2026-06-18 00:00:00 |   577.22      |        -68.75     | NEUTRAL  | Yahoo Finance |
| MPC        | 2026-06-18 00:00:00 |   242.91      |        -14.5833   | NEUTRAL  | Yahoo Finance |
| MRK        | 2026-06-18 00:00:00 |   113.87      |        -15.0833   | NEUTRAL  | Yahoo Finance |
| MU         | 2026-06-18 00:00:00 |  1133.99      |         48.6667   | NEUTRAL  | Yahoo Finance |
| NEAR-USD   | 2026-06-22 00:00:00 |     2.1797    |         42.8333   | NEUTRAL  | Kraken API    |
| NEM        | 2026-06-18 00:00:00 |   103.79      |         -5.91667  | NEUTRAL  | Yahoo Finance |
| NKE        | 2026-06-18 00:00:00 |    45.2       |        -15.8333   | NEUTRAL  | Yahoo Finance |
| NVDA       | 2026-06-18 00:00:00 |   210.69      |         -3        | NEUTRAL  | Yahoo Finance |
| OP-USD     | 2026-06-22 00:00:00 |     0.1028    |        -15.5833   | NEUTRAL  | Kraken API    |
| OXY        | 2026-06-18 00:00:00 |    51.82      |        -25.25     | NEUTRAL  | Yahoo Finance |
| PEP        | 2026-06-18 00:00:00 |   142.02      |        -29.9167   | NEUTRAL  | Yahoo Finance |
| PEPE-USD   | 2026-06-22 00:00:00 |     2.868e-06 |          3.16667  | NEUTRAL  | Kraken API    |
| PFE        | 2026-06-18 00:00:00 |    25.21      |        -33.4167   | NEUTRAL  | Yahoo Finance |
| POL-USD    | 2026-06-22 00:00:00 |     0.08081   |         20.6667   | NEUTRAL  | Kraken API    |
| QCOM       | 2026-06-18 00:00:00 |   226.11      |         19.9167   | NEUTRAL  | Yahoo Finance |
| QQQ        | 2026-06-18 00:00:00 |   740.62      |         37.5      | NEUTRAL  | Yahoo Finance |
| RENDER-USD | 2026-06-22 00:00:00 |     1.691     |        -23.5833   | NEUTRAL  | Kraken API    |
| SCHW       | 2026-06-18 00:00:00 |    91.7       |         26.1667   | NEUTRAL  | Yahoo Finance |
| SHIB-USD   | 2026-06-22 00:00:00 |     4.715e-06 |        -16.1667   | NEUTRAL  | Kraken API    |
| SHY        | 2026-06-18 00:00:00 |    81.99      |        -45.75     | NEUTRAL  | Yahoo Finance |
| SKY-USD    | 2026-06-22 00:00:00 |     0.05976   |         20.6667   | NEUTRAL  | Kraken API    |
| SLB        | 2026-06-18 00:00:00 |    48.09      |        -27        | NEUTRAL  | Yahoo Finance |
| SMH        | 2026-06-18 00:00:00 |   659.88      |         48.8333   | NEUTRAL  | Yahoo Finance |
| SNX-USD    | 2026-06-22 00:00:00 |     0.2413    |        -16.6667   | NEUTRAL  | Kraken API    |
| SOL-USD    | 2026-06-22 00:00:00 |    74.1       |         21.1667   | NEUTRAL  | Kraken API    |
| SOXX       | 2026-06-18 00:00:00 |   639.45      |         48.8333   | NEUTRAL  | Yahoo Finance |
| SPY        | 2026-06-18 00:00:00 |   746.74      |         18.5833   | NEUTRAL  | Yahoo Finance |
| SUSHI-USD  | 2026-06-22 00:00:00 |     0.1775    |        -16.0833   | NEUTRAL  | Kraken API    |
| TGT        | 2026-06-18 00:00:00 |   130.74      |         64.6667   | NEUTRAL  | Yahoo Finance |
| TLT        | 2026-06-18 00:00:00 |    86.75      |         33.4167   | NEUTRAL  | Yahoo Finance |
| TMUS       | 2026-06-18 00:00:00 |   181.67      |        -22.4167   | NEUTRAL  | Yahoo Finance |
| TSLA       | 2026-06-18 00:00:00 |   400.49      |        -18.8333   | NEUTRAL  | Yahoo Finance |
| TXN        | 2026-06-18 00:00:00 |   322.86      |         33.6667   | NEUTRAL  | Yahoo Finance |
| UPS        | 2026-06-18 00:00:00 |   104.86      |         18.4167   | NEUTRAL  | Yahoo Finance |
| USO        | 2026-06-18 00:00:00 |   114.87      |        -27.0833   | NEUTRAL  | Yahoo Finance |
| VEA        | 2026-06-18 00:00:00 |    72.31      |         41.3333   | NEUTRAL  | Yahoo Finance |
| VIXY       | 2026-06-18 00:00:00 |    21.9       |        -23.0833   | NEUTRAL  | Yahoo Finance |
| VNQ        | 2026-06-18 00:00:00 |    95.56      |         12.1667   | NEUTRAL  | Yahoo Finance |
| VTI        | 2026-06-18 00:00:00 |   369.99      |          7.83333  | NEUTRAL  | Yahoo Finance |
| VWO        | 2026-06-18 00:00:00 |    60.77      |         29.1667   | NEUTRAL  | Yahoo Finance |
| VZ         | 2026-06-18 00:00:00 |    45.37      |        -28        | NEUTRAL  | Yahoo Finance |
| WIF-USD    | 2026-06-22 00:00:00 |     0.1658    |          0.666667 | NEUTRAL  | Kraken API    |
| WMT        | 2026-06-18 00:00:00 |   117.18      |         29.6667   | NEUTRAL  | Yahoo Finance |
| XBI        | 2026-06-18 00:00:00 |   140.72      |         62.8333   | NEUTRAL  | Yahoo Finance |
| XLB        | 2026-06-18 00:00:00 |    51.81      |         53.6667   | NEUTRAL  | Yahoo Finance |
| XLE        | 2026-06-18 00:00:00 |    53.77      |        -23.5833   | NEUTRAL  | Yahoo Finance |
| XLF        | 2026-06-18 00:00:00 |    53.57      |         51.6667   | NEUTRAL  | Yahoo Finance |
| XLI        | 2026-06-18 00:00:00 |   180.91      |         63.1667   | NEUTRAL  | Yahoo Finance |
| XLK        | 2026-06-18 00:00:00 |   191.44      |         35.8333   | NEUTRAL  | Yahoo Finance |
| XLP        | 2026-06-18 00:00:00 |    83.3       |         34.4167   | NEUTRAL  | Yahoo Finance |
| XLU        | 2026-06-18 00:00:00 |    44.76      |         29.4167   | NEUTRAL  | Yahoo Finance |
| XLV        | 2026-06-18 00:00:00 |   149.4       |        -25.5833   | NEUTRAL  | Yahoo Finance |
| XLY        | 2026-06-18 00:00:00 |   117.16      |         -6.83333  | NEUTRAL  | Yahoo Finance |
| XOM        | 2026-06-18 00:00:00 |   137.81      |        -52.3333   | NEUTRAL  | Yahoo Finance |
| XRP-USD    | 2026-06-22 00:00:00 |     1.14322   |         -9.16667  | NEUTRAL  | Kraken API    |
| YFI-USD    | 2026-06-22 00:00:00 |  1839.2       |        -16.1667   | NEUTRAL  | Kraken API    |
| ZEC-USD    | 2026-06-22 00:00:00 |   449.93      |         17.0833   | NEUTRAL  | Kraken API    |
| ADBE       | 2026-06-18 00:00:00 |   195.16      |        -66.8333   | SHORT    | Yahoo Finance |
| BCH-USD    | 2026-06-22 00:00:00 |   199.31      |        -36.5      | SHORT    | Kraken API    |
| BITO       | 2026-06-18 00:00:00 |     8.56      |        -43.5833   | SHORT    | Yahoo Finance |
| CMCSA      | 2026-06-18 00:00:00 |    22.43      |        -49.3333   | SHORT    | Yahoo Finance |
| FET-USD    | 2026-06-22 00:00:00 |     0.1858    |        -37.3333   | SHORT    | Kraken API    |
| FXI        | 2026-06-18 00:00:00 |    33.3       |        -51.25     | SHORT    | Yahoo Finance |
| GDX        | 2026-06-18 00:00:00 |    82.51      |        -40.25     | SHORT    | Yahoo Finance |
| GDXJ       | 2026-06-18 00:00:00 |   107.22      |        -40.25     | SHORT    | Yahoo Finance |
| GLD        | 2026-06-18 00:00:00 |   387.12      |        -56.0833   | SHORT    | Yahoo Finance |
| IBIT       | 2026-06-18 00:00:00 |    35.62      |        -43.5833   | SHORT    | Yahoo Finance |
| IBM        | 2026-06-18 00:00:00 |   249.1       |        -54.4167   | SHORT    | Yahoo Finance |
| MSFT       | 2026-06-18 00:00:00 |   379.4       |        -62.8333   | SHORT    | Yahoo Finance |
| NFLX       | 2026-06-18 00:00:00 |    77.38      |        -61.1667   | SHORT    | Yahoo Finance |
| NOW        | 2026-06-18 00:00:00 |    95.04      |        -60.5833   | SHORT    | Yahoo Finance |
| ORCL       | 2026-06-18 00:00:00 |   184.29      |        -57.5      | SHORT    | Yahoo Finance |
| SLV        | 2026-06-18 00:00:00 |    59.51      |        -56.0833   | SHORT    | Yahoo Finance |
| T          | 2026-06-18 00:00:00 |    22.01      |        -61.6667   | SHORT    | Yahoo Finance |
| TMO        | 2026-06-18 00:00:00 |   464.61      |        -51.25     | SHORT    | Yahoo Finance |
| XLC        | 2026-06-18 00:00:00 |   109.45      |        -60.8333   | SHORT    | Yahoo Finance |

## Edge Summary

- Symbols with trades: **160** of 160
- Beat buy-and-hold: **35.00%** of traded symbols
- Positive return: **33.12%** of traded symbols
- Median strategy return: **-9.44%** (benchmark **12.50%**)
- Median excess vs benchmark: **-25.35%**
- Median Sharpe: **-0.04**
- Median exposure: **44.34%**

> Edge is real only if both _beat buy-and-hold_ and _median excess_ are convincingly positive across many symbols. Treat a single high-return symbol as noise.

## Portfolio Backtest

Actual capital-allocation books (not per-symbol averages). Benchmarks: `equal_weight_buyhold` (whole tracked universe), `spy_buyhold` (100% SPY), and `sixty_forty` (60% SPY / 40% AGG). `high_conf_voltarget` inverse-vol-weights the HIGH-confidence book; `conviction_long_short` is market-neutral. Judge on **Sharpe** and **max_drawdown** out-of-sample, not raw return: a fully-invested long book wins on return in a bull market but carries all the risk.

| strategy              | scope         | ann_return   | ann_vol   |   sharpe | max_drawdown   | total_return   |   avg_gross_exposure |
|:----------------------|:--------------|:-------------|:----------|---------:|:---------------|:---------------|---------------------:|
| equal_weight_buyhold  | full          | -10.36%      | 33.78%    |    -0.31 | -57.63%        | -38.86%        |                 1    |
| equal_weight_buyhold  | out_of_sample | -4.01%       | 34.37%    |    -0.12 | -39.63%        | -10.03%        |                 1    |
| all_signals_ew        | full          | -8.44%       | 28.21%    |    -0.3  | -59.88%        | -31.58%        |                 1    |
| all_signals_ew        | out_of_sample | 7.68%        | 28.50%    |     0.27 | -23.98%        | 3.97%          |                 1    |
| high_conf_ew          | full          | 2.11%        | 32.87%    |     0.06 | -44.49%        | -9.40%         |                 0.89 |
| high_conf_ew          | out_of_sample | 31.12%       | 36.40%    |     0.85 | -20.80%        | 30.10%         |                 0.89 |
| high_conf_voltarget   | full          | 3.19%        | 30.57%    |     0.1  | -36.53%        | -4.23%         |                 0.89 |
| high_conf_voltarget   | out_of_sample | 24.33%       | 34.63%    |     0.7  | -16.98%        | 21.84%         |                 0.89 |
| conviction_long_short | full          | -9.33%       | 23.52%    |    -0.4  | -35.58%        | -30.90%        |                 0.97 |
| conviction_long_short | out_of_sample | -6.47%       | 27.18%    |    -0.24 | -20.72%        | -10.30%        |                 0.97 |
| spy_buyhold           | full          | 8.02%        | 13.38%    |     0.6  | -17.81%        | 24.28%         |                 0.78 |
| spy_buyhold           | out_of_sample | -2.56%       | 9.98%     |    -0.26 | -14.83%        | -3.21%         |                 0.78 |
| sixty_forty           | full          | 4.63%        | 8.48%     |     0.55 | -10.80%        | 13.91%         |                 0.78 |
| sixty_forty           | out_of_sample | -2.55%       | 6.50%     |    -0.39 | -10.06%        | -2.91%         |                 0.78 |

## Walk-Forward Robustness

Each book measured across contiguous time folds (each a different regime). A book has durable edge only if `mean_sharpe` is positive, `min_sharpe` isn't deeply negative, and `pct_positive_folds` is high — a single great fold doesn't count. `fold_sharpes` lists each fold oldest-to-newest.

| strategy              |   n_folds |   mean_sharpe |   median_sharpe |   min_sharpe | pct_positive_folds   | mean_return   | fold_sharpes                |
|:----------------------|----------:|--------------:|----------------:|-------------:|:---------------------|:--------------|:----------------------------|
| equal_weight_buyhold  |         5 |         -0.02 |            0.08 |        -1.72 | 60.00%               | -6.93%        | 1.43;-1.72;0.85;-0.74;0.08  |
| all_signals_ew        |         5 |         -0.18 |            0.32 |        -1.24 | 60.00%               | -6.07%        | 0.32;0.47;-1.24;-1.19;0.75  |
| high_conf_ew          |         5 |          0.27 |           -0.11 |        -0.64 | 40.00%               | -1.19%        | 1.17;-0.15;-0.64;-0.11;1.08 |
| high_conf_voltarget   |         5 |          0.41 |            0.1  |        -0.67 | 60.00%               | -0.34%        | 2.06;0.10;-0.67;-0.04;0.60  |
| conviction_long_short |         5 |         -0.4  |           -0.3  |        -1.43 | 40.00%               | -6.82%        | -1.43;0.36;-0.30;-0.73;0.07 |
| spy_buyhold           |         5 |          0.6  |            0.23 |        -0.23 | 80.00%               | 4.57%         | 1.58;1.23;0.23;-0.23;0.20   |
| sixty_forty           |         5 |          0.53 |            0.24 |        -0.15 | 60.00%               | 2.70%         | 1.68;0.87;0.24;-0.15;-0.00  |

## Strategy Comparison

Each decision rule backtested over the same data. `out_of_sample` is the most recent ~35% of each symbol's history (unseen tail). A rule has real edge only if `median_excess` and `beat_benchmark_pct` stay positive out-of-sample, not just full-sample.

| strategy        | scope         |   symbols | beat_benchmark_pct   | positive_pct   | median_return   | median_benchmark   | median_excess   |   median_sharpe |   total_trades |
|:----------------|:--------------|----------:|:---------------------|:---------------|:----------------|:-------------------|:----------------|----------------:|---------------:|
| trend           | full          |       160 | 35.00%               | 33.12%         | -9.44%          | 12.50%             | -25.35%         |           -0.04 |          11204 |
| trend           | out_of_sample |       160 | 38.12%               | 54.37%         | 4.26%           | 4.11%              | -7.55%          |            0.38 |           3919 |
| mean_reversion  | full          |       157 | 42.04%               | 48.41%         | -0.20%          | 12.50%             | -16.07%         |           -0.03 |           1246 |
| mean_reversion  | out_of_sample |       128 | 43.75%               | 57.81%         | 0.33%           | 1.28%              | -2.37%          |            0.67 |            474 |
| regime_adaptive | full          |       160 | 36.25%               | 33.12%         | -9.34%          | 12.50%             | -25.46%         |           -0.04 |          11479 |
| regime_adaptive | out_of_sample |       160 | 37.50%               | 56.25%         | 4.14%           | 4.11%              | -7.84%          |            0.4  |           4022 |

## Signal Calibration

Realized forward return in the signal's direction, grouped by confidence. HIGH should outrank LOW for the confidence score to be meaningful.

| confidence_level   |   horizon |     n | mean_return   | median_return   | win_rate   |
|:-------------------|----------:|------:|:--------------|:----------------|:-----------|
| HIGH               |         5 |  8160 | 0.18%         | 0.14%           | 52.34%     |
| MEDIUM             |         5 | 29215 | 0.08%         | 0.10%           | 51.13%     |
| LOW                |         5 |  3278 | -0.55%        | -0.47%          | 45.21%     |
| ALL                |         5 | 40653 | 0.05%         | 0.07%           | 50.90%     |
| HIGH               |        10 |  8123 | 0.50%         | 0.19%           | 52.28%     |
| MEDIUM             |        10 | 28989 | 0.22%         | 0.14%           | 51.18%     |
| LOW                |        10 |  3253 | -0.83%        | -0.70%          | 45.43%     |
| ALL                |        10 | 40365 | 0.19%         | 0.11%           | 50.94%     |
| HIGH               |        20 |  8036 | 0.92%         | 0.50%           | 53.83%     |
| MEDIUM             |        20 | 28436 | 0.91%         | 0.64%           | 53.67%     |
| LOW                |        20 |  3210 | -0.58%        | -0.50%          | 47.20%     |
| ALL                |        20 | 39682 | 0.79%         | 0.54%           | 53.18%     |

## Backtest Summary

### Data Quality / Signal Availability

- **ok**: 160 symbols

| symbol     |   trades | return   | benchmark_return   | mdd     |   sharpe | exposure   | skipped_reason   |
|:-----------|---------:|:---------|:-------------------|:--------|---------:|:-----------|:-----------------|
| AAPL       |       63 | 13.75%   | 54.87%             | -20.65% |     0.37 | 48.42%     | ok               |
| AAVE-USD   |       76 | -61.36%  | -77.37%            | -68.72% |    -0.73 | 36.59%     | ok               |
| ABBV       |       64 | -14.10%  | 31.68%             | -30.55% |    -0.26 | 48.59%     | ok               |
| ADA-USD    |       84 | -83.00%  | -85.81%            | -89.69% |    -0.67 | 46.17%     | ok               |
| ADBE       |       68 | -22.41%  | -68.21%            | -38.12% |    -0.23 | 56.91%     | ok               |
| AGG        |       69 | -6.61%   | 0.85%              | -10.16% |    -1.1  | 31.11%     | ok               |
| ALGO-USD   |       86 | -50.43%  | -80.61%            | -53.13% |    -0.57 | 38.12%     | ok               |
| AMAT       |       69 | -14.57%  | 269.75%            | -57.21% |    -0.03 | 53.41%     | ok               |
| AMD        |       56 | 1.22%    | 203.17%            | -46.42% |     0.22 | 37.94%     | ok               |
| AMGN       |       71 | -19.93%  | 8.28%              | -34.14% |    -0.39 | 47.75%     | ok               |
| AMZN       |       74 | -33.84%  | 53.59%             | -42.48% |    -0.99 | 38.27%     | ok               |
| APT-USD    |       76 | -26.57%  | -93.06%            | -69.96% |    -0    | 44.25%     | ok               |
| ARB-USD    |       68 | -0.31%   | -89.60%            | -62.67% |     0.24 | 39.27%     | ok               |
| ARKK       |       79 | -30.02%  | 74.63%             | -32.63% |    -0.5  | 38.94%     | ok               |
| ATOM-USD   |       88 | -67.61%  | -74.76%            | -73.59% |    -1.11 | 44.25%     | ok               |
| AVAX-USD   |       70 | -20.17%  | -84.82%            | -53.72% |    -0.04 | 39.27%     | ok               |
| AVGO       |       60 | 32.21%   | 241.40%            | -35.76% |     0.5  | 45.26%     | ok               |
| BA         |       69 | 4.96%    | 8.40%              | -30.56% |     0.21 | 49.92%     | ok               |
| BAC        |       78 | -15.06%  | 68.11%             | -27.64% |    -0.36 | 46.92%     | ok               |
| BCH-USD    |       76 | -0.30%   | -59.26%            | -53.87% |     0.21 | 47.70%     | ok               |
| BITO       |       78 | 6.93%    | -57.83%            | -42.82% |     0.26 | 40.60%     | ok               |
| BLK        |       77 | -8.18%   | 33.38%             | -21.68% |    -0.18 | 42.76%     | ok               |
| BND        |       65 | -7.32%   | 0.88%              | -9.89%  |    -1.18 | 32.28%     | ok               |
| BONK-USD   |       70 | 70.45%   | -86.11%            | -45.22% |     0.72 | 41.95%     | ok               |
| BTC-USD    |       70 | 6.41%    | -38.20%            | -23.38% |     0.25 | 51.15%     | ok               |
| C          |       81 | -24.08%  | 166.55%            | -37.02% |    -0.45 | 50.58%     | ok               |
| CAT        |       70 | 34.32%   | 229.23%            | -21.02% |     0.62 | 56.74%     | ok               |
| CL         |       60 | 15.02%   | 8.03%              | -14.32% |     0.53 | 47.92%     | ok               |
| CMCSA      |       82 | -38.75%  | -48.26%            | -40.02% |    -1    | 44.26%     | ok               |
| COMP-USD   |       89 | -36.73%  | -80.19%            | -58.43% |    -0.21 | 45.02%     | ok               |
| COP        |       73 | -24.21%  | -4.00%             | -43.77% |    -0.45 | 40.27%     | ok               |
| COST       |       60 | 5.63%    | 38.52%             | -29.73% |     0.23 | 46.59%     | ok               |
| CRM        |       65 | -35.46%  | -45.78%            | -41.46% |    -0.72 | 43.76%     | ok               |
| CRV-USD    |       64 | -12.80%  | -79.77%            | -39.89% |     0.09 | 34.48%     | ok               |
| CSCO       |       59 | 21.86%   | 129.27%            | -21.79% |     0.49 | 50.42%     | ok               |
| CVX        |       69 | -15.07%  | 16.42%             | -26.75% |    -0.38 | 41.10%     | ok               |
| DASH-USD   |       65 | -42.91%  | -18.24%            | -64.43% |    -0.02 | 31.80%     | ok               |
| DBC        |       58 | -12.57%  | 22.20%             | -25.35% |    -0.43 | 32.78%     | ok               |
| DE         |       72 | -6.80%   | 49.70%             | -25.24% |    -0.06 | 45.76%     | ok               |
| DIA        |       60 | -2.42%   | 35.28%             | -12.94% |    -0.09 | 45.92%     | ok               |
| DIS        |       65 | -3.51%   | 8.95%              | -26.52% |     0.04 | 48.25%     | ok               |
| DOGE-USD   |       75 | -16.53%  | -79.79%            | -60.95% |     0.09 | 49.81%     | ok               |
| DOT-USD    |       90 | -46.67%  | -87.16%            | -60.68% |    -0.34 | 47.70%     | ok               |
| DXY-INDEX  |       40 | -1.45%   | -0.23%             | -6.02%  |    -0.22 | 28.85%     | ok               |
| EEM        |       64 | -9.40%   | 82.03%             | -25.67% |    -0.25 | 43.43%     | ok               |
| EFA        |       60 | -8.17%   | 39.12%             | -13.72% |    -0.29 | 44.09%     | ok               |
| EOG        |       77 | -24.73%  | 12.50%             | -48.13% |    -0.54 | 46.09%     | ok               |
| ETC-USD    |       64 | -35.69%  | -73.79%            | -48.16% |    -0.51 | 31.23%     | ok               |
| ETH-USD    |       58 | 164.78%  | -49.91%            | -30.11% |     1.31 | 44.64%     | ok               |
| EWJ        |       64 | -16.66%  | 47.21%             | -30.73% |    -0.52 | 40.77%     | ok               |
| FCX        |       69 | -31.93%  | 73.48%             | -46.84% |    -0.39 | 45.92%     | ok               |
| FET-USD    |       83 | -16.23%  | -86.80%            | -54.02% |     0.14 | 39.66%     | ok               |
| FIL-USD    |       70 | -33.66%  | -85.97%            | -49.05% |    -0.29 | 33.14%     | ok               |
| FXI        |       46 | -4.97%   | 47.35%             | -23.91% |    -0.04 | 28.29%     | ok               |
| GDX        |       62 | -0.72%   | 193.94%            | -34.99% |     0.12 | 48.09%     | ok               |
| GDXJ       |       68 | -27.99%  | 214.15%            | -44.93% |    -0.32 | 45.92%     | ok               |
| GE         |       74 | 20.01%   | 241.58%            | -27.82% |     0.43 | 52.25%     | ok               |
| GLD        |       48 | 22.59%   | 107.00%            | -16.63% |     0.6  | 44.76%     | ok               |
| GOOGL      |       63 | 68.66%   | 141.82%            | -20.41% |     1.06 | 53.91%     | ok               |
| GRT-USD    |       87 | -12.67%  | -91.53%            | -56.53% |     0.07 | 41.76%     | ok               |
| GS         |       76 | 0.54%    | 190.26%            | -22.13% |     0.11 | 51.41%     | ok               |
| HD         |       71 | -2.85%   | -5.92%             | -17.69% |     0    | 43.76%     | ok               |
| HON        |       97 | -28.76%  | 20.41%             | -30.75% |    -0.78 | 53.24%     | ok               |
| HYG        |       81 | -9.52%   | 3.07%              | -9.59%  |    -1.11 | 34.28%     | ok               |
| IBIT       |       32 | 35.91%   | -6.29%             | -18.95% |     0.76 | 30.83%     | ok               |
| IBM        |       72 | 11.96%   | 32.91%             | -25.31% |     0.33 | 50.42%     | ok               |
| ICP-USD    |       83 | -1.35%   | -79.90%            | -55.67% |     0.25 | 38.70%     | ok               |
| IEF        |       76 | -10.90%  | -0.63%             | -11.70% |    -1.54 | 32.78%     | ok               |
| IEMG       |       58 | -5.52%   | 74.86%             | -26.84% |    -0.12 | 43.59%     | ok               |
| INJ-USD    |       75 | -52.18%  | -79.73%            | -77.42% |    -0.49 | 37.93%     | ok               |
| INTC       |       70 | 55.82%   | 206.96%            | -60.60% |     0.62 | 49.25%     | ok               |
| INTU       |       65 | -12.51%  | -58.37%            | -43.77% |    -0.09 | 42.76%     | ok               |
| ITA        |       74 | -0.63%   | 95.83%             | -23.75% |     0.06 | 47.25%     | ok               |
| IWM        |       50 | 9.03%    | 50.83%             | -12.83% |     0.37 | 36.44%     | ok               |
| JNJ        |       72 | 5.96%    | 43.19%             | -17.51% |     0.27 | 50.42%     | ok               |
| JPM        |       75 | -20.07%  | 88.77%             | -33.43% |    -0.49 | 52.75%     | ok               |
| KO         |       51 | 27.92%   | 33.72%             | -8.07%  |     1    | 37.94%     | ok               |
| LDO-USD    |       74 | 1.95%    | -86.22%            | -60.93% |     0.29 | 37.93%     | ok               |
| LIN        |       68 | -0.80%   | 26.76%             | -21.53% |     0.03 | 38.94%     | ok               |
| LINK-USD   |       70 | -13.55%  | -68.35%            | -50.48% |     0.1  | 41.57%     | ok               |
| LLY        |       69 | -14.87%  | 71.85%             | -53.34% |    -0.12 | 51.41%     | ok               |
| LRCX       |       80 | -9.67%   | 363.67%            | -63.56% |     0.05 | 46.26%     | ok               |
| LTC-USD    |       66 | -34.00%  | -67.02%            | -53.76% |    -0.29 | 48.47%     | ok               |
| MCD        |       75 | -2.55%   | -4.67%             | -18.81% |    -0.05 | 38.10%     | ok               |
| META       |       72 | -14.91%  | 46.45%             | -38.96% |    -0.11 | 50.58%     | ok               |
| MPC        |       71 | -13.74%  | 51.33%             | -44.76% |    -0.14 | 49.92%     | ok               |
| MRK        |       67 | -27.01%  | -5.75%             | -34.46% |    -0.62 | 46.59%     | ok               |
| MS         |       81 | -13.59%  | 154.38%            | -27.79% |    -0.27 | 48.42%     | ok               |
| MSFT       |       83 | -34.40%  | -6.07%             | -38.02% |    -0.91 | 48.09%     | ok               |
| MU         |       51 | 270.31%  | 1187.89%           | -68.76% |     1.34 | 59.90%     | ok               |
| NEAR-USD   |       87 | 2.38%    | -62.11%            | -60.07% |     0.28 | 41.76%     | ok               |
| NEM        |       78 | -30.28%  | 203.39%            | -38.49% |    -0.31 | 54.91%     | ok               |
| NFLX       |       62 | 30.03%   | 35.65%             | -21.09% |     0.67 | 54.74%     | ok               |
| NKE        |       91 | -37.83%  | -56.01%            | -55.35% |    -0.53 | 43.76%     | ok               |
| NOW        |       80 | 25.64%   | -38.24%            | -30.25% |     0.46 | 45.92%     | ok               |
| NVDA       |       74 | -30.87%  | 121.77%            | -45.02% |    -0.27 | 59.00%     | ok               |
| OP-USD     |       72 | 8.32%    | -94.77%            | -70.27% |     0.33 | 35.63%     | ok               |
| ORCL       |       74 | 51.65%   | 60.76%             | -29.47% |     0.62 | 53.58%     | ok               |
| OXY        |       63 | 2.48%    | -11.27%            | -30.85% |     0.16 | 43.09%     | ok               |
| PEP        |       85 | -10.61%  | -15.39%            | -21.35% |    -0.25 | 50.08%     | ok               |
| PEPE-USD   |       77 | 10.36%   | -85.87%            | -57.66% |     0.36 | 43.87%     | ok               |
| PFE        |       77 | -39.48%  | -8.23%             | -42.29% |    -1.26 | 36.11%     | ok               |
| PG         |       62 | -11.11%  | -3.69%             | -21.65% |    -0.39 | 41.43%     | ok               |
| PM         |       81 | -1.28%   | 96.37%             | -33.68% |     0.07 | 57.57%     | ok               |
| POL-USD    |       79 | 64.83%   | -84.08%            | -46.45% |     0.77 | 49.62%     | ok               |
| QCOM       |       77 | -16.82%  | 50.02%             | -57.69% |    -0.06 | 47.75%     | ok               |
| QQQ        |       62 | 19.13%   | 74.75%             | -12.88% |     0.55 | 46.26%     | ok               |
| RENDER-USD |       96 | -17.59%  | -59.35%            | -45.00% |     0.11 | 43.74%     | ok               |
| RTX        |       58 | 19.95%   | 105.29%            | -16.99% |     0.53 | 51.58%     | ok               |
| SBUX       |       62 | -25.10%  | 8.46%              | -29.34% |    -0.52 | 38.60%     | ok               |
| SCHW       |       74 | -21.97%  | 43.19%             | -30.41% |    -0.52 | 45.42%     | ok               |
| SHIB-USD   |       76 | -25.73%  | -80.52%            | -48.95% |    -0.1  | 52.30%     | ok               |
| SHY        |       50 | -2.23%   | -0.16%             | -2.85%  |    -0.77 | 34.94%     | ok               |
| SKY-USD    |       68 | -29.87%  | 3.34%              | -43.98% |    -0.39 | 40.70%     | ok               |
| SLB        |       77 | -30.54%  | -9.13%             | -55.49% |    -0.55 | 49.92%     | ok               |
| SLV        |       58 | 34.54%   | 185.28%            | -42.66% |     0.56 | 40.43%     | ok               |
| SMH        |       48 | 98.56%   | 250.50%            | -33.99% |     1.22 | 50.75%     | ok               |
| SNX-USD    |       61 | 24.76%   | -87.83%            | -32.91% |     0.46 | 39.66%     | ok               |
| SOL-USD    |       68 | -42.35%  | -66.26%            | -56.90% |    -0.22 | 60.15%     | ok               |
| SOXX       |       55 | 86.24%   | 220.92%            | -40.34% |     1.07 | 49.75%     | ok               |
| SPY        |       60 | 6.50%    | 53.21%             | -16.47% |     0.28 | 50.92%     | ok               |
| SUSHI-USD  |       90 | -75.60%  | -89.64%            | -81.22% |    -1.06 | 35.44%     | ok               |
| T          |       62 | 37.57%   | 27.30%             | -17.01% |     0.87 | 50.58%     | ok               |
| TGT        |       56 | -11.79%  | -8.27%             | -41.74% |    -0.16 | 38.60%     | ok               |
| TIA-USD    |       84 | -17.64%  | -93.02%            | -55.19% |     0.06 | 34.48%     | ok               |
| TLT        |       70 | -23.55%  | -7.50%             | -23.95% |    -1.74 | 32.11%     | ok               |
| TMO        |       59 | 13.87%   | -15.11%            | -16.83% |     0.38 | 47.92%     | ok               |
| TMUS       |       72 | 14.44%   | 12.03%             | -24.50% |     0.39 | 48.09%     | ok               |
| TRX-USD    |       74 | 0.84%    | 31.75%             | -22.90% |     0.11 | 49.23%     | ok               |
| TSLA       |       66 | -0.11%   | 118.55%            | -54.91% |     0.21 | 42.26%     | ok               |
| TXN        |       77 | -15.83%  | 96.76%             | -46.98% |    -0.1  | 53.41%     | ok               |
| UNH        |       76 | 23.44%   | -20.32%            | -27.46% |     0.45 | 52.08%     | ok               |
| UNI-USD    |       90 | -73.41%  | -79.55%            | -81.03% |    -0.91 | 41.57%     | ok               |
| UPS        |       66 | -37.30%  | -34.17%            | -40.62% |    -0.74 | 39.93%     | ok               |
| USO        |       68 | 1.63%    | 57.14%             | -44.00% |     0.15 | 34.61%     | ok               |
| VEA        |       58 | -0.98%   | 52.46%             | -17.93% |     0.01 | 44.09%     | ok               |
| VIXY       |       94 | -78.98%  | -62.06%            | -87.58% |    -0.97 | 31.95%     | ok               |
| VNQ        |       75 | -16.77%  | 12.50%             | -24.92% |    -0.7  | 37.60%     | ok               |
| VTI        |       66 | -0.72%   | 52.81%             | -18.77% |     0.04 | 52.08%     | ok               |
| VWO        |       76 | -13.41%  | 51.32%             | -25.20% |    -0.47 | 44.09%     | ok               |
| VZ         |       85 | -27.54%  | 7.00%              | -31.88% |    -0.96 | 37.94%     | ok               |
| WFC        |       86 | -20.20%  | 63.35%             | -29.91% |    -0.36 | 47.92%     | ok               |
| WIF-USD    |       70 | -26.73%  | -91.17%            | -50.54% |    -0.01 | 32.18%     | ok               |
| WMT        |       57 | 27.82%   | 114.00%            | -21.31% |     0.75 | 51.75%     | ok               |
| XBI        |       62 | -4.13%   | 59.47%             | -21.75% |    -0.02 | 39.43%     | ok               |
| XLB        |       70 | -14.85%  | 25.58%             | -26.57% |    -0.51 | 37.60%     | ok               |
| XLC        |       65 | 15.26%   | 40.90%             | -12.33% |     0.53 | 55.57%     | ok               |
| XLE        |       71 | -9.48%   | 27.64%             | -36.18% |    -0.17 | 46.59%     | ok               |
| XLF        |       76 | -12.23%  | 38.60%             | -23.61% |    -0.41 | 48.25%     | ok               |
| XLI        |       64 | 5.22%    | 59.49%             | -11.38% |     0.25 | 46.59%     | ok               |
| XLK        |       42 | 64.71%   | 89.78%             | -14.75% |     1.2  | 48.25%     | ok               |
| XLM-USD    |       71 | -1.93%   | -55.99%            | -46.56% |     0.2  | 45.79%     | ok               |
| XLP        |       70 | 7.46%    | 14.69%             | -10.28% |     0.45 | 42.60%     | ok               |
| XLU        |       69 | -4.29%   | 46.25%             | -18.15% |    -0.15 | 38.44%     | ok               |
| XLV        |       68 | -10.46%  | 7.27%              | -16.83% |    -0.5  | 36.44%     | ok               |
| XLY        |       74 | 0.81%    | 36.49%             | -14.01% |     0.09 | 44.43%     | ok               |
| XOM        |       56 | 4.30%    | 33.80%             | -20.29% |     0.19 | 36.11%     | ok               |
| XRP-USD    |       62 | -36.21%  | -65.28%            | -48.42% |    -0.36 | 35.82%     | ok               |
| YFI-USD    |       81 | -53.87%  | -78.93%            | -67.78% |    -0.79 | 40.42%     | ok               |
| ZEC-USD    |       71 | 39.82%   | 717.61%            | -47.68% |     0.54 | 36.78%     | ok               |

## AAPL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 23.40%   | 54.87%             | -21.71% |     0.53 |       67 | 52.58%     | ok               |
|          25 | 17.50%   | 54.87%             | -20.03% |     0.43 |       65 | 50.42%     | ok               |
|          15 | 16.06%   | 54.87%             | -23.86% |     0.4  |       76 | 60.07%     | ok               |
|          30 | 13.75%   | 54.87%             | -20.65% |     0.37 |       63 | 48.42%     | ok               |
|          35 | 8.10%    | 54.87%             | -22.04% |     0.27 |       63 | 46.09%     | ok               |

## AAVE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 5.38%    | -77.37%            | -46.87% |     0.27 |       38 | 26.05%     | ok               |
|          40 | -0.24%   | -77.37%            | -43.61% |     0.21 |       38 | 29.69%     | ok               |
|          35 | -24.98%  | -77.37%            | -51.96% |    -0.1  |       52 | 32.38%     | ok               |
|          50 | -29.70%  | -77.37%            | -47.78% |    -0.27 |       42 | 20.31%     | ok               |
|          15 | -60.29%  | -77.37%            | -64.84% |    -0.5  |       82 | 50.57%     | ok               |

## ABBV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 2.18%    | 31.68%             | -23.85% |     0.14 |       50 | 38.10%     | ok               |
|          40 | -10.54%  | 31.68%             | -26.61% |    -0.19 |       64 | 42.93%     | ok               |
|          35 | -11.82%  | 31.68%             | -27.83% |    -0.22 |       66 | 45.76%     | ok               |
|          30 | -14.10%  | 31.68%             | -30.55% |    -0.26 |       64 | 48.59%     | ok               |
|          45 | -13.33%  | 31.68%             | -29.59% |    -0.27 |       54 | 40.27%     | ok               |

## ADA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -83.73%  | -85.81%            | -91.83% |    -0.58 |       80 | 61.49%     | ok               |
|          50 | -77.92%  | -85.81%            | -85.97% |    -0.59 |       55 | 26.82%     | ok               |
|          20 | -83.57%  | -85.81%            | -92.33% |    -0.6  |       84 | 56.32%     | ok               |
|          45 | -80.28%  | -85.81%            | -88.02% |    -0.62 |       58 | 31.61%     | ok               |
|          35 | -82.47%  | -85.81%            | -89.77% |    -0.66 |       76 | 42.15%     | ok               |

## ADBE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 11.03%   | -68.21%            | -21.34% |     0.3  |       78 | 49.25%     | ok               |
|          40 | -3.30%   | -68.21%            | -20.88% |     0.06 |       74 | 42.26%     | ok               |
|          25 | -8.77%   | -68.21%            | -32.72% |     0.02 |       52 | 61.23%     | ok               |
|          15 | -18.31%  | -68.21%            | -33.11% |    -0.13 |       61 | 66.06%     | ok               |
|          20 | -20.10%  | -68.21%            | -35.78% |    -0.16 |       52 | 63.39%     | ok               |

## AGG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -6.61%   | 0.85%              | -10.16% |    -1.1  |       69 | 31.11%     | ok               |
|          45 | -5.75%   | 0.85%              | -7.89%  |    -1.16 |       52 | 20.47%     | ok               |
|          20 | -8.00%   | 0.85%              | -10.96% |    -1.18 |       73 | 36.61%     | ok               |
|          50 | -5.57%   | 0.85%              | -7.92%  |    -1.25 |       46 | 16.97%     | ok               |
|          25 | -8.17%   | 0.85%              | -11.60% |    -1.25 |       73 | 34.94%     | ok               |

## ALGO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -50.43%  | -80.61%            | -53.13% |    -0.57 |       86 | 38.12%     | ok               |
|          15 | -59.49%  | -80.61%            | -69.47% |    -0.62 |       86 | 50.19%     | ok               |
|          25 | -61.32%  | -80.61%            | -73.33% |    -0.72 |       88 | 45.21%     | ok               |
|          20 | -63.10%  | -80.61%            | -72.09% |    -0.73 |       88 | 47.89%     | ok               |
|          50 | -45.64%  | -80.61%            | -48.43% |    -0.81 |       42 | 16.86%     | ok               |

## AMAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 2.07%    | 269.75%            | -54.05% |     0.21 |       66 | 62.06%     | ok               |
|          30 | -14.57%  | 269.75%            | -57.21% |    -0.03 |       69 | 53.41%     | ok               |
|          20 | -20.82%  | 269.75%            | -60.16% |    -0.1  |       72 | 58.57%     | ok               |
|          50 | -18.65%  | 269.75%            | -48.72% |    -0.13 |       52 | 39.27%     | ok               |
|          35 | -20.65%  | 269.75%            | -55.26% |    -0.13 |       71 | 51.25%     | ok               |

## AMD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 1.22%    | 203.17%            | -46.42% |     0.22 |       56 | 37.94%     | ok               |
|          50 | -0.56%   | 203.17%            | -48.07% |     0.2  |       60 | 32.28%     | ok               |
|          35 | -11.68%  | 203.17%            | -54.16% |     0.09 |       62 | 39.93%     | ok               |
|          45 | -19.13%  | 203.17%            | -55.61% |    -0.01 |       64 | 35.27%     | ok               |
|          30 | -23.33%  | 203.17%            | -59.51% |    -0.04 |       63 | 42.43%     | ok               |

## AMGN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -14.64%  | 8.28%              | -26.64% |    -0.23 |       73 | 53.91%     | ok               |
|          15 | -17.66%  | 8.28%              | -27.92% |    -0.28 |       71 | 59.57%     | ok               |
|          35 | -17.17%  | 8.28%              | -31.23% |    -0.32 |       69 | 44.09%     | ok               |
|          30 | -19.93%  | 8.28%              | -34.14% |    -0.39 |       71 | 47.75%     | ok               |
|          25 | -23.19%  | 8.28%              | -33.41% |    -0.47 |       67 | 50.08%     | ok               |

## AMZN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -17.76%  | 53.59%             | -28.64% |    -0.51 |       50 | 29.95%     | ok               |
|          50 | -25.03%  | 53.59%             | -35.48% |    -0.88 |       48 | 24.13%     | ok               |
|          45 | -25.83%  | 53.59%             | -35.42% |    -0.88 |       50 | 27.12%     | ok               |
|          35 | -29.64%  | 53.59%             | -38.24% |    -0.91 |       62 | 33.11%     | ok               |
|          30 | -33.84%  | 53.59%             | -42.48% |    -0.99 |       74 | 38.27%     | ok               |

## APT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 51.21%   | -93.06%            | -46.73% |     0.73 |       44 | 20.69%     | ok               |
|          45 | 14.97%   | -93.06%            | -63.86% |     0.37 |       60 | 26.82%     | ok               |
|          40 | -7.11%   | -93.06%            | -63.33% |     0.16 |       66 | 32.38%     | ok               |
|          20 | -15.40%  | -93.06%            | -70.51% |     0.14 |       71 | 52.30%     | ok               |
|          35 | -13.92%  | -93.06%            | -64.45% |     0.11 |       70 | 38.12%     | ok               |

## ARB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 56.78%   | -89.60%            | -53.74% |     0.65 |       85 | 56.32%     | ok               |
|          40 | 45.76%   | -89.60%            | -47.60% |     0.62 |       50 | 30.27%     | ok               |
|          35 | 31.50%   | -89.60%            | -56.00% |     0.51 |       60 | 33.72%     | ok               |
|          20 | 26.11%   | -89.60%            | -60.40% |     0.48 |       75 | 50.19%     | ok               |
|          45 | 24.86%   | -89.60%            | -50.83% |     0.46 |       56 | 23.37%     | ok               |

## ARKK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -26.33%  | 74.63%             | -34.90% |    -0.32 |       92 | 50.42%     | ok               |
|          20 | -30.68%  | 74.63%             | -34.90% |    -0.44 |       87 | 45.76%     | ok               |
|          30 | -30.02%  | 74.63%             | -32.63% |    -0.5  |       79 | 38.94%     | ok               |
|          35 | -31.21%  | 74.63%             | -33.79% |    -0.56 |       78 | 36.61%     | ok               |
|          40 | -32.66%  | 74.63%             | -34.78% |    -0.64 |       70 | 31.78%     | ok               |

## ATOM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -64.93%  | -74.76%            | -71.10% |    -0.95 |       93 | 50.96%     | ok               |
|          15 | -69.45%  | -74.76%            | -72.76% |    -1.01 |       93 | 60.73%     | ok               |
|          45 | -59.16%  | -74.76%            | -64.98% |    -1.09 |       72 | 28.35%     | ok               |
|          30 | -67.61%  | -74.76%            | -73.59% |    -1.11 |       88 | 44.25%     | ok               |
|          20 | -72.28%  | -74.76%            | -75.03% |    -1.16 |      101 | 54.79%     | ok               |

## AVAX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 23.77%   | -84.82%            | -29.53% |     0.47 |       34 | 19.16%     | ok               |
|          45 | 18.70%   | -84.82%            | -32.82% |     0.41 |       34 | 22.99%     | ok               |
|          40 | 18.66%   | -84.82%            | -32.96% |     0.41 |       40 | 25.86%     | ok               |
|          15 | 10.39%   | -84.82%            | -52.46% |     0.35 |       61 | 53.26%     | ok               |
|          35 | 10.11%   | -84.82%            | -36.30% |     0.32 |       58 | 31.23%     | ok               |

## AVGO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 32.21%   | 241.40%            | -35.76% |     0.5  |       60 | 45.26%     | ok               |
|          25 | 27.51%   | 241.40%            | -38.01% |     0.46 |       64 | 45.92%     | ok               |
|          35 | 23.22%   | 241.40%            | -36.19% |     0.42 |       70 | 42.60%     | ok               |
|          40 | 22.80%   | 241.40%            | -40.70% |     0.42 |       60 | 39.43%     | ok               |
|          50 | 16.73%   | 241.40%            | -35.84% |     0.36 |       62 | 33.28%     | ok               |

## BA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 27.46%   | 8.40%              | -13.34% |     0.7  |       42 | 31.61%     | ok               |
|          35 | 27.25%   | 8.40%              | -23.77% |     0.55 |       74 | 45.26%     | ok               |
|          40 | 15.06%   | 8.40%              | -23.87% |     0.38 |       50 | 39.10%     | ok               |
|          25 | 8.09%    | 8.40%              | -32.48% |     0.26 |       72 | 53.41%     | ok               |
|          30 | 4.96%    | 8.40%              | -30.56% |     0.21 |       69 | 49.92%     | ok               |

## BAC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -9.46%   | 68.11%             | -21.48% |    -0.15 |       80 | 51.58%     | ok               |
|          45 | -7.18%   | 68.11%             | -22.29% |    -0.17 |       62 | 35.27%     | ok               |
|          50 | -8.69%   | 68.11%             | -20.82% |    -0.24 |       60 | 32.11%     | ok               |
|          35 | -10.55%  | 68.11%             | -29.13% |    -0.25 |       70 | 43.09%     | ok               |
|          15 | -14.56%  | 68.11%             | -23.70% |    -0.27 |       80 | 56.57%     | ok               |

## BCH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 13.24%   | -59.26%            | -45.63% |     0.36 |       69 | 54.02%     | ok               |
|          15 | 0.29%    | -59.26%            | -48.75% |     0.23 |       78 | 58.62%     | ok               |
|          30 | -0.30%   | -59.26%            | -53.87% |     0.21 |       76 | 47.70%     | ok               |
|          25 | -1.01%   | -59.26%            | -51.09% |     0.21 |       70 | 49.81%     | ok               |
|          40 | -20.74%  | -59.26%            | -60.69% |    -0.08 |       67 | 40.23%     | ok               |

## BITO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 21.10%   | -57.83%            | -32.29% |     0.41 |       54 | 25.96%     | ok               |
|          30 | 6.93%    | -57.83%            | -42.82% |     0.26 |       78 | 40.60%     | ok               |
|          15 | 0.40%    | -57.83%            | -48.29% |     0.21 |       87 | 49.58%     | ok               |
|          45 | 1.00%    | -57.83%            | -43.53% |     0.17 |       58 | 28.95%     | ok               |
|          25 | -1.53%   | -57.83%            | -41.73% |     0.17 |       82 | 43.59%     | ok               |

## BLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -1.96%   | 33.38%             | -15.13% |     0.01 |       82 | 38.94%     | ok               |
|          40 | -3.77%   | 33.38%             | -17.32% |    -0.06 |       72 | 34.61%     | ok               |
|          20 | -5.54%   | 33.38%             | -18.79% |    -0.08 |       79 | 47.09%     | ok               |
|          30 | -8.18%   | 33.38%             | -21.68% |    -0.18 |       77 | 42.76%     | ok               |
|          25 | -9.10%   | 33.38%             | -20.72% |    -0.2  |       77 | 45.09%     | ok               |

## BND Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.17%   | 0.88%              | -9.05%  |    -0.9  |       63 | 38.10%     | ok               |
|          25 | -6.87%   | 0.88%              | -10.14% |    -1.05 |       67 | 36.11%     | ok               |
|          30 | -7.32%   | 0.88%              | -9.89%  |    -1.18 |       65 | 32.28%     | ok               |
|          15 | -8.39%   | 0.88%              | -10.58% |    -1.21 |       73 | 40.93%     | ok               |
|          45 | -7.56%   | 0.88%              | -9.57%  |    -1.47 |       50 | 21.96%     | ok               |

## BONK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 169.29%  | -86.11%            | -35.57% |     1.24 |       44 | 22.03%     | ok               |
|          25 | 155.05%  | -86.11%            | -47.99% |     1    |       65 | 48.28%     | ok               |
|          20 | 140.65%  | -86.11%            | -55.43% |     0.95 |       66 | 52.87%     | ok               |
|          15 | 146.15%  | -86.11%            | -63.45% |     0.94 |       69 | 57.85%     | ok               |
|          45 | 88.02%   | -86.11%            | -42.36% |     0.85 |       56 | 26.44%     | ok               |

## BTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 51.83%   | -38.20%            | -14.50% |     0.95 |       44 | 34.10%     | ok               |
|          45 | 41.09%   | -38.20%            | -15.18% |     0.81 |       44 | 30.65%     | ok               |
|          35 | 36.01%   | -38.20%            | -22.12% |     0.7  |       68 | 41.00%     | ok               |
|          30 | 17.30%   | -38.20%            | -21.75% |     0.41 |       70 | 47.51%     | ok               |
|          50 | 14.18%   | -38.20%            | -16.15% |     0.4  |       42 | 25.29%     | ok               |

## C Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -6.42%   | 166.55%            | -22.28% |    -0.11 |       66 | 35.61%     | ok               |
|          45 | -13.39%  | 166.55%            | -28.12% |    -0.29 |       78 | 39.60%     | ok               |
|          25 | -20.66%  | 166.55%            | -34.18% |    -0.35 |       73 | 52.58%     | ok               |
|          15 | -22.68%  | 166.55%            | -35.02% |    -0.37 |       74 | 59.23%     | ok               |
|          20 | -23.32%  | 166.55%            | -35.56% |    -0.41 |       81 | 55.57%     | ok               |

## CAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 34.32%   | 229.23%            | -21.02% |     0.62 |       70 | 56.74%     | ok               |
|          25 | 34.44%   | 229.23%            | -26.37% |     0.62 |       66 | 59.57%     | ok               |
|          20 | 31.72%   | 229.23%            | -25.65% |     0.58 |       76 | 62.90%     | ok               |
|          45 | 22.72%   | 229.23%            | -28.85% |     0.49 |       56 | 45.59%     | ok               |
|          15 | 21.50%   | 229.23%            | -30.60% |     0.44 |       69 | 68.89%     | ok               |

## CL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 15.52%   | 8.03%              | -12.98% |     0.64 |       42 | 31.95%     | ok               |
|          30 | 15.02%   | 8.03%              | -14.32% |     0.53 |       60 | 47.92%     | ok               |
|          45 | 10.24%   | 8.03%              | -13.51% |     0.44 |       46 | 34.94%     | ok               |
|          35 | 9.54%    | 8.03%              | -13.83% |     0.37 |       62 | 44.26%     | ok               |
|          40 | 6.37%    | 8.03%              | -12.70% |     0.29 |       56 | 38.94%     | ok               |

## CMCSA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -34.39%  | -48.26%            | -49.03% |    -0.75 |       87 | 58.74%     | ok               |
|          30 | -38.75%  | -48.26%            | -40.02% |    -1    |       82 | 44.26%     | ok               |
|          25 | -44.04%  | -48.26%            | -45.20% |    -1.17 |       89 | 49.58%     | ok               |
|          20 | -45.65%  | -48.26%            | -47.23% |    -1.2  |       93 | 54.74%     | ok               |
|          50 | -33.03%  | -48.26%            | -33.68% |    -1.28 |       50 | 16.64%     | ok               |

## COMP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -3.83%   | -80.19%            | -38.71% |     0.15 |       46 | 20.69%     | ok               |
|          25 | -37.88%  | -80.19%            | -60.58% |    -0.19 |       87 | 50.00%     | ok               |
|          30 | -36.73%  | -80.19%            | -58.43% |    -0.21 |       89 | 45.02%     | ok               |
|          15 | -46.13%  | -80.19%            | -65.55% |    -0.28 |      101 | 61.49%     | ok               |
|          40 | -41.16%  | -80.19%            | -47.52% |    -0.37 |       74 | 33.14%     | ok               |

## COP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -9.77%   | -4.00%             | -34.21% |    -0.15 |       48 | 27.29%     | ok               |
|          45 | -15.67%  | -4.00%             | -40.57% |    -0.3  |       58 | 30.12%     | ok               |
|          35 | -23.70%  | -4.00%             | -43.58% |    -0.45 |       75 | 37.10%     | ok               |
|          30 | -24.21%  | -4.00%             | -43.77% |    -0.45 |       73 | 40.27%     | ok               |
|          40 | -26.23%  | -4.00%             | -46.34% |    -0.57 |       68 | 32.78%     | ok               |

## COST Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 18.52%   | 38.52%             | -24.32% |     0.55 |       64 | 52.75%     | ok               |
|          25 | 17.45%   | 38.52%             | -24.73% |     0.53 |       61 | 50.08%     | ok               |
|          35 | 10.69%   | 38.52%             | -26.58% |     0.38 |       54 | 43.59%     | ok               |
|          30 | 5.63%    | 38.52%             | -29.73% |     0.23 |       60 | 46.59%     | ok               |
|          40 | 3.90%    | 38.52%             | -28.41% |     0.19 |       56 | 40.60%     | ok               |

## CRM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -30.33%  | -45.78%            | -38.20% |    -0.44 |       90 | 55.24%     | ok               |
|          35 | -24.86%  | -45.78%            | -36.72% |    -0.47 |       62 | 38.94%     | ok               |
|          40 | -30.31%  | -45.78%            | -41.30% |    -0.68 |       68 | 34.94%     | ok               |
|          30 | -35.46%  | -45.78%            | -41.46% |    -0.72 |       65 | 43.76%     | ok               |
|          20 | -40.61%  | -45.78%            | -42.88% |    -0.76 |       78 | 48.92%     | ok               |

## CRV-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 12.00%   | -79.77%            | -29.30% |     0.33 |       40 | 16.67%     | ok               |
|          35 | 9.80%    | -79.77%            | -37.78% |     0.32 |       66 | 29.89%     | ok               |
|          45 | 6.52%    | -79.77%            | -42.29% |     0.27 |       52 | 19.54%     | ok               |
|          40 | -0.48%   | -79.77%            | -38.86% |     0.2  |       56 | 25.67%     | ok               |
|          30 | -12.80%  | -79.77%            | -39.89% |     0.09 |       64 | 34.48%     | ok               |

## CSCO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 28.18%   | 129.27%            | -19.34% |     0.63 |       58 | 38.94%     | ok               |
|          45 | 26.53%   | 129.27%            | -19.34% |     0.59 |       51 | 41.43%     | ok               |
|          25 | 22.43%   | 129.27%            | -23.28% |     0.49 |       63 | 52.41%     | ok               |
|          35 | 21.85%   | 129.27%            | -23.68% |     0.49 |       51 | 47.92%     | ok               |
|          30 | 21.86%   | 129.27%            | -21.79% |     0.49 |       59 | 50.42%     | ok               |

## CVX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -13.07%  | 16.42%             | -26.07% |    -0.29 |       71 | 45.26%     | ok               |
|          25 | -13.44%  | 16.42%             | -25.65% |    -0.3  |       75 | 44.09%     | ok               |
|          45 | -12.87%  | 16.42%             | -28.32% |    -0.37 |       59 | 30.45%     | ok               |
|          30 | -15.07%  | 16.42%             | -26.75% |    -0.38 |       69 | 41.10%     | ok               |
|          35 | -14.82%  | 16.42%             | -27.83% |    -0.38 |       69 | 38.10%     | ok               |

## DASH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 110.90%  | -18.24%            | -31.38% |     0.88 |       42 | 17.24%     | ok               |
|          40 | 61.26%   | -18.24%            | -34.44% |     0.65 |       48 | 23.95%     | ok               |
|          45 | 52.31%   | -18.24%            | -39.58% |     0.61 |       46 | 19.54%     | ok               |
|          25 | -37.88%  | -18.24%            | -64.14% |     0.04 |       71 | 34.67%     | ok               |
|          35 | -37.69%  | -18.24%            | -63.23% |     0.03 |       71 | 28.35%     | ok               |

## DBC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -8.05%   | 22.20%             | -19.49% |    -0.3  |       44 | 20.80%     | ok               |
|          35 | -9.68%   | 22.20%             | -23.38% |    -0.31 |       60 | 31.61%     | ok               |
|          15 | -10.26%  | 22.20%             | -27.04% |    -0.32 |       69 | 37.44%     | ok               |
|          45 | -9.42%   | 22.20%             | -20.65% |    -0.33 |       56 | 24.13%     | ok               |
|          30 | -12.57%  | 22.20%             | -25.35% |    -0.43 |       58 | 32.78%     | ok               |

## DE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -5.92%   | 49.70%             | -28.94% |    -0.03 |       72 | 51.08%     | ok               |
|          30 | -6.80%   | 49.70%             | -25.24% |    -0.06 |       72 | 45.76%     | ok               |
|          25 | -8.25%   | 49.70%             | -26.67% |    -0.09 |       74 | 48.42%     | ok               |
|          50 | -9.68%   | 49.70%             | -24.57% |    -0.2  |       70 | 30.45%     | ok               |
|          15 | -14.19%  | 49.70%             | -27.41% |    -0.21 |       78 | 54.41%     | ok               |

## DIA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -0.36%   | 35.28%             | -13.15% |     0.02 |       60 | 43.76%     | ok               |
|          25 | -0.90%   | 35.28%             | -11.28% |    -0.01 |       60 | 47.09%     | ok               |
|          30 | -2.42%   | 35.28%             | -12.94% |    -0.09 |       60 | 45.92%     | ok               |
|          20 | -4.29%   | 35.28%             | -13.85% |    -0.18 |       64 | 49.42%     | ok               |
|          40 | -4.42%   | 35.28%             | -15.06% |    -0.22 |       66 | 40.93%     | ok               |

## DIS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 35.23%   | 8.95%              | -14.24% |     0.87 |       50 | 30.62%     | ok               |
|          45 | 6.87%    | 8.95%              | -16.54% |     0.24 |       51 | 34.11%     | ok               |
|          40 | 5.90%    | 8.95%              | -22.77% |     0.22 |       63 | 39.27%     | ok               |
|          35 | -0.34%   | 8.95%              | -25.09% |     0.1  |       73 | 45.26%     | ok               |
|          15 | -3.10%   | 8.95%              | -29.22% |     0.06 |       87 | 58.90%     | ok               |

## DOGE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 22.30%   | -79.79%            | -57.89% |     0.46 |       79 | 65.13%     | ok               |
|          20 | 4.42%    | -79.79%            | -55.83% |     0.31 |       82 | 60.34%     | ok               |
|          25 | 0.09%    | -79.79%            | -53.72% |     0.27 |       72 | 54.98%     | ok               |
|          30 | -16.53%  | -79.79%            | -60.95% |     0.09 |       75 | 49.81%     | ok               |
|          35 | -45.34%  | -79.79%            | -63.16% |    -0.38 |       72 | 43.10%     | ok               |

## DOT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -19.39%  | -87.16%            | -45.14% |    -0.11 |       56 | 26.05%     | ok               |
|          45 | -27.79%  | -87.16%            | -52.48% |    -0.23 |       50 | 30.65%     | ok               |
|          30 | -46.67%  | -87.16%            | -60.68% |    -0.34 |       90 | 47.70%     | ok               |
|          35 | -45.76%  | -87.16%            | -62.33% |    -0.35 |       76 | 40.80%     | ok               |
|          40 | -37.15%  | -87.16%            | -53.44% |    -0.36 |       54 | 33.91%     | ok               |

## DXY-INDEX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -1.45%   | -0.23%             | -6.02%  |    -0.22 |       40 | 28.85%     | ok               |
|          15 | -5.84%   | -0.23%             | -11.37% |    -0.53 |       88 | 75.92%     | ok               |
|          40 | -4.33%   | -0.23%             | -7.30%  |    -0.54 |       70 | 48.59%     | ok               |
|          30 | -5.29%   | -0.23%             | -9.83%  |    -0.6  |       72 | 59.65%     | ok               |
|          35 | -5.17%   | -0.23%             | -9.97%  |    -0.62 |       73 | 54.88%     | ok               |

## EEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -2.91%   | 82.03%             | -15.88% |    -0.04 |       50 | 36.11%     | ok               |
|          45 | -4.62%   | 82.03%             | -17.36% |    -0.11 |       52 | 37.60%     | ok               |
|          40 | -4.96%   | 82.03%             | -19.52% |    -0.11 |       64 | 39.77%     | ok               |
|          35 | -5.62%   | 82.03%             | -23.88% |    -0.12 |       66 | 41.76%     | ok               |
|          30 | -9.40%   | 82.03%             | -25.67% |    -0.25 |       64 | 43.43%     | ok               |

## EFA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -1.25%   | 39.12%             | -10.80% |     0.02 |       58 | 52.08%     | ok               |
|          20 | -8.10%   | 39.12%             | -12.49% |    -0.27 |       65 | 49.08%     | ok               |
|          30 | -8.17%   | 39.12%             | -13.72% |    -0.29 |       60 | 44.09%     | ok               |
|          40 | -9.56%   | 39.12%             | -15.58% |    -0.39 |       64 | 40.27%     | ok               |
|          50 | -9.07%   | 39.12%             | -17.56% |    -0.4  |       54 | 36.27%     | ok               |

## EOG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -15.90%  | 12.50%             | -38.89% |    -0.35 |       52 | 32.61%     | ok               |
|          50 | -17.13%  | 12.50%             | -37.65% |    -0.41 |       56 | 29.78%     | ok               |
|          40 | -20.88%  | 12.50%             | -40.83% |    -0.49 |       60 | 35.94%     | ok               |
|          35 | -22.50%  | 12.50%             | -44.05% |    -0.52 |       75 | 40.77%     | ok               |
|          30 | -24.73%  | 12.50%             | -48.13% |    -0.54 |       77 | 46.09%     | ok               |

## ETC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -7.93%   | -73.79%            | -27.89% |    -0.02 |       28 | 17.05%     | ok               |
|          35 | -15.03%  | -73.79%            | -42.62% |    -0.11 |       44 | 27.01%     | ok               |
|          45 | -16.07%  | -73.79%            | -35.44% |    -0.17 |       26 | 18.97%     | ok               |
|          40 | -21.04%  | -73.79%            | -40.48% |    -0.26 |       42 | 22.80%     | ok               |
|          30 | -35.69%  | -73.79%            | -48.16% |    -0.51 |       64 | 31.23%     | ok               |

## ETH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 164.78%  | -49.91%            | -30.11% |     1.31 |       58 | 44.64%     | ok               |
|          30 | 164.32%  | -49.91%            | -32.89% |     1.26 |       62 | 52.87%     | ok               |
|          40 | 62.72%   | -49.91%            | -33.11% |     0.8  |       56 | 37.36%     | ok               |
|          45 | 43.31%   | -49.91%            | -34.50% |     0.65 |       52 | 33.52%     | ok               |
|          25 | 43.93%   | -49.91%            | -40.90% |     0.61 |       67 | 58.81%     | ok               |

## EWJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -16.66%  | 47.21%             | -30.73% |    -0.52 |       64 | 40.77%     | ok               |
|          20 | -18.07%  | 47.21%             | -31.32% |    -0.56 |       60 | 42.76%     | ok               |
|          25 | -20.43%  | 47.21%             | -31.18% |    -0.66 |       60 | 41.76%     | ok               |
|          35 | -20.65%  | 47.21%             | -32.54% |    -0.69 |       70 | 39.10%     | ok               |
|          15 | -23.49%  | 47.21%             | -32.24% |    -0.72 |       74 | 45.92%     | ok               |

## FCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -7.45%   | 73.48%             | -26.57% |     0    |       56 | 29.62%     | ok               |
|          45 | -12.11%  | 73.48%             | -33.82% |    -0.06 |       56 | 33.94%     | ok               |
|          40 | -23.41%  | 73.48%             | -42.89% |    -0.26 |       66 | 39.10%     | ok               |
|          30 | -31.93%  | 73.48%             | -46.84% |    -0.39 |       69 | 45.92%     | ok               |
|          35 | -35.67%  | 73.48%             | -50.12% |    -0.49 |       73 | 43.93%     | ok               |

## FET-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 35.70%   | -86.80%            | -57.84% |     0.55 |       90 | 49.81%     | ok               |
|          15 | 1.48%    | -86.80%            | -59.58% |     0.33 |       86 | 52.87%     | ok               |
|          25 | -11.22%  | -86.80%            | -58.42% |     0.2  |       93 | 43.49%     | ok               |
|          30 | -16.23%  | -86.80%            | -54.02% |     0.14 |       83 | 39.66%     | ok               |
|          45 | -25.66%  | -86.80%            | -48.61% |    -0.15 |       56 | 18.77%     | ok               |

## FIL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -6.35%   | -85.97%            | -39.40% |     0.09 |       48 | 23.37%     | ok               |
|          35 | -30.36%  | -85.97%            | -45.88% |    -0.27 |       58 | 27.59%     | ok               |
|          45 | -27.58%  | -85.97%            | -43.98% |    -0.29 |       44 | 17.62%     | ok               |
|          30 | -33.66%  | -85.97%            | -49.05% |    -0.29 |       70 | 33.14%     | ok               |
|          50 | -26.52%  | -85.97%            | -44.97% |    -0.32 |       38 | 13.03%     | ok               |

## FXI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -4.42%   | 47.35%             | -22.57% |    -0.02 |       46 | 29.45%     | ok               |
|          30 | -4.97%   | 47.35%             | -23.91% |    -0.04 |       46 | 28.29%     | ok               |
|          15 | -7.25%   | 47.35%             | -21.68% |    -0.09 |       54 | 32.78%     | ok               |
|          20 | -8.27%   | 47.35%             | -24.53% |    -0.12 |       52 | 30.62%     | ok               |
|          45 | -8.60%   | 47.35%             | -26.75% |    -0.16 |       44 | 22.80%     | ok               |

## GDX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 12.93%   | 193.94%            | -31.87% |     0.33 |       62 | 42.76%     | ok               |
|          20 | 5.34%    | 193.94%            | -35.59% |     0.22 |       75 | 52.91%     | ok               |
|          35 | 4.67%    | 193.94%            | -32.37% |     0.2  |       68 | 45.09%     | ok               |
|          30 | -0.72%   | 193.94%            | -34.99% |     0.12 |       62 | 48.09%     | ok               |
|          45 | -1.99%   | 193.94%            | -32.07% |     0.08 |       58 | 39.43%     | ok               |

## GDXJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -19.15%  | 214.15%            | -45.05% |    -0.11 |       70 | 53.24%     | ok               |
|          50 | -16.59%  | 214.15%            | -42.44% |    -0.15 |       56 | 37.44%     | ok               |
|          30 | -27.99%  | 214.15%            | -44.93% |    -0.32 |       68 | 45.92%     | ok               |
|          45 | -27.77%  | 214.15%            | -42.73% |    -0.36 |       60 | 39.77%     | ok               |
|          40 | -29.17%  | 214.15%            | -44.27% |    -0.38 |       64 | 41.60%     | ok               |

## GE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 37.24%   | 241.58%            | -22.29% |     0.71 |       66 | 39.10%     | ok               |
|          45 | 26.88%   | 241.58%            | -25.68% |     0.56 |       74 | 41.93%     | ok               |
|          20 | 25.94%   | 241.58%            | -26.63% |     0.51 |       69 | 55.74%     | ok               |
|          35 | 20.29%   | 241.58%            | -27.11% |     0.44 |       80 | 47.25%     | ok               |
|          40 | 19.38%   | 241.58%            | -26.97% |     0.44 |       76 | 43.43%     | ok               |

## GLD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 28.71%   | 107.00%            | -14.61% |     0.71 |       46 | 45.92%     | ok               |
|          20 | 26.80%   | 107.00%            | -14.61% |     0.67 |       48 | 47.25%     | ok               |
|          30 | 22.59%   | 107.00%            | -16.63% |     0.6  |       48 | 44.76%     | ok               |
|          15 | 19.03%   | 107.00%            | -17.54% |     0.5  |       50 | 51.41%     | ok               |
|          35 | 16.60%   | 107.00%            | -17.29% |     0.47 |       50 | 44.09%     | ok               |

## GOOGL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 72.53%   | 141.82%            | -19.76% |     1.08 |       59 | 56.24%     | ok               |
|          30 | 68.66%   | 141.82%            | -20.41% |     1.06 |       63 | 53.91%     | ok               |
|          15 | 62.81%   | 141.82%            | -13.59% |     0.94 |       71 | 63.89%     | ok               |
|          35 | 53.81%   | 141.82%            | -22.85% |     0.94 |       69 | 48.75%     | ok               |
|          20 | 59.50%   | 141.82%            | -20.57% |     0.94 |       70 | 58.57%     | ok               |

## GRT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 46.24%   | -91.53%            | -30.00% |     0.71 |       40 | 21.07%     | ok               |
|          45 | 13.62%   | -91.53%            | -48.76% |     0.35 |       48 | 26.25%     | ok               |
|          20 | 10.02%   | -91.53%            | -46.47% |     0.34 |       83 | 55.75%     | ok               |
|          15 | 8.08%    | -91.53%            | -49.67% |     0.33 |       75 | 60.92%     | ok               |
|          35 | 9.43%    | -91.53%            | -49.87% |     0.31 |       60 | 35.44%     | ok               |

## GS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 30.29%   | 190.26%            | -20.56% |     0.61 |       74 | 60.23%     | ok               |
|          20 | 12.52%   | 190.26%            | -23.19% |     0.34 |       74 | 56.24%     | ok               |
|          25 | 6.82%    | 190.26%            | -23.32% |     0.24 |       74 | 53.74%     | ok               |
|          40 | 1.94%    | 190.26%            | -17.88% |     0.13 |       72 | 44.76%     | ok               |
|          30 | 0.54%    | 190.26%            | -22.13% |     0.11 |       76 | 51.41%     | ok               |

## HD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -2.85%   | -5.92%             | -17.69% |     0    |       71 | 43.76%     | ok               |
|          25 | -3.61%   | -5.92%             | -18.51% |    -0.02 |       70 | 45.76%     | ok               |
|          40 | -11.42%  | -5.92%             | -19.63% |    -0.31 |       80 | 33.78%     | ok               |
|          35 | -13.72%  | -5.92%             | -22.98% |    -0.34 |       78 | 39.93%     | ok               |
|          45 | -12.22%  | -5.92%             | -21.41% |    -0.36 |       60 | 28.45%     | ok               |

## HON Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -17.61%  | 20.41%             | -22.04% |    -0.51 |       76 | 37.27%     | ok               |
|          50 | -17.09%  | 20.41%             | -23.31% |    -0.53 |       74 | 32.11%     | ok               |
|          40 | -25.72%  | 20.41%             | -26.73% |    -0.74 |       78 | 41.60%     | ok               |
|          35 | -27.43%  | 20.41%             | -28.41% |    -0.77 |       95 | 48.09%     | ok               |
|          30 | -28.76%  | 20.41%             | -30.75% |    -0.78 |       97 | 53.24%     | ok               |

## HYG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -7.92%   | 3.07%              | -7.92%  |    -0.96 |       70 | 29.45%     | ok               |
|          15 | -9.71%   | 3.07%              | -10.06% |    -1.05 |       88 | 41.43%     | ok               |
|          20 | -9.69%   | 3.07%              | -10.29% |    -1.08 |       86 | 39.10%     | ok               |
|          45 | -8.60%   | 3.07%              | -8.60%  |    -1.08 |       66 | 26.29%     | ok               |
|          30 | -9.52%   | 3.07%              | -9.59%  |    -1.11 |       81 | 34.28%     | ok               |

## IBIT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 64.95%   | -6.29%             | -19.20% |     1.08 |       38 | 38.59%     | ok               |
|          50 | 52.30%   | -6.29%             | -17.37% |     1.07 |       20 | 23.06%     | ok               |
|          45 | 43.83%   | -6.29%             | -17.37% |     0.92 |       22 | 23.79%     | ok               |
|          40 | 42.41%   | -6.29%             | -17.78% |     0.89 |       24 | 25.24%     | ok               |
|          30 | 35.91%   | -6.29%             | -18.95% |     0.76 |       32 | 30.83%     | ok               |

## IBM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 21.85%   | 32.91%             | -28.20% |     0.47 |       89 | 62.40%     | ok               |
|          30 | 11.96%   | 32.91%             | -25.31% |     0.33 |       72 | 50.42%     | ok               |
|          35 | 9.71%    | 32.91%             | -25.15% |     0.29 |       68 | 46.09%     | ok               |
|          45 | 7.34%    | 32.91%             | -18.33% |     0.25 |       54 | 36.61%     | ok               |
|          40 | 4.15%    | 32.91%             | -24.66% |     0.18 |       64 | 40.60%     | ok               |

## ICP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 21.03%   | -79.90%            | -32.85% |     0.42 |       58 | 27.01%     | ok               |
|          35 | 9.43%    | -79.90%            | -45.97% |     0.32 |       68 | 32.38%     | ok               |
|          50 | 5.42%    | -79.90%            | -43.65% |     0.25 |       40 | 16.86%     | ok               |
|          30 | -1.35%   | -79.90%            | -55.67% |     0.25 |       83 | 38.70%     | ok               |
|          45 | -8.28%   | -79.90%            | -40.57% |     0.09 |       58 | 21.07%     | ok               |

## IEF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.92%   | -0.63%             | -9.79%  |    -0.82 |       70 | 42.26%     | ok               |
|          15 | -7.48%   | -0.63%             | -10.52% |    -0.88 |       69 | 43.76%     | ok               |
|          40 | -8.39%   | -0.63%             | -9.67%  |    -1.31 |       60 | 24.79%     | ok               |
|          45 | -8.07%   | -0.63%             | -9.73%  |    -1.33 |       50 | 22.80%     | ok               |
|          25 | -10.50%  | -0.63%             | -11.19% |    -1.34 |       76 | 39.43%     | ok               |

## IEMG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.10%   | 74.86%             | -13.91% |     0.05 |       52 | 34.44%     | ok               |
|          35 | -0.32%   | 74.86%             | -22.13% |     0.05 |       63 | 42.60%     | ok               |
|          45 | -0.91%   | 74.86%             | -14.92% |     0.02 |       48 | 36.94%     | ok               |
|          40 | -2.44%   | 74.86%             | -18.43% |    -0.03 |       60 | 39.93%     | ok               |
|          25 | -4.72%   | 74.86%             | -25.58% |    -0.09 |       59 | 45.42%     | ok               |

## INJ-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -20.16%  | -79.73%            | -61.19% |    -0.01 |       60 | 32.38%     | ok               |
|          45 | -16.04%  | -79.73%            | -56.91% |    -0.02 |       44 | 22.22%     | ok               |
|          50 | -25.16%  | -79.73%            | -52.76% |    -0.19 |       48 | 19.16%     | ok               |
|          40 | -30.93%  | -79.73%            | -59.56% |    -0.21 |       50 | 28.35%     | ok               |
|          20 | -56.26%  | -79.73%            | -81.53% |    -0.46 |       82 | 47.13%     | ok               |

## INTC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 76.11%   | 206.96%            | -49.32% |     0.74 |       60 | 34.28%     | ok               |
|          15 | 82.95%   | 206.96%            | -53.65% |     0.74 |       84 | 61.23%     | ok               |
|          25 | 75.50%   | 206.96%            | -56.41% |     0.72 |       75 | 51.58%     | ok               |
|          40 | 70.33%   | 206.96%            | -55.86% |     0.7  |       68 | 38.60%     | ok               |
|          20 | 72.70%   | 206.96%            | -52.47% |     0.7  |       82 | 56.57%     | ok               |

## INTU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 2.92%    | -58.37%            | -42.82% |     0.17 |       71 | 29.28%     | ok               |
|          45 | -0.60%   | -58.37%            | -44.66% |     0.11 |       69 | 33.44%     | ok               |
|          40 | -8.04%   | -58.37%            | -48.32% |    -0.03 |       69 | 36.11%     | ok               |
|          25 | -9.35%   | -58.37%            | -42.24% |    -0.03 |       64 | 45.42%     | ok               |
|          15 | -10.42%  | -58.37%            | -46.90% |    -0.04 |       79 | 50.92%     | ok               |

## ITA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 3.54%    | 95.83%             | -21.48% |     0.18 |       76 | 37.27%     | ok               |
|          15 | -0.57%   | 95.83%             | -28.17% |     0.07 |       86 | 58.90%     | ok               |
|          30 | -0.63%   | 95.83%             | -23.75% |     0.06 |       74 | 47.25%     | ok               |
|          35 | -3.19%   | 95.83%             | -23.16% |    -0.03 |       78 | 45.42%     | ok               |
|          40 | -4.31%   | 95.83%             | -20.58% |    -0.07 |       80 | 41.93%     | ok               |

## IWM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 9.03%    | 50.83%             | -12.83% |     0.37 |       50 | 36.44%     | ok               |
|          25 | 9.14%    | 50.83%             | -14.87% |     0.37 |       52 | 37.60%     | ok               |
|          40 | 6.82%    | 50.83%             | -14.38% |     0.32 |       44 | 31.78%     | ok               |
|          35 | 6.57%    | 50.83%             | -14.41% |     0.3  |       50 | 34.11%     | ok               |
|          20 | 4.84%    | 50.83%             | -15.39% |     0.23 |       62 | 38.60%     | ok               |

## JNJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 21.36%   | 43.19%             | -10.57% |     0.9  |       56 | 37.10%     | ok               |
|          15 | 17.03%   | 43.19%             | -18.02% |     0.59 |       66 | 57.57%     | ok               |
|          45 | 12.26%   | 43.19%             | -13.35% |     0.53 |       58 | 42.26%     | ok               |
|          20 | 12.61%   | 43.19%             | -17.61% |     0.48 |       72 | 54.08%     | ok               |
|          40 | 9.81%    | 43.19%             | -14.77% |     0.42 |       64 | 46.42%     | ok               |

## JPM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 18.58%   | 88.77%             | -15.90% |     0.63 |       52 | 40.27%     | ok               |
|          45 | 7.31%    | 88.77%             | -21.91% |     0.28 |       54 | 43.26%     | ok               |
|          40 | -6.86%   | 88.77%             | -28.47% |    -0.13 |       66 | 45.76%     | ok               |
|          20 | -13.59%  | 88.77%             | -33.59% |    -0.22 |       86 | 57.07%     | ok               |
|          35 | -12.06%  | 88.77%             | -27.43% |    -0.27 |       72 | 49.42%     | ok               |

## KO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 27.92%   | 33.72%             | -8.07%  |     1    |       51 | 37.94%     | ok               |
|          35 | 24.00%   | 33.72%             | -8.07%  |     0.89 |       54 | 36.61%     | ok               |
|          40 | 21.41%   | 33.72%             | -9.28%  |     0.86 |       56 | 33.44%     | ok               |
|          25 | 22.64%   | 33.72%             | -9.37%  |     0.83 |       57 | 40.60%     | ok               |
|          50 | 14.81%   | 33.72%             | -11.40% |     0.68 |       36 | 26.79%     | ok               |

## LDO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 24.99%   | -86.22%            | -46.95% |     0.48 |       81 | 51.92%     | ok               |
|          20 | 13.39%   | -86.22%            | -44.97% |     0.4  |       85 | 47.32%     | ok               |
|          50 | 13.59%   | -86.22%            | -48.77% |     0.35 |       46 | 16.67%     | ok               |
|          30 | 1.95%    | -86.22%            | -60.93% |     0.29 |       74 | 37.93%     | ok               |
|          35 | -1.80%   | -86.22%            | -63.16% |     0.23 |       74 | 30.84%     | ok               |

## LIN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 4.87%    | 26.76%             | -23.70% |     0.22 |       63 | 49.75%     | ok               |
|          25 | 3.57%    | 26.76%             | -22.01% |     0.18 |       65 | 41.76%     | ok               |
|          20 | 1.35%    | 26.76%             | -23.00% |     0.11 |       64 | 44.93%     | ok               |
|          35 | -0.17%   | 26.76%             | -21.18% |     0.05 |       64 | 32.45%     | ok               |
|          30 | -0.80%   | 26.76%             | -21.53% |     0.03 |       68 | 38.94%     | ok               |

## LINK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -13.55%  | -68.35%            | -50.48% |     0.1  |       70 | 41.57%     | ok               |
|          45 | -16.95%  | -68.35%            | -38.56% |    -0    |       50 | 26.25%     | ok               |
|          50 | -16.55%  | -68.35%            | -36.98% |    -0.02 |       40 | 20.88%     | ok               |
|          35 | -27.53%  | -68.35%            | -49.56% |    -0.1  |       60 | 36.40%     | ok               |
|          40 | -31.51%  | -68.35%            | -50.91% |    -0.19 |       56 | 30.65%     | ok               |

## LLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 26.10%   | 71.85%             | -38.23% |     0.55 |       42 | 39.10%     | ok               |
|          45 | 12.67%   | 71.85%             | -42.66% |     0.33 |       50 | 42.43%     | ok               |
|          15 | 6.25%    | 71.85%             | -48.12% |     0.23 |       63 | 61.90%     | ok               |
|          40 | -4.19%   | 71.85%             | -46.23% |     0.05 |       62 | 44.93%     | ok               |
|          20 | -10.86%  | 71.85%             | -51.34% |    -0.04 |       72 | 56.91%     | ok               |

## LRCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 11.23%   | 363.67%            | -60.45% |     0.31 |       83 | 55.57%     | ok               |
|          50 | 4.82%    | 363.67%            | -50.39% |     0.22 |       80 | 37.44%     | ok               |
|          40 | 1.68%    | 363.67%            | -56.86% |     0.19 |       72 | 43.26%     | ok               |
|          35 | -4.93%   | 363.67%            | -61.76% |     0.11 |       80 | 45.26%     | ok               |
|          20 | -7.68%   | 363.67%            | -67.64% |     0.08 |       87 | 51.25%     | ok               |

## LTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -12.22%  | -67.02%            | -44.78% |    -0    |       56 | 31.80%     | ok               |
|          35 | -22.47%  | -67.02%            | -54.86% |    -0.13 |       66 | 42.91%     | ok               |
|          30 | -34.00%  | -67.02%            | -53.76% |    -0.29 |       66 | 48.47%     | ok               |
|          40 | -31.40%  | -67.02%            | -56.10% |    -0.3  |       58 | 38.12%     | ok               |
|          25 | -36.79%  | -67.02%            | -54.26% |    -0.33 |       74 | 50.96%     | ok               |

## MCD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 2.49%    | -4.67%             | -9.22%  |     0.17 |       42 | 20.47%     | ok               |
|          30 | -2.55%   | -4.67%             | -18.81% |    -0.05 |       75 | 38.10%     | ok               |
|          25 | -3.59%   | -4.67%             | -20.47% |    -0.09 |       75 | 40.77%     | ok               |
|          35 | -7.68%   | -4.67%             | -15.45% |    -0.29 |       67 | 34.44%     | ok               |
|          40 | -7.95%   | -4.67%             | -16.86% |    -0.33 |       71 | 28.79%     | ok               |

## META Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 8.98%    | 46.45%             | -31.03% |     0.27 |       66 | 40.10%     | ok               |
|          40 | -3.00%   | 46.45%             | -35.11% |     0.08 |       66 | 43.09%     | ok               |
|          50 | -7.65%   | 46.45%             | -34.00% |    -0.02 |       70 | 36.27%     | ok               |
|          25 | -12.57%  | 46.45%             | -39.84% |    -0.07 |       67 | 53.74%     | ok               |
|          35 | -14.13%  | 46.45%             | -34.87% |    -0.11 |       77 | 47.92%     | ok               |

## MPC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 14.51%   | 51.33%             | -23.96% |     0.37 |       52 | 38.60%     | ok               |
|          45 | 7.25%    | 51.33%             | -25.09% |     0.24 |       58 | 42.26%     | ok               |
|          40 | 5.62%    | 51.33%             | -25.70% |     0.22 |       60 | 44.59%     | ok               |
|          35 | 2.36%    | 51.33%             | -35.90% |     0.16 |       68 | 47.09%     | ok               |
|          30 | -13.74%  | 51.33%             | -44.76% |    -0.14 |       71 | 49.92%     | ok               |

## MRK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -17.55%  | -5.75%             | -30.12% |    -0.3  |       87 | 57.57%     | ok               |
|          25 | -17.15%  | -5.75%             | -31.07% |    -0.32 |       72 | 49.58%     | ok               |
|          20 | -21.21%  | -5.75%             | -29.59% |    -0.42 |       77 | 52.91%     | ok               |
|          45 | -20.09%  | -5.75%             | -26.02% |    -0.5  |       57 | 35.77%     | ok               |
|          50 | -19.20%  | -5.75%             | -25.69% |    -0.51 |       58 | 32.61%     | ok               |

## MS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -0.08%   | 154.38%            | -19.99% |     0.08 |       70 | 40.10%     | ok               |
|          35 | -7.10%   | 154.38%            | -25.26% |    -0.1  |       76 | 44.76%     | ok               |
|          15 | -11.81%  | 154.38%            | -24.00% |    -0.17 |       80 | 56.91%     | ok               |
|          20 | -11.91%  | 154.38%            | -25.68% |    -0.2  |       84 | 53.08%     | ok               |
|          30 | -13.59%  | 154.38%            | -27.79% |    -0.27 |       81 | 48.42%     | ok               |

## MSFT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -18.94%  | -6.07%             | -26.27% |    -0.54 |       66 | 35.27%     | ok               |
|          50 | -22.59%  | -6.07%             | -28.83% |    -0.69 |       64 | 30.62%     | ok               |
|          35 | -30.57%  | -6.07%             | -33.68% |    -0.82 |       75 | 43.59%     | ok               |
|          25 | -33.95%  | -6.07%             | -37.59% |    -0.87 |       87 | 51.25%     | ok               |
|          40 | -31.39%  | -6.07%             | -34.46% |    -0.89 |       71 | 38.60%     | ok               |

## MU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 421.81%  | 1187.89%           | -61.96% |     1.55 |       48 | 68.05%     | ok               |
|          25 | 334.73%  | 1187.89%           | -67.90% |     1.46 |       49 | 61.73%     | ok               |
|          40 | 288.38%  | 1187.89%           | -64.30% |     1.4  |       56 | 55.07%     | ok               |
|          20 | 298.01%  | 1187.89%           | -67.25% |     1.37 |       55 | 63.89%     | ok               |
|          30 | 270.31%  | 1187.89%           | -68.76% |     1.34 |       51 | 59.90%     | ok               |

## NEAR-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 111.59%  | -62.11%            | -45.84% |     1.03 |       44 | 23.56%     | ok               |
|          50 | 77.92%   | -62.11%            | -51.20% |     0.87 |       40 | 18.58%     | ok               |
|          40 | 68.28%   | -62.11%            | -54.53% |     0.77 |       46 | 27.78%     | ok               |
|          35 | 39.72%   | -62.11%            | -58.86% |     0.58 |       70 | 33.14%     | ok               |
|          15 | 2.00%    | -62.11%            | -54.94% |     0.31 |       89 | 56.13%     | ok               |

## NEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 16.57%   | 203.39%            | -29.39% |     0.36 |       62 | 64.23%     | ok               |
|          20 | 5.60%    | 203.39%            | -30.47% |     0.24 |       74 | 59.73%     | ok               |
|          50 | -13.83%  | 203.39%            | -33.36% |    -0.07 |       60 | 41.43%     | ok               |
|          25 | -18.25%  | 203.39%            | -37.89% |    -0.09 |       72 | 57.24%     | ok               |
|          30 | -30.28%  | 203.39%            | -38.49% |    -0.31 |       78 | 54.91%     | ok               |

## NFLX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 53.48%   | 35.65%             | -11.94% |     1.12 |       46 | 47.25%     | ok               |
|          50 | 40.44%   | 35.65%             | -16.28% |     0.95 |       48 | 39.77%     | ok               |
|          35 | 45.59%   | 35.65%             | -18.30% |     0.94 |       60 | 50.75%     | ok               |
|          45 | 36.89%   | 35.65%             | -15.48% |     0.86 |       52 | 43.59%     | ok               |
|          25 | 35.29%   | 35.65%             | -21.09% |     0.75 |       60 | 57.24%     | ok               |

## NKE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -26.93%  | -56.01%            | -42.13% |    -0.38 |       75 | 37.27%     | ok               |
|          20 | -35.58%  | -56.01%            | -50.44% |    -0.46 |       95 | 52.75%     | ok               |
|          25 | -35.80%  | -56.01%            | -51.20% |    -0.47 |       91 | 48.92%     | ok               |
|          40 | -26.46%  | -56.01%            | -31.19% |    -0.5  |       63 | 30.12%     | ok               |
|          30 | -37.83%  | -56.01%            | -55.35% |    -0.53 |       91 | 43.76%     | ok               |

## NOW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 25.64%   | -38.24%            | -30.25% |     0.46 |       80 | 45.92%     | ok               |
|          20 | 26.20%   | -38.24%            | -26.36% |     0.46 |       79 | 51.91%     | ok               |
|          15 | 19.37%   | -38.24%            | -26.36% |     0.39 |       87 | 55.24%     | ok               |
|          35 | 17.53%   | -38.24%            | -29.30% |     0.38 |       81 | 40.60%     | ok               |
|          25 | 18.50%   | -38.24%            | -25.70% |     0.38 |       72 | 49.25%     | ok               |

## NVDA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -10.53%  | 121.77%            | -33.22% |     0.02 |       68 | 50.98%     | ok               |
|          30 | -12.21%  | 121.77%            | -35.26% |    -0.03 |       70 | 48.66%     | ok               |
|          20 | -16.47%  | 121.77%            | -40.59% |    -0.05 |       71 | 55.44%     | ok               |
|          50 | -19.49%  | 121.77%            | -40.84% |    -0.2  |       60 | 32.80%     | ok               |
|          35 | -22.50%  | 121.77%            | -41.25% |    -0.22 |       82 | 45.81%     | ok               |

## OP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 74.65%   | -94.77%            | -45.76% |     0.86 |       36 | 17.43%     | ok               |
|          50 | 66.86%   | -94.77%            | -36.11% |     0.86 |       34 | 12.45%     | ok               |
|          40 | 59.18%   | -94.77%            | -53.61% |     0.72 |       48 | 26.05%     | ok               |
|          35 | 32.48%   | -94.77%            | -58.33% |     0.52 |       56 | 29.12%     | ok               |
|          30 | 8.32%    | -94.77%            | -70.27% |     0.33 |       72 | 35.63%     | ok               |

## ORCL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 135.57%  | 60.76%             | -29.32% |     1.03 |       74 | 65.22%     | ok               |
|          25 | 76.72%   | 60.76%             | -27.76% |     0.76 |       75 | 57.74%     | ok               |
|          20 | 73.68%   | 60.76%             | -29.32% |     0.74 |       77 | 60.90%     | ok               |
|          35 | 51.51%   | 60.76%             | -31.95% |     0.62 |       68 | 49.42%     | ok               |
|          30 | 51.65%   | 60.76%             | -29.47% |     0.62 |       74 | 53.58%     | ok               |

## OXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 2.48%    | -11.27%            | -30.85% |     0.16 |       63 | 43.09%     | ok               |
|          35 | -0.66%   | -11.27%            | -30.50% |     0.1  |       68 | 38.60%     | ok               |
|          50 | -1.47%   | -11.27%            | -31.07% |     0.07 |       38 | 27.95%     | ok               |
|          40 | -3.09%   | -11.27%            | -32.21% |     0.05 |       56 | 34.61%     | ok               |
|          25 | -11.70%  | -11.27%            | -40.42% |    -0.09 |       71 | 46.59%     | ok               |

## PEP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 9.77%    | -15.39%            | -11.62% |     0.45 |       46 | 27.79%     | ok               |
|          45 | -0.55%   | -15.39%            | -14.22% |     0.03 |       70 | 32.61%     | ok               |
|          40 | -4.05%   | -15.39%            | -18.04% |    -0.09 |       78 | 38.44%     | ok               |
|          35 | -5.62%   | -15.39%            | -21.42% |    -0.12 |       87 | 43.43%     | ok               |
|          30 | -10.61%  | -15.39%            | -21.35% |    -0.25 |       85 | 50.08%     | ok               |

## PEPE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 10.36%   | -85.87%            | -57.66% |     0.36 |       77 | 43.87%     | ok               |
|          15 | -4.61%   | -85.87%            | -64.84% |     0.3  |       78 | 59.00%     | ok               |
|          35 | 4.07%    | -85.87%            | -51.35% |     0.29 |       62 | 38.51%     | ok               |
|          25 | -9.68%   | -85.87%            | -53.88% |     0.19 |       83 | 49.04%     | ok               |
|          20 | -25.63%  | -85.87%            | -64.07% |     0.06 |       84 | 55.36%     | ok               |

## PFE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -24.37%  | -8.23%             | -26.78% |    -0.87 |       52 | 20.80%     | ok               |
|          50 | -26.67%  | -8.23%             | -28.02% |    -1.06 |       44 | 16.97%     | ok               |
|          40 | -30.78%  | -8.23%             | -32.98% |    -1.06 |       76 | 25.62%     | ok               |
|          35 | -33.30%  | -8.23%             | -36.39% |    -1.07 |       82 | 32.61%     | ok               |
|          30 | -39.48%  | -8.23%             | -42.29% |    -1.26 |       77 | 36.11%     | ok               |

## PG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -0.00%   | -3.69%             | -19.77% |     0.05 |       52 | 34.94%     | ok               |
|          35 | -2.22%   | -3.69%             | -18.66% |    -0.04 |       60 | 38.27%     | ok               |
|          30 | -11.11%  | -3.69%             | -21.65% |    -0.39 |       62 | 41.43%     | ok               |
|          45 | -9.77%   | -3.69%             | -20.43% |    -0.4  |       52 | 32.45%     | ok               |
|          25 | -12.17%  | -3.69%             | -22.55% |    -0.43 |       72 | 42.60%     | ok               |

## PM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 1.99%    | 96.37%             | -32.20% |     0.14 |       88 | 53.58%     | ok               |
|          20 | -0.88%   | 96.37%             | -31.89% |     0.08 |       87 | 62.56%     | ok               |
|          30 | -1.28%   | 96.37%             | -33.68% |     0.07 |       81 | 57.57%     | ok               |
|          25 | -7.96%   | 96.37%             | -37.05% |    -0.08 |       81 | 59.90%     | ok               |
|          50 | -6.95%   | 96.37%             | -35.70% |    -0.09 |       74 | 42.10%     | ok               |

## POL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 64.83%   | -84.08%            | -46.45% |     0.77 |       79 | 49.62%     | ok               |
|          25 | 51.54%   | -84.08%            | -46.72% |     0.66 |       68 | 57.66%     | ok               |
|          20 | 41.20%   | -84.08%            | -52.88% |     0.58 |       76 | 63.03%     | ok               |
|          15 | 40.10%   | -84.08%            | -58.42% |     0.57 |       76 | 68.39%     | ok               |
|          50 | 20.67%   | -84.08%            | -22.86% |     0.45 |       50 | 20.69%     | ok               |

## QCOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -4.38%   | 50.02%             | -55.66% |     0.12 |       73 | 49.75%     | ok               |
|          35 | -6.63%   | 50.02%             | -51.84% |     0.08 |       83 | 45.09%     | ok               |
|          20 | -8.26%   | 50.02%             | -55.54% |     0.07 |       69 | 52.58%     | ok               |
|          30 | -16.82%  | 50.02%             | -57.69% |    -0.06 |       77 | 47.75%     | ok               |
|          15 | -23.51%  | 50.02%             | -59.01% |    -0.14 |       73 | 55.74%     | ok               |

## QQQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 24.22%   | 74.75%             | -12.88% |     0.64 |       57 | 49.25%     | ok               |
|          15 | 24.76%   | 74.75%             | -14.17% |     0.61 |       61 | 54.74%     | ok               |
|          20 | 21.22%   | 74.75%             | -12.98% |     0.56 |       65 | 51.91%     | ok               |
|          30 | 19.13%   | 74.75%             | -12.88% |     0.55 |       62 | 46.26%     | ok               |
|          35 | 6.95%    | 74.75%             | -19.00% |     0.27 |       68 | 42.60%     | ok               |

## RENDER-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 49.72%   | -59.35%            | -43.43% |     0.65 |       84 | 54.00%     | ok               |
|          15 | 32.34%   | -59.35%            | -44.59% |     0.55 |       84 | 57.08%     | ok               |
|          25 | 20.05%   | -59.35%            | -40.60% |     0.46 |       88 | 50.10%     | ok               |
|          30 | -17.59%  | -59.35%            | -45.00% |     0.11 |       96 | 43.74%     | ok               |
|          40 | -27.22%  | -59.35%            | -38.60% |    -0.1  |       70 | 29.16%     | ok               |

## RTX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 26.28%   | 105.29%            | -18.66% |     0.65 |       78 | 56.24%     | ok               |
|          50 | 19.09%   | 105.29%            | -18.42% |     0.6  |       58 | 42.10%     | ok               |
|          25 | 21.79%   | 105.29%            | -18.59% |     0.57 |       64 | 52.75%     | ok               |
|          30 | 19.95%   | 105.29%            | -16.99% |     0.53 |       58 | 51.58%     | ok               |
|          35 | 17.41%   | 105.29%            | -18.00% |     0.53 |       56 | 49.75%     | ok               |

## SBUX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -18.11%  | 8.46%              | -23.55% |    -0.32 |       63 | 40.93%     | ok               |
|          45 | -18.85%  | 8.46%              | -27.26% |    -0.44 |       64 | 28.45%     | ok               |
|          40 | -20.86%  | 8.46%              | -25.43% |    -0.46 |       60 | 32.45%     | ok               |
|          30 | -25.10%  | 8.46%              | -29.34% |    -0.52 |       62 | 38.60%     | ok               |
|          50 | -22.35%  | 8.46%              | -27.78% |    -0.58 |       52 | 24.63%     | ok               |

## SCHW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 1.55%    | 43.19%             | -15.92% |     0.12 |       54 | 33.28%     | ok               |
|          50 | -2.36%   | 43.19%             | -12.59% |    -0.02 |       48 | 30.78%     | ok               |
|          25 | -10.23%  | 43.19%             | -28.76% |    -0.16 |       61 | 47.75%     | ok               |
|          40 | -8.98%   | 43.19%             | -21.81% |    -0.18 |       62 | 36.27%     | ok               |
|          20 | -11.91%  | 43.19%             | -29.24% |    -0.2  |       69 | 50.42%     | ok               |

## SHIB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -0.73%   | -80.52%            | -49.21% |     0.24 |       78 | 68.39%     | ok               |
|          25 | -10.40%  | -80.52%            | -43.85% |     0.12 |       75 | 59.00%     | ok               |
|          20 | -11.72%  | -80.52%            | -46.92% |     0.12 |       77 | 63.60%     | ok               |
|          35 | -13.56%  | -80.52%            | -53.32% |     0.05 |       64 | 46.17%     | ok               |
|          40 | -16.59%  | -80.52%            | -50.74% |    -0.01 |       54 | 38.70%     | ok               |

## SHY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          30 | -2.23%   | -0.16%             | -2.85% |    -0.77 |       50 | 34.94%     | ok               |
|          35 | -2.34%   | -0.16%             | -3.27% |    -0.82 |       52 | 33.11%     | ok               |
|          40 | -2.46%   | -0.16%             | -3.33% |    -0.88 |       52 | 31.28%     | ok               |
|          45 | -2.44%   | -0.16%             | -3.23% |    -0.89 |       50 | 28.12%     | ok               |
|          50 | -2.61%   | -0.16%             | -3.40% |    -1    |       46 | 25.29%     | ok               |

## SKY-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -34.15%  | 3.34%              | -56.39% |    -0.39 |       58 | 51.16%     | ok               |
|          30 | -29.87%  | 3.34%              | -43.98% |    -0.39 |       68 | 40.70%     | ok               |
|          25 | -33.46%  | 3.34%              | -48.09% |    -0.45 |       63 | 44.42%     | ok               |
|          20 | -43.60%  | 3.34%              | -58.40% |    -0.64 |       60 | 48.14%     | ok               |
|          35 | -40.88%  | 3.34%              | -49.68% |    -0.75 |       62 | 34.19%     | ok               |

## SLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 11.83%   | -9.13%             | -24.10% |     0.34 |       48 | 35.77%     | ok               |
|          45 | 10.18%   | -9.13%             | -21.53% |     0.31 |       54 | 32.45%     | ok               |
|          50 | -10.05%  | -9.13%             | -29.84% |    -0.16 |       54 | 28.62%     | ok               |
|          35 | -17.17%  | -9.13%             | -43.22% |    -0.26 |       74 | 43.59%     | ok               |
|          30 | -30.54%  | -9.13%             | -55.49% |    -0.55 |       77 | 49.92%     | ok               |

## SLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 59.52%   | 185.28%            | -34.10% |     0.8  |       52 | 33.11%     | ok               |
|          45 | 56.99%   | 185.28%            | -31.82% |     0.78 |       56 | 33.94%     | ok               |
|          40 | 55.11%   | 185.28%            | -31.93% |     0.76 |       62 | 36.11%     | ok               |
|          35 | 42.84%   | 185.28%            | -36.89% |     0.64 |       64 | 38.27%     | ok               |
|          30 | 34.54%   | 185.28%            | -42.66% |     0.56 |       58 | 40.43%     | ok               |

## SMH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 124.67%  | 250.50%            | -30.17% |     1.37 |       47 | 53.58%     | ok               |
|          35 | 101.07%  | 250.50%            | -34.36% |     1.25 |       54 | 49.42%     | ok               |
|          25 | 100.93%  | 250.50%            | -32.94% |     1.23 |       46 | 52.41%     | ok               |
|          30 | 98.56%   | 250.50%            | -33.99% |     1.22 |       48 | 50.75%     | ok               |
|          45 | 84.11%   | 250.50%            | -32.75% |     1.18 |       52 | 43.59%     | ok               |

## SNX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 42.07%   | -87.83%            | -28.28% |     0.6  |       64 | 32.38%     | ok               |
|          20 | 27.43%   | -87.83%            | -43.20% |     0.49 |       72 | 50.00%     | ok               |
|          30 | 24.76%   | -87.83%            | -32.91% |     0.46 |       61 | 39.66%     | ok               |
|          25 | 4.95%    | -87.83%            | -36.73% |     0.3  |       73 | 44.06%     | ok               |
|          15 | -12.86%  | -87.83%            | -47.56% |     0.16 |       82 | 54.60%     | ok               |

## SOL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -20.20%  | -66.26%            | -55.65% |     0.01 |       64 | 39.08%     | ok               |
|          25 | -32.68%  | -66.26%            | -53.21% |    -0.09 |       72 | 57.66%     | ok               |
|          35 | -33.64%  | -66.26%            | -61.96% |    -0.13 |       72 | 46.74%     | ok               |
|          15 | -37.97%  | -66.26%            | -59.14% |    -0.14 |       74 | 64.75%     | ok               |
|          20 | -42.35%  | -66.26%            | -56.90% |    -0.22 |       68 | 60.15%     | ok               |

## SOXX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 101.18%  | 220.92%            | -38.67% |     1.18 |       53 | 52.25%     | ok               |
|          25 | 97.33%   | 220.92%            | -39.85% |     1.15 |       51 | 51.91%     | ok               |
|          35 | 91.81%   | 220.92%            | -38.63% |     1.13 |       59 | 47.25%     | ok               |
|          15 | 96.13%   | 220.92%            | -37.72% |     1.1  |       66 | 55.07%     | ok               |
|          30 | 86.24%   | 220.92%            | -40.34% |     1.07 |       55 | 49.75%     | ok               |

## SPY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 17.82%   | 53.21%             | -14.25% |     0.61 |       58 | 54.41%     | ok               |
|          15 | 16.65%   | 53.21%             | -16.80% |     0.56 |       65 | 57.40%     | ok               |
|          25 | 10.49%   | 53.21%             | -15.22% |     0.4  |       58 | 53.41%     | ok               |
|          30 | 6.50%    | 53.21%             | -16.47% |     0.28 |       60 | 50.92%     | ok               |
|          35 | 3.93%    | 53.21%             | -16.72% |     0.2  |       58 | 48.25%     | ok               |

## SUSHI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -24.39%  | -89.64%            | -40.79% |    -0.2  |       52 | 14.56%     | ok               |
|          45 | -56.30%  | -89.64%            | -64.69% |    -0.71 |       54 | 17.82%     | ok               |
|          40 | -59.39%  | -89.64%            | -66.97% |    -0.72 |       61 | 24.33%     | ok               |
|          35 | -67.00%  | -89.64%            | -75.30% |    -0.85 |       76 | 29.69%     | ok               |
|          15 | -80.09%  | -89.64%            | -81.81% |    -0.99 |       88 | 47.13%     | ok               |

## T Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 61.08%   | 27.30%             | -18.13% |     1.21 |       55 | 55.07%     | ok               |
|          25 | 52.82%   | 27.30%             | -17.66% |     1.1  |       60 | 52.75%     | ok               |
|          15 | 52.28%   | 27.30%             | -15.08% |     1.05 |       64 | 58.90%     | ok               |
|          30 | 37.57%   | 27.30%             | -17.01% |     0.87 |       62 | 50.58%     | ok               |
|          35 | 34.98%   | 27.30%             | -14.49% |     0.84 |       62 | 47.42%     | ok               |

## TGT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -8.23%   | -8.27%             | -41.89% |    -0.05 |       79 | 46.09%     | ok               |
|          15 | -11.23%  | -8.27%             | -39.76% |    -0.1  |       69 | 50.58%     | ok               |
|          25 | -10.93%  | -8.27%             | -43.53% |    -0.13 |       61 | 41.26%     | ok               |
|          45 | -10.17%  | -8.27%             | -30.47% |    -0.16 |       50 | 28.95%     | ok               |
|          30 | -11.79%  | -8.27%             | -41.74% |    -0.16 |       56 | 38.60%     | ok               |

## TIA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 37.75%   | -93.02%            | -31.28% |     0.56 |       60 | 24.90%     | ok               |
|          35 | 32.05%   | -93.02%            | -36.61% |     0.52 |       60 | 29.50%     | ok               |
|          45 | 15.72%   | -93.02%            | -44.21% |     0.37 |       50 | 18.58%     | ok               |
|          50 | 13.81%   | -93.02%            | -44.86% |     0.36 |       32 | 11.49%     | ok               |
|          30 | -17.64%  | -93.02%            | -55.19% |     0.06 |       84 | 34.48%     | ok               |

## TLT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -13.95%  | -7.50%             | -16.06% |    -1.49 |       34 | 14.48%     | ok               |
|          30 | -23.55%  | -7.50%             | -23.95% |    -1.74 |       70 | 32.11%     | ok               |
|          40 | -19.15%  | -7.50%             | -20.30% |    -1.78 |       60 | 20.97%     | ok               |
|          45 | -17.98%  | -7.50%             | -19.55% |    -1.84 |       42 | 16.97%     | ok               |
|          35 | -23.06%  | -7.50%             | -23.46% |    -1.94 |       68 | 26.12%     | ok               |

## TMO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 43.47%   | -15.11%            | -10.55% |     0.99 |       36 | 30.12%     | ok               |
|          45 | 42.67%   | -15.11%            | -12.29% |     0.94 |       44 | 35.11%     | ok               |
|          40 | 40.56%   | -15.11%            | -12.07% |     0.89 |       47 | 39.60%     | ok               |
|          35 | 24.33%   | -15.11%            | -16.12% |     0.58 |       59 | 43.93%     | ok               |
|          30 | 13.87%   | -15.11%            | -16.83% |     0.38 |       59 | 47.92%     | ok               |

## TMUS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 15.65%   | 12.03%             | -26.87% |     0.41 |       71 | 59.90%     | ok               |
|          30 | 14.44%   | 12.03%             | -24.50% |     0.39 |       72 | 48.09%     | ok               |
|          20 | 8.54%    | 12.03%             | -24.82% |     0.27 |       73 | 54.24%     | ok               |
|          25 | 7.47%    | 12.03%             | -25.91% |     0.25 |       77 | 50.58%     | ok               |
|          50 | 4.50%    | 12.03%             | -22.71% |     0.2  |       58 | 35.77%     | ok               |

## TRX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 1.39%    | 31.75%             | -18.79% |     0.12 |       54 | 37.93%     | ok               |
|          30 | 0.84%    | 31.75%             | -22.90% |     0.11 |       74 | 49.23%     | ok               |
|          35 | -0.53%   | 31.75%             | -21.77% |     0.07 |       70 | 46.55%     | ok               |
|          50 | -0.25%   | 31.75%             | -18.49% |     0.07 |       44 | 32.38%     | ok               |
|          25 | -0.97%   | 31.75%             | -26.84% |     0.07 |       70 | 52.49%     | ok               |

## TSLA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 63.39%   | 118.55%            | -32.60% |     0.78 |       64 | 30.62%     | ok               |
|          40 | 57.66%   | 118.55%            | -45.90% |     0.7  |       59 | 34.94%     | ok               |
|          45 | 33.57%   | 118.55%            | -46.86% |     0.52 |       63 | 32.28%     | ok               |
|          35 | 23.09%   | 118.55%            | -51.29% |     0.42 |       70 | 37.77%     | ok               |
|          30 | -0.11%   | 118.55%            | -54.91% |     0.21 |       66 | 42.26%     | ok               |

## TXN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 13.38%   | 96.76%             | -45.45% |     0.33 |       72 | 35.77%     | ok               |
|          20 | 2.88%    | 96.76%             | -38.98% |     0.19 |       62 | 59.90%     | ok               |
|          15 | 0.75%    | 96.76%             | -39.48% |     0.17 |       65 | 64.06%     | ok               |
|          35 | -5.44%   | 96.76%             | -43.38% |     0.05 |       78 | 50.42%     | ok               |
|          40 | -6.08%   | 96.76%             | -45.67% |     0.04 |       76 | 48.25%     | ok               |

## UNH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 25.26%   | -20.32%            | -36.91% |     0.49 |       50 | 28.79%     | ok               |
|          30 | 23.44%   | -20.32%            | -27.46% |     0.45 |       76 | 52.08%     | ok               |
|          35 | 18.88%   | -20.32%            | -29.39% |     0.4  |       70 | 46.76%     | ok               |
|          15 | 19.09%   | -20.32%            | -30.48% |     0.39 |       79 | 67.05%     | ok               |
|          20 | 16.27%   | -20.32%            | -31.00% |     0.36 |       81 | 61.90%     | ok               |

## UNI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -15.35%  | -79.55%            | -57.12% |     0.03 |       54 | 25.29%     | ok               |
|          40 | -25.14%  | -79.55%            | -63.75% |    -0.08 |       58 | 30.46%     | ok               |
|          50 | -23.03%  | -79.55%            | -55.74% |    -0.1  |       52 | 20.69%     | ok               |
|          35 | -37.17%  | -79.55%            | -69.40% |    -0.2  |       72 | 35.44%     | ok               |
|          20 | -72.45%  | -79.55%            | -80.81% |    -0.74 |       99 | 51.92%     | ok               |

## UPS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -36.12%  | -34.17%            | -42.25% |    -0.69 |       74 | 44.76%     | ok               |
|          35 | -34.91%  | -34.17%            | -40.47% |    -0.7  |       59 | 34.28%     | ok               |
|          20 | -37.19%  | -34.17%            | -45.77% |    -0.71 |       80 | 47.92%     | ok               |
|          30 | -37.30%  | -34.17%            | -40.62% |    -0.74 |       66 | 39.93%     | ok               |
|          40 | -36.21%  | -34.17%            | -42.12% |    -0.76 |       51 | 29.12%     | ok               |

## USO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 15.25%   | 57.14%             | -33.25% |     0.36 |       46 | 27.45%     | ok               |
|          30 | 1.63%    | 57.14%             | -44.00% |     0.15 |       68 | 34.61%     | ok               |
|          40 | 1.81%    | 57.14%             | -41.14% |     0.15 |       57 | 29.95%     | ok               |
|          50 | 2.11%    | 57.14%             | -31.13% |     0.15 |       54 | 24.96%     | ok               |
|          25 | -3.04%   | 57.14%             | -46.57% |     0.08 |       68 | 37.10%     | ok               |

## VEA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 5.44%    | 52.46%             | -16.28% |     0.25 |       60 | 50.58%     | ok               |
|          20 | 1.19%    | 52.46%             | -17.70% |     0.1  |       61 | 47.92%     | ok               |
|          25 | -0.82%   | 52.46%             | -17.79% |     0.02 |       57 | 46.26%     | ok               |
|          30 | -0.98%   | 52.46%             | -17.93% |     0.01 |       58 | 44.09%     | ok               |
|          35 | -2.09%   | 52.46%             | -16.79% |    -0.03 |       56 | 43.09%     | ok               |

## VIXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -46.17%  | -62.06%            | -68.69% |    -0.39 |       44 | 10.32%     | ok               |
|          45 | -56.13%  | -62.06%            | -74.13% |    -0.55 |       56 | 16.31%     | ok               |
|          40 | -64.45%  | -62.06%            | -80.03% |    -0.66 |       70 | 20.63%     | ok               |
|          35 | -68.17%  | -62.06%            | -83.81% |    -0.7  |       86 | 25.79%     | ok               |
|          15 | -78.02%  | -62.06%            | -89.47% |    -0.81 |      102 | 44.26%     | ok               |

## VNQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -8.60%   | 12.50%             | -19.07% |    -0.37 |       60 | 28.62%     | ok               |
|          50 | -9.03%   | 12.50%             | -17.13% |    -0.41 |       56 | 26.12%     | ok               |
|          25 | -13.12%  | 12.50%             | -22.34% |    -0.51 |       69 | 40.77%     | ok               |
|          40 | -14.13%  | 12.50%             | -24.84% |    -0.62 |       74 | 32.11%     | ok               |
|          20 | -16.52%  | 12.50%             | -23.79% |    -0.64 |       74 | 43.59%     | ok               |

## VTI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 19.29%   | 52.81%             | -13.96% |     0.64 |       62 | 55.74%     | ok               |
|          15 | 13.18%   | 52.81%             | -15.70% |     0.46 |       65 | 58.24%     | ok               |
|          25 | 6.34%    | 52.81%             | -16.10% |     0.27 |       58 | 53.91%     | ok               |
|          30 | -0.72%   | 52.81%             | -18.77% |     0.04 |       66 | 52.08%     | ok               |
|          40 | -2.95%   | 52.81%             | -20.44% |    -0.05 |       68 | 45.42%     | ok               |

## VWO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -9.03%   | 51.32%             | -24.01% |    -0.26 |       69 | 49.42%     | ok               |
|          50 | -7.89%   | 51.32%             | -21.68% |    -0.28 |       60 | 32.45%     | ok               |
|          20 | -10.06%  | 51.32%             | -26.14% |    -0.31 |       67 | 47.25%     | ok               |
|          40 | -8.98%   | 51.32%             | -23.57% |    -0.31 |       70 | 37.94%     | ok               |
|          45 | -9.69%   | 51.32%             | -23.75% |    -0.35 |       62 | 34.94%     | ok               |

## VZ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -6.24%   | 7.00%              | -16.98% |    -0.18 |       50 | 25.46%     | ok               |
|          45 | -14.65%  | 7.00%              | -20.38% |    -0.48 |       58 | 28.45%     | ok               |
|          35 | -19.70%  | 7.00%              | -24.68% |    -0.66 |       61 | 33.94%     | ok               |
|          25 | -22.70%  | 7.00%              | -28.84% |    -0.7  |       78 | 41.76%     | ok               |
|          40 | -22.48%  | 7.00%              | -26.72% |    -0.8  |       64 | 30.95%     | ok               |

## WFC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -2.92%   | 63.35%             | -18.29% |    -0.03 |       58 | 33.11%     | ok               |
|          35 | -7.13%   | 63.35%             | -22.53% |    -0.08 |       79 | 44.76%     | ok               |
|          45 | -10.05%  | 63.35%             | -24.02% |    -0.23 |       66 | 37.77%     | ok               |
|          20 | -18.54%  | 63.35%             | -29.96% |    -0.28 |       79 | 54.08%     | ok               |
|          40 | -13.65%  | 63.35%             | -24.88% |    -0.34 |       76 | 41.10%     | ok               |

## WIF-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 81.89%   | -91.17%            | -46.21% |     0.76 |       73 | 41.57%     | ok               |
|          20 | 75.46%   | -91.17%            | -40.67% |     0.73 |       67 | 38.89%     | ok               |
|          25 | 15.58%   | -91.17%            | -45.19% |     0.41 |       69 | 36.21%     | ok               |
|          30 | -26.73%  | -91.17%            | -50.54% |    -0.01 |       70 | 32.18%     | ok               |
|          50 | -21.97%  | -91.17%            | -38.87% |    -0.18 |       40 | 11.88%     | ok               |

## WMT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 61.82%   | 114.00%            | -9.18%  |     1.58 |       36 | 44.09%     | ok               |
|          50 | 55.24%   | 114.00%            | -12.19% |     1.52 |       30 | 41.93%     | ok               |
|          40 | 51.70%   | 114.00%            | -9.18%  |     1.35 |       40 | 45.26%     | ok               |
|          35 | 49.46%   | 114.00%            | -10.11% |     1.27 |       50 | 49.25%     | ok               |
|          30 | 27.82%   | 114.00%            | -21.31% |     0.75 |       57 | 51.75%     | ok               |

## XBI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 3.96%    | 59.47%             | -16.71% |     0.18 |       60 | 34.61%     | ok               |
|          45 | 3.16%    | 59.47%             | -16.88% |     0.16 |       52 | 31.45%     | ok               |
|          35 | -3.05%   | 59.47%             | -21.38% |     0.01 |       62 | 37.77%     | ok               |
|          30 | -4.13%   | 59.47%             | -21.75% |    -0.02 |       62 | 39.43%     | ok               |
|          50 | -5.14%   | 59.47%             | -16.83% |    -0.07 |       54 | 28.29%     | ok               |

## XLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -4.67%   | 25.58%             | -20.60% |    -0.12 |       60 | 32.11%     | ok               |
|          50 | -4.61%   | 25.58%             | -17.40% |    -0.14 |       44 | 27.79%     | ok               |
|          35 | -7.91%   | 25.58%             | -23.62% |    -0.24 |       60 | 35.61%     | ok               |
|          45 | -7.43%   | 25.58%             | -20.61% |    -0.25 |       44 | 29.28%     | ok               |
|          25 | -12.31%  | 25.58%             | -23.73% |    -0.4  |       70 | 41.43%     | ok               |

## XLC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 15.26%   | 40.90%             | -12.33% |     0.53 |       65 | 55.57%     | ok               |
|          25 | 13.09%   | 40.90%             | -12.31% |     0.46 |       62 | 57.40%     | ok               |
|          40 | 10.03%   | 40.90%             | -13.38% |     0.4  |       68 | 48.09%     | ok               |
|          35 | 10.00%   | 40.90%             | -13.38% |     0.39 |       64 | 52.58%     | ok               |
|          20 | 5.14%    | 40.90%             | -13.78% |     0.22 |       70 | 60.07%     | ok               |

## XLE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -1.92%   | 27.64%             | -25.98% |     0.02 |       56 | 36.77%     | ok               |
|          35 | -3.79%   | 27.64%             | -32.17% |    -0.02 |       65 | 44.59%     | ok               |
|          45 | -5.17%   | 27.64%             | -30.88% |    -0.07 |       62 | 39.60%     | ok               |
|          30 | -9.48%   | 27.64%             | -36.18% |    -0.17 |       71 | 46.59%     | ok               |
|          25 | -10.53%  | 27.64%             | -36.92% |    -0.18 |       78 | 49.92%     | ok               |

## XLF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -5.20%   | 38.60%             | -18.01% |    -0.12 |       66 | 54.08%     | ok               |
|          15 | -9.12%   | 38.60%             | -19.58% |    -0.25 |       74 | 56.91%     | ok               |
|          25 | -11.81%  | 38.60%             | -23.22% |    -0.38 |       75 | 50.58%     | ok               |
|          30 | -12.23%  | 38.60%             | -23.61% |    -0.41 |       76 | 48.25%     | ok               |
|          35 | -19.28%  | 38.60%             | -27.24% |    -0.77 |       66 | 44.09%     | ok               |

## XLI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 11.79%   | 59.49%             | -10.36% |     0.45 |       72 | 53.41%     | ok               |
|          20 | 7.58%    | 59.49%             | -12.74% |     0.33 |       63 | 49.08%     | ok               |
|          30 | 5.22%    | 59.49%             | -11.38% |     0.25 |       64 | 46.59%     | ok               |
|          45 | 4.47%    | 59.49%             | -12.27% |     0.24 |       62 | 37.94%     | ok               |
|          50 | 4.16%    | 59.49%             | -9.25%  |     0.23 |       56 | 35.94%     | ok               |

## XLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 84.82%   | 89.78%             | -14.75% |     1.35 |       41 | 53.74%     | ok               |
|          20 | 70.36%   | 89.78%             | -14.75% |     1.21 |       48 | 51.58%     | ok               |
|          25 | 66.89%   | 89.78%             | -14.75% |     1.21 |       42 | 49.42%     | ok               |
|          30 | 64.71%   | 89.78%             | -14.75% |     1.2  |       42 | 48.25%     | ok               |
|          35 | 46.33%   | 89.78%             | -13.61% |     0.96 |       54 | 45.59%     | ok               |

## XLM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 18.64%   | -55.99%            | -36.83% |     0.4  |       46 | 27.78%     | ok               |
|          45 | 15.07%   | -55.99%            | -42.02% |     0.37 |       52 | 31.42%     | ok               |
|          30 | -1.93%   | -55.99%            | -46.56% |     0.2  |       71 | 45.79%     | ok               |
|          40 | -8.80%   | -55.99%            | -41.83% |     0.11 |       51 | 35.63%     | ok               |
|          35 | -10.51%  | -55.99%            | -46.62% |     0.1  |       71 | 41.76%     | ok               |

## XLP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 11.54%   | 14.69%             | -5.66%  |     0.71 |       56 | 33.78%     | ok               |
|          50 | 9.69%    | 14.69%             | -6.08%  |     0.61 |       58 | 31.78%     | ok               |
|          40 | 9.29%    | 14.69%             | -7.77%  |     0.56 |       72 | 37.94%     | ok               |
|          35 | 8.34%    | 14.69%             | -9.73%  |     0.5  |       68 | 40.93%     | ok               |
|          30 | 7.46%    | 14.69%             | -10.28% |     0.45 |       70 | 42.60%     | ok               |

## XLU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 7.92%    | 46.25%             | -9.11%  |     0.42 |       50 | 30.62%     | ok               |
|          45 | 5.70%    | 46.25%             | -10.56% |     0.32 |       54 | 31.61%     | ok               |
|          40 | 2.78%    | 46.25%             | -11.94% |     0.18 |       58 | 33.11%     | ok               |
|          35 | -1.19%   | 46.25%             | -16.24% |    -0.01 |       62 | 35.44%     | ok               |
|          30 | -4.29%   | 46.25%             | -18.15% |    -0.15 |       69 | 38.44%     | ok               |

## XLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -10.46%  | 7.27%              | -16.83% |    -0.5  |       68 | 36.44%     | ok               |
|          25 | -11.78%  | 7.27%              | -18.06% |    -0.56 |       70 | 37.77%     | ok               |
|          15 | -15.78%  | 7.27%              | -21.47% |    -0.75 |       81 | 42.60%     | ok               |
|          20 | -15.71%  | 7.27%              | -21.56% |    -0.77 |       75 | 39.43%     | ok               |
|          35 | -15.14%  | 7.27%              | -20.96% |    -0.8  |       66 | 33.94%     | ok               |

## XLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 4.62%    | 36.49%             | -12.94% |     0.21 |       72 | 41.26%     | ok               |
|          30 | 0.81%    | 36.49%             | -14.01% |     0.09 |       74 | 44.43%     | ok               |
|          50 | -0.91%   | 36.49%             | -13.71% |     0.02 |       50 | 29.78%     | ok               |
|          15 | -2.27%   | 36.49%             | -15.77% |     0.01 |       77 | 51.75%     | ok               |
|          40 | -1.91%   | 36.49%             | -16.99% |    -0.01 |       68 | 37.10%     | ok               |

## XOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 5.34%    | 33.80%             | -19.90% |     0.22 |       56 | 36.77%     | ok               |
|          30 | 4.30%    | 33.80%             | -20.29% |     0.19 |       56 | 36.11%     | ok               |
|          20 | 1.45%    | 33.80%             | -25.56% |     0.12 |       61 | 39.27%     | ok               |
|          50 | 0.21%    | 33.80%             | -21.35% |     0.08 |       46 | 29.78%     | ok               |
|          35 | -1.82%   | 33.80%             | -20.93% |     0.02 |       58 | 34.78%     | ok               |

## XRP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -29.67%  | -65.28%            | -50.11% |    -0.21 |       70 | 41.95%     | ok               |
|          40 | -36.21%  | -65.28%            | -48.42% |    -0.36 |       62 | 35.82%     | ok               |
|          30 | -42.86%  | -65.28%            | -58.77% |    -0.42 |       74 | 46.36%     | ok               |
|          45 | -43.39%  | -65.28%            | -50.29% |    -0.52 |       62 | 31.42%     | ok               |
|          50 | -40.94%  | -65.28%            | -40.94% |    -0.58 |       64 | 23.75%     | ok               |

## YFI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -30.68%  | -78.93%            | -50.17% |    -0.41 |       60 | 27.20%     | ok               |
|          45 | -36.29%  | -78.93%            | -51.92% |    -0.62 |       62 | 22.61%     | ok               |
|          35 | -50.37%  | -78.93%            | -64.34% |    -0.77 |       71 | 34.48%     | ok               |
|          30 | -53.87%  | -78.93%            | -67.78% |    -0.79 |       81 | 40.42%     | ok               |
|          50 | -41.48%  | -78.93%            | -51.80% |    -0.84 |       52 | 17.43%     | ok               |

## ZEC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 124.17%  | 717.61%            | -24.66% |     0.9  |       50 | 23.18%     | ok               |
|          35 | 81.53%   | 717.61%            | -44.34% |     0.72 |       62 | 31.23%     | ok               |
|          25 | 55.64%   | 717.61%            | -48.59% |     0.62 |       63 | 40.23%     | ok               |
|          50 | 54.10%   | 717.61%            | -37.94% |     0.6  |       52 | 20.69%     | ok               |
|          30 | 39.82%   | 717.61%            | -47.68% |     0.54 |       71 | 36.78%     | ok               |
