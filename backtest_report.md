# Market Tracker Backtest Report

_Generated: 2026-09-14T04:51:20+00:00_

## Data Sources

- Crypto: Kraken -> Coinbase -> CoinGecko OHLC -> CoinPaprika fallback chain.
- Stocks / ETFs / indices: Stooq -> Yahoo Finance fallback chain.
- Data rows are generated from real market APIs. Mock OHLCV rows are not generated.

## Data Freshness

- Rows: **92,678**
- Symbols: **161**
- Date range: **2024-04-19** to **2026-09-14**

## Latest Signals

| symbol     | date                |         close |   composite_score | signal   | data_source   |
|:-----------|:--------------------|--------------:|------------------:|:---------|:--------------|
| AAPL       | 2026-09-11 00:00:00 |   332.27      |         71.25     | LONG     | Yahoo Finance |
| AAVE-USD   | 2026-09-14 00:00:00 |   126.26      |         48.5      | LONG     | Kraken API    |
| BTC-USD    | 2026-09-14 00:00:00 | 77548         |         44.3333   | LONG     | Kraken API    |
| COP        | 2026-09-11 00:00:00 |   137.35      |         46.5833   | LONG     | Yahoo Finance |
| CRM        | 2026-09-11 00:00:00 |   247.72      |         58.75     | LONG     | Yahoo Finance |
| CSCO       | 2026-09-11 00:00:00 |   112.13      |         44.4167   | LONG     | Yahoo Finance |
| CVX        | 2026-09-11 00:00:00 |   214.06      |         71.0833   | LONG     | Yahoo Finance |
| DBC        | 2026-09-11 00:00:00 |    33.16      |         69.75     | LONG     | Yahoo Finance |
| DE         | 2026-09-11 00:00:00 |   675.74      |         71.5833   | LONG     | Yahoo Finance |
| DIS        | 2026-09-11 00:00:00 |   106.55      |         43.9167   | LONG     | Yahoo Finance |
| DOT-USD    | 2026-09-14 00:00:00 |     1.02      |         44.9167   | LONG     | Kraken API    |
| ETH-USD    | 2026-09-14 00:00:00 |  2513.19      |         49.5      | LONG     | Kraken API    |
| FET-USD    | 2026-09-14 00:00:00 |     0.1724    |         48.3333   | LONG     | Kraken API    |
| FIL-USD    | 2026-09-14 00:00:00 |     0.963     |         71.25     | LONG     | Kraken API    |
| IBIT       | 2026-09-11 00:00:00 |    43.77      |         52.0833   | LONG     | Yahoo Finance |
| ICP-USD    | 2026-09-14 00:00:00 |     2.777     |         71.1667   | LONG     | Kraken API    |
| INJ-USD    | 2026-09-14 00:00:00 |     6.176     |         73.3333   | LONG     | Kraken API    |
| INTC       | 2026-09-11 00:00:00 |   102.94      |         77.0833   | LONG     | Yahoo Finance |
| LINK-USD   | 2026-09-14 00:00:00 |    11.3862    |         30.5      | LONG     | Kraken API    |
| LTC-USD    | 2026-09-14 00:00:00 |    54.17      |         60.1667   | LONG     | Kraken API    |
| META       | 2026-09-11 00:00:00 |   648.03      |         50.75     | LONG     | Yahoo Finance |
| MPC        | 2026-09-11 00:00:00 |   395.93      |         67.0833   | LONG     | Yahoo Finance |
| MS         | 2026-09-11 00:00:00 |   214.38      |         35.4167   | LONG     | Yahoo Finance |
| NEAR-USD   | 2026-09-14 00:00:00 |     2.3965    |         67.6667   | LONG     | Kraken API    |
| NOW        | 2026-09-11 00:00:00 |   132.53      |         48.5833   | LONG     | Yahoo Finance |
| POL-USD    | 2026-09-14 00:00:00 |     0.09661   |         59.25     | LONG     | Kraken API    |
| QCOM       | 2026-09-11 00:00:00 |   181.97      |         79        | LONG     | Yahoo Finance |
| SLB        | 2026-09-11 00:00:00 |    56.06      |         30.5833   | LONG     | Yahoo Finance |
| SOL-USD    | 2026-09-14 00:00:00 |   101.08      |         43.8333   | LONG     | Kraken API    |
| SUSHI-USD  | 2026-09-14 00:00:00 |     0.2213    |         50.75     | LONG     | Kraken API    |
| T          | 2026-09-11 00:00:00 |    26.06      |         38.25     | LONG     | Yahoo Finance |
| TSLA       | 2026-09-11 00:00:00 |   365.44      |         31.4167   | LONG     | Yahoo Finance |
| TXN        | 2026-09-11 00:00:00 |   268.7       |         53.6667   | LONG     | Yahoo Finance |
| UNI-USD    | 2026-09-14 00:00:00 |     6.3897    |         44.8333   | LONG     | Kraken API    |
| USO        | 2026-09-11 00:00:00 |   154.9       |         69.5833   | LONG     | Yahoo Finance |
| VZ         | 2026-09-11 00:00:00 |    50.61      |         58.25     | LONG     | Yahoo Finance |
| XLE        | 2026-09-11 00:00:00 |    65.14      |         54.0833   | LONG     | Yahoo Finance |
| ZEC-USD    | 2026-09-14 00:00:00 |  1114.93      |         48.8333   | LONG     | Kraken API    |
| ABBV       | 2026-09-11 00:00:00 |   257.12      |         27.9167   | NEUTRAL  | Yahoo Finance |
| ADA-USD    | 2026-09-14 00:00:00 |     0.206839  |         -4        | NEUTRAL  | Kraken API    |
| ADBE       | 2026-09-11 00:00:00 |   252.23      |        -24.5833   | NEUTRAL  | Yahoo Finance |
| AGG        | 2026-09-11 00:00:00 |    95.98      |        -68.3333   | NEUTRAL  | Yahoo Finance |
| ALGO-USD   | 2026-09-14 00:00:00 |     0.09624   |         27.75     | NEUTRAL  | Kraken API    |
| AMAT       | 2026-09-11 00:00:00 |   456.49      |          5.16667  | NEUTRAL  | Yahoo Finance |
| AMD        | 2026-09-11 00:00:00 |   516.13      |         63.3333   | NEUTRAL  | Yahoo Finance |
| AMGN       | 2026-09-11 00:00:00 |   377.35      |         -8.33333  | NEUTRAL  | Yahoo Finance |
| AMZN       | 2026-09-11 00:00:00 |   256.78      |         15.1667   | NEUTRAL  | Yahoo Finance |
| APT-USD    | 2026-09-14 00:00:00 |     0.5973    |         -6.5      | NEUTRAL  | Kraken API    |
| ARB-USD    | 2026-09-14 00:00:00 |     0.1378    |         49.0833   | NEUTRAL  | Kraken API    |
| ARKK       | 2026-09-11 00:00:00 |    83.58      |         18.4167   | NEUTRAL  | Yahoo Finance |
| ATOM-USD   | 2026-09-14 00:00:00 |     1.5928    |         17.5833   | NEUTRAL  | Kraken API    |
| AVAX-USD   | 2026-09-14 00:00:00 |     7.405     |          5.5      | NEUTRAL  | Kraken API    |
| BAC        | 2026-09-11 00:00:00 |    62.69      |         42.5      | NEUTRAL  | Yahoo Finance |
| BCH-USD    | 2026-09-14 00:00:00 |   224.24      |        -64.5833   | NEUTRAL  | Kraken API    |
| BITO       | 2026-09-11 00:00:00 |    10.37      |         22.1667   | NEUTRAL  | Yahoo Finance |
| BLK        | 2026-09-11 00:00:00 |  1079.65      |         -5.33333  | NEUTRAL  | Yahoo Finance |
| BND        | 2026-09-11 00:00:00 |    71.22      |        -68.3333   | NEUTRAL  | Yahoo Finance |
| BONK-USD   | 2026-09-14 00:00:00 |     2.755e-06 |        -45.0833   | NEUTRAL  | Kraken API    |
| C          | 2026-09-11 00:00:00 |   138.82      |         43.5      | NEUTRAL  | Yahoo Finance |
| CAT        | 2026-09-11 00:00:00 |   818.57      |         -3.58333  | NEUTRAL  | Yahoo Finance |
| CL         | 2026-09-11 00:00:00 |    86.8       |        -46.0833   | NEUTRAL  | Yahoo Finance |
| COMP-USD   | 2026-09-14 00:00:00 |    19.79      |         27        | NEUTRAL  | Kraken API    |
| COST       | 2026-09-11 00:00:00 |   904.77      |        -60.5      | NEUTRAL  | Yahoo Finance |
| CRV-USD    | 2026-09-14 00:00:00 |     0.35356   |         33.0833   | NEUTRAL  | Kraken API    |
| DASH-USD   | 2026-09-14 00:00:00 |    54.864     |         49.0833   | NEUTRAL  | Kraken API    |
| DIA        | 2026-09-11 00:00:00 |   525.79      |        -20.3333   | NEUTRAL  | Yahoo Finance |
| DOGE-USD   | 2026-09-14 00:00:00 |     0.0840112 |          7.25     | NEUTRAL  | Kraken API    |
| DXY-INDEX  | 2026-09-14 00:00:00 |    99.338     |         27.957    | NEUTRAL  | Yahoo Finance |
| EEM        | 2026-09-11 00:00:00 |    67.84      |         58.6667   | NEUTRAL  | Yahoo Finance |
| EFA        | 2026-09-11 00:00:00 |   106.7       |         -4.66667  | NEUTRAL  | Yahoo Finance |
| EOG        | 2026-09-11 00:00:00 |   147.36      |         28.6667   | NEUTRAL  | Yahoo Finance |
| ETC-USD    | 2026-09-14 00:00:00 |     7.61      |         25.25     | NEUTRAL  | Kraken API    |
| EWJ        | 2026-09-11 00:00:00 |    98.56      |         69.8333   | NEUTRAL  | Yahoo Finance |
| FCX        | 2026-09-11 00:00:00 |    71.07      |          0.416667 | NEUTRAL  | Yahoo Finance |
| FXI        | 2026-09-11 00:00:00 |    34.49      |        -60        | NEUTRAL  | Yahoo Finance |
| GDX        | 2026-09-11 00:00:00 |    97.1       |         18.4167   | NEUTRAL  | Yahoo Finance |
| GDXJ       | 2026-09-11 00:00:00 |   125.41      |         18.4167   | NEUTRAL  | Yahoo Finance |
| GE         | 2026-09-11 00:00:00 |   323.66      |        -29.8333   | NEUTRAL  | Yahoo Finance |
| GLD        | 2026-09-11 00:00:00 |   398.77      |        -26.8333   | NEUTRAL  | Yahoo Finance |
| GOOGL      | 2026-09-11 00:00:00 |   338.5       |        -26.0833   | NEUTRAL  | Yahoo Finance |
| GRT-USD    | 2026-09-14 00:00:00 |     0.01886   |         28        | NEUTRAL  | Kraken API    |
| GS         | 2026-09-11 00:00:00 |  1029.18      |        -20        | NEUTRAL  | Yahoo Finance |
| HBAR-USD   | 2026-09-14 00:00:00 |     0.07617   |         23.5      | NEUTRAL  | Kraken API    |
| IBM        | 2026-09-11 00:00:00 |   243.29      |         24        | NEUTRAL  | Yahoo Finance |
| IEF        | 2026-09-11 00:00:00 |    91.01      |        -68.8333   | NEUTRAL  | Yahoo Finance |
| IEMG       | 2026-09-11 00:00:00 |    82.57      |         60.6667   | NEUTRAL  | Yahoo Finance |
| INTU       | 2026-09-11 00:00:00 |   321.57      |        -65.3333   | NEUTRAL  | Yahoo Finance |
| IWM        | 2026-09-11 00:00:00 |   288.89      |        -13.25     | NEUTRAL  | Yahoo Finance |
| JNJ        | 2026-09-11 00:00:00 |   265.58      |         -1.08333  | NEUTRAL  | Yahoo Finance |
| JPM        | 2026-09-11 00:00:00 |   356.23      |         41.5      | NEUTRAL  | Yahoo Finance |
| KO         | 2026-09-11 00:00:00 |    88.29      |         20.4167   | NEUTRAL  | Yahoo Finance |
| LDO-USD    | 2026-09-14 00:00:00 |     0.369     |          1.83333  | NEUTRAL  | Kraken API    |
| LIN        | 2026-09-11 00:00:00 |   466.22      |        -54.3333   | NEUTRAL  | Yahoo Finance |
| LRCX       | 2026-09-11 00:00:00 |   298.22      |        -23.0833   | NEUTRAL  | Yahoo Finance |
| MRK        | 2026-09-11 00:00:00 |   143.93      |         16.4167   | NEUTRAL  | Yahoo Finance |
| MSFT       | 2026-09-11 00:00:00 |   495.63      |         47.8333   | NEUTRAL  | Yahoo Finance |
| MU         | 2026-09-11 00:00:00 |   975.26      |         55.8333   | NEUTRAL  | Yahoo Finance |
| NEM        | 2026-09-11 00:00:00 |   126.81      |         18.4167   | NEUTRAL  | Yahoo Finance |
| NFLX       | 2026-09-11 00:00:00 |    77.4       |        -26.0833   | NEUTRAL  | Yahoo Finance |
| NVDA       | 2026-09-11 00:00:00 |   218.29      |         22.6667   | NEUTRAL  | Yahoo Finance |
| OP-USD     | 2026-09-14 00:00:00 |     0.096     |        -18.75     | NEUTRAL  | Kraken API    |
| ORCL       | 2026-09-11 00:00:00 |   150.28      |         32.0833   | NEUTRAL  | Yahoo Finance |
| OXY        | 2026-09-11 00:00:00 |    61.46      |         35.3333   | NEUTRAL  | Yahoo Finance |
| PEP        | 2026-09-11 00:00:00 |   136.32      |        -65.8333   | NEUTRAL  | Yahoo Finance |
| PEPE-USD   | 2026-09-14 00:00:00 |     3.44e-06  |        -10.6667   | NEUTRAL  | Kraken API    |
| PFE        | 2026-09-11 00:00:00 |    27.72      |          2.41667  | NEUTRAL  | Yahoo Finance |
| PG         | 2026-09-11 00:00:00 |   145.27      |          0.666667 | NEUTRAL  | Yahoo Finance |
| PM         | 2026-09-11 00:00:00 |   191.06      |         32.1667   | NEUTRAL  | Yahoo Finance |
| QQQ        | 2026-09-11 00:00:00 |   714.88      |         47.1667   | NEUTRAL  | Yahoo Finance |
| RENDER-USD | 2026-09-14 00:00:00 |     1.393     |        -39.0833   | NEUTRAL  | Kraken API    |
| SBUX       | 2026-09-11 00:00:00 |    98.74      |        -55.0833   | NEUTRAL  | Yahoo Finance |
| SCHW       | 2026-09-11 00:00:00 |   107.25      |          9.41667  | NEUTRAL  | Yahoo Finance |
| SHIB-USD   | 2026-09-14 00:00:00 |     5.224e-06 |         27.25     | NEUTRAL  | Kraken API    |
| SLV        | 2026-09-11 00:00:00 |    58.12      |        -55.8333   | NEUTRAL  | Yahoo Finance |
| SMH        | 2026-09-11 00:00:00 |   568.53      |         53.3333   | NEUTRAL  | Yahoo Finance |
| SNX-USD    | 2026-09-14 00:00:00 |     0.2162    |         -3.91667  | NEUTRAL  | Kraken API    |
| SOXX       | 2026-09-11 00:00:00 |   527.07      |         35.3333   | NEUTRAL  | Yahoo Finance |
| SPY        | 2026-09-11 00:00:00 |   764.29      |         13.5      | NEUTRAL  | Yahoo Finance |
| TGT        | 2026-09-11 00:00:00 |   155.83      |         16.4167   | NEUTRAL  | Yahoo Finance |
| TIA-USD    | 2026-09-14 00:00:00 |     0.3579    |         -2.5      | NEUTRAL  | Kraken API    |
| TLT        | 2026-09-11 00:00:00 |    80.87      |        -60.5      | NEUTRAL  | Yahoo Finance |
| TMO        | 2026-09-11 00:00:00 |   609.82      |         18.9167   | NEUTRAL  | Yahoo Finance |
| TMUS       | 2026-09-11 00:00:00 |   182.33      |         -2.83333  | NEUTRAL  | Yahoo Finance |
| TRX-USD    | 2026-09-14 00:00:00 |     0.338537  |         55.8333   | NEUTRAL  | Kraken API    |
| UNH        | 2026-09-11 00:00:00 |   379.09      |        -13        | NEUTRAL  | Yahoo Finance |
| UPS        | 2026-09-11 00:00:00 |   100.28      |        -55.5      | NEUTRAL  | Yahoo Finance |
| VEA        | 2026-09-11 00:00:00 |    72.69      |         -4.66667  | NEUTRAL  | Yahoo Finance |
| VIXY       | 2026-09-11 00:00:00 |    17.3       |         -6.75     | NEUTRAL  | Yahoo Finance |
| VTI        | 2026-09-11 00:00:00 |   376.31      |          6        | NEUTRAL  | Yahoo Finance |
| VWO        | 2026-09-11 00:00:00 |    60.35      |          1.16667  | NEUTRAL  | Yahoo Finance |
| WFC        | 2026-09-11 00:00:00 |    90.29      |         44        | NEUTRAL  | Yahoo Finance |
| WIF-USD    | 2026-09-14 00:00:00 |     0.1921    |         -6.41667  | NEUTRAL  | Kraken API    |
| WMT        | 2026-09-11 00:00:00 |   107.15      |         -2.08333  | NEUTRAL  | Yahoo Finance |
| XBI        | 2026-09-11 00:00:00 |   156.2       |        -10.5833   | NEUTRAL  | Yahoo Finance |
| XLB        | 2026-09-11 00:00:00 |    50.95      |        -36.8333   | NEUTRAL  | Yahoo Finance |
| XLC        | 2026-09-11 00:00:00 |   112.6       |         38.0833   | NEUTRAL  | Yahoo Finance |
| XLF        | 2026-09-11 00:00:00 |    57.25      |          4.33333  | NEUTRAL  | Yahoo Finance |
| XLI        | 2026-09-11 00:00:00 |   172.37      |        -23.6667   | NEUTRAL  | Yahoo Finance |
| XLK        | 2026-09-11 00:00:00 |   187.67      |         62        | NEUTRAL  | Yahoo Finance |
| XLM-USD    | 2026-09-14 00:00:00 |     0.182253  |         16.25     | NEUTRAL  | Kraken API    |
| XLP        | 2026-09-11 00:00:00 |    83.38      |        -47.75     | NEUTRAL  | Yahoo Finance |
| XLU        | 2026-09-11 00:00:00 |    42.39      |        -48.6667   | NEUTRAL  | Yahoo Finance |
| XLV        | 2026-09-11 00:00:00 |   165.36      |        -11.9167   | NEUTRAL  | Yahoo Finance |
| XLY        | 2026-09-11 00:00:00 |   112.96      |        -60.75     | NEUTRAL  | Yahoo Finance |
| XOM        | 2026-09-11 00:00:00 |   165.99      |         26.5      | NEUTRAL  | Yahoo Finance |
| XRP-USD    | 2026-09-14 00:00:00 |     1.37382   |         36.8333   | NEUTRAL  | Kraken API    |
| YFI-USD    | 2026-09-14 00:00:00 |  2186.6       |        -10.6667   | NEUTRAL  | Kraken API    |
| AVGO       | 2026-09-11 00:00:00 |   361.99      |        -31.25     | SHORT    | Yahoo Finance |
| BA         | 2026-09-11 00:00:00 |   210.45      |        -42.8333   | SHORT    | Yahoo Finance |
| CMCSA      | 2026-09-11 00:00:00 |    25.2       |        -44.5833   | SHORT    | Yahoo Finance |
| HD         | 2026-09-11 00:00:00 |   308.74      |        -54.9167   | SHORT    | Yahoo Finance |
| HON        | 2026-09-11 00:00:00 |   202.36      |        -54.4167   | SHORT    | Yahoo Finance |
| HYG        | 2026-09-11 00:00:00 |    78.6       |        -57.0833   | SHORT    | Yahoo Finance |
| ITA        | 2026-09-11 00:00:00 |   219.01      |        -55.4167   | SHORT    | Yahoo Finance |
| LLY        | 2026-09-11 00:00:00 |  1115.7       |        -35.3333   | SHORT    | Yahoo Finance |
| MCD        | 2026-09-11 00:00:00 |   252.53      |        -59.0833   | SHORT    | Yahoo Finance |
| NKE        | 2026-09-11 00:00:00 |    36.8       |        -59.0833   | SHORT    | Yahoo Finance |
| RTX        | 2026-09-11 00:00:00 |   197.68      |        -31.1667   | SHORT    | Yahoo Finance |
| SHY        | 2026-09-11 00:00:00 |    81.37      |        -57.5833   | SHORT    | Yahoo Finance |
| SKY-USD    | 2026-09-14 00:00:00 |     0.06265   |        -44.5833   | SHORT    | Kraken API    |
| VNQ        | 2026-09-11 00:00:00 |    94.8       |        -38.1667   | SHORT    | Yahoo Finance |

## Edge Summary

- Symbols with trades: **160** of 160
- Beat buy-and-hold: **29.38%** of traded symbols
- Positive return: **28.75%** of traded symbols
- Median strategy return: **-10.36%** (benchmark **23.01%**)
- Median excess vs benchmark: **-29.20%**
- Median Sharpe: **-0.15**
- Median exposure: **44.51%**

> Edge is real only if both _beat buy-and-hold_ and _median excess_ are convincingly positive across many symbols. Treat a single high-return symbol as noise.

## Portfolio Backtest

Actual capital-allocation books (not per-symbol averages). Benchmarks: `equal_weight_buyhold` (whole tracked universe), `spy_buyhold` (100% SPY), and `sixty_forty` (60% SPY / 40% AGG). `high_conf_voltarget` inverse-vol-weights the HIGH-confidence book; `conviction_long_short` is market-neutral. Judge on **Sharpe** and **max_drawdown** out-of-sample, not raw return: a fully-invested long book wins on return in a bull market but carries all the risk.

| strategy              | scope         | ann_return   | ann_vol   |   sharpe | max_drawdown   | total_return   |   avg_gross_exposure |
|:----------------------|:--------------|:-------------|:----------|---------:|:---------------|:---------------|---------------------:|
| equal_weight_buyhold  | full          | 10.65%       | 28.30%    |     0.38 | -39.63%        | 22.46%         |                 1    |
| equal_weight_buyhold  | out_of_sample | 9.59%        | 27.92%    |     0.34 | -29.33%        | 6.29%          |                 1    |
| all_signals_ew        | full          | -19.59%      | 23.85%    |    -0.82 | -62.21%        | -49.57%        |                 1    |
| all_signals_ew        | out_of_sample | 9.94%        | 23.18%    |     0.43 | -22.46%        | 8.08%          |                 1    |
| high_conf_ew          | full          | -1.51%       | 30.64%    |    -0.05 | -43.54%        | -17.07%        |                 0.89 |
| high_conf_ew          | out_of_sample | 28.07%       | 26.65%    |     1.05 | -22.62%        | 29.85%         |                 0.89 |
| high_conf_voltarget   | full          | -0.34%       | 27.54%    |    -0.01 | -35.66%        | -11.61%        |                 0.89 |
| high_conf_voltarget   | out_of_sample | 17.65%       | 22.68%    |     0.78 | -16.94%        | 17.40%         |                 0.89 |
| conviction_long_short | full          | -17.98%      | 22.40%    |    -0.8  | -49.93%        | -46.53%        |                 0.97 |
| conviction_long_short | out_of_sample | -9.87%       | 20.55%    |    -0.48 | -26.05%        | -12.01%        |                 0.97 |
| spy_buyhold           | full          | 7.24%        | 13.49%    |     0.54 | -19.00%        | 21.32%         |                 0.78 |
| spy_buyhold           | out_of_sample | 1.92%        | 9.82%     |     0.2  | -12.06%        | 1.55%          |                 0.78 |
| sixty_forty           | full          | 4.24%        | 8.52%     |     0.5  | -11.66%        | 12.54%         |                 0.78 |
| sixty_forty           | out_of_sample | -0.70%       | 6.57%     |    -0.11 | -8.26%         | -0.97%         |                 0.78 |

## Walk-Forward Robustness

Each book measured across contiguous time folds (each a different regime). A book has durable edge only if `mean_sharpe` is positive, `min_sharpe` isn't deeply negative, and `pct_positive_folds` is high — a single great fold doesn't count. `fold_sharpes` lists each fold oldest-to-newest.

| strategy              |   n_folds |   mean_sharpe |   median_sharpe |   min_sharpe | pct_positive_folds   | mean_return   | fold_sharpes                 |
|:----------------------|----------:|--------------:|----------------:|-------------:|:---------------------|:--------------|:-----------------------------|
| equal_weight_buyhold  |         5 |          0.67 |            0.7  |        -1.34 | 80.00%               | 5.61%         | 1.97;0.70;0.68;-1.34;1.34    |
| all_signals_ew        |         5 |         -0.87 |           -0.89 |        -2.35 | 20.00%               | -9.71%        | -0.89;-2.29;-2.35;1.71;-0.51 |
| high_conf_ew          |         5 |         -0.07 |           -0.06 |        -2    | 40.00%               | -2.26%        | -0.14;-2.00;-0.06;1.04;0.82  |
| high_conf_voltarget   |         5 |          0.01 |            0.46 |        -1.88 | 80.00%               | -1.85%        | 0.46;-1.88;0.01;0.49;0.94    |
| conviction_long_short |         5 |         -0.89 |           -0.81 |        -1.91 | 20.00%               | -11.40%       | -1.91;-1.24;-0.81;0.28;-0.76 |
| spy_buyhold           |         5 |          0.65 |            0.56 |        -0.58 | 60.00%               | 4.31%         | 2.52;-0.11;0.56;-0.58;0.85   |
| sixty_forty           |         5 |          0.58 |            0.42 |        -0.75 | 60.00%               | 2.56%         | 2.63;-0.12;0.74;-0.75;0.42   |

## Strategy Comparison

Each decision rule backtested over the same data. `out_of_sample` is the most recent ~35% of each symbol's history (unseen tail). A rule has real edge only if `median_excess` and `beat_benchmark_pct` stay positive out-of-sample, not just full-sample.

| strategy        | scope         |   symbols | beat_benchmark_pct   | positive_pct   | median_return   | median_benchmark   | median_excess   |   median_sharpe |   total_trades |
|:----------------|:--------------|----------:|:---------------------|:---------------|:----------------|:-------------------|:----------------|----------------:|---------------:|
| trend           | full          |       160 | 29.38%               | 28.75%         | -10.36%         | 23.01%             | -29.20%         |           -0.15 |          11351 |
| trend           | out_of_sample |       160 | 28.75%               | 47.50%         | -0.68%          | 7.29%              | -10.96%         |            0.02 |           3747 |
| mean_reversion  | full          |       156 | 34.62%               | 48.72%         | -0.17%          | 19.50%             | -20.33%         |            0    |           1288 |
| mean_reversion  | out_of_sample |       119 | 36.97%               | 56.30%         | 0.39%           | 4.87%              | -7.07%          |            0.22 |            502 |
| regime_adaptive | full          |       160 | 28.75%               | 30.00%         | -11.14%         | 23.01%             | -29.69%         |           -0.15 |          11624 |
| regime_adaptive | out_of_sample |       160 | 28.12%               | 48.75%         | -0.52%          | 7.29%              | -11.30%         |            0.05 |           3880 |

## Signal Calibration

Realized forward return in the signal's direction, grouped by confidence. HIGH should outrank LOW for the confidence score to be meaningful.

| confidence_level   |   horizon |     n | mean_return   | median_return   | win_rate   |
|:-------------------|----------:|------:|:--------------|:----------------|:-----------|
| HIGH               |         5 |  7883 | 0.11%         | 0.06%           | 51.08%     |
| MEDIUM             |         5 | 28969 | -0.03%        | 0.02%           | 50.21%     |
| LOW                |         5 |  3595 | -0.47%        | -0.45%          | 45.65%     |
| ALL                |         5 | 40447 | -0.04%        | 0.00%           | 49.97%     |
| HIGH               |        10 |  7806 | 0.39%         | 0.09%           | 51.11%     |
| MEDIUM             |        10 | 28695 | 0.09%         | 0.05%           | 50.39%     |
| LOW                |        10 |  3545 | -0.77%        | -0.59%          | 46.26%     |
| ALL                |        10 | 40046 | 0.07%         | 0.02%           | 50.17%     |
| HIGH               |        20 |  7663 | 0.88%         | 0.34%           | 52.88%     |
| MEDIUM             |        20 | 28158 | 0.66%         | 0.52%           | 52.94%     |
| LOW                |        20 |  3436 | -0.89%        | -0.61%          | 46.92%     |
| ALL                |        20 | 39257 | 0.57%         | 0.41%           | 52.40%     |

## Backtest Summary

### Data Quality / Signal Availability

- **ok**: 160 symbols

| symbol     |   trades | return   | benchmark_return   | mdd     |   sharpe | exposure   | skipped_reason   |
|:-----------|---------:|:---------|:-------------------|:--------|---------:|:-----------|:-----------------|
| AAPL       |       60 | 8.91%    | 101.38%            | -23.09% |     0.28 | 49.25%     | ok               |
| AAVE-USD   |       73 | -35.00%  | -7.52%             | -66.17% |    -0.19 | 42.15%     | ok               |
| ABBV       |       68 | -26.32%  | 54.51%             | -30.52% |    -0.6  | 47.42%     | ok               |
| ADA-USD    |       81 | -40.45%  | -66.83%            | -45.96% |    -0.34 | 47.13%     | ok               |
| ADBE       |       69 | -15.83%  | -45.76%            | -31.20% |    -0.1  | 56.24%     | ok               |
| AGG        |       71 | -8.24%   | 0.63%              | -11.23% |    -1.35 | 33.11%     | ok               |
| ALGO-USD   |       80 | -34.91%  | -46.51%            | -43.00% |    -0.29 | 39.27%     | ok               |
| AMAT       |       65 | -31.93%  | 140.55%            | -57.08% |    -0.28 | 49.25%     | ok               |
| AMD        |       54 | 10.09%   | 251.97%            | -41.09% |     0.31 | 34.61%     | ok               |
| AMGN       |       71 | -9.22%   | 40.32%             | -34.19% |    -0.1  | 50.75%     | ok               |
| AMZN       |       84 | -56.13%  | 47.04%             | -57.22% |    -1.6  | 41.60%     | ok               |
| APT-USD    |       78 | -39.97%  | -87.53%            | -65.32% |    -0.24 | 41.00%     | ok               |
| ARB-USD    |       77 | -14.96%  | -53.22%            | -58.79% |     0.14 | 43.10%     | ok               |
| ARKK       |       87 | -31.65%  | 99.00%             | -33.88% |    -0.48 | 44.59%     | ok               |
| ATOM-USD   |       88 | -59.36%  | -62.48%            | -60.59% |    -0.87 | 46.74%     | ok               |
| AVAX-USD   |       72 | -37.60%  | -61.37%            | -45.19% |    -0.38 | 38.12%     | ok               |
| AVGO       |       64 | 18.95%   | 200.48%            | -36.08% |     0.38 | 41.10%     | ok               |
| BA         |       69 | -0.67%   | 23.93%             | -27.11% |     0.12 | 49.75%     | ok               |
| BAC        |       78 | -11.79%  | 69.57%             | -27.64% |    -0.25 | 48.92%     | ok               |
| BCH-USD    |       80 | 21.83%   | -28.28%            | -53.87% |     0.43 | 49.23%     | ok               |
| BITO       |       76 | -14.56%  | -63.10%            | -39.47% |    -0.03 | 39.93%     | ok               |
| BLK        |       81 | -7.54%   | 43.96%             | -26.90% |    -0.14 | 47.92%     | ok               |
| BND        |       71 | -8.24%   | 0.61%              | -10.70% |    -1.3  | 34.94%     | ok               |
| BONK-USD   |       74 | 0.74%    | -78.04%            | -51.50% |     0.3  | 44.64%     | ok               |
| BTC-USD    |       64 | 25.30%   | -7.04%             | -23.38% |     0.54 | 51.92%     | ok               |
| C          |       77 | -31.81%  | 134.73%            | -39.51% |    -0.65 | 48.09%     | ok               |
| CAT        |       70 | 10.17%   | 130.80%            | -18.88% |     0.29 | 49.58%     | ok               |
| CL         |       60 | 5.41%    | -0.38%             | -14.32% |     0.24 | 41.26%     | ok               |
| CMCSA      |       82 | -45.64%  | -33.18%            | -49.38% |    -1.22 | 42.26%     | ok               |
| COMP-USD   |       97 | -46.68%  | -51.05%            | -56.58% |    -0.37 | 47.89%     | ok               |
| COP        |       72 | -17.39%  | 6.16%              | -43.40% |    -0.25 | 43.59%     | ok               |
| COST       |       60 | 2.04%    | 27.52%             | -29.73% |     0.13 | 41.93%     | ok               |
| CRM        |       67 | -29.08%  | -8.38%             | -45.51% |    -0.39 | 45.76%     | ok               |
| CRV-USD    |       70 | 35.40%   | -41.75%            | -39.89% |     0.53 | 41.95%     | ok               |
| CSCO       |       57 | 20.38%   | 132.06%            | -21.79% |     0.46 | 47.75%     | ok               |
| CVX        |       73 | -8.49%   | 33.79%             | -29.13% |    -0.15 | 41.26%     | ok               |
| DASH-USD   |       57 | -4.61%   | 167.55%            | -64.43% |     0.35 | 30.08%     | ok               |
| DBC        |       64 | -4.03%   | 41.47%             | -25.02% |    -0.07 | 34.44%     | ok               |
| DE         |       74 | -11.16%  | 68.80%             | -22.93% |    -0.15 | 43.93%     | ok               |
| DIA        |       66 | -5.37%   | 38.44%             | -12.94% |    -0.26 | 44.76%     | ok               |
| DIS        |       64 | -14.66%  | -5.38%             | -28.17% |    -0.24 | 43.43%     | ok               |
| DOGE-USD   |       72 | -30.09%  | -47.51%            | -62.31% |    -0.09 | 48.85%     | ok               |
| DOT-USD    |       92 | -62.57%  | -71.35%            | -66.16% |    -0.69 | 48.28%     | ok               |
| DXY-INDEX  |       38 | -2.86%   | -5.88%             | -6.02%  |    -0.44 | 29.87%     | ok               |
| EEM        |       64 | -10.43%  | 70.84%             | -25.67% |    -0.28 | 41.76%     | ok               |
| EFA        |       58 | -10.29%  | 40.17%             | -12.96% |    -0.4  | 41.26%     | ok               |
| EOG        |       83 | -31.56%  | 10.66%             | -47.57% |    -0.7  | 45.92%     | ok               |
| ETC-USD    |       62 | -32.24%  | -49.80%            | -48.09% |    -0.43 | 28.74%     | ok               |
| ETH-USD    |       58 | 161.22%  | 60.46%             | -30.11% |     1.37 | 46.17%     | ok               |
| EWJ        |       64 | -23.51%  | 48.23%             | -29.40% |    -0.82 | 37.10%     | ok               |
| FCX        |       67 | -32.40%  | 43.26%             | -47.67% |    -0.38 | 44.76%     | ok               |
| FET-USD    |       73 | -27.41%  | -61.50%            | -56.90% |    -0.05 | 38.89%     | ok               |
| FIL-USD    |       67 | -50.92%  | -60.76%            | -51.47% |    -0.68 | 32.57%     | ok               |
| FXI        |       46 | -4.88%   | 43.65%             | -23.91% |    -0.04 | 32.11%     | ok               |
| GDX        |       60 | -0.39%   | 185.00%            | -34.99% |     0.13 | 45.59%     | ok               |
| GDXJ       |       68 | -35.63%  | 197.25%            | -44.61% |    -0.45 | 43.59%     | ok               |
| GE         |       80 | -11.13%  | 118.60%            | -27.82% |    -0.09 | 48.09%     | ok               |
| GLD        |       54 | 5.93%    | 80.41%             | -14.86% |     0.23 | 45.59%     | ok               |
| GOOGL      |       55 | 66.13%   | 119.68%            | -20.41% |     1.07 | 48.09%     | ok               |
| GRT-USD    |       83 | -29.06%  | -76.24%            | -53.91% |    -0.2  | 42.34%     | ok               |
| GS         |       68 | 0.13%    | 154.75%            | -22.13% |     0.1  | 47.59%     | ok               |
| HD         |       71 | -3.44%   | -7.94%             | -17.37% |    -0.01 | 42.76%     | ok               |
| HON        |       94 | -22.06%  | 5.38%              | -33.57% |    -0.52 | 55.74%     | ok               |
| HYG        |       87 | -9.11%   | 3.45%              | -10.25% |    -1.06 | 35.11%     | ok               |
| IBIT       |       36 | 31.05%   | 15.15%             | -18.95% |     0.63 | 32.34%     | ok               |
| IBM        |       73 | -25.87%  | 33.99%             | -48.94% |    -0.31 | 50.75%     | ok               |
| ICP-USD    |       77 | -0.72%   | -44.93%            | -47.52% |     0.24 | 36.40%     | ok               |
| IEF        |       84 | -12.25%  | -0.80%             | -12.90% |    -1.74 | 33.28%     | ok               |
| IEMG       |       60 | -7.71%   | 65.04%             | -26.84% |    -0.2  | 41.43%     | ok               |
| INJ-USD    |       71 | -42.85%  | -25.07%            | -74.43% |    -0.31 | 37.93%     | ok               |
| INTC       |       68 | 43.04%   | 200.99%            | -60.60% |     0.55 | 48.25%     | ok               |
| INTU       |       71 | -17.93%  | -46.86%            | -42.15% |    -0.18 | 44.59%     | ok               |
| ITA        |       72 | -3.07%   | 71.10%             | -23.75% |    -0.01 | 48.25%     | ok               |
| IWM        |       54 | 10.50%   | 49.58%             | -13.37% |     0.43 | 36.27%     | ok               |
| JNJ        |       68 | -0.07%   | 79.56%             | -17.51% |     0.06 | 48.09%     | ok               |
| JPM        |       73 | -20.40%  | 91.73%             | -32.74% |    -0.53 | 48.09%     | ok               |
| KO         |       52 | 30.03%   | 46.73%             | -8.64%  |     1.02 | 40.43%     | ok               |
| LDO-USD    |       74 | 0.17%    | -49.24%            | -63.49% |     0.28 | 46.93%     | ok               |
| LIN        |       70 | -10.87%  | 4.46%              | -20.61% |    -0.35 | 36.27%     | ok               |
| LINK-USD   |       71 | 46.87%   | -10.08%            | -33.64% |     0.63 | 45.98%     | ok               |
| LLY        |       71 | -28.27%  | 53.61%             | -53.34% |    -0.42 | 47.92%     | ok               |
| LRCX       |       84 | -25.21%  | 242.68%            | -61.08% |    -0.15 | 42.43%     | ok               |
| LTC-USD    |       70 | -4.85%   | -28.97%            | -33.94% |     0.13 | 51.92%     | ok               |
| MCD        |       77 | -6.28%   | -7.15%             | -21.88% |    -0.21 | 37.10%     | ok               |
| META       |       80 | -36.06%  | 34.71%             | -44.90% |    -0.65 | 47.75%     | ok               |
| MPC        |       67 | 5.64%    | 101.61%            | -37.91% |     0.22 | 49.58%     | ok               |
| MRK        |       67 | -23.87%  | 14.43%             | -35.95% |    -0.46 | 44.26%     | ok               |
| MS         |       75 | -5.44%   | 136.47%            | -27.79% |    -0.05 | 47.92%     | ok               |
| MSFT       |       79 | -28.90%  | 24.18%             | -37.80% |    -0.66 | 49.58%     | ok               |
| MU         |       49 | 164.65%  | 813.42%            | -68.76% |     1.08 | 53.91%     | ok               |
| NEAR-USD   |       73 | 5.36%    | 14.56%             | -60.10% |     0.3  | 42.34%     | ok               |
| NEM        |       68 | -18.95%  | 224.99%            | -39.56% |    -0.11 | 53.24%     | ok               |
| NFLX       |       76 | 12.79%   | 39.45%             | -21.09% |     0.35 | 53.24%     | ok               |
| NKE        |       79 | -28.99%  | -61.07%            | -55.35% |    -0.34 | 43.43%     | ok               |
| NOW        |       84 | 4.13%    | -7.18%             | -30.43% |     0.22 | 49.75%     | ok               |
| NVDA       |       77 | -47.20%  | 66.66%             | -52.37% |    -0.61 | 57.75%     | ok               |
| OP-USD     |       70 | -42.45%  | -85.53%            | -68.74% |    -0.35 | 33.52%     | ok               |
| ORCL       |       68 | 87.31%   | 30.81%             | -30.61% |     0.81 | 55.07%     | ok               |
| OXY        |       75 | -5.18%   | -7.76%             | -31.22% |     0.03 | 44.26%     | ok               |
| PEP        |       74 | -1.12%   | -21.71%            | -21.35% |     0.04 | 45.92%     | ok               |
| PEPE-USD   |       89 | -39.87%  | -50.36%            | -57.66% |    -0.17 | 47.70%     | ok               |
| PFE        |       83 | -36.58%  | 6.62%              | -43.50% |    -1.08 | 39.93%     | ok               |
| PG         |       66 | -20.10%  | -8.14%             | -24.55% |    -0.77 | 37.60%     | ok               |
| PM         |       79 | -1.38%   | 103.75%            | -35.15% |     0.07 | 53.91%     | ok               |
| POL-USD    |       83 | 20.92%   | -47.13%            | -45.67% |     0.43 | 49.43%     | ok               |
| QCOM       |       75 | -17.79%  | 15.44%             | -56.59% |    -0.08 | 42.60%     | ok               |
| QQQ        |       66 | 13.22%   | 72.41%             | -14.20% |     0.41 | 46.42%     | ok               |
| RENDER-USD |      100 | -38.05%  | -62.51%            | -46.98% |    -0.18 | 45.59%     | ok               |
| RTX        |       56 | 31.76%   | 94.64%             | -16.99% |     0.72 | 52.91%     | ok               |
| SBUX       |       60 | -17.36%  | 12.70%             | -29.22% |    -0.31 | 37.60%     | ok               |
| SCHW       |       78 | -14.15%  | 46.08%             | -31.92% |    -0.27 | 47.92%     | ok               |
| SHIB-USD   |       84 | -37.87%  | -57.18%            | -41.47% |    -0.35 | 53.07%     | ok               |
| SHY        |       50 | -2.36%   | 0.25%              | -3.30%  |    -0.82 | 34.61%     | ok               |
| SKY-USD    |       82 | -35.34%  | 8.33%              | -47.99% |    -0.4  | 45.53%     | ok               |
| SLB        |       77 | -29.62%  | 12.46%             | -54.95% |    -0.5  | 50.92%     | ok               |
| SLV        |       70 | 8.66%    | 121.83%            | -42.66% |     0.28 | 42.10%     | ok               |
| SMH        |       48 | 69.07%   | 185.39%            | -33.66% |     1    | 44.76%     | ok               |
| SNX-USD    |       62 | -18.44%  | -66.53%            | -47.16% |    -0    | 33.52%     | ok               |
| SOL-USD    |       70 | -19.88%  | -16.73%            | -44.99% |    -0.01 | 59.20%     | ok               |
| SOXX       |       58 | 68.55%   | 165.67%            | -40.14% |     0.94 | 43.43%     | ok               |
| SPY        |       64 | 3.49%    | 54.35%             | -15.53% |     0.18 | 51.58%     | ok               |
| SUSHI-USD  |      104 | -82.98%  | -60.48%            | -82.74% |    -1.47 | 37.93%     | ok               |
| T          |       72 | 42.02%   | 57.84%             | -17.01% |     0.89 | 58.07%     | ok               |
| TGT        |       58 | -11.96%  | -7.41%             | -35.83% |    -0.19 | 37.60%     | ok               |
| TIA-USD    |       87 | -58.50%  | -85.80%            | -72.44% |    -0.51 | 41.57%     | ok               |
| TLT        |       74 | -19.41%  | -9.29%             | -22.36% |    -1.42 | 34.78%     | ok               |
| TMO        |       65 | 24.66%   | 11.94%             | -18.85% |     0.54 | 54.08%     | ok               |
| TMUS       |       76 | 2.41%    | 12.32%             | -27.06% |     0.15 | 48.25%     | ok               |
| TRX-USD    |       68 | 10.93%   | 39.28%             | -22.90% |     0.38 | 52.30%     | ok               |
| TSLA       |       78 | -33.82%  | 148.51%            | -58.36% |    -0.2  | 42.93%     | ok               |
| TXN        |       71 | -18.16%  | 68.27%             | -46.98% |    -0.14 | 49.25%     | ok               |
| UNH        |       74 | 32.56%   | -24.35%            | -26.31% |     0.55 | 50.25%     | ok               |
| UNI-USD    |       92 | -65.01%  | 22.10%             | -78.80% |    -0.63 | 48.47%     | ok               |
| UPS        |       70 | -35.47%  | -29.76%            | -38.84% |    -0.71 | 40.27%     | ok               |
| USO        |       70 | 9.87%    | 96.45%             | -41.71% |     0.28 | 32.11%     | ok               |
| VEA        |       60 | -6.13%   | 51.88%             | -19.49% |    -0.21 | 42.43%     | ok               |
| VIXY       |      100 | -78.86%  | -71.84%            | -88.17% |    -0.95 | 34.44%     | ok               |
| VNQ        |       75 | -17.42%  | 20.00%             | -24.92% |    -0.73 | 38.27%     | ok               |
| VTI        |       70 | -5.97%   | 53.45%             | -17.64% |    -0.16 | 51.75%     | ok               |
| VWO        |       80 | -16.62%  | 47.59%             | -25.20% |    -0.61 | 41.76%     | ok               |
| VZ         |       83 | -18.72%  | 24.99%             | -25.90% |    -0.55 | 40.60%     | ok               |
| WFC        |       80 | -17.12%  | 49.61%             | -28.90% |    -0.28 | 46.92%     | ok               |
| WIF-USD    |       66 | -38.16%  | -51.40%            | -52.76% |    -0.14 | 35.63%     | ok               |
| WMT        |       65 | 10.38%   | 79.99%             | -21.98% |     0.35 | 48.09%     | ok               |
| XBI        |       66 | -2.09%   | 88.58%             | -18.40% |     0.04 | 42.43%     | ok               |
| XLB        |       62 | -13.15%  | 14.55%             | -25.78% |    -0.47 | 31.78%     | ok               |
| XLC        |       63 | 14.20%   | 41.69%             | -12.33% |     0.52 | 50.58%     | ok               |
| XLE        |       77 | -13.44%  | 37.18%             | -35.51% |    -0.27 | 44.43%     | ok               |
| XLF        |       80 | -9.66%   | 41.78%             | -23.61% |    -0.3  | 45.92%     | ok               |
| XLI        |       72 | -4.54%   | 43.08%             | -14.12% |    -0.13 | 40.93%     | ok               |
| XLK        |       40 | 66.88%   | 94.95%             | -14.75% |     1.23 | 47.42%     | ok               |
| XLM-USD    |       67 | -18.02%  | -22.04%            | -54.58% |     0    | 46.93%     | ok               |
| XLP        |       64 | 7.54%    | 12.01%             | -10.28% |     0.46 | 39.60%     | ok               |
| XLU        |       67 | -3.52%   | 29.57%             | -20.40% |    -0.11 | 39.27%     | ok               |
| XLV        |       68 | -15.42%  | 19.01%             | -19.16% |    -0.7  | 37.44%     | ok               |
| XLY        |       79 | -6.85%   | 33.08%             | -17.23% |    -0.15 | 46.09%     | ok               |
| XOM        |       59 | -1.19%   | 38.46%             | -20.29% |     0.05 | 35.27%     | ok               |
| XRP-USD    |       58 | 21.26%   | -32.08%            | -33.91% |     0.43 | 36.40%     | ok               |
| YFI-USD    |       81 | -68.18%  | -52.29%            | -72.54% |    -1.23 | 38.89%     | ok               |
| ZEC-USD    |       64 | 104.02%  | 2825.56%           | -56.50% |     0.8  | 40.61%     | ok               |

## AAPL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 15.72%   | 101.38%            | -22.53% |     0.39 |       69 | 54.08%     | ok               |
|          15 | 11.54%   | 101.38%            | -24.50% |     0.32 |       80 | 61.23%     | ok               |
|          40 | 9.00%    | 101.38%            | -28.08% |     0.28 |       54 | 43.93%     | ok               |
|          30 | 8.91%    | 101.38%            | -23.09% |     0.28 |       60 | 49.25%     | ok               |
|          35 | 7.35%    | 101.38%            | -24.45% |     0.25 |       60 | 47.92%     | ok               |

## AAVE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 42.35%   | -7.52%             | -43.61% |     0.6  |       43 | 35.25%     | ok               |
|          45 | 29.09%   | -7.52%             | -49.19% |     0.5  |       48 | 30.08%     | ok               |
|          35 | 24.17%   | -7.52%             | -48.79% |     0.45 |       51 | 38.31%     | ok               |
|          50 | 6.06%    | -7.52%             | -45.07% |     0.26 |       44 | 22.03%     | ok               |
|          15 | -24.80%  | -7.52%             | -61.76% |     0.04 |       76 | 56.13%     | ok               |

## ABBV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -14.35%  | 54.51%             | -26.55% |    -0.31 |       52 | 35.44%     | ok               |
|          25 | -26.41%  | 54.51%             | -30.41% |    -0.59 |       67 | 49.25%     | ok               |
|          40 | -24.31%  | 54.51%             | -27.36% |    -0.59 |       68 | 39.93%     | ok               |
|          30 | -26.32%  | 54.51%             | -30.52% |    -0.6  |       68 | 47.42%     | ok               |
|          20 | -26.97%  | 54.51%             | -29.62% |    -0.6  |       67 | 51.08%     | ok               |

## ADA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 11.41%   | -66.83%            | -35.54% |     0.32 |       50 | 25.86%     | ok               |
|          45 | 0.79%    | -66.83%            | -34.64% |     0.21 |       53 | 30.84%     | ok               |
|          40 | -17.13%  | -66.83%            | -40.73% |    -0    |       65 | 36.97%     | ok               |
|          35 | -22.70%  | -66.83%            | -42.89% |    -0.07 |       69 | 41.57%     | ok               |
|          15 | -35.32%  | -66.83%            | -48.11% |    -0.1  |       74 | 63.98%     | ok               |

## ADBE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -3.35%   | -45.76%            | -29.07% |     0.1  |       53 | 60.07%     | ok               |
|          35 | -6.28%   | -45.76%            | -30.52% |     0.02 |       78 | 47.59%     | ok               |
|          20 | -13.05%  | -45.76%            | -31.52% |    -0.04 |       57 | 63.06%     | ok               |
|          30 | -15.83%  | -45.76%            | -31.20% |    -0.1  |       69 | 56.24%     | ok               |
|          40 | -15.64%  | -45.76%            | -31.90% |    -0.17 |       70 | 40.10%     | ok               |

## AGG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -5.36%   | 0.63%              | -8.21%  |    -1.17 |       52 | 18.64%     | ok               |
|          20 | -9.02%   | 0.63%              | -11.83% |    -1.33 |       72 | 38.27%     | ok               |
|          30 | -8.24%   | 0.63%              | -11.23% |    -1.35 |       71 | 33.11%     | ok               |
|          25 | -8.94%   | 0.63%              | -12.22% |    -1.37 |       71 | 36.44%     | ok               |
|          45 | -7.34%   | 0.63%              | -9.31%  |    -1.4  |       62 | 23.46%     | ok               |

## ALGO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -34.91%  | -46.51%            | -43.00% |    -0.29 |       80 | 39.27%     | ok               |
|          15 | -40.56%  | -46.51%            | -51.70% |    -0.3  |       80 | 50.19%     | ok               |
|          25 | -44.02%  | -46.51%            | -59.19% |    -0.41 |       80 | 44.83%     | ok               |
|          20 | -46.81%  | -46.51%            | -55.13% |    -0.44 |       82 | 47.70%     | ok               |
|          35 | -46.20%  | -46.51%            | -49.75% |    -0.62 |       62 | 32.76%     | ok               |

## AMAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -26.70%  | 140.55%            | -53.90% |    -0.15 |       68 | 58.57%     | ok               |
|          30 | -31.93%  | 140.55%            | -57.08% |    -0.28 |       65 | 49.25%     | ok               |
|          35 | -31.65%  | 140.55%            | -54.63% |    -0.29 |       65 | 46.76%     | ok               |
|          50 | -29.89%  | 140.55%            | -47.29% |    -0.3  |       46 | 35.11%     | ok               |
|          40 | -35.34%  | 140.55%            | -55.84% |    -0.37 |       63 | 42.10%     | ok               |

## AMD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 14.50%   | 251.97%            | -40.05% |     0.34 |       56 | 29.45%     | ok               |
|          40 | 10.09%   | 251.97%            | -41.09% |     0.31 |       54 | 34.61%     | ok               |
|          35 | 7.82%    | 251.97%            | -43.15% |     0.29 |       62 | 36.11%     | ok               |
|          30 | -0.70%   | 251.97%            | -46.73% |     0.21 |       63 | 38.77%     | ok               |
|          25 | -7.52%   | 251.97%            | -52.53% |     0.15 |       63 | 41.43%     | ok               |

## AMGN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -3.22%   | 40.32%             | -31.29% |     0.03 |       65 | 46.92%     | ok               |
|          20 | -4.40%   | 40.32%             | -26.65% |     0.02 |       66 | 56.57%     | ok               |
|          15 | -8.30%   | 40.32%             | -27.98% |    -0.05 |       63 | 60.57%     | ok               |
|          30 | -9.22%   | 40.32%             | -34.19% |    -0.1  |       71 | 50.75%     | ok               |
|          25 | -11.22%  | 40.32%             | -33.47% |    -0.13 |       65 | 53.08%     | ok               |

## AMZN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -25.14%  | 47.04%             | -27.34% |    -0.75 |       54 | 30.45%     | ok               |
|          50 | -29.72%  | 47.04%             | -32.41% |    -1.07 |       50 | 23.46%     | ok               |
|          45 | -35.00%  | 47.04%             | -36.26% |    -1.23 |       56 | 26.96%     | ok               |
|          35 | -51.09%  | 47.04%             | -51.92% |    -1.48 |       77 | 35.61%     | ok               |
|          30 | -56.13%  | 47.04%             | -57.22% |    -1.6  |       84 | 41.60%     | ok               |

## APT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -4.49%   | -87.53%            | -39.68% |     0.08 |       44 | 16.86%     | ok               |
|          20 | -37.70%  | -87.53%            | -66.07% |    -0.18 |       81 | 49.62%     | ok               |
|          45 | -26.14%  | -87.53%            | -58.83% |    -0.18 |       60 | 23.37%     | ok               |
|          35 | -32.69%  | -87.53%            | -57.66% |    -0.19 |       72 | 34.48%     | ok               |
|          25 | -39.46%  | -87.53%            | -65.88% |    -0.22 |       74 | 45.02%     | ok               |

## ARB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 60.29%   | -53.22%            | -45.20% |     0.66 |       83 | 59.96%     | ok               |
|          45 | 36.61%   | -53.22%            | -35.92% |     0.54 |       58 | 25.29%     | ok               |
|          40 | 26.69%   | -53.22%            | -39.80% |     0.47 |       57 | 33.33%     | ok               |
|          20 | 23.21%   | -53.22%            | -53.77% |     0.47 |       69 | 53.83%     | ok               |
|          50 | 25.46%   | -53.22%            | -30.72% |     0.45 |       44 | 18.01%     | ok               |

## ARKK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -23.09%  | 99.00%             | -37.76% |    -0.22 |       92 | 56.24%     | ok               |
|          20 | -26.28%  | 99.00%             | -34.82% |    -0.3  |       89 | 51.91%     | ok               |
|          30 | -31.65%  | 99.00%             | -33.88% |    -0.48 |       87 | 44.59%     | ok               |
|          35 | -38.11%  | 99.00%             | -38.51% |    -0.68 |       88 | 41.76%     | ok               |
|          40 | -37.31%  | 99.00%             | -40.75% |    -0.69 |       80 | 36.94%     | ok               |

## ATOM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -39.29%  | -62.48%            | -48.20% |    -0.31 |       86 | 63.79%     | ok               |
|          25 | -49.40%  | -62.48%            | -53.09% |    -0.56 |       90 | 53.07%     | ok               |
|          20 | -56.75%  | -62.48%            | -59.03% |    -0.71 |       94 | 56.70%     | ok               |
|          30 | -59.36%  | -62.48%            | -60.59% |    -0.87 |       88 | 46.74%     | ok               |
|          45 | -56.01%  | -62.48%            | -56.63% |    -0.97 |       76 | 31.42%     | ok               |

## AVAX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 26.00%   | -61.37%            | -22.06% |     0.53 |       30 | 17.05%     | ok               |
|          40 | 18.88%   | -61.37%            | -26.27% |     0.42 |       32 | 24.14%     | ok               |
|          45 | 15.54%   | -61.37%            | -23.19% |     0.38 |       26 | 21.07%     | ok               |
|          15 | -7.37%   | -61.37%            | -42.39% |     0.15 |       70 | 52.30%     | ok               |
|          35 | -2.83%   | -61.37%            | -33.05% |     0.14 |       52 | 30.46%     | ok               |

## AVGO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 22.37%   | 200.48%            | -38.01% |     0.41 |       68 | 43.76%     | ok               |
|          30 | 18.95%   | 200.48%            | -36.08% |     0.38 |       64 | 41.10%     | ok               |
|          40 | 11.48%   | 200.48%            | -40.70% |     0.3  |       64 | 34.94%     | ok               |
|          35 | 11.37%   | 200.48%            | -37.55% |     0.3  |       72 | 38.10%     | ok               |
|          50 | 10.84%   | 200.48%            | -36.86% |     0.29 |       56 | 29.78%     | ok               |

## BA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 26.52%   | 23.93%             | -13.34% |     0.67 |       44 | 33.28%     | ok               |
|          35 | 20.45%   | 23.93%             | -21.02% |     0.45 |       70 | 45.76%     | ok               |
|          40 | 14.62%   | 23.93%             | -23.87% |     0.37 |       48 | 40.60%     | ok               |
|          25 | 2.08%    | 23.93%             | -29.13% |     0.16 |       72 | 53.08%     | ok               |
|          30 | -0.67%   | 23.93%             | -27.11% |     0.12 |       69 | 49.75%     | ok               |

## BAC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -1.31%   | 69.57%             | -18.41% |     0.06 |       80 | 53.41%     | ok               |
|          15 | -6.54%   | 69.57%             | -21.05% |    -0.07 |       84 | 58.40%     | ok               |
|          25 | -6.12%   | 69.57%             | -24.24% |    -0.08 |       78 | 51.41%     | ok               |
|          35 | -7.11%   | 69.57%             | -29.13% |    -0.13 |       70 | 45.09%     | ok               |
|          45 | -6.33%   | 69.57%             | -20.47% |    -0.14 |       64 | 36.27%     | ok               |

## BCH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 71.72%   | -28.28%            | -45.51% |     0.77 |       73 | 58.81%     | ok               |
|          20 | 41.98%   | -28.28%            | -45.82% |     0.58 |       69 | 55.36%     | ok               |
|          30 | 21.83%   | -28.28%            | -53.87% |     0.43 |       80 | 49.23%     | ok               |
|          25 | 21.31%   | -28.28%            | -51.09% |     0.43 |       70 | 51.92%     | ok               |
|          35 | -0.02%   | -28.28%            | -57.99% |     0.21 |       72 | 44.64%     | ok               |

## BITO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 0.07%    | -63.10%            | -31.98% |     0.14 |       54 | 23.96%     | ok               |
|          30 | -14.56%  | -63.10%            | -39.47% |    -0.03 |       76 | 39.93%     | ok               |
|          45 | -13.72%  | -63.10%            | -34.01% |    -0.07 |       60 | 27.45%     | ok               |
|          15 | -21.74%  | -63.10%            | -48.38% |    -0.07 |       85 | 48.59%     | ok               |
|          35 | -18.74%  | -63.10%            | -41.51% |    -0.1  |       68 | 35.77%     | ok               |

## BLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -1.18%   | 43.96%             | -20.79% |     0.04 |       88 | 44.26%     | ok               |
|          40 | -1.42%   | 43.96%             | -22.83% |     0.03 |       78 | 39.77%     | ok               |
|          20 | -3.69%   | 43.96%             | -21.48% |    -0.01 |       84 | 52.75%     | ok               |
|          25 | -5.07%   | 43.96%             | -24.62% |    -0.06 |       77 | 50.58%     | ok               |
|          30 | -7.54%   | 43.96%             | -26.90% |    -0.14 |       81 | 47.92%     | ok               |

## BND Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -7.16%   | 0.61%              | -10.21% |    -1.03 |       66 | 40.43%     | ok               |
|          25 | -7.80%   | 0.61%              | -11.27% |    -1.17 |       69 | 38.44%     | ok               |
|          15 | -8.85%   | 0.61%              | -11.52% |    -1.26 |       77 | 43.09%     | ok               |
|          30 | -8.24%   | 0.61%              | -10.70% |    -1.3  |       71 | 34.94%     | ok               |
|          40 | -9.19%   | 0.61%              | -11.70% |    -1.63 |       64 | 27.79%     | ok               |

## BONK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 122.32%  | -78.04%            | -35.57% |     1.05 |       46 | 22.03%     | ok               |
|          15 | 80.28%   | -78.04%            | -62.48% |     0.74 |       70 | 59.77%     | ok               |
|          25 | 59.03%   | -78.04%            | -54.47% |     0.66 |       71 | 51.34%     | ok               |
|          20 | 57.76%   | -78.04%            | -61.03% |     0.66 |       65 | 55.94%     | ok               |
|          45 | 29.98%   | -78.04%            | -47.53% |     0.5  |       66 | 27.78%     | ok               |

## BTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 65.88%   | -7.04%             | -12.20% |     1.17 |       38 | 32.18%     | ok               |
|          35 | 69.78%   | -7.04%             | -21.56% |     1.16 |       58 | 41.76%     | ok               |
|          40 | 66.03%   | -7.04%             | -14.50% |     1.16 |       40 | 35.82%     | ok               |
|          30 | 40.35%   | -7.04%             | -21.75% |     0.75 |       64 | 47.70%     | ok               |
|          50 | 31.38%   | -7.04%             | -19.38% |     0.73 |       38 | 26.63%     | ok               |

## C Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -10.42%  | 134.73%            | -21.80% |    -0.23 |       66 | 33.11%     | ok               |
|          45 | -21.42%  | 134.73%            | -29.60% |    -0.53 |       76 | 37.44%     | ok               |
|          25 | -28.35%  | 134.73%            | -36.44% |    -0.55 |       69 | 49.92%     | ok               |
|          15 | -32.54%  | 134.73%            | -38.43% |    -0.61 |       74 | 56.91%     | ok               |
|          20 | -31.40%  | 134.73%            | -37.39% |    -0.61 |       79 | 52.75%     | ok               |

## CAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 10.27%   | 130.80%            | -22.07% |     0.29 |       66 | 52.41%     | ok               |
|          30 | 10.17%   | 130.80%            | -18.88% |     0.29 |       70 | 49.58%     | ok               |
|          15 | 7.52%    | 130.80%            | -26.40% |     0.25 |       77 | 63.39%     | ok               |
|          20 | 5.21%    | 130.80%            | -21.30% |     0.21 |       78 | 56.07%     | ok               |
|          45 | 2.71%    | 130.80%            | -26.22% |     0.16 |       56 | 38.27%     | ok               |

## CL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 4.72%    | -0.38%             | -12.98% |     0.24 |       42 | 25.62%     | ok               |
|          30 | 5.41%    | -0.38%             | -14.32% |     0.24 |       60 | 41.26%     | ok               |
|          45 | 1.03%    | -0.38%             | -13.51% |     0.09 |       46 | 28.29%     | ok               |
|          35 | 0.39%    | -0.38%             | -13.83% |     0.07 |       62 | 37.60%     | ok               |
|          40 | -2.52%   | -0.38%             | -12.70% |    -0.04 |       56 | 32.28%     | ok               |

## CMCSA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -43.37%  | -33.18%            | -47.26% |    -0.99 |       91 | 56.74%     | ok               |
|          30 | -45.64%  | -33.18%            | -49.38% |    -1.22 |       82 | 42.26%     | ok               |
|          50 | -31.71%  | -33.18%            | -31.71% |    -1.27 |       48 | 13.31%     | ok               |
|          25 | -47.91%  | -33.18%            | -51.49% |    -1.28 |       89 | 47.42%     | ok               |
|          35 | -45.78%  | -33.18%            | -49.22% |    -1.31 |       96 | 36.61%     | ok               |

## COMP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -9.37%   | -51.05%            | -38.71% |     0.07 |       44 | 21.46%     | ok               |
|          30 | -46.68%  | -51.05%            | -56.58% |    -0.37 |       97 | 47.89%     | ok               |
|          25 | -51.95%  | -51.05%            | -55.45% |    -0.45 |       96 | 55.75%     | ok               |
|          40 | -50.65%  | -51.05%            | -54.08% |    -0.56 |       70 | 34.87%     | ok               |
|          15 | -60.17%  | -51.05%            | -61.96% |    -0.58 |      104 | 66.67%     | ok               |

## COP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -6.93%   | 6.16%              | -34.85% |    -0.07 |       50 | 29.78%     | ok               |
|          35 | -13.79%  | 6.16%              | -43.58% |    -0.18 |       71 | 40.43%     | ok               |
|          45 | -13.24%  | 6.16%              | -41.14% |    -0.21 |       62 | 33.61%     | ok               |
|          30 | -17.39%  | 6.16%              | -43.40% |    -0.25 |       72 | 43.59%     | ok               |
|          40 | -18.72%  | 6.16%              | -46.86% |    -0.33 |       68 | 36.77%     | ok               |

## COST Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 14.02%   | 27.52%             | -24.32% |     0.47 |       62 | 47.75%     | ok               |
|          25 | 10.99%   | 27.52%             | -24.73% |     0.39 |       61 | 44.93%     | ok               |
|          35 | 7.34%    | 27.52%             | -27.39% |     0.31 |       56 | 39.27%     | ok               |
|          30 | 2.04%    | 27.52%             | -29.73% |     0.13 |       60 | 41.93%     | ok               |
|          15 | -0.87%   | 27.52%             | -27.30% |     0.05 |       65 | 51.25%     | ok               |

## CRM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -21.42%  | -8.38%             | -34.84% |    -0.26 |       64 | 40.77%     | ok               |
|          15 | -27.03%  | -8.38%             | -47.54% |    -0.28 |       92 | 57.40%     | ok               |
|          40 | -25.24%  | -8.38%             | -40.30% |    -0.36 |       70 | 36.61%     | ok               |
|          25 | -28.84%  | -8.38%             | -47.11% |    -0.37 |       68 | 48.25%     | ok               |
|          20 | -30.90%  | -8.38%             | -48.38% |    -0.38 |       74 | 51.25%     | ok               |

## CRV-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 73.23%   | -41.75%            | -37.78% |     0.77 |       70 | 37.16%     | ok               |
|          40 | 43.53%   | -41.75%            | -38.86% |     0.59 |       60 | 32.76%     | ok               |
|          50 | 35.01%   | -41.75%            | -30.73% |     0.54 |       50 | 21.26%     | ok               |
|          30 | 35.40%   | -41.75%            | -39.89% |     0.53 |       70 | 41.95%     | ok               |
|          45 | 33.62%   | -41.75%            | -42.29% |     0.53 |       60 | 25.67%     | ok               |

## CSCO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 34.08%   | 132.06%            | -19.34% |     0.72 |       48 | 36.94%     | ok               |
|          45 | 29.55%   | 132.06%            | -19.34% |     0.63 |       49 | 38.60%     | ok               |
|          25 | 24.67%   | 132.06%            | -23.28% |     0.52 |       55 | 48.92%     | ok               |
|          35 | 22.86%   | 132.06%            | -23.68% |     0.5  |       51 | 45.26%     | ok               |
|          30 | 20.38%   | 132.06%            | -21.79% |     0.46 |       57 | 47.75%     | ok               |

## CVX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -2.95%   | 33.79%             | -24.33% |     0.01 |       73 | 43.59%     | ok               |
|          40 | -4.33%   | 33.79%             | -27.34% |    -0.05 |       77 | 36.44%     | ok               |
|          45 | -4.35%   | 33.79%             | -28.83% |    -0.06 |       67 | 32.78%     | ok               |
|          35 | -6.56%   | 33.79%             | -28.85% |    -0.1  |       69 | 38.60%     | ok               |
|          30 | -8.49%   | 33.79%             | -29.13% |    -0.15 |       73 | 41.26%     | ok               |

## DASH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 231.46%  | 167.55%            | -21.09% |     1.21 |       38 | 16.86%     | ok               |
|          40 | 147.83%  | 167.55%            | -25.22% |     0.97 |       44 | 23.18%     | ok               |
|          45 | 145.86%  | 167.55%            | -26.87% |     0.97 |       40 | 18.77%     | ok               |
|          30 | -4.61%   | 167.55%            | -64.43% |     0.35 |       57 | 30.08%     | ok               |
|          35 | -6.18%   | 167.55%            | -63.41% |     0.33 |       67 | 27.59%     | ok               |

## DBC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 1.16%    | 41.47%             | -26.79% |     0.1  |       78 | 39.77%     | ok               |
|          25 | -1.57%   | 41.47%             | -25.43% |     0.01 |       66 | 36.27%     | ok               |
|          20 | -2.67%   | 41.47%             | -25.96% |    -0.02 |       71 | 37.94%     | ok               |
|          30 | -4.03%   | 41.47%             | -25.02% |    -0.07 |       64 | 34.44%     | ok               |
|          35 | -3.96%   | 41.47%             | -23.42% |    -0.07 |       66 | 33.11%     | ok               |

## DE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -2.50%   | 68.80%             | -17.97% |     0.01 |       64 | 28.62%     | ok               |
|          20 | -9.77%   | 68.80%             | -26.00% |    -0.12 |       73 | 48.75%     | ok               |
|          45 | -8.81%   | 68.80%             | -21.83% |    -0.14 |       68 | 33.11%     | ok               |
|          25 | -11.01%  | 68.80%             | -24.31% |    -0.15 |       75 | 46.59%     | ok               |
|          30 | -11.16%  | 68.80%             | -22.93% |    -0.15 |       74 | 43.93%     | ok               |

## DIA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -2.74%   | 38.44%             | -11.28% |    -0.11 |       62 | 46.26%     | ok               |
|          35 | -2.75%   | 38.44%             | -13.15% |    -0.12 |       64 | 41.93%     | ok               |
|          30 | -5.37%   | 38.44%             | -12.94% |    -0.26 |       66 | 44.76%     | ok               |
|          20 | -6.13%   | 38.44%             | -13.85% |    -0.28 |       68 | 48.75%     | ok               |
|          40 | -6.68%   | 38.44%             | -15.06% |    -0.36 |       70 | 39.27%     | ok               |

## DIS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 21.21%   | -5.38%             | -12.35% |     0.65 |       46 | 25.29%     | ok               |
|          40 | -4.60%   | -5.38%             | -18.75% |    -0.01 |       61 | 33.78%     | ok               |
|          45 | -6.91%   | -5.38%             | -16.54% |    -0.09 |       47 | 29.12%     | ok               |
|          15 | -13.87%  | -5.38%             | -32.73% |    -0.17 |       91 | 55.07%     | ok               |
|          35 | -12.68%  | -5.38%             | -25.70% |    -0.2  |       75 | 40.10%     | ok               |

## DOGE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -0.22%   | -47.51%            | -59.36% |     0.28 |       78 | 64.37%     | ok               |
|          20 | -2.72%   | -47.51%            | -57.37% |     0.24 |       79 | 59.20%     | ok               |
|          25 | -13.79%  | -47.51%            | -55.33% |     0.12 |       71 | 54.98%     | ok               |
|          30 | -30.09%  | -47.51%            | -62.31% |    -0.09 |       72 | 48.85%     | ok               |
|          50 | -32.88%  | -47.51%            | -55.17% |    -0.28 |       58 | 23.75%     | ok               |

## DOT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -65.71%  | -71.35%            | -72.06% |    -0.59 |       83 | 63.98%     | ok               |
|          20 | -62.16%  | -71.35%            | -68.06% |    -0.6  |       93 | 60.15%     | ok               |
|          35 | -58.32%  | -71.35%            | -61.61% |    -0.61 |       84 | 41.76%     | ok               |
|          45 | -46.24%  | -71.35%            | -53.23% |    -0.61 |       54 | 30.65%     | ok               |
|          50 | -44.96%  | -71.35%            | -48.78% |    -0.65 |       62 | 24.90%     | ok               |

## DXY-INDEX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -2.86%   | -5.88%             | -6.02%  |    -0.44 |       38 | 29.87%     | ok               |
|          40 | -3.86%   | -5.88%             | -7.30%  |    -0.5  |       68 | 46.32%     | ok               |
|          45 | -4.24%   | -5.88%             | -8.14%  |    -0.59 |       60 | 35.93%     | ok               |
|          15 | -8.21%   | -5.88%             | -11.61% |    -0.8  |       91 | 72.94%     | ok               |
|          35 | -6.45%   | -5.88%             | -9.74%  |    -0.82 |       79 | 52.16%     | ok               |

## EEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -5.41%   | 70.84%             | -15.88% |    -0.14 |       54 | 34.11%     | ok               |
|          45 | -6.13%   | 70.84%             | -17.36% |    -0.16 |       54 | 35.77%     | ok               |
|          40 | -6.47%   | 70.84%             | -19.52% |    -0.17 |       66 | 37.94%     | ok               |
|          35 | -7.12%   | 70.84%             | -23.88% |    -0.17 |       68 | 39.93%     | ok               |
|          25 | -9.53%   | 70.84%             | -25.60% |    -0.25 |       65 | 43.09%     | ok               |

## EFA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -5.96%   | 40.17%             | -10.10% |    -0.16 |       64 | 49.92%     | ok               |
|          30 | -10.29%  | 40.17%             | -12.96% |    -0.4  |       58 | 41.26%     | ok               |
|          20 | -11.69%  | 40.17%             | -12.73% |    -0.43 |       69 | 46.92%     | ok               |
|          25 | -13.03%  | 40.17%             | -15.23% |    -0.51 |       66 | 44.26%     | ok               |
|          40 | -12.73%  | 40.17%             | -15.10% |    -0.55 |       66 | 37.44%     | ok               |

## EOG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -26.42%  | 10.66%             | -38.89% |    -0.63 |       56 | 32.28%     | ok               |
|          30 | -31.56%  | 10.66%             | -47.57% |    -0.7  |       83 | 45.92%     | ok               |
|          40 | -30.54%  | 10.66%             | -41.11% |    -0.74 |       66 | 35.61%     | ok               |
|          35 | -31.55%  | 10.66%             | -44.81% |    -0.75 |       79 | 40.77%     | ok               |
|          25 | -35.04%  | 10.66%             | -51.99% |    -0.77 |       84 | 48.92%     | ok               |

## ETC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -10.33%  | -49.80%            | -31.28% |    -0.07 |       28 | 15.71%     | ok               |
|          45 | -12.19%  | -49.80%            | -38.47% |    -0.09 |       28 | 17.62%     | ok               |
|          35 | -23.03%  | -49.80%            | -45.32% |    -0.26 |       48 | 24.90%     | ok               |
|          40 | -21.57%  | -49.80%            | -43.28% |    -0.27 |       38 | 20.50%     | ok               |
|          30 | -32.24%  | -49.80%            | -48.09% |    -0.43 |       62 | 28.74%     | ok               |

## ETH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 161.22%  | 60.46%             | -30.11% |     1.37 |       58 | 46.17%     | ok               |
|          30 | 128.31%  | 60.46%             | -32.89% |     1.16 |       62 | 53.64%     | ok               |
|          25 | 86.41%   | 60.46%             | -40.90% |     0.92 |       60 | 57.85%     | ok               |
|          40 | 59.54%   | 60.46%             | -33.11% |     0.81 |       62 | 38.31%     | ok               |
|          20 | 70.10%   | 60.46%             | -39.10% |     0.8  |       80 | 61.88%     | ok               |

## EWJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -24.14%  | 48.23%             | -30.00% |    -0.82 |       58 | 39.27%     | ok               |
|          30 | -23.51%  | 48.23%             | -29.40% |    -0.82 |       64 | 37.10%     | ok               |
|          25 | -26.33%  | 48.23%             | -29.85% |    -0.92 |       58 | 38.27%     | ok               |
|          15 | -28.45%  | 48.23%             | -31.15% |    -0.93 |       71 | 42.76%     | ok               |
|          45 | -24.47%  | 48.23%             | -27.68% |    -1    |       60 | 28.79%     | ok               |

## FCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -7.51%   | 43.26%             | -34.75% |     0.02 |       58 | 33.11%     | ok               |
|          50 | -8.62%   | 43.26%             | -27.30% |    -0.01 |       58 | 28.79%     | ok               |
|          40 | -19.37%  | 43.26%             | -43.78% |    -0.17 |       68 | 37.77%     | ok               |
|          30 | -32.40%  | 43.26%             | -47.67% |    -0.38 |       67 | 44.76%     | ok               |
|          35 | -36.57%  | 43.26%             | -50.89% |    -0.49 |       73 | 42.93%     | ok               |

## FET-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -23.35%  | -61.50%            | -63.21% |     0.06 |       90 | 51.15%     | ok               |
|          25 | -24.57%  | -61.50%            | -63.66% |     0.01 |       83 | 43.87%     | ok               |
|          15 | -31.55%  | -61.50%            | -59.58% |    -0.01 |       84 | 55.94%     | ok               |
|          30 | -27.41%  | -61.50%            | -56.90% |    -0.05 |       73 | 38.89%     | ok               |
|          45 | -35.88%  | -61.50%            | -44.36% |    -0.48 |       44 | 17.05%     | ok               |

## FIL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -38.90%  | -60.76%            | -49.44% |    -0.53 |       48 | 21.84%     | ok               |
|          50 | -36.55%  | -60.76%            | -37.86% |    -0.64 |       34 | 11.88%     | ok               |
|          30 | -50.92%  | -60.76%            | -51.47% |    -0.68 |       67 | 32.57%     | ok               |
|          35 | -53.60%  | -60.76%            | -54.93% |    -0.84 |       60 | 26.25%     | ok               |
|          15 | -66.60%  | -60.76%            | -66.97% |    -0.89 |       94 | 45.21%     | ok               |

## FXI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -4.62%   | 43.65%             | -22.57% |    -0.03 |       48 | 33.61%     | ok               |
|          30 | -4.88%   | 43.65%             | -23.91% |    -0.04 |       46 | 32.11%     | ok               |
|          15 | -8.62%   | 43.65%             | -21.68% |    -0.11 |       53 | 37.77%     | ok               |
|          20 | -8.25%   | 43.65%             | -24.53% |    -0.12 |       50 | 35.44%     | ok               |
|          35 | -8.56%   | 43.65%             | -27.53% |    -0.14 |       48 | 29.62%     | ok               |

## GDX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 4.31%    | 185.00%            | -35.59% |     0.21 |       74 | 49.92%     | ok               |
|          40 | 0.47%    | 185.00%            | -31.37% |     0.14 |       64 | 39.43%     | ok               |
|          30 | -0.39%   | 185.00%            | -34.99% |     0.13 |       60 | 45.59%     | ok               |
|          25 | -5.67%   | 185.00%            | -38.90% |     0.05 |       64 | 46.76%     | ok               |
|          35 | -5.74%   | 185.00%            | -31.88% |     0.04 |       72 | 42.26%     | ok               |

## GDXJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -25.63%  | 197.25%            | -44.73% |    -0.21 |       70 | 49.58%     | ok               |
|          50 | -30.22%  | 197.25%            | -46.83% |    -0.42 |       60 | 35.11%     | ok               |
|          30 | -35.63%  | 197.25%            | -44.61% |    -0.45 |       68 | 43.59%     | ok               |
|          25 | -39.93%  | 197.25%            | -46.95% |    -0.51 |       73 | 46.42%     | ok               |
|          35 | -38.81%  | 197.25%            | -41.76% |    -0.54 |       72 | 40.93%     | ok               |

## GE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 8.01%    | 118.60%            | -22.29% |     0.26 |       64 | 34.78%     | ok               |
|          45 | -3.87%   | 118.60%            | -25.68% |     0.03 |       74 | 37.27%     | ok               |
|          20 | -9.63%   | 118.60%            | -26.63% |    -0.05 |       75 | 52.08%     | ok               |
|          30 | -11.13%  | 118.60%            | -27.82% |    -0.09 |       80 | 48.09%     | ok               |
|          35 | -13.02%  | 118.60%            | -27.11% |    -0.14 |       82 | 42.76%     | ok               |

## GLD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 11.22%   | 80.41%             | -13.87% |     0.34 |       52 | 46.76%     | ok               |
|          20 | 9.34%    | 80.41%             | -13.87% |     0.3  |       55 | 48.59%     | ok               |
|          30 | 5.93%    | 80.41%             | -14.86% |     0.23 |       54 | 45.59%     | ok               |
|          35 | 3.12%    | 80.41%             | -15.53% |     0.16 |       56 | 43.26%     | ok               |
|          15 | 2.64%    | 80.41%             | -17.54% |     0.15 |       57 | 52.75%     | ok               |

## GOOGL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 70.24%   | 119.68%            | -18.25% |     1.14 |       57 | 44.59%     | ok               |
|          30 | 66.13%   | 119.68%            | -20.41% |     1.07 |       55 | 48.09%     | ok               |
|          45 | 55.91%   | 119.68%            | -14.13% |     1.03 |       50 | 37.94%     | ok               |
|          25 | 63.59%   | 119.68%            | -19.76% |     1.03 |       55 | 50.58%     | ok               |
|          40 | 52.42%   | 119.68%            | -19.94% |     0.96 |       48 | 39.60%     | ok               |

## GRT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 19.48%   | -76.24%            | -25.60% |     0.45 |       40 | 17.82%     | ok               |
|          15 | 7.49%    | -76.24%            | -45.50% |     0.32 |       74 | 61.11%     | ok               |
|          20 | -1.46%   | -76.24%            | -42.04% |     0.22 |       81 | 55.36%     | ok               |
|          25 | -19.78%  | -76.24%            | -51.18% |    -0    |       82 | 50.96%     | ok               |
|          45 | -13.82%  | -76.24%            | -47.52% |    -0.07 |       46 | 23.95%     | ok               |

## GS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 26.02%   | 154.75%            | -20.56% |     0.55 |       68 | 55.74%     | ok               |
|          20 | 6.66%    | 154.75%            | -23.19% |     0.23 |       68 | 52.41%     | ok               |
|          40 | 3.29%    | 154.75%            | -17.88% |     0.16 |       64 | 41.76%     | ok               |
|          25 | 1.26%    | 154.75%            | -23.32% |     0.13 |       68 | 49.92%     | ok               |
|          30 | 0.13%    | 154.75%            | -22.13% |     0.1  |       68 | 47.59%     | ok               |

## HD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -3.44%   | -7.94%             | -17.37% |    -0.01 |       71 | 42.76%     | ok               |
|          25 | -4.20%   | -7.94%             | -18.82% |    -0.03 |       70 | 44.76%     | ok               |
|          35 | -9.77%   | -7.94%             | -19.91% |    -0.21 |       78 | 38.77%     | ok               |
|          45 | -8.09%   | -7.94%             | -16.03% |    -0.21 |       54 | 27.62%     | ok               |
|          40 | -9.57%   | -7.94%             | -17.33% |    -0.24 |       80 | 32.61%     | ok               |

## HON Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -8.23%   | 5.38%              | -20.93% |    -0.18 |       70 | 34.44%     | ok               |
|          45 | -11.25%  | 5.38%              | -22.88% |    -0.26 |       70 | 40.27%     | ok               |
|          35 | -20.61%  | 5.38%              | -31.60% |    -0.5  |       88 | 50.92%     | ok               |
|          40 | -20.28%  | 5.38%              | -31.84% |    -0.51 |       74 | 44.43%     | ok               |
|          30 | -22.06%  | 5.38%              | -33.57% |    -0.52 |       94 | 55.74%     | ok               |

## HYG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -7.69%   | 3.45%              | -8.10%  |    -0.92 |       70 | 29.95%     | ok               |
|          30 | -9.11%   | 3.45%              | -10.25% |    -1.06 |       87 | 35.11%     | ok               |
|          25 | -9.70%   | 3.45%              | -11.06% |    -1.09 |       89 | 37.77%     | ok               |
|          35 | -9.24%   | 3.45%              | -9.90%  |    -1.1  |       81 | 31.95%     | ok               |
|          45 | -8.83%   | 3.45%              | -9.24%  |    -1.11 |       70 | 26.62%     | ok               |

## IBIT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 54.00%   | 15.15%             | -17.37% |     1    |       24 | 23.40%     | ok               |
|          15 | 57.19%   | 15.15%             | -19.20% |     0.9  |       42 | 39.36%     | ok               |
|          45 | 44.53%   | 15.15%             | -17.37% |     0.85 |       28 | 24.68%     | ok               |
|          40 | 38.29%   | 15.15%             | -17.78% |     0.76 |       28 | 26.38%     | ok               |
|          30 | 31.05%   | 15.15%             | -18.95% |     0.63 |       36 | 32.34%     | ok               |

## IBM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -20.22%  | 33.99%             | -49.43% |    -0.16 |       91 | 63.06%     | ok               |
|          35 | -24.24%  | 33.99%             | -47.10% |    -0.29 |       69 | 46.59%     | ok               |
|          30 | -25.87%  | 33.99%             | -48.94% |    -0.31 |       73 | 50.75%     | ok               |
|          20 | -30.94%  | 33.99%             | -53.45% |    -0.38 |       73 | 55.41%     | ok               |
|          50 | -29.24%  | 33.99%             | -45.88% |    -0.44 |       46 | 34.44%     | ok               |

## ICP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 4.43%    | -44.93%            | -45.07% |     0.25 |       70 | 30.27%     | ok               |
|          30 | -0.72%   | -44.93%            | -47.52% |     0.24 |       77 | 36.40%     | ok               |
|          40 | 3.61%    | -44.93%            | -38.04% |     0.24 |       58 | 25.29%     | ok               |
|          50 | -3.99%   | -44.93%            | -48.01% |     0.12 |       38 | 15.52%     | ok               |
|          15 | -31.11%  | -44.93%            | -58.26% |     0.01 |       75 | 48.85%     | ok               |

## IEF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -7.18%   | -0.80%             | -10.18% |    -0.87 |       72 | 41.93%     | ok               |
|          15 | -7.74%   | -0.80%             | -10.91% |    -0.92 |       71 | 43.43%     | ok               |
|          50 | -7.73%   | -0.80%             | -9.11%  |    -1.38 |       54 | 20.13%     | ok               |
|          25 | -10.73%  | -0.80%             | -11.68% |    -1.39 |       76 | 39.27%     | ok               |
|          40 | -9.13%   | -0.80%             | -10.79% |    -1.4  |       64 | 25.29%     | ok               |

## IEMG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.94%   | 65.04%             | -13.91% |     0.02 |       54 | 32.45%     | ok               |
|          45 | -1.75%   | 65.04%             | -14.92% |    -0.01 |       50 | 34.94%     | ok               |
|          35 | -2.63%   | 65.04%             | -22.13% |    -0.03 |       65 | 40.43%     | ok               |
|          40 | -3.27%   | 65.04%             | -18.43% |    -0.06 |       62 | 37.94%     | ok               |
|          25 | -6.92%   | 65.04%             | -25.58% |    -0.17 |       61 | 43.26%     | ok               |

## INJ-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -7.71%   | -25.07%            | -54.35% |     0.14 |       60 | 33.14%     | ok               |
|          45 | -10.72%  | -25.07%            | -47.58% |     0.05 |       50 | 24.14%     | ok               |
|          40 | -14.60%  | -25.07%            | -49.91% |     0.03 |       52 | 29.89%     | ok               |
|          30 | -42.85%  | -25.07%            | -74.43% |    -0.31 |       71 | 37.93%     | ok               |
|          15 | -51.45%  | -25.07%            | -81.76% |    -0.33 |       82 | 49.81%     | ok               |

## INTC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 74.86%   | 200.99%            | -49.32% |     0.74 |       58 | 33.28%     | ok               |
|          50 | 69.78%   | 200.99%            | -48.35% |     0.72 |       64 | 29.12%     | ok               |
|          15 | 65.00%   | 200.99%            | -53.65% |     0.65 |       80 | 59.90%     | ok               |
|          40 | 60.83%   | 200.99%            | -55.86% |     0.65 |       66 | 37.44%     | ok               |
|          25 | 48.47%   | 200.99%            | -56.41% |     0.58 |       79 | 50.75%     | ok               |

## INTU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 2.60%    | -46.86%            | -39.02% |     0.16 |       67 | 27.29%     | ok               |
|          45 | 0.60%    | -46.86%            | -40.08% |     0.13 |       65 | 31.28%     | ok               |
|          40 | -6.60%   | -46.86%            | -43.92% |     0    |       67 | 34.61%     | ok               |
|          25 | -9.57%   | -46.86%            | -39.21% |    -0.02 |       68 | 47.42%     | ok               |
|          15 | -13.56%  | -46.86%            | -43.23% |    -0.08 |       79 | 52.91%     | ok               |

## ITA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 1.07%    | 71.10%             | -21.48% |     0.1  |       72 | 38.10%     | ok               |
|          15 | -3.48%   | 71.10%             | -28.06% |     0    |       85 | 60.40%     | ok               |
|          30 | -3.07%   | 71.10%             | -23.75% |    -0.01 |       72 | 48.25%     | ok               |
|          35 | -5.10%   | 71.10%             | -23.16% |    -0.08 |       74 | 45.92%     | ok               |
|          40 | -5.28%   | 71.10%             | -20.58% |    -0.09 |       74 | 42.60%     | ok               |

## IWM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 12.85%   | 49.58%             | -12.34% |     0.5  |       54 | 37.27%     | ok               |
|          40 | 10.83%   | 49.58%             | -14.61% |     0.47 |       46 | 31.95%     | ok               |
|          35 | 10.58%   | 49.58%             | -14.64% |     0.44 |       52 | 34.28%     | ok               |
|          20 | 11.36%   | 49.58%             | -12.12% |     0.44 |       60 | 38.27%     | ok               |
|          30 | 10.50%   | 49.58%             | -13.37% |     0.43 |       54 | 36.27%     | ok               |

## JNJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 17.37%   | 79.56%             | -10.57% |     0.71 |       48 | 35.44%     | ok               |
|          15 | 9.08%    | 79.56%             | -18.02% |     0.34 |       64 | 55.07%     | ok               |
|          45 | 6.38%    | 79.56%             | -13.35% |     0.3  |       50 | 39.43%     | ok               |
|          20 | 4.04%    | 79.56%             | -17.61% |     0.2  |       70 | 51.58%     | ok               |
|          40 | 2.81%    | 79.56%             | -14.77% |     0.16 |       58 | 43.76%     | ok               |

## JPM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 6.98%    | 91.73%             | -15.90% |     0.29 |       52 | 35.27%     | ok               |
|          45 | -3.18%   | 91.73%             | -21.91% |    -0.03 |       54 | 38.27%     | ok               |
|          20 | -17.13%  | 91.73%             | -35.58% |    -0.33 |       82 | 52.41%     | ok               |
|          35 | -15.95%  | 91.73%             | -27.43% |    -0.42 |       74 | 44.59%     | ok               |
|          40 | -16.47%  | 91.73%             | -28.47% |    -0.44 |       66 | 40.93%     | ok               |

## KO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 30.03%   | 46.73%             | -8.64%  |     1.02 |       52 | 40.43%     | ok               |
|          35 | 24.82%   | 46.73%             | -8.21%  |     0.88 |       56 | 38.77%     | ok               |
|          40 | 21.82%   | 46.73%             | -9.28%  |     0.84 |       58 | 35.44%     | ok               |
|          25 | 23.52%   | 46.73%             | -10.16% |     0.82 |       58 | 43.26%     | ok               |
|          20 | 8.55%    | 46.73%             | -15.99% |     0.35 |       77 | 47.25%     | ok               |

## LDO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 39.36%   | -49.24%            | -48.17% |     0.57 |       76 | 60.15%     | ok               |
|          20 | 28.50%   | -49.24%            | -48.55% |     0.5  |       80 | 55.56%     | ok               |
|          30 | 0.17%    | -49.24%            | -63.49% |     0.28 |       74 | 46.93%     | ok               |
|          25 | -3.93%   | -49.24%            | -59.45% |     0.27 |       83 | 52.68%     | ok               |
|          35 | -11.87%  | -49.24%            | -64.26% |     0.14 |       78 | 38.70%     | ok               |

## LIN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -6.82%   | 4.46%              | -23.68% |    -0.17 |       70 | 46.09%     | ok               |
|          20 | -6.99%   | 4.46%              | -23.00% |    -0.18 |       64 | 41.93%     | ok               |
|          25 | -6.94%   | 4.46%              | -22.01% |    -0.19 |       67 | 39.10%     | ok               |
|          30 | -10.87%  | 4.46%              | -20.61% |    -0.35 |       70 | 36.27%     | ok               |
|          45 | -10.54%  | 4.46%              | -17.04% |    -0.42 |       42 | 20.47%     | ok               |

## LINK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 44.85%   | -10.08%            | -33.71% |     0.64 |       52 | 31.03%     | ok               |
|          30 | 46.87%   | -10.08%            | -33.64% |     0.63 |       71 | 45.98%     | ok               |
|          35 | 30.37%   | -10.08%            | -34.21% |     0.51 |       59 | 40.80%     | ok               |
|          40 | 23.21%   | -10.08%            | -34.00% |     0.45 |       55 | 35.06%     | ok               |
|          50 | 21.94%   | -10.08%            | -27.44% |     0.44 |       44 | 24.90%     | ok               |

## LLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 2.05%    | 53.61%             | -38.23% |     0.15 |       46 | 35.44%     | ok               |
|          15 | -6.71%   | 53.61%             | -48.12% |     0.04 |       65 | 58.40%     | ok               |
|          45 | -9.72%   | 53.61%             | -42.66% |    -0.08 |       52 | 38.77%     | ok               |
|          20 | -19.49%  | 53.61%             | -51.34% |    -0.2  |       72 | 53.58%     | ok               |
|          25 | -20.82%  | 53.61%             | -53.47% |    -0.24 |       68 | 50.92%     | ok               |

## LRCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -13.68%  | 242.68%            | -48.71% |    -0.02 |       76 | 33.61%     | ok               |
|          40 | -18.39%  | 242.68%            | -55.33% |    -0.06 |       72 | 39.60%     | ok               |
|          35 | -19.96%  | 242.68%            | -58.47% |    -0.08 |       80 | 41.76%     | ok               |
|          30 | -25.21%  | 242.68%            | -61.08% |    -0.15 |       84 | 42.43%     | ok               |
|          15 | -30.37%  | 242.68%            | -56.86% |    -0.16 |       87 | 52.25%     | ok               |

## LTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 2.43%    | -28.97%            | -34.94% |     0.21 |       68 | 44.25%     | ok               |
|          30 | -4.85%   | -28.97%            | -33.94% |     0.13 |       70 | 51.92%     | ok               |
|          45 | -3.93%   | -28.97%            | -37.29% |     0.11 |       60 | 33.14%     | ok               |
|          25 | -11.65%  | -28.97%            | -34.22% |     0.04 |       74 | 54.60%     | ok               |
|          40 | -10.41%  | -28.97%            | -40.31% |     0.01 |       58 | 38.51%     | ok               |

## MCD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 3.26%    | -7.15%             | -9.22%  |     0.2  |       44 | 22.13%     | ok               |
|          45 | -4.55%   | -7.15%             | -16.79% |    -0.18 |       52 | 25.79%     | ok               |
|          30 | -6.28%   | -7.15%             | -21.88% |    -0.21 |       77 | 37.10%     | ok               |
|          40 | -5.82%   | -7.15%             | -18.49% |    -0.23 |       67 | 29.12%     | ok               |
|          25 | -7.28%   | -7.15%             | -23.62% |    -0.24 |       77 | 39.77%     | ok               |

## META Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -21.11%  | 34.71%             | -37.54% |    -0.35 |       70 | 36.77%     | ok               |
|          40 | -26.22%  | 34.71%             | -40.90% |    -0.45 |       72 | 40.27%     | ok               |
|          50 | -29.90%  | 34.71%             | -39.33% |    -0.6  |       72 | 32.61%     | ok               |
|          25 | -36.04%  | 34.71%             | -45.70% |    -0.63 |       77 | 50.75%     | ok               |
|          30 | -36.06%  | 34.71%             | -44.90% |    -0.65 |       80 | 47.75%     | ok               |

## MPC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 37.31%   | 101.61%            | -18.24% |     0.71 |       48 | 38.77%     | ok               |
|          45 | 28.60%   | 101.61%            | -19.46% |     0.58 |       54 | 42.43%     | ok               |
|          40 | 23.75%   | 101.61%            | -20.11% |     0.5  |       56 | 44.59%     | ok               |
|          35 | 19.92%   | 101.61%            | -31.08% |     0.44 |       64 | 47.09%     | ok               |
|          30 | 5.64%    | 101.61%            | -37.91% |     0.22 |       67 | 49.58%     | ok               |

## MRK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -12.15%  | 14.43%             | -28.89% |    -0.14 |       85 | 53.74%     | ok               |
|          25 | -11.69%  | 14.43%             | -31.07% |    -0.15 |       72 | 46.42%     | ok               |
|          20 | -16.02%  | 14.43%             | -29.34% |    -0.24 |       77 | 49.75%     | ok               |
|          50 | -15.53%  | 14.43%             | -24.92% |    -0.32 |       58 | 30.45%     | ok               |
|          45 | -17.63%  | 14.43%             | -25.38% |    -0.36 |       59 | 33.78%     | ok               |

## MS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 2.48%    | 136.47%            | -19.99% |     0.14 |       70 | 39.60%     | ok               |
|          15 | -0.14%   | 136.47%            | -22.02% |     0.09 |       71 | 56.57%     | ok               |
|          20 | -0.26%   | 136.47%            | -25.68% |     0.08 |       75 | 52.75%     | ok               |
|          30 | -5.44%   | 136.47%            | -27.79% |    -0.05 |       75 | 47.92%     | ok               |
|          35 | -5.36%   | 136.47%            | -25.26% |    -0.05 |       76 | 44.43%     | ok               |

## MSFT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -13.84%  | 24.18%             | -25.23% |    -0.31 |       68 | 36.27%     | ok               |
|          50 | -20.54%  | 24.18%             | -26.37% |    -0.55 |       62 | 30.78%     | ok               |
|          35 | -26.86%  | 24.18%             | -36.02% |    -0.63 |       71 | 45.42%     | ok               |
|          40 | -26.90%  | 24.18%             | -35.43% |    -0.66 |       69 | 40.10%     | ok               |
|          30 | -28.90%  | 24.18%             | -37.80% |    -0.66 |       79 | 49.58%     | ok               |

## MU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 249.50%  | 813.42%            | -61.96% |     1.23 |       49 | 62.06%     | ok               |
|          40 | 198.28%  | 813.42%            | -64.36% |     1.2  |       54 | 49.42%     | ok               |
|          25 | 175.56%  | 813.42%            | -67.90% |     1.1  |       49 | 55.57%     | ok               |
|          30 | 164.65%  | 813.42%            | -68.76% |     1.08 |       49 | 53.91%     | ok               |
|          35 | 158.86%  | 813.42%            | -69.15% |     1.07 |       61 | 51.75%     | ok               |

## NEAR-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 60.92%   | 14.56%             | -53.32% |     0.73 |       40 | 30.08%     | ok               |
|          45 | 59.75%   | 14.56%             | -44.39% |     0.73 |       40 | 26.05%     | ok               |
|          50 | 37.23%   | 14.56%             | -49.90% |     0.57 |       32 | 21.07%     | ok               |
|          35 | 25.47%   | 14.56%             | -59.02% |     0.47 |       58 | 34.29%     | ok               |
|          30 | 5.36%    | 14.56%             | -60.10% |     0.3  |       73 | 42.34%     | ok               |

## NEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 19.95%   | 224.99%            | -31.25% |     0.39 |       58 | 60.73%     | ok               |
|          20 | 10.33%   | 224.99%            | -30.50% |     0.29 |       66 | 56.74%     | ok               |
|          25 | -7.33%   | 224.99%            | -39.51% |     0.07 |       64 | 54.91%     | ok               |
|          30 | -18.95%  | 224.99%            | -39.56% |    -0.11 |       68 | 53.24%     | ok               |
|          50 | -17.35%  | 224.99%            | -33.24% |    -0.14 |       56 | 40.60%     | ok               |

## NFLX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 41.22%   | 39.45%             | -13.37% |     0.91 |       48 | 42.43%     | ok               |
|          50 | 37.08%   | 39.45%             | -16.28% |     0.89 |       44 | 34.78%     | ok               |
|          35 | 41.25%   | 39.45%             | -18.30% |     0.86 |       70 | 46.92%     | ok               |
|          45 | 25.95%   | 39.45%             | -15.48% |     0.65 |       54 | 38.94%     | ok               |
|          15 | 22.14%   | 39.45%             | -26.59% |     0.48 |       71 | 65.22%     | ok               |

## NKE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -17.71%  | -61.07%            | -42.13% |    -0.18 |       69 | 37.77%     | ok               |
|          20 | -22.21%  | -61.07%            | -49.34% |    -0.2  |       83 | 50.08%     | ok               |
|          25 | -25.43%  | -61.07%            | -51.20% |    -0.26 |       83 | 47.42%     | ok               |
|          15 | -27.23%  | -61.07%            | -54.28% |    -0.29 |       86 | 53.91%     | ok               |
|          40 | -19.36%  | -61.07%            | -31.79% |    -0.32 |       63 | 29.78%     | ok               |

## NOW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 4.13%    | -7.18%             | -30.43% |     0.22 |       84 | 49.75%     | ok               |
|          20 | 2.74%    | -7.18%             | -39.71% |     0.21 |       81 | 56.24%     | ok               |
|          25 | -0.80%   | -7.18%             | -37.51% |     0.17 |       78 | 53.24%     | ok               |
|          15 | -4.77%   | -7.18%             | -43.06% |     0.13 |       89 | 59.23%     | ok               |
|          40 | -3.27%   | -7.18%             | -36.21% |     0.11 |       76 | 39.10%     | ok               |

## NVDA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -40.79%  | 66.66%             | -45.53% |    -0.51 |       76 | 54.55%     | ok               |
|          30 | -36.07%  | 66.66%             | -41.21% |    -0.52 |       78 | 46.35%     | ok               |
|          25 | -40.70%  | 66.66%             | -45.44% |    -0.56 |       77 | 49.55%     | ok               |
|          15 | -47.20%  | 66.66%             | -52.37% |    -0.61 |       77 | 57.75%     | ok               |
|          35 | -46.46%  | 66.66%             | -49.15% |    -0.8  |       88 | 43.32%     | ok               |

## OP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 23.57%   | -85.53%            | -31.68% |     0.49 |       32 | 9.58%      | ok               |
|          45 | -11.70%  | -85.53%            | -51.17% |     0.01 |       36 | 14.18%     | ok               |
|          40 | -21.95%  | -85.53%            | -60.08% |    -0.1  |       48 | 22.41%     | ok               |
|          30 | -42.45%  | -85.53%            | -68.74% |    -0.35 |       70 | 33.52%     | ok               |
|          35 | -40.91%  | -85.53%            | -63.95% |    -0.39 |       56 | 27.39%     | ok               |

## ORCL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 167.02%  | 30.81%             | -32.54% |     1.11 |       75 | 64.73%     | ok               |
|          45 | 102.05%  | 30.81%             | -32.35% |     0.93 |       60 | 41.10%     | ok               |
|          25 | 114.69%  | 30.81%             | -27.76% |     0.93 |       67 | 57.24%     | ok               |
|          20 | 108.71%  | 30.81%             | -29.32% |     0.9  |       76 | 60.40%     | ok               |
|          35 | 98.56%   | 30.81%             | -31.95% |     0.88 |       70 | 50.58%     | ok               |

## OXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -2.97%   | -7.76%             | -26.64% |     0.06 |       74 | 39.10%     | ok               |
|          30 | -5.18%   | -7.76%             | -31.22% |     0.03 |       75 | 44.26%     | ok               |
|          40 | -6.89%   | -7.76%             | -28.30% |    -0.02 |       62 | 35.27%     | ok               |
|          50 | -8.31%   | -7.76%             | -29.52% |    -0.07 |       52 | 28.29%     | ok               |
|          45 | -16.46%  | -7.76%             | -32.63% |    -0.25 |       54 | 30.62%     | ok               |

## PEP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 14.52%   | -21.71%            | -11.62% |     0.65 |       40 | 25.62%     | ok               |
|          45 | 7.21%    | -21.71%            | -14.22% |     0.34 |       56 | 29.62%     | ok               |
|          35 | 3.45%    | -21.71%            | -21.42% |     0.17 |       77 | 39.93%     | ok               |
|          40 | 1.23%    | -21.71%            | -18.04% |     0.1  |       70 | 35.27%     | ok               |
|          30 | -1.12%   | -21.71%            | -21.35% |     0.04 |       74 | 45.92%     | ok               |

## PEPE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -38.42%  | -50.36%            | -61.96% |    -0.02 |       80 | 63.03%     | ok               |
|          30 | -39.87%  | -50.36%            | -57.66% |    -0.17 |       89 | 47.70%     | ok               |
|          20 | -44.48%  | -50.36%            | -61.13% |    -0.17 |       86 | 59.58%     | ok               |
|          25 | -41.37%  | -50.36%            | -53.88% |    -0.17 |       93 | 53.64%     | ok               |
|          35 | -38.97%  | -50.36%            | -54.42% |    -0.22 |       72 | 41.76%     | ok               |

## PFE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -18.04%  | 6.62%              | -23.40% |    -0.58 |       56 | 22.63%     | ok               |
|          50 | -18.53%  | 6.62%              | -26.43% |    -0.66 |       44 | 18.97%     | ok               |
|          40 | -24.47%  | 6.62%              | -30.53% |    -0.76 |       76 | 27.79%     | ok               |
|          35 | -27.87%  | 6.62%              | -35.77% |    -0.82 |       88 | 35.27%     | ok               |
|          30 | -36.58%  | 6.62%              | -43.50% |    -1.08 |       83 | 39.93%     | ok               |

## PG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -9.01%   | -8.14%             | -20.08% |    -0.34 |       56 | 30.95%     | ok               |
|          35 | -12.11%  | -8.14%             | -18.99% |    -0.45 |       64 | 34.44%     | ok               |
|          30 | -20.10%  | -8.14%             | -24.55% |    -0.77 |       66 | 37.60%     | ok               |
|          45 | -17.90%  | -8.14%             | -22.43% |    -0.79 |       56 | 28.45%     | ok               |
|          25 | -21.92%  | -8.14%             | -26.24% |    -0.85 |       78 | 39.10%     | ok               |

## PM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 1.81%    | 103.75%            | -32.20% |     0.13 |       84 | 50.42%     | ok               |
|          20 | -0.85%   | 103.75%            | -33.51% |     0.08 |       83 | 59.07%     | ok               |
|          30 | -1.38%   | 103.75%            | -35.15% |     0.07 |       79 | 53.91%     | ok               |
|          50 | -5.47%   | 103.75%            | -35.70% |    -0.06 |       68 | 40.60%     | ok               |
|          40 | -5.96%   | 103.75%            | -37.94% |    -0.06 |       78 | 46.42%     | ok               |

## POL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 20.92%   | -47.13%            | -45.67% |     0.43 |       83 | 49.43%     | ok               |
|          25 | 12.51%   | -47.13%            | -46.72% |     0.35 |       70 | 56.13%     | ok               |
|          20 | -3.99%   | -47.13%            | -52.88% |     0.2  |       78 | 60.34%     | ok               |
|          50 | -2.90%   | -47.13%            | -26.14% |     0.1  |       46 | 19.54%     | ok               |
|          15 | -21.00%  | -47.13%            | -58.42% |     0.02 |       81 | 64.94%     | ok               |

## QCOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -0.42%   | 15.44%             | -54.50% |     0.17 |       71 | 44.59%     | ok               |
|          20 | -9.18%   | 15.44%             | -54.38% |     0.06 |       69 | 47.75%     | ok               |
|          35 | -7.91%   | 15.44%             | -50.58% |     0.06 |       77 | 40.27%     | ok               |
|          30 | -17.79%  | 15.44%             | -56.59% |    -0.08 |       75 | 42.60%     | ok               |
|          15 | -23.17%  | 15.44%             | -57.94% |    -0.13 |       73 | 50.92%     | ok               |

## QQQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 27.72%   | 72.41%             | -14.17% |     0.67 |       65 | 54.58%     | ok               |
|          25 | 19.05%   | 72.41%             | -12.88% |     0.53 |       63 | 48.59%     | ok               |
|          20 | 17.83%   | 72.41%             | -12.98% |     0.49 |       71 | 51.25%     | ok               |
|          30 | 13.22%   | 72.41%             | -14.20% |     0.41 |       66 | 46.42%     | ok               |
|          35 | 1.58%    | 72.41%             | -20.59% |     0.12 |       72 | 42.60%     | ok               |

## RENDER-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 19.61%   | -62.51%            | -44.59% |     0.44 |       86 | 61.11%     | ok               |
|          20 | 18.72%   | -62.51%            | -43.43% |     0.43 |       91 | 57.47%     | ok               |
|          25 | 5.27%    | -62.51%            | -40.60% |     0.33 |       91 | 52.49%     | ok               |
|          35 | -33.57%  | -62.51%            | -45.32% |    -0.17 |       82 | 37.74%     | ok               |
|          30 | -38.05%  | -62.51%            | -46.98% |    -0.18 |      100 | 45.59%     | ok               |

## RTX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 40.88%   | 94.64%             | -18.66% |     0.86 |       74 | 57.24%     | ok               |
|          25 | 36.07%   | 94.64%             | -18.59% |     0.79 |       62 | 54.58%     | ok               |
|          30 | 31.76%   | 94.64%             | -16.99% |     0.72 |       56 | 52.91%     | ok               |
|          15 | 33.20%   | 94.64%             | -19.55% |     0.72 |       69 | 62.06%     | ok               |
|          35 | 27.17%   | 94.64%             | -18.00% |     0.7  |       52 | 50.42%     | ok               |

## SBUX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -7.75%   | 12.70%             | -23.55% |    -0.07 |       57 | 39.77%     | ok               |
|          45 | -10.72%  | 12.70%             | -27.26% |    -0.2  |       62 | 28.79%     | ok               |
|          40 | -12.45%  | 12.70%             | -25.43% |    -0.22 |       58 | 32.28%     | ok               |
|          30 | -17.36%  | 12.70%             | -29.22% |    -0.31 |       60 | 37.60%     | ok               |
|          50 | -15.38%  | 12.70%             | -25.30% |    -0.35 |       52 | 24.79%     | ok               |

## SCHW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 0.96%    | 46.08%             | -16.53% |     0.1  |       62 | 33.94%     | ok               |
|          25 | -1.23%   | 46.08%             | -28.76% |     0.06 |       65 | 50.25%     | ok               |
|          20 | -4.78%   | 46.08%             | -29.24% |    -0.02 |       73 | 52.75%     | ok               |
|          50 | -4.80%   | 46.08%             | -13.28% |    -0.1  |       58 | 30.95%     | ok               |
|          40 | -8.55%   | 46.08%             | -23.35% |    -0.16 |       68 | 37.44%     | ok               |

## SHIB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -24.36%  | -57.18%            | -38.26% |    -0.09 |       77 | 60.54%     | ok               |
|          20 | -30.47%  | -57.18%            | -41.07% |    -0.17 |       79 | 63.98%     | ok               |
|          15 | -32.15%  | -57.18%            | -45.04% |    -0.19 |       84 | 68.20%     | ok               |
|          35 | -29.50%  | -57.18%            | -47.19% |    -0.23 |       74 | 46.17%     | ok               |
|          30 | -37.87%  | -57.18%            | -41.47% |    -0.35 |       84 | 53.07%     | ok               |

## SHY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          30 | -2.36%   | 0.25%              | -3.30% |    -0.82 |       50 | 34.61%     | ok               |
|          45 | -2.36%   | 0.25%              | -3.37% |    -0.88 |       50 | 26.62%     | ok               |
|          40 | -2.67%   | 0.25%              | -3.52% |    -0.95 |       54 | 31.45%     | ok               |
|          35 | -2.70%   | 0.25%              | -3.61% |    -0.95 |       52 | 32.61%     | ok               |
|          50 | -2.53%   | 0.25%              | -3.34% |    -1    |       46 | 23.13%     | ok               |

## SKY-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -35.34%  | 8.33%              | -47.99% |    -0.4  |       82 | 45.53%     | ok               |
|          15 | -42.18%  | 8.33%              | -56.39% |    -0.45 |       68 | 54.86%     | ok               |
|          25 | -42.44%  | 8.33%              | -53.70% |    -0.53 |       75 | 49.03%     | ok               |
|          35 | -40.91%  | 8.33%              | -49.68% |    -0.6  |       76 | 37.94%     | ok               |
|          20 | -50.48%  | 8.33%              | -61.78% |    -0.67 |       70 | 52.33%     | ok               |

## SLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 20.02%   | 12.46%             | -20.46% |     0.48 |       54 | 33.94%     | ok               |
|          40 | 18.33%   | 12.46%             | -23.07% |     0.44 |       46 | 37.60%     | ok               |
|          50 | 0.02%    | 12.46%             | -28.89% |     0.09 |       50 | 29.78%     | ok               |
|          35 | -11.63%  | 12.46%             | -41.81% |    -0.12 |       72 | 44.59%     | ok               |
|          30 | -29.62%  | 12.46%             | -54.95% |    -0.5  |       77 | 50.92%     | ok               |

## SLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 37.17%   | 121.83%            | -34.10% |     0.59 |       56 | 31.28%     | ok               |
|          45 | 26.44%   | 121.83%            | -31.82% |     0.48 |       65 | 32.95%     | ok               |
|          40 | 24.93%   | 121.83%            | -34.26% |     0.46 |       71 | 35.11%     | ok               |
|          15 | 15.11%   | 121.83%            | -47.98% |     0.36 |       75 | 51.58%     | ok               |
|          20 | 14.32%   | 121.83%            | -42.66% |     0.35 |       74 | 46.26%     | ok               |

## SMH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 88.78%   | 185.39%            | -31.01% |     1.15 |       49 | 47.75%     | ok               |
|          35 | 71.96%   | 185.39%            | -34.03% |     1.04 |       54 | 43.09%     | ok               |
|          25 | 70.87%   | 185.39%            | -32.94% |     1.01 |       46 | 46.42%     | ok               |
|          30 | 69.07%   | 185.39%            | -33.66% |     1    |       48 | 44.76%     | ok               |
|          45 | 55.28%   | 185.39%            | -33.35% |     0.93 |       54 | 37.44%     | ok               |

## SNX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -6.04%   | -66.53%            | -37.62% |     0.14 |       56 | 26.82%     | ok               |
|          20 | -13.37%  | -66.53%            | -47.56% |     0.11 |       71 | 43.87%     | ok               |
|          40 | -9.85%   | -66.53%            | -36.94% |     0.04 |       46 | 22.03%     | ok               |
|          30 | -18.44%  | -66.53%            | -47.16% |    -0    |       62 | 33.52%     | ok               |
|          15 | -39.55%  | -66.53%            | -49.47% |    -0.22 |       81 | 48.85%     | ok               |

## SOL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 46.94%   | -16.73%            | -38.17% |     0.67 |       52 | 37.74%     | ok               |
|          35 | 22.44%   | -16.73%            | -43.70% |     0.44 |       64 | 44.25%     | ok               |
|          45 | 15.51%   | -16.73%            | -46.83% |     0.37 |       54 | 32.38%     | ok               |
|          25 | -0.15%   | -16.73%            | -41.09% |     0.22 |       68 | 57.09%     | ok               |
|          30 | -4.70%   | -16.73%            | -45.53% |     0.16 |       78 | 51.92%     | ok               |

## SOXX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 74.69%   | 165.67%            | -39.65% |     0.99 |       56 | 45.76%     | ok               |
|          35 | 70.38%   | 165.67%            | -38.76% |     0.97 |       58 | 40.93%     | ok               |
|          30 | 68.55%   | 165.67%            | -40.14% |     0.94 |       58 | 43.43%     | ok               |
|          20 | 61.49%   | 165.67%            | -38.67% |     0.86 |       61 | 46.59%     | ok               |
|          40 | 48.85%   | 165.67%            | -41.03% |     0.78 |       58 | 38.77%     | ok               |

## SPY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 13.55%   | 54.35%             | -14.25% |     0.49 |       61 | 55.57%     | ok               |
|          15 | 11.90%   | 54.35%             | -16.80% |     0.43 |       67 | 58.40%     | ok               |
|          25 | 8.06%    | 54.35%             | -14.25% |     0.33 |       61 | 54.41%     | ok               |
|          30 | 3.49%    | 54.35%             | -15.53% |     0.18 |       64 | 51.58%     | ok               |
|          35 | 2.49%    | 54.35%             | -15.58% |     0.15 |       62 | 48.42%     | ok               |

## SUSHI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -14.68%  | -60.48%            | -34.75% |    -0.07 |       54 | 14.56%     | ok               |
|          45 | -64.10%  | -60.48%            | -64.10% |    -0.99 |       58 | 18.97%     | ok               |
|          40 | -68.58%  | -60.48%            | -66.85% |    -1.05 |       65 | 25.48%     | ok               |
|          15 | -82.29%  | -60.48%            | -82.71% |    -1.18 |       92 | 48.85%     | ok               |
|          20 | -81.60%  | -60.48%            | -82.04% |    -1.22 |       95 | 46.17%     | ok               |

## T Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 68.07%   | 57.84%             | -15.08% |     1.18 |       73 | 66.89%     | ok               |
|          20 | 63.93%   | 57.84%             | -18.13% |     1.17 |       68 | 62.40%     | ok               |
|          25 | 59.49%   | 57.84%             | -17.66% |     1.12 |       68 | 60.07%     | ok               |
|          30 | 42.02%   | 57.84%             | -17.01% |     0.89 |       72 | 58.07%     | ok               |
|          35 | 26.54%   | 57.84%             | -14.49% |     0.65 |       78 | 53.74%     | ok               |

## TGT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -11.96%  | -7.41%             | -35.83% |    -0.19 |       58 | 37.60%     | ok               |
|          25 | -13.01%  | -7.41%             | -39.14% |    -0.19 |       64 | 40.27%     | ok               |
|          20 | -15.49%  | -7.41%             | -40.95% |    -0.22 |       84 | 45.09%     | ok               |
|          45 | -13.22%  | -7.41%             | -26.91% |    -0.26 |       50 | 28.79%     | ok               |
|          15 | -21.93%  | -7.41%             | -40.65% |    -0.35 |       76 | 49.42%     | ok               |

## TIA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -33.01%  | -85.80%            | -60.24% |    -0.15 |       68 | 35.63%     | ok               |
|          15 | -47.96%  | -85.80%            | -63.05% |    -0.18 |       92 | 58.43%     | ok               |
|          45 | -35.35%  | -85.80%            | -59.25% |    -0.36 |       60 | 20.11%     | ok               |
|          40 | -44.84%  | -85.80%            | -62.94% |    -0.38 |       74 | 29.89%     | ok               |
|          20 | -58.88%  | -85.80%            | -64.15% |    -0.41 |       88 | 53.07%     | ok               |

## TLT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -19.41%  | -9.29%             | -22.36% |    -1.42 |       74 | 34.78%     | ok               |
|          50 | -13.43%  | -9.29%             | -14.46% |    -1.55 |       36 | 15.81%     | ok               |
|          40 | -17.68%  | -9.29%             | -18.31% |    -1.58 |       56 | 24.29%     | ok               |
|          15 | -25.10%  | -9.29%             | -28.21% |    -1.68 |       81 | 42.93%     | ok               |
|          35 | -20.86%  | -9.29%             | -22.12% |    -1.74 |       68 | 28.79%     | ok               |

## TMO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 48.61%   | 11.94%             | -8.17%  |     1.06 |       44 | 33.61%     | ok               |
|          45 | 42.82%   | 11.94%             | -9.69%  |     0.92 |       48 | 38.44%     | ok               |
|          40 | 38.64%   | 11.94%             | -9.91%  |     0.83 |       53 | 43.26%     | ok               |
|          35 | 33.32%   | 11.94%             | -13.84% |     0.7  |       65 | 48.59%     | ok               |
|          30 | 24.66%   | 11.94%             | -18.85% |     0.54 |       65 | 54.08%     | ok               |

## TMUS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 2.41%    | 12.32%             | -27.06% |     0.15 |       76 | 48.25%     | ok               |
|          15 | -1.02%   | 12.32%             | -34.48% |     0.08 |       68 | 60.90%     | ok               |
|          25 | -5.27%   | 12.32%             | -32.65% |    -0.01 |       79 | 51.08%     | ok               |
|          20 | -6.73%   | 12.32%             | -33.09% |    -0.04 |       74 | 55.24%     | ok               |
|          50 | -6.53%   | 12.32%             | -29.49% |    -0.11 |       60 | 34.94%     | ok               |

## TRX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 19.40%   | 39.28%             | -18.79% |     0.62 |       54 | 40.42%     | ok               |
|          35 | 12.97%   | 39.28%             | -21.77% |     0.43 |       68 | 49.23%     | ok               |
|          45 | 11.46%   | 39.28%             | -18.27% |     0.42 |       46 | 36.78%     | ok               |
|          20 | 12.33%   | 39.28%             | -25.45% |     0.39 |       61 | 59.39%     | ok               |
|          30 | 10.93%   | 39.28%             | -22.90% |     0.38 |       68 | 52.30%     | ok               |

## TSLA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 41.91%   | 148.51%            | -30.57% |     0.61 |       62 | 29.78%     | ok               |
|          40 | 14.07%   | 148.51%            | -50.11% |     0.34 |       61 | 35.27%     | ok               |
|          45 | -10.25%  | 148.51%            | -52.01% |     0.07 |       67 | 32.28%     | ok               |
|          35 | -17.74%  | 148.51%            | -58.86% |     0    |       72 | 37.94%     | ok               |
|          30 | -33.82%  | 148.51%            | -58.36% |    -0.2  |       78 | 42.93%     | ok               |

## TXN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 15.00%   | 68.27%             | -45.45% |     0.36 |       60 | 32.28%     | ok               |
|          35 | -4.29%   | 68.27%             | -43.38% |     0.07 |       68 | 46.26%     | ok               |
|          40 | -6.31%   | 68.27%             | -45.67% |     0.03 |       66 | 44.26%     | ok               |
|          20 | -11.77%  | 68.27%             | -38.98% |    -0.01 |       64 | 55.91%     | ok               |
|          45 | -9.87%   | 68.27%             | -46.24% |    -0.04 |       74 | 38.44%     | ok               |

## UNH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 32.56%   | -24.35%            | -26.31% |     0.55 |       74 | 50.25%     | ok               |
|          50 | 25.76%   | -24.35%            | -36.71% |     0.49 |       54 | 29.45%     | ok               |
|          35 | 25.77%   | -24.35%            | -27.21% |     0.48 |       68 | 44.93%     | ok               |
|          15 | 22.92%   | -24.35%            | -28.45% |     0.43 |       77 | 66.06%     | ok               |
|          25 | 20.62%   | -24.35%            | -25.25% |     0.41 |       72 | 55.24%     | ok               |

## UNI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 22.11%   | 22.10%             | -45.09% |     0.44 |       52 | 24.52%     | ok               |
|          45 | -0.44%   | 22.10%             | -51.70% |     0.23 |       60 | 31.99%     | ok               |
|          40 | -12.63%  | 22.10%             | -61.16% |     0.1  |       64 | 36.40%     | ok               |
|          35 | -25.18%  | 22.10%             | -65.47% |    -0.02 |       76 | 42.34%     | ok               |
|          20 | -65.70%  | 22.10%             | -81.19% |    -0.55 |       97 | 58.24%     | ok               |

## UPS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -29.07%  | -29.76%            | -31.52% |    -0.55 |       62 | 34.28%     | ok               |
|          40 | -29.19%  | -29.76%            | -31.37% |    -0.57 |       58 | 28.95%     | ok               |
|          20 | -34.44%  | -29.76%            | -38.08% |    -0.64 |       84 | 47.59%     | ok               |
|          25 | -34.97%  | -29.76%            | -38.37% |    -0.68 |       76 | 44.26%     | ok               |
|          15 | -36.76%  | -29.76%            | -40.07% |    -0.69 |       86 | 51.41%     | ok               |

## USO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 19.54%   | 96.45%             | -43.31% |     0.4  |       75 | 38.10%     | ok               |
|          45 | 17.99%   | 96.45%             | -32.35% |     0.39 |       46 | 25.12%     | ok               |
|          25 | 14.83%   | 96.45%             | -42.99% |     0.35 |       69 | 35.27%     | ok               |
|          15 | 13.90%   | 96.45%             | -42.96% |     0.33 |       74 | 41.26%     | ok               |
|          30 | 9.87%    | 96.45%             | -41.71% |     0.28 |       70 | 32.11%     | ok               |

## VEA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 2.85%    | 51.88%             | -16.79% |     0.16 |       60 | 49.75%     | ok               |
|          20 | -1.95%   | 51.88%             | -18.44% |    -0.02 |       61 | 46.92%     | ok               |
|          25 | -5.68%   | 51.88%             | -19.11% |    -0.18 |       59 | 44.93%     | ok               |
|          30 | -6.13%   | 51.88%             | -19.49% |    -0.21 |       60 | 42.43%     | ok               |
|          35 | -7.37%   | 51.88%             | -18.54% |    -0.27 |       56 | 41.26%     | ok               |

## VIXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -44.43%  | -71.84%            | -69.78% |    -0.36 |       40 | 10.98%     | ok               |
|          45 | -56.34%  | -71.84%            | -75.03% |    -0.56 |       60 | 15.97%     | ok               |
|          40 | -65.28%  | -71.84%            | -80.72% |    -0.69 |       72 | 19.97%     | ok               |
|          35 | -69.25%  | -71.84%            | -84.02% |    -0.74 |       94 | 26.46%     | ok               |
|          15 | -77.49%  | -71.84%            | -89.47% |    -0.8  |       99 | 45.59%     | ok               |

## VNQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -9.92%   | 20.00%             | -19.07% |    -0.44 |       60 | 28.79%     | ok               |
|          50 | -10.35%  | 20.00%             | -17.13% |    -0.48 |       56 | 26.29%     | ok               |
|          25 | -13.64%  | 20.00%             | -22.34% |    -0.53 |       71 | 41.60%     | ok               |
|          40 | -14.96%  | 20.00%             | -24.84% |    -0.66 |       74 | 32.78%     | ok               |
|          20 | -17.86%  | 20.00%             | -24.00% |    -0.7  |       76 | 44.76%     | ok               |

## VTI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 14.24%   | 53.45%             | -13.96% |     0.51 |       64 | 56.07%     | ok               |
|          15 | 8.40%    | 53.45%             | -15.70% |     0.33 |       63 | 58.57%     | ok               |
|          25 | 1.65%    | 53.45%             | -15.00% |     0.12 |       60 | 53.74%     | ok               |
|          30 | -5.97%   | 53.45%             | -17.64% |    -0.16 |       70 | 51.75%     | ok               |
|          40 | -7.10%   | 53.45%             | -19.77% |    -0.22 |       74 | 44.26%     | ok               |

## VWO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -7.37%   | 47.59%             | -21.18% |    -0.26 |       56 | 29.95%     | ok               |
|          45 | -9.18%   | 47.59%             | -23.26% |    -0.33 |       58 | 32.45%     | ok               |
|          15 | -11.71%  | 47.59%             | -24.01% |    -0.36 |       74 | 47.92%     | ok               |
|          40 | -10.21%  | 47.59%             | -23.57% |    -0.37 |       68 | 35.11%     | ok               |
|          20 | -13.11%  | 47.59%             | -26.14% |    -0.43 |       71 | 45.59%     | ok               |

## VZ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 2.58%    | 24.99%             | -12.55% |     0.15 |       54 | 27.45%     | ok               |
|          45 | -9.20%   | 24.99%             | -21.44% |    -0.24 |       66 | 31.28%     | ok               |
|          25 | -11.62%  | 24.99%             | -22.13% |    -0.27 |       79 | 45.09%     | ok               |
|          35 | -10.49%  | 24.99%             | -22.73% |    -0.27 |       61 | 37.10%     | ok               |
|          40 | -15.50%  | 24.99%             | -24.21% |    -0.46 |       66 | 34.44%     | ok               |

## WFC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -7.48%   | 49.61%             | -21.57% |    -0.09 |       77 | 43.76%     | ok               |
|          50 | -6.82%   | 49.61%             | -18.29% |    -0.15 |       60 | 32.11%     | ok               |
|          20 | -18.09%  | 49.61%             | -29.87% |    -0.26 |       77 | 52.41%     | ok               |
|          30 | -17.12%  | 49.61%             | -28.90% |    -0.28 |       80 | 46.92%     | ok               |
|          40 | -13.20%  | 49.61%             | -23.94% |    -0.31 |       72 | 40.43%     | ok               |

## WIF-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 44.34%   | -51.40%            | -40.67% |     0.59 |       65 | 43.68%     | ok               |
|          15 | 12.80%   | -51.40%            | -46.21% |     0.41 |       75 | 46.93%     | ok               |
|          25 | -14.61%  | -51.40%            | -44.74% |     0.17 |       69 | 39.46%     | ok               |
|          50 | -15.28%  | -51.40%            | -34.40% |    -0.09 |       34 | 11.49%     | ok               |
|          30 | -38.16%  | -51.40%            | -52.76% |    -0.14 |       66 | 35.63%     | ok               |

## WMT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 38.72%   | 79.99%             | -11.62% |     1.11 |       40 | 39.10%     | ok               |
|          50 | 33.90%   | 79.99%             | -12.19% |     1.05 |       32 | 36.77%     | ok               |
|          35 | 29.02%   | 79.99%             | -16.55% |     0.83 |       56 | 45.26%     | ok               |
|          40 | 27.36%   | 79.99%             | -15.99% |     0.82 |       48 | 40.60%     | ok               |
|          15 | 13.18%   | 79.99%             | -25.74% |     0.38 |       74 | 58.40%     | ok               |

## XBI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 10.67%   | 88.58%             | -15.46% |     0.34 |       52 | 34.28%     | ok               |
|          40 | 10.62%   | 88.58%             | -16.08% |     0.33 |       58 | 37.27%     | ok               |
|          50 | 2.21%    | 88.58%             | -15.97% |     0.14 |       54 | 30.78%     | ok               |
|          35 | -0.00%   | 88.58%             | -17.66% |     0.09 |       64 | 40.93%     | ok               |
|          30 | -2.09%   | 88.58%             | -18.40% |     0.04 |       66 | 42.43%     | ok               |

## XLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -4.10%   | 14.55%             | -19.74% |    -0.11 |       54 | 26.46%     | ok               |
|          50 | -4.33%   | 14.55%             | -17.40% |    -0.13 |       36 | 22.46%     | ok               |
|          35 | -7.36%   | 14.55%             | -22.80% |    -0.23 |       54 | 29.95%     | ok               |
|          45 | -6.88%   | 14.55%             | -19.76% |    -0.24 |       38 | 23.63%     | ok               |
|          25 | -10.56%  | 14.55%             | -23.37% |    -0.35 |       62 | 35.61%     | ok               |

## XLC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 14.20%   | 41.69%             | -12.33% |     0.52 |       63 | 50.58%     | ok               |
|          25 | 13.65%   | 41.69%             | -12.31% |     0.5  |       62 | 52.75%     | ok               |
|          50 | 7.28%    | 41.69%             | -11.12% |     0.38 |       66 | 38.60%     | ok               |
|          40 | 7.86%    | 41.69%             | -13.38% |     0.34 |       64 | 44.09%     | ok               |
|          35 | 7.13%    | 41.69%             | -13.38% |     0.31 |       62 | 47.92%     | ok               |

## XLE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.90%   | 37.18%             | -25.98% |     0.05 |       56 | 35.27%     | ok               |
|          35 | -6.39%   | 37.18%             | -28.82% |    -0.08 |       69 | 41.76%     | ok               |
|          45 | -6.10%   | 37.18%             | -29.68% |    -0.1  |       64 | 37.44%     | ok               |
|          25 | -11.24%  | 37.18%             | -34.66% |    -0.2  |       85 | 47.42%     | ok               |
|          15 | -13.67%  | 37.18%             | -38.01% |    -0.25 |       97 | 53.08%     | ok               |

## XLF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -3.58%   | 41.78%             | -18.63% |    -0.06 |       70 | 51.58%     | ok               |
|          15 | -6.29%   | 41.78%             | -20.19% |    -0.15 |       76 | 53.74%     | ok               |
|          25 | -9.62%   | 41.78%             | -23.22% |    -0.29 |       79 | 48.25%     | ok               |
|          30 | -9.66%   | 41.78%             | -23.61% |    -0.3  |       80 | 45.92%     | ok               |
|          35 | -16.69%  | 41.78%             | -24.48% |    -0.65 |       70 | 42.26%     | ok               |

## XLI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 5.77%    | 43.08%             | -11.06% |     0.25 |       86 | 49.25%     | ok               |
|          20 | 2.40%    | 43.08%             | -12.74% |     0.14 |       73 | 43.76%     | ok               |
|          25 | -3.96%   | 43.08%             | -14.41% |    -0.1  |       70 | 41.93%     | ok               |
|          45 | -3.93%   | 43.08%             | -16.29% |    -0.13 |       66 | 33.28%     | ok               |
|          30 | -4.54%   | 43.08%             | -14.12% |    -0.13 |       72 | 40.93%     | ok               |

## XLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 81.20%   | 94.95%             | -14.75% |     1.33 |       46 | 50.92%     | ok               |
|          25 | 77.51%   | 94.95%             | -14.75% |     1.33 |       40 | 48.75%     | ok               |
|          15 | 85.33%   | 94.95%             | -14.75% |     1.32 |       46 | 52.91%     | ok               |
|          30 | 66.88%   | 94.95%             | -14.75% |     1.23 |       40 | 47.42%     | ok               |
|          35 | 46.23%   | 94.95%             | -13.61% |     0.96 |       54 | 44.59%     | ok               |

## XLM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -8.81%   | -22.04%            | -51.28% |     0.07 |       56 | 31.42%     | ok               |
|          25 | -14.52%  | -22.04%            | -49.14% |     0.05 |       71 | 50.00%     | ok               |
|          50 | -9.34%   | -22.04%            | -48.81% |     0.05 |       46 | 26.05%     | ok               |
|          30 | -18.02%  | -22.04%            | -54.58% |     0    |       67 | 46.93%     | ok               |
|          40 | -22.07%  | -22.04%            | -47.28% |    -0.08 |       53 | 36.78%     | ok               |

## XLP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 11.62%   | 12.01%             | -5.66%  |     0.73 |       50 | 30.78%     | ok               |
|          40 | 9.37%    | 12.01%             | -7.77%  |     0.57 |       66 | 34.94%     | ok               |
|          50 | 8.19%    | 12.01%             | -6.08%  |     0.54 |       54 | 28.95%     | ok               |
|          35 | 8.42%    | 12.01%             | -9.73%  |     0.51 |       62 | 37.94%     | ok               |
|          30 | 7.54%    | 12.01%             | -10.28% |     0.46 |       64 | 39.60%     | ok               |

## XLU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 4.79%    | 29.57%             | -13.94% |     0.27 |       52 | 30.28%     | ok               |
|          45 | 3.64%    | 29.57%             | -14.88% |     0.22 |       56 | 31.45%     | ok               |
|          40 | 0.51%    | 29.57%             | -16.41% |     0.07 |       62 | 33.28%     | ok               |
|          35 | -2.16%   | 29.57%             | -19.71% |    -0.05 |       62 | 35.94%     | ok               |
|          30 | -3.52%   | 29.57%             | -20.40% |    -0.11 |       67 | 39.27%     | ok               |

## XLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -15.42%  | 19.01%             | -19.16% |    -0.7  |       68 | 37.44%     | ok               |
|          25 | -16.57%  | 19.01%             | -21.14% |    -0.75 |       70 | 39.43%     | ok               |
|          20 | -19.84%  | 19.01%             | -24.51% |    -0.91 |       73 | 41.10%     | ok               |
|          15 | -20.71%  | 19.01%             | -24.84% |    -0.93 |       81 | 43.93%     | ok               |
|          35 | -19.84%  | 19.01%             | -23.17% |    -0.98 |       66 | 34.94%     | ok               |

## XLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -2.35%   | 33.08%             | -15.77% |     0.01 |       80 | 52.58%     | ok               |
|          30 | -6.85%   | 33.08%             | -17.23% |    -0.15 |       79 | 46.09%     | ok               |
|          20 | -7.51%   | 33.08%             | -19.25% |    -0.15 |       76 | 49.25%     | ok               |
|          25 | -9.58%   | 33.08%             | -19.25% |    -0.22 |       73 | 47.75%     | ok               |
|          50 | -7.29%   | 33.08%             | -14.40% |    -0.26 |       60 | 30.95%     | ok               |

## XOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 0.31%    | 38.46%             | -21.35% |     0.08 |       40 | 27.29%     | ok               |
|          25 | -0.20%   | 38.46%             | -19.90% |     0.07 |       59 | 35.94%     | ok               |
|          30 | -1.19%   | 38.46%             | -20.29% |     0.05 |       59 | 35.27%     | ok               |
|          45 | -6.16%   | 38.46%             | -23.33% |    -0.11 |       46 | 28.79%     | ok               |
|          20 | -7.25%   | 38.46%             | -25.56% |    -0.12 |       68 | 38.10%     | ok               |

## XRP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 34.43%   | -32.08%            | -31.38% |     0.56 |       70 | 43.10%     | ok               |
|          40 | 21.26%   | -32.08%            | -33.91% |     0.43 |       58 | 36.40%     | ok               |
|          30 | 13.20%   | -32.08%            | -31.82% |     0.35 |       65 | 47.89%     | ok               |
|          45 | 8.85%    | -32.08%            | -36.27% |     0.3  |       56 | 31.99%     | ok               |
|          20 | -1.41%   | -32.08%            | -38.12% |     0.2  |       77 | 56.32%     | ok               |

## YFI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -48.46%  | -52.29%            | -47.65% |    -0.83 |       58 | 26.82%     | ok               |
|          45 | -48.67%  | -52.29%            | -47.74% |    -1.08 |       70 | 21.26%     | ok               |
|          35 | -63.42%  | -52.29%            | -64.69% |    -1.14 |       69 | 34.48%     | ok               |
|          30 | -68.18%  | -52.29%            | -72.54% |    -1.23 |       81 | 38.89%     | ok               |
|          15 | -72.52%  | -52.29%            | -76.87% |    -1.26 |       85 | 51.53%     | ok               |

## ZEC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 151.50%  | 2825.56%           | -30.64% |     0.96 |       46 | 29.50%     | ok               |
|          35 | 129.43%  | 2825.56%           | -50.84% |     0.88 |       52 | 36.40%     | ok               |
|          25 | 118.63%  | 2825.56%           | -58.07% |     0.84 |       56 | 43.49%     | ok               |
|          30 | 104.02%  | 2825.56%           | -56.50% |     0.8  |       64 | 40.61%     | ok               |
|          20 | 83.18%   | 2825.56%           | -62.70% |     0.72 |       63 | 45.59%     | ok               |
