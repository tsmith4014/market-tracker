# Market Tracker Backtest Report

_Generated: 2026-06-30T01:28:36+00:00_

## Data Sources

- Crypto: Kraken -> Coinbase -> CoinGecko OHLC -> CoinPaprika fallback chain.
- Stocks / ETFs / indices: Stooq -> Yahoo Finance fallback chain.
- Data rows are generated from real market APIs. Mock OHLCV rows are not generated.

## Data Freshness

- Rows: **92,445**
- Symbols: **161**
- Date range: **2024-02-05** to **2026-06-30**

## Latest Signals

| symbol     | date                |         close |   composite_score | signal   | data_source   |
|:-----------|:--------------------|--------------:|------------------:|:---------|:--------------|
| AAVE-USD   | 2026-06-30 00:00:00 |    90.43      |         46.6667   | LONG     | Kraken API    |
| AMAT       | 2026-06-29 00:00:00 |   694.64      |         70.0833   | LONG     | Yahoo Finance |
| BAC        | 2026-06-29 00:00:00 |    57.88      |         58.0833   | LONG     | Yahoo Finance |
| C          | 2026-06-29 00:00:00 |   142.49      |         59.9167   | LONG     | Yahoo Finance |
| CAT        | 2026-06-29 00:00:00 |  1033.19      |         72.9167   | LONG     | Yahoo Finance |
| DE         | 2026-06-29 00:00:00 |   626.63      |         79.0833   | LONG     | Yahoo Finance |
| DXY-INDEX  | 2026-06-29 00:00:00 |   101.268     |         75        | LONG     | Yahoo Finance |
| GE         | 2026-06-29 00:00:00 |   373.71      |         62.25     | LONG     | Yahoo Finance |
| HD         | 2026-06-29 00:00:00 |   350.81      |         65.5      | LONG     | Yahoo Finance |
| ITA        | 2026-06-29 00:00:00 |   239.13      |         65.0833   | LONG     | Yahoo Finance |
| JNJ        | 2026-06-29 00:00:00 |   258.51      |         75.75     | LONG     | Yahoo Finance |
| JPM        | 2026-06-29 00:00:00 |   329.39      |         59.6667   | LONG     | Yahoo Finance |
| LLY        | 2026-06-29 00:00:00 |  1229.93      |         51.0833   | LONG     | Yahoo Finance |
| LRCX       | 2026-06-29 00:00:00 |   410.91      |         73.4167   | LONG     | Yahoo Finance |
| PG         | 2026-06-29 00:00:00 |   148.45      |         39.4167   | LONG     | Yahoo Finance |
| QQQ        | 2026-06-29 00:00:00 |   724.08      |         41.4167   | LONG     | Yahoo Finance |
| RTX        | 2026-06-29 00:00:00 |   187.33      |         63.4167   | LONG     | Yahoo Finance |
| SBUX       | 2026-06-29 00:00:00 |   104.06      |         68.75     | LONG     | Yahoo Finance |
| TGT        | 2026-06-29 00:00:00 |   133.92      |         69.9167   | LONG     | Yahoo Finance |
| TLT        | 2026-06-29 00:00:00 |    87.45      |         69.5      | LONG     | Yahoo Finance |
| TMO        | 2026-06-29 00:00:00 |   506.42      |         63.0833   | LONG     | Yahoo Finance |
| UNH        | 2026-06-29 00:00:00 |   419.82      |         64.9167   | LONG     | Yahoo Finance |
| UPS        | 2026-06-29 00:00:00 |   108.01      |         42.8333   | LONG     | Yahoo Finance |
| WFC        | 2026-06-29 00:00:00 |    83.51      |         47.4167   | LONG     | Yahoo Finance |
| XBI        | 2026-06-29 00:00:00 |   158.31      |         73.75     | LONG     | Yahoo Finance |
| XLF        | 2026-06-29 00:00:00 |    53.72      |         65.4167   | LONG     | Yahoo Finance |
| XLU        | 2026-06-29 00:00:00 |    46.02      |         52.75     | LONG     | Yahoo Finance |
| AAPL       | 2026-06-29 00:00:00 |   281.74      |        -27.8333   | NEUTRAL  | Yahoo Finance |
| ABBV       | 2026-06-29 00:00:00 |   254.31      |         50.5      | NEUTRAL  | Yahoo Finance |
| AGG        | 2026-06-29 00:00:00 |    99.37      |         58.25     | NEUTRAL  | Yahoo Finance |
| ALGO-USD   | 2026-06-30 00:00:00 |     0.08509   |        -33.5833   | NEUTRAL  | Kraken API    |
| AMD        | 2026-06-29 00:00:00 |   539.49      |         44.6667   | NEUTRAL  | Yahoo Finance |
| AMGN       | 2026-06-29 00:00:00 |   360.55      |         62.3333   | NEUTRAL  | Yahoo Finance |
| AMZN       | 2026-06-29 00:00:00 |   240.14      |          4.66667  | NEUTRAL  | Yahoo Finance |
| APT-USD    | 2026-06-30 00:00:00 |     0.5694    |        -29        | NEUTRAL  | Kraken API    |
| ARB-USD    | 2026-06-30 00:00:00 |     0.0757    |        -49.25     | NEUTRAL  | Kraken API    |
| ARKK       | 2026-06-29 00:00:00 |    80.63      |         49.0833   | NEUTRAL  | Yahoo Finance |
| AVAX-USD   | 2026-06-30 00:00:00 |     6.621     |        -15.1667   | NEUTRAL  | Kraken API    |
| AVGO       | 2026-06-29 00:00:00 |   372.45      |        -27.6667   | NEUTRAL  | Yahoo Finance |
| BA         | 2026-06-29 00:00:00 |   214.69      |        -48.25     | NEUTRAL  | Yahoo Finance |
| BCH-USD    | 2026-06-30 00:00:00 |   199.17      |        -47.9167   | NEUTRAL  | Kraken API    |
| BLK        | 2026-06-29 00:00:00 |   950.17      |        -61.6667   | NEUTRAL  | Yahoo Finance |
| BND        | 2026-06-29 00:00:00 |    73.71      |         58.25     | NEUTRAL  | Yahoo Finance |
| BONK-USD   | 2026-06-30 00:00:00 |     4.214e-06 |        -40.25     | NEUTRAL  | Kraken API    |
| CL         | 2026-06-29 00:00:00 |    92.4       |         64        | NEUTRAL  | Yahoo Finance |
| CMCSA      | 2026-06-29 00:00:00 |    24.22      |         21.1667   | NEUTRAL  | Yahoo Finance |
| COST       | 2026-06-29 00:00:00 |   946.68      |        -35.75     | NEUTRAL  | Yahoo Finance |
| CSCO       | 2026-06-29 00:00:00 |   117.7       |         20.5833   | NEUTRAL  | Yahoo Finance |
| DASH-USD   | 2026-06-30 00:00:00 |    32.689     |        -72.75     | NEUTRAL  | Kraken API    |
| DBC        | 2026-06-29 00:00:00 |    26.56      |        -13.1667   | NEUTRAL  | Yahoo Finance |
| DIA        | 2026-06-29 00:00:00 |   521.68      |         34.3333   | NEUTRAL  | Yahoo Finance |
| DIS        | 2026-06-29 00:00:00 |    98.63      |        -52        | NEUTRAL  | Yahoo Finance |
| EEM        | 2026-06-29 00:00:00 |    67.43      |         11.5      | NEUTRAL  | Yahoo Finance |
| EFA        | 2026-06-29 00:00:00 |   103.45      |          2.58333  | NEUTRAL  | Yahoo Finance |
| EOG        | 2026-06-29 00:00:00 |   131.93      |        -24.75     | NEUTRAL  | Yahoo Finance |
| ETC-USD    | 2026-06-30 00:00:00 |     7.041     |        -36.9167   | NEUTRAL  | Kraken API    |
| EWJ        | 2026-06-29 00:00:00 |    93.21      |         19        | NEUTRAL  | Yahoo Finance |
| FCX        | 2026-06-29 00:00:00 |    61.62      |        -18.3333   | NEUTRAL  | Yahoo Finance |
| FIL-USD    | 2026-06-30 00:00:00 |     0.727     |        -29        | NEUTRAL  | Kraken API    |
| GDX        | 2026-06-29 00:00:00 |    75.68      |        -66.5      | NEUTRAL  | Yahoo Finance |
| GDXJ       | 2026-06-29 00:00:00 |    98.92      |        -57.75     | NEUTRAL  | Yahoo Finance |
| GOOGL      | 2026-06-29 00:00:00 |   353.65      |        -37.3333   | NEUTRAL  | Yahoo Finance |
| GRT-USD    | 2026-06-30 00:00:00 |     0.01771   |        -40.25     | NEUTRAL  | Kraken API    |
| GS         | 2026-06-29 00:00:00 |  1020.21      |         -1.58333  | NEUTRAL  | Yahoo Finance |
| HON        | 2026-06-29 00:00:00 |   227.8       |          4.91667  | NEUTRAL  | Yahoo Finance |
| HYG        | 2026-06-29 00:00:00 |    80.01      |         26.0833   | NEUTRAL  | Yahoo Finance |
| IBM        | 2026-06-29 00:00:00 |   278         |         22.3333   | NEUTRAL  | Yahoo Finance |
| ICP-USD    | 2026-06-30 00:00:00 |     2.161     |        -40.9167   | NEUTRAL  | Kraken API    |
| IEF        | 2026-06-29 00:00:00 |    95.06      |         31.25     | NEUTRAL  | Yahoo Finance |
| IEMG       | 2026-06-29 00:00:00 |    81.72      |         11.5      | NEUTRAL  | Yahoo Finance |
| INJ-USD    | 2026-06-30 00:00:00 |     4.66      |        -55.8333   | NEUTRAL  | Kraken API    |
| INTC       | 2026-06-29 00:00:00 |   131.72      |         55.3333   | NEUTRAL  | Yahoo Finance |
| IWM        | 2026-06-29 00:00:00 |   298.97      |         55.3333   | NEUTRAL  | Yahoo Finance |
| KO         | 2026-06-29 00:00:00 |    82.65      |         67.3333   | NEUTRAL  | Yahoo Finance |
| LDO-USD    | 2026-06-30 00:00:00 |     0.25      |        -40.25     | NEUTRAL  | Kraken API    |
| LIN        | 2026-06-29 00:00:00 |   511.06      |         23.8333   | NEUTRAL  | Yahoo Finance |
| LINK-USD   | 2026-06-30 00:00:00 |     7.28229   |        -60.5833   | NEUTRAL  | Kraken API    |
| LTC-USD    | 2026-06-30 00:00:00 |    42.64      |        -34.9167   | NEUTRAL  | Kraken API    |
| MCD        | 2026-06-29 00:00:00 |   267.18      |        -64.5      | NEUTRAL  | Yahoo Finance |
| META       | 2026-06-29 00:00:00 |   562.6       |        -59.8333   | NEUTRAL  | Yahoo Finance |
| MPC        | 2026-06-29 00:00:00 |   259.22      |         21.8333   | NEUTRAL  | Yahoo Finance |
| MRK        | 2026-06-29 00:00:00 |   129.38      |         67.3333   | NEUTRAL  | Yahoo Finance |
| MS         | 2026-06-29 00:00:00 |   211.72      |         23.9167   | NEUTRAL  | Yahoo Finance |
| MU         | 2026-06-29 00:00:00 |  1145.28      |         34.5      | NEUTRAL  | Yahoo Finance |
| NEAR-USD   | 2026-06-30 00:00:00 |     1.8299    |        -33.8333   | NEUTRAL  | Kraken API    |
| NEM        | 2026-06-29 00:00:00 |    94.51      |        -64.5      | NEUTRAL  | Yahoo Finance |
| NKE        | 2026-06-29 00:00:00 |    41.48      |        -60.8333   | NEUTRAL  | Yahoo Finance |
| OP-USD     | 2026-06-30 00:00:00 |     0.0993    |        -40.25     | NEUTRAL  | Kraken API    |
| PEP        | 2026-06-29 00:00:00 |   138.68      |        -60        | NEUTRAL  | Yahoo Finance |
| PFE        | 2026-06-29 00:00:00 |    24.37      |        -51.8333   | NEUTRAL  | Yahoo Finance |
| PM         | 2026-06-29 00:00:00 |   182.87      |         54.5      | NEUTRAL  | Yahoo Finance |
| POL-USD    | 2026-06-30 00:00:00 |     0.06951   |        -54.0833   | NEUTRAL  | Kraken API    |
| QCOM       | 2026-06-29 00:00:00 |   188.72      |        -31.0833   | NEUTRAL  | Yahoo Finance |
| SCHW       | 2026-06-29 00:00:00 |    90.55      |          0.416667 | NEUTRAL  | Yahoo Finance |
| SHY        | 2026-06-29 00:00:00 |    82.17      |         -2.58333  | NEUTRAL  | Yahoo Finance |
| SMH        | 2026-06-29 00:00:00 |   631.98      |         35.5      | NEUTRAL  | Yahoo Finance |
| SNX-USD    | 2026-06-30 00:00:00 |     0.2123    |        -63.5833   | NEUTRAL  | Kraken API    |
| SOL-USD    | 2026-06-30 00:00:00 |    73.99      |         -3.41667  | NEUTRAL  | Kraken API    |
| SOXX       | 2026-06-29 00:00:00 |   614.35      |         35.5      | NEUTRAL  | Yahoo Finance |
| SPY        | 2026-06-29 00:00:00 |   741         |         25.25     | NEUTRAL  | Yahoo Finance |
| SUSHI-USD  | 2026-06-30 00:00:00 |     0.1507    |        -62.5833   | NEUTRAL  | Kraken API    |
| TIA-USD    | 2026-06-30 00:00:00 |     0.3859    |         27.75     | NEUTRAL  | Kraken API    |
| TRX-USD    | 2026-06-30 00:00:00 |     0.318717  |         16.5      | NEUTRAL  | Kraken API    |
| TSLA       | 2026-06-29 00:00:00 |   411.84      |         27.5833   | NEUTRAL  | Yahoo Finance |
| TXN        | 2026-06-29 00:00:00 |   285.48      |        -18.8333   | NEUTRAL  | Yahoo Finance |
| UNI-USD    | 2026-06-30 00:00:00 |     2.8642    |        -23.5      | NEUTRAL  | Kraken API    |
| USO        | 2026-06-29 00:00:00 |   107.08      |        -16.4167   | NEUTRAL  | Yahoo Finance |
| VEA        | 2026-06-29 00:00:00 |    70.92      |         13.5      | NEUTRAL  | Yahoo Finance |
| VIXY       | 2026-06-29 00:00:00 |    21.7       |        -30.6667   | NEUTRAL  | Yahoo Finance |
| VNQ        | 2026-06-29 00:00:00 |    98.15      |         62.8333   | NEUTRAL  | Yahoo Finance |
| VTI        | 2026-06-29 00:00:00 |   367.12      |         23.9167   | NEUTRAL  | Yahoo Finance |
| VWO        | 2026-06-29 00:00:00 |    59.18      |         -4        | NEUTRAL  | Yahoo Finance |
| VZ         | 2026-06-29 00:00:00 |    44.1       |        -28.75     | NEUTRAL  | Yahoo Finance |
| WIF-USD    | 2026-06-30 00:00:00 |     0.1719    |          3.75     | NEUTRAL  | Kraken API    |
| WMT        | 2026-06-29 00:00:00 |   114.6       |        -57.4167   | NEUTRAL  | Yahoo Finance |
| XLB        | 2026-06-29 00:00:00 |    50.66      |         -8.66667  | NEUTRAL  | Yahoo Finance |
| XLE        | 2026-06-29 00:00:00 |    53.58      |        -17.3333   | NEUTRAL  | Yahoo Finance |
| XLI        | 2026-06-29 00:00:00 |   182.76      |         66.1667   | NEUTRAL  | Yahoo Finance |
| XLK        | 2026-06-29 00:00:00 |   185.41      |         25        | NEUTRAL  | Yahoo Finance |
| XLM-USD    | 2026-06-30 00:00:00 |     0.173979  |        -55.5833   | NEUTRAL  | Kraken API    |
| XLP        | 2026-06-29 00:00:00 |    84.37      |         69.4167   | NEUTRAL  | Yahoo Finance |
| XLV        | 2026-06-29 00:00:00 |   160.74      |         55.8333   | NEUTRAL  | Yahoo Finance |
| XLY        | 2026-06-29 00:00:00 |   117.12      |         25.3333   | NEUTRAL  | Yahoo Finance |
| XRP-USD    | 2026-06-30 00:00:00 |     1.04703   |        -60.5833   | NEUTRAL  | Kraken API    |
| YFI-USD    | 2026-06-30 00:00:00 |  1631.4       |        -51.25     | NEUTRAL  | Kraken API    |
| ZEC-USD    | 2026-06-30 00:00:00 |   398.88      |        -24.5833   | NEUTRAL  | Kraken API    |
| ADA-USD    | 2026-06-30 00:00:00 |     0.14382   |        -31        | SHORT    | Kraken API    |
| ADBE       | 2026-06-29 00:00:00 |   206.43      |        -58.9167   | SHORT    | Yahoo Finance |
| ATOM-USD   | 2026-06-30 00:00:00 |     1.5093    |        -53.3333   | SHORT    | Kraken API    |
| BITO       | 2026-06-29 00:00:00 |     8.19      |        -46.25     | SHORT    | Yahoo Finance |
| BTC-USD    | 2026-06-30 00:00:00 | 59725.4       |        -47.25     | SHORT    | Kraken API    |
| COMP-USD   | 2026-06-30 00:00:00 |    15.64      |        -51.3333   | SHORT    | Kraken API    |
| COP        | 2026-06-29 00:00:00 |   104.2       |        -48.0833   | SHORT    | Yahoo Finance |
| CRM        | 2026-06-29 00:00:00 |   157.93      |        -59.4167   | SHORT    | Yahoo Finance |
| CRV-USD    | 2026-06-30 00:00:00 |     0.18983   |        -53.3333   | SHORT    | Kraken API    |
| CVX        | 2026-06-29 00:00:00 |   168.47      |        -48.0833   | SHORT    | Yahoo Finance |
| DOGE-USD   | 2026-06-30 00:00:00 |     0.0723266 |        -51.3333   | SHORT    | Kraken API    |
| DOT-USD    | 2026-06-30 00:00:00 |     0.8172    |        -53.3333   | SHORT    | Kraken API    |
| ETH-USD    | 2026-06-30 00:00:00 |  1590.39      |        -57.25     | SHORT    | Kraken API    |
| FET-USD    | 2026-06-30 00:00:00 |     0.1735    |        -53.3333   | SHORT    | Kraken API    |
| FXI        | 2026-06-29 00:00:00 |    31.71      |        -57.0833   | SHORT    | Yahoo Finance |
| GLD        | 2026-06-29 00:00:00 |   368.58      |        -53.25     | SHORT    | Yahoo Finance |
| HBAR-USD   | 2026-06-30 00:00:00 |     0.07106   |        -49.3333   | SHORT    | Kraken API    |
| IBIT       | 2026-06-29 00:00:00 |    34.18      |        -46.25     | SHORT    | Yahoo Finance |
| INTU       | 2026-06-29 00:00:00 |   266.4       |        -41.5833   | SHORT    | Yahoo Finance |
| MSFT       | 2026-06-29 00:00:00 |   368.57      |        -56.0833   | SHORT    | Yahoo Finance |
| NFLX       | 2026-06-29 00:00:00 |    73.78      |        -52.4167   | SHORT    | Yahoo Finance |
| NOW        | 2026-06-29 00:00:00 |    99.97      |        -53.5833   | SHORT    | Yahoo Finance |
| NVDA       | 2026-06-29 00:00:00 |   194.97      |        -27.8333   | SHORT    | Yahoo Finance |
| ORCL       | 2026-06-29 00:00:00 |   147.76      |        -65.0833   | SHORT    | Yahoo Finance |
| OXY        | 2026-06-29 00:00:00 |    49.09      |        -48.0833   | SHORT    | Yahoo Finance |
| PEPE-USD   | 2026-06-30 00:00:00 |     2.323e-06 |        -53.3333   | SHORT    | Kraken API    |
| RENDER-USD | 2026-06-30 00:00:00 |     1.555     |        -48        | SHORT    | Kraken API    |
| SHIB-USD   | 2026-06-30 00:00:00 |     4.214e-06 |        -51.3333   | SHORT    | Kraken API    |
| SKY-USD    | 2026-06-30 00:00:00 |     0.05231   |        -52.5      | SHORT    | Kraken API    |
| SLB        | 2026-06-29 00:00:00 |    46.38      |        -48.0833   | SHORT    | Yahoo Finance |
| SLV        | 2026-06-29 00:00:00 |    52.68      |        -56.75     | SHORT    | Yahoo Finance |
| T          | 2026-06-29 00:00:00 |    21.82      |        -33.75     | SHORT    | Yahoo Finance |
| TMUS       | 2026-06-29 00:00:00 |   173.97      |        -39.75     | SHORT    | Yahoo Finance |
| XLC        | 2026-06-29 00:00:00 |   107.88      |        -46.5833   | SHORT    | Yahoo Finance |
| XOM        | 2026-06-29 00:00:00 |   136.06      |        -43.8333   | SHORT    | Yahoo Finance |

## Edge Summary

- Symbols with trades: **160** of 160
- Beat buy-and-hold: **36.25%** of traded symbols
- Positive return: **33.75%** of traded symbols
- Median strategy return: **-7.52%** (benchmark **13.66%**)
- Median excess vs benchmark: **-24.69%**
- Median Sharpe: **-0.05**
- Median exposure: **44.51%**

> Edge is real only if both _beat buy-and-hold_ and _median excess_ are convincingly positive across many symbols. Treat a single high-return symbol as noise.

## Portfolio Backtest

Actual capital-allocation books (not per-symbol averages). Benchmarks: `equal_weight_buyhold` (whole tracked universe), `spy_buyhold` (100% SPY), and `sixty_forty` (60% SPY / 40% AGG). `high_conf_voltarget` inverse-vol-weights the HIGH-confidence book; `conviction_long_short` is market-neutral. Judge on **Sharpe** and **max_drawdown** out-of-sample, not raw return: a fully-invested long book wins on return in a bull market but carries all the risk.

| strategy              | scope         | ann_return   | ann_vol   |   sharpe | max_drawdown   | total_return   |   avg_gross_exposure |
|:----------------------|:--------------|:-------------|:----------|---------:|:---------------|:---------------|---------------------:|
| equal_weight_buyhold  | full          | -9.19%       | 33.39%    |    -0.28 | -54.92%        | -36.34%        |                 1    |
| equal_weight_buyhold  | out_of_sample | -12.84%      | 34.20%    |    -0.38 | -39.63%        | -18.07%        |                 1    |
| all_signals_ew        | full          | -9.14%       | 28.15%    |    -0.32 | -59.69%        | -32.94%        |                 1    |
| all_signals_ew        | out_of_sample | 7.15%        | 28.57%    |     0.25 | -22.53%        | 3.37%          |                 1    |
| high_conf_ew          | full          | 5.80%        | 32.19%    |     0.18 | -44.22%        | 2.13%          |                 0.88 |
| high_conf_ew          | out_of_sample | 10.31%       | 35.06%    |     0.29 | -20.80%        | 4.71%          |                 0.88 |
| high_conf_voltarget   | full          | 6.56%        | 29.77%    |     0.22 | -36.20%        | 6.96%          |                 0.88 |
| high_conf_voltarget   | out_of_sample | 6.47%        | 32.76%    |     0.2  | -16.98%        | 1.33%          |                 0.88 |
| conviction_long_short | full          | -11.36%      | 23.48%    |    -0.48 | -39.14%        | -34.99%        |                 0.97 |
| conviction_long_short | out_of_sample | -13.04%      | 26.84%    |    -0.49 | -21.22%        | -16.30%        |                 0.97 |
| spy_buyhold           | full          | 7.27%        | 13.36%    |     0.54 | -17.81%        | 21.46%         |                 0.78 |
| spy_buyhold           | out_of_sample | -5.32%       | 10.10%    |    -0.53 | -14.83%        | -6.03%         |                 0.78 |
| sixty_forty           | full          | 4.37%        | 8.47%     |     0.52 | -10.80%        | 12.98%         |                 0.78 |
| sixty_forty           | out_of_sample | -3.92%       | 6.56%     |    -0.6  | -10.06%        | -4.32%         |                 0.78 |

## Walk-Forward Robustness

Each book measured across contiguous time folds (each a different regime). A book has durable edge only if `mean_sharpe` is positive, `min_sharpe` isn't deeply negative, and `pct_positive_folds` is high — a single great fold doesn't count. `fold_sharpes` lists each fold oldest-to-newest.

| strategy              |   n_folds |   mean_sharpe |   median_sharpe |   min_sharpe | pct_positive_folds   | mean_return   | fold_sharpes                  |
|:----------------------|----------:|--------------:|----------------:|-------------:|:---------------------|:--------------|:------------------------------|
| equal_weight_buyhold  |         5 |          0    |           -0.17 |        -1.38 | 40.00%               | -7.18%        | 1.66;-1.38;0.43;-0.54;-0.17   |
| all_signals_ew        |         5 |         -0.21 |            0.21 |        -1.29 | 60.00%               | -6.79%        | 0.21;0.24;-1.29;-0.78;0.56    |
| high_conf_ew          |         5 |          0.37 |            0.63 |        -1    | 80.00%               | 1.43%         | 1.16;0.63;-1.00;0.36;0.71     |
| high_conf_voltarget   |         5 |          0.51 |            0.5  |        -1.11 | 80.00%               | 2.43%         | 2.06;0.86;-1.11;0.50;0.24     |
| conviction_long_short |         5 |         -0.52 |           -0.47 |        -1.29 | 0.00%                | -8.14%        | -1.29;-0.47;-0.24;-0.56;-0.05 |
| spy_buyhold           |         5 |          0.49 |            0.52 |        -0.41 | 60.00%               | 4.14%         | 1.73;0.81;0.52;-0.19;-0.41    |
| sixty_forty           |         5 |          0.44 |            0.42 |        -0.52 | 60.00%               | 2.56%         | 1.90;0.42;0.58;-0.17;-0.52    |

## Strategy Comparison

Each decision rule backtested over the same data. `out_of_sample` is the most recent ~35% of each symbol's history (unseen tail). A rule has real edge only if `median_excess` and `beat_benchmark_pct` stay positive out-of-sample, not just full-sample.

| strategy        | scope         |   symbols | beat_benchmark_pct   | positive_pct   | median_return   | median_benchmark   | median_excess   |   median_sharpe |   total_trades |
|:----------------|:--------------|----------:|:---------------------|:---------------|:----------------|:-------------------|:----------------|----------------:|---------------:|
| trend           | full          |       160 | 36.25%               | 33.75%         | -7.52%          | 13.66%             | -24.69%         |           -0.05 |          11249 |
| trend           | out_of_sample |       160 | 43.12%               | 53.75%         | 3.66%           | 3.95%              | -5.20%          |            0.34 |           3905 |
| mean_reversion  | full          |       157 | 40.76%               | 49.68%         | -0.03%          | 12.86%             | -16.55%         |            0.01 |           1254 |
| mean_reversion  | out_of_sample |       127 | 48.03%               | 58.27%         | 0.33%           | -0.11%             | -2.43%          |            0.65 |            478 |
| regime_adaptive | full          |       160 | 36.88%               | 35.00%         | -8.55%          | 13.66%             | -25.04%         |           -0.06 |          11516 |
| regime_adaptive | out_of_sample |       160 | 43.12%               | 54.37%         | 3.66%           | 3.95%              | -5.35%          |            0.36 |           4000 |

## Signal Calibration

Realized forward return in the signal's direction, grouped by confidence. HIGH should outrank LOW for the confidence score to be meaningful.

| confidence_level   |   horizon |     n | mean_return   | median_return   | win_rate   |
|:-------------------|----------:|------:|:--------------|:----------------|:-----------|
| HIGH               |         5 |  8078 | 0.18%         | 0.13%           | 52.20%     |
| MEDIUM             |         5 | 29260 | 0.08%         | 0.11%           | 51.20%     |
| LOW                |         5 |  3282 | -0.59%        | -0.51%          | 44.94%     |
| ALL                |         5 | 40620 | 0.05%         | 0.07%           | 50.90%     |
| HIGH               |        10 |  8034 | 0.49%         | 0.17%           | 52.10%     |
| MEDIUM             |        10 | 29096 | 0.26%         | 0.17%           | 51.41%     |
| LOW                |        10 |  3270 | -0.89%        | -0.73%          | 45.29%     |
| ALL                |        10 | 40400 | 0.21%         | 0.12%           | 51.05%     |
| HIGH               |        20 |  7966 | 0.88%         | 0.45%           | 53.54%     |
| MEDIUM             |        20 | 28655 | 0.94%         | 0.66%           | 53.80%     |
| LOW                |        20 |  3230 | -0.63%        | -0.48%          | 47.28%     |
| ALL                |        20 | 39851 | 0.80%         | 0.54%           | 53.22%     |

## Backtest Summary

### Data Quality / Signal Availability

- **ok**: 160 symbols

| symbol     |   trades | return   | benchmark_return   | mdd     |   sharpe | exposure   | skipped_reason   |
|:-----------|---------:|:---------|:-------------------|:--------|---------:|:-----------|:-----------------|
| AAPL       |       63 | 12.31%   | 50.12%             | -20.65% |     0.34 | 48.59%     | ok               |
| AAVE-USD   |       74 | -51.10%  | -72.28%            | -68.26% |    -0.49 | 36.40%     | ok               |
| ABBV       |       64 | -17.54%  | 48.49%             | -30.55% |    -0.36 | 47.59%     | ok               |
| ADA-USD    |       88 | -82.30%  | -85.27%            | -89.12% |    -0.64 | 46.55%     | ok               |
| ADBE       |       68 | -27.04%  | -67.26%            | -37.27% |    -0.31 | 57.40%     | ok               |
| AGG        |       67 | -6.37%   | 1.76%              | -9.93%  |    -1.06 | 30.95%     | ok               |
| ALGO-USD   |       86 | -50.43%  | -78.86%            | -53.13% |    -0.57 | 38.12%     | ok               |
| AMAT       |       69 | -6.20%   | 306.01%            | -57.21% |     0.1  | 53.41%     | ok               |
| AMD        |       56 | 2.97%    | 209.64%            | -44.76% |     0.24 | 36.94%     | ok               |
| AMGN       |       71 | -22.32%  | 11.98%             | -34.14% |    -0.46 | 46.59%     | ok               |
| AMZN       |       78 | -37.42%  | 41.00%             | -42.48% |    -1.11 | 38.60%     | ok               |
| APT-USD    |       76 | -26.57%  | -92.97%            | -69.96% |    -0    | 44.25%     | ok               |
| ARB-USD    |       68 | -0.31%   | -89.19%            | -62.67% |     0.24 | 39.27%     | ok               |
| ARKK       |       79 | -30.02%  | 78.38%             | -32.63% |    -0.5  | 38.94%     | ok               |
| ATOM-USD   |       90 | -65.84%  | -75.61%            | -73.34% |    -1.05 | 45.21%     | ok               |
| AVAX-USD   |       74 | -34.19%  | -81.90%            | -60.45% |    -0.24 | 39.66%     | ok               |
| AVGO       |       62 | 25.50%   | 199.61%            | -35.76% |     0.44 | 44.43%     | ok               |
| BA         |       67 | 7.60%    | 3.90%              | -30.56% |     0.25 | 49.25%     | ok               |
| BAC        |       78 | -11.45%  | 75.45%             | -26.76% |    -0.24 | 47.59%     | ok               |
| BCH-USD    |       78 | -9.24%   | -55.25%            | -54.40% |     0.1  | 49.81%     | ok               |
| BITO       |       78 | 11.39%   | -59.15%            | -42.82% |     0.3  | 41.60%     | ok               |
| BLK        |       75 | -11.50%  | 21.32%             | -24.29% |    -0.28 | 43.43%     | ok               |
| BND        |       65 | -7.32%   | 1.78%              | -9.89%  |    -1.18 | 32.28%     | ok               |
| BONK-USD   |       70 | 70.45%   | -85.62%            | -45.22% |     0.72 | 41.95%     | ok               |
| BTC-USD    |       74 | 8.76%    | -42.96%            | -23.38% |     0.28 | 51.72%     | ok               |
| C          |       83 | -26.35%  | 161.45%            | -38.66% |    -0.5  | 51.75%     | ok               |
| CAT        |       72 | 34.94%   | 221.47%            | -21.02% |     0.62 | 57.07%     | ok               |
| CL         |       60 | 13.29%   | 9.88%              | -14.32% |     0.48 | 46.92%     | ok               |
| CMCSA      |       82 | -38.95%  | -42.41%            | -38.49% |    -1.01 | 44.09%     | ok               |
| COMP-USD   |       91 | -36.81%  | -79.11%            | -58.43% |    -0.21 | 45.98%     | ok               |
| COP        |       73 | -20.72%  | -5.25%             | -43.77% |    -0.36 | 40.60%     | ok               |
| COST       |       60 | 2.02%    | 33.12%             | -29.73% |     0.13 | 45.59%     | ok               |
| CRM        |       67 | -37.76%  | -45.18%            | -40.31% |    -0.78 | 43.59%     | ok               |
| CRV-USD    |       64 | 1.95%    | -76.21%            | -39.89% |     0.25 | 35.44%     | ok               |
| CSCO       |       59 | 26.50%   | 137.73%            | -21.79% |     0.56 | 50.58%     | ok               |
| CVX        |       71 | -13.81%  | 10.60%             | -26.75% |    -0.34 | 41.26%     | ok               |
| DASH-USD   |       63 | -37.83%  | -7.12%             | -64.43% |     0.03 | 31.61%     | ok               |
| DBC        |       58 | -12.57%  | 21.28%             | -25.35% |    -0.43 | 32.78%     | ok               |
| DE         |       72 | -2.31%   | 62.33%             | -25.24% |     0.05 | 46.26%     | ok               |
| DIA        |       60 | -1.70%   | 36.00%             | -12.94% |    -0.05 | 45.76%     | ok               |
| DIS        |       68 | -6.79%   | 2.05%              | -28.17% |    -0.03 | 47.75%     | ok               |
| DOGE-USD   |       78 | -18.64%  | -79.54%            | -62.31% |     0.07 | 50.00%     | ok               |
| DOT-USD    |       92 | -45.76%  | -87.06%            | -61.52% |    -0.32 | 49.04%     | ok               |
| DXY-INDEX  |       44 | -2.00%   | -0.07%             | -6.06%  |    -0.3  | 30.43%     | ok               |
| EEM        |       64 | -9.40%   | 74.24%             | -25.67% |    -0.25 | 43.43%     | ok               |
| EFA        |       62 | -9.39%   | 38.39%             | -14.87% |    -0.35 | 44.59%     | ok               |
| EOG        |       79 | -26.30%  | 20.32%             | -48.13% |    -0.58 | 46.26%     | ok               |
| ETC-USD    |       64 | -35.69%  | -73.96%            | -48.16% |    -0.51 | 31.23%     | ok               |
| ETH-USD    |       62 | 166.33%  | -52.04%            | -30.11% |     1.32 | 45.02%     | ok               |
| EWJ        |       64 | -17.66%  | 40.82%             | -30.73% |    -0.57 | 39.77%     | ok               |
| FCX        |       65 | -28.74%  | 59.31%             | -46.84% |    -0.33 | 45.42%     | ok               |
| FET-USD    |       83 | -13.43%  | -85.63%            | -54.02% |     0.17 | 40.80%     | ok               |
| FIL-USD    |       70 | -33.66%  | -85.41%            | -49.05% |    -0.29 | 33.14%     | ok               |
| FXI        |       46 | -2.13%   | 44.93%             | -24.33% |     0.03 | 29.28%     | ok               |
| GDX        |       60 | 11.28%   | 176.61%            | -34.99% |     0.3  | 48.09%     | ok               |
| GDXJ       |       68 | -23.13%  | 198.49%            | -44.93% |    -0.22 | 46.42%     | ok               |
| GE         |       74 | 25.40%   | 240.03%            | -27.82% |     0.5  | 53.24%     | ok               |
| GLD        |       48 | 28.53%   | 96.50%             | -16.63% |     0.71 | 45.76%     | ok               |
| GOOGL      |       63 | 77.91%   | 146.14%            | -20.41% |     1.16 | 53.74%     | ok               |
| GRT-USD    |       85 | -3.45%   | -90.27%            | -54.83% |     0.19 | 42.72%     | ok               |
| GS         |       76 | -2.38%   | 166.36%            | -22.13% |     0.05 | 52.08%     | ok               |
| HD         |       73 | -4.53%   | -1.22%             | -18.58% |    -0.04 | 43.43%     | ok               |
| HON        |       95 | -27.07%  | 19.11%             | -29.77% |    -0.73 | 52.58%     | ok               |
| HYG        |       81 | -9.52%   | 4.14%              | -9.59%  |    -1.11 | 34.28%     | ok               |
| IBIT       |       32 | 41.12%   | -10.08%            | -18.95% |     0.83 | 31.82%     | ok               |
| IBM        |       76 | 1.60%    | 51.56%             | -27.54% |     0.13 | 49.92%     | ok               |
| ICP-USD    |       85 | -3.65%   | -76.53%            | -57.53% |     0.23 | 38.89%     | ok               |
| IEF        |       76 | -10.90%  | 0.45%              | -11.70% |    -1.54 | 32.78%     | ok               |
| IEMG       |       58 | -5.52%   | 67.39%             | -26.84% |    -0.12 | 43.59%     | ok               |
| INJ-USD    |       77 | -51.75%  | -77.42%            | -76.97% |    -0.47 | 38.51%     | ok               |
| INTC       |       70 | 55.82%   | 207.97%            | -60.60% |     0.62 | 49.25%     | ok               |
| INTU       |       67 | -15.56%  | -58.41%            | -43.77% |    -0.15 | 42.60%     | ok               |
| ITA        |       74 | -1.46%   | 94.13%             | -23.75% |     0.03 | 47.59%     | ok               |
| IWM        |       48 | 9.40%    | 55.76%             | -12.83% |     0.39 | 35.77%     | ok               |
| JNJ        |       72 | 5.41%    | 65.92%             | -17.51% |     0.25 | 50.25%     | ok               |
| JPM        |       73 | -18.71%  | 88.76%             | -33.16% |    -0.44 | 53.58%     | ok               |
| KO         |       49 | 28.93%   | 37.66%             | -8.07%  |     1.03 | 37.77%     | ok               |
| LDO-USD    |       74 | 1.95%    | -87.45%            | -60.93% |     0.29 | 37.93%     | ok               |
| LIN        |       64 | 0.44%    | 27.56%             | -21.53% |     0.08 | 38.60%     | ok               |
| LINK-USD   |       69 | -11.40%  | -70.78%            | -49.35% |     0.12 | 41.57%     | ok               |
| LLY        |       71 | -19.51%  | 74.16%             | -53.34% |    -0.22 | 51.25%     | ok               |
| LRCX       |       82 | -5.51%   | 382.67%            | -63.39% |     0.11 | 46.09%     | ok               |
| LTC-USD    |       66 | -34.00%  | -65.62%            | -53.76% |    -0.29 | 48.47%     | ok               |
| MCD        |       75 | -2.55%   | -6.57%             | -18.81% |    -0.05 | 38.10%     | ok               |
| META       |       72 | -27.00%  | 22.46%             | -38.96% |    -0.44 | 49.58%     | ok               |
| MPC        |       71 | -13.74%  | 51.48%             | -44.76% |    -0.14 | 49.92%     | ok               |
| MRK        |       67 | -30.11%  | 2.54%              | -34.46% |    -0.73 | 45.59%     | ok               |
| MS         |       79 | -17.22%  | 146.50%            | -27.79% |    -0.36 | 49.58%     | ok               |
| MSFT       |       83 | -33.20%  | -9.14%             | -38.02% |    -0.84 | 48.09%     | ok               |
| MU         |       51 | 270.20%  | 1216.72%           | -68.76% |     1.34 | 59.90%     | ok               |
| NEAR-USD   |       89 | -6.29%   | -62.86%            | -61.22% |     0.2  | 42.34%     | ok               |
| NEM        |       74 | -31.65%  | 183.30%            | -38.49% |    -0.34 | 53.91%     | ok               |
| NFLX       |       62 | 37.66%   | 31.27%             | -21.09% |     0.78 | 54.74%     | ok               |
| NKE        |       91 | -37.83%  | -58.39%            | -55.35% |    -0.53 | 43.76%     | ok               |
| NOW        |       80 | 15.47%   | -36.31%            | -30.25% |     0.35 | 45.92%     | ok               |
| NVDA       |       76 | -25.95%  | 119.16%            | -45.02% |    -0.18 | 58.29%     | ok               |
| OP-USD     |       74 | -1.17%   | -93.92%            | -70.27% |     0.24 | 35.44%     | ok               |
| ORCL       |       74 | 84.52%   | 26.95%             | -29.47% |     0.81 | 53.58%     | ok               |
| OXY        |       65 | 9.71%    | -13.85%            | -30.43% |     0.28 | 43.26%     | ok               |
| PEP        |       83 | -7.73%   | -18.86%            | -21.35% |    -0.16 | 49.92%     | ok               |
| PEPE-USD   |       79 | 22.01%   | -84.55%            | -57.66% |     0.45 | 44.25%     | ok               |
| PFE        |       77 | -41.43%  | -8.28%             | -40.87% |    -1.35 | 35.11%     | ok               |
| PG         |       62 | -13.39%  | -6.17%             | -21.65% |    -0.48 | 41.43%     | ok               |
| PM         |       85 | -2.25%   | 99.57%             | -33.68% |     0.05 | 57.57%     | ok               |
| POL-USD    |       81 | 84.54%   | -84.05%            | -46.45% |     0.89 | 51.34%     | ok               |
| QCOM       |       75 | -10.63%  | 31.03%             | -56.59% |     0.03 | 46.92%     | ok               |
| QQQ        |       62 | 17.84%   | 69.00%             | -12.88% |     0.52 | 45.26%     | ok               |
| RENDER-USD |       98 | -16.89%  | -62.62%            | -45.00% |     0.12 | 43.84%     | ok               |
| RTX        |       58 | 18.66%   | 103.09%            | -16.99% |     0.51 | 51.58%     | ok               |
| SBUX       |       64 | -22.59%  | 12.49%             | -29.34% |    -0.45 | 39.60%     | ok               |
| SCHW       |       76 | -24.21%  | 45.18%             | -31.92% |    -0.58 | 45.92%     | ok               |
| SHIB-USD   |       78 | -22.62%  | -78.86%            | -47.96% |    -0.06 | 53.07%     | ok               |
| SHY        |       48 | -2.24%   | 0.50%              | -2.85%  |    -0.79 | 34.28%     | ok               |
| SKY-USD    |       70 | -28.82%  | -9.55%             | -43.98% |    -0.35 | 41.32%     | ok               |
| SLB        |       77 | -25.16%  | -4.47%             | -55.49% |    -0.43 | 50.08%     | ok               |
| SLV        |       58 | 50.68%   | 157.35%            | -42.66% |     0.7  | 41.43%     | ok               |
| SMH        |       48 | 91.75%   | 224.18%            | -33.99% |     1.17 | 49.75%     | ok               |
| SNX-USD    |       62 | -6.01%   | -86.68%            | -34.76% |     0.19 | 39.27%     | ok               |
| SOL-USD    |       68 | -43.05%  | -71.12%            | -56.90% |    -0.23 | 59.77%     | ok               |
| SOXX       |       55 | 84.13%   | 204.83%            | -40.34% |     1.05 | 48.75%     | ok               |
| SPY        |       62 | 4.36%    | 50.44%             | -16.47% |     0.21 | 50.42%     | ok               |
| SUSHI-USD  |       90 | -79.45%  | -88.55%            | -84.18% |    -1.18 | 35.63%     | ok               |
| T          |       62 | 38.33%   | 23.07%             | -17.01% |     0.87 | 51.58%     | ok               |
| TGT        |       56 | -10.02%  | -5.91%             | -40.57% |    -0.12 | 38.44%     | ok               |
| TIA-USD    |       88 | -29.83%  | -91.50%            | -62.78% |    -0.08 | 35.44%     | ok               |
| TLT        |       70 | -19.42%  | -7.10%             | -20.85% |    -1.51 | 31.28%     | ok               |
| TMO        |       61 | 10.27%   | -8.19%             | -18.11% |     0.31 | 48.25%     | ok               |
| TMUS       |       68 | 15.42%   | 7.38%              | -24.50% |     0.41 | 47.59%     | ok               |
| TRX-USD    |       74 | -4.49%   | 25.74%             | -22.90% |    -0.03 | 49.62%     | ok               |
| TSLA       |       67 | 16.71%   | 127.46%            | -42.22% |     0.36 | 41.76%     | ok               |
| TXN        |       77 | -15.83%  | 79.66%             | -46.98% |    -0.1  | 53.41%     | ok               |
| UNH        |       76 | 26.31%   | -16.53%            | -27.86% |     0.48 | 52.41%     | ok               |
| UNI-USD    |       88 | -72.81%  | -76.29%            | -80.61% |    -0.89 | 41.76%     | ok               |
| UPS        |       72 | -39.46%  | -22.34%            | -38.76% |    -0.81 | 40.27%     | ok               |
| USO        |       66 | 8.43%    | 57.05%             | -43.35% |     0.26 | 34.11%     | ok               |
| VEA        |       58 | -0.98%   | 50.16%             | -17.93% |     0.01 | 44.09%     | ok               |
| VIXY       |       96 | -80.03%  | -62.25%            | -88.16% |    -1    | 32.28%     | ok               |
| VNQ        |       75 | -16.77%  | 18.85%             | -24.92% |    -0.7  | 37.60%     | ok               |
| VTI        |       66 | -0.60%   | 50.45%             | -18.77% |     0.04 | 51.25%     | ok               |
| VWO        |       76 | -13.41%  | 48.96%             | -25.20% |    -0.47 | 44.09%     | ok               |
| VZ         |       87 | -29.67%  | 6.57%              | -29.58% |    -1.02 | 37.10%     | ok               |
| WFC        |       84 | -19.43%  | 71.48%             | -29.78% |    -0.34 | 48.92%     | ok               |
| WIF-USD    |       68 | -43.81%  | -86.55%            | -57.06% |    -0.24 | 32.18%     | ok               |
| WMT        |       59 | 20.63%   | 103.84%            | -21.31% |     0.59 | 51.08%     | ok               |
| XBI        |       62 | 5.32%    | 79.06%             | -19.90% |     0.21 | 40.43%     | ok               |
| XLB        |       66 | -10.84%  | 25.12%             | -26.57% |    -0.36 | 37.10%     | ok               |
| XLC        |       65 | 15.42%   | 37.22%             | -12.33% |     0.54 | 55.57%     | ok               |
| XLE        |       73 | -11.37%  | 28.63%             | -37.51% |    -0.22 | 46.76%     | ok               |
| XLF        |       76 | -11.26%  | 38.63%             | -23.61% |    -0.37 | 48.25%     | ok               |
| XLI        |       64 | 3.69%    | 58.99%             | -11.38% |     0.2  | 45.76%     | ok               |
| XLK        |       42 | 63.94%   | 82.94%             | -14.75% |     1.19 | 47.25%     | ok               |
| XLM-USD    |       69 | 0.26%    | -58.28%            | -50.36% |     0.22 | 45.59%     | ok               |
| XLP        |       68 | 6.56%    | 14.46%             | -11.16% |     0.4  | 42.93%     | ok               |
| XLU        |       67 | -3.67%   | 52.86%             | -18.15% |    -0.13 | 37.94%     | ok               |
| XLV        |       66 | -12.12%  | 12.86%             | -16.83% |    -0.59 | 35.61%     | ok               |
| XLY        |       72 | 2.75%    | 33.99%             | -14.01% |     0.15 | 44.26%     | ok               |
| XOM        |       58 | 4.90%    | 33.98%             | -20.29% |     0.21 | 36.61%     | ok               |
| XRP-USD    |       62 | -32.98%  | -66.31%            | -44.90% |    -0.31 | 34.48%     | ok               |
| YFI-USD    |       81 | -52.55%  | -78.41%            | -67.78% |    -0.75 | 40.80%     | ok               |
| ZEC-USD    |       65 | 55.36%   | 759.47%            | -47.68% |     0.61 | 36.59%     | ok               |

## AAPL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 23.22%   | 50.12%             | -21.71% |     0.52 |       67 | 52.58%     | ok               |
|          15 | 19.43%   | 50.12%             | -23.86% |     0.45 |       74 | 59.73%     | ok               |
|          25 | 17.33%   | 50.12%             | -20.03% |     0.43 |       65 | 50.42%     | ok               |
|          30 | 12.31%   | 50.12%             | -20.65% |     0.34 |       63 | 48.59%     | ok               |
|          35 | 7.94%    | 50.12%             | -22.04% |     0.26 |       61 | 46.59%     | ok               |

## AAVE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 13.21%   | -72.28%            | -43.61% |     0.35 |       38 | 29.69%     | ok               |
|          45 | 4.78%    | -72.28%            | -46.87% |     0.26 |       38 | 25.67%     | ok               |
|          35 | -6.88%   | -72.28%            | -51.96% |     0.14 |       50 | 32.38%     | ok               |
|          50 | -29.26%  | -72.28%            | -43.73% |    -0.28 |       42 | 19.54%     | ok               |
|          15 | -52.08%  | -72.28%            | -61.76% |    -0.34 |       80 | 50.57%     | ok               |

## ABBV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -1.91%   | 48.49%             | -23.85% |     0.03 |       50 | 37.10%     | ok               |
|          40 | -14.12%  | 48.49%             | -26.61% |    -0.29 |       64 | 41.93%     | ok               |
|          35 | -15.35%  | 48.49%             | -27.83% |    -0.32 |       66 | 44.76%     | ok               |
|          30 | -17.54%  | 48.49%             | -30.55% |    -0.36 |       64 | 47.59%     | ok               |
|          45 | -16.80%  | 48.49%             | -29.59% |    -0.38 |       54 | 39.27%     | ok               |

## ADA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -80.86%  | -85.27%            | -91.37% |    -0.47 |       80 | 63.22%     | ok               |
|          20 | -82.36%  | -85.27%            | -91.89% |    -0.55 |       90 | 57.47%     | ok               |
|          50 | -77.92%  | -85.27%            | -85.97% |    -0.59 |       55 | 26.82%     | ok               |
|          45 | -80.28%  | -85.27%            | -88.02% |    -0.62 |       58 | 31.61%     | ok               |
|          25 | -83.88%  | -85.27%            | -91.94% |    -0.63 |       83 | 53.64%     | ok               |

## ADBE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 4.41%    | -67.26%            | -21.34% |     0.2  |       78 | 49.75%     | ok               |
|          25 | -12.55%  | -67.26%            | -30.47% |    -0.04 |       52 | 61.56%     | ok               |
|          40 | -9.07%   | -67.26%            | -20.88% |    -0.05 |       74 | 42.76%     | ok               |
|          15 | -21.88%  | -67.26%            | -31.45% |    -0.19 |       63 | 66.22%     | ok               |
|          20 | -23.41%  | -67.26%            | -33.63% |    -0.22 |       52 | 63.73%     | ok               |

## AGG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -6.37%   | 1.76%              | -9.93%  |    -1.06 |       67 | 30.95%     | ok               |
|          20 | -7.76%   | 1.76%              | -10.85% |    -1.14 |       71 | 36.44%     | ok               |
|          45 | -5.75%   | 1.76%              | -7.89%  |    -1.16 |       52 | 20.47%     | ok               |
|          25 | -7.94%   | 1.76%              | -11.38% |    -1.22 |       71 | 34.78%     | ok               |
|          50 | -5.57%   | 1.76%              | -7.92%  |    -1.25 |       46 | 16.97%     | ok               |

## ALGO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -50.43%  | -78.86%            | -53.13% |    -0.57 |       86 | 38.12%     | ok               |
|          15 | -61.07%  | -78.86%            | -69.47% |    -0.66 |       88 | 50.57%     | ok               |
|          25 | -61.32%  | -78.86%            | -73.33% |    -0.72 |       88 | 45.21%     | ok               |
|          20 | -65.02%  | -78.86%            | -72.09% |    -0.78 |       90 | 48.28%     | ok               |
|          50 | -45.64%  | -78.86%            | -48.43% |    -0.81 |       42 | 16.86%     | ok               |

## AMAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 12.08%   | 306.01%            | -54.05% |     0.32 |       66 | 62.06%     | ok               |
|          30 | -6.20%   | 306.01%            | -57.21% |     0.1  |       69 | 53.41%     | ok               |
|          20 | -13.05%  | 306.01%            | -60.16% |     0.03 |       72 | 58.57%     | ok               |
|          50 | -10.67%  | 306.01%            | -48.72% |     0.02 |       52 | 39.27%     | ok               |
|          35 | -12.87%  | 306.01%            | -55.26% |     0.01 |       71 | 51.25%     | ok               |

## AMD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 2.97%    | 209.64%            | -44.76% |     0.24 |       56 | 36.94%     | ok               |
|          50 | 1.16%    | 209.64%            | -44.99% |     0.21 |       60 | 31.28%     | ok               |
|          35 | -10.15%  | 209.64%            | -54.16% |     0.11 |       62 | 38.94%     | ok               |
|          45 | -17.73%  | 209.64%            | -53.82% |     0    |       64 | 34.28%     | ok               |
|          30 | -22.00%  | 209.64%            | -59.51% |    -0.02 |       63 | 41.43%     | ok               |

## AMGN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -17.19%  | 11.98%             | -26.64% |    -0.3  |       73 | 52.75%     | ok               |
|          15 | -20.27%  | 11.98%             | -27.92% |    -0.35 |       71 | 58.57%     | ok               |
|          35 | -18.51%  | 11.98%             | -31.23% |    -0.36 |       67 | 42.76%     | ok               |
|          30 | -22.32%  | 11.98%             | -34.14% |    -0.46 |       71 | 46.59%     | ok               |
|          25 | -25.48%  | 11.98%             | -33.41% |    -0.54 |       67 | 48.92%     | ok               |

## AMZN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -19.23%  | 41.00%             | -28.70% |    -0.56 |       52 | 29.78%     | ok               |
|          50 | -24.37%  | 41.00%             | -35.48% |    -0.85 |       48 | 23.96%     | ok               |
|          45 | -27.16%  | 41.00%             | -35.47% |    -0.93 |       52 | 26.96%     | ok               |
|          35 | -31.33%  | 41.00%             | -38.29% |    -0.97 |       66 | 33.11%     | ok               |
|          30 | -37.42%  | 41.00%             | -42.48% |    -1.11 |       78 | 38.60%     | ok               |

## APT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 51.21%   | -92.97%            | -46.73% |     0.73 |       44 | 20.69%     | ok               |
|          45 | 14.97%   | -92.97%            | -63.86% |     0.37 |       60 | 26.82%     | ok               |
|          40 | -7.11%   | -92.97%            | -63.33% |     0.16 |       66 | 32.38%     | ok               |
|          20 | -13.80%  | -92.97%            | -70.51% |     0.16 |       73 | 52.87%     | ok               |
|          35 | -13.92%  | -92.97%            | -64.45% |     0.11 |       70 | 38.12%     | ok               |

## ARB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 72.02%   | -89.19%            | -53.74% |     0.72 |       87 | 56.70%     | ok               |
|          40 | 45.76%   | -89.19%            | -47.60% |     0.62 |       50 | 30.27%     | ok               |
|          35 | 31.50%   | -89.19%            | -56.00% |     0.51 |       60 | 33.72%     | ok               |
|          20 | 29.27%   | -89.19%            | -60.40% |     0.5  |       75 | 50.19%     | ok               |
|          45 | 24.86%   | -89.19%            | -50.83% |     0.46 |       56 | 23.37%     | ok               |

## ARKK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -24.32%  | 78.38%             | -34.75% |    -0.28 |       90 | 50.25%     | ok               |
|          20 | -28.79%  | 78.38%             | -34.66% |    -0.4  |       85 | 45.59%     | ok               |
|          30 | -30.02%  | 78.38%             | -32.63% |    -0.5  |       79 | 38.94%     | ok               |
|          35 | -31.21%  | 78.38%             | -33.79% |    -0.56 |       78 | 36.61%     | ok               |
|          40 | -32.66%  | 78.38%             | -34.78% |    -0.64 |       70 | 31.78%     | ok               |

## ATOM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -61.73%  | -75.61%            | -69.81% |    -0.85 |       93 | 51.53%     | ok               |
|          15 | -66.98%  | -75.61%            | -71.82% |    -0.93 |       93 | 60.92%     | ok               |
|          45 | -55.95%  | -75.61%            | -63.84% |    -0.97 |       76 | 29.50%     | ok               |
|          30 | -65.84%  | -75.61%            | -73.34% |    -1.05 |       90 | 45.21%     | ok               |
|          20 | -70.45%  | -75.61%            | -74.51% |    -1.09 |      101 | 55.17%     | ok               |

## AVAX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 15.04%   | -81.90%            | -34.50% |     0.37 |       38 | 19.54%     | ok               |
|          45 | 4.12%    | -81.90%            | -41.07% |     0.23 |       40 | 23.56%     | ok               |
|          15 | -3.41%   | -81.90%            | -52.46% |     0.22 |       65 | 53.83%     | ok               |
|          40 | -10.50%  | -81.90%            | -47.98% |     0.04 |       46 | 26.63%     | ok               |
|          25 | -16.70%  | -81.90%            | -52.93% |     0.04 |       73 | 44.44%     | ok               |

## AVGO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 25.50%   | 199.61%            | -35.76% |     0.44 |       62 | 44.43%     | ok               |
|          25 | 21.04%   | 199.61%            | -38.01% |     0.4  |       66 | 45.09%     | ok               |
|          35 | 19.43%   | 199.61%            | -36.19% |     0.38 |       70 | 41.60%     | ok               |
|          40 | 19.03%   | 199.61%            | -40.70% |     0.38 |       60 | 38.44%     | ok               |
|          50 | 13.14%   | 199.61%            | -35.84% |     0.32 |       62 | 32.28%     | ok               |

## BA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 26.03%   | 3.90%              | -13.34% |     0.67 |       42 | 31.45%     | ok               |
|          35 | 30.46%   | 3.90%              | -23.77% |     0.59 |       72 | 44.59%     | ok               |
|          40 | 20.11%   | 3.90%              | -23.90% |     0.47 |       46 | 38.60%     | ok               |
|          25 | 10.59%   | 3.90%              | -32.48% |     0.29 |       70 | 52.58%     | ok               |
|          30 | 7.60%    | 3.90%              | -30.56% |     0.25 |       67 | 49.25%     | ok               |

## BAC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -4.42%   | 75.45%             | -22.31% |    -0.08 |       60 | 36.77%     | ok               |
|          20 | -7.66%   | 75.45%             | -22.24% |    -0.1  |       82 | 52.25%     | ok               |
|          35 | -6.76%   | 75.45%             | -28.27% |    -0.13 |       70 | 43.76%     | ok               |
|          50 | -5.98%   | 75.45%             | -20.84% |    -0.14 |       58 | 33.61%     | ok               |
|          25 | -10.28%  | 75.45%             | -26.26% |    -0.2  |       80 | 50.25%     | ok               |

## BCH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -9.24%   | -55.25%            | -54.40% |     0.1  |       78 | 49.81%     | ok               |
|          15 | -14.50%  | -55.25%            | -58.01% |     0.09 |       76 | 60.34%     | ok               |
|          20 | -19.73%  | -55.25%            | -59.67% |     0.02 |       72 | 56.32%     | ok               |
|          40 | -20.29%  | -55.25%            | -61.24% |    -0.07 |       69 | 40.61%     | ok               |
|          25 | -28.96%  | -55.25%            | -64.31% |    -0.11 |       73 | 52.11%     | ok               |

## BITO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 21.07%   | -59.15%            | -32.29% |     0.41 |       54 | 25.96%     | ok               |
|          30 | 11.39%   | -59.15%            | -42.82% |     0.3  |       78 | 41.60%     | ok               |
|          15 | 4.40%    | -59.15%            | -48.38% |     0.25 |       87 | 50.42%     | ok               |
|          25 | 2.58%    | -59.15%            | -41.73% |     0.21 |       82 | 44.59%     | ok               |
|          45 | 1.27%    | -59.15%            | -43.53% |     0.17 |       60 | 29.28%     | ok               |

## BLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -5.80%   | 21.32%             | -21.48% |    -0.09 |       80 | 47.59%     | ok               |
|          35 | -5.42%   | 21.32%             | -17.97% |    -0.1  |       82 | 39.77%     | ok               |
|          40 | -7.21%   | 21.32%             | -20.08% |    -0.18 |       74 | 35.44%     | ok               |
|          25 | -10.52%  | 21.32%             | -23.36% |    -0.24 |       75 | 45.59%     | ok               |
|          30 | -11.50%  | 21.32%             | -24.29% |    -0.28 |       75 | 43.43%     | ok               |

## BND Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.45%   | 1.78%              | -9.32%  |    -0.94 |       63 | 37.94%     | ok               |
|          25 | -7.14%   | 1.78%              | -10.40% |    -1.09 |       67 | 35.94%     | ok               |
|          30 | -7.32%   | 1.78%              | -9.89%  |    -1.18 |       65 | 32.28%     | ok               |
|          15 | -8.65%   | 1.78%              | -10.85% |    -1.25 |       73 | 40.77%     | ok               |
|          45 | -7.22%   | 1.78%              | -9.57%  |    -1.39 |       50 | 22.13%     | ok               |

## BONK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 169.29%  | -85.62%            | -35.57% |     1.24 |       44 | 22.03%     | ok               |
|          45 | 121.76%  | -85.62%            | -42.36% |     1.02 |       54 | 26.25%     | ok               |
|          25 | 155.05%  | -85.62%            | -47.99% |     1    |       65 | 48.28%     | ok               |
|          40 | 122.45%  | -85.62%            | -50.07% |     0.97 |       50 | 33.33%     | ok               |
|          20 | 140.65%  | -85.62%            | -55.43% |     0.95 |       66 | 52.87%     | ok               |

## BTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 58.01%   | -42.96%            | -14.50% |     1.03 |       46 | 34.10%     | ok               |
|          45 | 45.84%   | -42.96%            | -13.36% |     0.88 |       44 | 30.46%     | ok               |
|          35 | 36.95%   | -42.96%            | -22.12% |     0.71 |       70 | 41.19%     | ok               |
|          50 | 18.09%   | -42.96%            | -16.15% |     0.48 |       40 | 25.10%     | ok               |
|          30 | 20.50%   | -42.96%            | -21.75% |     0.46 |       74 | 47.89%     | ok               |

## C Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -6.79%   | 161.45%            | -22.28% |    -0.11 |       66 | 36.61%     | ok               |
|          45 | -13.73%  | 161.45%            | -28.12% |    -0.29 |       78 | 40.60%     | ok               |
|          15 | -22.99%  | 161.45%            | -35.02% |    -0.38 |       74 | 60.23%     | ok               |
|          25 | -22.99%  | 161.45%            | -35.86% |    -0.41 |       73 | 53.74%     | ok               |
|          40 | -19.83%  | 161.45%            | -33.20% |    -0.43 |       82 | 43.09%     | ok               |

## CAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 34.94%   | 221.47%            | -21.02% |     0.62 |       72 | 57.07%     | ok               |
|          25 | 35.07%   | 221.47%            | -26.37% |     0.61 |       68 | 59.90%     | ok               |
|          20 | 32.33%   | 221.47%            | -25.65% |     0.58 |       78 | 63.23%     | ok               |
|          45 | 23.29%   | 221.47%            | -28.85% |     0.49 |       58 | 45.92%     | ok               |
|          15 | 22.07%   | 221.47%            | -30.60% |     0.45 |       71 | 69.22%     | ok               |

## CL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 13.79%   | 9.88%              | -12.98% |     0.59 |       42 | 30.95%     | ok               |
|          30 | 13.29%   | 9.88%              | -14.32% |     0.48 |       60 | 46.92%     | ok               |
|          45 | 8.59%    | 9.88%              | -13.51% |     0.38 |       46 | 33.94%     | ok               |
|          35 | 7.90%    | 9.88%              | -13.83% |     0.32 |       62 | 43.26%     | ok               |
|          40 | 4.77%    | 9.88%              | -12.70% |     0.23 |       56 | 37.94%     | ok               |

## CMCSA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -37.55%  | -42.41%            | -46.38% |    -0.84 |       87 | 58.74%     | ok               |
|          30 | -38.95%  | -42.41%            | -38.49% |    -1.01 |       82 | 44.09%     | ok               |
|          25 | -44.23%  | -42.41%            | -43.64% |    -1.18 |       89 | 49.42%     | ok               |
|          50 | -30.95%  | -42.41%            | -31.36% |    -1.21 |       50 | 15.64%     | ok               |
|          20 | -48.27%  | -42.41%            | -47.73% |    -1.29 |       93 | 54.74%     | ok               |

## COMP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -4.01%   | -79.11%            | -38.71% |     0.15 |       48 | 20.88%     | ok               |
|          25 | -37.96%  | -79.11%            | -60.58% |    -0.19 |       89 | 50.96%     | ok               |
|          30 | -36.81%  | -79.11%            | -58.43% |    -0.21 |       91 | 45.98%     | ok               |
|          15 | -46.20%  | -79.11%            | -65.55% |    -0.28 |      103 | 62.45%     | ok               |
|          40 | -41.23%  | -79.11%            | -47.89% |    -0.37 |       76 | 34.10%     | ok               |

## COP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -11.98%  | -5.25%             | -35.08% |    -0.2  |       50 | 27.45%     | ok               |
|          45 | -17.74%  | -5.25%             | -41.35% |    -0.35 |       60 | 30.28%     | ok               |
|          35 | -20.18%  | -5.25%             | -43.58% |    -0.35 |       75 | 37.44%     | ok               |
|          30 | -20.72%  | -5.25%             | -43.77% |    -0.36 |       73 | 40.60%     | ok               |
|          40 | -23.84%  | -5.25%             | -47.05% |    -0.5  |       70 | 33.28%     | ok               |

## COST Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 13.85%   | 33.12%             | -24.32% |     0.44 |       66 | 52.08%     | ok               |
|          25 | 12.13%   | 33.12%             | -24.73% |     0.4  |       63 | 49.25%     | ok               |
|          35 | 6.92%    | 33.12%             | -26.58% |     0.28 |       54 | 42.60%     | ok               |
|          30 | 2.02%    | 33.12%             | -29.73% |     0.13 |       60 | 45.59%     | ok               |
|          40 | 0.35%    | 33.12%             | -28.41% |     0.08 |       56 | 39.60%     | ok               |

## CRM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -33.05%  | -45.18%            | -41.65% |    -0.5  |       92 | 55.41%     | ok               |
|          35 | -27.54%  | -45.18%            | -35.48% |    -0.53 |       64 | 38.77%     | ok               |
|          30 | -37.76%  | -45.18%            | -40.31% |    -0.78 |       67 | 43.59%     | ok               |
|          40 | -34.08%  | -45.18%            | -41.30% |    -0.78 |       70 | 34.94%     | ok               |
|          20 | -42.92%  | -45.18%            | -43.99% |    -0.82 |       80 | 49.08%     | ok               |

## CRV-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 28.38%   | -76.21%            | -37.78% |     0.49 |       66 | 30.84%     | ok               |
|          50 | 11.52%   | -76.21%            | -29.30% |     0.32 |       44 | 17.24%     | ok               |
|          45 | 8.28%    | -76.21%            | -42.29% |     0.29 |       54 | 20.50%     | ok               |
|          30 | 1.95%    | -76.21%            | -39.89% |     0.25 |       64 | 35.44%     | ok               |
|          40 | 2.24%    | -76.21%            | -38.86% |     0.23 |       58 | 26.82%     | ok               |

## CSCO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 33.52%   | 137.73%            | -19.34% |     0.72 |       56 | 38.77%     | ok               |
|          45 | 31.32%   | 137.73%            | -19.34% |     0.67 |       51 | 41.43%     | ok               |
|          25 | 27.09%   | 137.73%            | -23.28% |     0.57 |       63 | 52.58%     | ok               |
|          35 | 26.49%   | 137.73%            | -23.68% |     0.56 |       51 | 48.09%     | ok               |
|          30 | 26.50%   | 137.73%            | -21.79% |     0.56 |       59 | 50.58%     | ok               |

## CVX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -11.78%  | 10.60%             | -26.07% |    -0.25 |       73 | 45.42%     | ok               |
|          25 | -12.16%  | 10.60%             | -25.65% |    -0.26 |       77 | 44.26%     | ok               |
|          45 | -11.58%  | 10.60%             | -28.32% |    -0.32 |       61 | 30.62%     | ok               |
|          30 | -13.81%  | 10.60%             | -26.75% |    -0.34 |       71 | 41.26%     | ok               |
|          35 | -13.56%  | 10.60%             | -27.83% |    -0.34 |       71 | 38.27%     | ok               |

## DASH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 129.69%  | -7.12%             | -31.38% |     0.96 |       40 | 17.05%     | ok               |
|          40 | 75.62%   | -7.12%             | -34.44% |     0.72 |       46 | 23.75%     | ok               |
|          45 | 65.87%   | -7.12%             | -39.58% |     0.68 |       44 | 19.35%     | ok               |
|          25 | -32.35%  | -7.12%             | -64.14% |     0.1  |       69 | 34.48%     | ok               |
|          35 | -32.14%  | -7.12%             | -63.23% |     0.09 |       69 | 28.16%     | ok               |

## DBC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -10.12%  | 21.28%             | -27.30% |    -0.31 |       71 | 37.60%     | ok               |
|          35 | -9.68%   | 21.28%             | -23.38% |    -0.31 |       60 | 31.61%     | ok               |
|          50 | -8.54%   | 21.28%             | -19.91% |    -0.32 |       42 | 21.13%     | ok               |
|          45 | -9.90%   | 21.28%             | -21.08% |    -0.35 |       54 | 24.46%     | ok               |
|          30 | -12.57%  | 21.28%             | -25.35% |    -0.43 |       58 | 32.78%     | ok               |

## DE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -1.40%   | 62.33%             | -28.94% |     0.07 |       72 | 51.58%     | ok               |
|          30 | -2.31%   | 62.33%             | -25.24% |     0.05 |       72 | 46.26%     | ok               |
|          25 | -3.84%   | 62.33%             | -26.67% |     0.02 |       74 | 48.92%     | ok               |
|          50 | -3.01%   | 62.33%             | -23.65% |    -0    |       68 | 31.28%     | ok               |
|          45 | -4.55%   | 62.33%             | -26.94% |    -0.03 |       68 | 35.61%     | ok               |

## DIA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 0.38%    | 36.00%             | -13.15% |     0.06 |       60 | 43.59%     | ok               |
|          25 | -0.16%   | 36.00%             | -11.28% |     0.03 |       60 | 46.92%     | ok               |
|          30 | -1.70%   | 36.00%             | -12.94% |    -0.05 |       60 | 45.76%     | ok               |
|          20 | -3.58%   | 36.00%             | -13.85% |    -0.14 |       64 | 49.25%     | ok               |
|          40 | -3.68%   | 36.00%             | -15.06% |    -0.18 |       66 | 40.93%     | ok               |

## DIS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 33.43%   | 2.05%              | -14.24% |     0.84 |       50 | 29.62%     | ok               |
|          45 | 5.58%    | 2.05%              | -16.54% |     0.22 |       53 | 33.28%     | ok               |
|          40 | 4.63%    | 2.05%              | -22.77% |     0.2  |       65 | 38.44%     | ok               |
|          35 | -2.31%   | 2.05%              | -25.70% |     0.06 |       75 | 44.59%     | ok               |
|          15 | -4.80%   | 2.05%              | -31.15% |     0.03 |       89 | 58.90%     | ok               |

## DOGE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 19.21%   | -79.54%            | -59.36% |     0.44 |       82 | 65.33%     | ok               |
|          20 | 1.79%    | -79.54%            | -57.37% |     0.29 |       85 | 60.54%     | ok               |
|          25 | -2.44%   | -79.54%            | -55.33% |     0.25 |       75 | 55.17%     | ok               |
|          30 | -18.64%  | -79.54%            | -62.31% |     0.07 |       78 | 50.00%     | ok               |
|          35 | -42.74%  | -79.54%            | -61.79% |    -0.33 |       74 | 43.68%     | ok               |

## DOT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -20.46%  | -87.06%            | -45.72% |    -0.13 |       58 | 26.44%     | ok               |
|          45 | -28.11%  | -87.06%            | -53.09% |    -0.23 |       52 | 31.23%     | ok               |
|          20 | -46.05%  | -87.06%            | -65.30% |    -0.27 |       92 | 60.92%     | ok               |
|          30 | -45.76%  | -87.06%            | -61.52% |    -0.32 |       92 | 49.04%     | ok               |
|          35 | -44.71%  | -87.06%            | -63.05% |    -0.33 |       82 | 42.34%     | ok               |

## DXY-INDEX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -2.00%   | -0.07%             | -6.06%  |    -0.3  |       44 | 30.43%     | ok               |
|          40 | -3.84%   | -0.07%             | -7.30%  |    -0.48 |       68 | 48.04%     | ok               |
|          15 | -5.37%   | -0.07%             | -11.57% |    -0.49 |       90 | 75.65%     | ok               |
|          30 | -4.76%   | -0.07%             | -9.98%  |    -0.54 |       70 | 58.70%     | ok               |
|          35 | -5.22%   | -0.07%             | -10.12% |    -0.63 |       73 | 54.13%     | ok               |

## EEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -2.91%   | 74.24%             | -15.88% |    -0.04 |       50 | 36.11%     | ok               |
|          45 | -4.62%   | 74.24%             | -17.36% |    -0.11 |       52 | 37.60%     | ok               |
|          40 | -4.96%   | 74.24%             | -19.52% |    -0.11 |       64 | 39.77%     | ok               |
|          35 | -5.62%   | 74.24%             | -23.88% |    -0.12 |       66 | 41.76%     | ok               |
|          30 | -9.40%   | 74.24%             | -25.67% |    -0.25 |       64 | 43.43%     | ok               |

## EFA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -2.15%   | 38.39%             | -10.80% |    -0.02 |       60 | 52.25%     | ok               |
|          20 | -8.94%   | 38.39%             | -12.49% |    -0.3  |       67 | 49.25%     | ok               |
|          30 | -9.39%   | 38.39%             | -14.87% |    -0.35 |       62 | 44.59%     | ok               |
|          50 | -9.07%   | 38.39%             | -17.56% |    -0.4  |       54 | 36.27%     | ok               |
|          25 | -10.84%  | 38.39%             | -16.11% |    -0.4  |       62 | 46.42%     | ok               |

## EOG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -20.10%  | 20.32%             | -39.69% |    -0.48 |       54 | 32.28%     | ok               |
|          50 | -21.27%  | 20.32%             | -40.57% |    -0.53 |       58 | 29.45%     | ok               |
|          30 | -26.30%  | 20.32%             | -48.13% |    -0.58 |       79 | 46.26%     | ok               |
|          40 | -24.83%  | 20.32%             | -43.26% |    -0.61 |       62 | 35.61%     | ok               |
|          35 | -27.12%  | 20.32%             | -46.26% |    -0.66 |       77 | 40.93%     | ok               |

## ETC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -7.93%   | -73.96%            | -27.89% |    -0.02 |       28 | 17.05%     | ok               |
|          35 | -15.03%  | -73.96%            | -42.62% |    -0.11 |       44 | 27.01%     | ok               |
|          45 | -16.07%  | -73.96%            | -35.44% |    -0.17 |       26 | 18.97%     | ok               |
|          40 | -21.04%  | -73.96%            | -40.48% |    -0.26 |       42 | 22.80%     | ok               |
|          30 | -35.69%  | -73.96%            | -48.16% |    -0.51 |       64 | 31.23%     | ok               |

## ETH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 166.33%  | -52.04%            | -30.11% |     1.32 |       62 | 45.02%     | ok               |
|          30 | 146.26%  | -52.04%            | -32.89% |     1.18 |       64 | 53.83%     | ok               |
|          40 | 63.12%   | -52.04%            | -33.11% |     0.8  |       58 | 37.55%     | ok               |
|          15 | 47.15%   | -52.04%            | -42.74% |     0.62 |       78 | 69.16%     | ok               |
|          20 | 44.43%   | -52.04%            | -39.10% |     0.61 |       81 | 63.60%     | ok               |

## EWJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -17.66%  | 40.82%             | -30.73% |    -0.57 |       64 | 39.77%     | ok               |
|          20 | -19.06%  | 40.82%             | -31.32% |    -0.6  |       60 | 41.76%     | ok               |
|          45 | -18.45%  | 40.82%             | -27.68% |    -0.69 |       60 | 31.95%     | ok               |
|          25 | -21.40%  | 40.82%             | -31.18% |    -0.7  |       60 | 40.77%     | ok               |
|          35 | -21.61%  | 40.82%             | -32.54% |    -0.73 |       70 | 38.10%     | ok               |

## FCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -3.99%   | 59.31%             | -26.57% |     0.06 |       54 | 29.45%     | ok               |
|          45 | -8.83%   | 59.31%             | -33.82% |    -0.01 |       54 | 33.78%     | ok               |
|          40 | -20.40%  | 59.31%             | -42.89% |    -0.2  |       64 | 38.77%     | ok               |
|          30 | -28.74%  | 59.31%             | -46.84% |    -0.33 |       65 | 45.42%     | ok               |
|          35 | -33.13%  | 59.31%             | -50.12% |    -0.44 |       71 | 43.59%     | ok               |

## FET-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 40.23%   | -85.63%            | -57.24% |     0.57 |       90 | 50.96%     | ok               |
|          15 | 4.87%    | -85.63%            | -59.58% |     0.36 |       86 | 54.02%     | ok               |
|          25 | -8.25%   | -85.63%            | -57.82% |     0.23 |       93 | 44.64%     | ok               |
|          30 | -13.43%  | -85.63%            | -54.02% |     0.17 |       83 | 40.80%     | ok               |
|          35 | -36.24%  | -85.63%            | -62.73% |    -0.17 |       71 | 34.29%     | ok               |

## FIL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -2.45%   | -85.41%            | -36.87% |     0.14 |       48 | 23.56%     | ok               |
|          35 | -27.46%  | -85.41%            | -43.62% |    -0.21 |       58 | 27.78%     | ok               |
|          45 | -24.61%  | -85.41%            | -41.68% |    -0.23 |       46 | 17.82%     | ok               |
|          30 | -33.66%  | -85.41%            | -49.05% |    -0.29 |       70 | 33.14%     | ok               |
|          50 | -26.52%  | -85.41%            | -44.97% |    -0.32 |       38 | 13.03%     | ok               |

## FXI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -1.57%   | 44.93%             | -22.99% |     0.05 |       46 | 30.45%     | ok               |
|          30 | -2.13%   | 44.93%             | -24.33% |     0.03 |       46 | 29.28%     | ok               |
|          15 | -3.96%   | 44.93%             | -21.68% |    -0    |       52 | 33.61%     | ok               |
|          45 | -4.11%   | 44.93%             | -26.75% |    -0.03 |       44 | 23.79%     | ok               |
|          20 | -5.54%   | 44.93%             | -24.94% |    -0.05 |       52 | 31.61%     | ok               |

## GDX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 18.06%   | 176.61%            | -35.59% |     0.39 |       73 | 52.91%     | ok               |
|          40 | 13.85%   | 176.61%            | -31.87% |     0.35 |       64 | 42.93%     | ok               |
|          30 | 11.28%   | 176.61%            | -34.99% |     0.3  |       60 | 48.09%     | ok               |
|          35 | 8.95%    | 176.61%            | -32.37% |     0.27 |       68 | 45.26%     | ok               |
|          25 | 6.77%    | 176.61%            | -38.90% |     0.24 |       63 | 49.75%     | ok               |

## GDXJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -7.90%   | 198.49%            | -45.05% |     0.06 |       67 | 53.24%     | ok               |
|          30 | -23.13%  | 198.49%            | -44.93% |    -0.22 |       68 | 46.42%     | ok               |
|          50 | -20.22%  | 198.49%            | -44.94% |    -0.22 |       58 | 37.77%     | ok               |
|          25 | -26.54%  | 198.49%            | -47.26% |    -0.25 |       72 | 49.92%     | ok               |
|          35 | -26.76%  | 198.49%            | -43.49% |    -0.3  |       70 | 44.09%     | ok               |

## GE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 43.40%   | 240.03%            | -22.29% |     0.8  |       66 | 40.10%     | ok               |
|          45 | 32.58%   | 240.03%            | -25.68% |     0.63 |       74 | 42.93%     | ok               |
|          20 | 31.60%   | 240.03%            | -26.63% |     0.58 |       69 | 56.74%     | ok               |
|          35 | 25.69%   | 240.03%            | -27.11% |     0.52 |       80 | 48.25%     | ok               |
|          40 | 24.74%   | 240.03%            | -26.97% |     0.52 |       76 | 44.43%     | ok               |

## GLD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 34.96%   | 96.50%             | -14.61% |     0.82 |       46 | 46.92%     | ok               |
|          20 | 32.95%   | 96.50%             | -14.61% |     0.78 |       48 | 48.25%     | ok               |
|          30 | 28.53%   | 96.50%             | -16.63% |     0.71 |       48 | 45.76%     | ok               |
|          15 | 24.80%   | 96.50%             | -17.54% |     0.6  |       50 | 52.41%     | ok               |
|          35 | 22.26%   | 96.50%             | -17.29% |     0.59 |       50 | 45.09%     | ok               |

## GOOGL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 83.38%   | 146.14%            | -19.76% |     1.2  |       57 | 56.41%     | ok               |
|          30 | 77.91%   | 146.14%            | -20.41% |     1.16 |       63 | 53.74%     | ok               |
|          20 | 69.53%   | 146.14%            | -20.57% |     1.05 |       68 | 58.74%     | ok               |
|          15 | 71.38%   | 146.14%            | -13.79% |     1.04 |       71 | 63.89%     | ok               |
|          35 | 60.60%   | 146.14%            | -22.85% |     1.04 |       71 | 48.59%     | ok               |

## GRT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 37.41%   | -90.27%            | -35.66% |     0.62 |       44 | 22.03%     | ok               |
|          45 | 21.41%   | -90.27%            | -46.59% |     0.44 |       50 | 27.39%     | ok               |
|          35 | 16.47%   | -90.27%            | -48.22% |     0.39 |       60 | 36.21%     | ok               |
|          15 | 14.49%   | -90.27%            | -49.67% |     0.39 |       75 | 61.88%     | ok               |
|          40 | 16.36%   | -90.27%            | -46.38% |     0.38 |       48 | 30.46%     | ok               |

## GS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 21.11%   | 166.36%            | -20.56% |     0.47 |       74 | 61.06%     | ok               |
|          20 | 4.59%    | 166.36%            | -23.19% |     0.19 |       74 | 57.07%     | ok               |
|          40 | 0.08%    | 166.36%            | -17.88% |     0.09 |       72 | 45.26%     | ok               |
|          25 | -0.70%   | 166.36%            | -23.32% |     0.09 |       74 | 54.58%     | ok               |
|          30 | -2.38%   | 166.36%            | -22.13% |     0.05 |       76 | 52.08%     | ok               |

## HD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -4.53%   | -1.22%             | -18.58% |    -0.04 |       73 | 43.43%     | ok               |
|          25 | -5.27%   | -1.22%             | -19.40% |    -0.06 |       72 | 45.42%     | ok               |
|          45 | -9.29%   | -1.22%             | -19.30% |    -0.25 |       58 | 27.95%     | ok               |
|          15 | -14.23%  | -1.22%             | -27.26% |    -0.28 |      107 | 54.08%     | ok               |
|          35 | -13.11%  | -1.22%             | -22.43% |    -0.32 |       80 | 39.60%     | ok               |

## HON Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -13.43%  | 19.11%             | -21.17% |    -0.4  |       72 | 31.78%     | ok               |
|          45 | -15.16%  | 19.11%             | -19.99% |    -0.43 |       74 | 36.77%     | ok               |
|          40 | -23.52%  | 19.11%             | -26.29% |    -0.66 |       76 | 41.10%     | ok               |
|          35 | -25.24%  | 19.11%             | -27.34% |    -0.7  |       93 | 47.59%     | ok               |
|          30 | -27.07%  | 19.11%             | -29.77% |    -0.73 |       95 | 52.58%     | ok               |

## HYG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -7.92%   | 4.14%              | -7.92%  |    -0.96 |       70 | 29.45%     | ok               |
|          15 | -9.71%   | 4.14%              | -10.06% |    -1.05 |       88 | 41.43%     | ok               |
|          20 | -9.69%   | 4.14%              | -10.29% |    -1.08 |       86 | 39.10%     | ok               |
|          45 | -8.60%   | 4.14%              | -8.60%  |    -1.08 |       66 | 26.29%     | ok               |
|          30 | -9.52%   | 4.14%              | -9.59%  |    -1.11 |       81 | 34.28%     | ok               |

## IBIT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 71.28%   | -10.08%            | -19.20% |     1.13 |       38 | 39.47%     | ok               |
|          50 | 53.73%   | -10.08%            | -17.37% |     1.08 |       22 | 22.97%     | ok               |
|          45 | 43.76%   | -10.08%            | -17.37% |     0.91 |       24 | 23.92%     | ok               |
|          30 | 41.12%   | -10.08%            | -18.95% |     0.83 |       32 | 31.82%     | ok               |
|          40 | 37.51%   | -10.08%            | -17.78% |     0.81 |       26 | 25.84%     | ok               |

## IBM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 13.17%   | 51.56%             | -28.20% |     0.34 |       92 | 62.06%     | ok               |
|          30 | 1.60%    | 51.56%             | -27.54% |     0.13 |       76 | 49.92%     | ok               |
|          35 | -2.83%   | 51.56%             | -27.54% |     0.04 |       72 | 45.42%     | ok               |
|          20 | -4.01%   | 51.56%             | -34.12% |     0.04 |       76 | 54.41%     | ok               |
|          50 | -2.36%   | 51.56%             | -22.50% |     0.04 |       52 | 32.95%     | ok               |

## ICP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 22.79%   | -76.53%            | -32.85% |     0.44 |       60 | 27.01%     | ok               |
|          35 | 6.47%    | -76.53%            | -48.44% |     0.29 |       72 | 32.76%     | ok               |
|          50 | 6.96%    | -76.53%            | -43.65% |     0.27 |       42 | 16.86%     | ok               |
|          30 | -3.65%   | -76.53%            | -57.53% |     0.23 |       85 | 38.89%     | ok               |
|          45 | -6.94%   | -76.53%            | -40.57% |     0.11 |       60 | 21.07%     | ok               |

## IEF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -7.23%   | 0.45%              | -10.09% |    -0.87 |       70 | 42.10%     | ok               |
|          15 | -7.78%   | 0.45%              | -10.82% |    -0.92 |       69 | 43.59%     | ok               |
|          40 | -8.39%   | 0.45%              | -9.67%  |    -1.31 |       60 | 24.79%     | ok               |
|          45 | -8.07%   | 0.45%              | -9.73%  |    -1.33 |       50 | 22.80%     | ok               |
|          25 | -10.80%  | 0.45%              | -11.49% |    -1.38 |       76 | 39.27%     | ok               |

## IEMG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.10%   | 67.39%             | -13.91% |     0.05 |       52 | 34.44%     | ok               |
|          35 | -0.32%   | 67.39%             | -22.13% |     0.05 |       63 | 42.60%     | ok               |
|          45 | -0.91%   | 67.39%             | -14.92% |     0.02 |       48 | 36.94%     | ok               |
|          40 | -2.44%   | 67.39%             | -18.43% |    -0.03 |       60 | 39.93%     | ok               |
|          25 | -4.72%   | 67.39%             | -25.58% |    -0.09 |       59 | 45.42%     | ok               |

## INJ-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -12.91%  | -77.42%            | -55.31% |     0.02 |       44 | 22.41%     | ok               |
|          35 | -18.57%  | -77.42%            | -60.42% |     0.01 |       60 | 32.57%     | ok               |
|          50 | -22.38%  | -77.42%            | -51.00% |    -0.14 |       48 | 19.35%     | ok               |
|          40 | -26.93%  | -77.42%            | -57.21% |    -0.15 |       50 | 28.74%     | ok               |
|          25 | -53.83%  | -77.42%            | -81.57% |    -0.46 |       77 | 43.30%     | ok               |

## INTC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 76.11%   | 207.97%            | -49.32% |     0.74 |       60 | 34.28%     | ok               |
|          15 | 83.79%   | 207.97%            | -53.65% |     0.74 |       82 | 61.06%     | ok               |
|          25 | 75.50%   | 207.97%            | -56.41% |     0.72 |       75 | 51.58%     | ok               |
|          40 | 70.33%   | 207.97%            | -55.86% |     0.7  |       68 | 38.60%     | ok               |
|          20 | 72.70%   | 207.97%            | -52.47% |     0.7  |       82 | 56.57%     | ok               |

## INTU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.81%   | -58.41%            | -42.60% |     0.1  |       73 | 28.79%     | ok               |
|          45 | -4.20%   | -58.41%            | -44.44% |     0.04 |       71 | 32.95%     | ok               |
|          40 | -10.96%  | -58.41%            | -48.15% |    -0.08 |       73 | 35.77%     | ok               |
|          25 | -12.51%  | -58.41%            | -42.24% |    -0.09 |       66 | 45.26%     | ok               |
|          15 | -13.55%  | -58.41%            | -46.90% |    -0.1  |       81 | 50.75%     | ok               |

## ITA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 2.11%    | 94.13%             | -21.48% |     0.13 |       76 | 37.60%     | ok               |
|          15 | -1.39%   | 94.13%             | -28.17% |     0.05 |       86 | 59.23%     | ok               |
|          30 | -1.46%   | 94.13%             | -23.75% |     0.03 |       74 | 47.59%     | ok               |
|          35 | -3.55%   | 94.13%             | -23.16% |    -0.04 |       78 | 45.92%     | ok               |
|          40 | -4.66%   | 94.13%             | -20.58% |    -0.08 |       80 | 42.43%     | ok               |

## IWM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 9.83%    | 55.76%             | -13.30% |     0.4  |       50 | 36.77%     | ok               |
|          40 | 8.60%    | 55.76%             | -14.08% |     0.39 |       42 | 31.28%     | ok               |
|          30 | 9.40%    | 55.76%             | -12.83% |     0.39 |       48 | 35.77%     | ok               |
|          35 | 8.35%    | 55.76%             | -14.11% |     0.36 |       48 | 33.61%     | ok               |
|          20 | 5.50%    | 55.76%             | -13.83% |     0.25 |       60 | 37.77%     | ok               |

## JNJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 21.36%   | 65.92%             | -10.57% |     0.9  |       56 | 37.10%     | ok               |
|          15 | 14.86%   | 65.92%             | -18.02% |     0.53 |       66 | 56.91%     | ok               |
|          45 | 11.68%   | 65.92%             | -13.35% |     0.51 |       58 | 42.10%     | ok               |
|          20 | 10.97%   | 65.92%             | -17.61% |     0.43 |       70 | 53.58%     | ok               |
|          40 | 9.25%    | 65.92%             | -14.77% |     0.4  |       64 | 46.26%     | ok               |

## JPM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 20.10%   | 88.76%             | -15.90% |     0.66 |       52 | 41.26%     | ok               |
|          45 | 8.69%    | 88.76%             | -21.91% |     0.32 |       54 | 44.26%     | ok               |
|          40 | -5.67%   | 88.76%             | -28.47% |    -0.09 |       66 | 46.76%     | ok               |
|          20 | -12.70%  | 88.76%             | -33.59% |    -0.2  |       84 | 58.07%     | ok               |
|          35 | -10.93%  | 88.76%             | -27.43% |    -0.23 |       72 | 50.42%     | ok               |

## KO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 28.93%   | 37.66%             | -8.07%  |     1.03 |       49 | 37.77%     | ok               |
|          35 | 24.98%   | 37.66%             | -8.07%  |     0.93 |       52 | 36.44%     | ok               |
|          40 | 22.37%   | 37.66%             | -9.28%  |     0.9  |       54 | 33.28%     | ok               |
|          25 | 23.60%   | 37.66%             | -9.37%  |     0.86 |       55 | 40.43%     | ok               |
|          50 | 14.81%   | 37.66%             | -11.40% |     0.68 |       36 | 26.79%     | ok               |

## LDO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 24.99%   | -87.45%            | -46.95% |     0.48 |       81 | 51.92%     | ok               |
|          20 | 13.39%   | -87.45%            | -44.97% |     0.4  |       85 | 47.32%     | ok               |
|          50 | 15.22%   | -87.45%            | -48.04% |     0.37 |       46 | 16.86%     | ok               |
|          30 | 1.95%    | -87.45%            | -60.93% |     0.29 |       74 | 37.93%     | ok               |
|          35 | -0.33%   | -87.45%            | -62.61% |     0.25 |       72 | 31.03%     | ok               |

## LIN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 5.16%    | 27.56%             | -23.68% |     0.23 |       62 | 49.42%     | ok               |
|          25 | 4.87%    | 27.56%             | -22.01% |     0.23 |       61 | 41.43%     | ok               |
|          20 | 2.62%    | 27.56%             | -23.00% |     0.15 |       60 | 44.59%     | ok               |
|          35 | 1.08%    | 27.56%             | -21.18% |     0.1  |       60 | 32.11%     | ok               |
|          30 | 0.44%    | 27.56%             | -21.53% |     0.08 |       64 | 38.60%     | ok               |

## LINK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -11.40%  | -70.78%            | -49.35% |     0.12 |       69 | 41.57%     | ok               |
|          45 | -13.28%  | -70.78%            | -38.11% |     0.05 |       50 | 26.63%     | ok               |
|          50 | -12.86%  | -70.78%            | -36.52% |     0.03 |       40 | 21.26%     | ok               |
|          35 | -24.33%  | -70.78%            | -49.18% |    -0.05 |       59 | 36.78%     | ok               |
|          25 | -34.06%  | -70.78%            | -46.32% |    -0.12 |       68 | 47.13%     | ok               |

## LLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 14.60%   | 74.16%             | -38.23% |     0.37 |       44 | 38.27%     | ok               |
|          15 | 7.68%    | 74.16%             | -48.12% |     0.25 |       63 | 61.90%     | ok               |
|          45 | 2.36%    | 74.16%             | -42.66% |     0.16 |       52 | 41.60%     | ok               |
|          20 | -9.66%   | 74.16%             | -51.34% |    -0.02 |       72 | 56.91%     | ok               |
|          25 | -11.15%  | 74.16%             | -53.47% |    -0.05 |       68 | 54.24%     | ok               |

## LRCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 15.78%   | 382.67%            | -60.45% |     0.35 |       83 | 55.57%     | ok               |
|          50 | 9.12%    | 382.67%            | -50.39% |     0.28 |       80 | 37.44%     | ok               |
|          40 | 5.84%    | 382.67%            | -56.86% |     0.24 |       72 | 43.26%     | ok               |
|          35 | -1.03%   | 382.67%            | -61.76% |     0.17 |       80 | 45.26%     | ok               |
|          20 | -3.43%   | 382.67%            | -67.48% |     0.15 |       89 | 51.08%     | ok               |

## LTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -12.22%  | -65.62%            | -44.78% |    -0    |       56 | 31.80%     | ok               |
|          35 | -22.47%  | -65.62%            | -54.86% |    -0.13 |       66 | 42.91%     | ok               |
|          30 | -34.00%  | -65.62%            | -53.76% |    -0.29 |       66 | 48.47%     | ok               |
|          40 | -31.40%  | -65.62%            | -56.10% |    -0.3  |       58 | 38.12%     | ok               |
|          25 | -36.79%  | -65.62%            | -54.26% |    -0.33 |       74 | 50.96%     | ok               |

## MCD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 2.85%    | -6.57%             | -9.22%  |     0.19 |       42 | 20.63%     | ok               |
|          30 | -2.55%   | -6.57%             | -18.81% |    -0.05 |       75 | 38.10%     | ok               |
|          25 | -3.59%   | -6.57%             | -20.47% |    -0.09 |       75 | 40.77%     | ok               |
|          35 | -7.68%   | -6.57%             | -15.45% |    -0.29 |       67 | 34.44%     | ok               |
|          40 | -7.95%   | -6.57%             | -16.86% |    -0.33 |       71 | 28.79%     | ok               |

## META Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -6.50%   | 22.46%             | -31.03% |    -0.02 |       66 | 39.10%     | ok               |
|          40 | -16.78%  | 22.46%             | -35.11% |    -0.23 |       66 | 42.10%     | ok               |
|          50 | -20.77%  | 22.46%             | -34.00% |    -0.37 |       70 | 35.27%     | ok               |
|          25 | -24.99%  | 22.46%             | -39.84% |    -0.37 |       67 | 52.75%     | ok               |
|          30 | -27.00%  | 22.46%             | -38.96% |    -0.44 |       72 | 49.58%     | ok               |

## MPC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 14.51%   | 51.48%             | -23.96% |     0.37 |       52 | 38.60%     | ok               |
|          45 | 7.25%    | 51.48%             | -25.09% |     0.24 |       58 | 42.26%     | ok               |
|          40 | 5.62%    | 51.48%             | -25.70% |     0.22 |       60 | 44.59%     | ok               |
|          35 | 2.36%    | 51.48%             | -35.90% |     0.16 |       68 | 47.09%     | ok               |
|          30 | -13.74%  | 51.48%             | -44.76% |    -0.14 |       71 | 49.92%     | ok               |

## MRK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -21.05%  | 2.54%              | -30.12% |    -0.39 |       87 | 56.57%     | ok               |
|          25 | -20.67%  | 2.54%              | -31.07% |    -0.42 |       72 | 48.59%     | ok               |
|          20 | -24.56%  | 2.54%              | -29.59% |    -0.52 |       77 | 51.91%     | ok               |
|          45 | -23.49%  | 2.54%              | -26.02% |    -0.63 |       57 | 34.78%     | ok               |
|          50 | -23.14%  | 2.54%              | -25.69% |    -0.66 |       56 | 31.78%     | ok               |

## MS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -4.22%   | 146.50%            | -19.99% |    -0.02 |       70 | 41.10%     | ok               |
|          35 | -10.89%  | 146.50%            | -25.26% |    -0.19 |       74 | 45.76%     | ok               |
|          15 | -15.50%  | 146.50%            | -23.25% |    -0.26 |       78 | 58.07%     | ok               |
|          20 | -15.61%  | 146.50%            | -25.68% |    -0.29 |       82 | 54.24%     | ok               |
|          30 | -17.22%  | 146.50%            | -27.79% |    -0.36 |       79 | 49.58%     | ok               |

## MSFT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -17.44%  | -9.14%             | -26.27% |    -0.46 |       66 | 35.27%     | ok               |
|          50 | -21.16%  | -9.14%             | -28.83% |    -0.6  |       64 | 30.62%     | ok               |
|          35 | -29.29%  | -9.14%             | -33.68% |    -0.75 |       75 | 43.59%     | ok               |
|          25 | -32.73%  | -9.14%             | -37.59% |    -0.8  |       87 | 51.25%     | ok               |
|          40 | -30.12%  | -9.14%             | -34.46% |    -0.81 |       71 | 38.60%     | ok               |

## MU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 421.65%  | 1216.72%           | -61.96% |     1.55 |       48 | 68.05%     | ok               |
|          25 | 334.60%  | 1216.72%           | -67.90% |     1.46 |       49 | 61.73%     | ok               |
|          40 | 290.77%  | 1216.72%           | -64.07% |     1.4  |       56 | 55.24%     | ok               |
|          20 | 297.89%  | 1216.72%           | -67.25% |     1.37 |       55 | 63.89%     | ok               |
|          30 | 270.20%  | 1216.72%           | -68.76% |     1.34 |       51 | 59.90%     | ok               |

## NEAR-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 99.44%   | -62.86%            | -48.95% |     0.97 |       44 | 23.18%     | ok               |
|          50 | 70.90%   | -62.86%            | -53.13% |     0.82 |       38 | 18.39%     | ok               |
|          40 | 57.99%   | -62.86%            | -57.15% |     0.71 |       48 | 27.59%     | ok               |
|          35 | 31.48%   | -62.86%            | -61.02% |     0.51 |       70 | 32.95%     | ok               |
|          15 | 2.55%    | -62.86%            | -54.94% |     0.32 |       87 | 57.09%     | ok               |

## NEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 2.46%    | 183.30%            | -29.41% |     0.21 |       64 | 62.23%     | ok               |
|          20 | -8.51%   | 183.30%            | -30.47% |     0.06 |       74 | 57.74%     | ok               |
|          25 | -21.86%  | 183.30%            | -37.89% |    -0.15 |       70 | 55.57%     | ok               |
|          50 | -25.02%  | 183.30%            | -33.36% |    -0.27 |       58 | 40.43%     | ok               |
|          30 | -31.65%  | 183.30%            | -38.49% |    -0.34 |       74 | 53.91%     | ok               |

## NFLX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 62.48%   | 31.27%             | -11.94% |     1.22 |       46 | 47.25%     | ok               |
|          50 | 48.67%   | 31.27%             | -16.28% |     1.07 |       48 | 39.77%     | ok               |
|          35 | 54.13%   | 31.27%             | -18.30% |     1.05 |       60 | 50.75%     | ok               |
|          45 | 44.91%   | 31.27%             | -15.48% |     0.97 |       52 | 43.59%     | ok               |
|          25 | 43.22%   | 31.27%             | -21.09% |     0.85 |       60 | 57.24%     | ok               |

## NKE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -26.93%  | -58.39%            | -42.13% |    -0.38 |       75 | 37.27%     | ok               |
|          20 | -33.86%  | -58.39%            | -50.44% |    -0.42 |       93 | 52.58%     | ok               |
|          25 | -34.08%  | -58.39%            | -51.20% |    -0.44 |       89 | 48.75%     | ok               |
|          40 | -26.46%  | -58.39%            | -31.19% |    -0.5  |       63 | 30.12%     | ok               |
|          15 | -38.05%  | -58.39%            | -55.28% |    -0.5  |       90 | 57.07%     | ok               |

## NOW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 15.98%   | -36.31%            | -26.36% |     0.35 |       79 | 51.91%     | ok               |
|          30 | 15.47%   | -36.31%            | -30.25% |     0.35 |       80 | 45.92%     | ok               |
|          15 | 9.71%    | -36.31%            | -26.36% |     0.28 |       87 | 55.24%     | ok               |
|          25 | 8.90%    | -36.31%            | -25.70% |     0.27 |       72 | 49.25%     | ok               |
|          35 | 8.01%    | -36.31%            | -29.30% |     0.26 |       81 | 40.60%     | ok               |

## NVDA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -4.15%   | 119.16%            | -33.22% |     0.11 |       70 | 50.27%     | ok               |
|          30 | -4.77%   | 119.16%            | -35.26% |     0.09 |       72 | 47.77%     | ok               |
|          20 | -10.51%  | 119.16%            | -40.59% |     0.03 |       73 | 54.72%     | ok               |
|          50 | -14.29%  | 119.16%            | -40.84% |    -0.11 |       56 | 32.09%     | ok               |
|          35 | -17.64%  | 119.16%            | -41.25% |    -0.13 |       80 | 44.92%     | ok               |

## OP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 66.86%   | -93.92%            | -36.11% |     0.86 |       34 | 12.45%     | ok               |
|          45 | 65.66%   | -93.92%            | -45.76% |     0.8  |       36 | 17.05%     | ok               |
|          40 | 45.24%   | -93.92%            | -53.61% |     0.62 |       50 | 25.86%     | ok               |
|          35 | 20.88%   | -93.92%            | -58.33% |     0.42 |       58 | 28.93%     | ok               |
|          30 | -1.17%   | -93.92%            | -70.27% |     0.24 |       74 | 35.44%     | ok               |

## ORCL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 186.63%  | 26.95%             | -29.32% |     1.21 |       74 | 65.22%     | ok               |
|          25 | 115.02%  | 26.95%             | -27.76% |     0.95 |       75 | 57.74%     | ok               |
|          20 | 111.33%  | 26.95%             | -29.32% |     0.93 |       77 | 60.90%     | ok               |
|          35 | 84.36%   | 26.95%             | -31.95% |     0.82 |       68 | 49.42%     | ok               |
|          30 | 84.52%   | 26.95%             | -29.47% |     0.81 |       74 | 53.58%     | ok               |

## OXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 9.71%    | -13.85%            | -30.43% |     0.28 |       65 | 43.26%     | ok               |
|          35 | 5.72%    | -13.85%            | -30.50% |     0.22 |       68 | 38.94%     | ok               |
|          40 | 3.13%    | -13.85%            | -32.21% |     0.17 |       56 | 34.94%     | ok               |
|          50 | 2.16%    | -13.85%            | -30.19% |     0.15 |       36 | 27.62%     | ok               |
|          25 | -5.47%   | -13.85%            | -40.06% |     0.02 |       73 | 46.76%     | ok               |

## PEP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 12.74%   | -18.86%            | -11.62% |     0.57 |       48 | 27.29%     | ok               |
|          45 | 4.48%    | -18.86%            | -14.22% |     0.23 |       72 | 32.11%     | ok               |
|          40 | -1.62%   | -18.86%            | -18.04% |    -0    |       82 | 38.27%     | ok               |
|          35 | -2.35%   | -18.86%            | -21.42% |    -0.01 |       87 | 43.09%     | ok               |
|          30 | -7.73%   | -18.86%            | -21.35% |    -0.16 |       83 | 49.92%     | ok               |

## PEPE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 22.05%   | -84.55%            | -61.96% |     0.48 |       78 | 59.77%     | ok               |
|          30 | 22.01%   | -84.55%            | -57.66% |     0.45 |       79 | 44.25%     | ok               |
|          35 | 15.05%   | -84.55%            | -51.35% |     0.39 |       64 | 38.89%     | ok               |
|          25 | -0.14%   | -84.55%            | -53.88% |     0.28 |       85 | 49.43%     | ok               |
|          20 | -4.84%   | -84.55%            | -61.13% |     0.26 |       84 | 56.13%     | ok               |

## PFE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -27.31%  | -8.28%             | -25.48% |    -1.01 |       52 | 19.13%     | ok               |
|          35 | -34.85%  | -8.28%             | -34.24% |    -1.15 |       84 | 31.45%     | ok               |
|          50 | -28.55%  | -8.28%             | -26.74% |    -1.17 |       42 | 15.47%     | ok               |
|          40 | -33.47%  | -8.28%             | -31.73% |    -1.2  |       76 | 23.96%     | ok               |
|          30 | -41.43%  | -8.28%             | -40.87% |    -1.35 |       77 | 35.11%     | ok               |

## PG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -2.58%   | -6.17%             | -19.77% |    -0.06 |       52 | 34.94%     | ok               |
|          35 | -4.74%   | -6.17%             | -18.66% |    -0.14 |       60 | 38.27%     | ok               |
|          30 | -13.39%  | -6.17%             | -21.65% |    -0.48 |       62 | 41.43%     | ok               |
|          45 | -12.09%  | -6.17%             | -20.43% |    -0.5  |       52 | 32.45%     | ok               |
|          25 | -14.43%  | -6.17%             | -22.55% |    -0.52 |       72 | 42.60%     | ok               |

## PM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 0.71%    | 99.57%             | -32.20% |     0.11 |       88 | 53.91%     | ok               |
|          30 | -2.25%   | 99.57%             | -33.68% |     0.05 |       85 | 57.57%     | ok               |
|          20 | -2.49%   | 99.57%             | -31.89% |     0.05 |       89 | 62.73%     | ok               |
|          50 | -5.39%   | 99.57%             | -35.70% |    -0.05 |       76 | 42.93%     | ok               |
|          40 | -7.41%   | 99.57%             | -37.94% |    -0.09 |       82 | 50.08%     | ok               |

## POL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 84.54%   | -84.05%            | -46.45% |     0.89 |       81 | 51.34%     | ok               |
|          25 | 87.94%   | -84.05%            | -46.72% |     0.87 |       66 | 59.20%     | ok               |
|          20 | 73.48%   | -84.05%            | -52.88% |     0.78 |       72 | 63.41%     | ok               |
|          15 | 54.81%   | -84.05%            | -58.42% |     0.66 |       74 | 68.20%     | ok               |
|          50 | 18.38%   | -84.05%            | -22.86% |     0.42 |       52 | 20.88%     | ok               |

## QCOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 2.68%    | 31.03%             | -54.50% |     0.2  |       73 | 48.92%     | ok               |
|          35 | 0.80%    | 31.03%             | -50.58% |     0.17 |       79 | 44.43%     | ok               |
|          20 | -1.49%   | 31.03%             | -54.38% |     0.16 |       69 | 51.75%     | ok               |
|          30 | -10.63%  | 31.03%             | -56.59% |     0.03 |       75 | 46.92%     | ok               |
|          15 | -17.86%  | 31.03%             | -57.94% |    -0.06 |       73 | 54.91%     | ok               |

## QQQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 22.88%   | 69.00%             | -12.88% |     0.62 |       57 | 48.25%     | ok               |
|          15 | 23.41%   | 69.00%             | -14.17% |     0.59 |       61 | 53.74%     | ok               |
|          20 | 19.91%   | 69.00%             | -12.98% |     0.54 |       65 | 50.92%     | ok               |
|          30 | 17.84%   | 69.00%             | -12.88% |     0.52 |       62 | 45.26%     | ok               |
|          35 | 5.79%    | 69.00%             | -19.00% |     0.24 |       68 | 41.60%     | ok               |

## RENDER-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 50.99%   | -62.62%            | -43.43% |     0.65 |       86 | 53.94%     | ok               |
|          15 | 33.47%   | -62.62%            | -44.59% |     0.55 |       86 | 56.97%     | ok               |
|          25 | 21.07%   | -62.62%            | -40.60% |     0.46 |       90 | 50.10%     | ok               |
|          30 | -16.89%  | -62.62%            | -45.00% |     0.12 |       98 | 43.84%     | ok               |
|          35 | -29.90%  | -62.62%            | -41.33% |    -0.1  |       84 | 35.35%     | ok               |

## RTX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 24.93%   | 103.09%            | -18.66% |     0.62 |       78 | 56.24%     | ok               |
|          25 | 20.49%   | 103.09%            | -18.59% |     0.54 |       64 | 52.75%     | ok               |
|          30 | 18.66%   | 103.09%            | -16.99% |     0.51 |       58 | 51.58%     | ok               |
|          35 | 16.16%   | 103.09%            | -18.00% |     0.5  |       56 | 49.75%     | ok               |
|          50 | 14.86%   | 103.09%            | -18.42% |     0.49 |       60 | 41.93%     | ok               |

## SBUX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -15.36%  | 12.49%             | -23.55% |    -0.25 |       65 | 41.93%     | ok               |
|          45 | -18.17%  | 12.49%             | -27.26% |    -0.42 |       68 | 29.78%     | ok               |
|          40 | -20.15%  | 12.49%             | -27.00% |    -0.44 |       62 | 33.78%     | ok               |
|          30 | -22.59%  | 12.49%             | -29.34% |    -0.45 |       64 | 39.60%     | ok               |
|          20 | -27.37%  | 12.49%             | -34.85% |    -0.52 |       70 | 43.93%     | ok               |

## SCHW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -0.45%   | 45.18%             | -16.53% |     0.06 |       56 | 33.44%     | ok               |
|          50 | -4.29%   | 45.18%             | -13.28% |    -0.09 |       50 | 30.95%     | ok               |
|          25 | -12.81%  | 45.18%             | -28.76% |    -0.23 |       63 | 48.25%     | ok               |
|          40 | -10.77%  | 45.18%             | -23.35% |    -0.23 |       64 | 36.44%     | ok               |
|          20 | -14.44%  | 45.18%             | -29.24% |    -0.26 |       71 | 50.92%     | ok               |

## SHIB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 1.05%    | -78.86%            | -49.21% |     0.26 |       80 | 68.97%     | ok               |
|          25 | -6.65%   | -78.86%            | -43.85% |     0.16 |       77 | 59.77%     | ok               |
|          20 | -11.16%  | -78.86%            | -46.38% |     0.12 |       79 | 64.18%     | ok               |
|          35 | -9.94%   | -78.86%            | -53.32% |     0.09 |       66 | 46.93%     | ok               |
|          40 | -16.49%  | -78.86%            | -49.96% |    -0.01 |       56 | 39.27%     | ok               |

## SHY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          30 | -2.24%   | 0.50%              | -2.85% |    -0.79 |       48 | 34.28%     | ok               |
|          35 | -2.36%   | 0.50%              | -3.27% |    -0.84 |       50 | 32.45%     | ok               |
|          40 | -2.47%   | 0.50%              | -3.33% |    -0.89 |       50 | 30.62%     | ok               |
|          45 | -2.45%   | 0.50%              | -3.23% |    -0.9  |       48 | 27.45%     | ok               |
|          50 | -2.62%   | 0.50%              | -3.40% |    -1.01 |       44 | 24.63%     | ok               |

## SKY-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -28.82%  | -9.55%             | -43.98% |    -0.35 |       70 | 41.32%     | ok               |
|          15 | -33.17%  | -9.55%             | -56.39% |    -0.35 |       60 | 51.60%     | ok               |
|          25 | -32.47%  | -9.55%             | -48.09% |    -0.41 |       65 | 44.98%     | ok               |
|          20 | -42.76%  | -9.55%             | -58.40% |    -0.6  |       62 | 48.63%     | ok               |
|          35 | -39.99%  | -9.55%             | -49.68% |    -0.7  |       64 | 34.93%     | ok               |

## SLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 20.48%   | -4.47%             | -24.10% |     0.5  |       48 | 35.94%     | ok               |
|          45 | 17.59%   | -4.47%             | -21.53% |     0.46 |       56 | 32.45%     | ok               |
|          50 | -2.98%   | -4.47%             | -29.84% |     0.01 |       52 | 28.45%     | ok               |
|          35 | -10.77%  | -4.47%             | -43.22% |    -0.12 |       74 | 43.76%     | ok               |
|          30 | -25.16%  | -4.47%             | -55.49% |    -0.43 |       77 | 50.08%     | ok               |

## SLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 78.65%   | 157.35%            | -34.10% |     0.94 |       52 | 34.11%     | ok               |
|          45 | 75.82%   | 157.35%            | -31.82% |     0.92 |       56 | 34.94%     | ok               |
|          40 | 73.72%   | 157.35%            | -31.93% |     0.9  |       62 | 37.10%     | ok               |
|          35 | 59.97%   | 157.35%            | -36.89% |     0.79 |       64 | 39.27%     | ok               |
|          30 | 50.68%   | 157.35%            | -42.66% |     0.7  |       58 | 41.43%     | ok               |

## SMH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 116.97%  | 224.18%            | -30.17% |     1.32 |       47 | 52.58%     | ok               |
|          35 | 94.18%   | 224.18%            | -34.36% |     1.2  |       54 | 48.42%     | ok               |
|          25 | 94.04%   | 224.18%            | -32.94% |     1.18 |       46 | 51.41%     | ok               |
|          30 | 91.75%   | 224.18%            | -33.99% |     1.17 |       48 | 49.75%     | ok               |
|          45 | 77.80%   | 224.18%            | -32.75% |     1.13 |       52 | 42.60%     | ok               |

## SNX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 27.64%   | -86.68%            | -43.20% |     0.49 |       73 | 49.62%     | ok               |
|          35 | 3.98%    | -86.68%            | -30.08% |     0.28 |       66 | 32.18%     | ok               |
|          30 | -6.01%   | -86.68%            | -34.76% |     0.19 |       62 | 39.27%     | ok               |
|          25 | -9.66%   | -86.68%            | -38.88% |     0.17 |       74 | 44.06%     | ok               |
|          15 | -13.98%  | -86.68%            | -44.00% |     0.17 |       81 | 54.21%     | ok               |

## SOL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -19.44%  | -71.12%            | -54.68% |     0.02 |       64 | 38.89%     | ok               |
|          25 | -33.50%  | -71.12%            | -53.21% |    -0.11 |       72 | 57.28%     | ok               |
|          35 | -34.45%  | -71.12%            | -61.96% |    -0.15 |       72 | 46.36%     | ok               |
|          15 | -38.72%  | -71.12%            | -59.14% |    -0.15 |       74 | 64.37%     | ok               |
|          20 | -43.05%  | -71.12%            | -56.90% |    -0.23 |       68 | 59.77%     | ok               |

## SOXX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 98.90%   | 204.83%            | -38.67% |     1.16 |       53 | 51.25%     | ok               |
|          25 | 95.09%   | 204.83%            | -39.85% |     1.13 |       51 | 50.92%     | ok               |
|          35 | 89.64%   | 204.83%            | -38.63% |     1.11 |       59 | 46.26%     | ok               |
|          15 | 93.90%   | 204.83%            | -37.72% |     1.09 |       66 | 54.08%     | ok               |
|          30 | 84.13%   | 204.83%            | -40.34% |     1.05 |       55 | 48.75%     | ok               |

## SPY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 15.46%   | 50.44%             | -14.25% |     0.54 |       60 | 53.91%     | ok               |
|          15 | 13.88%   | 50.44%             | -16.80% |     0.49 |       69 | 57.07%     | ok               |
|          25 | 8.27%    | 50.44%             | -15.22% |     0.33 |       60 | 52.91%     | ok               |
|          30 | 4.36%    | 50.44%             | -16.47% |     0.21 |       62 | 50.42%     | ok               |
|          35 | 3.58%    | 50.44%             | -16.72% |     0.19 |       58 | 47.59%     | ok               |

## SUSHI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -23.49%  | -88.55%            | -40.08% |    -0.19 |       52 | 14.75%     | ok               |
|          45 | -55.77%  | -88.55%            | -64.27% |    -0.7  |       54 | 18.01%     | ok               |
|          40 | -58.91%  | -88.55%            | -66.57% |    -0.7  |       61 | 24.52%     | ok               |
|          15 | -76.99%  | -88.55%            | -78.98% |    -0.89 |       87 | 46.93%     | ok               |
|          35 | -71.87%  | -88.55%            | -78.94% |    -0.97 |       76 | 30.08%     | ok               |

## T Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 60.32%   | 23.07%             | -18.13% |     1.18 |       56 | 55.74%     | ok               |
|          25 | 55.35%   | 23.07%             | -17.66% |     1.12 |       58 | 53.58%     | ok               |
|          15 | 51.57%   | 23.07%             | -15.08% |     1.03 |       65 | 59.57%     | ok               |
|          30 | 38.33%   | 23.07%             | -17.01% |     0.87 |       62 | 51.58%     | ok               |
|          35 | 30.51%   | 23.07%             | -14.49% |     0.75 |       62 | 48.25%     | ok               |

## TGT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -8.23%   | -5.91%             | -41.89% |    -0.05 |       79 | 46.09%     | ok               |
|          25 | -9.14%   | -5.91%             | -42.39% |    -0.09 |       61 | 41.10%     | ok               |
|          15 | -11.23%  | -5.91%             | -39.76% |    -0.1  |       69 | 50.58%     | ok               |
|          45 | -8.37%   | -5.91%             | -29.07% |    -0.12 |       50 | 28.79%     | ok               |
|          30 | -10.02%  | -5.91%             | -40.57% |    -0.12 |       56 | 38.44%     | ok               |

## TIA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 15.53%   | -91.50%            | -40.83% |     0.37 |       66 | 26.05%     | ok               |
|          35 | 15.05%   | -91.50%            | -41.15% |     0.37 |       64 | 30.84%     | ok               |
|          50 | 13.81%   | -91.50%            | -44.86% |     0.36 |       32 | 11.49%     | ok               |
|          45 | 11.18%   | -91.50%            | -46.40% |     0.32 |       54 | 18.97%     | ok               |
|          30 | -29.83%  | -91.50%            | -62.78% |    -0.08 |       88 | 35.44%     | ok               |

## TLT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -19.42%  | -7.10%             | -20.85% |    -1.51 |       70 | 31.28%     | ok               |
|          50 | -13.94%  | -7.10%             | -15.73% |    -1.69 |       30 | 13.98%     | ok               |
|          15 | -25.91%  | -7.10%             | -27.29% |    -1.82 |       76 | 39.43%     | ok               |
|          35 | -20.62%  | -7.10%             | -21.45% |    -1.84 |       62 | 25.29%     | ok               |
|          40 | -19.03%  | -7.10%             | -19.89% |    -1.86 |       56 | 20.63%     | ok               |

## TMO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 44.35%   | -8.19%             | -8.17%  |     1.02 |       38 | 30.28%     | ok               |
|          45 | 36.71%   | -8.19%             | -10.13% |     0.84 |       46 | 35.11%     | ok               |
|          40 | 34.69%   | -8.19%             | -9.91%  |     0.79 |       49 | 39.60%     | ok               |
|          35 | 19.17%   | -8.19%             | -14.06% |     0.49 |       59 | 43.93%     | ok               |
|          30 | 10.27%   | -8.19%             | -18.11% |     0.31 |       61 | 48.25%     | ok               |

## TMUS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 15.42%   | 7.38%              | -24.50% |     0.41 |       68 | 47.59%     | ok               |
|          15 | 15.88%   | 7.38%              | -26.87% |     0.41 |       69 | 59.73%     | ok               |
|          20 | 6.52%    | 7.38%              | -25.10% |     0.23 |       73 | 53.91%     | ok               |
|          25 | 5.57%    | 7.38%              | -26.30% |     0.22 |       75 | 50.25%     | ok               |
|          50 | 4.50%    | 7.38%              | -22.71% |     0.2  |       58 | 35.77%     | ok               |

## TRX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 1.07%    | 25.74%             | -18.79% |     0.11 |       54 | 37.74%     | ok               |
|          50 | -2.29%   | 25.74%             | -18.49% |     0.01 |       46 | 32.18%     | ok               |
|          30 | -4.49%   | 25.74%             | -22.90% |    -0.03 |       74 | 49.62%     | ok               |
|          35 | -5.28%   | 25.74%             | -21.77% |    -0.06 |       70 | 46.36%     | ok               |
|          25 | -6.20%   | 25.74%             | -26.84% |    -0.07 |       70 | 52.87%     | ok               |

## TSLA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 84.21%   | 127.46%            | -30.67% |     0.9  |       60 | 34.44%     | ok               |
|          45 | 56.06%   | 127.46%            | -31.89% |     0.71 |       64 | 31.78%     | ok               |
|          50 | 48.96%   | 127.46%            | -32.60% |     0.67 |       66 | 30.28%     | ok               |
|          35 | 43.82%   | 127.46%            | -37.58% |     0.6  |       71 | 37.27%     | ok               |
|          30 | 16.71%   | 127.46%            | -42.22% |     0.36 |       67 | 41.76%     | ok               |

## TXN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 13.38%   | 79.66%             | -45.45% |     0.33 |       72 | 35.77%     | ok               |
|          20 | 2.88%    | 79.66%             | -38.98% |     0.19 |       62 | 59.90%     | ok               |
|          15 | 0.75%    | 79.66%             | -39.48% |     0.17 |       65 | 64.06%     | ok               |
|          35 | -5.44%   | 79.66%             | -43.38% |     0.05 |       78 | 50.42%     | ok               |
|          40 | -6.08%   | 79.66%             | -45.67% |     0.04 |       76 | 48.25%     | ok               |

## UNH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 31.68%   | -16.53%            | -37.02% |     0.56 |       52 | 30.12%     | ok               |
|          30 | 26.31%   | -16.53%            | -27.86% |     0.48 |       76 | 52.41%     | ok               |
|          35 | 22.87%   | -16.53%            | -29.20% |     0.44 |       68 | 47.25%     | ok               |
|          15 | 22.90%   | -16.53%            | -32.14% |     0.43 |       76 | 67.55%     | ok               |
|          40 | 20.28%   | -16.53%            | -35.94% |     0.42 |       60 | 42.26%     | ok               |

## UNI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -18.07%  | -76.29%            | -58.49% |    -0    |       54 | 25.67%     | ok               |
|          40 | -23.44%  | -76.29%            | -63.75% |    -0.05 |       56 | 30.65%     | ok               |
|          50 | -25.51%  | -76.29%            | -57.60% |    -0.14 |       52 | 21.07%     | ok               |
|          35 | -35.75%  | -76.29%            | -68.71% |    -0.18 |       70 | 35.63%     | ok               |
|          20 | -73.62%  | -76.29%            | -81.22% |    -0.77 |      102 | 52.30%     | ok               |

## UPS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -37.84%  | -22.34%            | -44.52% |    -0.72 |       84 | 48.25%     | ok               |
|          35 | -37.16%  | -22.34%            | -38.61% |    -0.77 |       61 | 34.28%     | ok               |
|          25 | -38.83%  | -22.34%            | -40.93% |    -0.77 |       80 | 44.76%     | ok               |
|          40 | -37.57%  | -22.34%            | -39.56% |    -0.8  |       51 | 28.79%     | ok               |
|          30 | -39.46%  | -22.34%            | -38.76% |    -0.81 |       72 | 40.27%     | ok               |

## USO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 16.31%   | 57.05%             | -33.25% |     0.38 |       48 | 26.62%     | ok               |
|          30 | 8.43%    | 57.05%             | -43.35% |     0.26 |       66 | 34.11%     | ok               |
|          40 | 4.41%    | 57.05%             | -41.14% |     0.2  |       59 | 29.28%     | ok               |
|          50 | 3.92%    | 57.05%             | -31.13% |     0.18 |       52 | 24.13%     | ok               |
|          20 | 3.37%    | 57.05%             | -46.76% |     0.18 |       74 | 39.43%     | ok               |

## VEA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 5.44%    | 50.16%             | -16.28% |     0.25 |       60 | 50.58%     | ok               |
|          20 | 1.19%    | 50.16%             | -17.70% |     0.1  |       61 | 47.92%     | ok               |
|          25 | -0.82%   | 50.16%             | -17.79% |     0.02 |       57 | 46.26%     | ok               |
|          30 | -0.98%   | 50.16%             | -17.93% |     0.01 |       58 | 44.09%     | ok               |
|          35 | -2.09%   | 50.16%             | -16.79% |    -0.03 |       56 | 43.09%     | ok               |

## VIXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -46.17%  | -62.25%            | -68.69% |    -0.39 |       44 | 10.32%     | ok               |
|          45 | -56.13%  | -62.25%            | -74.13% |    -0.55 |       56 | 16.31%     | ok               |
|          40 | -65.03%  | -62.25%            | -80.03% |    -0.67 |       72 | 20.80%     | ok               |
|          35 | -68.25%  | -62.25%            | -83.81% |    -0.7  |       88 | 26.12%     | ok               |
|          15 | -77.15%  | -62.25%            | -89.47% |    -0.77 |      101 | 44.76%     | ok               |

## VNQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -8.60%   | 18.85%             | -19.07% |    -0.37 |       60 | 28.62%     | ok               |
|          50 | -9.03%   | 18.85%             | -17.13% |    -0.41 |       56 | 26.12%     | ok               |
|          25 | -13.12%  | 18.85%             | -22.34% |    -0.51 |       69 | 40.77%     | ok               |
|          40 | -14.13%  | 18.85%             | -24.84% |    -0.62 |       74 | 32.11%     | ok               |
|          20 | -16.52%  | 18.85%             | -23.79% |    -0.64 |       74 | 43.59%     | ok               |

## VTI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 19.43%   | 50.45%             | -13.96% |     0.65 |       62 | 54.91%     | ok               |
|          15 | 13.32%   | 50.45%             | -15.70% |     0.47 |       65 | 57.40%     | ok               |
|          25 | 6.47%    | 50.45%             | -16.10% |     0.28 |       58 | 53.08%     | ok               |
|          30 | -0.60%   | 50.45%             | -18.77% |     0.04 |       66 | 51.25%     | ok               |
|          40 | -2.83%   | 50.45%             | -20.44% |    -0.05 |       68 | 44.59%     | ok               |

## VWO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -9.03%   | 48.96%             | -24.01% |    -0.26 |       69 | 49.42%     | ok               |
|          50 | -7.89%   | 48.96%             | -21.68% |    -0.28 |       60 | 32.45%     | ok               |
|          20 | -10.06%  | 48.96%             | -26.14% |    -0.31 |       67 | 47.25%     | ok               |
|          40 | -8.98%   | 48.96%             | -23.57% |    -0.31 |       70 | 37.94%     | ok               |
|          45 | -9.69%   | 48.96%             | -23.75% |    -0.35 |       62 | 34.94%     | ok               |

## VZ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -8.99%   | 6.57%              | -14.18% |    -0.27 |       52 | 24.63%     | ok               |
|          45 | -17.16%  | 6.57%              | -19.37% |    -0.56 |       60 | 27.62%     | ok               |
|          35 | -22.06%  | 6.57%              | -22.13% |    -0.73 |       63 | 33.11%     | ok               |
|          25 | -27.26%  | 6.57%              | -26.75% |    -0.85 |       82 | 41.26%     | ok               |
|          40 | -24.76%  | 6.57%              | -24.24% |    -0.87 |       66 | 30.12%     | ok               |

## WFC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -1.37%   | 71.48%             | -18.29% |     0.02 |       58 | 34.11%     | ok               |
|          35 | -6.42%   | 71.48%             | -22.53% |    -0.06 |       79 | 45.92%     | ok               |
|          45 | -9.36%   | 71.48%             | -24.02% |    -0.2  |       66 | 38.94%     | ok               |
|          20 | -17.13%  | 71.48%             | -29.87% |    -0.24 |       79 | 54.91%     | ok               |
|          40 | -12.98%  | 71.48%             | -24.88% |    -0.31 |       76 | 42.26%     | ok               |

## WIF-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 60.65%   | -86.55%            | -46.21% |     0.66 |       71 | 41.38%     | ok               |
|          20 | 54.98%   | -86.55%            | -40.67% |     0.64 |       65 | 38.70%     | ok               |
|          25 | -11.37%  | -86.55%            | -52.41% |     0.2  |       67 | 36.21%     | ok               |
|          50 | -20.06%  | -86.55%            | -37.87% |    -0.14 |       40 | 12.07%     | ok               |
|          30 | -43.81%  | -86.55%            | -57.06% |    -0.24 |       68 | 32.18%     | ok               |

## WMT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 57.61%   | 103.84%            | -9.18%  |     1.51 |       36 | 43.09%     | ok               |
|          50 | 51.20%   | 103.84%            | -12.19% |     1.44 |       30 | 40.93%     | ok               |
|          40 | 47.75%   | 103.84%            | -9.18%  |     1.27 |       40 | 44.26%     | ok               |
|          35 | 44.97%   | 103.84%            | -10.48% |     1.18 |       52 | 48.42%     | ok               |
|          30 | 20.63%   | 103.84%            | -21.31% |     0.59 |       59 | 51.08%     | ok               |

## XBI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 8.73%    | 79.06%             | -16.56% |     0.29 |       62 | 35.11%     | ok               |
|          45 | 7.89%    | 79.06%             | -16.74% |     0.28 |       54 | 31.95%     | ok               |
|          35 | 6.50%    | 79.06%             | -19.52% |     0.24 |       62 | 38.77%     | ok               |
|          30 | 5.32%    | 79.06%             | -19.90% |     0.21 |       62 | 40.43%     | ok               |
|          25 | 0.47%    | 79.06%             | -24.31% |     0.1  |       70 | 42.43%     | ok               |

## XLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -1.55%   | 25.12%             | -20.60% |    -0    |       58 | 31.78%     | ok               |
|          50 | -1.49%   | 25.12%             | -17.40% |    -0.01 |       42 | 27.45%     | ok               |
|          45 | -4.40%   | 25.12%             | -20.61% |    -0.13 |       42 | 28.95%     | ok               |
|          35 | -4.89%   | 25.12%             | -23.62% |    -0.13 |       58 | 35.27%     | ok               |
|          25 | -8.18%   | 25.12%             | -23.73% |    -0.24 |       66 | 40.93%     | ok               |

## XLC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 15.42%   | 37.22%             | -12.33% |     0.54 |       65 | 55.57%     | ok               |
|          25 | 13.25%   | 37.22%             | -12.31% |     0.47 |       62 | 57.40%     | ok               |
|          40 | 10.18%   | 37.22%             | -13.38% |     0.41 |       68 | 48.09%     | ok               |
|          35 | 10.16%   | 37.22%             | -13.38% |     0.41 |       64 | 52.58%     | ok               |
|          20 | 5.29%    | 37.22%             | -13.78% |     0.23 |       70 | 60.07%     | ok               |

## XLE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.02%   | 28.63%             | -25.98% |     0.07 |       54 | 36.94%     | ok               |
|          35 | -3.79%   | 28.63%             | -32.17% |    -0.02 |       65 | 44.59%     | ok               |
|          45 | -5.17%   | 28.63%             | -30.88% |    -0.07 |       62 | 39.60%     | ok               |
|          25 | -11.35%  | 28.63%             | -37.50% |    -0.2  |       81 | 49.92%     | ok               |
|          30 | -11.37%  | 28.63%             | -37.51% |    -0.22 |       73 | 46.76%     | ok               |

## XLF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.15%   | 38.63%             | -18.63% |    -0.15 |       68 | 53.74%     | ok               |
|          15 | -10.04%  | 38.63%             | -20.19% |    -0.29 |       76 | 56.57%     | ok               |
|          30 | -11.26%  | 38.63%             | -23.61% |    -0.37 |       76 | 48.25%     | ok               |
|          25 | -12.03%  | 38.63%             | -23.22% |    -0.39 |       77 | 50.42%     | ok               |
|          35 | -17.35%  | 38.63%             | -25.31% |    -0.68 |       66 | 44.76%     | ok               |

## XLI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 8.86%    | 58.99%             | -10.61% |     0.36 |       72 | 52.75%     | ok               |
|          20 | 6.01%    | 58.99%             | -12.74% |     0.28 |       63 | 48.25%     | ok               |
|          30 | 3.69%    | 58.99%             | -11.38% |     0.2  |       64 | 45.76%     | ok               |
|          50 | 3.10%    | 58.99%             | -9.25%  |     0.19 |       56 | 35.11%     | ok               |
|          45 | 3.09%    | 58.99%             | -12.27% |     0.18 |       62 | 36.94%     | ok               |

## XLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 83.95%   | 82.94%             | -14.75% |     1.34 |       41 | 52.75%     | ok               |
|          20 | 69.56%   | 82.94%             | -14.75% |     1.2  |       48 | 50.58%     | ok               |
|          25 | 66.11%   | 82.94%             | -14.75% |     1.2  |       42 | 48.42%     | ok               |
|          30 | 63.94%   | 82.94%             | -14.75% |     1.19 |       42 | 47.25%     | ok               |
|          35 | 45.65%   | 82.94%             | -13.61% |     0.96 |       54 | 44.59%     | ok               |

## XLM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 26.14%   | -58.28%            | -38.97% |     0.48 |       44 | 27.39%     | ok               |
|          45 | 22.34%   | -58.28%            | -43.99% |     0.44 |       50 | 31.03%     | ok               |
|          30 | 0.26%    | -58.28%            | -50.36% |     0.22 |       69 | 45.59%     | ok               |
|          40 | -3.03%   | -58.28%            | -43.80% |     0.17 |       49 | 35.25%     | ok               |
|          35 | -8.51%   | -58.28%            | -50.42% |     0.12 |       69 | 41.57%     | ok               |

## XLP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 11.69%   | 14.46%             | -5.66%  |     0.71 |       54 | 34.28%     | ok               |
|          50 | 9.69%    | 14.46%             | -6.08%  |     0.61 |       58 | 31.78%     | ok               |
|          40 | 9.44%    | 14.46%             | -7.77%  |     0.57 |       70 | 38.44%     | ok               |
|          35 | 8.49%    | 14.46%             | -9.73%  |     0.51 |       66 | 41.43%     | ok               |
|          30 | 6.56%    | 14.46%             | -11.16% |     0.4  |       68 | 42.93%     | ok               |

## XLU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 10.52%   | 52.86%             | -9.11%  |     0.55 |       48 | 29.95%     | ok               |
|          45 | 8.24%    | 52.86%             | -10.56% |     0.44 |       52 | 30.95%     | ok               |
|          40 | 4.79%    | 52.86%             | -11.94% |     0.27 |       58 | 32.61%     | ok               |
|          35 | -1.31%   | 52.86%             | -16.24% |    -0.02 |       62 | 34.78%     | ok               |
|          30 | -3.67%   | 52.86%             | -18.15% |    -0.13 |       67 | 37.94%     | ok               |

## XLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -12.12%  | 12.86%             | -16.83% |    -0.59 |       66 | 35.61%     | ok               |
|          25 | -13.41%  | 12.86%             | -18.06% |    -0.66 |       68 | 36.94%     | ok               |
|          15 | -17.34%  | 12.86%             | -21.47% |    -0.84 |       79 | 41.76%     | ok               |
|          20 | -17.27%  | 12.86%             | -21.56% |    -0.86 |       73 | 38.60%     | ok               |
|          50 | -14.45%  | 12.86%             | -18.24% |    -0.87 |       54 | 24.29%     | ok               |

## XLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 4.62%    | 33.99%             | -12.94% |     0.21 |       72 | 41.26%     | ok               |
|          30 | 2.75%    | 33.99%             | -14.01% |     0.15 |       72 | 44.26%     | ok               |
|          15 | 1.20%    | 33.99%             | -15.77% |     0.11 |       74 | 51.25%     | ok               |
|          50 | 1.30%    | 33.99%             | -11.79% |     0.1  |       50 | 29.62%     | ok               |
|          40 | -1.91%   | 33.99%             | -16.99% |    -0.01 |       68 | 37.10%     | ok               |

## XOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 5.95%    | 33.98%             | -19.90% |     0.24 |       58 | 37.27%     | ok               |
|          30 | 4.90%    | 33.98%             | -20.29% |     0.21 |       58 | 36.61%     | ok               |
|          20 | 2.03%    | 33.98%             | -25.56% |     0.13 |       63 | 39.77%     | ok               |
|          50 | 1.92%    | 33.98%             | -21.35% |     0.13 |       46 | 29.95%     | ok               |
|          35 | 0.44%    | 33.98%             | -20.93% |     0.09 |       60 | 35.44%     | ok               |

## XRP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -26.11%  | -66.31%            | -46.89% |    -0.16 |       70 | 40.61%     | ok               |
|          40 | -32.98%  | -66.31%            | -44.90% |    -0.31 |       62 | 34.48%     | ok               |
|          30 | -39.97%  | -66.31%            | -56.11% |    -0.38 |       74 | 45.02%     | ok               |
|          45 | -40.52%  | -66.31%            | -46.85% |    -0.47 |       62 | 30.08%     | ok               |
|          50 | -37.96%  | -66.31%            | -39.26% |    -0.53 |       64 | 22.41%     | ok               |

## YFI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -32.83%  | -78.41%            | -52.37% |    -0.46 |       62 | 27.20%     | ok               |
|          45 | -38.27%  | -78.41%            | -54.04% |    -0.66 |       64 | 22.61%     | ok               |
|          35 | -49.34%  | -78.41%            | -64.08% |    -0.73 |       73 | 34.67%     | ok               |
|          30 | -52.55%  | -78.41%            | -67.78% |    -0.75 |       81 | 40.80%     | ok               |
|          50 | -41.48%  | -78.41%            | -51.80% |    -0.84 |       52 | 17.43%     | ok               |

## ZEC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 127.78%  | 759.47%            | -24.66% |     0.91 |       48 | 23.37%     | ok               |
|          35 | 101.71%  | 759.47%            | -44.34% |     0.8  |       56 | 31.03%     | ok               |
|          25 | 70.20%   | 759.47%            | -48.59% |     0.68 |       59 | 39.85%     | ok               |
|          50 | 56.58%   | 759.47%            | -37.94% |     0.61 |       50 | 20.88%     | ok               |
|          30 | 55.36%   | 759.47%            | -47.68% |     0.61 |       65 | 36.59%     | ok               |
