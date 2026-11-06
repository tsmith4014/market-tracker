# Market Tracker Backtest Report

_Generated: 2026-11-06T06:37:36+00:00_

## Data Sources

- Crypto: Kraken -> Coinbase -> CoinGecko OHLC -> CoinPaprika fallback chain.
- Stocks / ETFs / indices: Stooq -> Yahoo Finance fallback chain.
- Data rows are generated from real market APIs. Mock OHLCV rows are not generated.

## Data Freshness

- Rows: **92,778**
- Symbols: **161**
- Date range: **2024-06-14** to **2026-11-06**

## Latest Signals

| symbol     | date                |         close |   composite_score | signal   | data_source   |
|:-----------|:--------------------|--------------:|------------------:|:---------|:--------------|
| AAPL       | 2026-11-05 00:00:00 |   344.17      |         43        | LONG     | Yahoo Finance |
| ABBV       | 2026-11-05 00:00:00 |   288.24      |         52.0833   | LONG     | Yahoo Finance |
| AGG        | 2026-11-05 00:00:00 |    96.62      |         40.9167   | LONG     | Yahoo Finance |
| AMGN       | 2026-11-05 00:00:00 |   460.28      |         74.4167   | LONG     | Yahoo Finance |
| BLK        | 2026-11-05 00:00:00 |  1170.67      |         69.4167   | LONG     | Yahoo Finance |
| BND        | 2026-11-05 00:00:00 |    71.65      |         35.9167   | LONG     | Yahoo Finance |
| CL         | 2026-11-05 00:00:00 |    98.69      |         58.4167   | LONG     | Yahoo Finance |
| COST       | 2026-11-05 00:00:00 |  1065.59      |         66.0833   | LONG     | Yahoo Finance |
| DE         | 2026-11-05 00:00:00 |   663.31      |         55.9167   | LONG     | Yahoo Finance |
| DIS        | 2026-11-05 00:00:00 |   117.22      |         73.5833   | LONG     | Yahoo Finance |
| HD         | 2026-11-05 00:00:00 |   349.94      |         59.9167   | LONG     | Yahoo Finance |
| IEF        | 2026-11-05 00:00:00 |    91.97      |         37.5833   | LONG     | Yahoo Finance |
| INTU       | 2026-11-05 00:00:00 |   354.84      |         51.1667   | LONG     | Yahoo Finance |
| JNJ        | 2026-11-05 00:00:00 |   272.32      |         52.4167   | LONG     | Yahoo Finance |
| KO         | 2026-11-05 00:00:00 |    95.73      |         72.9167   | LONG     | Yahoo Finance |
| LIN        | 2026-11-05 00:00:00 |   521.23      |         61.9167   | LONG     | Yahoo Finance |
| LLY        | 2026-11-05 00:00:00 |  1364.73      |         70.9167   | LONG     | Yahoo Finance |
| MCD        | 2026-11-05 00:00:00 |   278.04      |         63.8333   | LONG     | Yahoo Finance |
| MRK        | 2026-11-05 00:00:00 |   146.94      |         69.9167   | LONG     | Yahoo Finance |
| NKE        | 2026-11-05 00:00:00 |    39.56      |         32.25     | LONG     | Yahoo Finance |
| PEP        | 2026-11-05 00:00:00 |   142.71      |         67.1667   | LONG     | Yahoo Finance |
| PEPE-USD   | 2026-11-06 00:00:00 |     4.91e-06  |         63.0833   | LONG     | Kraken API    |
| PFE        | 2026-11-05 00:00:00 |    29.88      |         49.8333   | LONG     | Yahoo Finance |
| PG         | 2026-11-05 00:00:00 |   167.1       |         70.9167   | LONG     | Yahoo Finance |
| SBUX       | 2026-11-05 00:00:00 |   106.16      |         60.9167   | LONG     | Yahoo Finance |
| SHY        | 2026-11-05 00:00:00 |    81.67      |         41.6667   | LONG     | Yahoo Finance |
| TLT        | 2026-11-05 00:00:00 |    81.93      |         33.4167   | LONG     | Yahoo Finance |
| UPS        | 2026-11-05 00:00:00 |   111.04      |         57.5833   | LONG     | Yahoo Finance |
| VIXY       | 2026-11-05 00:00:00 |    21.22      |         38.0833   | LONG     | Yahoo Finance |
| VNQ        | 2026-11-05 00:00:00 |    96.23      |         62.9167   | LONG     | Yahoo Finance |
| WMT        | 2026-11-05 00:00:00 |   127.72      |         59.9167   | LONG     | Yahoo Finance |
| XLB        | 2026-11-05 00:00:00 |    52.33      |         61.4167   | LONG     | Yahoo Finance |
| XLF        | 2026-11-05 00:00:00 |    57.5       |         74.9167   | LONG     | Yahoo Finance |
| XLP        | 2026-11-05 00:00:00 |    91.25      |         61.9167   | LONG     | Yahoo Finance |
| XLU        | 2026-11-05 00:00:00 |    43.3       |         38.6667   | LONG     | Yahoo Finance |
| XLV        | 2026-11-05 00:00:00 |   184.91      |         79.9167   | LONG     | Yahoo Finance |
| XLY        | 2026-11-05 00:00:00 |   117.64      |         59.4167   | LONG     | Yahoo Finance |
| AAVE-USD   | 2026-11-06 00:00:00 |   129.85      |        -10.5833   | NEUTRAL  | Kraken API    |
| ADBE       | 2026-11-05 00:00:00 |   246.44      |        -19.6667   | NEUTRAL  | Yahoo Finance |
| AMD        | 2026-11-05 00:00:00 |   404.4       |        -45.75     | NEUTRAL  | Yahoo Finance |
| AMZN       | 2026-11-05 00:00:00 |   260.21      |         45.6667   | NEUTRAL  | Yahoo Finance |
| ARB-USD    | 2026-11-06 00:00:00 |     0.1676    |        -10.0833   | NEUTRAL  | Kraken API    |
| BAC        | 2026-11-05 00:00:00 |    49.76      |         -9.91667  | NEUTRAL  | Yahoo Finance |
| BCH-USD    | 2026-11-06 00:00:00 |   274.6       |        -55.5      | NEUTRAL  | Kraken API    |
| BONK-USD   | 2026-11-06 00:00:00 |     2.859e-06 |        -49.25     | NEUTRAL  | Kraken API    |
| C          | 2026-11-05 00:00:00 |   118.45      |        -48.4167   | NEUTRAL  | Yahoo Finance |
| CMCSA      | 2026-11-05 00:00:00 |    24.95      |         14.5      | NEUTRAL  | Yahoo Finance |
| COP        | 2026-11-05 00:00:00 |   135.46      |         -1.58333  | NEUTRAL  | Yahoo Finance |
| CRM        | 2026-11-05 00:00:00 |   222.41      |        -17.75     | NEUTRAL  | Yahoo Finance |
| CVX        | 2026-11-05 00:00:00 |   212.93      |        -20.0833   | NEUTRAL  | Yahoo Finance |
| DASH-USD   | 2026-11-06 00:00:00 |    44.764     |        -63.25     | NEUTRAL  | Kraken API    |
| DBC        | 2026-11-05 00:00:00 |    31.47      |        -18.5833   | NEUTRAL  | Yahoo Finance |
| DIA        | 2026-11-05 00:00:00 |   514.27      |          0.166667 | NEUTRAL  | Yahoo Finance |
| DOT-USD    | 2026-11-06 00:00:00 |     0.9181    |        -55.9167   | NEUTRAL  | Kraken API    |
| DXY-INDEX  | 2026-11-06 00:00:00 |   101.787     |         40.0538   | NEUTRAL  | Yahoo Finance |
| EFA        | 2026-11-05 00:00:00 |   102.7       |        -13.6667   | NEUTRAL  | Yahoo Finance |
| EOG        | 2026-11-05 00:00:00 |   144.89      |          0.416667 | NEUTRAL  | Yahoo Finance |
| ETH-USD    | 2026-11-06 00:00:00 |  2217.51      |        -14.25     | NEUTRAL  | Kraken API    |
| FXI        | 2026-11-05 00:00:00 |    34.94      |         20.9167   | NEUTRAL  | Yahoo Finance |
| GDX        | 2026-11-05 00:00:00 |    85.75      |         12.1667   | NEUTRAL  | Yahoo Finance |
| GDXJ       | 2026-11-05 00:00:00 |   104.79      |        -15.25     | NEUTRAL  | Yahoo Finance |
| GE         | 2026-11-05 00:00:00 |   314.73      |          8.41667  | NEUTRAL  | Yahoo Finance |
| GLD        | 2026-11-05 00:00:00 |   375.49      |        -30.8333   | NEUTRAL  | Yahoo Finance |
| GS         | 2026-11-05 00:00:00 |   868.95      |        -48.4167   | NEUTRAL  | Yahoo Finance |
| HON        | 2026-11-05 00:00:00 |   215.78      |        -18.5      | NEUTRAL  | Yahoo Finance |
| HYG        | 2026-11-05 00:00:00 |    77.28      |        -22.8333   | NEUTRAL  | Yahoo Finance |
| IBM        | 2026-11-05 00:00:00 |   247.11      |         28.9167   | NEUTRAL  | Yahoo Finance |
| INJ-USD    | 2026-11-06 00:00:00 |     8.161     |         42.75     | NEUTRAL  | Kraken API    |
| INTC       | 2026-11-05 00:00:00 |    52.25      |        -66.3333   | NEUTRAL  | Yahoo Finance |
| ITA        | 2026-11-05 00:00:00 |    68.11      |        -42.6667   | NEUTRAL  | Yahoo Finance |
| IWM        | 2026-11-05 00:00:00 |   270.98      |        -28.5      | NEUTRAL  | Yahoo Finance |
| JPM        | 2026-11-05 00:00:00 |   337.34      |         11        | NEUTRAL  | Yahoo Finance |
| MPC        | 2026-11-05 00:00:00 |   377.32      |        -20.8333   | NEUTRAL  | Yahoo Finance |
| MS         | 2026-11-05 00:00:00 |   182.44      |        -34.25     | NEUTRAL  | Yahoo Finance |
| MSFT       | 2026-11-05 00:00:00 |   535.93      |         29        | NEUTRAL  | Yahoo Finance |
| NEAR-USD   | 2026-11-06 00:00:00 |     3.6923    |        -23.25     | NEUTRAL  | Kraken API    |
| NEM        | 2026-11-05 00:00:00 |   119.71      |         38.3333   | NEUTRAL  | Yahoo Finance |
| ORCL       | 2026-11-05 00:00:00 |   115.16      |        -56.3333   | NEUTRAL  | Yahoo Finance |
| PM         | 2026-11-05 00:00:00 |   201.5       |         16.25     | NEUTRAL  | Yahoo Finance |
| POL-USD    | 2026-11-06 00:00:00 |     0.09283   |         -5.08333  | NEUTRAL  | Kraken API    |
| QCOM       | 2026-11-05 00:00:00 |   156.75      |        -56.4167   | NEUTRAL  | Yahoo Finance |
| RTX        | 2026-11-05 00:00:00 |   191.88      |          9.75     | NEUTRAL  | Yahoo Finance |
| SCHW       | 2026-11-05 00:00:00 |    92.58      |          4.41667  | NEUTRAL  | Yahoo Finance |
| SLB        | 2026-11-05 00:00:00 |    49.64      |        -37.3333   | NEUTRAL  | Yahoo Finance |
| TGT        | 2026-11-05 00:00:00 |   157.95      |         58.6667   | NEUTRAL  | Yahoo Finance |
| TMO        | 2026-11-05 00:00:00 |   676.94      |         -4.33333  | NEUTRAL  | Yahoo Finance |
| TMUS       | 2026-11-05 00:00:00 |   160.59      |         -8.5      | NEUTRAL  | Yahoo Finance |
| TSLA       | 2026-11-05 00:00:00 |   343.69      |        -49.3333   | NEUTRAL  | Yahoo Finance |
| TXN        | 2026-11-05 00:00:00 |   278.15      |         -4.91667  | NEUTRAL  | Yahoo Finance |
| UNH        | 2026-11-05 00:00:00 |   395.72      |          5.41667  | NEUTRAL  | Yahoo Finance |
| UNI-USD    | 2026-11-06 00:00:00 |     6.9033    |          7.75     | NEUTRAL  | Kraken API    |
| USO        | 2026-11-05 00:00:00 |   148.21      |         -8.58333  | NEUTRAL  | Yahoo Finance |
| VEA        | 2026-11-05 00:00:00 |    68.19      |        -40.6667   | NEUTRAL  | Yahoo Finance |
| VZ         | 2026-11-05 00:00:00 |    46.12      |         41.9167   | NEUTRAL  | Yahoo Finance |
| WFC        | 2026-11-05 00:00:00 |    84.8       |         53.6667   | NEUTRAL  | Yahoo Finance |
| XBI        | 2026-11-05 00:00:00 |   148.4       |         16.25     | NEUTRAL  | Yahoo Finance |
| XLI        | 2026-11-05 00:00:00 |   162.47      |        -38.75     | NEUTRAL  | Yahoo Finance |
| XOM        | 2026-11-05 00:00:00 |   165.3       |        -16.3333   | NEUTRAL  | Yahoo Finance |
| XRP-USD    | 2026-11-06 00:00:00 |     1.19099   |        -57.25     | NEUTRAL  | Kraken API    |
| YFI-USD    | 2026-11-06 00:00:00 |  1984         |        -26        | NEUTRAL  | Kraken API    |
| ZEC-USD    | 2026-11-06 00:00:00 |  1263         |         51.4167   | NEUTRAL  | Kraken API    |
| ADA-USD    | 2026-11-06 00:00:00 |     0.18366   |        -46.6667   | SHORT    | Kraken API    |
| ALGO-USD   | 2026-11-06 00:00:00 |     0.09304   |        -46.6667   | SHORT    | Kraken API    |
| AMAT       | 2026-11-05 00:00:00 |   319.25      |        -64        | SHORT    | Yahoo Finance |
| APT-USD    | 2026-11-06 00:00:00 |     0.5989    |        -48.1667   | SHORT    | Kraken API    |
| ARKK       | 2026-11-05 00:00:00 |    73.15      |        -41.5      | SHORT    | Yahoo Finance |
| ATOM-USD   | 2026-11-06 00:00:00 |     1.4029    |        -48.3333   | SHORT    | Kraken API    |
| AVAX-USD   | 2026-11-06 00:00:00 |     8.273     |        -37.5833   | SHORT    | Kraken API    |
| AVGO       | 2026-11-05 00:00:00 |   291.53      |        -58.3333   | SHORT    | Yahoo Finance |
| BA         | 2026-11-05 00:00:00 |   172.5       |        -58.25     | SHORT    | Yahoo Finance |
| BITO       | 2026-11-05 00:00:00 |    10.13      |        -39.3333   | SHORT    | Yahoo Finance |
| BTC-USD    | 2026-11-06 00:00:00 | 75444.9       |        -40.5833   | SHORT    | Kraken API    |
| CAT        | 2026-11-05 00:00:00 |   553.64      |        -65.6667   | SHORT    | Yahoo Finance |
| COMP-USD   | 2026-11-06 00:00:00 |    19.84      |        -49.6667   | SHORT    | Kraken API    |
| CRV-USD    | 2026-11-06 00:00:00 |     0.25566   |        -53.3333   | SHORT    | Kraken API    |
| CSCO       | 2026-11-05 00:00:00 |    95.72      |        -44.8333   | SHORT    | Yahoo Finance |
| DOGE-USD   | 2026-11-06 00:00:00 |     0.0713968 |        -32        | SHORT    | Kraken API    |
| EEM        | 2026-11-05 00:00:00 |    58.05      |        -58.3333   | SHORT    | Yahoo Finance |
| ETC-USD    | 2026-11-06 00:00:00 |     6.982     |        -41        | SHORT    | Kraken API    |
| EWJ        | 2026-11-05 00:00:00 |    88.26      |        -55.9167   | SHORT    | Yahoo Finance |
| FCX        | 2026-11-05 00:00:00 |    57.9       |        -63.3333   | SHORT    | Yahoo Finance |
| FET-USD    | 2026-11-06 00:00:00 |     0.1467    |        -48.3333   | SHORT    | Kraken API    |
| FIL-USD    | 2026-11-06 00:00:00 |     0.803     |        -51.6667   | SHORT    | Kraken API    |
| GOOGL      | 2026-11-05 00:00:00 |   282.57      |        -61.9167   | SHORT    | Yahoo Finance |
| GRT-USD    | 2026-11-06 00:00:00 |     0.01916   |        -51.6667   | SHORT    | Kraken API    |
| HBAR-USD   | 2026-11-06 00:00:00 |     0.06824   |        -35.8333   | SHORT    | Kraken API    |
| IBIT       | 2026-11-05 00:00:00 |    43.03      |        -41.0833   | SHORT    | Yahoo Finance |
| ICP-USD    | 2026-11-06 00:00:00 |     2.41      |        -37.6667   | SHORT    | Kraken API    |
| IEMG       | 2026-11-05 00:00:00 |    70.71      |        -61.6667   | SHORT    | Yahoo Finance |
| LDO-USD    | 2026-11-06 00:00:00 |     0.329     |        -46.3333   | SHORT    | Kraken API    |
| LINK-USD   | 2026-11-06 00:00:00 |    10.7039    |        -39.25     | SHORT    | Kraken API    |
| LRCX       | 2026-11-05 00:00:00 |   185.2       |        -68        | SHORT    | Yahoo Finance |
| LTC-USD    | 2026-11-06 00:00:00 |    52.14      |        -43        | SHORT    | Kraken API    |
| META       | 2026-11-05 00:00:00 |   605.08      |        -48.4167   | SHORT    | Yahoo Finance |
| MU         | 2026-11-05 00:00:00 |   656.39      |        -49.5      | SHORT    | Yahoo Finance |
| NFLX       | 2026-11-05 00:00:00 |    65.56      |        -42.75     | SHORT    | Yahoo Finance |
| NOW        | 2026-11-05 00:00:00 |   102.36      |        -52.0833   | SHORT    | Yahoo Finance |
| NVDA       | 2026-11-05 00:00:00 |   181.6       |        -48.1667   | SHORT    | Yahoo Finance |
| OP-USD     | 2026-11-06 00:00:00 |     0.1039    |        -50.6667   | SHORT    | Kraken API    |
| OXY        | 2026-11-05 00:00:00 |    56.36      |        -34.8333   | SHORT    | Yahoo Finance |
| QQQ        | 2026-11-05 00:00:00 |   647.05      |        -41.0833   | SHORT    | Yahoo Finance |
| RENDER-USD | 2026-11-06 00:00:00 |     1.52      |        -46.6667   | SHORT    | Kraken API    |
| SHIB-USD   | 2026-11-06 00:00:00 |     4.558e-06 |        -41        | SHORT    | Kraken API    |
| SKY-USD    | 2026-11-06 00:00:00 |     0.06472   |        -46.3333   | SHORT    | Kraken API    |
| SLV        | 2026-11-05 00:00:00 |    46.93      |        -56.0833   | SHORT    | Yahoo Finance |
| SMH        | 2026-11-05 00:00:00 |   447.73      |        -59        | SHORT    | Yahoo Finance |
| SNX-USD    | 2026-11-06 00:00:00 |     0.1649    |        -49.9167   | SHORT    | Kraken API    |
| SOL-USD    | 2026-11-06 00:00:00 |    89.33      |        -43.9167   | SHORT    | Kraken API    |
| SOXX       | 2026-11-05 00:00:00 |   131.9       |        -59        | SHORT    | Yahoo Finance |
| SPY        | 2026-11-05 00:00:00 |   733         |        -44.5      | SHORT    | Yahoo Finance |
| SUSHI-USD  | 2026-11-06 00:00:00 |     0.1819    |        -48.3333   | SHORT    | Kraken API    |
| T          | 2026-11-05 00:00:00 |    21.82      |        -34.9167   | SHORT    | Yahoo Finance |
| TIA-USD    | 2026-11-06 00:00:00 |     0.4179    |        -55.6667   | SHORT    | Kraken API    |
| TRX-USD    | 2026-11-06 00:00:00 |     0.318052  |        -48.3333   | SHORT    | Kraken API    |
| VTI        | 2026-11-05 00:00:00 |   360.52      |        -44.5      | SHORT    | Yahoo Finance |
| VWO        | 2026-11-05 00:00:00 |    54.24      |        -59.6667   | SHORT    | Yahoo Finance |
| WIF-USD    | 2026-11-06 00:00:00 |     0.1644    |        -47        | SHORT    | Kraken API    |
| XLC        | 2026-11-05 00:00:00 |   104.34      |        -55.8333   | SHORT    | Yahoo Finance |
| XLE        | 2026-11-05 00:00:00 |    61.63      |        -30.4167   | SHORT    | Yahoo Finance |
| XLK        | 2026-11-05 00:00:00 |   162.38      |        -37.75     | SHORT    | Yahoo Finance |
| XLM-USD    | 2026-11-06 00:00:00 |     0.153466  |        -34        | SHORT    | Kraken API    |

## Edge Summary

- Symbols with trades: **161** of 161
- Beat buy-and-hold: **36.02%** of traded symbols
- Positive return: **32.30%** of traded symbols
- Median strategy return: **-8.59%** (benchmark **18.58%**)
- Median excess vs benchmark: **-24.85%**
- Median Sharpe: **-0.09**
- Median exposure: **44.26%**

> Edge is real only if both _beat buy-and-hold_ and _median excess_ are convincingly positive across many symbols. Treat a single high-return symbol as noise.

## Portfolio Backtest

Actual capital-allocation books (not per-symbol averages). Benchmarks: `equal_weight_buyhold` (whole tracked universe), `spy_buyhold` (100% SPY), and `sixty_forty` (60% SPY / 40% AGG). `high_conf_voltarget` inverse-vol-weights the HIGH-confidence book; `conviction_long_short` is market-neutral. Judge on **Sharpe** and **max_drawdown** out-of-sample, not raw return: a fully-invested long book wins on return in a bull market but carries all the risk.

| strategy              | scope         | ann_return   | ann_vol   |   sharpe | max_drawdown   | total_return   |   avg_gross_exposure |
|:----------------------|:--------------|:-------------|:----------|---------:|:---------------|:---------------|---------------------:|
| equal_weight_buyhold  | full          | 7.73%        | 28.49%    |     0.27 | -39.53%        | 11.81%         |                 1    |
| equal_weight_buyhold  | out_of_sample | 17.11%       | 26.51%    |     0.65 | -15.77%        | 15.57%         |                 1    |
| all_signals_ew        | full          | -12.92%      | 24.23%    |    -0.53 | -54.82%        | -38.27%        |                 1    |
| all_signals_ew        | out_of_sample | -3.50%       | 21.56%    |    -0.16 | -23.35%        | -6.00%         |                 1    |
| high_conf_ew          | full          | -6.49%       | 29.90%    |    -0.22 | -46.65%        | -28.27%        |                 0.89 |
| high_conf_ew          | out_of_sample | -2.74%       | 27.09%    |    -0.1  | -22.80%        | -6.65%         |                 0.89 |
| high_conf_voltarget   | full          | -6.76%       | 26.58%    |    -0.25 | -40.81%        | -26.78%        |                 0.89 |
| high_conf_voltarget   | out_of_sample | -5.41%       | 22.77%    |    -0.24 | -17.69%        | -8.24%         |                 0.89 |
| conviction_long_short | full          | -14.66%      | 22.08%    |    -0.66 | -48.77%        | -40.56%        |                 0.96 |
| conviction_long_short | out_of_sample | -18.34%      | 17.46%    |    -1.05 | -27.55%        | -19.05%        |                 0.96 |
| spy_buyhold           | full          | 3.02%        | 13.95%    |     0.22 | -19.00%        | 6.44%          |                 0.79 |
| spy_buyhold           | out_of_sample | -2.74%       | 10.84%    |    -0.25 | -11.45%        | -3.48%         |                 0.79 |
| sixty_forty           | full          | 1.42%        | 8.74%     |     0.16 | -11.66%        | 3.22%          |                 0.79 |
| sixty_forty           | out_of_sample | -3.39%       | 7.16%     |    -0.47 | -8.19%         | -3.80%         |                 0.79 |

## Walk-Forward Robustness

Each book measured across contiguous time folds (each a different regime). A book has durable edge only if `mean_sharpe` is positive, `min_sharpe` isn't deeply negative, and `pct_positive_folds` is high — a single great fold doesn't count. `fold_sharpes` lists each fold oldest-to-newest.

| strategy              |   n_folds |   mean_sharpe |   median_sharpe |   min_sharpe | pct_positive_folds   | mean_return   | fold_sharpes                 |
|:----------------------|----------:|--------------:|----------------:|-------------:|:---------------------|:--------------|:-----------------------------|
| equal_weight_buyhold  |         5 |          0.52 |            0.75 |        -0.86 | 60.00%               | 3.42%         | 1.68;1.34;-0.32;-0.86;0.75   |
| all_signals_ew        |         5 |         -0.57 |           -0.5  |        -1.81 | 20.00%               | -7.92%        | -1.19;-0.48;-1.81;1.11;-0.50 |
| high_conf_ew          |         5 |         -0.13 |           -0.46 |        -1.7  | 40.00%               | -4.67%        | 0.56;-1.70;-0.46;1.55;-0.58  |
| high_conf_voltarget   |         5 |         -0.19 |           -0.31 |        -1.75 | 40.00%               | -5.18%        | 0.80;-1.75;-0.31;0.94;-0.62  |
| conviction_long_short |         5 |         -0.67 |           -0.6  |        -1.97 | 40.00%               | -9.25%        | -1.97;0.35;-1.24;0.11;-0.60  |
| spy_buyhold           |         5 |          0.22 |            0.13 |        -0.98 | 60.00%               | 1.47%         | 1.62;-0.08;0.13;0.39;-0.98   |
| sixty_forty           |         5 |          0.14 |            0.09 |        -1    | 60.00%               | 0.71%         | 1.50;-0.04;0.16;0.09;-1.00   |

## Strategy Comparison

Each decision rule backtested over the same data. `out_of_sample` is the most recent ~35% of each symbol's history (unseen tail). A rule has real edge only if `median_excess` and `beat_benchmark_pct` stay positive out-of-sample, not just full-sample.

| strategy        | scope         |   symbols | beat_benchmark_pct   | positive_pct   | median_return   | median_benchmark   | median_excess   |   median_sharpe |   total_trades |
|:----------------|:--------------|----------:|:---------------------|:---------------|:----------------|:-------------------|:----------------|----------------:|---------------:|
| trend           | full          |       161 | 36.02%               | 32.30%         | -8.59%          | 18.58%             | -24.85%         |           -0.09 |          11312 |
| trend           | out_of_sample |       161 | 45.96%               | 50.31%         | 0.10%           | -0.19%             | -2.66%          |            0.14 |           3875 |
| mean_reversion  | full          |       159 | 38.36%               | 49.06%         | -0.02%          | 18.58%             | -19.53%         |            0.02 |           1278 |
| mean_reversion  | out_of_sample |       132 | 53.79%               | 57.58%         | 0.33%           | -2.12%             | 1.59%           |            0.39 |            494 |
| regime_adaptive | full          |       161 | 36.65%               | 34.16%         | -8.97%          | 18.58%             | -23.76%         |           -0.05 |          11584 |
| regime_adaptive | out_of_sample |       161 | 45.34%               | 50.31%         | 0.10%           | -0.19%             | -2.97%          |            0.11 |           3983 |

## Signal Calibration

Realized forward return in the signal's direction, grouped by confidence. HIGH should outrank LOW for the confidence score to be meaningful.

| confidence_level   |   horizon |     n | mean_return   | median_return   | win_rate   |
|:-------------------|----------:|------:|:--------------|:----------------|:-----------|
| HIGH               |         5 |  7843 | 0.20%         | 0.08%           | 51.28%     |
| MEDIUM             |         5 | 29054 | 0.06%         | 0.05%           | 50.50%     |
| LOW                |         5 |  3607 | -0.24%        | -0.27%          | 47.30%     |
| ALL                |         5 | 40504 | 0.06%         | 0.04%           | 50.37%     |
| HIGH               |        10 |  7770 | 0.45%         | 0.09%           | 51.00%     |
| MEDIUM             |        10 | 28768 | 0.18%         | 0.06%           | 50.47%     |
| LOW                |        10 |  3555 | -0.54%        | -0.31%          | 47.79%     |
| ALL                |        10 | 40093 | 0.17%         | 0.04%           | 50.34%     |
| HIGH               |        20 |  7669 | 0.87%         | 0.20%           | 51.58%     |
| MEDIUM             |        20 | 28316 | 0.69%         | 0.45%           | 52.50%     |
| LOW                |        20 |  3455 | -0.46%        | -0.56%          | 47.41%     |
| ALL                |        20 | 39440 | 0.63%         | 0.32%           | 51.87%     |

## Backtest Summary

### Data Quality / Signal Availability

- **ok**: 161 symbols

| symbol     |   trades | return   | benchmark_return   | mdd     |   sharpe | exposure   | skipped_reason   |
|:-----------|---------:|:---------|:-------------------|:--------|---------:|:-----------|:-----------------|
| AAPL       |       68 | -11.15%  | 61.97%             | -23.09% |    -0.13 | 48.42%     | ok               |
| AAVE-USD   |       67 | -48.62%  | -51.28%            | -64.31% |    -0.43 | 39.08%     | ok               |
| ABBV       |       68 | -18.41%  | 70.97%             | -30.52% |    -0.35 | 50.08%     | ok               |
| ADA-USD    |       76 | -22.62%  | -73.15%            | -52.70% |    -0.06 | 48.28%     | ok               |
| ADBE       |       76 | 3.21%    | -53.09%            | -31.20% |     0.19 | 55.41%     | ok               |
| AGG        |       63 | -6.61%   | -1.33%             | -11.01% |    -1.05 | 33.11%     | ok               |
| ALGO-USD   |       82 | -28.77%  | -52.88%            | -42.04% |    -0.15 | 42.15%     | ok               |
| AMAT       |       73 | -28.16%  | 34.69%             | -57.56% |    -0.16 | 51.75%     | ok               |
| AMD        |       52 | 22.57%   | 153.34%            | -38.64% |     0.42 | 35.94%     | ok               |
| AMGN       |       63 | -4.82%   | 54.14%             | -34.19% |    -0.01 | 52.25%     | ok               |
| AMZN       |       84 | -59.52%  | 41.68%             | -59.95% |    -1.75 | 41.43%     | ok               |
| APT-USD    |       74 | -35.40%  | -87.87%            | -56.73% |    -0.18 | 38.89%     | ok               |
| ARB-USD    |       73 | 4.78%    | -53.44%            | -44.81% |     0.31 | 42.53%     | ok               |
| ARKK       |       83 | -23.52%  | 66.74%             | -30.25% |    -0.31 | 43.26%     | ok               |
| ATOM-USD   |       84 | -58.22%  | -68.25%            | -64.83% |    -0.88 | 46.74%     | ok               |
| AVAX-USD   |       66 | -28.93%  | -60.83%            | -46.93% |    -0.19 | 41.57%     | ok               |
| AVGO       |       66 | 3.47%    | 68.02%             | -40.82% |     0.21 | 40.43%     | ok               |
| BA         |       67 | 13.52%   | -2.69%             | -24.47% |     0.34 | 51.41%     | ok               |
| BAC        |       78 | -7.42%   | 26.81%             | -23.14% |    -0.12 | 49.08%     | ok               |
| BCH-USD    |       82 | -14.22%  | -31.53%            | -54.04% |     0.04 | 47.89%     | ok               |
| BITO       |       81 | -27.08%  | -58.97%            | -43.13% |    -0.22 | 40.93%     | ok               |
| BLK        |       79 | -8.59%   | 52.17%             | -26.90% |    -0.15 | 47.09%     | ok               |
| BND        |       67 | -6.65%   | -1.39%             | -10.91% |    -1.03 | 34.78%     | ok               |
| BONK-USD   |       72 | 59.03%   | -82.94%            | -53.32% |     0.67 | 45.21%     | ok               |
| BTC-USD    |       79 | -13.24%  | -28.45%            | -23.58% |    -0.12 | 50.38%     | ok               |
| C          |       81 | -35.20%  | 99.65%             | -39.84% |    -0.76 | 47.42%     | ok               |
| CAT        |       70 | 38.15%   | 72.22%             | -21.87% |     0.64 | 50.42%     | ok               |
| CL         |       60 | 7.12%    | 4.30%              | -14.32% |     0.28 | 39.77%     | ok               |
| CMCSA      |       84 | -37.44%  | -28.90%            | -46.48% |    -0.91 | 43.43%     | ok               |
| COMP-USD   |       99 | -47.13%  | -55.46%            | -61.97% |    -0.36 | 48.66%     | ok               |
| COP        |       64 | -15.96%  | 23.83%             | -39.71% |    -0.2  | 43.76%     | ok               |
| COST       |       62 | -0.23%   | 24.53%             | -31.32% |     0.06 | 41.10%     | ok               |
| CRM        |       67 | -30.72%  | -4.11%             | -41.89% |    -0.43 | 46.26%     | ok               |
| CRV-USD    |       66 | 43.42%   | -62.65%            | -39.89% |     0.59 | 36.97%     | ok               |
| CSCO       |       63 | 8.84%    | 109.54%            | -23.09% |     0.27 | 50.92%     | ok               |
| CVX        |       69 | -13.55%  | 39.56%             | -27.78% |    -0.28 | 43.09%     | ok               |
| DASH-USD   |       57 | -15.94%  | 100.58%            | -64.43% |     0.28 | 30.65%     | ok               |
| DBC        |       68 | -11.81%  | 36.41%             | -24.10% |    -0.34 | 36.11%     | ok               |
| DE         |       72 | -8.15%   | 75.48%             | -22.44% |    -0.08 | 43.59%     | ok               |
| DIA        |       70 | -9.40%   | 33.07%             | -15.89% |    -0.48 | 44.26%     | ok               |
| DIS        |       62 | -0.72%   | 17.26%             | -27.81% |     0.08 | 45.59%     | ok               |
| DOGE-USD   |       70 | -26.29%  | -63.02%            | -61.39% |    -0.11 | 47.32%     | ok               |
| DOT-USD    |       80 | -47.40%  | -77.82%            | -63.40% |    -0.36 | 45.98%     | ok               |
| DXY-INDEX  |       40 | -2.27%   | -6.69%             | -6.06%  |    -0.37 | 31.17%     | ok               |
| EEM        |       66 | -4.23%   | 37.46%             | -24.14% |    -0.06 | 40.93%     | ok               |
| EFA        |       64 | -9.07%   | 31.95%             | -12.63% |    -0.35 | 38.94%     | ok               |
| EOG        |       78 | -30.39%  | 22.54%             | -47.87% |    -0.65 | 44.93%     | ok               |
| ETC-USD    |       54 | -8.68%   | -60.26%            | -45.54% |     0.04 | 34.10%     | ok               |
| ETH-USD    |       59 | 108.52%  | -14.53%            | -30.11% |     1.11 | 46.55%     | ok               |
| EWJ        |       64 | -22.16%  | 31.48%             | -29.40% |    -0.75 | 37.27%     | ok               |
| FCX        |       69 | -23.15%  | 20.35%             | -46.84% |    -0.2  | 44.93%     | ok               |
| FET-USD    |       79 | -34.32%  | -82.16%            | -66.52% |    -0.09 | 44.44%     | ok               |
| FIL-USD    |       71 | -36.78%  | -69.42%            | -58.54% |    -0.27 | 38.12%     | ok               |
| FXI        |       46 | -3.03%   | 33.51%             | -23.91% |     0.01 | 30.12%     | ok               |
| GDX        |       66 | -3.66%   | 156.66%            | -33.40% |     0.08 | 44.93%     | ok               |
| GDXJ       |       68 | -25.59%  | 150.39%            | -35.04% |    -0.24 | 44.26%     | ok               |
| GE         |       78 | -13.14%  | 101.91%            | -27.82% |    -0.14 | 48.42%     | ok               |
| GLD        |       52 | 11.67%   | 74.06%             | -14.15% |     0.35 | 46.09%     | ok               |
| GOOGL      |       57 | 77.51%   | 59.83%             | -16.84% |     1.17 | 48.09%     | ok               |
| GRT-USD    |       75 | 45.55%   | -80.37%            | -43.87% |     0.61 | 47.32%     | ok               |
| GS         |       68 | -2.77%   | 94.63%             | -21.94% |     0.04 | 47.42%     | ok               |
| HBAR-USD   |       40 | -30.58%  | -33.83%            | -56.47% |    -0.46 | 42.66%     | ok               |
| HD         |       73 | 6.90%    | 0.89%              | -17.15% |     0.25 | 44.59%     | ok               |
| HON        |       89 | -28.67%  | 4.68%              | -33.87% |    -0.74 | 53.58%     | ok               |
| HYG        |       87 | -6.94%   | 0.29%              | -10.69% |    -0.77 | 39.60%     | ok               |
| IBIT       |       44 | 28.46%   | 13.21%             | -18.95% |     0.56 | 34.97%     | ok               |
| IBM        |       69 | -19.90%  | 46.04%             | -48.94% |    -0.19 | 50.75%     | ok               |
| ICP-USD    |       72 | 2.24%    | -54.68%            | -40.43% |     0.28 | 39.08%     | ok               |
| IEF        |       80 | -9.87%   | -2.78%             | -13.34% |    -1.33 | 33.94%     | ok               |
| IEMG       |       62 | -0.96%   | 33.19%             | -24.73% |     0.04 | 40.77%     | ok               |
| INJ-USD    |       57 | -19.46%  | -34.77%            | -64.47% |     0.06 | 39.08%     | ok               |
| INTC       |       70 | 64.96%   | 71.59%             | -60.60% |     0.66 | 48.92%     | ok               |
| INTU       |       71 | 10.88%   | -40.43%            | -37.44% |     0.29 | 47.75%     | ok               |
| ITA        |       72 | -1.32%   | 54.46%             | -23.75% |     0.04 | 47.42%     | ok               |
| IWM        |       58 | 10.62%   | 36.36%             | -8.62%  |     0.43 | 34.78%     | ok               |
| JNJ        |       60 | 10.77%   | 87.11%             | -17.51% |     0.42 | 46.42%     | ok               |
| JPM        |       75 | -25.99%  | 74.08%             | -32.74% |    -0.75 | 44.43%     | ok               |
| KO         |       52 | 28.20%   | 53.05%             | -8.64%  |     0.94 | 38.60%     | ok               |
| LDO-USD    |       70 | 47.84%   | -60.93%            | -53.44% |     0.61 | 47.89%     | ok               |
| LIN        |       70 | -3.93%   | 19.29%             | -20.61% |    -0.07 | 40.93%     | ok               |
| LINK-USD   |       66 | 31.11%   | -24.18%            | -34.17% |     0.51 | 43.30%     | ok               |
| LLY        |       80 | -33.55%  | 55.36%             | -53.61% |    -0.52 | 49.42%     | ok               |
| LRCX       |       82 | -2.24%   | 78.77%             | -58.92% |     0.17 | 45.09%     | ok               |
| LTC-USD    |       69 | 9.35%    | -41.76%            | -30.78% |     0.31 | 50.77%     | ok               |
| MCD        |       77 | 9.57%    | 9.65%              | -22.20% |     0.38 | 40.43%     | ok               |
| META       |       72 | -29.07%  | 20.02%             | -44.90% |    -0.41 | 50.08%     | ok               |
| MPC        |       70 | 10.68%   | 121.86%            | -33.74% |     0.29 | 53.24%     | ok               |
| MRK        |       65 | -23.45%  | 13.48%             | -35.95% |    -0.45 | 42.43%     | ok               |
| MS         |       77 | -7.18%   | 91.04%             | -27.79% |    -0.09 | 48.42%     | ok               |
| MSFT       |       83 | -28.52%  | 21.09%             | -39.07% |    -0.63 | 50.92%     | ok               |
| MU         |       51 | 116.71%  | 364.34%            | -68.76% |     0.91 | 49.92%     | ok               |
| NEAR-USD   |       65 | 172.41%  | 47.22%             | -46.79% |     1.12 | 43.10%     | ok               |
| NEM        |       70 | -25.86%  | 193.26%            | -39.56% |    -0.25 | 49.75%     | ok               |
| NFLX       |       82 | -9.34%   | -2.06%             | -27.17% |    -0.1  | 50.92%     | ok               |
| NKE        |       85 | -29.16%  | -57.64%            | -55.35% |    -0.33 | 47.92%     | ok               |
| NOW        |       81 | -9.05%   | -29.75%            | -42.66% |     0.11 | 51.58%     | ok               |
| NVDA       |       82 | -38.43%  | 56.36%             | -51.51% |    -0.49 | 55.79%     | ok               |
| OP-USD     |       72 | -37.21%  | -84.36%            | -58.87% |    -0.25 | 34.29%     | ok               |
| ORCL       |       58 | 72.68%   | -16.63%            | -30.61% |     0.74 | 50.42%     | ok               |
| OXY        |       65 | 2.79%    | -5.82%             | -28.48% |     0.17 | 43.09%     | ok               |
| PEP        |       74 | 1.33%    | -12.88%            | -21.35% |     0.11 | 45.09%     | ok               |
| PEPE-USD   |       72 | -42.60%  | -59.94%            | -57.70% |    -0.21 | 46.17%     | ok               |
| PFE        |       77 | -31.28%  | 8.54%              | -41.77% |    -0.93 | 37.27%     | ok               |
| PG         |       62 | -18.67%  | 0.19%              | -24.55% |    -0.65 | 35.94%     | ok               |
| PM         |       81 | -8.12%   | 97.16%             | -37.61% |    -0.09 | 48.92%     | ok               |
| POL-USD    |       83 | 12.93%   | -56.88%            | -44.63% |     0.35 | 51.15%     | ok               |
| QCOM       |       79 | -40.14%  | -27.20%            | -56.59% |    -0.44 | 40.93%     | ok               |
| QQQ        |       68 | 0.21%    | 35.03%             | -14.20% |     0.09 | 43.59%     | ok               |
| RENDER-USD |       92 | -34.55%  | -60.67%            | -50.55% |    -0.11 | 48.47%     | ok               |
| RTX        |       68 | 22.88%   | 84.09%             | -16.99% |     0.55 | 51.75%     | ok               |
| SBUX       |       64 | -9.73%   | 33.28%             | -29.22% |    -0.11 | 39.93%     | ok               |
| SCHW       |       84 | -16.47%  | 26.39%             | -31.92% |    -0.34 | 48.09%     | ok               |
| SHIB-USD   |       81 | -37.49%  | -65.07%            | -52.92% |    -0.38 | 52.68%     | ok               |
| SHY        |       54 | -1.83%   | 0.07%              | -3.18%  |    -0.6  | 38.27%     | ok               |
| SKY-USD    |       89 | -60.93%  | -16.39%            | -63.60% |    -0.99 | 44.06%     | ok               |
| SLB        |       78 | -49.01%  | 15.44%             | -59.05% |    -1.06 | 48.42%     | ok               |
| SLV        |       66 | 29.03%   | 73.75%             | -37.05% |     0.5  | 40.93%     | ok               |
| SMH        |       50 | 59.59%   | 67.13%             | -34.29% |     0.88 | 42.10%     | ok               |
| SNX-USD    |       60 | 7.33%    | -76.41%            | -50.74% |     0.3  | 36.02%     | ok               |
| SOL-USD    |       74 | -14.77%  | -42.48%            | -45.52% |     0.06 | 57.66%     | ok               |
| SOXX       |       56 | 72.93%   | 57.00%             | -39.81% |     0.96 | 40.93%     | ok               |
| SPY        |       62 | -4.86%   | 35.05%             | -15.53% |    -0.11 | 47.59%     | ok               |
| SUSHI-USD  |       91 | -61.46%  | -74.09%            | -76.86% |    -0.73 | 42.34%     | ok               |
| T          |       68 | 53.12%   | 23.70%             | -17.01% |     0.95 | 57.07%     | ok               |
| TGT        |       58 | -8.89%   | 11.89%             | -32.83% |    -0.11 | 37.27%     | ok               |
| TIA-USD    |       91 | -43.82%  | -81.37%            | -75.93% |    -0.18 | 42.53%     | ok               |
| TLT        |       66 | -19.74%  | -13.46%            | -21.85% |    -1.5  | 33.94%     | ok               |
| TMO        |       63 | 30.62%   | 18.34%             | -18.85% |     0.63 | 54.91%     | ok               |
| TMUS       |       74 | -6.41%   | -8.75%             | -33.05% |    -0.04 | 47.42%     | ok               |
| TRX-USD    |       64 | 3.83%    | 17.62%             | -22.90% |     0.19 | 47.32%     | ok               |
| TSLA       |       74 | -30.19%  | 93.07%             | -58.36% |    -0.15 | 42.76%     | ok               |
| TXN        |       81 | -31.23%  | 43.45%             | -46.56% |    -0.37 | 48.59%     | ok               |
| UNH        |       73 | 41.00%   | -20.40%            | -26.31% |     0.63 | 49.25%     | ok               |
| UNI-USD    |       84 | -27.09%  | 3.97%              | -61.00% |     0.01 | 49.43%     | ok               |
| UPS        |       76 | -35.37%  | -18.14%            | -41.51% |    -0.68 | 41.76%     | ok               |
| USO        |       65 | -13.01%  | 94.81%             | -43.52% |    -0.05 | 34.28%     | ok               |
| VEA        |       62 | -5.22%   | 37.76%             | -17.27% |    -0.17 | 41.93%     | ok               |
| VIXY       |       92 | -80.56%  | -52.46%            | -89.28% |    -1.03 | 31.11%     | ok               |
| VNQ        |       71 | -10.63%  | 14.56%             | -24.92% |    -0.39 | 39.77%     | ok               |
| VTI        |       66 | -11.47%  | 35.18%             | -17.64% |    -0.36 | 47.59%     | ok               |
| VWO        |       78 | -11.22%  | 23.95%             | -25.20% |    -0.37 | 40.93%     | ok               |
| VZ         |       87 | -29.15%  | 16.26%             | -31.67% |    -0.9  | 43.43%     | ok               |
| WFC        |       84 | -22.09%  | 47.74%             | -29.78% |    -0.4  | 46.59%     | ok               |
| WIF-USD    |       64 | -7.02%   | -83.07%            | -48.32% |     0.2  | 41.38%     | ok               |
| WMT        |       71 | 9.14%    | 90.57%             | -25.96% |     0.31 | 48.42%     | ok               |
| XBI        |       60 | 0.63%    | 61.74%             | -17.66% |     0.1  | 37.77%     | ok               |
| XLB        |       64 | -9.81%   | 17.62%             | -24.18% |    -0.31 | 33.61%     | ok               |
| XLC        |       61 | 9.28%    | 24.02%             | -12.33% |     0.36 | 49.42%     | ok               |
| XLE        |       69 | 1.25%    | 40.00%             | -28.77% |     0.12 | 47.25%     | ok               |
| XLF        |       78 | -3.35%   | 41.45%             | -23.61% |    -0.05 | 48.25%     | ok               |
| XLI        |       84 | -10.61%  | 34.11%             | -18.31% |    -0.38 | 42.93%     | ok               |
| XLK        |       42 | 41.64%   | 42.65%             | -14.75% |     0.87 | 43.76%     | ok               |
| XLM-USD    |       71 | 7.96%    | -43.77%            | -54.58% |     0.3  | 48.47%     | ok               |
| XLP        |       63 | 14.75%   | 18.58%             | -8.96%  |     0.73 | 39.77%     | ok               |
| XLU        |       69 | -1.15%   | 23.82%             | -20.40% |    -0    | 39.77%     | ok               |
| XLV        |       74 | -19.35%  | 26.75%             | -22.82% |    -0.87 | 36.44%     | ok               |
| XLY        |       77 | -3.08%   | 31.94%             | -18.44% |    -0.02 | 47.75%     | ok               |
| XOM        |       55 | 2.46%    | 51.50%             | -20.29% |     0.14 | 36.27%     | ok               |
| XRP-USD    |       74 | -4.99%   | -46.97%            | -33.91% |     0.12 | 35.44%     | ok               |
| YFI-USD    |       74 | -52.78%  | -62.80%            | -58.78% |    -0.83 | 40.23%     | ok               |
| ZEC-USD    |       56 | 97.69%   | 2222.97%           | -56.50% |     0.77 | 37.36%     | ok               |

## AAPL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -5.59%   | 61.97%             | -22.53% |    -0    |       77 | 53.24%     | ok               |
|          15 | -9.76%   | 61.97%             | -24.50% |    -0.08 |       86 | 60.73%     | ok               |
|          30 | -11.15%  | 61.97%             | -23.09% |    -0.13 |       68 | 48.42%     | ok               |
|          35 | -12.42%  | 61.97%             | -24.45% |    -0.17 |       68 | 47.09%     | ok               |
|          40 | -12.09%  | 61.97%             | -28.08% |    -0.17 |       64 | 42.93%     | ok               |

## AAVE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 4.68%    | -51.28%            | -43.61% |     0.27 |       43 | 33.52%     | ok               |
|          35 | -9.10%   | -51.28%            | -48.79% |     0.12 |       53 | 36.78%     | ok               |
|          45 | -10.37%  | -51.28%            | -49.19% |     0.07 |       48 | 28.54%     | ok               |
|          50 | -11.28%  | -51.28%            | -45.07% |     0.04 |       44 | 21.26%     | ok               |
|          15 | -45.40%  | -51.28%            | -60.75% |    -0.26 |       76 | 52.87%     | ok               |

## ABBV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -9.90%   | 70.97%             | -27.91% |    -0.17 |       54 | 37.94%     | ok               |
|          20 | -15.21%  | 70.97%             | -28.73% |    -0.26 |       64 | 53.41%     | ok               |
|          25 | -15.31%  | 70.97%             | -30.04% |    -0.27 |       67 | 51.91%     | ok               |
|          30 | -18.41%  | 70.97%             | -30.52% |    -0.35 |       68 | 50.08%     | ok               |
|          40 | -18.46%  | 70.97%             | -27.36% |    -0.39 |       70 | 43.09%     | ok               |

## ADA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 11.11%   | -73.15%            | -32.15% |     0.32 |       48 | 25.86%     | ok               |
|          15 | -2.47%   | -73.15%            | -47.27% |     0.25 |       69 | 62.84%     | ok               |
|          35 | 2.14%    | -73.15%            | -44.07% |     0.24 |       64 | 42.72%     | ok               |
|          45 | 3.23%    | -73.15%            | -37.32% |     0.23 |       52 | 31.99%     | ok               |
|          40 | -1.15%   | -73.15%            | -41.47% |     0.19 |       60 | 38.31%     | ok               |

## ADBE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 21.98%   | -53.09%            | -29.07% |     0.44 |       57 | 60.07%     | ok               |
|          20 | 5.13%    | -53.09%            | -31.52% |     0.22 |       65 | 63.39%     | ok               |
|          30 | 3.21%    | -53.09%            | -31.20% |     0.19 |       76 | 55.41%     | ok               |
|          35 | -2.78%   | -53.09%            | -32.89% |     0.08 |       79 | 46.26%     | ok               |
|          15 | -5.16%   | -53.09%            | -34.98% |     0.08 |       65 | 65.72%     | ok               |

## AGG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -5.44%   | -1.33%             | -9.59%  |    -0.99 |       52 | 23.96%     | ok               |
|          50 | -4.84%   | -1.33%             | -8.07%  |    -1.04 |       50 | 18.97%     | ok               |
|          30 | -6.61%   | -1.33%             | -11.01% |    -1.05 |       63 | 33.11%     | ok               |
|          20 | -8.20%   | -1.33%             | -11.89% |    -1.17 |       68 | 39.10%     | ok               |
|          35 | -7.21%   | -1.33%             | -11.73% |    -1.18 |       62 | 29.62%     | ok               |

## ALGO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -28.77%  | -52.88%            | -42.04% |    -0.15 |       82 | 42.15%     | ok               |
|          25 | -32.53%  | -52.88%            | -50.24% |    -0.18 |       84 | 46.55%     | ok               |
|          15 | -39.42%  | -52.88%            | -52.81% |    -0.26 |       79 | 52.49%     | ok               |
|          35 | -38.40%  | -52.88%            | -52.80% |    -0.38 |       70 | 37.16%     | ok               |
|          20 | -45.74%  | -52.88%            | -55.53% |    -0.39 |       83 | 49.23%     | ok               |

## AMAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -9.91%   | 34.69%             | -38.30% |     0.05 |       50 | 36.44%     | ok               |
|          15 | -20.89%  | 34.69%             | -53.90% |    -0.04 |       74 | 60.57%     | ok               |
|          35 | -22.82%  | 34.69%             | -52.00% |    -0.1  |       73 | 49.08%     | ok               |
|          30 | -28.16%  | 34.69%             | -57.56% |    -0.16 |       73 | 51.75%     | ok               |
|          40 | -29.11%  | 34.69%             | -54.64% |    -0.2  |       71 | 44.26%     | ok               |

## AMD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 38.95%   | 153.34%            | -37.12% |     0.55 |       50 | 31.11%     | ok               |
|          40 | 22.57%   | 153.34%            | -38.64% |     0.42 |       52 | 35.94%     | ok               |
|          35 | 17.30%   | 153.34%            | -40.22% |     0.37 |       60 | 37.60%     | ok               |
|          45 | 10.91%   | 153.34%            | -45.23% |     0.31 |       56 | 33.94%     | ok               |
|          30 | -0.34%   | 153.34%            | -47.20% |     0.22 |       63 | 40.27%     | ok               |

## AMGN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 0.21%    | 54.14%             | -26.65% |     0.11 |       62 | 57.57%     | ok               |
|          35 | -2.42%   | 54.14%             | -31.29% |     0.05 |       65 | 48.92%     | ok               |
|          30 | -4.82%   | 54.14%             | -34.19% |    -0.01 |       63 | 52.25%     | ok               |
|          15 | -7.22%   | 54.14%             | -27.98% |    -0.04 |       61 | 61.56%     | ok               |
|          25 | -6.78%   | 54.14%             | -33.47% |    -0.04 |       59 | 54.41%     | ok               |

## AMZN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -32.85%  | 41.68%             | -33.72% |    -1.02 |       60 | 30.28%     | ok               |
|          50 | -34.90%  | 41.68%             | -35.58% |    -1.27 |       52 | 22.96%     | ok               |
|          45 | -40.35%  | 41.68%             | -40.97% |    -1.45 |       60 | 26.62%     | ok               |
|          35 | -54.77%  | 41.68%             | -55.24% |    -1.63 |       79 | 35.44%     | ok               |
|          30 | -59.52%  | 41.68%             | -59.95% |    -1.75 |       84 | 41.43%     | ok               |

## APT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 47.37%   | -87.87%            | -25.96% |     0.8  |       40 | 15.71%     | ok               |
|          45 | 14.65%   | -87.87%            | -52.49% |     0.37 |       58 | 22.80%     | ok               |
|          20 | -13.48%  | -87.87%            | -56.22% |     0.15 |       84 | 49.23%     | ok               |
|          15 | -31.24%  | -87.87%            | -58.22% |    -0.02 |       79 | 55.56%     | ok               |
|          35 | -22.11%  | -87.87%            | -49.10% |    -0.04 |       72 | 34.48%     | ok               |

## ARB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 91.55%   | -53.44%            | -28.01% |     0.86 |       52 | 25.67%     | ok               |
|          40 | 52.10%   | -53.44%            | -38.69% |     0.63 |       53 | 33.14%     | ok               |
|          35 | 50.31%   | -53.44%            | -40.80% |     0.62 |       65 | 37.55%     | ok               |
|          50 | 48.08%   | -53.44%            | -30.74% |     0.62 |       46 | 18.20%     | ok               |
|          15 | 36.17%   | -53.44%            | -52.14% |     0.54 |       90 | 58.24%     | ok               |

## ARKK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -7.08%   | 66.74%             | -37.76% |     0.04 |       84 | 54.24%     | ok               |
|          20 | -16.38%  | 66.74%             | -34.82% |    -0.12 |       85 | 49.58%     | ok               |
|          30 | -23.52%  | 66.74%             | -30.25% |    -0.31 |       83 | 43.26%     | ok               |
|          35 | -31.55%  | 66.74%             | -37.22% |    -0.51 |       84 | 40.60%     | ok               |
|          25 | -34.54%  | 66.74%             | -42.86% |    -0.54 |       93 | 45.76%     | ok               |

## ATOM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -43.99%  | -68.25%            | -56.26% |    -0.41 |       82 | 64.56%     | ok               |
|          25 | -46.87%  | -68.25%            | -58.01% |    -0.53 |       86 | 52.68%     | ok               |
|          20 | -51.27%  | -68.25%            | -62.05% |    -0.6  |       90 | 56.90%     | ok               |
|          45 | -52.48%  | -68.25%            | -58.69% |    -0.83 |       74 | 32.38%     | ok               |
|          40 | -54.67%  | -68.25%            | -62.66% |    -0.85 |       72 | 37.55%     | ok               |

## AVAX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 59.53%   | -60.83%            | -22.06% |     0.89 |       34 | 19.73%     | ok               |
|          40 | 28.47%   | -60.83%            | -26.27% |     0.52 |       40 | 29.89%     | ok               |
|          45 | 18.00%   | -60.83%            | -24.48% |     0.41 |       36 | 25.48%     | ok               |
|          35 | 5.58%    | -60.83%            | -33.05% |     0.26 |       54 | 36.02%     | ok               |
|          15 | -1.15%   | -60.83%            | -43.71% |     0.22 |       73 | 53.64%     | ok               |

## AVGO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 6.44%    | 68.02%             | -39.09% |     0.25 |       70 | 43.09%     | ok               |
|          30 | 3.47%    | 68.02%             | -40.82% |     0.21 |       66 | 40.43%     | ok               |
|          20 | -0.60%   | 68.02%             | -40.93% |     0.17 |       79 | 46.42%     | ok               |
|          50 | -4.36%   | 68.02%             | -38.98% |     0.1  |       60 | 28.29%     | ok               |
|          15 | -9.25%   | 68.02%             | -41.62% |     0.09 |       79 | 51.25%     | ok               |

## BA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 41.09%   | -2.69%             | -13.34% |     0.89 |       46 | 35.94%     | ok               |
|          40 | 31.81%   | -2.69%             | -23.87% |     0.63 |       46 | 43.43%     | ok               |
|          35 | 26.97%   | -2.69%             | -18.09% |     0.54 |       66 | 48.25%     | ok               |
|          25 | 23.04%   | -2.69%             | -26.02% |     0.47 |       68 | 54.74%     | ok               |
|          30 | 13.52%   | -2.69%             | -24.47% |     0.34 |       67 | 51.41%     | ok               |

## BAC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 0.90%    | 26.81%             | -16.89% |     0.11 |       82 | 54.41%     | ok               |
|          35 | -2.14%   | 26.81%             | -24.72% |     0.01 |       70 | 44.43%     | ok               |
|          25 | -3.76%   | 26.81%             | -22.06% |    -0.02 |       82 | 52.25%     | ok               |
|          15 | -5.72%   | 26.81%             | -21.05% |    -0.04 |       86 | 61.06%     | ok               |
|          45 | -5.16%   | 26.81%             | -18.05% |    -0.1  |       58 | 34.61%     | ok               |

## BCH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 17.04%   | -31.53%            | -45.51% |     0.39 |       80 | 56.51%     | ok               |
|          20 | 2.67%    | -31.53%            | -45.52% |     0.25 |       74 | 53.45%     | ok               |
|          35 | -9.06%   | -31.53%            | -57.75% |     0.1  |       72 | 44.06%     | ok               |
|          25 | -11.85%  | -31.53%            | -48.42% |     0.08 |       78 | 49.81%     | ok               |
|          30 | -14.22%  | -31.53%            | -54.04% |     0.04 |       82 | 47.89%     | ok               |

## BITO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -1.54%   | -58.97%            | -31.98% |     0.11 |       52 | 24.13%     | ok               |
|          45 | -15.11%  | -58.97%            | -32.05% |    -0.09 |       58 | 27.62%     | ok               |
|          15 | -30.39%  | -58.97%            | -51.86% |    -0.21 |       87 | 49.42%     | ok               |
|          40 | -23.67%  | -58.97%            | -40.13% |    -0.21 |       64 | 32.45%     | ok               |
|          30 | -27.08%  | -58.97%            | -43.13% |    -0.22 |       81 | 40.93%     | ok               |

## BLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 0.77%    | 52.17%             | -20.79% |     0.1  |       86 | 43.59%     | ok               |
|          20 | -2.75%   | 52.17%             | -21.48% |     0.02 |       82 | 51.75%     | ok               |
|          25 | -4.15%   | 52.17%             | -24.62% |    -0.02 |       75 | 49.58%     | ok               |
|          40 | -3.61%   | 52.17%             | -22.83% |    -0.03 |       78 | 39.10%     | ok               |
|          30 | -8.59%   | 52.17%             | -26.90% |    -0.15 |       79 | 47.09%     | ok               |

## BND Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.42%   | -1.39%             | -10.21% |    -0.9  |       64 | 40.77%     | ok               |
|          25 | -6.87%   | -1.39%             | -11.27% |    -1.01 |       69 | 38.44%     | ok               |
|          30 | -6.65%   | -1.39%             | -10.91% |    -1.03 |       67 | 34.78%     | ok               |
|          15 | -7.79%   | -1.39%             | -11.52% |    -1.09 |       76 | 43.26%     | ok               |
|          40 | -7.78%   | -1.39%             | -11.70% |    -1.34 |       56 | 28.79%     | ok               |

## BONK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 149.39%  | -82.94%            | -23.92% |     1.26 |       36 | 17.24%     | ok               |
|          40 | 140.84%  | -82.94%            | -43.89% |     1.09 |       66 | 34.87%     | ok               |
|          45 | 113.63%  | -82.94%            | -33.76% |     1.02 |       64 | 23.95%     | ok               |
|          35 | 97.69%   | -82.94%            | -48.16% |     0.87 |       62 | 40.80%     | ok               |
|          15 | 82.26%   | -82.94%            | -55.03% |     0.76 |       65 | 61.30%     | ok               |

## BTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 33.26%   | -28.45%            | -12.58% |     0.74 |       40 | 29.89%     | ok               |
|          40 | 30.35%   | -28.45%            | -19.29% |     0.67 |       48 | 34.67%     | ok               |
|          35 | 31.52%   | -28.45%            | -22.51% |     0.67 |       62 | 40.04%     | ok               |
|          50 | 17.11%   | -28.45%            | -20.63% |     0.48 |       36 | 25.29%     | ok               |
|          30 | 2.01%    | -28.45%            | -23.71% |     0.17 |       72 | 45.79%     | ok               |

## C Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -12.24%  | 99.65%             | -22.72% |    -0.29 |       68 | 30.95%     | ok               |
|          45 | -22.47%  | 99.65%             | -30.69% |    -0.57 |       78 | 36.27%     | ok               |
|          40 | -27.35%  | 99.65%             | -35.05% |    -0.67 |       74 | 38.77%     | ok               |
|          25 | -34.24%  | 99.65%             | -37.53% |    -0.72 |       71 | 50.08%     | ok               |
|          30 | -35.20%  | 99.65%             | -39.84% |    -0.76 |       81 | 47.42%     | ok               |

## CAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 50.74%   | 72.22%             | -21.80% |     0.75 |       73 | 61.56%     | ok               |
|          25 | 47.97%   | 72.22%             | -21.79% |     0.74 |       66 | 52.75%     | ok               |
|          45 | 38.99%   | 72.22%             | -23.56% |     0.67 |       54 | 38.94%     | ok               |
|          30 | 38.15%   | 72.22%             | -21.87% |     0.64 |       70 | 50.42%     | ok               |
|          50 | 33.12%   | 72.22%             | -21.79% |     0.6  |       54 | 37.10%     | ok               |

## CL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 10.02%   | 4.30%              | -13.51% |     0.41 |       42 | 24.79%     | ok               |
|          30 | 7.12%    | 4.30%              | -14.32% |     0.28 |       60 | 39.77%     | ok               |
|          45 | 4.33%    | 4.30%              | -13.13% |     0.21 |       46 | 27.29%     | ok               |
|          35 | 2.85%    | 4.30%              | -15.39% |     0.15 |       60 | 35.94%     | ok               |
|          40 | -0.72%   | 4.30%              | -15.09% |     0.04 |       56 | 30.78%     | ok               |

## CMCSA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -15.93%  | -28.90%            | -26.31% |    -0.51 |       48 | 16.31%     | ok               |
|          45 | -23.42%  | -28.90%            | -34.99% |    -0.74 |       60 | 20.97%     | ok               |
|          15 | -36.63%  | -28.90%            | -44.16% |    -0.76 |       88 | 58.40%     | ok               |
|          40 | -31.30%  | -28.90%            | -42.42% |    -0.84 |       89 | 28.45%     | ok               |
|          30 | -37.44%  | -28.90%            | -46.48% |    -0.91 |       84 | 43.43%     | ok               |

## COMP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -29.57%  | -55.46%            | -43.08% |    -0.24 |       50 | 23.37%     | ok               |
|          30 | -47.13%  | -55.46%            | -61.97% |    -0.36 |       99 | 48.66%     | ok               |
|          25 | -52.45%  | -55.46%            | -65.80% |    -0.43 |       98 | 56.70%     | ok               |
|          20 | -60.94%  | -55.46%            | -68.38% |    -0.59 |      106 | 63.03%     | ok               |
|          15 | -63.40%  | -55.46%            | -71.57% |    -0.59 |      103 | 67.82%     | ok               |

## COP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -9.15%   | 23.83%             | -34.61% |    -0.1  |       48 | 30.45%     | ok               |
|          35 | -14.59%  | 23.83%             | -41.23% |    -0.18 |       67 | 41.43%     | ok               |
|          30 | -15.96%  | 23.83%             | -39.71% |    -0.2  |       64 | 43.76%     | ok               |
|          45 | -14.10%  | 23.83%             | -39.75% |    -0.2  |       60 | 34.11%     | ok               |
|          40 | -19.52%  | 23.83%             | -46.32% |    -0.32 |       66 | 37.27%     | ok               |

## COST Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 14.32%   | 24.53%             | -24.32% |     0.46 |       64 | 47.59%     | ok               |
|          25 | 10.51%   | 24.53%             | -24.93% |     0.37 |       63 | 44.59%     | ok               |
|          35 | 4.96%    | 24.53%             | -30.16% |     0.22 |       58 | 38.44%     | ok               |
|          30 | -0.23%   | 24.53%             | -31.32% |     0.06 |       62 | 41.10%     | ok               |
|          15 | -1.17%   | 24.53%             | -27.30% |     0.05 |       69 | 51.25%     | ok               |

## CRM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -19.70%  | -4.11%             | -29.70% |    -0.22 |       64 | 41.43%     | ok               |
|          40 | -22.71%  | -4.11%             | -35.43% |    -0.3  |       70 | 37.27%     | ok               |
|          15 | -31.45%  | -4.11%             | -47.54% |    -0.36 |       92 | 58.07%     | ok               |
|          30 | -30.72%  | -4.11%             | -41.89% |    -0.43 |       67 | 46.26%     | ok               |
|          20 | -33.83%  | -4.11%             | -45.97% |    -0.44 |       74 | 51.75%     | ok               |

## CRV-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 78.45%   | -62.65%            | -37.78% |     0.82 |       66 | 32.38%     | ok               |
|          40 | 62.55%   | -62.65%            | -38.86% |     0.73 |       54 | 28.16%     | ok               |
|          45 | 44.46%   | -62.65%            | -42.29% |     0.62 |       54 | 21.84%     | ok               |
|          30 | 43.42%   | -62.65%            | -39.89% |     0.59 |       66 | 36.97%     | ok               |
|          50 | 31.81%   | -62.65%            | -30.73% |     0.52 |       48 | 17.62%     | ok               |

## CSCO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 37.68%   | 109.54%            | -19.34% |     0.75 |       52 | 41.26%     | ok               |
|          50 | 30.48%   | 109.54%            | -19.34% |     0.64 |       52 | 39.77%     | ok               |
|          40 | 19.65%   | 109.54%            | -22.37% |     0.45 |       56 | 44.09%     | ok               |
|          35 | 15.88%   | 109.54%            | -23.68% |     0.39 |       58 | 47.59%     | ok               |
|          25 | 9.14%    | 109.54%            | -23.73% |     0.27 |       63 | 51.91%     | ok               |

## CVX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -9.50%   | 39.56%             | -23.80% |    -0.15 |       71 | 45.92%     | ok               |
|          40 | -12.19%  | 39.56%             | -27.34% |    -0.27 |       75 | 39.10%     | ok               |
|          30 | -13.55%  | 39.56%             | -27.78% |    -0.28 |       69 | 43.09%     | ok               |
|          45 | -12.58%  | 39.56%             | -28.83% |    -0.29 |       67 | 35.77%     | ok               |
|          20 | -14.64%  | 39.56%             | -24.17% |    -0.29 |       73 | 47.42%     | ok               |

## DASH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 77.59%   | 100.58%            | -43.46% |     0.72 |       42 | 17.62%     | ok               |
|          40 | 71.19%   | 100.58%            | -42.64% |     0.69 |       48 | 24.14%     | ok               |
|          45 | 34.38%   | 100.58%            | -46.93% |     0.5  |       46 | 20.11%     | ok               |
|          30 | -15.94%  | 100.58%            | -64.43% |     0.28 |       57 | 30.65%     | ok               |
|          25 | -16.74%  | 100.58%            | -64.14% |     0.27 |       67 | 32.95%     | ok               |

## DBC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -4.64%   | 36.41%             | -26.05% |    -0.08 |       81 | 42.26%     | ok               |
|          20 | -8.83%   | 36.41%             | -25.69% |    -0.22 |       73 | 40.60%     | ok               |
|          25 | -9.03%   | 36.41%             | -24.84% |    -0.23 |       68 | 38.44%     | ok               |
|          50 | -9.26%   | 36.41%             | -18.84% |    -0.3  |       50 | 25.46%     | ok               |
|          35 | -11.42%  | 36.41%             | -23.19% |    -0.33 |       68 | 35.11%     | ok               |

## DE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 0.11%    | 75.48%             | -17.97% |     0.08 |       58 | 29.78%     | ok               |
|          45 | -2.26%   | 75.48%             | -18.05% |     0.03 |       58 | 33.78%     | ok               |
|          20 | -6.40%   | 75.48%             | -22.20% |    -0.04 |       66 | 48.42%     | ok               |
|          25 | -7.76%   | 75.48%             | -22.39% |    -0.07 |       73 | 46.42%     | ok               |
|          30 | -8.15%   | 75.48%             | -22.44% |    -0.08 |       72 | 43.59%     | ok               |

## DIA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -7.31%   | 33.07%             | -13.26% |    -0.35 |       64 | 45.42%     | ok               |
|          20 | -9.54%   | 33.07%             | -15.28% |    -0.46 |       68 | 47.59%     | ok               |
|          35 | -9.00%   | 33.07%             | -16.63% |    -0.47 |       72 | 41.10%     | ok               |
|          30 | -9.40%   | 33.07%             | -15.89% |    -0.48 |       70 | 44.26%     | ok               |
|          40 | -11.59%  | 33.07%             | -18.12% |    -0.65 |       74 | 37.60%     | ok               |

## DIS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 41.80%   | 17.26%             | -10.17% |     1.2  |       50 | 28.12%     | ok               |
|          40 | 12.39%   | 17.26%             | -18.75% |     0.37 |       65 | 36.27%     | ok               |
|          45 | 9.79%    | 17.26%             | -16.54% |     0.32 |       51 | 31.78%     | ok               |
|          15 | 3.88%    | 17.26%             | -32.73% |     0.18 |       81 | 55.41%     | ok               |
|          35 | 1.58%    | 17.26%             | -25.30% |     0.13 |       73 | 42.26%     | ok               |

## DOGE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 0.19%    | -63.02%            | -49.94% |     0.19 |       54 | 22.80%     | ok               |
|          15 | -16.67%  | -63.02%            | -59.12% |     0.08 |       81 | 63.41%     | ok               |
|          20 | -16.28%  | -63.02%            | -59.20% |     0.06 |       77 | 57.66%     | ok               |
|          25 | -15.93%  | -63.02%            | -59.73% |     0.05 |       72 | 53.64%     | ok               |
|          30 | -26.29%  | -63.02%            | -61.39% |    -0.11 |       70 | 47.32%     | ok               |

## DOT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -46.55%  | -77.82%            | -65.96% |    -0.29 |       83 | 56.51%     | ok               |
|          15 | -51.73%  | -77.82%            | -72.35% |    -0.32 |       72 | 60.34%     | ok               |
|          30 | -47.40%  | -77.82%            | -63.40% |    -0.36 |       80 | 45.98%     | ok               |
|          25 | -54.86%  | -77.82%            | -71.03% |    -0.47 |       74 | 51.53%     | ok               |
|          35 | -54.57%  | -77.82%            | -65.25% |    -0.54 |       80 | 40.42%     | ok               |

## DXY-INDEX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -2.27%   | -6.69%             | -6.06%  |    -0.37 |       40 | 31.17%     | ok               |
|          40 | -4.56%   | -6.69%             | -7.30%  |    -0.63 |       66 | 46.54%     | ok               |
|          45 | -4.54%   | -6.69%             | -8.12%  |    -0.67 |       60 | 37.45%     | ok               |
|          15 | -9.33%   | -6.69%             | -11.81% |    -0.95 |       97 | 72.51%     | ok               |
|          30 | -7.69%   | -6.69%             | -9.98%  |    -0.98 |       76 | 56.71%     | ok               |

## EEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -2.00%   | 37.46%             | -26.88% |     0.01 |       66 | 44.26%     | ok               |
|          35 | -2.67%   | 37.46%             | -23.88% |    -0.02 |       70 | 39.10%     | ok               |
|          25 | -3.07%   | 37.46%             | -25.42% |    -0.02 |       66 | 42.60%     | ok               |
|          40 | -3.15%   | 37.46%             | -19.52% |    -0.04 |       70 | 37.27%     | ok               |
|          30 | -4.23%   | 37.46%             | -24.14% |    -0.06 |       66 | 40.93%     | ok               |

## EFA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -1.46%   | 31.95%             | -10.10% |     0.01 |       62 | 49.25%     | ok               |
|          20 | -8.60%   | 31.95%             | -12.23% |    -0.3  |       69 | 46.42%     | ok               |
|          30 | -9.07%   | 31.95%             | -12.63% |    -0.35 |       64 | 38.94%     | ok               |
|          25 | -9.53%   | 31.95%             | -13.73% |    -0.36 |       68 | 42.60%     | ok               |
|          40 | -8.70%   | 31.95%             | -14.58% |    -0.37 |       58 | 34.28%     | ok               |

## EOG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -16.83%  | 22.54%             | -35.29% |    -0.33 |       56 | 32.78%     | ok               |
|          40 | -20.14%  | 22.54%             | -37.34% |    -0.41 |       68 | 36.11%     | ok               |
|          35 | -24.45%  | 22.54%             | -40.74% |    -0.52 |       79 | 40.10%     | ok               |
|          50 | -22.52%  | 22.54%             | -35.58% |    -0.52 |       56 | 30.28%     | ok               |
|          30 | -30.39%  | 22.54%             | -47.87% |    -0.65 |       78 | 44.93%     | ok               |

## ETC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -2.30%   | -60.26%            | -28.33% |     0.1  |       28 | 18.20%     | ok               |
|          35 | -5.67%   | -60.26%            | -42.62% |     0.08 |       46 | 30.84%     | ok               |
|          30 | -8.68%   | -60.26%            | -45.54% |     0.04 |       54 | 34.10%     | ok               |
|          45 | -6.54%   | -60.26%            | -35.44% |     0.03 |       32 | 21.26%     | ok               |
|          40 | -13.08%  | -60.26%            | -40.48% |    -0.07 |       46 | 25.29%     | ok               |

## ETH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 108.52%  | -14.53%            | -30.11% |     1.11 |       59 | 46.55%     | ok               |
|          30 | 73.22%   | -14.53%            | -32.89% |     0.85 |       63 | 54.21%     | ok               |
|          40 | 55.90%   | -14.53%            | -33.11% |     0.78 |       60 | 38.70%     | ok               |
|          45 | 46.60%   | -14.53%            | -34.50% |     0.71 |       62 | 35.63%     | ok               |
|          25 | 52.47%   | -14.53%            | -40.90% |     0.69 |       61 | 58.05%     | ok               |

## EWJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -18.52%  | 31.48%             | -30.00% |    -0.56 |       58 | 39.43%     | ok               |
|          25 | -20.52%  | 31.48%             | -29.85% |    -0.64 |       58 | 38.60%     | ok               |
|          15 | -22.43%  | 31.48%             | -31.15% |    -0.66 |       69 | 42.76%     | ok               |
|          30 | -22.16%  | 31.48%             | -29.40% |    -0.75 |       64 | 37.27%     | ok               |
|          45 | -23.95%  | 31.48%             | -27.68% |    -0.98 |       58 | 28.12%     | ok               |

## FCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 6.25%    | 20.35%             | -30.39% |     0.23 |       54 | 32.61%     | ok               |
|          50 | 3.55%    | 20.35%             | -26.57% |     0.19 |       56 | 28.95%     | ok               |
|          40 | -7.23%   | 20.35%             | -42.89% |     0.04 |       66 | 37.44%     | ok               |
|          30 | -23.15%  | 20.35%             | -46.84% |    -0.2  |       69 | 44.93%     | ok               |
|          35 | -27.02%  | 20.35%             | -50.12% |    -0.29 |       71 | 42.60%     | ok               |

## FET-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 15.64%   | -82.16%            | -59.58% |     0.42 |       71 | 57.47%     | ok               |
|          25 | -12.65%  | -82.16%            | -65.31% |     0.18 |       79 | 48.85%     | ok               |
|          20 | -14.52%  | -82.16%            | -66.17% |     0.17 |       82 | 54.02%     | ok               |
|          30 | -34.32%  | -82.16%            | -66.52% |    -0.09 |       79 | 44.44%     | ok               |
|          45 | -37.74%  | -82.16%            | -51.19% |    -0.39 |       54 | 22.22%     | ok               |

## FIL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -36.78%  | -69.42%            | -58.54% |    -0.27 |       71 | 38.12%     | ok               |
|          15 | -53.98%  | -69.42%            | -71.82% |    -0.45 |       93 | 51.72%     | ok               |
|          40 | -42.60%  | -69.42%            | -57.60% |    -0.47 |       50 | 27.78%     | ok               |
|          35 | -45.21%  | -69.42%            | -63.99% |    -0.48 |       62 | 31.61%     | ok               |
|          20 | -59.67%  | -69.42%            | -75.30% |    -0.61 |       96 | 47.89%     | ok               |

## FXI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -0.74%   | 33.51%             | -21.68% |     0.07 |       50 | 34.61%     | ok               |
|          25 | -0.86%   | 33.51%             | -22.57% |     0.06 |       48 | 31.45%     | ok               |
|          30 | -3.03%   | 33.51%             | -23.91% |     0.01 |       46 | 30.12%     | ok               |
|          20 | -6.09%   | 33.51%             | -24.53% |    -0.07 |       48 | 32.78%     | ok               |
|          35 | -6.68%   | 33.51%             | -27.53% |    -0.09 |       48 | 27.79%     | ok               |

## GDX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 0.03%    | 156.66%            | -30.00% |     0.15 |       80 | 51.08%     | ok               |
|          40 | -2.19%   | 156.66%            | -33.54% |     0.09 |       64 | 38.77%     | ok               |
|          30 | -3.66%   | 156.66%            | -33.40% |     0.08 |       66 | 44.93%     | ok               |
|          35 | -7.85%   | 156.66%            | -37.85% |     0.01 |       72 | 41.43%     | ok               |
|          25 | -12.72%  | 156.66%            | -41.63% |    -0.06 |       70 | 46.76%     | ok               |

## GDXJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -11.42%  | 150.39%            | -34.84% |     0.02 |       70 | 51.41%     | ok               |
|          35 | -23.47%  | 150.39%            | -37.15% |    -0.21 |       68 | 41.60%     | ok               |
|          30 | -25.59%  | 150.39%            | -35.04% |    -0.24 |       68 | 44.26%     | ok               |
|          25 | -30.10%  | 150.39%            | -39.58% |    -0.29 |       73 | 47.42%     | ok               |
|          40 | -26.38%  | 150.39%            | -44.70% |    -0.29 |       62 | 39.10%     | ok               |

## GE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 4.89%    | 101.91%            | -21.25% |     0.2  |       60 | 33.78%     | ok               |
|          45 | -7.35%   | 101.91%            | -21.88% |    -0.05 |       72 | 36.77%     | ok               |
|          30 | -13.14%  | 101.91%            | -27.82% |    -0.14 |       78 | 48.42%     | ok               |
|          25 | -13.54%  | 101.91%            | -29.91% |    -0.14 |       74 | 50.25%     | ok               |
|          20 | -14.02%  | 101.91%            | -25.05% |    -0.14 |       74 | 52.91%     | ok               |

## GLD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 21.05%   | 74.06%             | -13.87% |     0.54 |       48 | 47.59%     | ok               |
|          20 | 19.41%   | 74.06%             | -13.87% |     0.51 |       49 | 49.25%     | ok               |
|          30 | 11.67%   | 74.06%             | -14.15% |     0.35 |       52 | 46.09%     | ok               |
|          35 | 8.96%    | 74.06%             | -15.57% |     0.3  |       52 | 43.43%     | ok               |
|          15 | 9.15%    | 74.06%             | -18.05% |     0.29 |       55 | 52.75%     | ok               |

## GOOGL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 80.37%   | 59.83%             | -17.38% |     1.23 |       59 | 44.26%     | ok               |
|          30 | 77.51%   | 59.83%             | -16.84% |     1.17 |       57 | 48.09%     | ok               |
|          45 | 67.54%   | 59.83%             | -11.66% |     1.16 |       52 | 37.77%     | ok               |
|          25 | 74.80%   | 59.83%             | -16.16% |     1.13 |       57 | 50.58%     | ok               |
|          50 | 62.60%   | 59.83%             | -11.52% |     1.12 |       44 | 32.95%     | ok               |

## GRT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 71.49%   | -80.37%            | -36.70% |     0.75 |       70 | 61.88%     | ok               |
|          45 | 50.91%   | -80.37%            | -39.68% |     0.68 |       50 | 29.12%     | ok               |
|          35 | 47.42%   | -80.37%            | -37.94% |     0.63 |       66 | 42.15%     | ok               |
|          30 | 45.55%   | -80.37%            | -43.87% |     0.61 |       75 | 47.32%     | ok               |
|          25 | 45.28%   | -80.37%            | -37.25% |     0.6  |       80 | 52.49%     | ok               |

## GS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 22.58%   | 94.63%             | -20.56% |     0.5  |       66 | 55.24%     | ok               |
|          40 | 7.27%    | 94.63%             | -16.16% |     0.25 |       64 | 40.93%     | ok               |
|          20 | 7.49%    | 94.63%             | -23.19% |     0.25 |       64 | 51.91%     | ok               |
|          25 | -0.60%   | 94.63%             | -23.32% |     0.09 |       66 | 49.92%     | ok               |
|          35 | -1.92%   | 94.63%             | -19.95% |     0.06 |       68 | 44.59%     | ok               |

## HBAR-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -21.68%  | -33.83%            | -49.09% |    -0.28 |       26 | 27.97%     | ok               |
|          40 | -23.38%  | -33.83%            | -51.16% |    -0.31 |       30 | 33.92%     | ok               |
|          50 | -25.34%  | -33.83%            | -40.09% |    -0.43 |       32 | 19.23%     | ok               |
|          35 | -29.85%  | -33.83%            | -56.01% |    -0.46 |       30 | 38.46%     | ok               |
|          30 | -30.58%  | -33.83%            | -56.47% |    -0.46 |       40 | 42.66%     | ok               |

## HD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 6.90%    | 0.89%              | -17.15% |     0.25 |       73 | 44.59%     | ok               |
|          35 | 5.49%    | 0.89%              | -18.52% |     0.22 |       74 | 39.93%     | ok               |
|          25 | 3.25%    | 0.89%              | -18.88% |     0.16 |       74 | 47.09%     | ok               |
|          40 | 1.21%    | 0.89%              | -18.05% |     0.11 |       76 | 34.94%     | ok               |
|          45 | 0.41%    | 0.89%              | -18.71% |     0.08 |       52 | 30.12%     | ok               |

## HON Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -10.86%  | 4.68%              | -20.54% |    -0.27 |       64 | 31.95%     | ok               |
|          45 | -14.48%  | 4.68%              | -22.88% |    -0.37 |       66 | 37.10%     | ok               |
|          35 | -27.07%  | 4.68%              | -31.66% |    -0.72 |       89 | 48.59%     | ok               |
|          30 | -28.67%  | 4.68%              | -33.87% |    -0.74 |       89 | 53.58%     | ok               |
|          40 | -26.84%  | 4.68%              | -31.84% |    -0.74 |       74 | 41.26%     | ok               |

## HYG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -4.17%   | 0.29%              | -7.76%  |    -0.47 |       68 | 34.28%     | ok               |
|          45 | -5.94%   | 0.29%              | -8.86%  |    -0.71 |       68 | 30.62%     | ok               |
|          35 | -6.39%   | 0.29%              | -9.66%  |    -0.73 |       77 | 36.11%     | ok               |
|          30 | -6.94%   | 0.29%              | -10.69% |    -0.77 |       87 | 39.60%     | ok               |
|          25 | -7.66%   | 0.29%              | -11.32% |    -0.83 |       89 | 42.60%     | ok               |

## IBIT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 52.34%   | 13.21%             | -17.37% |     0.92 |       26 | 24.75%     | ok               |
|          15 | 56.87%   | 13.21%             | -19.20% |     0.84 |       46 | 42.44%     | ok               |
|          45 | 42.91%   | 13.21%             | -17.37% |     0.78 |       32 | 26.13%     | ok               |
|          30 | 28.46%   | 13.21%             | -18.95% |     0.56 |       44 | 34.97%     | ok               |
|          40 | 26.72%   | 13.21%             | -22.57% |     0.56 |       36 | 28.49%     | ok               |

## IBM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -13.25%  | 46.04%             | -49.43% |    -0.04 |       83 | 62.23%     | ok               |
|          35 | -18.19%  | 46.04%             | -47.10% |    -0.16 |       63 | 47.59%     | ok               |
|          30 | -19.90%  | 46.04%             | -48.94% |    -0.19 |       69 | 50.75%     | ok               |
|          20 | -25.70%  | 46.04%             | -53.45% |    -0.27 |       69 | 55.24%     | ok               |
|          25 | -30.78%  | 46.04%             | -55.45% |    -0.38 |       66 | 52.91%     | ok               |

## ICP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 2.24%    | -54.68%            | -40.43% |     0.28 |       72 | 39.08%     | ok               |
|          15 | -26.78%  | -54.68%            | -59.70% |     0.08 |       72 | 50.77%     | ok               |
|          40 | -12.50%  | -54.68%            | -46.21% |     0.07 |       62 | 29.89%     | ok               |
|          35 | -13.92%  | -54.68%            | -52.13% |     0.07 |       70 | 34.10%     | ok               |
|          20 | -26.09%  | -54.68%            | -63.34% |     0.07 |       80 | 47.70%     | ok               |

## IEF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -5.06%   | -2.78%             | -10.18% |    -0.59 |       72 | 42.26%     | ok               |
|          15 | -6.30%   | -2.78%             | -10.91% |    -0.72 |       71 | 43.93%     | ok               |
|          25 | -8.61%   | -2.78%             | -11.95% |    -1.08 |       76 | 39.27%     | ok               |
|          40 | -8.18%   | -2.78%             | -11.24% |    -1.19 |       60 | 26.46%     | ok               |
|          50 | -7.12%   | -2.78%             | -9.11%  |    -1.21 |       54 | 21.46%     | ok               |

## IEMG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 2.45%    | 33.19%             | -21.81% |     0.14 |       67 | 39.77%     | ok               |
|          25 | 2.38%    | 33.19%             | -23.73% |     0.14 |       61 | 43.09%     | ok               |
|          20 | 0.65%    | 33.19%             | -25.26% |     0.09 |       59 | 44.76%     | ok               |
|          40 | 0.35%    | 33.19%             | -18.73% |     0.07 |       66 | 37.77%     | ok               |
|          30 | -0.96%   | 33.19%             | -24.73% |     0.04 |       62 | 40.77%     | ok               |

## INJ-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 22.90%   | -34.77%            | -44.07% |     0.44 |       54 | 36.02%     | ok               |
|          40 | 19.78%   | -34.77%            | -36.12% |     0.41 |       46 | 32.95%     | ok               |
|          45 | 6.85%    | -34.77%            | -38.36% |     0.29 |       52 | 27.01%     | ok               |
|          15 | -16.49%  | -34.77%            | -69.00% |     0.13 |       70 | 47.51%     | ok               |
|          25 | -20.17%  | -34.77%            | -63.91% |     0.07 |       61 | 42.53%     | ok               |

## INTC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 109.67%  | 71.59%             | -49.32% |     0.89 |       58 | 34.44%     | ok               |
|          50 | 103.15%  | 71.59%             | -48.35% |     0.87 |       62 | 30.62%     | ok               |
|          40 | 86.67%   | 71.59%             | -55.86% |     0.77 |       66 | 38.60%     | ok               |
|          15 | 86.44%   | 71.59%             | -53.65% |     0.74 |       78 | 59.57%     | ok               |
|          20 | 79.56%   | 71.59%             | -52.47% |     0.72 |       80 | 55.74%     | ok               |

## INTU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 21.49%   | -40.43%            | -34.18% |     0.47 |       67 | 29.45%     | ok               |
|          35 | 17.36%   | -40.43%            | -41.63% |     0.39 |       69 | 41.76%     | ok               |
|          25 | 16.37%   | -40.43%            | -35.24% |     0.37 |       69 | 50.58%     | ok               |
|          45 | 14.79%   | -40.43%            | -36.41% |     0.36 |       65 | 33.44%     | ok               |
|          40 | 14.14%   | -40.43%            | -38.72% |     0.35 |       69 | 37.10%     | ok               |

## ITA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.12%   | 54.46%             | -21.48% |     0.06 |       68 | 34.94%     | ok               |
|          30 | -1.32%   | 54.46%             | -23.75% |     0.04 |       72 | 47.42%     | ok               |
|          15 | -2.28%   | 54.46%             | -28.06% |     0.04 |       73 | 59.90%     | ok               |
|          40 | -4.89%   | 54.46%             | -20.54% |    -0.08 |       70 | 39.93%     | ok               |
|          35 | -5.60%   | 54.46%             | -23.12% |    -0.09 |       72 | 43.59%     | ok               |

## IWM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          25 | 17.01%   | 36.36%             | -8.02% |     0.63 |       54 | 36.11%     | ok               |
|          20 | 15.47%   | 36.36%             | -9.67% |     0.57 |       60 | 37.10%     | ok               |
|          40 | 10.02%   | 36.36%             | -9.06% |     0.45 |       48 | 29.62%     | ok               |
|          15 | 11.92%   | 36.36%             | -8.91% |     0.44 |       78 | 42.93%     | ok               |
|          30 | 10.62%   | 36.36%             | -8.62% |     0.43 |       58 | 34.78%     | ok               |

## JNJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 19.65%   | 87.11%             | -10.97% |     0.77 |       42 | 35.44%     | ok               |
|          15 | 15.76%   | 87.11%             | -18.02% |     0.55 |       58 | 52.91%     | ok               |
|          30 | 10.77%   | 87.11%             | -17.51% |     0.42 |       60 | 46.42%     | ok               |
|          20 | 10.41%   | 87.11%             | -17.61% |     0.4  |       64 | 49.42%     | ok               |
|          45 | 9.41%    | 87.11%             | -13.35% |     0.4  |       48 | 39.10%     | ok               |

## JPM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 1.50%    | 74.08%             | -15.90% |     0.11 |       50 | 31.78%     | ok               |
|          45 | -8.97%   | 74.08%             | -21.91% |    -0.23 |       54 | 34.44%     | ok               |
|          20 | -24.26%  | 74.08%             | -35.58% |    -0.55 |       86 | 48.75%     | ok               |
|          40 | -21.46%  | 74.08%             | -28.47% |    -0.65 |       66 | 37.10%     | ok               |
|          35 | -22.15%  | 74.08%             | -27.43% |    -0.66 |       76 | 40.60%     | ok               |

## KO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 28.20%   | 53.05%             | -8.64%  |     0.94 |       52 | 38.60%     | ok               |
|          35 | 23.84%   | 53.05%             | -8.73%  |     0.83 |       56 | 37.10%     | ok               |
|          40 | 20.86%   | 53.05%             | -9.28%  |     0.78 |       58 | 33.78%     | ok               |
|          25 | 21.96%   | 53.05%             | -10.61% |     0.75 |       58 | 41.26%     | ok               |
|          50 | 8.08%    | 53.05%             | -16.13% |     0.37 |       42 | 27.95%     | ok               |

## LDO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 141.40%  | -60.93%            | -39.01% |     0.99 |       74 | 59.77%     | ok               |
|          20 | 90.62%   | -60.93%            | -44.07% |     0.81 |       77 | 55.17%     | ok               |
|          30 | 47.84%   | -60.93%            | -53.44% |     0.61 |       70 | 47.89%     | ok               |
|          25 | 34.36%   | -60.93%            | -48.17% |     0.53 |       78 | 52.49%     | ok               |
|          35 | 23.44%   | -60.93%            | -60.70% |     0.45 |       80 | 40.80%     | ok               |

## LIN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -0.62%   | 19.29%             | -22.01% |     0.04 |       69 | 43.76%     | ok               |
|          20 | -1.40%   | 19.29%             | -23.00% |     0.02 |       64 | 46.59%     | ok               |
|          15 | -3.30%   | 19.29%             | -23.68% |    -0.04 |       70 | 49.58%     | ok               |
|          30 | -3.93%   | 19.29%             | -20.61% |    -0.07 |       70 | 40.93%     | ok               |
|          45 | -4.21%   | 19.29%             | -17.04% |    -0.12 |       48 | 24.63%     | ok               |

## LINK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 31.11%   | -24.18%            | -34.17% |     0.51 |       66 | 43.30%     | ok               |
|          35 | 17.53%   | -24.18%            | -34.21% |     0.39 |       60 | 39.46%     | ok               |
|          45 | 14.98%   | -24.18%            | -33.71% |     0.36 |       54 | 30.65%     | ok               |
|          40 | 14.50%   | -24.18%            | -34.00% |     0.36 |       56 | 34.29%     | ok               |
|          50 | 12.43%   | -24.18%            | -27.70% |     0.33 |       46 | 25.29%     | ok               |

## LLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 0.65%    | 55.36%             | -38.23% |     0.13 |       50 | 35.44%     | ok               |
|          15 | -13.55%  | 55.36%             | -48.12% |    -0.07 |       70 | 60.23%     | ok               |
|          45 | -12.97%  | 55.36%             | -42.99% |    -0.13 |       60 | 39.27%     | ok               |
|          40 | -24.03%  | 55.36%             | -46.54% |    -0.34 |       70 | 42.26%     | ok               |
|          20 | -27.36%  | 55.36%             | -52.31% |    -0.35 |       77 | 55.24%     | ok               |

## LRCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 8.96%    | 78.77%             | -48.71% |     0.28 |       76 | 36.27%     | ok               |
|          40 | 5.31%    | 78.77%             | -53.45% |     0.25 |       72 | 42.43%     | ok               |
|          35 | 3.29%    | 78.77%             | -56.72% |     0.23 |       80 | 44.59%     | ok               |
|          15 | -2.60%   | 78.77%             | -57.13% |     0.19 |       80 | 53.41%     | ok               |
|          20 | -3.05%   | 78.77%             | -59.99% |     0.18 |       84 | 49.25%     | ok               |

## LTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 18.09%   | -41.76%            | -34.94% |     0.4  |       68 | 44.06%     | ok               |
|          45 | 17.31%   | -41.76%            | -36.44% |     0.4  |       56 | 34.10%     | ok               |
|          30 | 9.35%    | -41.76%            | -30.78% |     0.31 |       69 | 50.77%     | ok               |
|          25 | 8.08%    | -41.76%            | -34.22% |     0.29 |       69 | 53.45%     | ok               |
|          50 | 5.08%    | -41.76%            | -33.81% |     0.24 |       54 | 25.67%     | ok               |

## MCD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 10.05%   | 9.65%              | -9.22%  |     0.47 |       48 | 25.12%     | ok               |
|          30 | 9.57%    | 9.65%              | -22.20% |     0.38 |       77 | 40.43%     | ok               |
|          35 | 7.42%    | 9.65%              | -16.97% |     0.33 |       69 | 37.77%     | ok               |
|          25 | 6.17%    | 9.65%              | -23.93% |     0.27 |       77 | 42.93%     | ok               |
|          20 | 1.84%    | 9.65%              | -24.58% |     0.12 |       79 | 46.09%     | ok               |

## META Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -12.74%  | 20.02%             | -37.54% |    -0.12 |       66 | 39.10%     | ok               |
|          40 | -16.44%  | 20.02%             | -40.90% |    -0.18 |       68 | 42.43%     | ok               |
|          50 | -22.46%  | 20.02%             | -39.33% |    -0.34 |       68 | 34.94%     | ok               |
|          30 | -29.07%  | 20.02%             | -44.90% |    -0.41 |       72 | 50.08%     | ok               |
|          25 | -31.20%  | 20.02%             | -45.70% |    -0.45 |       73 | 52.75%     | ok               |

## MPC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 19.12%   | 121.86%            | -19.02% |     0.43 |       54 | 41.60%     | ok               |
|          40 | 17.16%   | 121.86%            | -20.88% |     0.39 |       64 | 48.25%     | ok               |
|          35 | 16.33%   | 121.86%            | -31.08% |     0.38 |       70 | 50.92%     | ok               |
|          45 | 15.10%   | 121.86%            | -20.23% |     0.37 |       60 | 45.59%     | ok               |
|          30 | 10.68%   | 121.86%            | -33.74% |     0.29 |       70 | 53.24%     | ok               |

## MRK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -13.10%  | 13.48%             | -28.40% |    -0.16 |       85 | 52.08%     | ok               |
|          25 | -13.87%  | 13.48%             | -31.07% |    -0.2  |       72 | 44.26%     | ok               |
|          20 | -18.09%  | 13.48%             | -29.34% |    -0.29 |       77 | 47.59%     | ok               |
|          50 | -14.54%  | 13.48%             | -23.01% |    -0.3  |       56 | 28.45%     | ok               |
|          45 | -16.67%  | 13.48%             | -25.38% |    -0.33 |       57 | 31.78%     | ok               |

## MS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 0.02%    | 91.04%             | -22.02% |     0.1  |       74 | 57.74%     | ok               |
|          40 | 0.40%    | 91.04%             | -19.99% |     0.09 |       70 | 39.10%     | ok               |
|          20 | -3.21%   | 91.04%             | -25.68% |     0.02 |       75 | 53.41%     | ok               |
|          30 | -7.18%   | 91.04%             | -27.79% |    -0.09 |       77 | 48.42%     | ok               |
|          25 | -8.64%   | 91.04%             | -28.36% |    -0.12 |       75 | 50.58%     | ok               |

## MSFT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -15.96%  | 21.09%             | -24.64% |    -0.37 |       70 | 36.94%     | ok               |
|          50 | -19.36%  | 21.09%             | -25.48% |    -0.5  |       60 | 31.78%     | ok               |
|          35 | -25.42%  | 21.09%             | -35.38% |    -0.57 |       73 | 46.26%     | ok               |
|          40 | -25.20%  | 21.09%             | -34.92% |    -0.59 |       69 | 40.60%     | ok               |
|          30 | -28.52%  | 21.09%             | -39.07% |    -0.63 |       83 | 50.92%     | ok               |

## MU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 138.92%  | 364.34%            | -64.26% |     1.01 |       58 | 45.42%     | ok               |
|          30 | 116.71%  | 364.34%            | -68.76% |     0.91 |       51 | 49.92%     | ok               |
|          35 | 108.99%  | 364.34%            | -69.35% |     0.89 |       63 | 47.75%     | ok               |
|          15 | 119.68%  | 364.34%            | -61.96% |     0.87 |       54 | 58.40%     | ok               |
|          25 | 104.59%  | 364.34%            | -67.90% |     0.85 |       53 | 51.58%     | ok               |

## NEAR-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 235.36%  | 47.22%             | -37.89% |     1.45 |       28 | 22.61%     | ok               |
|          40 | 257.67%  | 47.22%             | -41.76% |     1.41 |       40 | 32.38%     | ok               |
|          45 | 200.17%  | 47.22%             | -38.08% |     1.26 |       42 | 28.35%     | ok               |
|          30 | 172.41%  | 47.22%             | -46.79% |     1.12 |       65 | 43.10%     | ok               |
|          35 | 161.03%  | 47.22%             | -52.15% |     1.11 |       60 | 36.21%     | ok               |

## NEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -4.57%   | 193.26%            | -30.50% |     0.1  |       71 | 54.08%     | ok               |
|          15 | -7.30%   | 193.26%            | -35.45% |     0.08 |       66 | 58.74%     | ok               |
|          50 | -12.51%  | 193.26%            | -33.03% |    -0.06 |       48 | 37.77%     | ok               |
|          25 | -19.14%  | 193.26%            | -39.51% |    -0.12 |       68 | 51.75%     | ok               |
|          30 | -25.86%  | 193.26%            | -39.56% |    -0.25 |       70 | 49.75%     | ok               |

## NFLX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 17.19%   | -2.06%             | -16.28% |     0.49 |       44 | 31.28%     | ok               |
|          40 | 15.86%   | -2.06%             | -20.78% |     0.44 |       52 | 39.10%     | ok               |
|          35 | 11.92%   | -2.06%             | -18.30% |     0.35 |       76 | 43.76%     | ok               |
|          45 | 5.48%    | -2.06%             | -18.06% |     0.22 |       58 | 35.61%     | ok               |
|          15 | -1.29%   | -2.06%             | -26.59% |     0.1  |       76 | 63.89%     | ok               |

## NKE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -18.37%  | -57.64%            | -42.13% |    -0.19 |       73 | 40.43%     | ok               |
|          20 | -23.09%  | -57.64%            | -49.34% |    -0.2  |       87 | 55.07%     | ok               |
|          25 | -26.28%  | -57.64%            | -51.20% |    -0.26 |       87 | 52.41%     | ok               |
|          15 | -29.79%  | -57.64%            | -55.79% |    -0.32 |       90 | 58.90%     | ok               |
|          30 | -29.16%  | -57.64%            | -55.35% |    -0.33 |       85 | 47.92%     | ok               |

## NOW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -9.05%   | -29.75%            | -42.66% |     0.11 |       81 | 51.58%     | ok               |
|          20 | -11.52%  | -29.75%            | -49.77% |     0.09 |       73 | 57.40%     | ok               |
|          25 | -15.57%  | -29.75%            | -47.93% |     0.03 |       73 | 54.91%     | ok               |
|          15 | -17.10%  | -29.75%            | -52.56% |     0.02 |       81 | 60.23%     | ok               |
|          35 | -21.40%  | -29.75%            | -48.24% |    -0.08 |       84 | 46.76%     | ok               |

## NVDA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -26.05%  | 56.36%             | -39.50% |    -0.26 |       76 | 51.52%     | ok               |
|          25 | -31.28%  | 56.36%             | -44.52% |    -0.39 |       81 | 47.59%     | ok               |
|          30 | -31.06%  | 56.36%             | -43.72% |    -0.41 |       82 | 44.74%     | ok               |
|          15 | -38.43%  | 56.36%             | -51.51% |    -0.49 |       82 | 55.79%     | ok               |
|          35 | -41.43%  | 56.36%             | -52.08% |    -0.68 |       92 | 41.89%     | ok               |

## OP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 23.24%   | -84.36%            | -30.63% |     0.49 |       34 | 9.58%      | ok               |
|          45 | 10.76%   | -84.36%            | -36.09% |     0.31 |       38 | 15.13%     | ok               |
|          40 | -13.67%  | -84.36%            | -47.76% |     0.02 |       50 | 23.56%     | ok               |
|          15 | -36.73%  | -84.36%            | -55.83% |    -0.16 |       75 | 45.21%     | ok               |
|          30 | -37.21%  | -84.36%            | -58.87% |    -0.25 |       72 | 34.29%     | ok               |

## ORCL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 146.17%  | -16.63%            | -32.54% |     1.06 |       65 | 60.07%     | ok               |
|          25 | 97.93%   | -16.63%            | -27.76% |     0.86 |       57 | 52.58%     | ok               |
|          45 | 84.00%   | -16.63%            | -32.35% |     0.85 |       54 | 38.10%     | ok               |
|          35 | 88.56%   | -16.63%            | -31.95% |     0.84 |       58 | 46.76%     | ok               |
|          20 | 92.41%   | -16.63%            | -29.32% |     0.83 |       66 | 55.74%     | ok               |

## OXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 2.79%    | -5.82%             | -28.48% |     0.17 |       65 | 43.09%     | ok               |
|          35 | 0.56%    | -5.82%             | -26.37% |     0.13 |       68 | 39.27%     | ok               |
|          40 | -3.65%   | -5.82%             | -28.30% |     0.05 |       58 | 36.11%     | ok               |
|          50 | -5.66%   | -5.82%             | -27.98% |    -0.01 |       48 | 29.45%     | ok               |
|          25 | -11.57%  | -5.82%             | -38.51% |    -0.07 |       77 | 46.59%     | ok               |

## PEP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 18.03%   | -12.88%            | -11.62% |     0.75 |       38 | 24.96%     | ok               |
|          45 | 6.20%    | -12.88%            | -14.22% |     0.3  |       54 | 28.79%     | ok               |
|          30 | 1.33%    | -12.88%            | -21.35% |     0.11 |       74 | 45.09%     | ok               |
|          35 | -0.25%   | -12.88%            | -21.42% |     0.06 |       77 | 39.43%     | ok               |
|          40 | -2.35%   | -12.88%            | -18.04% |    -0.03 |       70 | 34.44%     | ok               |

## PEPE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -37.95%  | -59.94%            | -62.24% |    -0.02 |       77 | 61.11%     | ok               |
|          20 | -40.97%  | -59.94%            | -61.07% |    -0.13 |       85 | 56.90%     | ok               |
|          30 | -42.60%  | -59.94%            | -57.70% |    -0.21 |       72 | 46.17%     | ok               |
|          25 | -52.94%  | -59.94%            | -62.02% |    -0.36 |       86 | 51.34%     | ok               |
|          35 | -47.79%  | -59.94%            | -58.37% |    -0.38 |       64 | 42.34%     | ok               |

## PFE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -10.80%  | 8.54%              | -23.37% |    -0.3  |       50 | 22.46%     | ok               |
|          40 | -12.46%  | 8.54%              | -27.08% |    -0.34 |       70 | 27.45%     | ok               |
|          50 | -11.30%  | 8.54%              | -25.42% |    -0.35 |       38 | 19.30%     | ok               |
|          35 | -20.89%  | 8.54%              | -32.87% |    -0.6  |       80 | 33.94%     | ok               |
|          30 | -31.28%  | 8.54%              | -41.77% |    -0.93 |       77 | 37.27%     | ok               |

## PG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -7.38%   | 0.19%              | -20.08% |    -0.23 |       52 | 29.28%     | ok               |
|          35 | -10.54%  | 0.19%              | -18.99% |    -0.35 |       60 | 32.78%     | ok               |
|          45 | -15.23%  | 0.19%              | -22.00% |    -0.58 |       52 | 26.96%     | ok               |
|          30 | -18.67%  | 0.19%              | -24.55% |    -0.65 |       62 | 35.94%     | ok               |
|          25 | -20.52%  | 0.19%              | -25.84% |    -0.72 |       74 | 37.44%     | ok               |

## PM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -5.14%   | 97.16%             | -34.56% |    -0.03 |       86 | 45.42%     | ok               |
|          20 | -7.62%   | 97.16%             | -36.03% |    -0.07 |       85 | 54.08%     | ok               |
|          30 | -8.12%   | 97.16%             | -37.61% |    -0.09 |       81 | 48.92%     | ok               |
|          50 | -10.12%  | 97.16%             | -36.94% |    -0.19 |       68 | 35.77%     | ok               |
|          40 | -12.38%  | 97.16%             | -39.92% |    -0.23 |       80 | 41.43%     | ok               |

## POL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 12.93%   | -56.88%            | -44.63% |     0.35 |       83 | 51.15%     | ok               |
|          25 | 5.35%    | -56.88%            | -44.63% |     0.28 |       73 | 55.94%     | ok               |
|          20 | -3.15%   | -56.88%            | -46.48% |     0.2  |       82 | 59.39%     | ok               |
|          40 | -4.64%   | -56.88%            | -35.22% |     0.13 |       60 | 32.57%     | ok               |
|          50 | -7.18%   | -56.88%            | -29.40% |     0.05 |       52 | 21.46%     | ok               |

## QCOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -25.98%  | -27.20%            | -54.50% |    -0.17 |       73 | 42.76%     | ok               |
|          20 | -31.42%  | -27.20%            | -54.38% |    -0.25 |       69 | 46.09%     | ok               |
|          35 | -32.23%  | -27.20%            | -50.58% |    -0.31 |       81 | 38.44%     | ok               |
|          15 | -39.71%  | -27.20%            | -57.94% |    -0.39 |       71 | 48.75%     | ok               |
|          30 | -40.14%  | -27.20%            | -56.59% |    -0.44 |       79 | 40.93%     | ok               |

## QQQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 11.12%   | 35.03%             | -14.17% |     0.34 |       69 | 52.75%     | ok               |
|          25 | 7.47%    | 35.03%             | -12.88% |     0.27 |       63 | 45.59%     | ok               |
|          20 | 6.18%    | 35.03%             | -12.98% |     0.23 |       75 | 48.75%     | ok               |
|          30 | 0.21%    | 35.03%             | -14.20% |     0.09 |       68 | 43.59%     | ok               |
|          35 | -10.08%  | 35.03%             | -20.59% |    -0.22 |       74 | 39.77%     | ok               |

## RENDER-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 28.18%   | -60.67%            | -43.43% |     0.5  |       91 | 59.00%     | ok               |
|          15 | 25.84%   | -60.67%            | -44.59% |     0.48 |       84 | 63.22%     | ok               |
|          25 | 13.99%   | -60.67%            | -43.13% |     0.4  |       89 | 54.21%     | ok               |
|          30 | -34.55%  | -60.67%            | -50.55% |    -0.11 |       92 | 48.47%     | ok               |
|          35 | -41.83%  | -60.67%            | -54.35% |    -0.28 |       84 | 42.53%     | ok               |

## RTX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 36.81%   | 84.09%             | -18.66% |     0.77 |       73 | 57.40%     | ok               |
|          25 | 32.13%   | 84.09%             | -18.59% |     0.7  |       61 | 54.74%     | ok               |
|          15 | 28.54%   | 84.09%             | -19.55% |     0.63 |       66 | 61.90%     | ok               |
|          30 | 22.88%   | 84.09%             | -16.99% |     0.55 |       68 | 51.75%     | ok               |
|          50 | 14.37%   | 84.09%             | -18.42% |     0.46 |       60 | 39.27%     | ok               |

## SBUX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 1.85%    | 33.28%             | -23.55% |     0.14 |       59 | 41.93%     | ok               |
|          40 | 0.75%    | 33.28%             | -25.43% |     0.11 |       62 | 33.44%     | ok               |
|          45 | -1.17%   | 33.28%             | -27.26% |     0.06 |       68 | 28.62%     | ok               |
|          35 | -3.71%   | 33.28%             | -26.54% |     0.02 |       62 | 36.77%     | ok               |
|          50 | -6.38%   | 33.28%             | -25.13% |    -0.09 |       54 | 24.13%     | ok               |

## SCHW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -2.12%   | 26.39%             | -29.24% |     0.04 |       73 | 52.75%     | ok               |
|          25 | -3.28%   | 26.39%             | -28.76% |     0.02 |       67 | 50.92%     | ok               |
|          45 | -3.45%   | 26.39%             | -16.53% |    -0.04 |       62 | 31.28%     | ok               |
|          15 | -6.17%   | 26.39%             | -31.37% |    -0.05 |       78 | 56.57%     | ok               |
|          50 | -3.90%   | 26.39%             | -13.28% |    -0.08 |       54 | 28.12%     | ok               |

## SHIB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -17.29%  | -65.07%            | -42.96% |    -0    |       85 | 66.67%     | ok               |
|          50 | -10.95%  | -65.07%            | -32.18% |    -0.03 |       50 | 22.99%     | ok               |
|          20 | -26.95%  | -65.07%            | -49.05% |    -0.15 |       80 | 62.07%     | ok               |
|          40 | -23.76%  | -65.07%            | -41.51% |    -0.19 |       58 | 38.31%     | ok               |
|          35 | -26.97%  | -65.07%            | -45.16% |    -0.21 |       75 | 46.55%     | ok               |

## SHY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          30 | -1.83%   | 0.07%              | -3.18% |    -0.6  |       54 | 38.27%     | ok               |
|          35 | -2.37%   | 0.07%              | -3.49% |    -0.8  |       56 | 36.11%     | ok               |
|          40 | -2.45%   | 0.07%              | -3.58% |    -0.83 |       56 | 34.78%     | ok               |
|          25 | -2.78%   | 0.07%              | -4.32% |    -0.89 |       64 | 41.10%     | ok               |
|          15 | -3.21%   | 0.07%              | -4.64% |    -0.97 |       67 | 46.92%     | ok               |

## SKY-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -61.00%  | -16.39%            | -65.72% |    -0.85 |       81 | 54.60%     | ok               |
|          35 | -58.07%  | -16.39%            | -60.94% |    -0.97 |       80 | 36.02%     | ok               |
|          30 | -60.93%  | -16.39%            | -63.60% |    -0.99 |       89 | 44.06%     | ok               |
|          25 | -65.35%  | -16.39%            | -66.89% |    -1.09 |       82 | 47.32%     | ok               |
|          45 | -60.25%  | -16.39%            | -61.83% |    -1.15 |       74 | 27.20%     | ok               |

## SLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -7.42%   | 15.44%             | -24.85% |    -0.06 |       60 | 31.11%     | ok               |
|          40 | -12.89%  | 15.44%             | -28.06% |    -0.17 |       52 | 33.94%     | ok               |
|          50 | -13.09%  | 15.44%             | -27.36% |    -0.24 |       50 | 24.96%     | ok               |
|          35 | -37.15%  | 15.44%             | -48.02% |    -0.76 |       78 | 41.93%     | ok               |
|          25 | -44.52%  | 15.44%             | -55.01% |    -0.89 |       87 | 52.25%     | ok               |

## SLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 69.43%   | 73.75%             | -28.72% |     0.88 |       52 | 31.28%     | ok               |
|          45 | 55.04%   | 73.75%             | -31.33% |     0.75 |       63 | 32.78%     | ok               |
|          40 | 53.82%   | 73.75%             | -34.28% |     0.74 |       67 | 34.78%     | ok               |
|          20 | 40.48%   | 73.75%             | -37.05% |     0.6  |       70 | 44.76%     | ok               |
|          35 | 36.08%   | 73.75%             | -37.86% |     0.57 |       74 | 37.77%     | ok               |

## SMH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 80.37%   | 67.13%             | -31.66% |     1.05 |       49 | 44.93%     | ok               |
|          25 | 64.06%   | 67.13%             | -33.57% |     0.92 |       46 | 43.43%     | ok               |
|          30 | 59.59%   | 67.13%             | -34.29% |     0.88 |       50 | 42.10%     | ok               |
|          35 | 47.72%   | 67.13%             | -34.65% |     0.77 |       56 | 40.10%     | ok               |
|          45 | 34.66%   | 67.13%             | -33.35% |     0.65 |       56 | 34.28%     | ok               |

## SNX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 25.21%   | -76.41%            | -41.29% |     0.47 |       54 | 29.89%     | ok               |
|          20 | 20.95%   | -76.41%            | -53.03% |     0.44 |       69 | 45.21%     | ok               |
|          40 | 15.69%   | -76.41%            | -33.19% |     0.37 |       46 | 25.10%     | ok               |
|          15 | 7.59%    | -76.41%            | -54.74% |     0.32 |       70 | 49.23%     | ok               |
|          30 | 7.33%    | -76.41%            | -50.74% |     0.3  |       60 | 36.02%     | ok               |

## SOL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 40.72%   | -42.48%            | -40.41% |     0.61 |       58 | 38.70%     | ok               |
|          35 | 15.73%   | -42.48%            | -44.32% |     0.38 |       72 | 44.83%     | ok               |
|          45 | 6.89%    | -42.48%            | -47.42% |     0.27 |       54 | 32.95%     | ok               |
|          15 | -3.56%   | -42.48%            | -46.84% |     0.2  |       73 | 62.45%     | ok               |
|          25 | -3.79%   | -42.48%            | -42.01% |     0.18 |       70 | 55.36%     | ok               |

## SOXX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 77.87%   | 57.00%             | -39.32% |     0.99 |       55 | 43.09%     | ok               |
|          35 | 73.86%   | 57.00%             | -38.76% |     0.98 |       58 | 38.60%     | ok               |
|          30 | 72.93%   | 57.00%             | -39.81% |     0.96 |       56 | 40.93%     | ok               |
|          20 | 62.16%   | 57.00%             | -39.19% |     0.84 |       61 | 44.09%     | ok               |
|          40 | 52.60%   | 57.00%             | -41.03% |     0.79 |       60 | 36.44%     | ok               |

## SPY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 4.74%    | 35.05%             | -14.25% |     0.22 |       59 | 51.08%     | ok               |
|          15 | 4.68%    | 35.05%             | -16.80% |     0.21 |       65 | 53.91%     | ok               |
|          25 | 0.03%    | 35.05%             | -14.25% |     0.07 |       59 | 50.08%     | ok               |
|          30 | -4.86%   | 35.05%             | -15.53% |    -0.11 |       62 | 47.59%     | ok               |
|          35 | -5.78%   | 35.05%             | -15.58% |    -0.15 |       60 | 44.43%     | ok               |

## SUSHI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -8.74%   | -74.09%            | -35.27% |     0.04 |       60 | 16.86%     | ok               |
|          45 | -36.69%  | -74.09%            | -58.32% |    -0.38 |       64 | 22.99%     | ok               |
|          35 | -44.93%  | -74.09%            | -68.95% |    -0.41 |       79 | 36.21%     | ok               |
|          40 | -42.39%  | -74.09%            | -62.35% |    -0.43 |       66 | 30.84%     | ok               |
|          15 | -63.63%  | -74.09%            | -78.43% |    -0.63 |       85 | 52.11%     | ok               |

## T Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 70.03%   | 23.70%             | -15.08% |     1.1  |       71 | 65.72%     | ok               |
|          20 | 65.83%   | 23.70%             | -18.13% |     1.08 |       66 | 61.23%     | ok               |
|          25 | 63.95%   | 23.70%             | -17.66% |     1.07 |       66 | 59.07%     | ok               |
|          30 | 53.12%   | 23.70%             | -17.01% |     0.95 |       68 | 57.07%     | ok               |
|          35 | 36.33%   | 23.70%             | -14.49% |     0.74 |       74 | 52.58%     | ok               |

## TGT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -8.89%   | 11.89%             | -32.83% |    -0.11 |       58 | 37.27%     | ok               |
|          25 | -13.16%  | 11.89%             | -34.51% |    -0.2  |       68 | 40.43%     | ok               |
|          20 | -14.66%  | 11.89%             | -36.78% |    -0.2  |       86 | 45.09%     | ok               |
|          45 | -12.30%  | 11.89%             | -26.12% |    -0.24 |       48 | 28.79%     | ok               |
|          35 | -15.41%  | 11.89%             | -30.71% |    -0.3  |       58 | 33.61%     | ok               |

## TIA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -25.31%  | -81.37%            | -66.82% |     0.13 |       95 | 58.81%     | ok               |
|          25 | -30.61%  | -81.37%            | -69.36% |     0.02 |       92 | 47.89%     | ok               |
|          35 | -24.80%  | -81.37%            | -66.58% |    -0.04 |       74 | 35.44%     | ok               |
|          20 | -41.91%  | -81.37%            | -71.87% |    -0.09 |       91 | 53.26%     | ok               |
|          30 | -43.82%  | -81.37%            | -75.93% |    -0.18 |       91 | 42.53%     | ok               |

## TLT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -9.44%   | -13.46%            | -12.71% |    -1.04 |       30 | 17.14%     | ok               |
|          40 | -14.39%  | -13.46%            | -17.65% |    -1.27 |       48 | 24.63%     | ok               |
|          45 | -12.99%  | -13.46%            | -15.22% |    -1.35 |       40 | 20.13%     | ok               |
|          30 | -19.74%  | -13.46%            | -21.85% |    -1.5  |       66 | 33.94%     | ok               |
|          35 | -19.18%  | -13.46%            | -21.33% |    -1.62 |       66 | 28.79%     | ok               |

## TMO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 50.73%   | 18.34%             | -8.17%  |     1.07 |       50 | 35.27%     | ok               |
|          45 | 43.82%   | 18.34%             | -9.69%  |     0.92 |       54 | 40.10%     | ok               |
|          35 | 41.67%   | 18.34%             | -13.84% |     0.81 |       65 | 50.42%     | ok               |
|          40 | 36.94%   | 18.34%             | -11.54% |     0.79 |       59 | 45.26%     | ok               |
|          20 | 36.28%   | 18.34%             | -22.89% |     0.68 |       74 | 60.90%     | ok               |

## TMUS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -5.13%   | -8.75%             | -41.04% |     0.01 |       68 | 60.23%     | ok               |
|          30 | -6.41%   | -8.75%             | -33.05% |    -0.04 |       74 | 47.42%     | ok               |
|          25 | -9.06%   | -8.75%             | -39.29% |    -0.09 |       75 | 50.42%     | ok               |
|          20 | -10.60%  | -8.75%             | -39.79% |    -0.11 |       74 | 54.58%     | ok               |
|          50 | -9.37%   | -8.75%             | -32.38% |    -0.19 |       60 | 32.95%     | ok               |

## TRX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 10.94%   | 17.62%             | -18.79% |     0.41 |       54 | 37.55%     | ok               |
|          35 | 4.93%    | 17.62%             | -21.77% |     0.22 |       64 | 44.83%     | ok               |
|          50 | 3.84%    | 17.62%             | -22.22% |     0.2  |       44 | 32.95%     | ok               |
|          30 | 3.83%    | 17.62%             | -22.90% |     0.19 |       64 | 47.32%     | ok               |
|          20 | 3.50%    | 17.62%             | -25.45% |     0.18 |       61 | 54.02%     | ok               |

## TSLA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 47.27%   | 93.07%             | -30.57% |     0.66 |       62 | 29.95%     | ok               |
|          40 | 18.38%   | 93.07%             | -50.11% |     0.38 |       61 | 35.44%     | ok               |
|          45 | -6.85%   | 93.07%             | -52.01% |     0.11 |       67 | 32.45%     | ok               |
|          35 | -14.63%  | 93.07%             | -58.86% |     0.04 |       72 | 38.10%     | ok               |
|          30 | -30.19%  | 93.07%             | -58.36% |    -0.15 |       74 | 42.76%     | ok               |

## TXN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -4.00%   | 43.45%             | -43.95% |     0.06 |       68 | 31.45%     | ok               |
|          35 | -18.91%  | 43.45%             | -42.08% |    -0.17 |       82 | 45.26%     | ok               |
|          20 | -24.68%  | 43.45%             | -37.19% |    -0.21 |       72 | 55.07%     | ok               |
|          15 | -26.06%  | 43.45%             | -38.02% |    -0.22 |       79 | 59.57%     | ok               |
|          40 | -23.87%  | 43.45%             | -44.52% |    -0.27 |       76 | 42.76%     | ok               |

## UNH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 41.00%   | -20.40%            | -26.31% |     0.63 |       73 | 49.25%     | ok               |
|          35 | 36.71%   | -20.40%            | -27.21% |     0.59 |       68 | 44.26%     | ok               |
|          50 | 32.73%   | -20.40%            | -36.82% |     0.57 |       54 | 30.12%     | ok               |
|          20 | 33.32%   | -20.40%            | -26.96% |     0.54 |       75 | 58.07%     | ok               |
|          25 | 32.15%   | -20.40%            | -24.25% |     0.54 |       73 | 54.08%     | ok               |

## UNI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 92.21%   | 3.97%              | -21.42% |     0.95 |       44 | 25.29%     | ok               |
|          45 | 74.77%   | 3.97%              | -30.17% |     0.81 |       50 | 32.38%     | ok               |
|          40 | 62.92%   | 3.97%              | -43.84% |     0.73 |       56 | 38.31%     | ok               |
|          35 | 47.53%   | 3.97%              | -48.64% |     0.62 |       62 | 43.68%     | ok               |
|          20 | -22.44%  | 3.97%              | -68.99% |     0.1  |       88 | 58.43%     | ok               |

## UPS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -29.81%  | -18.14%            | -36.93% |    -0.5  |       86 | 49.75%     | ok               |
|          35 | -29.46%  | -18.14%            | -32.91% |    -0.55 |       68 | 35.44%     | ok               |
|          15 | -32.29%  | -18.14%            | -39.16% |    -0.55 |       88 | 53.58%     | ok               |
|          40 | -29.33%  | -18.14%            | -33.49% |    -0.56 |       60 | 30.62%     | ok               |
|          25 | -31.71%  | -18.14%            | -38.19% |    -0.56 |       78 | 46.26%     | ok               |

## USO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 5.47%    | 94.81%             | -38.83% |     0.23 |       64 | 41.43%     | ok               |
|          45 | 4.80%    | 94.81%             | -33.44% |     0.21 |       48 | 27.12%     | ok               |
|          20 | 3.62%    | 94.81%             | -40.84% |     0.2  |       70 | 38.27%     | ok               |
|          25 | -6.08%   | 94.81%             | -43.22% |     0.06 |       66 | 35.94%     | ok               |
|          50 | -4.33%   | 94.81%             | -29.54% |     0.06 |       52 | 25.46%     | ok               |

## VEA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 3.75%    | 37.76%             | -15.99% |     0.19 |       56 | 50.25%     | ok               |
|          20 | -0.56%   | 37.76%             | -17.04% |     0.03 |       59 | 47.59%     | ok               |
|          25 | -4.35%   | 37.76%             | -17.13% |    -0.12 |       57 | 45.59%     | ok               |
|          30 | -5.22%   | 37.76%             | -17.27% |    -0.17 |       62 | 41.93%     | ok               |
|          35 | -5.68%   | 37.76%             | -16.11% |    -0.19 |       50 | 39.60%     | ok               |

## VIXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -54.55%  | -52.46%            | -69.78% |    -0.63 |       34 | 8.65%      | ok               |
|          45 | -64.29%  | -52.46%            | -75.03% |    -0.84 |       54 | 13.64%     | ok               |
|          40 | -71.97%  | -52.46%            | -80.72% |    -0.97 |       68 | 17.64%     | ok               |
|          35 | -75.41%  | -52.46%            | -84.03% |    -1    |       90 | 23.96%     | ok               |
|          30 | -80.56%  | -52.46%            | -89.28% |    -1.03 |       92 | 31.11%     | ok               |

## VNQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -6.88%   | 14.56%             | -22.34% |    -0.22 |       70 | 42.60%     | ok               |
|          45 | -6.99%   | 14.56%             | -19.07% |    -0.28 |       60 | 27.95%     | ok               |
|          50 | -7.91%   | 14.56%             | -17.13% |    -0.34 |       52 | 24.63%     | ok               |
|          30 | -10.63%  | 14.56%             | -24.92% |    -0.39 |       71 | 39.77%     | ok               |
|          20 | -11.63%  | 14.56%             | -24.00% |    -0.42 |       75 | 45.26%     | ok               |

## VTI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 6.25%    | 35.18%             | -13.96% |     0.26 |       62 | 51.58%     | ok               |
|          15 | 1.49%    | 35.18%             | -15.70% |     0.11 |       61 | 54.08%     | ok               |
|          25 | -4.29%   | 35.18%             | -15.00% |    -0.08 |       56 | 49.58%     | ok               |
|          40 | -8.53%   | 35.18%             | -19.77% |    -0.29 |       68 | 39.93%     | ok               |
|          35 | -10.54%  | 35.18%             | -20.22% |    -0.35 |       62 | 44.26%     | ok               |

## VWO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -3.86%   | 23.95%             | -21.68% |    -0.1  |       56 | 29.45%     | ok               |
|          15 | -6.37%   | 23.95%             | -24.01% |    -0.16 |       72 | 46.42%     | ok               |
|          20 | -6.39%   | 23.95%             | -26.14% |    -0.16 |       67 | 44.43%     | ok               |
|          45 | -5.73%   | 23.95%             | -23.75% |    -0.18 |       58 | 31.95%     | ok               |
|          40 | -6.22%   | 23.95%             | -23.57% |    -0.19 |       68 | 34.78%     | ok               |

## VZ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -2.64%   | 16.26%             | -12.55% |    -0.02 |       56 | 28.45%     | ok               |
|          20 | -23.40%  | 16.26%             | -35.02% |    -0.46 |       80 | 53.08%     | ok               |
|          25 | -20.27%  | 16.26%             | -26.32% |    -0.51 |       83 | 48.09%     | ok               |
|          45 | -18.61%  | 16.26%             | -26.23% |    -0.57 |       72 | 32.95%     | ok               |
|          35 | -20.48%  | 16.26%             | -26.97% |    -0.61 |       65 | 39.27%     | ok               |

## WFC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -10.77%  | 47.74%             | -22.54% |    -0.17 |       79 | 43.26%     | ok               |
|          50 | -8.46%   | 47.74%             | -18.29% |    -0.21 |       58 | 32.28%     | ok               |
|          20 | -23.30%  | 47.74%             | -29.87% |    -0.38 |       82 | 52.91%     | ok               |
|          45 | -15.46%  | 47.74%             | -24.02% |    -0.4  |       66 | 36.77%     | ok               |
|          30 | -22.09%  | 47.74%             | -29.78% |    -0.4  |       84 | 46.59%     | ok               |

## WIF-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 38.53%   | -83.07%            | -40.67% |     0.55 |       67 | 48.08%     | ok               |
|          25 | 18.16%   | -83.07%            | -44.74% |     0.42 |       63 | 44.06%     | ok               |
|          15 | 8.26%    | -83.07%            | -46.21% |     0.35 |       77 | 51.34%     | ok               |
|          30 | -7.02%   | -83.07%            | -48.32% |     0.2  |       64 | 41.38%     | ok               |
|          35 | -11.43%  | -83.07%            | -52.54% |     0.1  |       60 | 35.44%     | ok               |

## WMT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 42.12%   | 90.57%             | -12.87% |     1.19 |       38 | 36.61%     | ok               |
|          45 | 40.92%   | 90.57%             | -14.82% |     1.12 |       44 | 38.94%     | ok               |
|          35 | 30.64%   | 90.57%             | -18.90% |     0.84 |       60 | 45.26%     | ok               |
|          40 | 28.96%   | 90.57%             | -19.17% |     0.83 |       52 | 40.60%     | ok               |
|          15 | 11.47%   | 90.57%             | -26.82% |     0.34 |       84 | 59.23%     | ok               |

## XBI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 13.75%   | 61.74%             | -16.08% |     0.41 |       50 | 33.44%     | ok               |
|          45 | 9.43%    | 61.74%             | -15.46% |     0.32 |       48 | 30.95%     | ok               |
|          35 | 2.78%    | 61.74%             | -17.66% |     0.15 |       58 | 36.27%     | ok               |
|          30 | 0.63%    | 61.74%             | -17.66% |     0.1  |       60 | 37.77%     | ok               |
|          50 | 0.20%    | 61.74%             | -15.41% |     0.08 |       48 | 27.95%     | ok               |

## XLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 1.12%    | 17.62%             | -15.73% |     0.1  |       40 | 23.96%     | ok               |
|          40 | 0.80%    | 17.62%             | -17.29% |     0.09 |       54 | 28.29%     | ok               |
|          45 | -1.91%   | 17.62%             | -17.09% |    -0.02 |       42 | 25.79%     | ok               |
|          35 | -2.89%   | 17.62%             | -20.65% |    -0.05 |       54 | 31.45%     | ok               |
|          25 | -6.37%   | 17.62%             | -21.62% |    -0.17 |       62 | 37.44%     | ok               |

## XLC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 9.28%    | 24.02%             | -12.33% |     0.36 |       61 | 49.42%     | ok               |
|          25 | 8.74%    | 24.02%             | -12.31% |     0.34 |       60 | 51.58%     | ok               |
|          50 | 4.05%    | 24.02%             | -12.48% |     0.23 |       64 | 37.60%     | ok               |
|          40 | 4.61%    | 24.02%             | -13.38% |     0.22 |       62 | 43.09%     | ok               |
|          20 | 4.46%    | 24.02%             | -14.06% |     0.21 |       65 | 53.91%     | ok               |

## XLE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 1.25%    | 40.00%             | -28.77% |     0.12 |       69 | 47.25%     | ok               |
|          50 | -0.76%   | 40.00%             | -25.98% |     0.06 |       58 | 38.60%     | ok               |
|          45 | -2.15%   | 40.00%             | -28.46% |     0.02 |       60 | 40.93%     | ok               |
|          35 | -2.69%   | 40.00%             | -26.70% |     0.02 |       65 | 45.09%     | ok               |
|          25 | -3.52%   | 40.00%             | -32.07% |     0.01 |       79 | 50.42%     | ok               |

## XLF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 5.23%    | 41.45%             | -20.19% |     0.23 |       70 | 56.07%     | ok               |
|          20 | 4.58%    | 41.45%             | -18.63% |     0.21 |       70 | 53.41%     | ok               |
|          25 | -2.71%   | 41.45%             | -23.22% |    -0.03 |       77 | 50.25%     | ok               |
|          30 | -3.35%   | 41.45%             | -23.61% |    -0.05 |       78 | 48.25%     | ok               |
|          35 | -11.27%  | 41.45%             | -24.48% |    -0.38 |       70 | 44.76%     | ok               |

## XLI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 4.98%    | 34.11%             | -11.40% |     0.23 |       85 | 51.25%     | ok               |
|          20 | 0.03%    | 34.11%             | -12.74% |     0.06 |       77 | 46.59%     | ok               |
|          50 | -4.76%   | 34.11%             | -14.94% |    -0.18 |       60 | 31.78%     | ok               |
|          45 | -5.38%   | 34.11%             | -16.29% |    -0.19 |       70 | 34.28%     | ok               |
|          25 | -10.03%  | 34.11%             | -18.74% |    -0.34 |       80 | 44.59%     | ok               |

## XLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 50.66%   | 42.65%             | -14.75% |     0.98 |       42 | 45.09%     | ok               |
|          20 | 51.01%   | 42.65%             | -14.75% |     0.95 |       52 | 47.42%     | ok               |
|          15 | 53.29%   | 42.65%             | -17.54% |     0.94 |       53 | 50.08%     | ok               |
|          30 | 41.64%   | 42.65%             | -14.75% |     0.87 |       42 | 43.76%     | ok               |
|          35 | 27.33%   | 42.65%             | -14.71% |     0.65 |       56 | 41.10%     | ok               |

## XLM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 14.00%   | -43.77%            | -49.14% |     0.36 |       73 | 51.15%     | ok               |
|          30 | 7.96%    | -43.77%            | -54.58% |     0.3  |       71 | 48.47%     | ok               |
|          40 | 8.62%    | -43.77%            | -49.47% |     0.3  |       52 | 36.40%     | ok               |
|          50 | 7.86%    | -43.77%            | -48.14% |     0.28 |       40 | 24.90%     | ok               |
|          15 | -0.06%   | -43.77%            | -61.51% |     0.24 |       76 | 60.15%     | ok               |

## XLP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          45 | 20.22%   | 18.58%             | -5.66% |     1.02 |       48 | 31.28%     | ok               |
|          40 | 19.21%   | 18.58%             | -7.32% |     0.95 |       66 | 34.94%     | ok               |
|          50 | 17.39%   | 18.58%             | -6.08% |     0.91 |       54 | 29.45%     | ok               |
|          35 | 18.17%   | 18.58%             | -8.39% |     0.89 |       62 | 37.94%     | ok               |
|          30 | 14.75%   | 18.58%             | -8.96% |     0.73 |       63 | 39.77%     | ok               |

## XLU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 5.80%    | 23.82%             | -14.03% |     0.33 |       54 | 29.45%     | ok               |
|          45 | 4.64%    | 23.82%             | -14.97% |     0.27 |       58 | 30.62%     | ok               |
|          35 | 3.32%    | 23.82%             | -19.71% |     0.2  |       64 | 36.27%     | ok               |
|          40 | 0.56%    | 23.82%             | -16.41% |     0.07 |       68 | 33.11%     | ok               |
|          30 | -1.15%   | 23.82%             | -20.40% |    -0    |       69 | 39.77%     | ok               |

## XLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -18.98%  | 26.75%             | -22.46% |    -0.84 |       74 | 38.10%     | ok               |
|          30 | -19.35%  | 26.75%             | -22.82% |    -0.87 |       74 | 36.44%     | ok               |
|          15 | -21.72%  | 26.75%             | -24.77% |    -0.95 |       81 | 42.10%     | ok               |
|          20 | -21.55%  | 26.75%             | -24.61% |    -0.96 |       77 | 39.60%     | ok               |
|          35 | -23.37%  | 26.75%             | -26.64% |    -1.13 |       68 | 33.44%     | ok               |

## XLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 0.42%    | 31.94%             | -16.52% |     0.09 |       78 | 54.41%     | ok               |
|          30 | -3.08%   | 31.94%             | -18.44% |    -0.02 |       77 | 47.75%     | ok               |
|          20 | -4.90%   | 31.94%             | -20.14% |    -0.06 |       74 | 51.08%     | ok               |
|          25 | -7.02%   | 31.94%             | -21.01% |    -0.13 |       71 | 49.58%     | ok               |
|          50 | -6.20%   | 31.94%             | -17.00% |    -0.19 |       66 | 32.45%     | ok               |

## XOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 3.48%    | 51.50%             | -21.35% |     0.17 |       40 | 29.28%     | ok               |
|          25 | 3.49%    | 51.50%             | -19.90% |     0.17 |       55 | 36.94%     | ok               |
|          30 | 2.46%    | 51.50%             | -20.29% |     0.14 |       55 | 36.27%     | ok               |
|          45 | -1.68%   | 51.50%             | -23.33% |     0.03 |       44 | 30.45%     | ok               |
|          40 | -3.14%   | 51.50%             | -21.45% |    -0.01 |       54 | 33.78%     | ok               |

## XRP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 7.07%    | -46.97%            | -33.31% |     0.28 |       84 | 43.49%     | ok               |
|          40 | -4.99%   | -46.97%            | -33.91% |     0.12 |       74 | 35.44%     | ok               |
|          20 | -13.82%  | -46.97%            | -36.83% |     0.04 |       79 | 56.51%     | ok               |
|          30 | -13.79%  | -46.97%            | -33.97% |     0.03 |       75 | 49.43%     | ok               |
|          45 | -11.73%  | -46.97%            | -36.27% |     0.02 |       66 | 29.31%     | ok               |

## YFI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -44.04%  | -62.80%            | -45.42% |    -0.71 |       60 | 28.35%     | ok               |
|          35 | -48.17%  | -62.80%            | -53.44% |    -0.74 |       62 | 36.40%     | ok               |
|          30 | -52.78%  | -62.80%            | -58.78% |    -0.83 |       74 | 40.23%     | ok               |
|          25 | -55.51%  | -62.80%            | -61.18% |    -0.87 |       73 | 44.64%     | ok               |
|          15 | -63.72%  | -62.80%            | -68.34% |    -1.03 |       81 | 52.11%     | ok               |

## ZEC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 194.55%  | 2222.97%           | -30.64% |     1.06 |       46 | 29.50%     | ok               |
|          50 | 125.09%  | 2222.97%           | -41.34% |     0.88 |       46 | 26.63%     | ok               |
|          35 | 128.83%  | 2222.97%           | -50.84% |     0.88 |       54 | 34.48%     | ok               |
|          40 | 121.03%  | 2222.97%           | -54.22% |     0.85 |       54 | 32.76%     | ok               |
|          30 | 97.69%   | 2222.97%           | -56.50% |     0.77 |       56 | 37.36%     | ok               |
