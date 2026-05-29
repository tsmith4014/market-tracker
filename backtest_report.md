# Market Tracker Backtest Report

_Generated: 2026-05-29T15:09:44+00:00_

## Data Sources

- Crypto: Kraken -> Coinbase -> CoinGecko OHLC -> CoinPaprika fallback chain.
- Stocks / ETFs / indices: Stooq -> Yahoo Finance fallback chain.
- Data rows are generated from real market APIs. Mock OHLCV rows are not generated.

## Data Freshness

- Rows: **92,330**
- Symbols: **161**
- Date range: **2024-01-05** to **2026-05-29**

## Latest Signals

| symbol     | date                |         close |   composite_score | signal   | data_source   |
|:-----------|:--------------------|--------------:|------------------:|:---------|:--------------|
| AAPL       | 2026-05-29 00:00:00 |   312.12      |         60.3333   | LONG     | Yahoo Finance |
| ABBV       | 2026-05-29 00:00:00 |   217.435     |         61.75     | LONG     | Yahoo Finance |
| AMD        | 2026-05-29 00:00:00 |   515.365     |         61.6667   | LONG     | Yahoo Finance |
| BAC        | 2026-05-29 00:00:00 |    51.46      |         46.4167   | LONG     | Yahoo Finance |
| CL         | 2026-05-29 00:00:00 |    90.9       |         72.6667   | LONG     | Yahoo Finance |
| CSCO       | 2026-05-29 00:00:00 |   119.52      |         69.8333   | LONG     | Yahoo Finance |
| FCX        | 2026-05-29 00:00:00 |    65.8201    |         75.1667   | LONG     | Yahoo Finance |
| HON        | 2026-05-29 00:00:00 |   236.725     |         74        | LONG     | Yahoo Finance |
| HYG        | 2026-05-29 00:00:00 |    80.3128    |         69.5833   | LONG     | Yahoo Finance |
| IBM        | 2026-05-29 00:00:00 |   289.055     |         60.25     | LONG     | Yahoo Finance |
| INJ-USD    | 2026-05-29 00:00:00 |     6.35      |         61.5833   | LONG     | Kraken API    |
| INTC       | 2026-05-29 00:00:00 |   119.54      |         39.6667   | LONG     | Yahoo Finance |
| ITA        | 2026-05-29 00:00:00 |   234.06      |         63.4167   | LONG     | Yahoo Finance |
| KO         | 2026-05-29 00:00:00 |    79.65      |         30.3333   | LONG     | Yahoo Finance |
| LLY        | 2026-05-29 00:00:00 |  1098.51      |         71.5      | LONG     | Yahoo Finance |
| MRK        | 2026-05-29 00:00:00 |   118.77      |         68.1667   | LONG     | Yahoo Finance |
| MU         | 2026-05-29 00:00:00 |   966.48      |         66.6667   | LONG     | Yahoo Finance |
| NOW        | 2026-05-29 00:00:00 |   121.756     |         31.25     | LONG     | Yahoo Finance |
| NVDA       | 2026-05-29 00:00:00 |   215.22      |         30.8333   | LONG     | Yahoo Finance |
| ORCL       | 2026-05-29 00:00:00 |   219.26      |         56.5833   | LONG     | Yahoo Finance |
| QCOM       | 2026-05-29 00:00:00 |   250.34      |         61.6667   | LONG     | Yahoo Finance |
| QQQ        | 2026-05-29 00:00:00 |   737.362     |         36.3333   | LONG     | Yahoo Finance |
| SMH        | 2026-05-29 00:00:00 |   600.795     |         65.6667   | LONG     | Yahoo Finance |
| SOXX       | 2026-05-29 00:00:00 |   569.245     |         65.6667   | LONG     | Yahoo Finance |
| SPY        | 2026-05-29 00:00:00 |   756.14      |         36.3333   | LONG     | Yahoo Finance |
| TGT        | 2026-05-29 00:00:00 |   126.29      |         69.8333   | LONG     | Yahoo Finance |
| TSLA       | 2026-05-29 00:00:00 |   431.19      |         48.9167   | LONG     | Yahoo Finance |
| TXN        | 2026-05-29 00:00:00 |   311.41      |         49.8333   | LONG     | Yahoo Finance |
| UNH        | 2026-05-29 00:00:00 |   380.125     |         46.8333   | LONG     | Yahoo Finance |
| UPS        | 2026-05-29 00:00:00 |   105.69      |         80.5833   | LONG     | Yahoo Finance |
| VTI        | 2026-05-29 00:00:00 |   372.18      |         51.3333   | LONG     | Yahoo Finance |
| XLK        | 2026-05-29 00:00:00 |   190.28      |         62.8333   | LONG     | Yahoo Finance |
| XLM-USD    | 2026-05-29 00:00:00 |     0.206814  |         74.75     | LONG     | Kraken API    |
| ADBE       | 2026-05-29 00:00:00 |   251.18      |        -15.0833   | NEUTRAL  | Yahoo Finance |
| AGG        | 2026-05-29 00:00:00 |    99.1151    |         23.25     | NEUTRAL  | Yahoo Finance |
| ALGO-USD   | 2026-05-29 00:00:00 |     0.11272   |        -24.6667   | NEUTRAL  | Kraken API    |
| AMAT       | 2026-05-29 00:00:00 |   450.76      |         58.9167   | NEUTRAL  | Yahoo Finance |
| AMGN       | 2026-05-29 00:00:00 |   335.37      |         18.5      | NEUTRAL  | Yahoo Finance |
| AMZN       | 2026-05-29 00:00:00 |   271.171     |         26.5833   | NEUTRAL  | Yahoo Finance |
| ARKK       | 2026-05-29 00:00:00 |    81.17      |         46.8333   | NEUTRAL  | Yahoo Finance |
| ATOM-USD   | 2026-05-29 00:00:00 |     1.9958    |          8.08333  | NEUTRAL  | Kraken API    |
| AVGO       | 2026-05-29 00:00:00 |   437.387     |         27        | NEUTRAL  | Yahoo Finance |
| BA         | 2026-05-29 00:00:00 |   229.92      |          8.91667  | NEUTRAL  | Yahoo Finance |
| BITO       | 2026-05-29 00:00:00 |     9.99      |        -67.5833   | NEUTRAL  | Yahoo Finance |
| BLK        | 2026-05-29 00:00:00 |  1056.96      |         -8.83333  | NEUTRAL  | Yahoo Finance |
| BND        | 2026-05-29 00:00:00 |    73.495     |         23.25     | NEUTRAL  | Yahoo Finance |
| C          | 2026-05-29 00:00:00 |   125.84      |         10.25     | NEUTRAL  | Yahoo Finance |
| CAT        | 2026-05-29 00:00:00 |   879.745     |         21.4167   | NEUTRAL  | Yahoo Finance |
| CMCSA      | 2026-05-29 00:00:00 |    24.8899    |        -17.5      | NEUTRAL  | Yahoo Finance |
| COMP-USD   | 2026-05-29 00:00:00 |    17.51      |        -64.5833   | NEUTRAL  | Kraken API    |
| COP        | 2026-05-29 00:00:00 |   113.86      |        -20.3333   | NEUTRAL  | Yahoo Finance |
| COST       | 2026-05-29 00:00:00 |   950.125     |        -43.25     | NEUTRAL  | Yahoo Finance |
| CRM        | 2026-05-29 00:00:00 |   189.31      |         20.6667   | NEUTRAL  | Yahoo Finance |
| CVX        | 2026-05-29 00:00:00 |   181.655     |         -7.83333  | NEUTRAL  | Yahoo Finance |
| DASH-USD   | 2026-05-29 00:00:00 |    39.533     |        -72.5833   | NEUTRAL  | Kraken API    |
| DBC        | 2026-05-29 00:00:00 |    29.43      |        -21.5833   | NEUTRAL  | Yahoo Finance |
| DE         | 2026-05-29 00:00:00 |   542.69      |        -11.5833   | NEUTRAL  | Yahoo Finance |
| DIA        | 2026-05-29 00:00:00 |   510.57      |         55        | NEUTRAL  | Yahoo Finance |
| DIS        | 2026-05-29 00:00:00 |   103.19      |        -55.8333   | NEUTRAL  | Yahoo Finance |
| DOT-USD    | 2026-05-29 00:00:00 |     1.1945    |        -50.25     | NEUTRAL  | Kraken API    |
| DXY-INDEX  | 2026-05-29 00:00:00 |    98.875     |         48.1183   | NEUTRAL  | Yahoo Finance |
| EEM        | 2026-05-29 00:00:00 |    68.825     |         46.9167   | NEUTRAL  | Yahoo Finance |
| EFA        | 2026-05-29 00:00:00 |   105.31      |         54.9167   | NEUTRAL  | Yahoo Finance |
| EOG        | 2026-05-29 00:00:00 |   133.355     |         -4.91667  | NEUTRAL  | Yahoo Finance |
| ETC-USD    | 2026-05-29 00:00:00 |     8.132     |        -49.8333   | NEUTRAL  | Kraken API    |
| EWJ        | 2026-05-29 00:00:00 |    93.06      |         30.9167   | NEUTRAL  | Yahoo Finance |
| FET-USD    | 2026-05-29 00:00:00 |     0.2358    |         31.8333   | NEUTRAL  | Kraken API    |
| FIL-USD    | 2026-05-29 00:00:00 |     0.946     |        -39.3333   | NEUTRAL  | Kraken API    |
| FXI        | 2026-05-29 00:00:00 |    35.2363    |        -61.75     | NEUTRAL  | Yahoo Finance |
| GDX        | 2026-05-29 00:00:00 |    88.96      |        -33.5      | NEUTRAL  | Yahoo Finance |
| GDXJ       | 2026-05-29 00:00:00 |   118.06      |        -15        | NEUTRAL  | Yahoo Finance |
| GE         | 2026-05-29 00:00:00 |   321.015     |         55.8333   | NEUTRAL  | Yahoo Finance |
| GLD        | 2026-05-29 00:00:00 |   419.67      |        -29.3333   | NEUTRAL  | Yahoo Finance |
| GOOGL      | 2026-05-29 00:00:00 |   382.5       |         14.1667   | NEUTRAL  | Yahoo Finance |
| GRT-USD    | 2026-05-29 00:00:00 |     0.02549   |        -33.1667   | NEUTRAL  | Kraken API    |
| GS         | 2026-05-29 00:00:00 |  1020.21      |         49.25     | NEUTRAL  | Yahoo Finance |
| HBAR-USD   | 2026-05-29 00:00:00 |     0.08969   |        -13.8333   | NEUTRAL  | Kraken API    |
| HD         | 2026-05-29 00:00:00 |   320.93      |          4.16667  | NEUTRAL  | Yahoo Finance |
| IBIT       | 2026-05-29 00:00:00 |    41.495     |        -67.5833   | NEUTRAL  | Yahoo Finance |
| ICP-USD    | 2026-05-29 00:00:00 |     2.679     |         -5.5      | NEUTRAL  | Kraken API    |
| IEF        | 2026-05-29 00:00:00 |    94.65      |         -3.5      | NEUTRAL  | Yahoo Finance |
| IEMG       | 2026-05-29 00:00:00 |    83.69      |         46.9167   | NEUTRAL  | Yahoo Finance |
| INTU       | 2026-05-29 00:00:00 |   325.385     |        -70.5833   | NEUTRAL  | Yahoo Finance |
| IWM        | 2026-05-29 00:00:00 |   289.2       |         56.0833   | NEUTRAL  | Yahoo Finance |
| JNJ        | 2026-05-29 00:00:00 |   227.895     |         16.25     | NEUTRAL  | Yahoo Finance |
| LIN        | 2026-05-29 00:00:00 |   500.51      |         24.5833   | NEUTRAL  | Yahoo Finance |
| LRCX       | 2026-05-29 00:00:00 |   320.87      |         58.5833   | NEUTRAL  | Yahoo Finance |
| MCD        | 2026-05-29 00:00:00 |   279.22      |        -28.0833   | NEUTRAL  | Yahoo Finance |
| META       | 2026-05-29 00:00:00 |   625.08      |         12.9167   | NEUTRAL  | Yahoo Finance |
| MPC        | 2026-05-29 00:00:00 |   249.85      |         28.25     | NEUTRAL  | Yahoo Finance |
| MS         | 2026-05-29 00:00:00 |   206.84      |         49.25     | NEUTRAL  | Yahoo Finance |
| MSFT       | 2026-05-29 00:00:00 |   443.275     |         58.0833   | NEUTRAL  | Yahoo Finance |
| NEAR-USD   | 2026-05-29 00:00:00 |     2.453     |         65.5833   | NEUTRAL  | Kraken API    |
| NEM        | 2026-05-29 00:00:00 |   110.081     |        -33        | NEUTRAL  | Yahoo Finance |
| NFLX       | 2026-05-29 00:00:00 |    85.725     |        -40.4167   | NEUTRAL  | Yahoo Finance |
| NKE        | 2026-05-29 00:00:00 |    46.57      |         16.3333   | NEUTRAL  | Yahoo Finance |
| OXY        | 2026-05-29 00:00:00 |    56.525     |         -0.916667 | NEUTRAL  | Yahoo Finance |
| PFE        | 2026-05-29 00:00:00 |    26.02      |         -4.83333  | NEUTRAL  | Yahoo Finance |
| PG         | 2026-05-29 00:00:00 |   144.361     |        -13.5      | NEUTRAL  | Yahoo Finance |
| PM         | 2026-05-29 00:00:00 |   176.485     |         28.3333   | NEUTRAL  | Yahoo Finance |
| RENDER-USD | 2026-05-29 00:00:00 |     1.985     |         30.0833   | NEUTRAL  | Kraken API    |
| RTX        | 2026-05-29 00:00:00 |   178.39      |         18.5      | NEUTRAL  | Yahoo Finance |
| SBUX       | 2026-05-29 00:00:00 |    99.56      |         -7.16667  | NEUTRAL  | Yahoo Finance |
| SCHW       | 2026-05-29 00:00:00 |    86.8       |        -63.25     | NEUTRAL  | Yahoo Finance |
| SHY        | 2026-05-29 00:00:00 |    82.3099    |         18.4167   | NEUTRAL  | Yahoo Finance |
| SKY-USD    | 2026-05-29 00:00:00 |     0.06542   |        -27.9167   | NEUTRAL  | Kraken API    |
| SLB        | 2026-05-29 00:00:00 |    55.06      |         24.25     | NEUTRAL  | Yahoo Finance |
| SLV        | 2026-05-29 00:00:00 |    68.6299    |        -15.5      | NEUTRAL  | Yahoo Finance |
| TIA-USD    | 2026-05-29 00:00:00 |     0.4109    |        -26.1667   | NEUTRAL  | Kraken API    |
| TLT        | 2026-05-29 00:00:00 |    85.792     |         -7.5      | NEUTRAL  | Yahoo Finance |
| TMO        | 2026-05-29 00:00:00 |   489.5       |         20.6667   | NEUTRAL  | Yahoo Finance |
| TMUS       | 2026-05-29 00:00:00 |   186.66      |        -57.9167   | NEUTRAL  | Yahoo Finance |
| TRX-USD    | 2026-05-29 00:00:00 |     0.346091  |         16.4167   | NEUTRAL  | Kraken API    |
| USO        | 2026-05-29 00:00:00 |   128.48      |        -23.5833   | NEUTRAL  | Yahoo Finance |
| VEA        | 2026-05-29 00:00:00 |    72.04      |         61.4167   | NEUTRAL  | Yahoo Finance |
| VNQ        | 2026-05-29 00:00:00 |    95.85      |          6.91667  | NEUTRAL  | Yahoo Finance |
| VWO        | 2026-05-29 00:00:00 |    60.07      |         10.9167   | NEUTRAL  | Yahoo Finance |
| VZ         | 2026-05-29 00:00:00 |    47.905     |         61.4167   | NEUTRAL  | Yahoo Finance |
| WFC        | 2026-05-29 00:00:00 |    77.355     |         -4.83333  | NEUTRAL  | Yahoo Finance |
| XBI        | 2026-05-29 00:00:00 |   135.81      |         59.4167   | NEUTRAL  | Yahoo Finance |
| XLB        | 2026-05-29 00:00:00 |    51.51      |         40.5833   | NEUTRAL  | Yahoo Finance |
| XLC        | 2026-05-29 00:00:00 |   115.75      |        -16.5833   | NEUTRAL  | Yahoo Finance |
| XLE        | 2026-05-29 00:00:00 |    56.29      |        -14.9167   | NEUTRAL  | Yahoo Finance |
| XLF        | 2026-05-29 00:00:00 |    51.635     |         12.5      | NEUTRAL  | Yahoo Finance |
| XLI        | 2026-05-29 00:00:00 |   173.205     |         40.5833   | NEUTRAL  | Yahoo Finance |
| XLP        | 2026-05-29 00:00:00 |    83.115     |         -7.33333  | NEUTRAL  | Yahoo Finance |
| XLU        | 2026-05-29 00:00:00 |    44.38      |        -13.4167   | NEUTRAL  | Yahoo Finance |
| XLV        | 2026-05-29 00:00:00 |   149.72      |         55.8333   | NEUTRAL  | Yahoo Finance |
| XLY        | 2026-05-29 00:00:00 |   121.265     |         41.4167   | NEUTRAL  | Yahoo Finance |
| XOM        | 2026-05-29 00:00:00 |   146.09      |         -7.33333  | NEUTRAL  | Yahoo Finance |
| ZEC-USD    | 2026-05-29 00:00:00 |   528.65      |        -12.5      | NEUTRAL  | Kraken API    |
| AAVE-USD   | 2026-05-29 00:00:00 |    81.07      |        -47.5833   | SHORT    | Kraken API    |
| ADA-USD    | 2026-05-29 00:00:00 |     0.232115  |        -40.3333   | SHORT    | Kraken API    |
| APT-USD    | 2026-05-29 00:00:00 |     0.9075    |        -39.8333   | SHORT    | Kraken API    |
| ARB-USD    | 2026-05-29 00:00:00 |     0.102     |        -51.6667   | SHORT    | Kraken API    |
| AVAX-USD   | 2026-05-29 00:00:00 |     8.72      |        -46.5      | SHORT    | Kraken API    |
| BCH-USD    | 2026-05-29 00:00:00 |   299.99      |        -65.0833   | SHORT    | Kraken API    |
| BONK-USD   | 2026-05-29 00:00:00 |     5.396e-06 |        -51.5833   | SHORT    | Kraken API    |
| BTC-USD    | 2026-05-29 00:00:00 | 72743.4       |        -47.5833   | SHORT    | Kraken API    |
| CRV-USD    | 2026-05-29 00:00:00 |     0.2102    |        -44.3333   | SHORT    | Kraken API    |
| DOGE-USD   | 2026-05-29 00:00:00 |     0.0985913 |        -40.3333   | SHORT    | Kraken API    |
| ETH-USD    | 2026-05-29 00:00:00 |  1991.14      |        -58.9167   | SHORT    | Kraken API    |
| JPM        | 2026-05-29 00:00:00 |   296.82      |        -48        | SHORT    | Yahoo Finance |
| LDO-USD    | 2026-05-29 00:00:00 |     0.318     |        -51.6667   | SHORT    | Kraken API    |
| LINK-USD   | 2026-05-29 00:00:00 |     8.87727   |        -49.3333   | SHORT    | Kraken API    |
| LTC-USD    | 2026-05-29 00:00:00 |    51.59      |        -47.3333   | SHORT    | Kraken API    |
| OP-USD     | 2026-05-29 00:00:00 |     0.1167    |        -37.5833   | SHORT    | Kraken API    |
| PEP        | 2026-05-29 00:00:00 |   144.13      |        -46.5      | SHORT    | Yahoo Finance |
| PEPE-USD   | 2026-05-29 00:00:00 |     3.353e-06 |        -53.3333   | SHORT    | Kraken API    |
| POL-USD    | 2026-05-29 00:00:00 |     0.08768   |        -33.6667   | SHORT    | Kraken API    |
| SHIB-USD   | 2026-05-29 00:00:00 |     5.34e-06  |        -53.3333   | SHORT    | Kraken API    |
| SNX-USD    | 2026-05-29 00:00:00 |     0.3028    |        -37.3333   | SHORT    | Kraken API    |
| SOL-USD    | 2026-05-29 00:00:00 |    80.79      |        -40.3333   | SHORT    | Kraken API    |
| SUSHI-USD  | 2026-05-29 00:00:00 |     0.1901    |        -44.5833   | SHORT    | Kraken API    |
| T          | 2026-05-29 00:00:00 |    24.765     |        -35        | SHORT    | Yahoo Finance |
| UNI-USD    | 2026-05-29 00:00:00 |     2.981     |        -42.5833   | SHORT    | Kraken API    |
| VIXY       | 2026-05-29 00:00:00 |    23.435     |        -49.3333   | SHORT    | Yahoo Finance |
| WIF-USD    | 2026-05-29 00:00:00 |     0.1838    |        -44.5833   | SHORT    | Kraken API    |
| WMT        | 2026-05-29 00:00:00 |   115.09      |        -44.3333   | SHORT    | Yahoo Finance |
| XRP-USD    | 2026-05-29 00:00:00 |     1.30403   |        -47.5833   | SHORT    | Kraken API    |
| YFI-USD    | 2026-05-29 00:00:00 |  2230         |        -49.5833   | SHORT    | Kraken API    |

## Edge Summary

- Symbols with trades: **160** of 160
- Beat buy-and-hold: **33.75%** of traded symbols
- Positive return: **35.00%** of traded symbols
- Median strategy return: **-9.07%** (benchmark **17.29%**)
- Median excess vs benchmark: **-31.65%**
- Median Sharpe: **-0.09**
- Median exposure: **44.54%**

> Edge is real only if both _beat buy-and-hold_ and _median excess_ are convincingly positive across many symbols. Treat a single high-return symbol as noise.

## Portfolio Backtest

Actual capital-allocation books (not per-symbol averages). Benchmarks: `equal_weight_buyhold` (whole tracked universe), `spy_buyhold` (100% SPY), and `sixty_forty` (60% SPY / 40% AGG). `high_conf_voltarget` inverse-vol-weights the HIGH-confidence book; `conviction_long_short` is market-neutral. Judge on **Sharpe** and **max_drawdown** out-of-sample, not raw return: a fully-invested long book wins on return in a bull market but carries all the risk.

| strategy              | scope         | ann_return   | ann_vol   |   sharpe | max_drawdown   | total_return   |   avg_gross_exposure |
|:----------------------|:--------------|:-------------|:----------|---------:|:---------------|:---------------|---------------------:|
| equal_weight_buyhold  | full          | -12.50%      | 34.09%    |    -0.37 | -60.43%        | -42.84%        |                 1    |
| equal_weight_buyhold  | out_of_sample | -12.37%      | 34.47%    |    -0.36 | -39.63%        | -17.75%        |                 1    |
| all_signals_ew        | full          | -6.43%       | 28.33%    |    -0.23 | -60.64%        | -27.30%        |                 1    |
| all_signals_ew        | out_of_sample | 2.83%        | 28.59%    |     0.1  | -33.68%        | -1.31%         |                 1    |
| high_conf_ew          | full          | -0.85%       | 32.68%    |    -0.03 | -50.57%        | -17.03%        |                 0.89 |
| high_conf_ew          | out_of_sample | 25.94%       | 37.39%    |     0.69 | -20.90%        | 22.62%         |                 0.89 |
| high_conf_voltarget   | full          | -0.88%       | 30.12%    |    -0.03 | -43.58%        | -15.01%        |                 0.89 |
| high_conf_voltarget   | out_of_sample | 17.88%       | 35.69%    |     0.5  | -17.06%        | 13.28%         |                 0.89 |
| conviction_long_short | full          | -10.23%      | 23.27%    |    -0.44 | -39.91%        | -32.59%        |                 0.97 |
| conviction_long_short | out_of_sample | -5.77%       | 26.92%    |    -0.21 | -20.85%        | -9.56%         |                 0.97 |
| spy_buyhold           | full          | 10.70%       | 13.24%    |     0.81 | -17.81%        | 34.82%         |                 0.79 |
| spy_buyhold           | out_of_sample | 2.11%        | 9.36%     |     0.22 | -14.83%        | 1.80%          |                 0.79 |
| sixty_forty           | full          | 6.16%        | 8.39%     |     0.73 | -10.80%        | 19.32%         |                 0.79 |
| sixty_forty           | out_of_sample | 0.40%        | 6.06%     |     0.07 | -10.09%        | 0.23%          |                 0.79 |

## Walk-Forward Robustness

Each book measured across contiguous time folds (each a different regime). A book has durable edge only if `mean_sharpe` is positive, `min_sharpe` isn't deeply negative, and `pct_positive_folds` is high — a single great fold doesn't count. `fold_sharpes` lists each fold oldest-to-newest.

| strategy              |   n_folds |   mean_sharpe |   median_sharpe |   min_sharpe | pct_positive_folds   | mean_return   | fold_sharpes                 |
|:----------------------|----------:|--------------:|----------------:|-------------:|:---------------------|:--------------|:-----------------------------|
| equal_weight_buyhold  |         5 |         -0.15 |           -0.17 |        -1.93 | 40.00%               | -8.87%        | 1.84;-1.93;0.43;-0.91;-0.17  |
| all_signals_ew        |         5 |          0.12 |            0.91 |        -2.51 | 60.00%               | -2.57%        | 0.91;1.31;-0.75;-2.51;1.64   |
| high_conf_ew          |         5 |          0.31 |           -0.45 |        -1.1  | 40.00%               | -1.12%        | 1.76;-0.45;-0.48;-1.10;1.84  |
| high_conf_voltarget   |         5 |          0.39 |           -0.19 |        -0.95 | 40.00%               | -1.64%        | 2.46;-0.59;-0.19;-0.95;1.24  |
| conviction_long_short |         5 |         -0.42 |           -0.34 |        -1.08 | 20.00%               | -7.34%        | -0.43;-0.34;-0.33;-1.08;0.07 |
| spy_buyhold           |         5 |          0.87 |            0.69 |        -0.28 | 80.00%               | 6.39%         | 2.21;1.55;0.17;-0.28;0.69    |
| sixty_forty           |         5 |          0.76 |            0.38 |        -0.08 | 80.00%               | 3.68%         | 2.15;1.19;0.16;-0.08;0.38    |

## Strategy Comparison

Each decision rule backtested over the same data. `out_of_sample` is the most recent ~35% of each symbol's history (unseen tail). A rule has real edge only if `median_excess` and `beat_benchmark_pct` stay positive out-of-sample, not just full-sample.

| strategy        | scope         |   symbols | beat_benchmark_pct   | positive_pct   | median_return   | median_benchmark   | median_excess   |   median_sharpe |   total_trades |
|:----------------|:--------------|----------:|:---------------------|:---------------|:----------------|:-------------------|:----------------|----------------:|---------------:|
| trend           | full          |       160 | 33.75%               | 35.00%         | -9.07%          | 17.29%             | -31.65%         |           -0.09 |          11311 |
| trend           | out_of_sample |       160 | 37.50%               | 55.00%         | 2.86%           | 7.30%              | -7.35%          |            0.3  |           3960 |
| mean_reversion  | full          |       159 | 38.99%               | 47.80%         | -0.20%          | 15.42%             | -17.47%         |           -0.04 |           1264 |
| mean_reversion  | out_of_sample |       127 | 44.09%               | 56.69%         | 0.32%           | 3.29%              | -3.93%          |            0.64 |            472 |
| regime_adaptive | full          |       160 | 34.38%               | 34.38%         | -9.09%          | 17.29%             | -31.71%         |           -0.09 |          11589 |
| regime_adaptive | out_of_sample |       160 | 36.88%               | 57.50%         | 2.75%           | 7.30%              | -7.69%          |            0.29 |           4063 |

## Signal Calibration

Realized forward return in the signal's direction, grouped by confidence. HIGH should outrank LOW for the confidence score to be meaningful.

| confidence_level   |   horizon |     n | mean_return   | median_return   | win_rate   |
|:-------------------|----------:|------:|:--------------|:----------------|:-----------|
| HIGH               |         5 |  8082 | 0.15%         | 0.13%           | 52.31%     |
| MEDIUM             |         5 | 29088 | 0.01%         | 0.08%           | 50.98%     |
| LOW                |         5 |  3271 | -0.65%        | -0.51%          | 44.88%     |
| ALL                |         5 | 40441 | -0.02%        | 0.06%           | 50.75%     |
| HIGH               |        10 |  8044 | 0.48%         | 0.18%           | 52.26%     |
| MEDIUM             |        10 | 28773 | 0.15%         | 0.15%           | 51.21%     |
| LOW                |        10 |  3245 | -0.99%        | -0.79%          | 44.81%     |
| ALL                |        10 | 40062 | 0.13%         | 0.11%           | 50.90%     |
| HIGH               |        20 |  7914 | 0.85%         | 0.47%           | 53.68%     |
| MEDIUM             |        20 | 28141 | 0.75%         | 0.62%           | 53.61%     |
| LOW                |        20 |  3166 | -0.57%        | -0.48%          | 47.22%     |
| ALL                |        20 | 39221 | 0.67%         | 0.52%           | 53.11%     |

## Backtest Summary

### Data Quality / Signal Availability

- **ok**: 160 symbols

| symbol     |   trades | return   | benchmark_return   | mdd     |   sharpe | exposure   | skipped_reason   |
|:-----------|---------:|:---------|:-------------------|:--------|---------:|:-----------|:-----------------|
| AAPL       |       67 | 13.69%   | 72.27%             | -20.65% |     0.37 | 48.75%     | ok               |
| AAVE-USD   |       82 | -69.44%  | -78.39%            | -71.25% |    -1.02 | 34.10%     | ok               |
| ABBV       |       64 | -16.82%  | 34.10%             | -30.55% |    -0.34 | 49.25%     | ok               |
| ADA-USD    |       86 | -87.53%  | -75.19%            | -91.71% |    -0.91 | 44.44%     | ok               |
| ADBE       |       66 | -24.79%  | -55.51%            | -39.11% |    -0.27 | 57.07%     | ok               |
| AGG        |       73 | -7.43%   | 0.93%              | -10.16% |    -1.22 | 31.61%     | ok               |
| ALGO-USD   |       82 | -47.49%  | -71.56%            | -61.76% |    -0.5  | 37.74%     | ok               |
| AMAT       |       67 | -19.38%  | 202.52%            | -57.80% |    -0.1  | 53.58%     | ok               |
| AMD        |       56 | 54.89%   | 271.89%            | -47.17% |     0.65 | 38.94%     | ok               |
| AMGN       |       71 | -17.45%  | 10.68%             | -34.14% |    -0.32 | 49.92%     | ok               |
| AMZN       |       74 | -33.84%  | 86.71%             | -42.48% |    -0.99 | 38.27%     | ok               |
| APT-USD    |       78 | -53.62%  | -90.75%            | -69.65% |    -0.45 | 41.38%     | ok               |
| ARB-USD    |       76 | -14.74%  | -87.52%            | -63.42% |     0.09 | 37.74%     | ok               |
| ARKK       |       81 | -32.67%  | 65.99%             | -34.13% |    -0.57 | 38.94%     | ok               |
| ATOM-USD   |       88 | -68.51%  | -71.64%            | -70.79% |    -1.2  | 43.49%     | ok               |
| AVAX-USD   |       72 | -40.79%  | -78.83%            | -53.54% |    -0.4  | 36.02%     | ok               |
| AVGO       |       60 | 48.21%   | 316.84%            | -35.76% |     0.63 | 47.42%     | ok               |
| BA         |       71 | 4.66%    | -7.66%             | -30.56% |     0.21 | 51.58%     | ok               |
| BAC        |       78 | -20.55%  | 49.46%             | -27.64% |    -0.54 | 45.92%     | ok               |
| BCH-USD    |       80 | -43.97%  | -36.20%            | -58.22% |    -0.51 | 44.64%     | ok               |
| BITO       |       76 | 3.90%    | -53.34%            | -42.82% |     0.22 | 38.77%     | ok               |
| BLK        |       75 | -1.96%   | 35.02%             | -20.81% |     0.01 | 42.43%     | ok               |
| BND        |       67 | -7.84%   | 1.02%              | -9.89%  |    -1.25 | 32.61%     | ok               |
| BONK-USD   |       72 | 53.47%   | -83.86%            | -45.22% |     0.64 | 39.27%     | ok               |
| BTC-USD    |       74 | -14.62%  | -26.26%            | -29.23% |    -0.11 | 49.81%     | ok               |
| C          |       83 | -29.99%  | 131.62%            | -36.36% |    -0.61 | 51.58%     | ok               |
| CAT        |       74 | 30.89%   | 204.48%            | -21.02% |     0.58 | 58.24%     | ok               |
| CL         |       60 | 23.63%   | 13.65%             | -14.32% |     0.77 | 49.08%     | ok               |
| CMCSA      |       80 | -36.01%  | -38.30%            | -39.80% |    -0.9  | 44.26%     | ok               |
| COMP-USD   |       91 | -44.84%  | -80.02%            | -63.55% |    -0.35 | 44.25%     | ok               |
| COP        |       81 | -27.18%  | -2.29%             | -43.99% |    -0.52 | 42.10%     | ok               |
| COST       |       64 | 10.01%   | 44.83%             | -29.73% |     0.35 | 48.09%     | ok               |
| CRM        |       68 | -31.42%  | -24.61%            | -40.29% |    -0.6  | 44.76%     | ok               |
| CRV-USD    |       60 | 11.24%   | -79.25%            | -39.89% |     0.34 | 30.65%     | ok               |
| CSCO       |       61 | 22.75%   | 138.61%            | -21.79% |     0.52 | 48.42%     | ok               |
| CVX        |       75 | -19.18%  | 20.78%             | -29.70% |    -0.51 | 42.10%     | ok               |
| DASH-USD   |       65 | -44.95%  | -9.62%             | -64.43% |    -0.06 | 30.46%     | ok               |
| DBC        |       62 | -12.97%  | 32.99%             | -25.70% |    -0.44 | 33.78%     | ok               |
| DE         |       74 | -11.10%  | 37.06%             | -25.98% |    -0.17 | 45.59%     | ok               |
| DIA        |       58 | -1.59%   | 36.28%             | -12.94% |    -0.05 | 46.42%     | ok               |
| DIS        |       59 | 2.59%    | 13.52%             | -22.67% |     0.16 | 47.42%     | ok               |
| DOGE-USD   |       79 | -28.48%  | -70.73%            | -60.95% |    -0.05 | 47.89%     | ok               |
| DOT-USD    |       88 | -46.93%  | -84.18%            | -57.66% |    -0.34 | 46.74%     | ok               |
| DXY-INDEX  |       42 | -4.29%   | -5.02%             | -6.05%  |    -0.71 | 26.46%     | ok               |
| EEM        |       64 | -9.40%   | 74.51%             | -25.67% |    -0.25 | 43.43%     | ok               |
| EFA        |       60 | -9.30%   | 41.98%             | -13.53% |    -0.34 | 43.76%     | ok               |
| EOG        |       83 | -29.95%  | 10.78%             | -48.13% |    -0.69 | 47.75%     | ok               |
| ETC-USD    |       70 | -47.32%  | -70.88%            | -55.66% |    -0.82 | 30.27%     | ok               |
| ETH-USD    |       60 | 116.35%  | -42.96%            | -30.11% |     1.1  | 42.34%     | ok               |
| EWJ        |       64 | -18.27%  | 46.48%             | -30.73% |    -0.59 | 41.43%     | ok               |
| FCX        |       73 | -34.97%  | 58.95%             | -48.56% |    -0.49 | 45.09%     | ok               |
| FET-USD    |       71 | 15.54%   | -83.10%            | -46.20% |     0.4  | 38.89%     | ok               |
| FIL-USD    |       74 | -27.05%  | -82.69%            | -47.34% |    -0.17 | 32.38%     | ok               |
| FXI        |       44 | -10.87%  | 51.68%             | -23.91% |    -0.2  | 26.46%     | ok               |
| GDX        |       62 | 3.89%    | 198.82%            | -34.99% |     0.19 | 48.92%     | ok               |
| GDXJ       |       66 | -22.23%  | 228.13%            | -44.93% |    -0.22 | 47.25%     | ok               |
| GE         |       74 | 8.49%    | 218.50%            | -27.82% |     0.26 | 51.91%     | ok               |
| GLD        |       50 | 17.86%   | 121.64%            | -16.63% |     0.51 | 43.93%     | ok               |
| GOOGL      |       65 | 82.93%   | 181.81%            | -20.41% |     1.2  | 55.57%     | ok               |
| GRT-USD    |       89 | -30.28%  | -88.92%            | -56.53% |    -0.16 | 41.57%     | ok               |
| GS         |       76 | -0.53%   | 164.00%            | -22.13% |     0.09 | 50.92%     | ok               |
| HD         |       69 | -0.67%   | -6.42%             | -17.69% |     0.06 | 45.59%     | ok               |
| HON        |       95 | -19.41%  | 23.40%             | -28.64% |    -0.51 | 51.58%     | ok               |
| HYG        |       83 | -8.84%   | 4.74%              | -9.57%  |    -1.02 | 34.78%     | ok               |
| IBIT       |       30 | 35.78%   | 9.17%              | -18.95% |     0.79 | 29.40%     | ok               |
| IBM        |       74 | 41.51%   | 81.61%             | -25.31% |     0.86 | 50.42%     | ok               |
| ICP-USD    |       79 | 4.61%    | -76.28%            | -51.29% |     0.29 | 36.78%     | ok               |
| IEF        |       80 | -11.63%  | -0.71%             | -12.27% |    -1.63 | 33.28%     | ok               |
| IEMG       |       58 | -5.52%   | 68.46%             | -26.84% |    -0.12 | 43.59%     | ok               |
| INJ-USD    |       81 | -48.69%  | -72.72%            | -79.17% |    -0.43 | 38.51%     | ok               |
| INTC       |       70 | 72.47%   | 154.94%            | -60.60% |     0.7  | 49.92%     | ok               |
| INTU       |       67 | -14.99%  | -44.76%            | -43.77% |    -0.14 | 42.93%     | ok               |
| ITA        |       70 | 4.35%    | 89.00%             | -23.75% |     0.2  | 45.42%     | ok               |
| IWM        |       50 | 9.94%    | 49.65%             | -12.83% |     0.4  | 36.77%     | ok               |
| JNJ        |       76 | 2.53%    | 41.44%             | -17.51% |     0.15 | 51.58%     | ok               |
| JPM        |       75 | -23.26%  | 72.30%             | -31.39% |    -0.61 | 52.91%     | ok               |
| KO         |       49 | 24.89%   | 33.48%             | -8.07%  |     0.93 | 37.10%     | ok               |
| LDO-USD    |       78 | -15.09%  | -83.73%            | -58.32% |     0.13 | 35.82%     | ok               |
| LIN        |       72 | -3.07%   | 22.34%             | -21.53% |    -0.05 | 39.27%     | ok               |
| LINK-USD   |       70 | -18.89%  | -65.04%            | -55.61% |     0.03 | 39.85%     | ok               |
| LLY        |       69 | -13.00%  | 77.59%             | -53.34% |    -0.09 | 51.08%     | ok               |
| LRCX       |       82 | -16.50%  | 338.11%            | -63.56% |    -0.07 | 46.26%     | ok               |
| LTC-USD    |       67 | -45.14%  | -52.37%            | -55.04% |    -0.52 | 45.98%     | ok               |
| MCD        |       75 | -0.67%   | -3.38%             | -19.14% |     0.03 | 39.27%     | ok               |
| META       |       72 | 3.15%    | 77.60%             | -33.58% |     0.18 | 52.25%     | ok               |
| MPC        |       71 | -13.34%  | 63.84%             | -44.76% |    -0.13 | 49.92%     | ok               |
| MRK        |       67 | -17.84%  | 1.32%              | -32.14% |    -0.36 | 47.09%     | ok               |
| MS         |       81 | -16.73%  | 121.84%            | -26.72% |    -0.36 | 47.75%     | ok               |
| MSFT       |       74 | -25.88%  | 20.54%             | -30.56% |    -0.65 | 47.25%     | ok               |
| MU         |       55 | 206.33%  | 1058.15%           | -68.76% |     1.23 | 58.57%     | ok               |
| NEAR-USD   |       89 | 14.59%   | -55.82%            | -60.07% |     0.39 | 43.30%     | ok               |
| NEM        |       70 | -19.45%  | 172.88%            | -38.49% |    -0.12 | 55.74%     | ok               |
| NFLX       |       64 | 23.70%   | 80.83%             | -21.09% |     0.56 | 54.91%     | ok               |
| NKE        |       93 | -37.52%  | -54.38%            | -55.35% |    -0.52 | 45.76%     | ok               |
| NOW        |       78 | 20.96%   | -9.96%             | -31.32% |     0.42 | 45.76%     | ok               |
| NVDA       |       72 | -20.14%  | 150.36%            | -45.02% |    -0.08 | 61.14%     | ok               |
| OP-USD     |       75 | -2.73%   | -94.02%            | -70.11% |     0.21 | 34.48%     | ok               |
| ORCL       |       72 | 66.84%   | 113.43%            | -29.47% |     0.73 | 52.08%     | ok               |
| OXY        |       71 | 0.50%    | -4.10%             | -31.01% |     0.13 | 44.26%     | ok               |
| PEP        |       83 | -11.56%  | -14.69%            | -21.35% |    -0.29 | 48.42%     | ok               |
| PEPE-USD   |       79 | -9.56%   | -82.58%            | -57.66% |     0.18 | 41.57%     | ok               |
| PFE        |       77 | -38.05%  | -11.71%            | -42.29% |    -1.18 | 37.27%     | ok               |
| PG         |       61 | -9.37%   | -2.08%             | -20.33% |    -0.34 | 40.43%     | ok               |
| PM         |       83 | 3.14%    | 85.19%             | -33.68% |     0.16 | 56.91%     | ok               |
| POL-USD    |       78 | 57.24%   | -83.39%            | -46.45% |     0.72 | 47.70%     | ok               |
| QCOM       |       81 | -1.41%   | 83.09%             | -57.69% |     0.14 | 48.42%     | ok               |
| QQQ        |       60 | 24.00%   | 85.85%             | -12.88% |     0.67 | 46.09%     | ok               |
| RENDER-USD |       92 | -7.44%   | -52.28%            | -45.00% |     0.22 | 44.71%     | ok               |
| RTX        |       58 | 19.25%   | 108.94%            | -16.99% |     0.52 | 52.58%     | ok               |
| SBUX       |       65 | -23.57%  | 7.07%              | -31.15% |    -0.48 | 40.77%     | ok               |
| SCHW       |       76 | -22.57%  | 29.11%             | -30.41% |    -0.53 | 45.76%     | ok               |
| SHIB-USD   |       78 | -38.38%  | -77.26%            | -48.95% |    -0.32 | 49.81%     | ok               |
| SHY        |       50 | -1.95%   | 0.51%              | -2.85%  |    -0.66 | 37.27%     | ok               |
| SKY-USD    |       64 | -25.11%  | 13.12%             | -43.98% |    -0.31 | 39.66%     | ok               |
| SLB        |       77 | -29.41%  | 6.17%              | -54.23% |    -0.51 | 51.91%     | ok               |
| SLV        |       58 | 36.93%   | 223.57%            | -42.66% |     0.58 | 40.60%     | ok               |
| SMH        |       50 | 87.49%   | 261.75%            | -33.99% |     1.13 | 51.75%     | ok               |
| SNX-USD    |       65 | 7.46%    | -86.45%            | -32.91% |     0.31 | 37.93%     | ok               |
| SOL-USD    |       72 | -51.20%  | -58.97%            | -58.01% |    -0.38 | 58.43%     | ok               |
| SOXX       |       57 | 75.79%   | 215.17%            | -40.34% |     0.98 | 50.92%     | ok               |
| SPY        |       60 | 9.95%    | 61.60%             | -16.47% |     0.4  | 50.75%     | ok               |
| SUSHI-USD  |       91 | -74.47%  | -88.50%            | -77.95% |    -1.06 | 34.67%     | ok               |
| T          |       64 | 14.54%   | 41.76%             | -17.01% |     0.42 | 49.42%     | ok               |
| TGT        |       58 | -10.11%  | -10.27%            | -40.57% |    -0.12 | 39.27%     | ok               |
| TIA-USD    |       76 | -0.51%   | -92.36%            | -51.15% |     0.24 | 33.33%     | ok               |
| TLT        |       70 | -22.73%  | -10.90%            | -24.69% |    -1.65 | 33.44%     | ok               |
| TMO        |       59 | 25.18%   | -7.86%             | -16.83% |     0.58 | 50.25%     | ok               |
| TMUS       |       68 | 19.70%   | 14.26%             | -24.50% |     0.49 | 49.25%     | ok               |
| TRX-USD    |       70 | -2.64%   | 35.01%             | -22.90% |     0.03 | 49.23%     | ok               |
| TSLA       |       68 | 12.01%   | 81.56%             | -57.89% |     0.32 | 43.93%     | ok               |
| TXN        |       77 | -4.13%   | 88.62%             | -46.98% |     0.08 | 52.91%     | ok               |
| UNH        |       78 | 15.29%   | -29.26%            | -32.80% |     0.35 | 52.25%     | ok               |
| UNI-USD    |       92 | -70.85%  | -79.55%            | -79.17% |    -0.82 | 39.08%     | ok               |
| UPS        |       66 | -36.95%  | -33.41%            | -40.62% |    -0.77 | 37.77%     | ok               |
| USO        |       68 | 2.80%    | 86.12%             | -43.35% |     0.17 | 34.44%     | ok               |
| VEA        |       60 | -2.87%   | 52.85%             | -19.49% |    -0.07 | 43.43%     | ok               |
| VIXY       |       90 | -77.40%  | -62.20%            | -87.63% |    -0.92 | 30.62%     | ok               |
| VNQ        |       81 | -18.88%  | 10.67%             | -24.92% |    -0.79 | 38.27%     | ok               |
| VTI        |       70 | 0.48%    | 59.65%             | -18.77% |     0.08 | 52.08%     | ok               |
| VWO        |       76 | -13.41%  | 48.36%             | -25.20% |    -0.47 | 44.09%     | ok               |
| VZ         |       83 | -21.84%  | 19.17%             | -31.88% |    -0.65 | 40.10%     | ok               |
| WFC        |       84 | -23.33%  | 54.96%             | -30.22% |    -0.45 | 47.42%     | ok               |
| WIF-USD    |       72 | -38.04%  | -91.03%            | -50.40% |    -0.15 | 30.08%     | ok               |
| WMT        |       53 | 38.75%   | 120.32%            | -21.31% |     0.99 | 53.24%     | ok               |
| XBI        |       64 | -3.68%   | 52.08%             | -20.48% |    -0    | 40.43%     | ok               |
| XLB        |       66 | -10.52%  | 22.15%             | -24.41% |    -0.34 | 36.77%     | ok               |
| XLC        |       63 | 21.96%   | 60.67%             | -12.33% |     0.71 | 57.24%     | ok               |
| XLE        |       81 | -11.84%  | 32.95%             | -37.64% |    -0.23 | 47.09%     | ok               |
| XLF        |       76 | -11.55%  | 36.78%             | -23.61% |    -0.38 | 49.92%     | ok               |
| XLI        |       66 | 5.61%    | 55.44%             | -11.38% |     0.27 | 48.09%     | ok               |
| XLK        |       42 | 77.08%   | 106.69%            | -14.75% |     1.42 | 48.59%     | ok               |
| XLM-USD    |       67 | 39.96%   | -48.56%            | -33.79% |     0.58 | 46.55%     | ok               |
| XLP        |       72 | 8.49%    | 15.42%             | -8.96%  |     0.5  | 44.26%     | ok               |
| XLU        |       67 | -4.20%   | 37.55%             | -13.66% |    -0.15 | 38.27%     | ok               |
| XLV        |       66 | -8.65%   | 7.62%              | -14.71% |    -0.4  | 37.77%     | ok               |
| XLY        |       78 | -1.30%   | 40.50%             | -14.01% |     0.03 | 44.76%     | ok               |
| XOM        |       61 | -0.77%   | 42.35%             | -20.29% |     0.05 | 36.77%     | ok               |
| XRP-USD    |       64 | -44.43%  | -43.84%            | -54.34% |    -0.54 | 34.29%     | ok               |
| YFI-USD    |       83 | -59.54%  | -76.13%            | -67.78% |    -1.03 | 37.93%     | ok               |
| ZEC-USD    |       69 | 31.33%   | 665.60%            | -46.93% |     0.5  | 36.97%     | ok               |

## AAPL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 22.96%   | 72.27%             | -21.71% |     0.52 |       69 | 53.74%     | ok               |
|          25 | 19.72%   | 72.27%             | -20.03% |     0.47 |       67 | 51.25%     | ok               |
|          15 | 18.83%   | 72.27%             | -23.86% |     0.44 |       75 | 61.23%     | ok               |
|          30 | 13.69%   | 72.27%             | -20.65% |     0.37 |       67 | 48.75%     | ok               |
|          35 | 11.07%   | 72.27%             | -22.04% |     0.32 |       63 | 45.76%     | ok               |

## AAVE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -13.02%  | -78.39%            | -43.61% |     0.04 |       38 | 26.63%     | ok               |
|          45 | -14.80%  | -78.39%            | -46.87% |     0    |       34 | 23.75%     | ok               |
|          35 | -34.59%  | -78.39%            | -51.96% |    -0.28 |       52 | 29.31%     | ok               |
|          50 | -32.67%  | -78.39%            | -47.78% |    -0.35 |       36 | 19.16%     | ok               |
|          15 | -66.28%  | -78.39%            | -68.63% |    -0.68 |       84 | 47.89%     | ok               |

## ABBV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -5.18%   | 34.10%             | -27.91% |    -0.05 |       48 | 39.27%     | ok               |
|          40 | -12.31%  | 34.10%             | -26.61% |    -0.24 |       62 | 43.76%     | ok               |
|          35 | -14.61%  | 34.10%             | -27.83% |    -0.3  |       66 | 46.42%     | ok               |
|          45 | -15.04%  | 34.10%             | -29.59% |    -0.33 |       52 | 41.10%     | ok               |
|          30 | -16.82%  | 34.10%             | -30.55% |    -0.34 |       64 | 49.25%     | ok               |

## ADA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -88.15%  | -75.19%            | -91.83% |    -0.79 |       82 | 60.73%     | ok               |
|          50 | -83.55%  | -75.19%            | -88.20% |    -0.83 |       55 | 26.82%     | ok               |
|          20 | -88.55%  | -75.19%            | -92.33% |    -0.83 |       88 | 55.75%     | ok               |
|          30 | -87.53%  | -75.19%            | -91.71% |    -0.91 |       86 | 44.44%     | ok               |
|          45 | -86.10%  | -75.19%            | -89.92% |    -0.91 |       60 | 30.27%     | ok               |

## ADBE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 9.36%    | -55.51%            | -21.34% |     0.28 |       74 | 49.25%     | ok               |
|          40 | -4.81%   | -55.51%            | -20.88% |     0.03 |       72 | 42.26%     | ok               |
|          25 | -10.65%  | -55.51%            | -33.75% |    -0.01 |       50 | 61.23%     | ok               |
|          15 | -19.55%  | -55.51%            | -33.77% |    -0.15 |       59 | 65.72%     | ok               |
|          20 | -21.75%  | -55.51%            | -36.77% |    -0.19 |       50 | 63.39%     | ok               |

## AGG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -8.30%   | 0.93%              | -10.95% |    -1.21 |       77 | 37.27%     | ok               |
|          30 | -7.43%   | 0.93%              | -10.16% |    -1.22 |       73 | 31.61%     | ok               |
|          45 | -6.34%   | 0.93%              | -7.89%  |    -1.25 |       54 | 20.80%     | ok               |
|          25 | -8.59%   | 0.93%              | -11.59% |    -1.31 |       75 | 35.44%     | ok               |
|          15 | -9.41%   | 0.93%              | -12.40% |    -1.34 |       81 | 40.77%     | ok               |

## ALGO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -47.49%  | -71.56%            | -61.76% |    -0.5  |       82 | 37.74%     | ok               |
|          15 | -57.91%  | -71.56%            | -70.86% |    -0.58 |       78 | 49.43%     | ok               |
|          25 | -58.02%  | -71.56%            | -75.14% |    -0.63 |       84 | 45.02%     | ok               |
|          35 | -51.05%  | -71.56%            | -54.80% |    -0.7  |       60 | 30.65%     | ok               |
|          20 | -62.36%  | -71.56%            | -73.99% |    -0.71 |       82 | 47.32%     | ok               |

## AMAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -5.33%   | 202.52%            | -54.69% |     0.12 |       66 | 62.40%     | ok               |
|          30 | -19.38%  | 202.52%            | -57.80% |    -0.1  |       67 | 53.58%     | ok               |
|          20 | -25.27%  | 202.52%            | -60.72% |    -0.17 |       70 | 58.74%     | ok               |
|          35 | -25.12%  | 202.52%            | -55.89% |    -0.21 |       69 | 51.41%     | ok               |
|          25 | -28.77%  | 202.52%            | -60.95% |    -0.25 |       69 | 56.41%     | ok               |

## AMD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 54.89%   | 271.89%            | -47.17% |     0.65 |       56 | 38.94%     | ok               |
|          50 | 44.76%   | 271.89%            | -48.79% |     0.59 |       60 | 33.44%     | ok               |
|          35 | 35.14%   | 271.89%            | -54.57% |     0.51 |       62 | 40.93%     | ok               |
|          45 | 23.74%   | 271.89%            | -56.22% |     0.43 |       64 | 36.27%     | ok               |
|          30 | 17.32%   | 271.89%            | -59.88% |     0.37 |       63 | 43.43%     | ok               |

## AMGN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -11.73%  | 10.68%             | -26.64% |    -0.16 |       73 | 55.91%     | ok               |
|          35 | -13.41%  | 10.68%             | -31.23% |    -0.22 |       67 | 46.09%     | ok               |
|          15 | -15.43%  | 10.68%             | -27.92% |    -0.23 |       72 | 61.73%     | ok               |
|          30 | -17.45%  | 10.68%             | -34.14% |    -0.32 |       71 | 49.92%     | ok               |
|          25 | -20.81%  | 10.68%             | -33.41% |    -0.4  |       67 | 52.25%     | ok               |

## AMZN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -17.83%  | 86.71%             | -28.70% |    -0.52 |       50 | 29.78%     | ok               |
|          50 | -25.03%  | 86.71%             | -35.48% |    -0.88 |       48 | 24.13%     | ok               |
|          45 | -25.89%  | 86.71%             | -35.47% |    -0.89 |       50 | 26.96%     | ok               |
|          35 | -29.70%  | 86.71%             | -38.29% |    -0.91 |       62 | 32.95%     | ok               |
|          30 | -33.84%  | 86.71%             | -42.48% |    -0.99 |       74 | 38.27%     | ok               |

## APT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 28.30%   | -90.75%            | -46.73% |     0.52 |       46 | 18.77%     | ok               |
|          45 | -14.07%  | -90.75%            | -64.17% |     0.03 |       64 | 25.10%     | ok               |
|          40 | -32.68%  | -90.75%            | -63.33% |    -0.18 |       68 | 30.65%     | ok               |
|          35 | -38.37%  | -90.75%            | -64.09% |    -0.23 |       72 | 36.02%     | ok               |
|          20 | -47.29%  | -90.75%            | -70.51% |    -0.29 |       77 | 49.81%     | ok               |

## ARB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 47.17%   | -87.52%            | -52.62% |     0.6  |       89 | 55.36%     | ok               |
|          40 | 28.04%   | -87.52%            | -45.37% |     0.49 |       52 | 28.35%     | ok               |
|          50 | 15.68%   | -87.52%            | -44.38% |     0.37 |       40 | 16.67%     | ok               |
|          35 | 12.82%   | -87.52%            | -54.93% |     0.36 |       66 | 32.38%     | ok               |
|          20 | 8.70%    | -87.52%            | -61.20% |     0.35 |       81 | 49.23%     | ok               |

## ARKK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -29.68%  | 65.99%             | -39.54% |    -0.39 |       96 | 51.41%     | ok               |
|          20 | -31.80%  | 65.99%             | -35.95% |    -0.47 |       89 | 45.92%     | ok               |
|          30 | -32.67%  | 65.99%             | -34.13% |    -0.57 |       81 | 38.94%     | ok               |
|          35 | -33.82%  | 65.99%             | -35.25% |    -0.63 |       80 | 36.61%     | ok               |
|          40 | -34.16%  | 65.99%             | -35.67% |    -0.68 |       70 | 31.61%     | ok               |

## ATOM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -67.89%  | -71.64%            | -75.71% |    -0.99 |       95 | 60.73%     | ok               |
|          25 | -65.51%  | -71.64%            | -68.50% |    -1.03 |       95 | 49.81%     | ok               |
|          20 | -70.44%  | -71.64%            | -74.33% |    -1.13 |      103 | 54.41%     | ok               |
|          30 | -68.51%  | -71.64%            | -70.79% |    -1.2  |       88 | 43.49%     | ok               |
|          35 | -66.09%  | -71.64%            | -66.74% |    -1.24 |       78 | 39.08%     | ok               |

## AVAX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.47%   | -78.83%            | -29.53% |     0.16 |       32 | 18.58%     | ok               |
|          45 | -3.51%   | -78.83%            | -32.82% |     0.12 |       34 | 21.46%     | ok               |
|          35 | -11.14%  | -78.83%            | -36.01% |     0.05 |       58 | 28.74%     | ok               |
|          15 | -19.76%  | -78.83%            | -50.68% |     0.04 |       65 | 50.77%     | ok               |
|          40 | -9.91%   | -78.83%            | -32.65% |     0.03 |       40 | 23.18%     | ok               |

## AVGO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 48.21%   | 316.84%            | -35.76% |     0.63 |       60 | 47.42%     | ok               |
|          25 | 42.94%   | 316.84%            | -38.01% |     0.59 |       64 | 48.09%     | ok               |
|          35 | 35.61%   | 316.84%            | -36.19% |     0.53 |       72 | 44.59%     | ok               |
|          40 | 29.71%   | 316.84%            | -40.70% |     0.48 |       62 | 40.93%     | ok               |
|          20 | 29.43%   | 316.84%            | -40.10% |     0.47 |       72 | 50.92%     | ok               |

## BA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 23.99%   | -7.66%             | -23.77% |     0.49 |       76 | 46.76%     | ok               |
|          50 | 16.03%   | -7.66%             | -16.71% |     0.46 |       46 | 31.61%     | ok               |
|          25 | 7.78%    | -7.66%             | -32.48% |     0.25 |       74 | 55.07%     | ok               |
|          30 | 4.66%    | -7.66%             | -30.56% |     0.21 |       71 | 51.58%     | ok               |
|          40 | 2.19%    | -7.66%             | -30.87% |     0.15 |       52 | 39.93%     | ok               |

## BAC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -10.23%  | 49.46%             | -20.40% |    -0.28 |       58 | 33.94%     | ok               |
|          20 | -14.57%  | 49.46%             | -20.73% |    -0.29 |       79 | 50.58%     | ok               |
|          35 | -14.80%  | 49.46%             | -27.83% |    -0.39 |       70 | 41.93%     | ok               |
|          15 | -19.06%  | 49.46%             | -22.24% |    -0.4  |       81 | 55.57%     | ok               |
|          50 | -13.28%  | 49.46%             | -20.35% |    -0.42 |       56 | 30.95%     | ok               |

## BCH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -44.63%  | -36.20%            | -61.84% |    -0.42 |       87 | 57.09%     | ok               |
|          20 | -45.80%  | -36.20%            | -61.14% |    -0.47 |       84 | 52.11%     | ok               |
|          30 | -43.97%  | -36.20%            | -58.22% |    -0.51 |       80 | 44.64%     | ok               |
|          25 | -49.75%  | -36.20%            | -61.79% |    -0.6  |       76 | 47.32%     | ok               |
|          40 | -48.33%  | -36.20%            | -62.46% |    -0.68 |       65 | 37.55%     | ok               |

## BITO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 17.67%   | -53.34%            | -32.29% |     0.38 |       52 | 24.13%     | ok               |
|          30 | 3.90%    | -53.34%            | -42.82% |     0.22 |       76 | 38.77%     | ok               |
|          15 | -2.62%   | -53.34%            | -48.38% |     0.17 |       85 | 47.59%     | ok               |
|          45 | -1.86%   | -53.34%            | -43.53% |     0.13 |       56 | 27.12%     | ok               |
|          25 | -4.32%   | -53.34%            | -41.73% |     0.13 |       80 | 41.76%     | ok               |

## BLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 4.68%    | 35.02%             | -14.19% |     0.21 |       80 | 38.60%     | ok               |
|          40 | 3.48%    | 35.02%             | -15.20% |     0.18 |       74 | 34.28%     | ok               |
|          20 | 0.36%    | 35.02%             | -17.89% |     0.09 |       77 | 47.25%     | ok               |
|          30 | -1.96%   | 35.02%             | -20.81% |     0.01 |       75 | 42.43%     | ok               |
|          25 | -2.94%   | 35.02%             | -19.84% |    -0.01 |       75 | 44.76%     | ok               |

## BND Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -7.25%   | 1.02%              | -9.05%  |    -1.05 |       69 | 39.27%     | ok               |
|          25 | -7.47%   | 1.02%              | -10.14% |    -1.13 |       71 | 36.61%     | ok               |
|          30 | -7.84%   | 1.02%              | -9.89%  |    -1.25 |       67 | 32.61%     | ok               |
|          15 | -9.46%   | 1.02%              | -10.58% |    -1.35 |       73 | 42.26%     | ok               |
|          45 | -8.27%   | 1.02%              | -9.57%  |    -1.58 |       52 | 22.13%     | ok               |

## BONK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 130.96%  | -83.86%            | -35.57% |     1.09 |       42 | 20.88%     | ok               |
|          20 | 146.15%  | -83.86%            | -55.43% |     0.97 |       68 | 50.38%     | ok               |
|          45 | 105.86%  | -83.86%            | -42.36% |     0.96 |       52 | 24.14%     | ok               |
|          25 | 129.64%  | -83.86%            | -47.99% |     0.93 |       67 | 45.59%     | ok               |
|          15 | 138.12%  | -83.86%            | -63.45% |     0.92 |       69 | 54.79%     | ok               |

## BTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 29.82%   | -26.26%            | -19.59% |     0.66 |       42 | 28.54%     | ok               |
|          40 | 26.84%   | -26.26%            | -20.30% |     0.59 |       46 | 31.80%     | ok               |
|          50 | 14.92%   | -26.26%            | -17.58% |     0.41 |       40 | 25.29%     | ok               |
|          35 | 10.29%   | -26.26%            | -32.64% |     0.31 |       72 | 39.08%     | ok               |
|          30 | -5.31%   | -26.26%            | -29.09% |     0.05 |       74 | 45.98%     | ok               |

## C Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -13.97%  | 131.62%            | -21.64% |    -0.34 |       70 | 35.27%     | ok               |
|          15 | -27.74%  | 131.62%            | -34.03% |    -0.5  |       76 | 60.23%     | ok               |
|          25 | -26.44%  | 131.62%            | -33.47% |    -0.5  |       75 | 53.41%     | ok               |
|          20 | -28.30%  | 131.62%            | -34.53% |    -0.54 |       81 | 56.57%     | ok               |
|          45 | -22.96%  | 131.62%            | -29.28% |    -0.59 |       84 | 39.93%     | ok               |

## CAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 30.89%   | 204.48%            | -21.02% |     0.58 |       74 | 58.24%     | ok               |
|          25 | 31.01%   | 204.48%            | -26.37% |     0.57 |       70 | 61.06%     | ok               |
|          20 | 28.36%   | 204.48%            | -25.65% |     0.54 |       80 | 64.39%     | ok               |
|          45 | 21.92%   | 204.48%            | -28.85% |     0.47 |       58 | 46.59%     | ok               |
|          15 | 21.25%   | 204.48%            | -30.60% |     0.44 |       73 | 70.72%     | ok               |

## CL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 23.63%   | 13.65%             | -14.32% |     0.77 |       60 | 49.08%     | ok               |
|          45 | 18.78%   | 13.65%             | -13.51% |     0.74 |       46 | 35.94%     | ok               |
|          50 | 17.80%   | 13.65%             | -13.51% |     0.73 |       44 | 33.11%     | ok               |
|          35 | 17.75%   | 13.65%             | -13.83% |     0.62 |       62 | 45.42%     | ok               |
|          25 | 17.52%   | 13.65%             | -14.29% |     0.59 |       58 | 50.42%     | ok               |

## CMCSA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -36.01%  | -38.30%            | -39.80% |    -0.9  |       80 | 44.26%     | ok               |
|          15 | -39.55%  | -38.30%            | -49.03% |    -0.93 |       89 | 58.74%     | ok               |
|          25 | -41.18%  | -38.30%            | -44.66% |    -1.06 |       87 | 49.08%     | ok               |
|          20 | -42.72%  | -38.30%            | -47.23% |    -1.08 |       95 | 55.07%     | ok               |
|          50 | -29.51%  | -38.30%            | -33.68% |    -1.08 |       50 | 17.14%     | ok               |

## COMP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -20.22%  | -80.02%            | -38.71% |    -0.09 |       46 | 19.73%     | ok               |
|          25 | -45.78%  | -80.02%            | -63.29% |    -0.32 |       91 | 49.62%     | ok               |
|          30 | -44.84%  | -80.02%            | -63.55% |    -0.35 |       91 | 44.25%     | ok               |
|          15 | -53.97%  | -80.02%            | -67.05% |    -0.42 |      109 | 61.88%     | ok               |
|          40 | -44.82%  | -80.02%            | -47.56% |    -0.46 |       74 | 32.18%     | ok               |

## COP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -16.52%  | -2.29%             | -34.85% |    -0.32 |       54 | 28.12%     | ok               |
|          45 | -23.78%  | -2.29%             | -41.14% |    -0.52 |       66 | 30.95%     | ok               |
|          35 | -26.65%  | -2.29%             | -43.88% |    -0.52 |       81 | 38.10%     | ok               |
|          30 | -27.18%  | -2.29%             | -43.99% |    -0.52 |       81 | 42.10%     | ok               |
|          25 | -34.54%  | -2.29%             | -49.23% |    -0.7  |       90 | 46.26%     | ok               |

## COST Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 22.40%   | 44.83%             | -24.73% |     0.65 |       63 | 51.58%     | ok               |
|          20 | 21.77%   | 44.83%             | -24.32% |     0.62 |       64 | 54.08%     | ok               |
|          35 | 16.57%   | 44.83%             | -26.58% |     0.54 |       56 | 44.93%     | ok               |
|          40 | 9.41%    | 44.83%             | -28.41% |     0.35 |       58 | 41.93%     | ok               |
|          30 | 10.01%   | 44.83%             | -29.73% |     0.35 |       64 | 48.09%     | ok               |

## CRM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -24.32%  | -24.61%            | -38.20% |    -0.31 |       91 | 56.24%     | ok               |
|          35 | -20.16%  | -24.61%            | -35.46% |    -0.34 |       66 | 39.93%     | ok               |
|          40 | -27.40%  | -24.61%            | -41.30% |    -0.59 |       70 | 35.61%     | ok               |
|          30 | -31.42%  | -24.61%            | -40.29% |    -0.6  |       68 | 44.76%     | ok               |
|          20 | -37.89%  | -24.61%            | -42.67% |    -0.68 |       79 | 49.75%     | ok               |

## CRV-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 39.22%   | -79.25%            | -37.78% |     0.58 |       60 | 26.25%     | ok               |
|          50 | 29.03%   | -79.25%            | -29.30% |     0.51 |       34 | 15.71%     | ok               |
|          40 | 21.58%   | -79.25%            | -38.86% |     0.43 |       48 | 22.80%     | ok               |
|          45 | 16.41%   | -79.25%            | -42.29% |     0.38 |       46 | 18.20%     | ok               |
|          30 | 11.24%   | -79.25%            | -39.89% |     0.34 |       60 | 30.65%     | ok               |

## CSCO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 29.24%   | 138.61%            | -19.34% |     0.68 |       56 | 37.44%     | ok               |
|          45 | 25.89%   | 138.61%            | -19.34% |     0.6  |       51 | 39.60%     | ok               |
|          30 | 22.75%   | 138.61%            | -21.79% |     0.52 |       61 | 48.42%     | ok               |
|          25 | 22.43%   | 138.61%            | -23.28% |     0.51 |       66 | 50.58%     | ok               |
|          40 | 20.23%   | 138.61%            | -19.61% |     0.48 |       53 | 42.10%     | ok               |

## CVX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -14.81%  | 20.78%             | -25.91% |    -0.34 |       74 | 44.59%     | ok               |
|          35 | -16.76%  | 20.78%             | -28.85% |    -0.44 |       69 | 39.10%     | ok               |
|          20 | -18.91%  | 20.78%             | -30.41% |    -0.47 |       80 | 46.09%     | ok               |
|          30 | -19.18%  | 20.78%             | -29.70% |    -0.51 |       75 | 42.10%     | ok               |
|          40 | -17.80%  | 20.78%             | -28.41% |    -0.52 |       79 | 36.11%     | ok               |

## DASH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 117.25%  | -9.62%             | -32.30% |     0.91 |       42 | 15.71%     | ok               |
|          40 | 70.64%   | -9.62%             | -32.07% |     0.7  |       48 | 22.41%     | ok               |
|          45 | 56.89%   | -9.62%             | -40.40% |     0.63 |       46 | 18.01%     | ok               |
|          25 | -40.83%  | -9.62%             | -64.14% |     0.01 |       73 | 33.91%     | ok               |
|          35 | -39.92%  | -9.62%             | -63.23% |     0    |       71 | 27.01%     | ok               |

## DBC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -7.75%   | 32.99%             | -20.31% |    -0.29 |       40 | 21.13%     | ok               |
|          45 | -9.53%   | 32.99%             | -21.46% |    -0.33 |       54 | 24.63%     | ok               |
|          35 | -11.02%  | 32.99%             | -23.91% |    -0.37 |       62 | 31.61%     | ok               |
|          15 | -11.67%  | 32.99%             | -26.60% |    -0.38 |       65 | 38.44%     | ok               |
|          30 | -12.97%  | 32.99%             | -25.70% |    -0.44 |       62 | 33.78%     | ok               |

## DE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -9.56%   | 37.06%             | -28.94% |    -0.12 |       74 | 51.25%     | ok               |
|          50 | -7.18%   | 37.06%             | -23.74% |    -0.13 |       62 | 29.78%     | ok               |
|          15 | -11.19%  | 37.06%             | -27.41% |    -0.16 |       78 | 54.58%     | ok               |
|          25 | -10.96%  | 37.06%             | -26.67% |    -0.16 |       76 | 48.42%     | ok               |
|          30 | -11.10%  | 37.06%             | -25.98% |    -0.17 |       74 | 45.59%     | ok               |

## DIA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 0.07%    | 36.28%             | -11.28% |     0.04 |       58 | 47.75%     | ok               |
|          35 | 0.07%    | 36.28%             | -13.15% |     0.04 |       60 | 44.59%     | ok               |
|          30 | -1.59%   | 36.28%             | -12.94% |    -0.05 |       58 | 46.42%     | ok               |
|          20 | -2.76%   | 36.28%             | -14.29% |    -0.1  |       60 | 50.25%     | ok               |
|          40 | -3.77%   | 36.28%             | -15.06% |    -0.18 |       66 | 41.60%     | ok               |

## DIS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 40.04%   | 13.52%             | -14.24% |     0.96 |       46 | 30.12%     | ok               |
|          45 | 9.81%    | 13.52%             | -15.09% |     0.3  |       49 | 33.44%     | ok               |
|          40 | 8.82%    | 13.52%             | -22.77% |     0.28 |       61 | 38.60%     | ok               |
|          35 | 5.61%    | 13.52%             | -20.85% |     0.21 |       69 | 44.43%     | ok               |
|          30 | 2.59%    | 13.52%             | -22.67% |     0.16 |       59 | 47.42%     | ok               |

## DOGE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 8.00%    | -70.73%            | -57.89% |     0.36 |       83 | 64.56%     | ok               |
|          20 | -4.01%   | -70.73%            | -55.83% |     0.25 |       86 | 60.34%     | ok               |
|          25 | -11.47%  | -70.73%            | -53.72% |     0.16 |       78 | 53.83%     | ok               |
|          30 | -28.48%  | -70.73%            | -60.95% |    -0.05 |       79 | 47.89%     | ok               |
|          35 | -53.17%  | -70.73%            | -68.58% |    -0.53 |       76 | 41.19%     | ok               |

## DOT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -24.98%  | -84.18%            | -43.91% |    -0.21 |       54 | 26.25%     | ok               |
|          45 | -29.59%  | -84.18%            | -48.71% |    -0.26 |       50 | 29.69%     | ok               |
|          30 | -46.93%  | -84.18%            | -57.66% |    -0.34 |       88 | 46.74%     | ok               |
|          35 | -45.90%  | -84.18%            | -59.34% |    -0.35 |       78 | 40.04%     | ok               |
|          40 | -37.31%  | -84.18%            | -48.60% |    -0.35 |       56 | 33.14%     | ok               |

## DXY-INDEX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -4.53%   | -5.02%             | -11.66% |    -0.4  |       90 | 75.27%     | ok               |
|          30 | -3.72%   | -5.02%             | -10.02% |    -0.4  |       68 | 57.70%     | ok               |
|          35 | -4.16%   | -5.02%             | -9.23%  |    -0.48 |       71 | 52.06%     | ok               |
|          40 | -4.40%   | -5.02%             | -7.30%  |    -0.56 |       66 | 45.12%     | ok               |
|          25 | -6.32%   | -5.02%             | -11.69% |    -0.67 |       82 | 63.12%     | ok               |

## EEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -4.96%   | 74.51%             | -19.52% |    -0.11 |       64 | 39.77%     | ok               |
|          35 | -5.62%   | 74.51%             | -23.88% |    -0.12 |       66 | 41.76%     | ok               |
|          50 | -4.94%   | 74.51%             | -15.88% |    -0.12 |       52 | 35.77%     | ok               |
|          45 | -6.04%   | 74.51%             | -17.36% |    -0.16 |       54 | 37.44%     | ok               |
|          25 | -8.49%   | 74.51%             | -25.60% |    -0.21 |       65 | 44.76%     | ok               |

## EFA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -1.66%   | 41.98%             | -11.27% |     0    |       60 | 51.75%     | ok               |
|          20 | -7.88%   | 41.98%             | -12.37% |    -0.26 |       65 | 48.92%     | ok               |
|          30 | -9.30%   | 41.98%             | -13.53% |    -0.34 |       60 | 43.76%     | ok               |
|          50 | -9.33%   | 41.98%             | -17.80% |    -0.41 |       56 | 36.44%     | ok               |
|          25 | -11.34%  | 41.98%             | -15.78% |    -0.42 |       64 | 46.42%     | ok               |

## EOG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -29.95%  | 10.78%             | -48.13% |    -0.69 |       83 | 47.75%     | ok               |
|          25 | -31.71%  | 10.78%             | -51.99% |    -0.7  |       84 | 51.08%     | ok               |
|          40 | -28.13%  | 10.78%             | -43.26% |    -0.72 |       64 | 36.77%     | ok               |
|          45 | -28.02%  | 10.78%             | -43.17% |    -0.76 |       58 | 33.28%     | ok               |
|          35 | -30.72%  | 10.78%             | -46.26% |    -0.77 |       81 | 42.43%     | ok               |

## ETC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -14.16%  | -70.88%            | -30.24% |    -0.14 |       26 | 16.86%     | ok               |
|          35 | -26.49%  | -70.88%            | -42.62% |    -0.34 |       44 | 25.29%     | ok               |
|          45 | -26.10%  | -70.88%            | -36.69% |    -0.4  |       26 | 18.01%     | ok               |
|          40 | -30.62%  | -70.88%            | -42.37% |    -0.49 |       40 | 21.26%     | ok               |
|          15 | -52.43%  | -70.88%            | -59.26% |    -0.79 |       84 | 44.64%     | ok               |

## ETH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 116.35%  | -42.96%            | -30.11% |     1.1  |       60 | 42.34%     | ok               |
|          30 | 107.18%  | -42.96%            | -32.89% |     1.01 |       66 | 50.00%     | ok               |
|          40 | 45.65%   | -42.96%            | -33.11% |     0.67 |       56 | 35.44%     | ok               |
|          50 | 41.53%   | -42.96%            | -30.50% |     0.65 |       54 | 26.44%     | ok               |
|          45 | 36.87%   | -42.96%            | -34.50% |     0.59 |       52 | 31.99%     | ok               |

## EWJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -18.27%  | 46.48%             | -30.73% |    -0.59 |       64 | 41.43%     | ok               |
|          20 | -19.65%  | 46.48%             | -31.32% |    -0.62 |       60 | 43.43%     | ok               |
|          25 | -21.97%  | 46.48%             | -31.18% |    -0.72 |       60 | 42.43%     | ok               |
|          35 | -22.19%  | 46.48%             | -32.54% |    -0.75 |       70 | 39.77%     | ok               |
|          15 | -24.97%  | 46.48%             | -32.24% |    -0.78 |       74 | 46.59%     | ok               |

## FCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -12.91%  | 58.95%             | -27.80% |    -0.11 |       58 | 28.95%     | ok               |
|          45 | -17.09%  | 58.95%             | -35.28% |    -0.17 |       60 | 33.44%     | ok               |
|          40 | -28.92%  | 58.95%             | -44.23% |    -0.4  |       70 | 38.44%     | ok               |
|          20 | -36.77%  | 58.95%             | -57.65% |    -0.46 |       80 | 52.75%     | ok               |
|          30 | -34.97%  | 58.95%             | -48.56% |    -0.49 |       73 | 45.09%     | ok               |

## FET-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 89.35%   | -83.10%            | -44.27% |     0.8  |       86 | 50.38%     | ok               |
|          15 | 30.38%   | -83.10%            | -55.21% |     0.52 |       90 | 53.64%     | ok               |
|          25 | 21.98%   | -83.10%            | -45.03% |     0.45 |       87 | 43.30%     | ok               |
|          30 | 15.54%   | -83.10%            | -46.20% |     0.4  |       71 | 38.89%     | ok               |
|          35 | -14.89%  | -83.10%            | -51.18% |     0.09 |       59 | 32.38%     | ok               |

## FIL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 1.58%    | -82.69%            | -38.41% |     0.2  |       46 | 22.61%     | ok               |
|          50 | -6.50%   | -82.69%            | -38.12% |     0.06 |       34 | 12.84%     | ok               |
|          45 | -17.61%  | -82.69%            | -38.83% |    -0.1  |       44 | 17.43%     | ok               |
|          35 | -23.77%  | -82.69%            | -44.93% |    -0.15 |       56 | 26.44%     | ok               |
|          30 | -27.05%  | -82.69%            | -47.34% |    -0.17 |       74 | 32.38%     | ok               |

## FXI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -10.87%  | 51.68%             | -23.91% |    -0.2  |       44 | 26.46%     | ok               |
|          50 | -10.98%  | 51.68%             | -23.27% |    -0.23 |       36 | 19.30%     | ok               |
|          25 | -12.39%  | 51.68%             | -22.57% |    -0.24 |       46 | 27.45%     | ok               |
|          45 | -12.44%  | 51.68%             | -24.52% |    -0.27 |       40 | 21.30%     | ok               |
|          15 | -14.30%  | 51.68%             | -21.68% |    -0.28 |       52 | 31.11%     | ok               |

## GDX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 21.37%   | 198.82%            | -31.87% |     0.46 |       60 | 43.09%     | ok               |
|          20 | 14.61%   | 198.82%            | -35.59% |     0.35 |       72 | 53.24%     | ok               |
|          35 | 6.14%    | 198.82%            | -32.37% |     0.23 |       66 | 45.59%     | ok               |
|          30 | 3.89%    | 198.82%            | -34.99% |     0.19 |       62 | 48.92%     | ok               |
|          50 | 3.99%    | 198.82%            | -28.64% |     0.19 |       50 | 38.27%     | ok               |

## GDXJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -8.43%   | 228.13%            | -45.05% |     0.04 |       67 | 52.91%     | ok               |
|          50 | -10.73%  | 228.13%            | -35.02% |    -0.06 |       62 | 37.77%     | ok               |
|          30 | -22.23%  | 228.13%            | -44.93% |    -0.22 |       66 | 47.25%     | ok               |
|          25 | -26.04%  | 228.13%            | -47.26% |    -0.26 |       70 | 49.75%     | ok               |
|          40 | -24.73%  | 228.13%            | -44.27% |    -0.3  |       64 | 42.76%     | ok               |

## GE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 21.26%   | 218.50%            | -22.29% |     0.49 |       66 | 38.44%     | ok               |
|          45 | 13.14%   | 218.50%            | -25.68% |     0.35 |       76 | 41.43%     | ok               |
|          20 | 13.85%   | 218.50%            | -26.63% |     0.34 |       69 | 55.41%     | ok               |
|          15 | 8.99%    | 218.50%            | -28.62% |     0.27 |       68 | 57.74%     | ok               |
|          35 | 8.74%    | 218.50%            | -27.11% |     0.27 |       80 | 46.92%     | ok               |

## GLD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 19.38%   | 121.64%            | -14.61% |     0.54 |       48 | 44.93%     | ok               |
|          20 | 18.59%   | 121.64%            | -14.61% |     0.52 |       50 | 46.09%     | ok               |
|          30 | 17.86%   | 121.64%            | -16.63% |     0.51 |       50 | 43.93%     | ok               |
|          35 | 12.10%   | 121.64%            | -17.29% |     0.38 |       52 | 43.26%     | ok               |
|          15 | 12.22%   | 121.64%            | -16.82% |     0.37 |       52 | 50.75%     | ok               |

## GOOGL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 92.11%   | 181.81%            | -19.76% |     1.27 |       59 | 57.74%     | ok               |
|          15 | 90.67%   | 181.81%            | -13.59% |     1.21 |       67 | 65.06%     | ok               |
|          30 | 82.93%   | 181.81%            | -20.41% |     1.2  |       65 | 55.57%     | ok               |
|          20 | 79.47%   | 181.81%            | -20.57% |     1.14 |       68 | 59.90%     | ok               |
|          35 | 66.83%   | 181.81%            | -22.85% |     1.09 |       71 | 50.42%     | ok               |

## GRT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 25.48%   | -88.92%            | -30.82% |     0.49 |       46 | 22.22%     | ok               |
|          15 | 0.50%    | -88.92%            | -49.67% |     0.27 |       81 | 60.92%     | ok               |
|          45 | 3.68%    | -88.92%            | -46.73% |     0.23 |       52 | 26.63%     | ok               |
|          40 | 0.93%    | -88.92%            | -45.40% |     0.2  |       52 | 29.69%     | ok               |
|          20 | -6.93%   | -88.92%            | -46.47% |     0.18 |       91 | 55.56%     | ok               |

## GS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 26.30%   | 164.00%            | -20.56% |     0.56 |       74 | 59.90%     | ok               |
|          20 | 9.07%    | 164.00%            | -23.19% |     0.28 |       74 | 55.91%     | ok               |
|          25 | 5.62%    | 164.00%            | -23.32% |     0.21 |       74 | 53.41%     | ok               |
|          40 | 0.86%    | 164.00%            | -17.88% |     0.11 |       72 | 44.26%     | ok               |
|          30 | -0.53%   | 164.00%            | -22.13% |     0.09 |       76 | 50.92%     | ok               |

## HD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -0.67%   | -6.42%             | -17.69% |     0.06 |       69 | 45.59%     | ok               |
|          25 | -1.44%   | -6.42%             | -18.51% |     0.04 |       68 | 47.59%     | ok               |
|          35 | -9.91%   | -6.42%             | -22.98% |    -0.21 |       76 | 41.93%     | ok               |
|          40 | -10.67%  | -6.42%             | -20.58% |    -0.28 |       82 | 35.44%     | ok               |
|          20 | -14.17%  | -6.42%             | -23.94% |    -0.3  |       85 | 50.75%     | ok               |

## HON Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -11.84%  | 23.40%             | -23.12% |    -0.35 |       74 | 31.45%     | ok               |
|          45 | -14.57%  | 23.40%             | -22.74% |    -0.42 |       80 | 36.94%     | ok               |
|          40 | -15.51%  | 23.40%             | -23.13% |    -0.43 |       80 | 40.93%     | ok               |
|          35 | -17.12%  | 23.40%             | -26.26% |    -0.46 |       95 | 47.25%     | ok               |
|          30 | -19.41%  | 23.40%             | -28.64% |    -0.51 |       95 | 51.58%     | ok               |

## HYG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          40 | -7.27%   | 4.74%              | -8.02% |    -0.87 |       70 | 29.78%     | ok               |
|          15 | -8.55%   | 4.74%              | -9.99% |    -0.91 |       90 | 42.10%     | ok               |
|          20 | -8.48%   | 4.74%              | -9.99% |    -0.93 |       88 | 39.77%     | ok               |
|          45 | -7.96%   | 4.74%              | -8.70% |    -0.99 |       66 | 26.62%     | ok               |
|          25 | -9.14%   | 4.74%              | -9.87% |    -1.02 |       85 | 37.44%     | ok               |

## IBIT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 52.15%   | 9.17%              | -12.64% |     1.12 |       18 | 21.36%     | ok               |
|          15 | 64.79%   | 9.17%              | -19.20% |     1.11 |       36 | 37.44%     | ok               |
|          45 | 43.69%   | 9.17%              | -17.12% |     0.96 |       20 | 22.11%     | ok               |
|          40 | 42.27%   | 9.17%              | -17.12% |     0.93 |       22 | 23.62%     | ok               |
|          30 | 35.78%   | 9.17%              | -18.95% |     0.79 |       30 | 29.40%     | ok               |

## IBM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 49.64%   | 81.61%             | -28.20% |     0.87 |       87 | 62.56%     | ok               |
|          30 | 41.51%   | 81.61%             | -25.31% |     0.86 |       74 | 50.42%     | ok               |
|          35 | 35.35%   | 81.61%             | -25.15% |     0.78 |       70 | 45.92%     | ok               |
|          45 | 28.55%   | 81.61%             | -18.73% |     0.71 |       54 | 36.77%     | ok               |
|          50 | 23.97%   | 81.61%             | -21.46% |     0.63 |       52 | 33.78%     | ok               |

## ICP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 23.34%   | -76.28%            | -38.23% |     0.45 |       64 | 30.84%     | ok               |
|          40 | 16.82%   | -76.28%            | -30.85% |     0.38 |       58 | 26.44%     | ok               |
|          50 | 12.63%   | -76.28%            | -32.35% |     0.33 |       38 | 16.67%     | ok               |
|          30 | 4.61%    | -76.28%            | -51.29% |     0.29 |       79 | 36.78%     | ok               |
|          20 | -20.49%  | -76.28%            | -56.15% |     0.11 |       91 | 47.70%     | ok               |

## IEF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -8.36%   | -0.71%             | -9.79%  |    -1    |       74 | 42.26%     | ok               |
|          15 | -8.91%   | -0.71%             | -10.52% |    -1.05 |       73 | 43.76%     | ok               |
|          40 | -8.39%   | -0.71%             | -9.67%  |    -1.31 |       60 | 24.79%     | ok               |
|          45 | -8.07%   | -0.71%             | -9.73%  |    -1.33 |       50 | 22.80%     | ok               |
|          25 | -10.98%  | -0.71%             | -11.58% |    -1.38 |       76 | 39.77%     | ok               |

## IEMG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -0.32%   | 68.46%             | -22.13% |     0.05 |       63 | 42.60%     | ok               |
|          50 | -2.69%   | 68.46%             | -14.40% |    -0.05 |       56 | 33.94%     | ok               |
|          40 | -2.99%   | 68.46%             | -18.89% |    -0.05 |       62 | 39.77%     | ok               |
|          45 | -2.90%   | 68.46%             | -15.40% |    -0.05 |       52 | 36.61%     | ok               |
|          25 | -4.72%   | 68.46%             | -25.58% |    -0.09 |       59 | 45.42%     | ok               |

## INJ-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 0.44%    | -72.72%            | -57.50% |     0.19 |       50 | 22.80%     | ok               |
|          35 | -14.32%  | -72.72%            | -65.08% |     0.06 |       66 | 32.95%     | ok               |
|          50 | -14.98%  | -72.72%            | -52.76% |    -0.05 |       52 | 19.16%     | ok               |
|          40 | -24.07%  | -72.72%            | -65.15% |    -0.11 |       54 | 29.12%     | ok               |
|          20 | -45.58%  | -72.72%            | -80.74% |    -0.28 |       83 | 47.70%     | ok               |

## INTC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 98.19%   | 154.94%            | -53.65% |     0.8  |       84 | 62.06%     | ok               |
|          25 | 94.25%   | 154.94%            | -56.41% |     0.8  |       75 | 52.25%     | ok               |
|          20 | 91.15%   | 154.94%            | -52.47% |     0.78 |       82 | 57.24%     | ok               |
|          40 | 79.73%   | 154.94%            | -55.86% |     0.75 |       68 | 39.43%     | ok               |
|          45 | 76.87%   | 154.94%            | -49.32% |     0.75 |       62 | 35.11%     | ok               |

## INTU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -1.36%   | -44.76%            | -42.41% |     0.09 |       69 | 28.62%     | ok               |
|          45 | -4.74%   | -44.76%            | -44.25% |     0.03 |       67 | 32.78%     | ok               |
|          15 | -9.50%   | -44.76%            | -47.30% |    -0.03 |       81 | 51.41%     | ok               |
|          25 | -11.92%  | -44.76%            | -42.24% |    -0.08 |       66 | 45.59%     | ok               |
|          40 | -11.09%  | -44.76%            | -48.32% |    -0.09 |       73 | 35.77%     | ok               |

## ITA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 8.73%    | 89.00%             | -21.48% |     0.35 |       72 | 35.44%     | ok               |
|          30 | 4.35%    | 89.00%             | -23.75% |     0.2  |       70 | 45.42%     | ok               |
|          35 | 1.66%    | 89.00%             | -23.16% |     0.12 |       74 | 43.59%     | ok               |
|          15 | 0.55%    | 89.00%             | -26.46% |     0.1  |       89 | 58.40%     | ok               |
|          40 | 0.49%    | 89.00%             | -20.58% |     0.08 |       76 | 40.10%     | ok               |

## IWM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 9.94%    | 49.65%             | -12.83% |     0.4  |       50 | 36.77%     | ok               |
|          25 | 8.91%    | 49.65%             | -14.80% |     0.36 |       52 | 38.44%     | ok               |
|          35 | 7.46%    | 49.65%             | -14.41% |     0.33 |       50 | 34.44%     | ok               |
|          40 | 6.82%    | 49.65%             | -14.38% |     0.32 |       44 | 31.95%     | ok               |
|          20 | 3.62%    | 49.65%             | -15.32% |     0.18 |       64 | 39.60%     | ok               |

## JNJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 15.67%   | 41.44%             | -11.39% |     0.69 |       62 | 38.27%     | ok               |
|          15 | 10.62%   | 41.44%             | -18.02% |     0.4  |       72 | 58.24%     | ok               |
|          20 | 7.87%    | 41.44%             | -17.61% |     0.33 |       76 | 54.74%     | ok               |
|          45 | 6.05%    | 41.44%             | -15.23% |     0.3  |       64 | 43.26%     | ok               |
|          40 | 4.54%    | 41.44%             | -14.77% |     0.23 |       70 | 47.59%     | ok               |

## JPM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 11.63%   | 72.30%             | -14.65% |     0.44 |       56 | 40.27%     | ok               |
|          45 | 1.99%    | 72.30%             | -20.75% |     0.13 |       56 | 43.43%     | ok               |
|          40 | -10.10%  | 72.30%             | -26.28% |    -0.24 |       66 | 45.76%     | ok               |
|          20 | -15.42%  | 72.30%             | -32.10% |    -0.28 |       84 | 57.40%     | ok               |
|          35 | -15.12%  | 72.30%             | -25.21% |    -0.37 |       72 | 49.42%     | ok               |

## KO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 24.89%   | 33.48%             | -8.07%  |     0.93 |       49 | 37.10%     | ok               |
|          35 | 20.50%   | 33.48%             | -8.07%  |     0.8  |       52 | 35.94%     | ok               |
|          50 | 17.33%   | 33.48%             | -11.40% |     0.79 |       34 | 26.62%     | ok               |
|          25 | 20.08%   | 33.48%             | -9.33%  |     0.77 |       55 | 39.60%     | ok               |
|          40 | 18.07%   | 33.48%             | -9.28%  |     0.77 |       54 | 32.95%     | ok               |

## LDO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -4.49%   | -83.73%            | -44.15% |     0.28 |       88 | 50.19%     | ok               |
|          20 | -3.24%   | -83.73%            | -43.71% |     0.28 |       91 | 45.40%     | ok               |
|          30 | -15.09%  | -83.73%            | -58.32% |     0.13 |       78 | 35.82%     | ok               |
|          25 | -27.47%  | -83.73%            | -54.15% |     0.02 |       87 | 41.38%     | ok               |
|          50 | -11.65%  | -83.73%            | -48.77% |    -0.01 |       44 | 15.90%     | ok               |

## LIN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 3.30%    | 22.34%             | -23.70% |     0.17 |       68 | 50.25%     | ok               |
|          25 | 1.46%    | 22.34%             | -22.01% |     0.11 |       68 | 41.93%     | ok               |
|          20 | -0.71%   | 22.34%             | -23.00% |     0.04 |       67 | 45.09%     | ok               |
|          35 | -2.45%   | 22.34%             | -21.18% |    -0.04 |       68 | 32.78%     | ok               |
|          30 | -3.07%   | 22.34%             | -21.53% |    -0.05 |       72 | 39.27%     | ok               |

## LINK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -18.89%  | -65.04%            | -55.61% |     0.03 |       70 | 39.85%     | ok               |
|          50 | -22.09%  | -65.04%            | -42.26% |    -0.11 |       36 | 20.11%     | ok               |
|          45 | -25.48%  | -65.04%            | -43.89% |    -0.13 |       46 | 24.33%     | ok               |
|          35 | -32.41%  | -65.04%            | -53.72% |    -0.17 |       60 | 34.48%     | ok               |
|          25 | -43.87%  | -65.04%            | -56.54% |    -0.27 |       66 | 45.40%     | ok               |

## LLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 27.35%   | 77.59%             | -38.23% |     0.57 |       42 | 38.94%     | ok               |
|          45 | 15.14%   | 77.59%             | -42.66% |     0.37 |       50 | 42.10%     | ok               |
|          15 | 8.58%    | 77.59%             | -48.12% |     0.27 |       63 | 61.56%     | ok               |
|          40 | -2.08%   | 77.59%             | -46.23% |     0.09 |       62 | 44.59%     | ok               |
|          20 | -8.90%   | 77.59%             | -51.34% |    -0.01 |       72 | 56.57%     | ok               |

## LRCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 12.61%   | 338.11%            | -60.45% |     0.32 |       81 | 56.07%     | ok               |
|          50 | 0.69%    | 338.11%            | -50.39% |     0.15 |       76 | 36.61%     | ok               |
|          40 | -9.55%   | 338.11%            | -56.86% |     0.02 |       74 | 42.60%     | ok               |
|          35 | -12.11%  | 338.11%            | -61.76% |    -0.01 |       82 | 45.26%     | ok               |
|          20 | -14.66%  | 338.11%            | -67.64% |    -0.03 |       89 | 51.25%     | ok               |

## LTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -30.22%  | -52.37%            | -47.47% |    -0.32 |       56 | 30.46%     | ok               |
|          35 | -36.79%  | -52.37%            | -56.94% |    -0.39 |       68 | 40.61%     | ok               |
|          50 | -32.64%  | -52.37%            | -48.91% |    -0.4  |       52 | 24.52%     | ok               |
|          30 | -45.14%  | -52.37%            | -55.04% |    -0.52 |       67 | 45.98%     | ok               |
|          25 | -47.45%  | -52.37%            | -55.83% |    -0.55 |       75 | 48.47%     | ok               |

## MCD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 2.92%    | -3.38%             | -9.22%  |     0.19 |       44 | 20.47%     | ok               |
|          30 | -0.67%   | -3.38%             | -19.14% |     0.03 |       75 | 39.27%     | ok               |
|          25 | -2.03%   | -3.38%             | -20.78% |    -0.02 |       75 | 41.76%     | ok               |
|          40 | -6.24%   | -3.38%             | -16.86% |    -0.24 |       73 | 29.78%     | ok               |
|          35 | -7.87%   | -3.38%             | -15.80% |    -0.29 |       71 | 35.77%     | ok               |

## META Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 21.42%   | 77.60%             | -31.03% |     0.44 |       68 | 42.10%     | ok               |
|          40 | 8.07%    | 77.60%             | -35.11% |     0.25 |       68 | 45.09%     | ok               |
|          25 | 5.99%    | 77.60%             | -34.54% |     0.22 |       67 | 55.41%     | ok               |
|          30 | 3.15%    | 77.60%             | -33.58% |     0.18 |       72 | 52.25%     | ok               |
|          50 | 2.89%    | 77.60%             | -34.00% |     0.17 |       72 | 38.27%     | ok               |

## MPC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 14.51%   | 63.84%             | -23.96% |     0.37 |       52 | 38.60%     | ok               |
|          45 | 7.75%    | 63.84%             | -25.09% |     0.25 |       58 | 42.26%     | ok               |
|          40 | 6.12%    | 63.84%             | -25.70% |     0.22 |       60 | 44.59%     | ok               |
|          35 | 2.83%    | 63.84%             | -35.90% |     0.17 |       68 | 47.09%     | ok               |
|          30 | -13.34%  | 63.84%             | -44.76% |    -0.13 |       71 | 49.92%     | ok               |

## MRK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -11.86%  | 1.32%              | -29.91% |    -0.17 |       85 | 57.74%     | ok               |
|          25 | -11.44%  | 1.32%              | -31.07% |    -0.18 |       70 | 49.75%     | ok               |
|          20 | -15.78%  | 1.32%              | -29.38% |    -0.29 |       75 | 53.08%     | ok               |
|          35 | -17.22%  | 1.32%              | -30.50% |    -0.35 |       67 | 43.59%     | ok               |
|          30 | -17.84%  | 1.32%              | -32.14% |    -0.36 |       67 | 47.09%     | ok               |

## MS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -2.45%   | 121.84%            | -19.61% |     0.01 |       70 | 38.77%     | ok               |
|          35 | -10.96%  | 121.84%            | -21.83% |    -0.21 |       74 | 43.93%     | ok               |
|          50 | -10.06%  | 121.84%            | -15.66% |    -0.3  |       58 | 30.45%     | ok               |
|          20 | -16.57%  | 121.84%            | -25.68% |    -0.33 |       84 | 52.58%     | ok               |
|          30 | -16.73%  | 121.84%            | -26.72% |    -0.36 |       81 | 47.75%     | ok               |

## MSFT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -9.69%   | 20.54%             | -25.28% |    -0.24 |       58 | 34.94%     | ok               |
|          50 | -13.45%  | 20.54%             | -28.69% |    -0.38 |       56 | 30.62%     | ok               |
|          35 | -22.64%  | 20.54%             | -30.52% |    -0.58 |       67 | 43.26%     | ok               |
|          40 | -23.56%  | 20.54%             | -32.42% |    -0.64 |       63 | 38.27%     | ok               |
|          25 | -26.35%  | 20.54%             | -31.00% |    -0.64 |       80 | 50.58%     | ok               |

## MU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 343.56%  | 1058.15%           | -61.96% |     1.48 |       50 | 66.89%     | ok               |
|          25 | 259.62%  | 1058.15%           | -67.90% |     1.36 |       53 | 60.40%     | ok               |
|          40 | 220.77%  | 1058.15%           | -64.36% |     1.29 |       60 | 54.08%     | ok               |
|          20 | 229.25%  | 1058.15%           | -67.25% |     1.27 |       59 | 62.56%     | ok               |
|          30 | 206.33%  | 1058.15%           | -68.76% |     1.23 |       55 | 58.57%     | ok               |

## NEAR-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 110.22%  | -55.82%            | -44.39% |     1.01 |       48 | 26.05%     | ok               |
|          40 | 79.22%   | -55.82%            | -53.32% |     0.83 |       48 | 30.08%     | ok               |
|          50 | 69.73%   | -55.82%            | -49.90% |     0.8  |       46 | 20.88%     | ok               |
|          35 | 42.27%   | -55.82%            | -58.99% |     0.59 |       70 | 35.06%     | ok               |
|          30 | 14.59%   | -55.82%            | -60.07% |     0.39 |       89 | 43.30%     | ok               |

## NEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 30.17%   | 172.88%            | -25.79% |     0.49 |       60 | 63.73%     | ok               |
|          20 | 16.24%   | 172.88%            | -30.47% |     0.36 |       70 | 59.23%     | ok               |
|          25 | -2.49%   | 172.88%            | -30.80% |     0.13 |       66 | 57.24%     | ok               |
|          30 | -19.45%  | 172.88%            | -38.49% |    -0.12 |       70 | 55.74%     | ok               |
|          35 | -19.14%  | 172.88%            | -39.55% |    -0.12 |       77 | 52.91%     | ok               |

## NFLX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 43.82%   | 80.83%             | -11.94% |     0.97 |       48 | 47.09%     | ok               |
|          50 | 37.40%   | 80.83%             | -16.28% |     0.92 |       50 | 39.10%     | ok               |
|          35 | 39.59%   | 80.83%             | -18.30% |     0.85 |       62 | 50.75%     | ok               |
|          45 | 30.35%   | 80.83%             | -15.48% |     0.75 |       56 | 43.09%     | ok               |
|          25 | 32.27%   | 80.83%             | -21.09% |     0.7  |       60 | 57.74%     | ok               |

## NKE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -27.12%  | -54.38%            | -42.13% |    -0.38 |       77 | 39.27%     | ok               |
|          20 | -35.31%  | -54.38%            | -50.44% |    -0.45 |       97 | 54.91%     | ok               |
|          25 | -36.70%  | -54.38%            | -51.20% |    -0.49 |       95 | 51.08%     | ok               |
|          15 | -38.56%  | -54.38%            | -55.28% |    -0.51 |       98 | 59.57%     | ok               |
|          30 | -37.52%  | -54.38%            | -55.35% |    -0.52 |       93 | 45.76%     | ok               |

## NOW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 40.43%   | -9.96%             | -26.36% |     0.62 |       77 | 51.25%     | ok               |
|          15 | 31.09%   | -9.96%             | -27.25% |     0.52 |       86 | 54.41%     | ok               |
|          25 | 29.64%   | -9.96%             | -26.83% |     0.51 |       72 | 48.75%     | ok               |
|          35 | 26.03%   | -9.96%             | -29.30% |     0.49 |       75 | 40.93%     | ok               |
|          40 | 20.43%   | -9.96%             | -30.87% |     0.43 |       64 | 36.27%     | ok               |

## NVDA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 3.36%    | 150.36%            | -33.22% |     0.22 |       66 | 53.12%     | ok               |
|          30 | 1.42%    | 150.36%            | -35.26% |     0.18 |       68 | 50.80%     | ok               |
|          20 | -3.50%   | 150.36%            | -40.59% |     0.14 |       69 | 57.58%     | ok               |
|          35 | -10.46%  | 150.36%            | -41.25% |     0    |       80 | 47.95%     | ok               |
|          50 | -11.03%  | 150.36%            | -40.84% |    -0.03 |       60 | 35.29%     | ok               |

## OP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 41.49%   | -94.02%            | -60.08% |     0.6  |       50 | 25.67%     | ok               |
|          50 | 30.16%   | -94.02%            | -36.11% |     0.53 |       36 | 12.64%     | ok               |
|          45 | 17.45%   | -94.02%            | -53.32% |     0.39 |       42 | 17.62%     | ok               |
|          35 | 14.53%   | -94.02%            | -63.95% |     0.37 |       55 | 28.54%     | ok               |
|          30 | -2.73%   | -94.02%            | -70.11% |     0.21 |       75 | 34.48%     | ok               |

## ORCL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 178.36%  | 113.43%            | -21.44% |     1.23 |       73 | 64.23%     | ok               |
|          25 | 110.94%  | 113.43%            | -24.79% |     0.96 |       72 | 56.24%     | ok               |
|          20 | 110.78%  | 113.43%            | -22.81% |     0.96 |       76 | 59.73%     | ok               |
|          35 | 70.57%   | 113.43%            | -31.95% |     0.76 |       62 | 47.59%     | ok               |
|          45 | 66.35%   | 113.43%            | -25.84% |     0.75 |       58 | 39.93%     | ok               |

## OXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 2.99%    | -4.10%             | -29.57% |     0.16 |       36 | 28.62%     | ok               |
|          30 | 0.50%    | -4.10%             | -31.01% |     0.13 |       71 | 44.26%     | ok               |
|          35 | 0.47%    | -4.10%             | -30.16% |     0.12 |       68 | 38.94%     | ok               |
|          40 | -1.69%   | -4.10%             | -31.66% |     0.07 |       54 | 34.78%     | ok               |
|          45 | -6.26%   | -4.10%             | -34.84% |    -0.03 |       42 | 30.45%     | ok               |

## PEP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 8.79%    | -14.69%            | -11.62% |     0.41 |       44 | 27.95%     | ok               |
|          45 | -1.68%   | -14.69%            | -14.22% |    -0.02 |       66 | 32.78%     | ok               |
|          40 | -4.81%   | -14.69%            | -18.04% |    -0.13 |       78 | 37.94%     | ok               |
|          35 | -7.06%   | -14.69%            | -21.42% |    -0.17 |       89 | 42.60%     | ok               |
|          30 | -11.56%  | -14.69%            | -21.35% |    -0.29 |       83 | 48.42%     | ok               |

## PEPE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -9.56%   | -82.58%            | -57.66% |     0.18 |       79 | 41.57%     | ok               |
|          35 | -15.63%  | -82.58%            | -51.35% |     0.08 |       64 | 36.40%     | ok               |
|          25 | -31.82%  | -82.58%            | -62.34% |    -0.05 |       89 | 47.13%     | ok               |
|          50 | -24.04%  | -82.58%            | -39.66% |    -0.11 |       50 | 21.84%     | ok               |
|          15 | -48.20%  | -82.58%            | -73.26% |    -0.13 |       88 | 57.66%     | ok               |

## PFE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -24.03%  | -11.71%            | -27.99% |    -0.84 |       52 | 21.30%     | ok               |
|          35 | -31.86%  | -11.71%            | -36.39% |    -1    |       82 | 33.61%     | ok               |
|          50 | -26.33%  | -11.71%            | -29.22% |    -1.03 |       44 | 17.47%     | ok               |
|          40 | -30.46%  | -11.71%            | -34.09% |    -1.04 |       76 | 26.12%     | ok               |
|          30 | -38.05%  | -11.71%            | -42.29% |    -1.18 |       77 | 37.27%     | ok               |

## PG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -4.32%   | -2.08%             | -19.77% |    -0.14 |       56 | 33.94%     | ok               |
|          35 | -4.99%   | -2.08%             | -18.66% |    -0.16 |       60 | 37.77%     | ok               |
|          30 | -9.37%   | -2.08%             | -20.33% |    -0.34 |       61 | 40.43%     | ok               |
|          25 | -10.46%  | -2.08%             | -20.01% |    -0.38 |       71 | 41.60%     | ok               |
|          45 | -15.02%  | -2.08%             | -20.33% |    -0.68 |       56 | 30.95%     | ok               |

## PM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 3.42%    | 85.19%             | -31.89% |     0.17 |       89 | 61.90%     | ok               |
|          30 | 3.14%    | 85.19%             | -33.68% |     0.16 |       83 | 56.91%     | ok               |
|          35 | 2.43%    | 85.19%             | -32.20% |     0.15 |       86 | 53.24%     | ok               |
|          25 | -3.97%   | 85.19%             | -37.05% |     0.01 |       83 | 59.23%     | ok               |
|          50 | -3.76%   | 85.19%             | -35.70% |    -0.01 |       78 | 43.43%     | ok               |

## POL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 57.24%   | -83.39%            | -46.45% |     0.72 |       78 | 47.70%     | ok               |
|          20 | 47.81%   | -83.39%            | -52.88% |     0.63 |       78 | 62.26%     | ok               |
|          25 | 39.16%   | -83.39%            | -46.72% |     0.57 |       70 | 56.51%     | ok               |
|          50 | 16.81%   | -83.39%            | -22.46% |     0.4  |       56 | 20.50%     | ok               |
|          15 | 15.37%   | -83.39%            | -58.42% |     0.39 |       77 | 68.58%     | ok               |

## QCOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 18.26%   | 83.09%             | -55.66% |     0.38 |       75 | 50.58%     | ok               |
|          20 | 17.16%   | 83.09%             | -57.05% |     0.36 |       72 | 53.41%     | ok               |
|          35 | 10.68%   | 83.09%             | -51.84% |     0.29 |       87 | 45.76%     | ok               |
|          15 | -2.31%   | 83.09%             | -60.40% |     0.14 |       76 | 56.57%     | ok               |
|          30 | -1.41%   | 83.09%             | -57.69% |     0.14 |       81 | 48.42%     | ok               |

## QQQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 28.19%   | 85.85%             | -12.88% |     0.74 |       57 | 48.92%     | ok               |
|          20 | 27.64%   | 85.85%             | -12.98% |     0.7  |       65 | 51.41%     | ok               |
|          15 | 27.56%   | 85.85%             | -14.17% |     0.68 |       65 | 54.08%     | ok               |
|          30 | 24.00%   | 85.85%             | -12.88% |     0.67 |       60 | 46.09%     | ok               |
|          35 | 11.33%   | 85.85%             | -19.00% |     0.39 |       66 | 42.43%     | ok               |

## RENDER-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 68.17%   | -52.28%            | -43.43% |     0.77 |       80 | 55.51%     | ok               |
|          15 | 48.64%   | -52.28%            | -44.59% |     0.66 |       80 | 58.75%     | ok               |
|          25 | 34.84%   | -52.28%            | -40.60% |     0.57 |       84 | 51.40%     | ok               |
|          30 | -7.44%   | -52.28%            | -45.00% |     0.22 |       92 | 44.71%     | ok               |
|          40 | -17.84%  | -52.28%            | -38.60% |     0.02 |       66 | 29.59%     | ok               |

## RTX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 26.40%   | 108.94%            | -18.66% |     0.66 |       76 | 57.24%     | ok               |
|          25 | 21.68%   | 108.94%            | -18.59% |     0.57 |       64 | 53.91%     | ok               |
|          50 | 15.99%   | 108.94%            | -18.42% |     0.53 |       60 | 42.26%     | ok               |
|          30 | 19.25%   | 108.94%            | -16.99% |     0.52 |       58 | 52.58%     | ok               |
|          35 | 16.66%   | 108.94%            | -18.00% |     0.52 |       54 | 50.58%     | ok               |

## SBUX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -14.68%  | 7.07%              | -23.55% |    -0.23 |       62 | 42.93%     | ok               |
|          45 | -16.40%  | 7.07%              | -27.26% |    -0.36 |       70 | 29.78%     | ok               |
|          40 | -19.36%  | 7.07%              | -27.13% |    -0.42 |       68 | 33.44%     | ok               |
|          30 | -23.57%  | 7.07%              | -31.15% |    -0.48 |       65 | 40.77%     | ok               |
|          20 | -26.43%  | 7.07%              | -34.48% |    -0.49 |       67 | 44.93%     | ok               |

## SCHW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 2.81%    | 29.11%             | -15.92% |     0.15 |       52 | 33.11%     | ok               |
|          50 | -2.36%   | 29.11%             | -12.59% |    -0.02 |       48 | 30.78%     | ok               |
|          40 | -7.85%   | 29.11%             | -21.81% |    -0.15 |       60 | 36.11%     | ok               |
|          25 | -10.93%  | 29.11%             | -28.76% |    -0.18 |       63 | 48.09%     | ok               |
|          20 | -12.59%  | 29.11%             | -29.24% |    -0.22 |       71 | 50.75%     | ok               |

## SHIB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -13.06%  | -77.26%            | -49.21% |     0.11 |       82 | 67.24%     | ok               |
|          20 | -25.63%  | -77.26%            | -48.69% |    -0.06 |       83 | 62.64%     | ok               |
|          25 | -27.58%  | -77.26%            | -43.85% |    -0.1  |       81 | 57.28%     | ok               |
|          30 | -38.38%  | -77.26%            | -48.95% |    -0.32 |       78 | 49.81%     | ok               |
|          35 | -37.56%  | -77.26%            | -55.49% |    -0.35 |       68 | 43.49%     | ok               |

## SHY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          30 | -1.95%   | 0.51%              | -2.85% |    -0.66 |       50 | 37.27%     | ok               |
|          35 | -2.07%   | 0.51%              | -3.27% |    -0.7  |       52 | 35.44%     | ok               |
|          40 | -2.19%   | 0.51%              | -3.33% |    -0.75 |       52 | 33.61%     | ok               |
|          45 | -2.16%   | 0.51%              | -3.23% |    -0.76 |       50 | 30.45%     | ok               |
|          50 | -2.34%   | 0.51%              | -3.40% |    -0.86 |       46 | 27.62%     | ok               |

## SKY-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -25.11%  | 13.12%             | -43.98% |    -0.31 |       64 | 39.66%     | ok               |
|          25 | -30.60%  | 13.12%             | -48.09% |    -0.42 |       61 | 43.35%     | ok               |
|          15 | -36.85%  | 13.12%             | -56.39% |    -0.49 |       56 | 49.51%     | ok               |
|          20 | -41.77%  | 13.12%             | -58.40% |    -0.64 |       58 | 47.04%     | ok               |
|          35 | -40.17%  | 13.12%             | -49.68% |    -0.79 |       58 | 33.50%     | ok               |

## SLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 11.63%   | 6.17%              | -23.33% |     0.33 |       50 | 37.27%     | ok               |
|          45 | 6.27%    | 6.17%              | -20.73% |     0.23 |       56 | 33.78%     | ok               |
|          35 | -16.40%  | 6.17%              | -42.01% |    -0.23 |       78 | 45.26%     | ok               |
|          50 | -17.63%  | 6.17%              | -32.46% |    -0.36 |       58 | 29.95%     | ok               |
|          30 | -29.41%  | 6.17%              | -54.23% |    -0.51 |       77 | 51.91%     | ok               |

## SLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 67.27%   | 223.57%            | -29.75% |     0.86 |       60 | 36.27%     | ok               |
|          45 | 62.01%   | 223.57%            | -31.82% |     0.82 |       54 | 34.44%     | ok               |
|          50 | 57.25%   | 223.57%            | -34.10% |     0.78 |       52 | 33.61%     | ok               |
|          35 | 54.63%   | 223.57%            | -36.89% |     0.75 |       62 | 38.60%     | ok               |
|          30 | 36.93%   | 223.57%            | -42.66% |     0.58 |       58 | 40.60%     | ok               |

## SMH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 119.66%  | 261.75%            | -30.17% |     1.34 |       49 | 54.74%     | ok               |
|          35 | 89.86%   | 261.75%            | -34.36% |     1.16 |       56 | 50.42%     | ok               |
|          25 | 89.73%   | 261.75%            | -32.94% |     1.14 |       48 | 53.41%     | ok               |
|          30 | 87.49%   | 261.75%            | -33.99% |     1.13 |       50 | 51.75%     | ok               |
|          15 | 86.62%   | 261.75%            | -32.34% |     1.07 |       57 | 56.74%     | ok               |

## SNX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 28.04%   | -86.45%            | -28.28% |     0.49 |       64 | 30.27%     | ok               |
|          30 | 7.46%    | -86.45%            | -32.91% |     0.31 |       65 | 37.93%     | ok               |
|          20 | -8.97%   | -86.45%            | -43.20% |     0.19 |       76 | 49.62%     | ok               |
|          25 | -17.94%  | -86.45%            | -35.81% |     0.06 |       78 | 42.53%     | ok               |
|          40 | -12.57%  | -86.45%            | -30.74% |     0.02 |       54 | 24.90%     | ok               |

## SOL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -33.54%  | -58.97%            | -59.95% |    -0.19 |       64 | 37.55%     | ok               |
|          25 | -40.63%  | -58.97%            | -53.71% |    -0.22 |       74 | 55.56%     | ok               |
|          15 | -44.14%  | -58.97%            | -59.14% |    -0.24 |       80 | 63.98%     | ok               |
|          35 | -43.48%  | -58.97%            | -62.37% |    -0.3  |       72 | 45.02%     | ok               |
|          20 | -51.20%  | -58.97%            | -58.01% |    -0.38 |       72 | 58.43%     | ok               |

## SOXX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 96.07%   | 215.17%            | -38.67% |     1.14 |       55 | 53.58%     | ok               |
|          15 | 91.15%   | 215.17%            | -37.72% |     1.07 |       68 | 56.41%     | ok               |
|          25 | 86.25%   | 215.17%            | -39.85% |     1.07 |       53 | 53.08%     | ok               |
|          35 | 77.65%   | 215.17%            | -38.63% |     1.01 |       65 | 48.09%     | ok               |
|          30 | 75.79%   | 215.17%            | -40.34% |     0.98 |       57 | 50.92%     | ok               |

## SPY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 22.77%   | 61.60%             | -14.25% |     0.75 |       58 | 54.08%     | ok               |
|          15 | 21.98%   | 61.60%             | -16.80% |     0.71 |       63 | 56.91%     | ok               |
|          25 | 14.07%   | 61.60%             | -15.22% |     0.51 |       58 | 53.24%     | ok               |
|          30 | 9.95%    | 61.60%             | -16.47% |     0.4  |       60 | 50.75%     | ok               |
|          35 | 6.59%    | 61.60%             | -16.72% |     0.29 |       60 | 48.25%     | ok               |

## SUSHI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -24.33%  | -88.50%            | -35.74% |    -0.19 |       50 | 14.75%     | ok               |
|          40 | -57.06%  | -88.50%            | -67.87% |    -0.67 |       59 | 23.75%     | ok               |
|          35 | -60.35%  | -88.50%            | -74.04% |    -0.72 |       77 | 28.54%     | ok               |
|          45 | -57.00%  | -88.50%            | -64.69% |    -0.72 |       50 | 17.43%     | ok               |
|          15 | -77.12%  | -88.50%            | -80.65% |    -0.91 |       87 | 46.55%     | ok               |

## T Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 32.30%   | 41.76%             | -18.13% |     0.75 |       61 | 53.91%     | ok               |
|          25 | 25.89%   | 41.76%             | -17.66% |     0.65 |       64 | 51.41%     | ok               |
|          15 | 25.07%   | 41.76%             | -15.08% |     0.61 |       70 | 57.74%     | ok               |
|          35 | 15.20%   | 41.76%             | -14.49% |     0.45 |       64 | 46.26%     | ok               |
|          30 | 14.54%   | 41.76%             | -17.01% |     0.42 |       64 | 49.42%     | ok               |

## TGT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -7.68%   | -10.27%            | -41.89% |    -0.04 |       81 | 47.09%     | ok               |
|          15 | -10.70%  | -10.27%            | -39.76% |    -0.09 |       71 | 51.58%     | ok               |
|          25 | -9.23%   | -10.27%            | -42.39% |    -0.09 |       63 | 41.93%     | ok               |
|          45 | -8.65%   | -10.27%            | -29.07% |    -0.12 |       52 | 29.12%     | ok               |
|          30 | -10.11%  | -10.27%            | -40.57% |    -0.12 |       58 | 39.27%     | ok               |

## TIA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 64.91%   | -92.36%            | -32.94% |     0.75 |       58 | 29.69%     | ok               |
|          40 | 53.68%   | -92.36%            | -34.27% |     0.68 |       60 | 25.86%     | ok               |
|          45 | 33.66%   | -92.36%            | -35.29% |     0.55 |       58 | 19.35%     | ok               |
|          50 | 18.25%   | -92.36%            | -41.31% |     0.42 |       38 | 11.69%     | ok               |
|          15 | -5.25%   | -92.36%            | -40.88% |     0.27 |       95 | 50.96%     | ok               |

## TLT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -18.28%  | -10.90%            | -20.35% |    -1.65 |       60 | 22.30%     | ok               |
|          30 | -22.73%  | -10.90%            | -24.69% |    -1.65 |       70 | 33.44%     | ok               |
|          50 | -16.26%  | -10.90%            | -18.15% |    -1.78 |       36 | 15.14%     | ok               |
|          45 | -17.99%  | -10.90%            | -19.60% |    -1.81 |       42 | 17.97%     | ok               |
|          35 | -22.23%  | -10.90%            | -24.20% |    -1.82 |       68 | 27.45%     | ok               |

## TMO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 51.23%   | -7.86%             | -12.29% |     1.07 |       46 | 35.44%     | ok               |
|          40 | 49.15%   | -7.86%             | -12.07% |     1.02 |       51 | 40.43%     | ok               |
|          50 | 43.47%   | -7.86%             | -10.55% |     0.99 |       36 | 30.12%     | ok               |
|          35 | 35.24%   | -7.86%             | -16.12% |     0.77 |       63 | 45.26%     | ok               |
|          30 | 25.18%   | -7.86%             | -16.83% |     0.58 |       59 | 50.25%     | ok               |

## TMUS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 21.16%   | 14.26%             | -26.87% |     0.51 |       67 | 60.90%     | ok               |
|          30 | 19.70%   | 14.26%             | -24.50% |     0.49 |       68 | 49.25%     | ok               |
|          20 | 13.72%   | 14.26%             | -24.82% |     0.38 |       69 | 55.24%     | ok               |
|          25 | 12.59%   | 14.26%             | -25.91% |     0.36 |       73 | 51.58%     | ok               |
|          50 | 8.75%    | 14.26%             | -18.84% |     0.31 |       58 | 37.10%     | ok               |

## TRX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -2.64%   | 35.01%             | -22.90% |     0.03 |       70 | 49.23%     | ok               |
|          35 | -3.97%   | 35.01%             | -21.77% |    -0.01 |       66 | 46.55%     | ok               |
|          25 | -4.39%   | 35.01%             | -26.84% |    -0.02 |       66 | 52.49%     | ok               |
|          40 | -3.78%   | 35.01%             | -22.27% |    -0.02 |       52 | 38.51%     | ok               |
|          50 | -6.77%   | 35.01%             | -21.14% |    -0.13 |       46 | 33.14%     | ok               |

## TSLA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 100.17%  | 81.56%             | -32.60% |     1.02 |       64 | 31.78%     | ok               |
|          40 | 90.09%   | 81.56%             | -45.90% |     0.89 |       61 | 36.27%     | ok               |
|          45 | 61.04%   | 81.56%             | -46.86% |     0.72 |       65 | 33.61%     | ok               |
|          35 | 37.95%   | 81.56%             | -54.51% |     0.54 |       74 | 39.43%     | ok               |
|          30 | 12.01%   | 81.56%             | -57.89% |     0.32 |       68 | 43.93%     | ok               |

## TXN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 16.65%   | 88.62%             | -45.45% |     0.38 |       70 | 35.44%     | ok               |
|          20 | 7.76%    | 88.62%             | -38.98% |     0.25 |       66 | 60.07%     | ok               |
|          40 | 7.92%    | 88.62%             | -45.67% |     0.25 |       74 | 47.59%     | ok               |
|          35 | 7.70%    | 88.62%             | -43.38% |     0.25 |       78 | 49.92%     | ok               |
|          15 | 6.67%    | 88.62%             | -39.48% |     0.24 |       69 | 63.73%     | ok               |

## UNH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 23.39%   | -29.26%            | -37.02% |     0.46 |       52 | 29.12%     | ok               |
|          30 | 15.29%   | -29.26%            | -32.80% |     0.35 |       78 | 52.25%     | ok               |
|          35 | 11.87%   | -29.26%            | -34.05% |     0.31 |       70 | 47.25%     | ok               |
|          15 | 10.23%   | -29.26%            | -36.80% |     0.29 |       77 | 67.05%     | ok               |
|          40 | 7.76%    | -29.26%            | -39.28% |     0.26 |       66 | 41.43%     | ok               |

## UNI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -11.27%  | -79.55%            | -53.40% |     0.09 |       50 | 23.18%     | ok               |
|          50 | -16.75%  | -79.55%            | -50.59% |    -0    |       46 | 19.73%     | ok               |
|          40 | -24.11%  | -79.55%            | -60.60% |    -0.06 |       54 | 27.59%     | ok               |
|          35 | -34.32%  | -79.55%            | -65.80% |    -0.16 |       72 | 32.18%     | ok               |
|          20 | -73.61%  | -79.55%            | -80.81% |    -0.79 |      101 | 49.43%     | ok               |

## UPS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -35.62%  | -33.41%            | -42.25% |    -0.71 |       74 | 42.43%     | ok               |
|          35 | -34.55%  | -33.41%            | -40.47% |    -0.72 |       59 | 32.11%     | ok               |
|          20 | -36.70%  | -33.41%            | -45.77% |    -0.72 |       80 | 45.59%     | ok               |
|          30 | -36.95%  | -33.41%            | -40.62% |    -0.77 |       66 | 37.77%     | ok               |
|          40 | -35.85%  | -33.41%            | -42.12% |    -0.78 |       51 | 26.96%     | ok               |

## USO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 8.31%    | 86.12%             | -35.12% |     0.26 |       50 | 26.79%     | ok               |
|          30 | 2.80%    | 86.12%             | -43.35% |     0.17 |       68 | 34.44%     | ok               |
|          25 | 1.57%    | 86.12%             | -43.43% |     0.16 |       70 | 37.44%     | ok               |
|          20 | 0.27%    | 86.12%             | -44.16% |     0.14 |       74 | 39.43%     | ok               |
|          40 | -1.01%   | 86.12%             | -41.14% |     0.11 |       61 | 29.62%     | ok               |

## VEA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 4.85%    | 52.85%             | -17.55% |     0.23 |       64 | 50.42%     | ok               |
|          20 | 1.26%    | 52.85%             | -18.44% |     0.1  |       63 | 47.92%     | ok               |
|          25 | -2.41%   | 52.85%             | -19.11% |    -0.04 |       59 | 45.92%     | ok               |
|          30 | -2.87%   | 52.85%             | -19.49% |    -0.07 |       60 | 43.43%     | ok               |
|          35 | -4.16%   | 52.85%             | -18.54% |    -0.12 |       56 | 42.26%     | ok               |

## VIXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -46.17%  | -62.20%            | -68.69% |    -0.39 |       44 | 10.32%     | ok               |
|          45 | -53.84%  | -62.20%            | -74.12% |    -0.51 |       54 | 15.47%     | ok               |
|          40 | -63.34%  | -62.20%            | -79.44% |    -0.64 |       68 | 19.47%     | ok               |
|          35 | -67.18%  | -62.20%            | -83.87% |    -0.68 |       84 | 24.63%     | ok               |
|          15 | -77.08%  | -62.20%            | -89.47% |    -0.79 |       97 | 41.93%     | ok               |

## VNQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -8.60%   | 10.67%             | -19.07% |    -0.37 |       60 | 28.62%     | ok               |
|          50 | -9.03%   | 10.67%             | -17.13% |    -0.41 |       56 | 26.12%     | ok               |
|          25 | -15.75%  | 10.67%             | -22.16% |    -0.61 |       76 | 41.76%     | ok               |
|          40 | -14.13%  | 10.67%             | -24.84% |    -0.62 |       74 | 32.11%     | ok               |
|          15 | -19.94%  | 10.67%             | -24.74% |    -0.77 |       78 | 46.59%     | ok               |

## VTI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 19.24%   | 59.65%             | -13.96% |     0.65 |       62 | 55.74%     | ok               |
|          15 | 15.77%   | 59.65%             | -15.70% |     0.54 |       65 | 58.57%     | ok               |
|          25 | 8.02%    | 59.65%             | -16.10% |     0.33 |       60 | 54.08%     | ok               |
|          30 | 0.48%    | 59.65%             | -18.77% |     0.08 |       70 | 52.08%     | ok               |
|          35 | -2.05%   | 59.65%             | -21.19% |    -0.02 |       64 | 48.92%     | ok               |

## VWO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -7.30%   | 48.36%             | -21.18% |    -0.25 |       60 | 32.61%     | ok               |
|          15 | -9.03%   | 48.36%             | -24.01% |    -0.26 |       69 | 49.42%     | ok               |
|          20 | -10.06%  | 48.36%             | -26.14% |    -0.31 |       67 | 47.25%     | ok               |
|          40 | -8.98%   | 48.36%             | -23.57% |    -0.31 |       70 | 37.94%     | ok               |
|          45 | -9.11%   | 48.36%             | -23.26% |    -0.33 |       62 | 35.11%     | ok               |

## VZ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -2.86%   | 19.17%             | -16.98% |    -0.03 |       52 | 27.62%     | ok               |
|          45 | -9.56%   | 19.17%             | -20.38% |    -0.25 |       58 | 30.45%     | ok               |
|          35 | -13.38%  | 19.17%             | -24.68% |    -0.36 |       59 | 36.11%     | ok               |
|          25 | -16.62%  | 19.17%             | -28.84% |    -0.43 |       76 | 43.93%     | ok               |
|          40 | -17.86%  | 19.17%             | -26.72% |    -0.54 |       64 | 32.95%     | ok               |

## WFC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -2.27%   | 54.96%             | -18.29% |    -0.01 |       54 | 31.61%     | ok               |
|          35 | -10.82%  | 54.96%             | -23.06% |    -0.17 |       79 | 44.26%     | ok               |
|          45 | -9.25%   | 54.96%             | -23.40% |    -0.21 |       64 | 36.27%     | ok               |
|          20 | -20.05%  | 54.96%             | -27.90% |    -0.31 |       79 | 53.24%     | ok               |
|          40 | -15.89%  | 54.96%             | -24.26% |    -0.41 |       76 | 40.10%     | ok               |

## WIF-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 35.16%   | -91.03%            | -40.67% |     0.54 |       69 | 37.55%     | ok               |
|          15 | 32.84%   | -91.03%            | -46.21% |     0.53 |       76 | 40.42%     | ok               |
|          25 | -0.68%   | -91.03%            | -45.19% |     0.29 |       73 | 34.67%     | ok               |
|          50 | -3.56%   | -91.03%            | -31.17% |     0.11 |       32 | 10.92%     | ok               |
|          45 | -16.27%  | -91.03%            | -44.01% |    -0.06 |       40 | 13.22%     | ok               |

## WMT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 64.57%   | 120.32%            | -9.85%  |     1.63 |       34 | 45.92%     | ok               |
|          50 | 54.40%   | 120.32%            | -12.19% |     1.51 |       32 | 43.59%     | ok               |
|          35 | 60.43%   | 120.32%            | -9.90%  |     1.5  |       46 | 50.58%     | ok               |
|          40 | 57.57%   | 120.32%            | -9.99%  |     1.48 |       38 | 46.76%     | ok               |
|          30 | 38.75%   | 120.32%            | -21.31% |     0.99 |       53 | 53.24%     | ok               |

## XBI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 0.61%    | 52.08%             | -16.71% |     0.1  |       62 | 35.11%     | ok               |
|          45 | -0.16%   | 52.08%             | -16.88% |     0.08 |       54 | 31.95%     | ok               |
|          35 | -1.80%   | 52.08%             | -20.11% |     0.04 |       64 | 38.60%     | ok               |
|          30 | -3.68%   | 52.08%             | -20.48% |    -0    |       64 | 40.43%     | ok               |
|          50 | -6.10%   | 52.08%             | -16.83% |    -0.1  |       56 | 28.62%     | ok               |

## XLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 0.40%    | 22.15%             | -17.59% |     0.07 |       42 | 27.29%     | ok               |
|          40 | -1.80%   | 22.15%             | -19.67% |    -0.01 |       56 | 31.61%     | ok               |
|          45 | -2.15%   | 22.15%             | -19.78% |    -0.03 |       44 | 28.45%     | ok               |
|          35 | -5.03%   | 22.15%             | -22.65% |    -0.13 |       58 | 34.94%     | ok               |
|          25 | -10.74%  | 22.15%             | -23.63% |    -0.34 |       67 | 41.43%     | ok               |

## XLC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 21.96%   | 60.67%             | -12.33% |     0.71 |       63 | 57.24%     | ok               |
|          25 | 19.67%   | 60.67%             | -12.31% |     0.64 |       60 | 59.07%     | ok               |
|          40 | 15.87%   | 60.67%             | -13.38% |     0.58 |       66 | 49.92%     | ok               |
|          35 | 15.84%   | 60.67%             | -13.38% |     0.57 |       62 | 54.41%     | ok               |
|          20 | 11.25%   | 60.67%             | -13.37% |     0.39 |       68 | 61.73%     | ok               |

## XLE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.94%   | 32.95%             | -25.98% |     0.05 |       60 | 37.10%     | ok               |
|          35 | -3.18%   | 32.95%             | -31.51% |     0    |       71 | 44.59%     | ok               |
|          45 | -3.24%   | 32.95%             | -29.68% |    -0.02 |       64 | 39.60%     | ok               |
|          25 | -9.60%   | 32.95%             | -36.05% |    -0.16 |       89 | 50.08%     | ok               |
|          40 | -10.37%  | 32.95%             | -34.51% |    -0.22 |       70 | 42.26%     | ok               |

## XLF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -3.21%   | 36.78%             | -18.01% |    -0.05 |       68 | 56.24%     | ok               |
|          15 | -7.22%   | 36.78%             | -19.58% |    -0.18 |       76 | 59.07%     | ok               |
|          25 | -11.33%  | 36.78%             | -23.22% |    -0.36 |       77 | 52.58%     | ok               |
|          30 | -11.55%  | 36.78%             | -23.61% |    -0.38 |       76 | 49.92%     | ok               |
|          35 | -18.65%  | 36.78%             | -27.06% |    -0.74 |       66 | 45.76%     | ok               |

## XLI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 13.87%   | 55.44%             | -10.36% |     0.51 |       72 | 56.07%     | ok               |
|          20 | 7.98%    | 55.44%             | -12.74% |     0.34 |       65 | 50.58%     | ok               |
|          50 | 6.69%    | 55.44%             | -9.25%  |     0.34 |       58 | 35.77%     | ok               |
|          45 | 6.38%    | 55.44%             | -12.27% |     0.32 |       66 | 38.44%     | ok               |
|          30 | 5.61%    | 55.44%             | -11.38% |     0.27 |       66 | 48.09%     | ok               |

## XLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 106.75%  | 106.69%            | -14.75% |     1.64 |       41 | 54.08%     | ok               |
|          20 | 92.95%   | 106.69%            | -14.75% |     1.53 |       46 | 51.91%     | ok               |
|          25 | 84.69%   | 106.69%            | -14.75% |     1.48 |       40 | 49.92%     | ok               |
|          30 | 77.08%   | 106.69%            | -14.75% |     1.42 |       42 | 48.59%     | ok               |
|          35 | 57.60%   | 106.69%            | -16.03% |     1.19 |       52 | 45.92%     | ok               |

## XLM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 70.18%   | -48.56%            | -23.69% |     0.84 |       48 | 32.38%     | ok               |
|          50 | 65.43%   | -48.56%            | -20.78% |     0.82 |       44 | 28.54%     | ok               |
|          30 | 39.96%   | -48.56%            | -33.79% |     0.58 |       67 | 46.55%     | ok               |
|          40 | 31.89%   | -48.56%            | -30.70% |     0.52 |       47 | 36.59%     | ok               |
|          35 | 29.41%   | -48.56%            | -32.99% |     0.5  |       67 | 42.72%     | ok               |

## XLP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          40 | 11.77%   | 15.42%             | -7.32% |     0.69 |       72 | 39.43%     | ok               |
|          45 | 11.31%   | 15.42%             | -5.66% |     0.69 |       58 | 34.94%     | ok               |
|          35 | 10.80%   | 15.42%             | -8.39% |     0.63 |       68 | 42.43%     | ok               |
|          50 | 7.83%    | 15.42%             | -6.08% |     0.5  |       60 | 32.95%     | ok               |
|          30 | 8.49%    | 15.42%             | -8.96% |     0.5  |       72 | 44.26%     | ok               |

## XLU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 7.31%    | 37.55%             | -8.58%  |     0.39 |       48 | 31.28%     | ok               |
|          50 | 7.26%    | 37.55%             | -8.47%  |     0.39 |       48 | 30.62%     | ok               |
|          40 | 4.54%    | 37.55%             | -8.58%  |     0.26 |       56 | 32.45%     | ok               |
|          35 | -2.39%   | 37.55%             | -13.87% |    -0.07 |       62 | 35.11%     | ok               |
|          30 | -4.20%   | 37.55%             | -13.66% |    -0.15 |       67 | 38.27%     | ok               |

## XLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -8.65%   | 7.62%              | -14.71% |    -0.4  |       66 | 37.77%     | ok               |
|          25 | -11.37%  | 7.62%              | -17.25% |    -0.54 |       70 | 39.60%     | ok               |
|          45 | -11.82%  | 7.62%              | -16.50% |    -0.69 |       54 | 27.45%     | ok               |
|          50 | -11.88%  | 7.62%              | -15.90% |    -0.71 |       52 | 25.12%     | ok               |
|          15 | -15.39%  | 7.62%              | -20.69% |    -0.73 |       83 | 44.43%     | ok               |

## XLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 2.94%    | 40.50%             | -12.94% |     0.16 |       74 | 41.43%     | ok               |
|          30 | -1.30%   | 40.50%             | -14.01% |     0.03 |       78 | 44.76%     | ok               |
|          50 | -0.91%   | 40.50%             | -13.71% |     0.02 |       50 | 29.78%     | ok               |
|          15 | -2.54%   | 40.50%             | -15.77% |     0.01 |       81 | 53.41%     | ok               |
|          45 | -1.70%   | 40.50%             | -13.71% |    -0.01 |       52 | 32.28%     | ok               |

## XOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 1.96%    | 42.35%             | -21.35% |     0.13 |       40 | 29.28%     | ok               |
|          40 | 0.98%    | 42.35%             | -21.45% |     0.1  |       48 | 33.28%     | ok               |
|          25 | -0.20%   | 42.35%             | -19.90% |     0.07 |       61 | 38.10%     | ok               |
|          30 | -0.77%   | 42.35%             | -20.29% |     0.05 |       61 | 36.77%     | ok               |
|          35 | -1.46%   | 42.35%             | -20.93% |     0.03 |       60 | 35.27%     | ok               |

## XRP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -39.25%  | -43.84%            | -55.83% |    -0.39 |       74 | 40.23%     | ok               |
|          40 | -44.43%  | -43.84%            | -54.34% |    -0.54 |       64 | 34.29%     | ok               |
|          50 | -43.13%  | -43.84%            | -46.41% |    -0.63 |       64 | 23.56%     | ok               |
|          30 | -54.25%  | -43.84%            | -63.92% |    -0.69 |       80 | 45.02%     | ok               |
|          45 | -52.84%  | -43.84%            | -56.00% |    -0.77 |       62 | 30.27%     | ok               |

## YFI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -43.79%  | -76.13%            | -50.28% |    -0.81 |       62 | 24.52%     | ok               |
|          45 | -45.81%  | -76.13%            | -52.02% |    -0.95 |       58 | 20.88%     | ok               |
|          30 | -59.54%  | -76.13%            | -67.78% |    -1.03 |       83 | 37.93%     | ok               |
|          50 | -46.82%  | -76.13%            | -51.80% |    -1.07 |       50 | 17.05%     | ok               |
|          35 | -60.00%  | -76.13%            | -64.42% |    -1.13 |       75 | 31.99%     | ok               |

## ZEC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 100.94%  | 665.60%            | -24.66% |     0.81 |       52 | 23.75%     | ok               |
|          35 | 70.50%   | 665.60%            | -43.54% |     0.68 |       60 | 31.42%     | ok               |
|          25 | 58.46%   | 665.60%            | -46.61% |     0.63 |       61 | 40.23%     | ok               |
|          50 | 38.13%   | 665.60%            | -37.94% |     0.51 |       54 | 21.26%     | ok               |
|          30 | 31.33%   | 665.60%            | -46.93% |     0.5  |       69 | 36.97%     | ok               |
