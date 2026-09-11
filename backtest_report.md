# Market Tracker Backtest Report

_Generated: 2026-09-11T04:43:00+00:00_

## Data Sources

- Crypto: Kraken -> Coinbase -> CoinGecko OHLC -> CoinPaprika fallback chain.
- Stocks / ETFs / indices: Stooq -> Yahoo Finance fallback chain.
- Data rows are generated from real market APIs. Mock OHLCV rows are not generated.

## Data Freshness

- Rows: **92,671**
- Symbols: **161**
- Date range: **2024-04-18** to **2026-09-11**

## Latest Signals

| symbol     | date                |         close |   composite_score | signal   | data_source   |
|:-----------|:--------------------|--------------:|------------------:|:---------|:--------------|
| AAVE-USD   | 2026-09-11 00:00:00 |   122.36      |         30.5      | LONG     | Kraken API    |
| APT-USD    | 2026-09-11 00:00:00 |     0.649     |         43        | LONG     | Kraken API    |
| ATOM-USD   | 2026-09-11 00:00:00 |     1.7638    |         45        | LONG     | Kraken API    |
| BITO       | 2026-09-10 00:00:00 |    10.37      |         35.3333   | LONG     | Yahoo Finance |
| BTC-USD    | 2026-09-11 00:00:00 | 76991         |         41.8333   | LONG     | Kraken API    |
| COMP-USD   | 2026-09-11 00:00:00 |    20.11      |         30        | LONG     | Kraken API    |
| COP        | 2026-09-10 00:00:00 |   137.04      |         46.5833   | LONG     | Yahoo Finance |
| CRM        | 2026-09-10 00:00:00 |   243         |         56.25     | LONG     | Yahoo Finance |
| CRV-USD    | 2026-09-11 00:00:00 |     0.34849   |         42.5      | LONG     | Kraken API    |
| CVX        | 2026-09-10 00:00:00 |   212.76      |         69.0833   | LONG     | Yahoo Finance |
| DBC        | 2026-09-10 00:00:00 |    33.62      |         77.75     | LONG     | Yahoo Finance |
| DE         | 2026-09-10 00:00:00 |   677.94      |         74.9167   | LONG     | Yahoo Finance |
| DOT-USD    | 2026-09-11 00:00:00 |     1.1269    |         45.3333   | LONG     | Kraken API    |
| ETH-USD    | 2026-09-11 00:00:00 |  2451.85      |         46        | LONG     | Kraken API    |
| FET-USD    | 2026-09-11 00:00:00 |     0.1714    |         41.8333   | LONG     | Kraken API    |
| GRT-USD    | 2026-09-11 00:00:00 |     0.01775   |         36.5833   | LONG     | Kraken API    |
| IBIT       | 2026-09-10 00:00:00 |    43.68      |         54.0833   | LONG     | Yahoo Finance |
| ICP-USD    | 2026-09-11 00:00:00 |     2.795     |         71.1667   | LONG     | Kraken API    |
| INJ-USD    | 2026-09-11 00:00:00 |     6.01      |         67.8333   | LONG     | Kraken API    |
| INTC       | 2026-09-10 00:00:00 |   100.32      |         71.6667   | LONG     | Yahoo Finance |
| LTC-USD    | 2026-09-11 00:00:00 |    53.09      |         51        | LONG     | Kraken API    |
| META       | 2026-09-10 00:00:00 |   644.38      |         50.75     | LONG     | Yahoo Finance |
| MPC        | 2026-09-10 00:00:00 |   392.42      |         66.5833   | LONG     | Yahoo Finance |
| NEAR-USD   | 2026-09-11 00:00:00 |     2.453     |         69.5      | LONG     | Kraken API    |
| QCOM       | 2026-09-10 00:00:00 |   176.88      |         79        | LONG     | Yahoo Finance |
| SLB        | 2026-09-10 00:00:00 |    56.01      |         39.0833   | LONG     | Yahoo Finance |
| SOL-USD    | 2026-09-11 00:00:00 |    99.51      |         32.6667   | LONG     | Kraken API    |
| T          | 2026-09-10 00:00:00 |    25.55      |         38.5833   | LONG     | Yahoo Finance |
| TIA-USD    | 2026-09-11 00:00:00 |     0.3742    |         45.5833   | LONG     | Kraken API    |
| UNI-USD    | 2026-09-11 00:00:00 |     6.0781    |         48.8333   | LONG     | Kraken API    |
| USO        | 2026-09-10 00:00:00 |   158.38      |         77.25     | LONG     | Yahoo Finance |
| VZ         | 2026-09-10 00:00:00 |    49.97      |         56.0833   | LONG     | Yahoo Finance |
| XLE        | 2026-09-10 00:00:00 |    64.93      |         54.0833   | LONG     | Yahoo Finance |
| ZEC-USD    | 2026-09-11 00:00:00 |  1080.39      |         60.1667   | LONG     | Kraken API    |
| AAPL       | 2026-09-10 00:00:00 |   326.57      |         65.1667   | NEUTRAL  | Yahoo Finance |
| ABBV       | 2026-09-10 00:00:00 |   255         |         11.5833   | NEUTRAL  | Yahoo Finance |
| ADA-USD    | 2026-09-11 00:00:00 |     0.208826  |         25.25     | NEUTRAL  | Kraken API    |
| ADBE       | 2026-09-10 00:00:00 |   248.83      |        -38.3333   | NEUTRAL  | Yahoo Finance |
| AGG        | 2026-09-10 00:00:00 |    96.05      |        -70.5833   | NEUTRAL  | Yahoo Finance |
| ALGO-USD   | 2026-09-11 00:00:00 |     0.09166   |         23.8333   | NEUTRAL  | Kraken API    |
| AMAT       | 2026-09-10 00:00:00 |   454.01      |          1        | NEUTRAL  | Yahoo Finance |
| AMD        | 2026-09-10 00:00:00 |   503.6       |         60.3333   | NEUTRAL  | Yahoo Finance |
| AMGN       | 2026-09-10 00:00:00 |   382.47      |         -1.66667  | NEUTRAL  | Yahoo Finance |
| AMZN       | 2026-09-10 00:00:00 |   251.89      |        -14.0833   | NEUTRAL  | Yahoo Finance |
| ARB-USD    | 2026-09-11 00:00:00 |     0.1472    |         67.4167   | NEUTRAL  | Kraken API    |
| ARKK       | 2026-09-10 00:00:00 |    83.06      |         23.4167   | NEUTRAL  | Yahoo Finance |
| AVAX-USD   | 2026-09-11 00:00:00 |     7.487     |         21.5      | NEUTRAL  | Kraken API    |
| BAC        | 2026-09-10 00:00:00 |    62.56      |         31.5      | NEUTRAL  | Yahoo Finance |
| BND        | 2026-09-10 00:00:00 |    71.27      |        -68.8333   | NEUTRAL  | Yahoo Finance |
| C          | 2026-09-10 00:00:00 |   138.5       |         43.5      | NEUTRAL  | Yahoo Finance |
| CAT        | 2026-09-10 00:00:00 |   805         |        -19.0833   | NEUTRAL  | Yahoo Finance |
| CL         | 2026-09-10 00:00:00 |    87.9       |        -48.0833   | NEUTRAL  | Yahoo Finance |
| COST       | 2026-09-10 00:00:00 |   902.38      |        -60.8333   | NEUTRAL  | Yahoo Finance |
| CSCO       | 2026-09-10 00:00:00 |   107.44      |          3.66667  | NEUTRAL  | Yahoo Finance |
| DASH-USD   | 2026-09-11 00:00:00 |    56.119     |         65.9167   | NEUTRAL  | Kraken API    |
| DIA        | 2026-09-10 00:00:00 |   520.75      |        -25.0833   | NEUTRAL  | Yahoo Finance |
| DIS        | 2026-09-10 00:00:00 |   105.82      |         18.9167   | NEUTRAL  | Yahoo Finance |
| DOGE-USD   | 2026-09-11 00:00:00 |     0.0840931 |          0.583333 | NEUTRAL  | Kraken API    |
| DXY-INDEX  | 2026-09-11 00:00:00 |    99.097     |          5.64516  | NEUTRAL  | Yahoo Finance |
| EEM        | 2026-09-10 00:00:00 |    67         |         34.1667   | NEUTRAL  | Yahoo Finance |
| EFA        | 2026-09-10 00:00:00 |   105.66      |        -27.3333   | NEUTRAL  | Yahoo Finance |
| EOG        | 2026-09-10 00:00:00 |   147.46      |         28.6667   | NEUTRAL  | Yahoo Finance |
| ETC-USD    | 2026-09-11 00:00:00 |     7.61      |         23.25     | NEUTRAL  | Kraken API    |
| EWJ        | 2026-09-10 00:00:00 |    96.44      |         62.3333   | NEUTRAL  | Yahoo Finance |
| FCX        | 2026-09-10 00:00:00 |    71.21      |          5.41667  | NEUTRAL  | Yahoo Finance |
| FIL-USD    | 2026-09-11 00:00:00 |     0.791     |         35.4167   | NEUTRAL  | Kraken API    |
| FXI        | 2026-09-10 00:00:00 |    34.35      |        -61        | NEUTRAL  | Yahoo Finance |
| GDX        | 2026-09-10 00:00:00 |    96.03      |         -2.08333  | NEUTRAL  | Yahoo Finance |
| GDXJ       | 2026-09-10 00:00:00 |   124.1       |         -2.08333  | NEUTRAL  | Yahoo Finance |
| GE         | 2026-09-10 00:00:00 |   324.15      |        -11.8333   | NEUTRAL  | Yahoo Finance |
| GLD        | 2026-09-10 00:00:00 |   396.36      |        -20.0833   | NEUTRAL  | Yahoo Finance |
| GOOGL      | 2026-09-10 00:00:00 |   332.6       |        -33.5833   | NEUTRAL  | Yahoo Finance |
| GS         | 2026-09-10 00:00:00 |  1019.77      |        -19.8333   | NEUTRAL  | Yahoo Finance |
| HBAR-USD   | 2026-09-11 00:00:00 |     0.07548   |         -3.16667  | NEUTRAL  | Kraken API    |
| IBM        | 2026-09-10 00:00:00 |   234.02      |        -33.3333   | NEUTRAL  | Yahoo Finance |
| IEF        | 2026-09-10 00:00:00 |    91.18      |        -70.5833   | NEUTRAL  | Yahoo Finance |
| IEMG       | 2026-09-10 00:00:00 |    81.58      |         36.1667   | NEUTRAL  | Yahoo Finance |
| INTU       | 2026-09-10 00:00:00 |   312.77      |        -67.8333   | NEUTRAL  | Yahoo Finance |
| IWM        | 2026-09-10 00:00:00 |   287.7       |        -17.5      | NEUTRAL  | Yahoo Finance |
| JNJ        | 2026-09-10 00:00:00 |   266.35      |         -1.08333  | NEUTRAL  | Yahoo Finance |
| JPM        | 2026-09-10 00:00:00 |   353.56      |         15.5      | NEUTRAL  | Yahoo Finance |
| KO         | 2026-09-10 00:00:00 |    87.83      |         20.4167   | NEUTRAL  | Yahoo Finance |
| LDO-USD    | 2026-09-11 00:00:00 |     0.373     |         19.8333   | NEUTRAL  | Kraken API    |
| LIN        | 2026-09-10 00:00:00 |   461.62      |        -45        | NEUTRAL  | Yahoo Finance |
| LINK-USD   | 2026-09-11 00:00:00 |    11.4958    |         28.5      | NEUTRAL  | Kraken API    |
| LRCX       | 2026-09-10 00:00:00 |   298.01      |        -10.25     | NEUTRAL  | Yahoo Finance |
| MRK        | 2026-09-10 00:00:00 |   144.71      |         15.9167   | NEUTRAL  | Yahoo Finance |
| MS         | 2026-09-10 00:00:00 |   212.66      |          9.41667  | NEUTRAL  | Yahoo Finance |
| MSFT       | 2026-09-10 00:00:00 |   492.44      |         41        | NEUTRAL  | Yahoo Finance |
| MU         | 2026-09-10 00:00:00 |   977.41      |         53.6667   | NEUTRAL  | Yahoo Finance |
| NEM        | 2026-09-10 00:00:00 |   126.14      |         15.9167   | NEUTRAL  | Yahoo Finance |
| NFLX       | 2026-09-10 00:00:00 |    76.01      |        -28.5833   | NEUTRAL  | Yahoo Finance |
| NOW        | 2026-09-10 00:00:00 |   131.17      |         28.5833   | NEUTRAL  | Yahoo Finance |
| NVDA       | 2026-09-10 00:00:00 |   218.36      |         20.5      | NEUTRAL  | Yahoo Finance |
| OP-USD     | 2026-09-11 00:00:00 |     0.0964    |        -24.4167   | NEUTRAL  | Kraken API    |
| ORCL       | 2026-09-10 00:00:00 |   152.94      |         40.8333   | NEUTRAL  | Yahoo Finance |
| OXY        | 2026-09-10 00:00:00 |    61.16      |         26.6667   | NEUTRAL  | Yahoo Finance |
| PEP        | 2026-09-10 00:00:00 |   136.65      |        -62.5      | NEUTRAL  | Yahoo Finance |
| PEPE-USD   | 2026-09-11 00:00:00 |     3.312e-06 |         -8.58333  | NEUTRAL  | Kraken API    |
| PFE        | 2026-09-10 00:00:00 |    27.65      |          5.91667  | NEUTRAL  | Yahoo Finance |
| PG         | 2026-09-10 00:00:00 |   142.97      |        -30.8333   | NEUTRAL  | Yahoo Finance |
| PM         | 2026-09-10 00:00:00 |   189.77      |         22.6667   | NEUTRAL  | Yahoo Finance |
| POL-USD    | 2026-09-11 00:00:00 |     0.0932    |        -10.9167   | NEUTRAL  | Kraken API    |
| QQQ        | 2026-09-10 00:00:00 |   708.69      |         -0.166667 | NEUTRAL  | Yahoo Finance |
| RENDER-USD | 2026-09-11 00:00:00 |     1.416     |        -21.1667   | NEUTRAL  | Kraken API    |
| RTX        | 2026-09-10 00:00:00 |   198.12      |        -29.1667   | NEUTRAL  | Yahoo Finance |
| SBUX       | 2026-09-10 00:00:00 |    99.22      |        -52.25     | NEUTRAL  | Yahoo Finance |
| SCHW       | 2026-09-10 00:00:00 |   107.33      |          9.41667  | NEUTRAL  | Yahoo Finance |
| SHIB-USD   | 2026-09-11 00:00:00 |     5.102e-06 |          2.58333  | NEUTRAL  | Kraken API    |
| SMH        | 2026-09-10 00:00:00 |   560.28      |         -6.5      | NEUTRAL  | Yahoo Finance |
| SNX-USD    | 2026-09-11 00:00:00 |     0.2064    |        -46.5833   | NEUTRAL  | Kraken API    |
| SOXX       | 2026-09-10 00:00:00 |   517.43      |         -2.75     | NEUTRAL  | Yahoo Finance |
| SPY        | 2026-09-10 00:00:00 |   757.83      |        -16.6667   | NEUTRAL  | Yahoo Finance |
| SUSHI-USD  | 2026-09-11 00:00:00 |     0.2172    |         28.25     | NEUTRAL  | Kraken API    |
| TGT        | 2026-09-10 00:00:00 |   155.73      |         15.9167   | NEUTRAL  | Yahoo Finance |
| TLT        | 2026-09-10 00:00:00 |    80.78      |        -62.75     | NEUTRAL  | Yahoo Finance |
| TMO        | 2026-09-10 00:00:00 |   603.18      |         -1.58333  | NEUTRAL  | Yahoo Finance |
| TMUS       | 2026-09-10 00:00:00 |   177.16      |        -46.5      | NEUTRAL  | Yahoo Finance |
| TRX-USD    | 2026-09-11 00:00:00 |     0.339803  |         29.6667   | NEUTRAL  | Kraken API    |
| TSLA       | 2026-09-10 00:00:00 |   363.56      |         28.9167   | NEUTRAL  | Yahoo Finance |
| TXN        | 2026-09-10 00:00:00 |   258.82      |         10.5      | NEUTRAL  | Yahoo Finance |
| UNH        | 2026-09-10 00:00:00 |   388.28      |         18.4167   | NEUTRAL  | Yahoo Finance |
| UPS        | 2026-09-10 00:00:00 |    99.97      |        -58.8333   | NEUTRAL  | Yahoo Finance |
| VEA        | 2026-09-10 00:00:00 |    71.92      |        -27.3333   | NEUTRAL  | Yahoo Finance |
| VIXY       | 2026-09-10 00:00:00 |    18.16      |         25.25     | NEUTRAL  | Yahoo Finance |
| VTI        | 2026-09-10 00:00:00 |   373.24      |        -16.6667   | NEUTRAL  | Yahoo Finance |
| VWO        | 2026-09-10 00:00:00 |    59.94      |         -1.83333  | NEUTRAL  | Yahoo Finance |
| WFC        | 2026-09-10 00:00:00 |    89.45      |         43.5      | NEUTRAL  | Yahoo Finance |
| WIF-USD    | 2026-09-11 00:00:00 |     0.194     |        -10.5833   | NEUTRAL  | Kraken API    |
| WMT        | 2026-09-10 00:00:00 |   105.73      |        -15.0833   | NEUTRAL  | Yahoo Finance |
| XBI        | 2026-09-10 00:00:00 |   156.82      |        -11.0833   | NEUTRAL  | Yahoo Finance |
| XLB        | 2026-09-10 00:00:00 |    50.76      |        -32.25     | NEUTRAL  | Yahoo Finance |
| XLC        | 2026-09-10 00:00:00 |   111.5       |        -14.25     | NEUTRAL  | Yahoo Finance |
| XLF        | 2026-09-10 00:00:00 |    56.87      |          1.83333  | NEUTRAL  | Yahoo Finance |
| XLK        | 2026-09-10 00:00:00 |   185.22      |         35.8333   | NEUTRAL  | Yahoo Finance |
| XLM-USD    | 2026-09-11 00:00:00 |     0.176666  |        -21.1667   | NEUTRAL  | Kraken API    |
| XLP        | 2026-09-10 00:00:00 |    83.09      |        -49.75     | NEUTRAL  | Yahoo Finance |
| XLU        | 2026-09-10 00:00:00 |    42.52      |        -52.5      | NEUTRAL  | Yahoo Finance |
| XLV        | 2026-09-10 00:00:00 |   165.66      |         -9.08333  | NEUTRAL  | Yahoo Finance |
| XLY        | 2026-09-10 00:00:00 |   111.96      |        -59.25     | NEUTRAL  | Yahoo Finance |
| XOM        | 2026-09-10 00:00:00 |   165.23      |         12.3333   | NEUTRAL  | Yahoo Finance |
| XRP-USD    | 2026-09-11 00:00:00 |     1.34478   |          0.583333 | NEUTRAL  | Kraken API    |
| YFI-USD    | 2026-09-11 00:00:00 |  2148.3       |        -26.5833   | NEUTRAL  | Kraken API    |
| AVGO       | 2026-09-10 00:00:00 |   360.83      |        -46.5833   | SHORT    | Yahoo Finance |
| BA         | 2026-09-10 00:00:00 |   204.8       |        -52.4167   | SHORT    | Yahoo Finance |
| BCH-USD    | 2026-09-11 00:00:00 |   227.69      |        -48.6667   | SHORT    | Kraken API    |
| BLK        | 2026-09-10 00:00:00 |  1062.4       |        -35.3333   | SHORT    | Yahoo Finance |
| BONK-USD   | 2026-09-11 00:00:00 |     2.713e-06 |        -35.5      | SHORT    | Kraken API    |
| CMCSA      | 2026-09-10 00:00:00 |    25.17      |        -44.5833   | SHORT    | Yahoo Finance |
| HD         | 2026-09-10 00:00:00 |   305.69      |        -59.5833   | SHORT    | Yahoo Finance |
| HON        | 2026-09-10 00:00:00 |   202.18      |        -59.9167   | SHORT    | Yahoo Finance |
| HYG        | 2026-09-10 00:00:00 |    78.62      |        -59.3333   | SHORT    | Yahoo Finance |
| ITA        | 2026-09-10 00:00:00 |   218.32      |        -59.0833   | SHORT    | Yahoo Finance |
| LLY        | 2026-09-10 00:00:00 |  1123         |        -34.8333   | SHORT    | Yahoo Finance |
| MCD        | 2026-09-10 00:00:00 |   253.05      |        -59.0833   | SHORT    | Yahoo Finance |
| NKE        | 2026-09-10 00:00:00 |    36.62      |        -61.5833   | SHORT    | Yahoo Finance |
| SHY        | 2026-09-10 00:00:00 |    81.42      |        -54.8333   | SHORT    | Yahoo Finance |
| SKY-USD    | 2026-09-11 00:00:00 |     0.05975   |        -44.8333   | SHORT    | Kraken API    |
| SLV        | 2026-09-10 00:00:00 |    57.5       |        -47.0833   | SHORT    | Yahoo Finance |
| VNQ        | 2026-09-10 00:00:00 |    94.12      |        -42.3333   | SHORT    | Yahoo Finance |
| XLI        | 2026-09-10 00:00:00 |   170.55      |        -54.1667   | SHORT    | Yahoo Finance |

## Edge Summary

- Symbols with trades: **160** of 160
- Beat buy-and-hold: **28.12%** of traded symbols
- Positive return: **30.00%** of traded symbols
- Median strategy return: **-10.87%** (benchmark **23.15%**)
- Median excess vs benchmark: **-34.94%**
- Median Sharpe: **-0.15**
- Median exposure: **44.34%**

> Edge is real only if both _beat buy-and-hold_ and _median excess_ are convincingly positive across many symbols. Treat a single high-return symbol as noise.

## Portfolio Backtest

Actual capital-allocation books (not per-symbol averages). Benchmarks: `equal_weight_buyhold` (whole tracked universe), `spy_buyhold` (100% SPY), and `sixty_forty` (60% SPY / 40% AGG). `high_conf_voltarget` inverse-vol-weights the HIGH-confidence book; `conviction_long_short` is market-neutral. Judge on **Sharpe** and **max_drawdown** out-of-sample, not raw return: a fully-invested long book wins on return in a bull market but carries all the risk.

| strategy              | scope         | ann_return   | ann_vol   |   sharpe | max_drawdown   | total_return   |   avg_gross_exposure |
|:----------------------|:--------------|:-------------|:----------|---------:|:---------------|:---------------|---------------------:|
| equal_weight_buyhold  | full          | 10.67%       | 28.42%    |     0.38 | -39.63%        | 22.35%         |                 1    |
| equal_weight_buyhold  | out_of_sample | 10.18%       | 27.92%    |     0.36 | -29.33%        | 6.96%          |                 1    |
| all_signals_ew        | full          | -19.77%      | 23.95%    |    -0.83 | -62.63%        | -49.80%        |                 1    |
| all_signals_ew        | out_of_sample | 9.30%        | 23.20%    |     0.4  | -22.44%        | 7.34%          |                 1    |
| high_conf_ew          | full          | -1.45%       | 30.58%    |    -0.05 | -44.20%        | -16.82%        |                 0.89 |
| high_conf_ew          | out_of_sample | 27.93%       | 26.82%    |     1.04 | -22.62%        | 29.61%         |                 0.89 |
| high_conf_voltarget   | full          | 0.08%        | 27.62%    |     0    | -35.11%        | -10.53%        |                 0.89 |
| high_conf_voltarget   | out_of_sample | 17.98%       | 22.69%    |     0.79 | -16.94%        | 17.80%         |                 0.89 |
| conviction_long_short | full          | -18.24%      | 22.36%    |    -0.82 | -49.84%        | -46.84%        |                 0.97 |
| conviction_long_short | out_of_sample | -11.79%      | 20.79%    |    -0.57 | -26.05%        | -13.84%        |                 0.97 |
| spy_buyhold           | full          | 6.70%        | 13.51%    |     0.5  | -19.00%        | 19.24%         |                 0.79 |
| spy_buyhold           | out_of_sample | 2.40%        | 9.83%     |     0.24 | -12.06%        | 2.07%          |                 0.79 |
| sixty_forty           | full          | 3.93%        | 8.53%     |     0.46 | -11.66%        | 11.46%         |                 0.79 |
| sixty_forty           | out_of_sample | -0.47%       | 6.58%     |    -0.07 | -8.26%         | -0.73%         |                 0.79 |

## Walk-Forward Robustness

Each book measured across contiguous time folds (each a different regime). A book has durable edge only if `mean_sharpe` is positive, `min_sharpe` isn't deeply negative, and `pct_positive_folds` is high — a single great fold doesn't count. `fold_sharpes` lists each fold oldest-to-newest.

| strategy              |   n_folds |   mean_sharpe |   median_sharpe |   min_sharpe | pct_positive_folds   | mean_return   | fold_sharpes                 |
|:----------------------|----------:|--------------:|----------------:|-------------:|:---------------------|:--------------|:-----------------------------|
| equal_weight_buyhold  |         5 |          0.64 |            0.72 |        -1.37 | 80.00%               | 5.55%         | 1.94;0.72;0.68;-1.37;1.23    |
| all_signals_ew        |         5 |         -0.88 |           -0.88 |        -2.31 | 20.00%               | -9.97%        | -0.88;-2.31;-2.25;1.66;-0.62 |
| high_conf_ew          |         5 |         -0.13 |            0.3  |        -2.1  | 60.00%               | -2.42%        | -0.23;-2.10;0.30;0.34;1.07   |
| high_conf_voltarget   |         5 |         -0    |            0.33 |        -1.68 | 60.00%               | -1.69%        | 0.34;-1.68;0.33;-0.16;1.15   |
| conviction_long_short |         5 |         -0.92 |           -0.92 |        -1.94 | 20.00%               | -11.64%       | -1.94;-1.17;-0.55;0.00;-0.92 |
| spy_buyhold           |         5 |          0.59 |            0.57 |        -0.75 | 60.00%               | 3.92%         | 2.33;-0.09;0.57;-0.75;0.90   |
| sixty_forty           |         5 |          0.54 |            0.5  |        -0.9  | 60.00%               | 2.35%         | 2.48;-0.14;0.78;-0.90;0.50   |

## Strategy Comparison

Each decision rule backtested over the same data. `out_of_sample` is the most recent ~35% of each symbol's history (unseen tail). A rule has real edge only if `median_excess` and `beat_benchmark_pct` stay positive out-of-sample, not just full-sample.

| strategy        | scope         |   symbols | beat_benchmark_pct   | positive_pct   | median_return   | median_benchmark   | median_excess   |   median_sharpe |   total_trades |
|:----------------|:--------------|----------:|:---------------------|:---------------|:----------------|:-------------------|:----------------|----------------:|---------------:|
| trend           | full          |       160 | 28.12%               | 30.00%         | -10.87%         | 23.15%             | -34.94%         |           -0.15 |          11332 |
| trend           | out_of_sample |       160 | 25.62%               | 47.50%         | -0.59%          | 8.69%              | -12.07%         |            0.04 |           3714 |
| mean_reversion  | full          |       156 | 32.05%               | 49.36%         | -0.08%          | 20.76%             | -21.10%         |            0.02 |           1296 |
| mean_reversion  | out_of_sample |       119 | 33.61%               | 55.46%         | 0.34%           | 7.41%              | -7.94%          |            0.21 |            502 |
| regime_adaptive | full          |       160 | 26.88%               | 31.25%         | -11.66%         | 23.15%             | -35.49%         |           -0.15 |          11605 |
| regime_adaptive | out_of_sample |       160 | 25.62%               | 48.75%         | -0.45%          | 8.69%              | -11.97%         |            0.07 |           3848 |

## Signal Calibration

Realized forward return in the signal's direction, grouped by confidence. HIGH should outrank LOW for the confidence score to be meaningful.

| confidence_level   |   horizon |     n | mean_return   | median_return   | win_rate   |
|:-------------------|----------:|------:|:--------------|:----------------|:-----------|
| HIGH               |         5 |  7928 | 0.13%         | 0.07%           | 51.16%     |
| MEDIUM             |         5 | 28939 | -0.02%        | 0.03%           | 50.30%     |
| LOW                |         5 |  3581 | -0.47%        | -0.43%          | 45.71%     |
| ALL                |         5 | 40448 | -0.03%        | 0.01%           | 50.06%     |
| HIGH               |        10 |  7851 | 0.37%         | 0.09%           | 51.00%     |
| MEDIUM             |        10 | 28676 | 0.07%         | 0.05%           | 50.39%     |
| LOW                |        10 |  3532 | -0.82%        | -0.64%          | 45.98%     |
| ALL                |        10 | 40059 | 0.05%         | 0.01%           | 50.12%     |
| HIGH               |        20 |  7696 | 0.80%         | 0.33%           | 52.79%     |
| MEDIUM             |        20 | 28108 | 0.61%         | 0.51%           | 52.86%     |
| LOW                |        20 |  3435 | -0.94%        | -0.68%          | 46.75%     |
| ALL                |        20 | 39239 | 0.51%         | 0.40%           | 52.32%     |

## Backtest Summary

### Data Quality / Signal Availability

- **ok**: 160 symbols

| symbol     |   trades | return   | benchmark_return   | mdd     |   sharpe | exposure   | skipped_reason   |
|:-----------|---------:|:---------|:-------------------|:--------|---------:|:-----------|:-----------------|
| AAPL       |       60 | 8.94%    | 95.50%             | -23.09% |     0.28 | 49.25%     | ok               |
| AAVE-USD   |       71 | -42.70%  | -2.02%             | -66.17% |    -0.29 | 42.15%     | ok               |
| ABBV       |       68 | -26.32%  | 54.86%             | -30.52% |    -0.6  | 47.42%     | ok               |
| ADA-USD    |       81 | -39.80%  | -62.56%            | -45.96% |    -0.33 | 47.51%     | ok               |
| ADBE       |       69 | -14.38%  | -47.41%            | -31.20% |    -0.08 | 56.41%     | ok               |
| AGG        |       69 | -8.04%   | 0.81%              | -10.95% |    -1.32 | 33.11%     | ok               |
| ALGO-USD   |       78 | -35.63%  | -40.83%            | -43.00% |    -0.3  | 38.89%     | ok               |
| AMAT       |       65 | -26.91%  | 133.64%            | -53.91% |    -0.19 | 49.42%     | ok               |
| AMD        |       54 | 10.09%   | 224.74%            | -41.56% |     0.31 | 34.61%     | ok               |
| AMGN       |       69 | -8.10%   | 45.56%             | -34.19% |    -0.07 | 50.75%     | ok               |
| AMZN       |       82 | -55.80%  | 40.55%             | -56.90% |    -1.59 | 41.76%     | ok               |
| APT-USD    |       76 | -39.69%  | -85.09%            | -65.32% |    -0.23 | 41.38%     | ok               |
| ARB-USD    |       77 | -24.93%  | -44.16%            | -58.79% |     0.04 | 43.68%     | ok               |
| ARKK       |       87 | -31.37%  | 93.57%             | -35.94% |    -0.48 | 44.59%     | ok               |
| ATOM-USD   |       90 | -58.53%  | -57.74%            | -60.59% |    -0.84 | 46.55%     | ok               |
| AVAX-USD   |       74 | -48.72%  | -53.58%            | -45.50% |    -0.58 | 38.70%     | ok               |
| AVGO       |       64 | 19.33%   | 186.60%            | -36.08% |     0.38 | 40.93%     | ok               |
| BA         |       69 | 2.39%    | 20.31%             | -27.11% |     0.17 | 49.75%     | ok               |
| BAC        |       78 | -11.79%  | 74.90%             | -27.64% |    -0.25 | 48.92%     | ok               |
| BCH-USD    |       82 | -0.32%   | -15.37%            | -53.87% |     0.22 | 49.43%     | ok               |
| BITO       |       76 | -14.56%  | -62.66%            | -39.47% |    -0.03 | 39.77%     | ok               |
| BLK        |       79 | -8.28%   | 42.17%             | -26.90% |    -0.16 | 48.09%     | ok               |
| BND        |       69 | -7.79%   | 0.81%              | -10.16% |    -1.24 | 34.94%     | ok               |
| BONK-USD   |       74 | 5.08%    | -71.47%            | -51.50% |     0.33 | 44.25%     | ok               |
| BTC-USD    |       64 | 12.18%   | 0.94%              | -23.38% |     0.34 | 51.92%     | ok               |
| C          |       77 | -31.81%  | 137.48%            | -39.51% |    -0.65 | 48.09%     | ok               |
| CAT        |       70 | 10.17%   | 124.90%            | -18.88% |     0.29 | 49.58%     | ok               |
| CL         |       60 | 5.41%    | 1.37%              | -14.32% |     0.24 | 41.26%     | ok               |
| CMCSA      |       82 | -46.43%  | -32.22%            | -49.38% |    -1.25 | 42.26%     | ok               |
| COMP-USD   |       97 | -43.72%  | -44.83%            | -55.77% |    -0.32 | 47.70%     | ok               |
| COP        |       72 | -17.29%  | 7.22%              | -43.40% |    -0.25 | 43.59%     | ok               |
| COST       |       58 | 2.80%    | 26.87%             | -29.73% |     0.15 | 41.76%     | ok               |
| CRM        |       67 | -30.44%  | -10.64%            | -45.51% |    -0.42 | 45.59%     | ok               |
| CRV-USD    |       70 | 35.40%   | -22.90%            | -39.89% |     0.53 | 41.95%     | ok               |
| CSCO       |       58 | 18.11%   | 123.32%            | -21.79% |     0.42 | 47.59%     | ok               |
| CVX        |       73 | -8.67%   | 35.03%             | -29.13% |    -0.16 | 41.26%     | ok               |
| DASH-USD   |       57 | -12.80%  | 195.85%            | -64.43% |     0.29 | 30.65%     | ok               |
| DBC        |       64 | -2.70%   | 44.11%             | -25.02% |    -0.03 | 34.28%     | ok               |
| DE         |       74 | -10.87%  | 69.23%             | -22.93% |    -0.15 | 43.76%     | ok               |
| DIA        |       64 | -4.94%   | 37.82%             | -12.94% |    -0.23 | 45.26%     | ok               |
| DIS        |       64 | -14.66%  | -5.88%             | -28.17% |    -0.24 | 43.43%     | ok               |
| DOGE-USD   |       72 | -30.09%  | -40.82%            | -62.31% |    -0.09 | 48.85%     | ok               |
| DOT-USD    |       92 | -61.22%  | -66.57%            | -66.83% |    -0.65 | 48.28%     | ok               |
| DXY-INDEX  |       38 | -2.36%   | -5.62%             | -6.02%  |    -0.36 | 30.09%     | ok               |
| EEM        |       64 | -10.43%  | 68.05%             | -25.67% |    -0.28 | 41.76%     | ok               |
| EFA        |       58 | -10.29%  | 38.86%             | -12.96% |    -0.4  | 41.26%     | ok               |
| EOG        |       83 | -30.83%  | 11.92%             | -47.57% |    -0.68 | 46.09%     | ok               |
| ETC-USD    |       62 | -37.87%  | -45.78%            | -48.09% |    -0.54 | 29.31%     | ok               |
| ETH-USD    |       58 | 133.18%  | 66.57%             | -30.11% |     1.2  | 46.17%     | ok               |
| EWJ        |       64 | -23.51%  | 44.18%             | -29.40% |    -0.82 | 37.10%     | ok               |
| FCX        |       67 | -33.12%  | 41.97%             | -47.67% |    -0.4  | 44.93%     | ok               |
| FET-USD    |       73 | -47.46%  | -54.62%            | -56.90% |    -0.31 | 39.27%     | ok               |
| FIL-USD    |       65 | -51.47%  | -64.92%            | -51.47% |    -0.7  | 32.38%     | ok               |
| FXI        |       46 | -4.88%   | 42.65%             | -23.91% |    -0.04 | 32.11%     | ok               |
| GDX        |       60 | 0.59%    | 184.53%            | -34.99% |     0.15 | 45.76%     | ok               |
| GDXJ       |       68 | -34.79%  | 197.89%            | -44.61% |    -0.44 | 43.76%     | ok               |
| GE         |       78 | -11.13%  | 111.95%            | -27.82% |    -0.09 | 48.09%     | ok               |
| GLD        |       54 | 6.26%    | 79.89%             | -16.56% |     0.23 | 45.76%     | ok               |
| GOOGL      |       55 | 64.08%   | 113.19%            | -20.41% |     1.04 | 48.25%     | ok               |
| GRT-USD    |       81 | -31.97%  | -75.17%            | -52.11% |    -0.22 | 43.68%     | ok               |
| GS         |       68 | 0.35%    | 152.98%            | -22.13% |     0.11 | 47.75%     | ok               |
| HD         |       73 | -5.65%   | -8.17%             | -18.07% |    -0.07 | 42.60%     | ok               |
| HON        |       94 | -21.99%  | 7.04%              | -33.57% |    -0.51 | 55.57%     | ok               |
| HYG        |       91 | -9.70%   | 3.67%              | -10.59% |    -1.13 | 35.27%     | ok               |
| IBIT       |       36 | 30.78%   | 14.92%             | -18.95% |     0.63 | 32.20%     | ok               |
| IBM        |       73 | -25.87%  | 28.96%             | -48.94% |    -0.31 | 50.75%     | ok               |
| ICP-USD    |       77 | -5.03%   | -39.53%            | -47.30% |     0.21 | 36.78%     | ok               |
| IEF        |       84 | -12.52%  | -0.48%             | -13.06% |    -1.78 | 33.28%     | ok               |
| IEMG       |       60 | -7.71%   | 62.28%             | -26.84% |    -0.2  | 41.43%     | ok               |
| INJ-USD    |       71 | -54.28%  | -13.53%            | -74.43% |    -0.51 | 37.93%     | ok               |
| INTC       |       66 | 42.79%   | 186.30%            | -60.60% |     0.54 | 48.25%     | ok               |
| INTU       |       71 | -17.93%  | -48.59%            | -42.15% |    -0.18 | 44.59%     | ok               |
| ITA        |       72 | -2.77%   | 71.29%             | -23.75% |    -0    | 48.09%     | ok               |
| IWM        |       54 | 11.41%   | 49.19%             | -12.65% |     0.46 | 36.44%     | ok               |
| JNJ        |       68 | -1.56%   | 82.76%             | -17.51% |     0.01 | 48.25%     | ok               |
| JPM        |       73 | -20.40%  | 95.07%             | -32.74% |    -0.53 | 48.09%     | ok               |
| KO         |       53 | 27.17%   | 49.09%             | -8.64%  |     0.93 | 40.60%     | ok               |
| LDO-USD    |       74 | 10.25%   | -40.42%            | -61.16% |     0.36 | 47.13%     | ok               |
| LIN        |       70 | -10.87%  | 3.40%              | -20.61% |    -0.35 | 36.27%     | ok               |
| LINK-USD   |       71 | 22.48%   | 5.34%              | -33.64% |     0.44 | 46.55%     | ok               |
| LLY        |       69 | -28.72%  | 50.55%             | -53.34% |    -0.43 | 47.75%     | ok               |
| LRCX       |       84 | -25.21%  | 235.25%            | -61.08% |    -0.15 | 42.43%     | ok               |
| LTC-USD    |       70 | -16.41%  | -23.25%            | -33.94% |    -0.03 | 51.92%     | ok               |
| MCD        |       77 | -6.47%   | -6.62%             | -21.88% |    -0.21 | 36.94%     | ok               |
| META       |       78 | -36.40%  | 28.41%             | -44.90% |    -0.66 | 47.59%     | ok               |
| MPC        |       67 | 4.70%    | 101.22%            | -37.91% |     0.2  | 49.42%     | ok               |
| MRK        |       67 | -23.85%  | 15.56%             | -35.95% |    -0.46 | 44.26%     | ok               |
| MS         |       75 | -5.41%   | 135.61%            | -27.79% |    -0.05 | 47.92%     | ok               |
| MSFT       |       79 | -29.20%  | 21.81%             | -38.06% |    -0.67 | 49.42%     | ok               |
| MU         |       49 | 164.65%  | 773.23%            | -68.76% |     1.08 | 53.91%     | ok               |
| NEAR-USD   |       77 | 12.88%   | 28.70%             | -59.86% |     0.37 | 42.15%     | ok               |
| NEM        |       68 | -17.93%  | 227.21%            | -39.56% |    -0.09 | 53.41%     | ok               |
| NFLX       |       76 | 12.79%   | 24.49%             | -21.09% |     0.35 | 53.24%     | ok               |
| NKE        |       79 | -28.63%  | -61.75%            | -55.35% |    -0.33 | 43.26%     | ok               |
| NOW        |       84 | 4.16%    | -10.32%            | -30.43% |     0.22 | 49.75%     | ok               |
| NVDA       |       77 | -47.57%  | 65.57%             | -52.37% |    -0.62 | 57.93%     | ok               |
| OP-USD     |       70 | -49.54%  | -83.69%            | -68.74% |    -0.47 | 34.10%     | ok               |
| ORCL       |       68 | 87.31%   | 31.84%             | -30.61% |     0.81 | 55.07%     | ok               |
| OXY        |       77 | -6.02%   | -7.39%             | -31.83% |     0.02 | 44.09%     | ok               |
| PEP        |       74 | -0.06%   | -20.68%            | -21.35% |     0.07 | 46.09%     | ok               |
| PEPE-USD   |       89 | -39.87%  | -45.16%            | -57.66% |    -0.17 | 47.70%     | ok               |
| PFE        |       83 | -38.10%  | 8.90%              | -43.50% |    -1.13 | 40.10%     | ok               |
| PG         |       66 | -20.10%  | -9.10%             | -24.55% |    -0.77 | 37.60%     | ok               |
| PM         |       79 | -1.38%   | 108.08%            | -35.15% |     0.07 | 53.91%     | ok               |
| POL-USD    |       81 | 24.65%   | -44.21%            | -45.67% |     0.46 | 49.62%     | ok               |
| QCOM       |       75 | -20.09%  | 9.56%              | -56.59% |    -0.12 | 42.43%     | ok               |
| QQQ        |       66 | 13.22%   | 67.38%             | -14.20% |     0.41 | 46.42%     | ok               |
| RENDER-USD |      102 | -31.90%  | -49.82%            | -44.84% |    -0.08 | 45.98%     | ok               |
| RTX        |       56 | 32.91%   | 96.72%             | -16.99% |     0.74 | 53.08%     | ok               |
| SBUX       |       58 | -18.02%  | 13.85%             | -29.22% |    -0.33 | 37.94%     | ok               |
| SCHW       |       78 | -13.57%  | 47.17%             | -31.92% |    -0.26 | 48.09%     | ok               |
| SHIB-USD   |       84 | -43.72%  | -52.05%            | -40.60% |    -0.45 | 53.07%     | ok               |
| SHY        |       50 | -2.45%   | 0.33%              | -3.30%  |    -0.85 | 34.61%     | ok               |
| SKY-USD    |       80 | -31.07%  | 3.32%              | -47.82% |    -0.32 | 45.40%     | ok               |
| SLB        |       77 | -28.18%  | 9.95%              | -54.95% |    -0.47 | 50.92%     | ok               |
| SLV        |       69 | 11.36%   | 122.35%            | -42.66% |     0.31 | 42.10%     | ok               |
| SMH        |       48 | 67.47%   | 168.55%            | -34.29% |     0.99 | 44.93%     | ok               |
| SNX-USD    |       62 | -27.61%  | -64.66%            | -47.16% |    -0.12 | 34.10%     | ok               |
| SOL-USD    |       68 | -31.27%  | -5.57%             | -44.99% |    -0.15 | 59.20%     | ok               |
| SOXX       |       58 | 68.55%   | 150.41%            | -40.14% |     0.94 | 43.43%     | ok               |
| SPY        |       64 | 3.49%    | 51.71%             | -15.53% |     0.18 | 51.58%     | ok               |
| SUSHI-USD  |      102 | -84.91%  | -55.67%            | -83.76% |    -1.55 | 38.31%     | ok               |
| T          |       72 | 37.66%   | 56.46%             | -17.01% |     0.82 | 58.07%     | ok               |
| TGT        |       60 | -12.70%  | -6.51%             | -36.37% |    -0.2  | 37.77%     | ok               |
| TIA-USD    |       91 | -57.93%  | -83.92%            | -73.13% |    -0.5  | 41.38%     | ok               |
| TLT        |       72 | -19.20%  | -9.06%             | -21.87% |    -1.4  | 35.11%     | ok               |
| TMO        |       65 | 24.66%   | 11.39%             | -18.85% |     0.54 | 54.08%     | ok               |
| TMUS       |       76 | 2.41%    | 10.14%             | -27.06% |     0.15 | 48.25%     | ok               |
| TRX-USD    |       68 | 10.93%   | 47.51%             | -22.90% |     0.38 | 52.30%     | ok               |
| TSLA       |       78 | -33.80%  | 142.49%            | -58.36% |    -0.2  | 42.93%     | ok               |
| TXN        |       71 | -18.16%  | 58.14%             | -46.98% |    -0.14 | 49.25%     | ok               |
| UNH        |       74 | 32.56%   | -21.27%            | -26.31% |     0.55 | 50.25%     | ok               |
| UNI-USD    |       92 | -70.43%  | 27.42%             | -78.97% |    -0.76 | 48.47%     | ok               |
| UPS        |       70 | -35.47%  | -29.96%            | -38.84% |    -0.71 | 40.27%     | ok               |
| USO        |       70 | 12.34%   | 101.04%            | -41.71% |     0.31 | 31.95%     | ok               |
| VEA        |       58 | -4.31%   | 50.37%             | -17.93% |    -0.13 | 43.09%     | ok               |
| VIXY       |      100 | -78.35%  | -69.73%            | -88.17% |    -0.94 | 34.61%     | ok               |
| VNQ        |       75 | -16.82%  | 19.72%             | -24.92% |    -0.71 | 38.10%     | ok               |
| VTI        |       70 | -5.97%   | 51.01%             | -17.64% |    -0.16 | 51.75%     | ok               |
| VWO        |       80 | -16.62%  | 46.16%             | -25.20% |    -0.61 | 41.76%     | ok               |
| VZ         |       83 | -19.75%  | 24.52%             | -25.90% |    -0.59 | 40.43%     | ok               |
| WFC        |       80 | -17.12%  | 52.28%             | -28.90% |    -0.28 | 46.92%     | ok               |
| WIF-USD    |       66 | -49.89%  | -39.28%            | -61.76% |    -0.31 | 36.21%     | ok               |
| WMT        |       65 | 10.38%   | 78.42%             | -21.98% |     0.35 | 48.09%     | ok               |
| XBI        |       66 | 0.56%    | 87.85%             | -18.30% |     0.1  | 42.60%     | ok               |
| XLB        |       60 | -12.29%  | 14.03%             | -25.04% |    -0.43 | 31.95%     | ok               |
| XLC        |       63 | 14.20%   | 38.77%             | -12.33% |     0.52 | 50.58%     | ok               |
| XLE        |       77 | -13.08%  | 38.38%             | -35.03% |    -0.26 | 44.43%     | ok               |
| XLF        |       80 | -9.66%   | 42.78%             | -23.61% |    -0.3  | 45.92%     | ok               |
| XLI        |       70 | -3.48%   | 41.31%             | -14.12% |    -0.09 | 40.77%     | ok               |
| XLK        |       40 | 66.88%   | 88.44%             | -14.75% |     1.23 | 47.42%     | ok               |
| XLM-USD    |       67 | -19.59%  | -20.10%            | -54.58% |    -0.01 | 47.70%     | ok               |
| XLP        |       64 | 7.54%    | 12.71%             | -10.28% |     0.46 | 39.60%     | ok               |
| XLU        |       67 | -3.52%   | 31.97%             | -20.40% |    -0.11 | 39.27%     | ok               |
| XLV        |       70 | -16.95%  | 19.67%             | -20.62% |    -0.78 | 37.77%     | ok               |
| XLY        |       79 | -6.85%   | 30.75%             | -17.23% |    -0.15 | 46.09%     | ok               |
| XOM        |       59 | -0.05%   | 39.41%             | -20.29% |     0.08 | 35.44%     | ok               |
| XRP-USD    |       58 | 5.78%    | -25.03%            | -33.91% |     0.27 | 36.40%     | ok               |
| YFI-USD    |       81 | -69.75%  | -51.23%            | -72.54% |    -1.27 | 39.46%     | ok               |
| ZEC-USD    |       66 | 95.71%   | 2635.86%           | -56.50% |     0.77 | 39.85%     | ok               |

## AAPL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 15.76%   | 95.50%             | -22.53% |     0.39 |       69 | 54.08%     | ok               |
|          15 | 11.57%   | 95.50%             | -24.50% |     0.32 |       80 | 61.23%     | ok               |
|          40 | 9.04%    | 95.50%             | -28.08% |     0.28 |       54 | 43.93%     | ok               |
|          30 | 8.94%    | 95.50%             | -23.09% |     0.28 |       60 | 49.25%     | ok               |
|          35 | 7.38%    | 95.50%             | -24.45% |     0.25 |       60 | 47.92%     | ok               |

## AAVE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 25.49%   | -2.02%             | -43.61% |     0.46 |       41 | 35.25%     | ok               |
|          45 | 12.68%   | -2.02%             | -49.19% |     0.34 |       44 | 30.27%     | ok               |
|          35 | 9.46%    | -2.02%             | -48.79% |     0.32 |       49 | 38.31%     | ok               |
|          50 | -5.93%   | -2.02%             | -45.07% |     0.12 |       42 | 22.41%     | ok               |
|          15 | -35.19%  | -2.02%             | -61.76% |    -0.08 |       76 | 56.13%     | ok               |

## ABBV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -14.35%  | 54.86%             | -26.55% |    -0.31 |       52 | 35.44%     | ok               |
|          25 | -26.41%  | 54.86%             | -30.41% |    -0.59 |       67 | 49.25%     | ok               |
|          40 | -24.31%  | 54.86%             | -27.36% |    -0.59 |       68 | 39.93%     | ok               |
|          30 | -26.32%  | 54.86%             | -30.52% |    -0.6  |       68 | 47.42%     | ok               |
|          20 | -26.97%  | 54.86%             | -29.62% |    -0.6  |       67 | 51.08%     | ok               |

## ADA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 10.73%   | -62.56%            | -35.54% |     0.32 |       52 | 26.63%     | ok               |
|          45 | 0.18%    | -62.56%            | -34.64% |     0.2  |       55 | 31.61%     | ok               |
|          40 | -17.64%  | -62.56%            | -41.08% |    -0.01 |       67 | 37.74%     | ok               |
|          35 | -22.30%  | -62.56%            | -42.89% |    -0.06 |       69 | 42.15%     | ok               |
|          15 | -34.61%  | -62.56%            | -48.46% |    -0.09 |       74 | 64.37%     | ok               |

## ADBE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -1.47%   | -47.41%            | -29.07% |     0.13 |       53 | 60.07%     | ok               |
|          35 | -4.67%   | -47.41%            | -30.52% |     0.05 |       78 | 47.75%     | ok               |
|          20 | -11.35%  | -47.41%            | -31.52% |    -0.01 |       57 | 63.06%     | ok               |
|          30 | -14.38%  | -47.41%            | -31.20% |    -0.08 |       69 | 56.41%     | ok               |
|          40 | -14.18%  | -47.41%            | -31.90% |    -0.14 |       70 | 40.27%     | ok               |

## AGG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -5.06%   | 0.81%              | -7.92%  |    -1.1  |       50 | 18.47%     | ok               |
|          20 | -8.86%   | 0.81%              | -11.58% |    -1.31 |       71 | 38.27%     | ok               |
|          30 | -8.04%   | 0.81%              | -10.95% |    -1.32 |       69 | 33.11%     | ok               |
|          45 | -7.13%   | 0.81%              | -9.11%  |    -1.36 |       60 | 23.13%     | ok               |
|          25 | -9.03%   | 0.81%              | -12.22% |    -1.39 |       71 | 36.61%     | ok               |

## ALGO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -35.63%  | -40.83%            | -43.00% |    -0.3  |       78 | 38.89%     | ok               |
|          15 | -42.44%  | -40.83%            | -51.70% |    -0.34 |       80 | 49.81%     | ok               |
|          25 | -44.64%  | -40.83%            | -59.19% |    -0.42 |       78 | 44.44%     | ok               |
|          20 | -47.40%  | -40.83%            | -55.13% |    -0.45 |       80 | 47.32%     | ok               |
|          35 | -45.71%  | -40.83%            | -49.66% |    -0.61 |       60 | 32.57%     | ok               |

## AMAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -26.70%  | 133.64%            | -53.90% |    -0.15 |       68 | 58.57%     | ok               |
|          30 | -26.91%  | 133.64%            | -53.91% |    -0.19 |       65 | 49.42%     | ok               |
|          35 | -26.60%  | 133.64%            | -51.27% |    -0.2  |       65 | 46.92%     | ok               |
|          50 | -24.71%  | 133.64%            | -43.40% |    -0.2  |       46 | 35.27%     | ok               |
|          40 | -30.57%  | 133.64%            | -52.58% |    -0.27 |       63 | 42.26%     | ok               |

## AMD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 14.50%   | 224.74%            | -40.05% |     0.34 |       56 | 29.45%     | ok               |
|          40 | 10.09%   | 224.74%            | -41.56% |     0.31 |       54 | 34.61%     | ok               |
|          35 | 7.82%    | 224.74%            | -43.60% |     0.29 |       62 | 36.11%     | ok               |
|          30 | -0.70%   | 224.74%            | -47.15% |     0.21 |       63 | 38.77%     | ok               |
|          25 | -7.52%   | 224.74%            | -53.19% |     0.15 |       63 | 41.43%     | ok               |

## AMGN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -2.11%   | 45.56%             | -26.65% |     0.07 |       65 | 56.41%     | ok               |
|          35 | -4.38%   | 45.56%             | -31.29% |     0.01 |       67 | 47.09%     | ok               |
|          15 | -6.10%   | 45.56%             | -27.98% |    -0.01 |       62 | 60.40%     | ok               |
|          30 | -8.10%   | 45.56%             | -34.19% |    -0.07 |       69 | 50.75%     | ok               |
|          25 | -10.12%  | 45.56%             | -33.47% |    -0.11 |       63 | 53.08%     | ok               |

## AMZN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -25.14%  | 40.55%             | -27.34% |    -0.75 |       54 | 30.45%     | ok               |
|          50 | -29.72%  | 40.55%             | -32.41% |    -1.07 |       50 | 23.46%     | ok               |
|          45 | -35.00%  | 40.55%             | -36.26% |    -1.23 |       56 | 26.96%     | ok               |
|          35 | -50.72%  | 40.55%             | -51.56% |    -1.47 |       75 | 35.77%     | ok               |
|          30 | -55.80%  | 40.55%             | -56.90% |    -1.59 |       82 | 41.76%     | ok               |

## APT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -9.25%   | -85.09%            | -41.21% |     0.01 |       44 | 17.24%     | ok               |
|          20 | -37.41%  | -85.09%            | -66.07% |    -0.17 |       79 | 50.00%     | ok               |
|          35 | -32.37%  | -85.09%            | -57.84% |    -0.18 |       70 | 34.87%     | ok               |
|          45 | -27.51%  | -85.09%            | -61.63% |    -0.2  |       60 | 23.95%     | ok               |
|          25 | -39.18%  | -85.09%            | -65.88% |    -0.22 |       72 | 45.40%     | ok               |

## ARB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 41.48%   | -44.16%            | -45.20% |     0.57 |       83 | 60.54%     | ok               |
|          45 | 20.58%   | -44.16%            | -40.44% |     0.42 |       58 | 25.86%     | ok               |
|          20 | 8.75%    | -44.16%            | -53.77% |     0.38 |       69 | 54.41%     | ok               |
|          40 | 11.82%   | -44.16%            | -39.80% |     0.36 |       57 | 33.91%     | ok               |
|          50 | 10.74%   | -44.16%            | -35.70% |     0.33 |       44 | 18.58%     | ok               |

## ARKK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -23.28%  | 93.57%             | -37.76% |    -0.23 |       93 | 56.07%     | ok               |
|          20 | -26.46%  | 93.57%             | -35.07% |    -0.31 |       89 | 51.75%     | ok               |
|          30 | -31.37%  | 93.57%             | -35.94% |    -0.48 |       87 | 44.59%     | ok               |
|          35 | -36.80%  | 93.57%             | -39.39% |    -0.64 |       88 | 41.93%     | ok               |
|          40 | -35.98%  | 93.57%             | -40.75% |    -0.65 |       80 | 37.10%     | ok               |

## ATOM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -38.57%  | -57.74%            | -48.20% |    -0.29 |       88 | 63.41%     | ok               |
|          25 | -48.80%  | -57.74%            | -53.09% |    -0.55 |       92 | 52.68%     | ok               |
|          20 | -56.23%  | -57.74%            | -59.03% |    -0.7  |       96 | 56.32%     | ok               |
|          30 | -58.53%  | -57.74%            | -60.59% |    -0.84 |       90 | 46.55%     | ok               |
|          45 | -55.79%  | -57.74%            | -55.96% |    -0.96 |       78 | 31.42%     | ok               |

## AVAX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 3.54%    | -53.58%            | -22.06% |     0.21 |       32 | 17.62%     | ok               |
|          40 | -2.31%   | -53.58%            | -26.27% |     0.13 |       34 | 24.71%     | ok               |
|          45 | -5.05%   | -53.58%            | -23.19% |     0.08 |       28 | 21.65%     | ok               |
|          15 | -23.88%  | -53.58%            | -42.39% |    -0.04 |       72 | 52.87%     | ok               |
|          35 | -20.15%  | -53.58%            | -33.05% |    -0.11 |       54 | 31.03%     | ok               |

## AVGO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 22.76%   | 186.60%            | -38.01% |     0.42 |       68 | 43.59%     | ok               |
|          30 | 19.33%   | 186.60%            | -36.08% |     0.38 |       64 | 40.93%     | ok               |
|          40 | 11.84%   | 186.60%            | -40.70% |     0.3  |       64 | 34.78%     | ok               |
|          35 | 11.73%   | 186.60%            | -37.55% |     0.3  |       72 | 37.94%     | ok               |
|          50 | 10.84%   | 186.60%            | -36.86% |     0.29 |       56 | 29.78%     | ok               |

## BA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 30.43%   | 20.31%             | -13.34% |     0.75 |       44 | 33.28%     | ok               |
|          35 | 24.16%   | 20.31%             | -21.02% |     0.51 |       70 | 45.76%     | ok               |
|          40 | 18.15%   | 20.31%             | -23.87% |     0.43 |       48 | 40.60%     | ok               |
|          25 | 5.23%    | 20.31%             | -29.13% |     0.21 |       72 | 53.08%     | ok               |
|          30 | 2.39%    | 20.31%             | -27.11% |     0.17 |       69 | 49.75%     | ok               |

## BAC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -1.58%   | 74.90%             | -18.63% |     0.05 |       80 | 53.41%     | ok               |
|          15 | -6.94%   | 74.90%             | -21.05% |    -0.07 |       82 | 58.74%     | ok               |
|          25 | -6.18%   | 74.90%             | -24.29% |    -0.08 |       80 | 51.58%     | ok               |
|          35 | -7.11%   | 74.90%             | -29.13% |    -0.13 |       70 | 45.09%     | ok               |
|          45 | -6.85%   | 74.90%             | -20.91% |    -0.15 |       62 | 36.94%     | ok               |

## BCH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 42.40%   | -15.37%            | -45.51% |     0.59 |       75 | 58.81%     | ok               |
|          20 | 17.74%   | -15.37%            | -45.82% |     0.4  |       71 | 55.36%     | ok               |
|          25 | 0.59%    | -15.37%            | -51.09% |     0.24 |       72 | 51.92%     | ok               |
|          30 | -0.32%   | -15.37%            | -53.87% |     0.22 |       82 | 49.43%     | ok               |
|          35 | -18.25%  | -15.37%            | -61.21% |     0    |       76 | 44.83%     | ok               |

## BITO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -3.93%   | -62.66%            | -31.98% |     0.08 |       54 | 24.13%     | ok               |
|          30 | -14.56%  | -62.66%            | -39.47% |    -0.03 |       76 | 39.77%     | ok               |
|          15 | -22.72%  | -62.66%            | -48.38% |    -0.09 |       87 | 48.59%     | ok               |
|          35 | -18.74%  | -62.66%            | -41.51% |    -0.1  |       68 | 35.61%     | ok               |
|          45 | -17.16%  | -62.66%            | -36.67% |    -0.12 |       60 | 27.62%     | ok               |

## BLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -2.42%   | 42.17%             | -21.48% |     0.02 |       82 | 52.75%     | ok               |
|          35 | -1.97%   | 42.17%             | -20.79% |     0.02 |       86 | 44.43%     | ok               |
|          25 | -3.82%   | 42.17%             | -24.62% |    -0.02 |       75 | 50.58%     | ok               |
|          40 | -3.83%   | 42.17%             | -22.83% |    -0.05 |       78 | 40.10%     | ok               |
|          30 | -8.28%   | 42.17%             | -26.90% |    -0.16 |       79 | 48.09%     | ok               |

## BND Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.71%   | 0.81%              | -9.66%  |    -0.97 |       65 | 40.43%     | ok               |
|          25 | -7.36%   | 0.81%              | -10.73% |    -1.11 |       67 | 38.44%     | ok               |
|          30 | -7.79%   | 0.81%              | -10.16% |    -1.24 |       69 | 34.94%     | ok               |
|          15 | -8.97%   | 0.81%              | -11.52% |    -1.28 |       77 | 43.26%     | ok               |
|          40 | -9.03%   | 0.81%              | -11.15% |    -1.62 |       66 | 27.45%     | ok               |

## BONK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 130.69%  | -71.47%            | -35.57% |     1.08 |       48 | 22.22%     | ok               |
|          15 | 90.35%   | -71.47%            | -62.48% |     0.78 |       72 | 59.39%     | ok               |
|          25 | 67.92%   | -71.47%            | -54.47% |     0.7  |       73 | 50.96%     | ok               |
|          20 | 66.58%   | -71.47%            | -61.03% |     0.69 |       67 | 55.56%     | ok               |
|          45 | 34.87%   | -71.47%            | -47.53% |     0.53 |       68 | 27.97%     | ok               |

## BTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 54.44%   | 0.94%              | -21.56% |     0.94 |       58 | 41.95%     | ok               |
|          40 | 51.03%   | 0.94%              | -14.50% |     0.93 |       40 | 36.02%     | ok               |
|          45 | 49.98%   | 0.94%              | -12.20% |     0.93 |       38 | 32.57%     | ok               |
|          30 | 25.65%   | 0.94%              | -21.75% |     0.54 |       64 | 47.70%     | ok               |
|          50 | 18.80%   | 0.94%              | -19.38% |     0.48 |       40 | 27.20%     | ok               |

## C Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -10.42%  | 137.48%            | -21.80% |    -0.23 |       66 | 33.11%     | ok               |
|          45 | -21.42%  | 137.48%            | -29.60% |    -0.53 |       76 | 37.44%     | ok               |
|          25 | -28.74%  | 137.48%            | -36.78% |    -0.56 |       69 | 50.08%     | ok               |
|          15 | -31.97%  | 137.48%            | -38.73% |    -0.6  |       74 | 57.24%     | ok               |
|          20 | -31.77%  | 137.48%            | -37.73% |    -0.63 |       79 | 52.91%     | ok               |

## CAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 10.27%   | 124.90%            | -22.07% |     0.29 |       66 | 52.41%     | ok               |
|          30 | 10.17%   | 124.90%            | -18.88% |     0.29 |       70 | 49.58%     | ok               |
|          15 | 6.54%    | 124.90%            | -26.40% |     0.23 |       77 | 63.56%     | ok               |
|          20 | 5.21%    | 124.90%            | -21.30% |     0.21 |       78 | 56.07%     | ok               |
|          45 | 2.71%    | 124.90%            | -26.22% |     0.16 |       56 | 38.27%     | ok               |

## CL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 4.72%    | 1.37%              | -12.98% |     0.24 |       42 | 25.62%     | ok               |
|          30 | 5.41%    | 1.37%              | -14.32% |     0.24 |       60 | 41.26%     | ok               |
|          45 | 1.03%    | 1.37%              | -13.51% |     0.09 |       46 | 28.29%     | ok               |
|          35 | 0.39%    | 1.37%              | -13.83% |     0.07 |       62 | 37.60%     | ok               |
|          40 | -2.52%   | 1.37%              | -12.70% |    -0.04 |       56 | 32.28%     | ok               |

## CMCSA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -44.19%  | -32.22%            | -47.26% |    -1.02 |       91 | 56.74%     | ok               |
|          30 | -46.43%  | -32.22%            | -49.38% |    -1.25 |       82 | 42.26%     | ok               |
|          25 | -48.67%  | -32.22%            | -51.49% |    -1.31 |       89 | 47.42%     | ok               |
|          50 | -32.82%  | -32.22%            | -31.73% |    -1.32 |       50 | 13.48%     | ok               |
|          35 | -46.57%  | -32.22%            | -49.22% |    -1.35 |       96 | 36.61%     | ok               |

## COMP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -5.51%   | -44.83%            | -38.71% |     0.13 |       44 | 21.65%     | ok               |
|          30 | -43.72%  | -44.83%            | -55.77% |    -0.32 |       97 | 47.70%     | ok               |
|          25 | -49.27%  | -44.83%            | -54.41% |    -0.39 |       96 | 55.56%     | ok               |
|          40 | -47.85%  | -44.83%            | -53.14% |    -0.49 |       70 | 35.25%     | ok               |
|          45 | -47.75%  | -44.83%            | -55.45% |    -0.52 |       62 | 29.69%     | ok               |

## COP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -7.23%   | 7.22%              | -35.08% |    -0.07 |       50 | 29.62%     | ok               |
|          35 | -13.69%  | 7.22%              | -43.58% |    -0.18 |       71 | 40.43%     | ok               |
|          45 | -13.45%  | 7.22%              | -41.35% |    -0.21 |       62 | 33.44%     | ok               |
|          30 | -17.29%  | 7.22%              | -43.40% |    -0.25 |       72 | 43.59%     | ok               |
|          40 | -18.91%  | 7.22%              | -47.05% |    -0.34 |       68 | 36.61%     | ok               |

## COST Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 14.80%   | 26.87%             | -24.32% |     0.49 |       62 | 47.59%     | ok               |
|          25 | 11.82%   | 26.87%             | -24.73% |     0.41 |       59 | 44.76%     | ok               |
|          35 | 7.34%    | 26.87%             | -27.39% |     0.31 |       56 | 39.27%     | ok               |
|          30 | 2.80%    | 26.87%             | -29.73% |     0.15 |       58 | 41.76%     | ok               |
|          15 | -0.19%   | 26.87%             | -27.30% |     0.07 |       65 | 51.08%     | ok               |

## CRM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -22.92%  | -10.64%            | -34.84% |    -0.29 |       64 | 40.60%     | ok               |
|          15 | -29.40%  | -10.64%            | -47.54% |    -0.33 |       92 | 57.57%     | ok               |
|          40 | -26.66%  | -10.64%            | -40.30% |    -0.4  |       70 | 36.44%     | ok               |
|          30 | -30.44%  | -10.64%            | -45.51% |    -0.42 |       67 | 45.59%     | ok               |
|          20 | -33.18%  | -10.64%            | -49.37% |    -0.43 |       76 | 51.41%     | ok               |

## CRV-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 73.23%   | -22.90%            | -37.78% |     0.77 |       70 | 37.16%     | ok               |
|          40 | 43.53%   | -22.90%            | -38.86% |     0.59 |       60 | 32.76%     | ok               |
|          50 | 35.01%   | -22.90%            | -30.73% |     0.54 |       50 | 21.26%     | ok               |
|          30 | 35.40%   | -22.90%            | -39.89% |     0.53 |       70 | 41.95%     | ok               |
|          45 | 33.62%   | -22.90%            | -42.29% |     0.53 |       60 | 25.67%     | ok               |

## CSCO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 31.56%   | 123.32%            | -19.34% |     0.68 |       48 | 36.77%     | ok               |
|          45 | 27.11%   | 123.32%            | -19.34% |     0.59 |       50 | 38.44%     | ok               |
|          25 | 24.67%   | 123.32%            | -23.28% |     0.52 |       55 | 48.92%     | ok               |
|          35 | 20.55%   | 123.32%            | -23.68% |     0.46 |       52 | 45.09%     | ok               |
|          20 | 18.61%   | 123.32%            | -22.32% |     0.43 |       65 | 51.25%     | ok               |

## CVX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -4.04%   | 35.03%             | -24.33% |    -0.02 |       73 | 43.76%     | ok               |
|          40 | -4.02%   | 35.03%             | -27.34% |    -0.04 |       77 | 36.11%     | ok               |
|          45 | -4.93%   | 35.03%             | -28.83% |    -0.07 |       67 | 32.61%     | ok               |
|          35 | -6.25%   | 35.03%             | -28.85% |    -0.1  |       69 | 38.27%     | ok               |
|          30 | -8.67%   | 35.03%             | -29.13% |    -0.16 |       73 | 41.26%     | ok               |

## DASH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 193.60%  | 195.85%            | -21.17% |     1.11 |       38 | 17.62%     | ok               |
|          40 | 126.55%  | 195.85%            | -25.22% |     0.9  |       44 | 23.75%     | ok               |
|          45 | 117.78%  | 195.85%            | -27.62% |     0.88 |       40 | 19.54%     | ok               |
|          30 | -12.80%  | 195.85%            | -64.43% |     0.29 |       57 | 30.65%     | ok               |
|          35 | -14.23%  | 195.85%            | -63.41% |     0.28 |       67 | 28.16%     | ok               |

## DBC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 3.04%    | 44.11%             | -26.79% |     0.16 |       78 | 39.77%     | ok               |
|          25 | -0.20%   | 44.11%             | -25.43% |     0.06 |       66 | 36.11%     | ok               |
|          20 | -0.86%   | 44.11%             | -25.96% |     0.04 |       71 | 37.94%     | ok               |
|          50 | -2.06%   | 44.11%             | -20.31% |    -0.02 |       46 | 23.46%     | ok               |
|          35 | -2.63%   | 44.11%             | -23.42% |    -0.03 |       66 | 32.95%     | ok               |

## DE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.41%   | 69.23%             | -17.97% |     0.07 |       62 | 28.79%     | ok               |
|          45 | -6.66%   | 69.23%             | -20.42% |    -0.08 |       66 | 33.44%     | ok               |
|          20 | -8.40%   | 69.23%             | -25.20% |    -0.08 |       72 | 48.92%     | ok               |
|          25 | -10.72%  | 69.23%             | -24.31% |    -0.14 |       75 | 46.42%     | ok               |
|          30 | -10.87%  | 69.23%             | -22.93% |    -0.15 |       74 | 43.76%     | ok               |

## DIA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -1.59%   | 37.82%             | -11.28% |    -0.04 |       58 | 46.59%     | ok               |
|          35 | -3.49%   | 37.82%             | -13.15% |    -0.16 |       66 | 42.26%     | ok               |
|          20 | -4.30%   | 37.82%             | -13.60% |    -0.18 |       62 | 48.75%     | ok               |
|          30 | -4.94%   | 37.82%             | -12.94% |    -0.23 |       64 | 45.26%     | ok               |
|          40 | -6.68%   | 37.82%             | -15.06% |    -0.36 |       70 | 39.27%     | ok               |

## DIS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 21.21%   | -5.88%             | -12.35% |     0.65 |       46 | 25.29%     | ok               |
|          40 | -4.60%   | -5.88%             | -18.75% |    -0.01 |       61 | 33.78%     | ok               |
|          45 | -6.91%   | -5.88%             | -16.54% |    -0.09 |       47 | 29.12%     | ok               |
|          15 | -12.43%  | -5.88%             | -31.15% |    -0.14 |       87 | 55.07%     | ok               |
|          35 | -12.68%  | -5.88%             | -25.70% |    -0.2  |       75 | 40.10%     | ok               |

## DOGE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -0.22%   | -40.82%            | -59.36% |     0.28 |       78 | 64.37%     | ok               |
|          20 | -2.72%   | -40.82%            | -57.37% |     0.24 |       79 | 59.20%     | ok               |
|          25 | -13.79%  | -40.82%            | -55.33% |     0.12 |       71 | 54.98%     | ok               |
|          30 | -30.09%  | -40.82%            | -62.31% |    -0.09 |       72 | 48.85%     | ok               |
|          50 | -32.88%  | -40.82%            | -55.17% |    -0.28 |       58 | 23.75%     | ok               |

## DOT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -64.47%  | -66.57%            | -72.29% |    -0.56 |       83 | 63.98%     | ok               |
|          20 | -60.79%  | -66.57%            | -68.69% |    -0.56 |       93 | 60.15%     | ok               |
|          35 | -56.82%  | -66.57%            | -62.17% |    -0.57 |       84 | 41.76%     | ok               |
|          45 | -46.06%  | -66.57%            | -53.44% |    -0.6  |       54 | 31.23%     | ok               |
|          40 | -50.22%  | -66.57%            | -55.69% |    -0.63 |       60 | 34.29%     | ok               |

## DXY-INDEX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -2.36%   | -5.62%             | -6.02%  |    -0.36 |       38 | 30.09%     | ok               |
|          40 | -4.38%   | -5.62%             | -7.30%  |    -0.57 |       70 | 46.32%     | ok               |
|          45 | -4.70%   | -5.62%             | -8.14%  |    -0.67 |       60 | 35.93%     | ok               |
|          15 | -7.74%   | -5.62%             | -11.61% |    -0.75 |       91 | 73.16%     | ok               |
|          30 | -7.35%   | -5.62%             | -9.61%  |    -0.89 |       78 | 57.36%     | ok               |

## EEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -5.41%   | 68.05%             | -15.88% |    -0.14 |       54 | 34.11%     | ok               |
|          45 | -6.13%   | 68.05%             | -17.36% |    -0.16 |       54 | 35.77%     | ok               |
|          40 | -6.47%   | 68.05%             | -19.52% |    -0.17 |       66 | 37.94%     | ok               |
|          35 | -7.12%   | 68.05%             | -23.88% |    -0.17 |       68 | 39.93%     | ok               |
|          30 | -10.43%  | 68.05%             | -25.67% |    -0.28 |       64 | 41.76%     | ok               |

## EFA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -6.48%   | 38.86%             | -10.53% |    -0.18 |       66 | 50.08%     | ok               |
|          30 | -10.29%  | 38.86%             | -12.96% |    -0.4  |       58 | 41.26%     | ok               |
|          20 | -12.18%  | 38.86%             | -13.22% |    -0.45 |       71 | 47.09%     | ok               |
|          25 | -13.03%  | 38.86%             | -15.23% |    -0.51 |       66 | 44.26%     | ok               |
|          40 | -12.48%  | 38.86%             | -14.85% |    -0.54 |       64 | 37.27%     | ok               |

## EOG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -26.42%  | 11.92%             | -38.89% |    -0.63 |       56 | 32.28%     | ok               |
|          30 | -30.83%  | 11.92%             | -47.57% |    -0.68 |       83 | 46.09%     | ok               |
|          40 | -30.54%  | 11.92%             | -41.11% |    -0.74 |       66 | 35.61%     | ok               |
|          25 | -34.34%  | 11.92%             | -51.99% |    -0.75 |       84 | 49.08%     | ok               |
|          35 | -31.55%  | 11.92%             | -44.81% |    -0.75 |       79 | 40.77%     | ok               |

## ETC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -17.78%  | -45.78%            | -31.28% |    -0.22 |       28 | 16.28%     | ok               |
|          45 | -19.48%  | -45.78%            | -38.47% |    -0.22 |       28 | 18.20%     | ok               |
|          35 | -29.42%  | -45.78%            | -45.32% |    -0.38 |       48 | 25.48%     | ok               |
|          40 | -28.08%  | -45.78%            | -43.28% |    -0.39 |       38 | 21.07%     | ok               |
|          30 | -37.87%  | -45.78%            | -48.09% |    -0.54 |       62 | 29.31%     | ok               |

## ETH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 133.18%  | 66.57%             | -30.11% |     1.2  |       58 | 46.17%     | ok               |
|          30 | 103.80%  | 66.57%             | -32.89% |     1.01 |       62 | 53.64%     | ok               |
|          25 | 66.40%   | 66.57%             | -40.90% |     0.78 |       60 | 57.85%     | ok               |
|          40 | 46.18%   | 66.57%             | -33.11% |     0.68 |       60 | 38.31%     | ok               |
|          20 | 51.84%   | 66.57%             | -39.10% |     0.67 |       80 | 61.88%     | ok               |

## EWJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -24.14%  | 44.18%             | -30.00% |    -0.82 |       58 | 39.27%     | ok               |
|          30 | -23.51%  | 44.18%             | -29.40% |    -0.82 |       64 | 37.10%     | ok               |
|          25 | -26.33%  | 44.18%             | -29.85% |    -0.92 |       58 | 38.27%     | ok               |
|          15 | -28.45%  | 44.18%             | -31.15% |    -0.93 |       71 | 42.76%     | ok               |
|          45 | -24.13%  | 44.18%             | -27.35% |    -0.98 |       62 | 28.95%     | ok               |

## FCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -6.46%   | 41.97%             | -33.28% |     0.04 |       58 | 33.11%     | ok               |
|          50 | -6.88%   | 41.97%             | -26.57% |     0.02 |       58 | 28.95%     | ok               |
|          40 | -20.25%  | 41.97%             | -43.78% |    -0.19 |       68 | 37.94%     | ok               |
|          30 | -33.12%  | 41.97%             | -47.67% |    -0.4  |       67 | 44.93%     | ok               |
|          35 | -37.25%  | 41.97%             | -50.89% |    -0.5  |       73 | 43.09%     | ok               |

## FET-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -38.18%  | -54.62%            | -63.21% |    -0.1  |       90 | 51.15%     | ok               |
|          15 | -44.79%  | -54.62%            | -59.58% |    -0.16 |       84 | 55.94%     | ok               |
|          25 | -44.45%  | -54.62%            | -63.66% |    -0.23 |       83 | 44.25%     | ok               |
|          30 | -47.46%  | -54.62%            | -56.90% |    -0.31 |       73 | 39.27%     | ok               |
|          50 | -42.23%  | -54.62%            | -40.07% |    -0.67 |       42 | 11.88%     | ok               |

## FIL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -39.58%  | -64.92%            | -49.44% |    -0.55 |       46 | 21.65%     | ok               |
|          50 | -37.26%  | -64.92%            | -37.86% |    -0.66 |       32 | 11.69%     | ok               |
|          30 | -51.47%  | -64.92%            | -51.47% |    -0.7  |       65 | 32.38%     | ok               |
|          35 | -54.12%  | -64.92%            | -54.93% |    -0.85 |       58 | 26.05%     | ok               |
|          15 | -66.97%  | -64.92%            | -66.97% |    -0.9  |       92 | 45.02%     | ok               |

## FXI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -4.62%   | 42.65%             | -22.57% |    -0.03 |       48 | 33.61%     | ok               |
|          30 | -4.88%   | 42.65%             | -23.91% |    -0.04 |       46 | 32.11%     | ok               |
|          15 | -7.71%   | 42.65%             | -21.68% |    -0.09 |       52 | 37.60%     | ok               |
|          20 | -8.25%   | 42.65%             | -24.53% |    -0.12 |       50 | 35.44%     | ok               |
|          35 | -8.56%   | 42.65%             | -27.53% |    -0.14 |       48 | 29.62%     | ok               |

## GDX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 5.33%    | 184.53%            | -35.59% |     0.22 |       74 | 50.08%     | ok               |
|          40 | 1.42%    | 184.53%            | -31.37% |     0.15 |       64 | 39.60%     | ok               |
|          30 | 0.59%    | 184.53%            | -34.99% |     0.15 |       60 | 45.76%     | ok               |
|          25 | -4.74%   | 184.53%            | -38.90% |     0.07 |       64 | 46.92%     | ok               |
|          35 | -4.82%   | 184.53%            | -31.88% |     0.06 |       72 | 42.43%     | ok               |

## GDXJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -24.66%  | 197.89%            | -44.73% |    -0.19 |       70 | 49.75%     | ok               |
|          50 | -29.33%  | 197.89%            | -46.83% |    -0.4  |       60 | 35.27%     | ok               |
|          30 | -34.79%  | 197.89%            | -44.61% |    -0.44 |       68 | 43.76%     | ok               |
|          25 | -39.14%  | 197.89%            | -46.95% |    -0.49 |       73 | 46.59%     | ok               |
|          35 | -38.01%  | 197.89%            | -42.52% |    -0.52 |       72 | 41.10%     | ok               |

## GE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 4.50%    | 111.95%            | -22.29% |     0.19 |       66 | 34.94%     | ok               |
|          45 | -7.00%   | 111.95%            | -25.68% |    -0.04 |       76 | 37.44%     | ok               |
|          20 | -9.68%   | 111.95%            | -25.05% |    -0.05 |       75 | 52.08%     | ok               |
|          30 | -11.13%  | 111.95%            | -27.82% |    -0.09 |       78 | 48.09%     | ok               |
|          35 | -13.06%  | 111.95%            | -27.11% |    -0.14 |       82 | 42.76%     | ok               |

## GLD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 11.57%   | 79.89%             | -14.54% |     0.35 |       52 | 46.92%     | ok               |
|          20 | 10.39%   | 79.89%             | -14.54% |     0.32 |       53 | 48.59%     | ok               |
|          30 | 6.26%    | 79.89%             | -16.56% |     0.23 |       54 | 45.76%     | ok               |
|          15 | 3.62%    | 79.89%             | -17.54% |     0.17 |       55 | 52.75%     | ok               |
|          35 | 3.45%    | 79.89%             | -17.22% |     0.17 |       56 | 43.43%     | ok               |

## GOOGL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 68.15%   | 113.19%            | -18.25% |     1.11 |       57 | 44.76%     | ok               |
|          30 | 64.08%   | 113.19%            | -20.41% |     1.04 |       55 | 48.25%     | ok               |
|          25 | 61.58%   | 113.19%            | -19.76% |     1    |       55 | 50.75%     | ok               |
|          45 | 53.90%   | 113.19%            | -14.13% |     1    |       52 | 38.10%     | ok               |
|          40 | 50.54%   | 113.19%            | -19.94% |     0.94 |       48 | 39.77%     | ok               |

## GRT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -8.28%   | -75.17%            | -45.50% |     0.17 |       72 | 61.49%     | ok               |
|          50 | -1.85%   | -75.17%            | -30.80% |     0.12 |       42 | 18.97%     | ok               |
|          20 | -15.92%  | -75.17%            | -42.04% |     0.07 |       79 | 55.75%     | ok               |
|          45 | -20.28%  | -75.17%            | -44.68% |    -0.15 |       48 | 25.48%     | ok               |
|          25 | -31.55%  | -75.17%            | -51.18% |    -0.16 |       80 | 51.34%     | ok               |

## GS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 26.30%   | 152.98%            | -20.56% |     0.56 |       68 | 55.91%     | ok               |
|          20 | 6.90%    | 152.98%            | -23.19% |     0.24 |       68 | 52.58%     | ok               |
|          40 | 3.29%    | 152.98%            | -17.88% |     0.16 |       64 | 41.76%     | ok               |
|          25 | 1.48%    | 152.98%            | -23.32% |     0.13 |       68 | 50.08%     | ok               |
|          30 | 0.35%    | 152.98%            | -22.13% |     0.11 |       68 | 47.75%     | ok               |

## HD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -5.65%   | -8.17%             | -18.07% |    -0.07 |       73 | 42.60%     | ok               |
|          25 | -6.39%   | -8.17%             | -18.89% |    -0.09 |       72 | 44.59%     | ok               |
|          45 | -7.60%   | -8.17%             | -16.42% |    -0.19 |       52 | 27.45%     | ok               |
|          35 | -9.53%   | -8.17%             | -19.91% |    -0.2  |       78 | 38.77%     | ok               |
|          40 | -10.19%  | -8.17%             | -18.06% |    -0.26 |       82 | 32.78%     | ok               |

## HON Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -8.50%   | 7.04%              | -21.23% |    -0.19 |       72 | 34.44%     | ok               |
|          45 | -11.51%  | 7.04%              | -23.18% |    -0.27 |       72 | 40.27%     | ok               |
|          35 | -20.80%  | 7.04%              | -31.82% |    -0.5  |       88 | 50.92%     | ok               |
|          30 | -21.99%  | 7.04%              | -33.57% |    -0.51 |       94 | 55.57%     | ok               |
|          40 | -20.51%  | 7.04%              | -32.11% |    -0.52 |       76 | 44.43%     | ok               |

## HYG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -7.94%   | 3.67%              | -8.13%  |    -0.95 |       72 | 29.95%     | ok               |
|          45 | -8.85%   | 3.67%              | -9.24%  |    -1.11 |       70 | 26.46%     | ok               |
|          15 | -10.27%  | 3.67%              | -11.48% |    -1.11 |       98 | 43.09%     | ok               |
|          30 | -9.70%   | 3.67%              | -10.59% |    -1.13 |       91 | 35.27%     | ok               |
|          20 | -10.16%  | 3.67%              | -11.64% |    -1.13 |       98 | 40.60%     | ok               |

## IBIT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 53.69%   | 14.92%             | -17.37% |     1    |       24 | 23.24%     | ok               |
|          15 | 56.87%   | 14.92%             | -19.20% |     0.9  |       42 | 39.23%     | ok               |
|          45 | 44.23%   | 14.92%             | -17.37% |     0.85 |       28 | 24.52%     | ok               |
|          40 | 38.00%   | 14.92%             | -17.78% |     0.76 |       28 | 26.23%     | ok               |
|          30 | 30.78%   | 14.92%             | -18.95% |     0.63 |       36 | 32.20%     | ok               |

## IBM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -19.41%  | 28.96%             | -49.43% |    -0.14 |       89 | 62.90%     | ok               |
|          35 | -24.24%  | 28.96%             | -47.10% |    -0.29 |       69 | 46.59%     | ok               |
|          30 | -25.87%  | 28.96%             | -48.94% |    -0.31 |       73 | 50.75%     | ok               |
|          20 | -30.94%  | 28.96%             | -53.45% |    -0.38 |       73 | 55.41%     | ok               |
|          50 | -29.24%  | 28.96%             | -45.88% |    -0.44 |       46 | 34.44%     | ok               |

## ICP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -0.04%   | -39.53%            | -44.60% |     0.21 |       68 | 30.65%     | ok               |
|          30 | -5.03%   | -39.53%            | -47.30% |     0.21 |       77 | 36.78%     | ok               |
|          40 | -1.73%   | -39.53%            | -38.04% |     0.18 |       58 | 25.48%     | ok               |
|          50 | -12.34%  | -39.53%            | -48.01% |     0    |       40 | 15.52%     | ok               |
|          15 | -37.07%  | -39.53%            | -58.26% |    -0.06 |       75 | 48.85%     | ok               |

## IEF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -7.44%   | -0.48%             | -10.32% |    -0.9  |       72 | 42.26%     | ok               |
|          15 | -7.99%   | -0.48%             | -11.04% |    -0.95 |       71 | 43.76%     | ok               |
|          50 | -7.73%   | -0.48%             | -9.11%  |    -1.38 |       54 | 20.13%     | ok               |
|          25 | -10.98%  | -0.48%             | -11.82% |    -1.42 |       76 | 39.60%     | ok               |
|          40 | -9.46%   | -0.48%             | -10.95% |    -1.46 |       66 | 25.29%     | ok               |

## IEMG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -1.30%   | 62.28%             | -14.22% |     0.01 |       54 | 32.78%     | ok               |
|          45 | -2.11%   | 62.28%             | -15.23% |    -0.02 |       50 | 35.27%     | ok               |
|          35 | -2.63%   | 62.28%             | -22.13% |    -0.03 |       65 | 40.43%     | ok               |
|          40 | -3.62%   | 62.28%             | -18.73% |    -0.08 |       62 | 38.27%     | ok               |
|          25 | -6.92%   | 62.28%             | -25.58% |    -0.17 |       61 | 43.26%     | ok               |

## INJ-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -26.17%  | -13.53%            | -55.24% |    -0.08 |       60 | 33.14%     | ok               |
|          45 | -25.96%  | -13.53%            | -48.45% |    -0.16 |       52 | 24.33%     | ok               |
|          40 | -29.13%  | -13.53%            | -51.61% |    -0.17 |       52 | 30.08%     | ok               |
|          15 | -61.16%  | -13.53%            | -81.76% |    -0.5  |       82 | 49.81%     | ok               |
|          30 | -54.28%  | -13.53%            | -74.43% |    -0.51 |       71 | 37.93%     | ok               |

## INTC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 59.75%   | 186.30%            | -49.32% |     0.66 |       58 | 33.11%     | ok               |
|          15 | 64.71%   | 186.30%            | -53.65% |     0.65 |       78 | 59.90%     | ok               |
|          50 | 58.00%   | 186.30%            | -48.35% |     0.65 |       62 | 28.79%     | ok               |
|          40 | 60.54%   | 186.30%            | -55.86% |     0.65 |       64 | 37.44%     | ok               |
|          25 | 48.20%   | 186.30%            | -56.41% |     0.57 |       77 | 50.75%     | ok               |

## INTU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 2.82%    | -48.59%            | -38.89% |     0.17 |       67 | 27.12%     | ok               |
|          45 | 0.82%    | -48.59%            | -39.95% |     0.13 |       65 | 31.11%     | ok               |
|          40 | -6.60%   | -48.59%            | -43.92% |     0    |       67 | 34.61%     | ok               |
|          25 | -9.57%   | -48.59%            | -39.21% |    -0.02 |       68 | 47.42%     | ok               |
|          15 | -13.56%  | -48.59%            | -43.23% |    -0.08 |       79 | 52.91%     | ok               |

## ITA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 1.39%    | 71.29%             | -21.48% |     0.11 |       72 | 37.94%     | ok               |
|          15 | -3.65%   | 71.29%             | -28.06% |     0    |       87 | 60.40%     | ok               |
|          30 | -2.77%   | 71.29%             | -23.75% |    -0    |       72 | 48.09%     | ok               |
|          35 | -4.80%   | 71.29%             | -23.16% |    -0.07 |       74 | 45.76%     | ok               |
|          40 | -4.98%   | 71.29%             | -20.58% |    -0.08 |       74 | 42.43%     | ok               |

## IWM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 11.70%   | 49.19%             | -13.94% |     0.51 |       48 | 32.28%     | ok               |
|          25 | 12.85%   | 49.19%             | -12.34% |     0.5  |       54 | 37.27%     | ok               |
|          35 | 11.49%   | 49.19%             | -13.94% |     0.47 |       52 | 34.44%     | ok               |
|          30 | 11.41%   | 49.19%             | -12.65% |     0.46 |       54 | 36.44%     | ok               |
|          20 | 11.36%   | 49.19%             | -12.12% |     0.44 |       60 | 38.27%     | ok               |

## JNJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 16.54%   | 82.76%             | -10.57% |     0.68 |       46 | 35.77%     | ok               |
|          15 | 7.46%    | 82.76%             | -18.02% |     0.3  |       64 | 55.24%     | ok               |
|          45 | 5.63%    | 82.76%             | -13.35% |     0.27 |       48 | 39.77%     | ok               |
|          20 | 2.49%    | 82.76%             | -17.61% |     0.15 |       70 | 51.75%     | ok               |
|          40 | 2.08%    | 82.76%             | -14.77% |     0.13 |       56 | 44.09%     | ok               |

## JPM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 6.98%    | 95.07%             | -15.90% |     0.29 |       52 | 35.27%     | ok               |
|          45 | -3.18%   | 95.07%             | -21.91% |    -0.03 |       54 | 38.27%     | ok               |
|          20 | -17.13%  | 95.07%             | -35.58% |    -0.33 |       82 | 52.41%     | ok               |
|          35 | -15.95%  | 95.07%             | -27.43% |    -0.42 |       74 | 44.59%     | ok               |
|          40 | -16.47%  | 95.07%             | -28.47% |    -0.44 |       66 | 40.93%     | ok               |

## KO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 27.17%   | 49.09%             | -8.64%  |     0.93 |       53 | 40.60%     | ok               |
|          35 | 22.08%   | 49.09%             | -8.21%  |     0.79 |       58 | 38.94%     | ok               |
|          40 | 19.14%   | 49.09%             | -9.28%  |     0.74 |       60 | 35.61%     | ok               |
|          25 | 20.80%   | 49.09%             | -10.16% |     0.74 |       59 | 43.43%     | ok               |
|          50 | 6.38%    | 49.09%             | -15.35% |     0.32 |       44 | 29.45%     | ok               |

## LDO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 44.17%   | -40.42%            | -48.17% |     0.59 |       78 | 60.34%     | ok               |
|          20 | 40.69%   | -40.42%            | -45.55% |     0.57 |       80 | 55.56%     | ok               |
|          30 | 10.25%   | -40.42%            | -61.16% |     0.36 |       74 | 47.13%     | ok               |
|          25 | 5.74%    | -40.42%            | -56.86% |     0.34 |       83 | 52.87%     | ok               |
|          35 | -3.00%   | -40.42%            | -61.98% |     0.23 |       78 | 38.89%     | ok               |

## LIN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -6.85%   | 3.40%              | -23.68% |    -0.17 |       72 | 46.26%     | ok               |
|          20 | -6.99%   | 3.40%              | -23.00% |    -0.18 |       64 | 41.93%     | ok               |
|          25 | -6.94%   | 3.40%              | -22.01% |    -0.19 |       67 | 39.10%     | ok               |
|          30 | -10.87%  | 3.40%              | -20.61% |    -0.35 |       70 | 36.27%     | ok               |
|          45 | -10.54%  | 3.40%              | -17.04% |    -0.42 |       42 | 20.47%     | ok               |

## LINK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 22.48%   | 5.34%              | -33.64% |     0.44 |       71 | 46.55%     | ok               |
|          45 | 21.61%   | 5.34%              | -33.71% |     0.43 |       50 | 31.42%     | ok               |
|          35 | 8.72%    | 5.34%              | -34.21% |     0.32 |       59 | 41.38%     | ok               |
|          40 | 2.75%    | 5.34%              | -34.00% |     0.25 |       55 | 35.63%     | ok               |
|          50 | 1.98%    | 5.34%              | -27.44% |     0.22 |       44 | 25.48%     | ok               |

## LLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 2.05%    | 50.55%             | -38.23% |     0.15 |       46 | 35.44%     | ok               |
|          15 | -7.29%   | 50.55%             | -48.12% |     0.03 |       63 | 58.24%     | ok               |
|          45 | -9.72%   | 50.55%             | -42.66% |    -0.08 |       52 | 38.77%     | ok               |
|          20 | -19.99%  | 50.55%             | -51.34% |    -0.21 |       70 | 53.41%     | ok               |
|          25 | -21.31%  | 50.55%             | -53.47% |    -0.25 |       66 | 50.75%     | ok               |

## LRCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -13.68%  | 235.25%            | -48.71% |    -0.02 |       76 | 33.61%     | ok               |
|          40 | -18.39%  | 235.25%            | -55.33% |    -0.06 |       72 | 39.60%     | ok               |
|          35 | -19.96%  | 235.25%            | -58.47% |    -0.08 |       80 | 41.76%     | ok               |
|          30 | -25.21%  | 235.25%            | -61.08% |    -0.15 |       84 | 42.43%     | ok               |
|          15 | -30.37%  | 235.25%            | -56.86% |    -0.16 |       87 | 52.25%     | ok               |

## LTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -10.02%  | -23.25%            | -34.94% |     0.04 |       68 | 44.25%     | ok               |
|          30 | -16.41%  | -23.25%            | -33.94% |    -0.03 |       70 | 51.92%     | ok               |
|          45 | -15.28%  | -23.25%            | -37.29% |    -0.07 |       58 | 33.14%     | ok               |
|          25 | -22.38%  | -23.25%            | -34.22% |    -0.11 |       74 | 54.60%     | ok               |
|          40 | -20.99%  | -23.25%            | -40.31% |    -0.16 |       56 | 38.51%     | ok               |

## MCD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 3.05%    | -6.62%             | -9.22%  |     0.19 |       44 | 21.96%     | ok               |
|          45 | -4.74%   | -6.62%             | -16.79% |    -0.19 |       52 | 25.62%     | ok               |
|          30 | -6.47%   | -6.62%             | -21.88% |    -0.21 |       77 | 36.94%     | ok               |
|          40 | -6.01%   | -6.62%             | -18.49% |    -0.23 |       67 | 28.95%     | ok               |
|          25 | -7.47%   | -6.62%             | -23.62% |    -0.25 |       77 | 39.60%     | ok               |

## META Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -21.54%  | 28.41%             | -37.54% |    -0.36 |       68 | 36.61%     | ok               |
|          40 | -26.61%  | 28.41%             | -40.90% |    -0.46 |       70 | 40.10%     | ok               |
|          50 | -30.27%  | 28.41%             | -39.33% |    -0.61 |       70 | 32.45%     | ok               |
|          25 | -36.38%  | 28.41%             | -45.70% |    -0.64 |       75 | 50.58%     | ok               |
|          30 | -36.40%  | 28.41%             | -44.90% |    -0.66 |       78 | 47.59%     | ok               |

## MPC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 36.10%   | 101.22%            | -18.24% |     0.7  |       48 | 38.60%     | ok               |
|          45 | 27.46%   | 101.22%            | -19.46% |     0.56 |       54 | 42.26%     | ok               |
|          40 | 22.65%   | 101.22%            | -20.11% |     0.49 |       56 | 44.43%     | ok               |
|          35 | 18.86%   | 101.22%            | -31.08% |     0.42 |       64 | 46.92%     | ok               |
|          30 | 4.70%    | 101.22%            | -37.91% |     0.2  |       67 | 49.42%     | ok               |

## MRK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -11.92%  | 15.56%             | -29.09% |    -0.13 |       85 | 53.74%     | ok               |
|          25 | -11.92%  | 15.56%             | -31.07% |    -0.15 |       72 | 46.59%     | ok               |
|          20 | -16.23%  | 15.56%             | -29.34% |    -0.24 |       77 | 49.92%     | ok               |
|          50 | -15.53%  | 15.56%             | -24.92% |    -0.32 |       58 | 30.45%     | ok               |
|          45 | -17.63%  | 15.56%             | -25.38% |    -0.36 |       59 | 33.78%     | ok               |

## MS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 2.51%    | 135.61%            | -19.99% |     0.14 |       70 | 39.60%     | ok               |
|          15 | 0.33%    | 135.61%            | -22.02% |     0.1  |       71 | 56.74%     | ok               |
|          20 | 0.21%    | 135.61%            | -25.68% |     0.09 |       75 | 52.91%     | ok               |
|          30 | -5.41%   | 135.61%            | -27.79% |    -0.05 |       75 | 47.92%     | ok               |
|          35 | -5.34%   | 135.61%            | -25.26% |    -0.05 |       76 | 44.43%     | ok               |

## MSFT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -14.20%  | 21.81%             | -25.54% |    -0.32 |       68 | 36.11%     | ok               |
|          50 | -20.54%  | 21.81%             | -26.37% |    -0.55 |       62 | 30.78%     | ok               |
|          35 | -27.17%  | 21.81%             | -36.28% |    -0.64 |       71 | 45.26%     | ok               |
|          40 | -27.20%  | 21.81%             | -35.70% |    -0.67 |       69 | 39.93%     | ok               |
|          30 | -29.20%  | 21.81%             | -38.06% |    -0.67 |       79 | 49.42%     | ok               |

## MU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 198.28%  | 773.23%            | -64.36% |     1.2  |       54 | 49.42%     | ok               |
|          15 | 233.19%  | 773.23%            | -61.96% |     1.19 |       51 | 62.23%     | ok               |
|          25 | 175.56%  | 773.23%            | -67.90% |     1.1  |       49 | 55.57%     | ok               |
|          30 | 164.65%  | 773.23%            | -68.76% |     1.08 |       49 | 53.91%     | ok               |
|          35 | 158.86%  | 773.23%            | -69.15% |     1.07 |       61 | 51.75%     | ok               |

## NEAR-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 57.89%   | 28.70%             | -57.15% |     0.71 |       42 | 28.93%     | ok               |
|          45 | 56.75%   | 28.70%             | -48.95% |     0.71 |       42 | 24.90%     | ok               |
|          50 | 37.23%   | 28.70%             | -53.13% |     0.57 |       32 | 20.11%     | ok               |
|          35 | 27.13%   | 28.70%             | -61.02% |     0.48 |       64 | 33.52%     | ok               |
|          30 | 12.88%   | 28.70%             | -59.86% |     0.37 |       77 | 42.15%     | ok               |

## NEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 20.77%   | 227.21%            | -31.25% |     0.4  |       58 | 60.73%     | ok               |
|          20 | 11.71%   | 227.21%            | -30.50% |     0.31 |       66 | 56.91%     | ok               |
|          25 | -6.17%   | 227.21%            | -39.51% |     0.09 |       64 | 55.07%     | ok               |
|          30 | -17.93%  | 227.21%            | -39.56% |    -0.09 |       68 | 53.41%     | ok               |
|          50 | -16.40%  | 227.21%            | -33.24% |    -0.12 |       56 | 40.77%     | ok               |

## NFLX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 41.22%   | 24.49%             | -13.37% |     0.91 |       48 | 42.43%     | ok               |
|          50 | 37.08%   | 24.49%             | -16.28% |     0.89 |       44 | 34.78%     | ok               |
|          35 | 41.25%   | 24.49%             | -18.30% |     0.86 |       70 | 46.92%     | ok               |
|          45 | 25.95%   | 24.49%             | -15.48% |     0.65 |       54 | 38.94%     | ok               |
|          15 | 24.42%   | 24.49%             | -26.59% |     0.51 |       71 | 65.06%     | ok               |

## NKE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -17.30%  | -61.75%            | -42.13% |    -0.18 |       69 | 37.60%     | ok               |
|          20 | -21.82%  | -61.75%            | -49.34% |    -0.19 |       83 | 49.92%     | ok               |
|          25 | -25.06%  | -61.75%            | -51.20% |    -0.26 |       83 | 47.25%     | ok               |
|          15 | -26.87%  | -61.75%            | -54.28% |    -0.28 |       86 | 53.74%     | ok               |
|          40 | -18.96%  | -61.75%            | -31.79% |    -0.31 |       63 | 29.62%     | ok               |

## NOW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 4.16%    | -10.32%            | -30.43% |     0.22 |       84 | 49.75%     | ok               |
|          20 | 1.68%    | -10.32%            | -39.71% |     0.2  |       81 | 56.07%     | ok               |
|          25 | -1.82%   | -10.32%            | -37.51% |     0.16 |       78 | 53.08%     | ok               |
|          15 | -5.75%   | -10.32%            | -43.06% |     0.12 |       89 | 59.07%     | ok               |
|          40 | -4.16%   | -10.32%            | -36.21% |     0.09 |       76 | 39.27%     | ok               |

## NVDA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -41.20%  | 65.57%             | -45.53% |    -0.52 |       76 | 54.72%     | ok               |
|          30 | -36.51%  | 65.57%             | -41.21% |    -0.53 |       78 | 46.52%     | ok               |
|          25 | -41.10%  | 65.57%             | -45.44% |    -0.57 |       77 | 49.73%     | ok               |
|          15 | -47.57%  | 65.57%             | -52.37% |    -0.62 |       77 | 57.93%     | ok               |
|          35 | -46.83%  | 65.57%             | -49.15% |    -0.81 |       88 | 43.49%     | ok               |

## OP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 8.35%    | -83.69%            | -31.68% |     0.28 |       32 | 10.15%     | ok               |
|          45 | -22.57%  | -83.69%            | -51.17% |    -0.15 |       36 | 14.75%     | ok               |
|          40 | -31.56%  | -83.69%            | -60.08% |    -0.24 |       48 | 22.99%     | ok               |
|          30 | -49.54%  | -83.69%            | -68.74% |    -0.47 |       70 | 34.10%     | ok               |
|          35 | -48.18%  | -83.69%            | -63.95% |    -0.52 |       56 | 27.97%     | ok               |

## ORCL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 167.02%  | 31.84%             | -32.54% |     1.11 |       75 | 64.73%     | ok               |
|          45 | 102.05%  | 31.84%             | -32.35% |     0.93 |       60 | 41.10%     | ok               |
|          25 | 114.69%  | 31.84%             | -27.76% |     0.93 |       67 | 57.24%     | ok               |
|          20 | 108.71%  | 31.84%             | -29.32% |     0.9  |       76 | 60.40%     | ok               |
|          35 | 98.56%   | 31.84%             | -31.95% |     0.88 |       70 | 50.58%     | ok               |

## OXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -3.70%   | -7.39%             | -27.20% |     0.05 |       76 | 38.60%     | ok               |
|          30 | -6.02%   | -7.39%             | -31.83% |     0.02 |       77 | 44.09%     | ok               |
|          50 | -5.00%   | -7.39%             | -26.98% |     0    |       44 | 26.79%     | ok               |
|          40 | -8.69%   | -7.39%             | -28.30% |    -0.06 |       62 | 33.94%     | ok               |
|          25 | -18.96%  | -7.39%             | -42.27% |    -0.22 |       85 | 48.25%     | ok               |

## PEP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 14.52%   | -20.68%            | -11.62% |     0.65 |       40 | 25.62%     | ok               |
|          45 | 8.36%    | -20.68%            | -14.22% |     0.39 |       56 | 29.78%     | ok               |
|          35 | 4.57%    | -20.68%            | -21.42% |     0.21 |       77 | 40.10%     | ok               |
|          40 | 2.32%    | -20.68%            | -18.04% |     0.14 |       70 | 35.44%     | ok               |
|          30 | -0.06%   | -20.68%            | -21.35% |     0.07 |       74 | 46.09%     | ok               |

## PEPE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -38.54%  | -45.16%            | -61.96% |    -0.02 |       80 | 63.03%     | ok               |
|          30 | -39.87%  | -45.16%            | -57.66% |    -0.17 |       89 | 47.70%     | ok               |
|          20 | -44.58%  | -45.16%            | -61.13% |    -0.17 |       86 | 59.58%     | ok               |
|          25 | -41.49%  | -45.16%            | -53.88% |    -0.17 |       93 | 53.64%     | ok               |
|          35 | -38.97%  | -45.16%            | -54.42% |    -0.22 |       72 | 41.76%     | ok               |

## PFE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -19.32%  | 8.90%              | -23.51% |    -0.63 |       56 | 22.63%     | ok               |
|          50 | -19.80%  | 8.90%              | -26.54% |    -0.71 |       44 | 18.97%     | ok               |
|          40 | -25.65%  | 8.90%              | -30.63% |    -0.81 |       76 | 27.79%     | ok               |
|          35 | -29.61%  | 8.90%              | -35.77% |    -0.88 |       88 | 35.44%     | ok               |
|          30 | -38.10%  | 8.90%              | -43.50% |    -1.13 |       83 | 40.10%     | ok               |

## PG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -9.01%   | -9.10%             | -20.08% |    -0.34 |       56 | 30.95%     | ok               |
|          35 | -12.11%  | -9.10%             | -18.99% |    -0.45 |       64 | 34.44%     | ok               |
|          30 | -20.10%  | -9.10%             | -24.55% |    -0.77 |       66 | 37.60%     | ok               |
|          45 | -17.90%  | -9.10%             | -22.43% |    -0.79 |       56 | 28.45%     | ok               |
|          25 | -21.92%  | -9.10%             | -26.24% |    -0.85 |       78 | 39.10%     | ok               |

## PM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 1.81%    | 108.08%            | -32.20% |     0.13 |       84 | 50.42%     | ok               |
|          20 | -0.85%   | 108.08%            | -33.51% |     0.08 |       83 | 59.07%     | ok               |
|          30 | -1.38%   | 108.08%            | -35.15% |     0.07 |       79 | 53.91%     | ok               |
|          50 | -5.47%   | 108.08%            | -35.70% |    -0.06 |       68 | 40.60%     | ok               |
|          40 | -5.96%   | 108.08%            | -37.94% |    -0.06 |       78 | 46.42%     | ok               |

## POL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 24.65%   | -44.21%            | -45.67% |     0.46 |       81 | 49.62%     | ok               |
|          25 | 15.98%   | -44.21%            | -46.72% |     0.39 |       68 | 56.32%     | ok               |
|          20 | -1.02%   | -44.21%            | -52.88% |     0.23 |       76 | 60.54%     | ok               |
|          50 | -0.36%   | -44.21%            | -26.14% |     0.14 |       48 | 19.73%     | ok               |
|          15 | -18.56%  | -44.21%            | -58.42% |     0.05 |       79 | 65.13%     | ok               |

## QCOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -3.20%   | 9.56%              | -54.50% |     0.13 |       71 | 44.43%     | ok               |
|          20 | -11.72%  | 9.56%              | -54.38% |     0.03 |       69 | 47.59%     | ok               |
|          35 | -10.49%  | 9.56%              | -50.58% |     0.02 |       77 | 40.10%     | ok               |
|          30 | -20.09%  | 9.56%              | -56.59% |    -0.12 |       75 | 42.43%     | ok               |
|          15 | -25.32%  | 9.56%              | -57.94% |    -0.17 |       73 | 50.75%     | ok               |

## QQQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 27.72%   | 67.38%             | -14.17% |     0.67 |       65 | 54.58%     | ok               |
|          25 | 19.05%   | 67.38%             | -12.88% |     0.53 |       63 | 48.59%     | ok               |
|          20 | 17.83%   | 67.38%             | -12.98% |     0.49 |       71 | 51.25%     | ok               |
|          30 | 13.22%   | 67.38%             | -14.20% |     0.41 |       66 | 46.42%     | ok               |
|          35 | 1.58%    | 67.38%             | -20.59% |     0.12 |       72 | 42.60%     | ok               |

## RENDER-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 24.52%   | -49.82%            | -43.43% |     0.47 |       95 | 57.28%     | ok               |
|          15 | 16.40%   | -49.82%            | -44.59% |     0.42 |       90 | 61.11%     | ok               |
|          25 | 12.56%   | -49.82%            | -40.60% |     0.39 |       93 | 52.68%     | ok               |
|          30 | -31.90%  | -49.82%            | -44.84% |    -0.08 |      102 | 45.98%     | ok               |
|          35 | -33.53%  | -49.82%            | -43.79% |    -0.17 |       84 | 38.12%     | ok               |

## RTX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 41.76%   | 96.72%             | -18.66% |     0.87 |       74 | 57.24%     | ok               |
|          25 | 36.91%   | 96.72%             | -18.59% |     0.8  |       62 | 54.58%     | ok               |
|          30 | 32.91%   | 96.72%             | -16.99% |     0.74 |       56 | 53.08%     | ok               |
|          15 | 34.02%   | 96.72%             | -19.55% |     0.73 |       69 | 62.06%     | ok               |
|          35 | 28.24%   | 96.72%             | -18.00% |     0.72 |       52 | 50.58%     | ok               |

## SBUX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -8.48%   | 13.85%             | -23.55% |    -0.09 |       55 | 40.10%     | ok               |
|          45 | -11.25%  | 13.85%             | -27.26% |    -0.21 |       64 | 28.95%     | ok               |
|          40 | -12.97%  | 13.85%             | -25.43% |    -0.24 |       60 | 32.45%     | ok               |
|          30 | -18.02%  | 13.85%             | -29.22% |    -0.33 |       58 | 37.94%     | ok               |
|          50 | -15.88%  | 13.85%             | -25.30% |    -0.37 |       54 | 24.96%     | ok               |

## SCHW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 1.64%    | 47.17%             | -16.53% |     0.12 |       62 | 34.11%     | ok               |
|          25 | -0.57%   | 47.17%             | -28.76% |     0.08 |       65 | 50.42%     | ok               |
|          20 | -4.14%   | 47.17%             | -29.24% |    -0    |       73 | 52.91%     | ok               |
|          50 | -4.16%   | 47.17%             | -13.28% |    -0.08 |       58 | 31.11%     | ok               |
|          40 | -7.93%   | 47.17%             | -23.35% |    -0.14 |       68 | 37.60%     | ok               |

## SHIB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -31.49%  | -52.05%            | -38.26% |    -0.18 |       77 | 60.54%     | ok               |
|          20 | -37.02%  | -52.05%            | -41.07% |    -0.27 |       79 | 63.98%     | ok               |
|          15 | -38.54%  | -52.05%            | -45.04% |    -0.28 |       84 | 68.20%     | ok               |
|          35 | -39.25%  | -52.05%            | -48.18% |    -0.39 |       76 | 46.55%     | ok               |
|          30 | -43.72%  | -52.05%            | -40.60% |    -0.45 |       84 | 53.07%     | ok               |

## SHY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          30 | -2.45%   | 0.33%              | -3.30% |    -0.85 |       50 | 34.61%     | ok               |
|          45 | -2.48%   | 0.33%              | -3.43% |    -0.93 |       50 | 26.29%     | ok               |
|          35 | -2.85%   | 0.33%              | -3.61% |    -1    |       54 | 32.61%     | ok               |
|          40 | -2.87%   | 0.33%              | -3.58% |    -1.02 |       56 | 31.28%     | ok               |
|          50 | -2.65%   | 0.33%              | -3.40% |    -1.05 |       46 | 22.80%     | ok               |

## SKY-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -31.07%  | 3.32%              | -47.82% |    -0.32 |       80 | 45.40%     | ok               |
|          15 | -39.27%  | 3.32%              | -56.39% |    -0.4  |       68 | 54.60%     | ok               |
|          25 | -38.63%  | 3.32%              | -52.77% |    -0.45 |       73 | 48.92%     | ok               |
|          35 | -37.00%  | 3.32%              | -49.68% |    -0.51 |       74 | 37.77%     | ok               |
|          20 | -47.98%  | 3.32%              | -61.38% |    -0.61 |       70 | 52.05%     | ok               |

## SLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 22.62%   | 9.95%              | -20.46% |     0.52 |       54 | 34.11%     | ok               |
|          40 | 20.90%   | 9.95%              | -23.07% |     0.48 |       46 | 37.77%     | ok               |
|          50 | 2.19%    | 9.95%              | -28.89% |     0.14 |       50 | 29.95%     | ok               |
|          35 | -9.82%   | 9.95%              | -41.81% |    -0.08 |       72 | 44.59%     | ok               |
|          30 | -28.18%  | 9.95%              | -54.95% |    -0.47 |       77 | 50.92%     | ok               |

## SLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 38.97%   | 122.35%            | -34.10% |     0.61 |       56 | 31.45%     | ok               |
|          45 | 29.54%   | 122.35%            | -31.82% |     0.51 |       63 | 32.95%     | ok               |
|          40 | 27.99%   | 122.35%            | -33.52% |     0.5  |       69 | 35.11%     | ok               |
|          15 | 17.97%   | 122.35%            | -47.98% |     0.38 |       74 | 51.58%     | ok               |
|          20 | 17.16%   | 122.35%            | -42.66% |     0.38 |       73 | 46.26%     | ok               |

## SMH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 86.99%   | 168.55%            | -31.66% |     1.13 |       49 | 47.92%     | ok               |
|          35 | 70.33%   | 168.55%            | -34.65% |     1.02 |       54 | 43.26%     | ok               |
|          25 | 69.26%   | 168.55%            | -33.57% |     1    |       46 | 46.59%     | ok               |
|          30 | 67.47%   | 168.55%            | -34.29% |     0.99 |       48 | 44.93%     | ok               |
|          45 | 55.28%   | 168.55%            | -33.35% |     0.93 |       54 | 37.44%     | ok               |

## SNX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -16.61%  | -64.66%            | -37.62% |     0.01 |       56 | 27.39%     | ok               |
|          20 | -23.11%  | -64.66%            | -47.56% |    -0    |       71 | 44.44%     | ok               |
|          40 | -19.99%  | -64.66%            | -36.94% |    -0.11 |       46 | 22.61%     | ok               |
|          30 | -27.61%  | -64.66%            | -47.16% |    -0.12 |       62 | 34.10%     | ok               |
|          15 | -46.35%  | -64.66%            | -49.47% |    -0.31 |       81 | 49.43%     | ok               |

## SOL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 28.31%   | -5.57%             | -38.17% |     0.5  |       52 | 37.93%     | ok               |
|          35 | 6.93%    | -5.57%             | -43.70% |     0.29 |       64 | 44.44%     | ok               |
|          45 | -0.75%   | -5.57%             | -46.37% |     0.18 |       56 | 32.57%     | ok               |
|          25 | -12.80%  | -5.57%             | -41.09% |     0.09 |       68 | 57.28%     | ok               |
|          30 | -16.77%  | -5.57%             | -45.53% |     0.03 |       78 | 52.11%     | ok               |

## SOXX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 74.69%   | 150.41%            | -39.65% |     0.99 |       56 | 45.76%     | ok               |
|          35 | 70.38%   | 150.41%            | -38.76% |     0.97 |       58 | 40.93%     | ok               |
|          30 | 68.55%   | 150.41%            | -40.14% |     0.94 |       58 | 43.43%     | ok               |
|          20 | 61.49%   | 150.41%            | -38.67% |     0.86 |       61 | 46.59%     | ok               |
|          40 | 48.85%   | 150.41%            | -41.03% |     0.78 |       58 | 38.77%     | ok               |

## SPY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 13.55%   | 51.71%             | -14.25% |     0.49 |       61 | 55.57%     | ok               |
|          15 | 12.87%   | 51.71%             | -16.80% |     0.46 |       67 | 58.57%     | ok               |
|          25 | 8.06%    | 51.71%             | -14.25% |     0.33 |       61 | 54.41%     | ok               |
|          30 | 3.49%    | 51.71%             | -15.53% |     0.18 |       64 | 51.58%     | ok               |
|          35 | 2.49%    | 51.71%             | -15.58% |     0.15 |       62 | 48.42%     | ok               |

## SUSHI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -24.68%  | -55.67%            | -34.75% |    -0.22 |       54 | 14.94%     | ok               |
|          45 | -68.31%  | -55.67%            | -65.10% |    -1.1  |       58 | 19.35%     | ok               |
|          40 | -72.25%  | -55.67%            | -69.43% |    -1.15 |       63 | 25.86%     | ok               |
|          15 | -82.79%  | -55.67%            | -81.47% |    -1.2  |       91 | 48.66%     | ok               |
|          35 | -78.70%  | -55.67%            | -77.07% |    -1.32 |       86 | 31.23%     | ok               |

## T Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 62.92%   | 56.46%             | -15.08% |     1.12 |       73 | 66.89%     | ok               |
|          20 | 58.90%   | 56.46%             | -18.13% |     1.1  |       68 | 62.40%     | ok               |
|          25 | 54.60%   | 56.46%             | -17.66% |     1.06 |       68 | 60.07%     | ok               |
|          30 | 37.66%   | 56.46%             | -17.01% |     0.82 |       72 | 58.07%     | ok               |
|          35 | 22.66%   | 56.46%             | -14.49% |     0.57 |       78 | 53.74%     | ok               |

## TGT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -12.70%  | -6.51%             | -36.37% |    -0.2  |       60 | 37.77%     | ok               |
|          25 | -13.74%  | -6.51%             | -39.65% |    -0.21 |       66 | 40.43%     | ok               |
|          20 | -15.49%  | -6.51%             | -40.95% |    -0.22 |       84 | 45.09%     | ok               |
|          45 | -12.96%  | -6.51%             | -26.68% |    -0.25 |       52 | 28.79%     | ok               |
|          15 | -21.98%  | -6.51%             | -40.65% |    -0.35 |       76 | 49.25%     | ok               |

## TIA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -42.74%  | -83.92%            | -63.05% |    -0.11 |       94 | 58.62%     | ok               |
|          35 | -39.50%  | -83.92%            | -60.91% |    -0.26 |       72 | 35.06%     | ok               |
|          20 | -57.24%  | -83.92%            | -64.15% |    -0.38 |       90 | 53.26%     | ok               |
|          25 | -56.26%  | -83.92%            | -63.32% |    -0.4  |       93 | 47.51%     | ok               |
|          45 | -38.58%  | -83.92%            | -62.76% |    -0.43 |       60 | 19.73%     | ok               |

## TLT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -19.20%  | -9.06%             | -21.87% |    -1.4  |       72 | 35.11%     | ok               |
|          40 | -18.03%  | -9.06%             | -18.31% |    -1.61 |       58 | 24.46%     | ok               |
|          50 | -14.00%  | -9.06%             | -15.03% |    -1.63 |       36 | 15.64%     | ok               |
|          15 | -24.90%  | -9.06%             | -27.76% |    -1.66 |       79 | 43.26%     | ok               |
|          35 | -20.65%  | -9.06%             | -21.63% |    -1.71 |       66 | 29.12%     | ok               |

## TMO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 48.61%   | 11.39%             | -8.17%  |     1.06 |       44 | 33.61%     | ok               |
|          45 | 42.82%   | 11.39%             | -9.69%  |     0.92 |       48 | 38.44%     | ok               |
|          40 | 38.64%   | 11.39%             | -9.91%  |     0.83 |       53 | 43.26%     | ok               |
|          35 | 33.32%   | 11.39%             | -13.84% |     0.7  |       65 | 48.59%     | ok               |
|          30 | 24.66%   | 11.39%             | -18.85% |     0.54 |       65 | 54.08%     | ok               |

## TMUS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 2.41%    | 10.14%             | -27.06% |     0.15 |       76 | 48.25%     | ok               |
|          15 | -1.02%   | 10.14%             | -34.48% |     0.08 |       68 | 60.90%     | ok               |
|          25 | -5.27%   | 10.14%             | -32.65% |    -0.01 |       79 | 51.08%     | ok               |
|          20 | -6.73%   | 10.14%             | -33.09% |    -0.04 |       74 | 55.24%     | ok               |
|          50 | -6.53%   | 10.14%             | -29.49% |    -0.11 |       60 | 34.94%     | ok               |

## TRX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 19.40%   | 47.51%             | -18.79% |     0.62 |       54 | 40.42%     | ok               |
|          35 | 12.97%   | 47.51%             | -21.77% |     0.43 |       68 | 49.23%     | ok               |
|          20 | 12.33%   | 47.51%             | -25.45% |     0.39 |       61 | 59.39%     | ok               |
|          30 | 10.93%   | 47.51%             | -22.90% |     0.38 |       68 | 52.30%     | ok               |
|          25 | 8.24%    | 47.51%             | -26.84% |     0.3  |       66 | 55.94%     | ok               |

## TSLA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 41.91%   | 142.49%            | -30.57% |     0.61 |       62 | 29.78%     | ok               |
|          40 | 14.07%   | 142.49%            | -50.11% |     0.34 |       61 | 35.27%     | ok               |
|          45 | -10.25%  | 142.49%            | -52.01% |     0.07 |       67 | 32.28%     | ok               |
|          35 | -17.74%  | 142.49%            | -58.86% |     0    |       72 | 37.94%     | ok               |
|          30 | -33.80%  | 142.49%            | -58.36% |    -0.2  |       78 | 42.93%     | ok               |

## TXN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 14.88%   | 58.14%             | -45.45% |     0.36 |       60 | 32.11%     | ok               |
|          35 | -4.29%   | 58.14%             | -43.38% |     0.07 |       68 | 46.26%     | ok               |
|          40 | -6.31%   | 58.14%             | -45.67% |     0.03 |       66 | 44.26%     | ok               |
|          20 | -11.77%  | 58.14%             | -38.98% |    -0.01 |       64 | 55.91%     | ok               |
|          45 | -9.87%   | 58.14%             | -46.24% |    -0.04 |       74 | 38.44%     | ok               |

## UNH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 32.56%   | -21.27%            | -26.31% |     0.55 |       74 | 50.25%     | ok               |
|          50 | 25.76%   | -21.27%            | -36.71% |     0.49 |       54 | 29.45%     | ok               |
|          35 | 25.77%   | -21.27%            | -27.21% |     0.48 |       68 | 44.93%     | ok               |
|          15 | 25.90%   | -21.27%            | -28.45% |     0.46 |       77 | 65.89%     | ok               |
|          25 | 20.62%   | -21.27%            | -25.25% |     0.41 |       72 | 55.24%     | ok               |

## UNI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 7.69%    | 27.42%             | -49.16% |     0.31 |       52 | 24.71%     | ok               |
|          45 | -15.87%  | 27.42%             | -53.77% |     0.06 |       60 | 31.99%     | ok               |
|          40 | -26.17%  | 27.42%             | -61.16% |    -0.06 |       64 | 36.40%     | ok               |
|          35 | -36.77%  | 27.42%             | -66.07% |    -0.17 |       76 | 42.34%     | ok               |
|          20 | -71.01%  | 27.42%             | -81.34% |    -0.67 |       97 | 58.24%     | ok               |

## UPS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -29.07%  | -29.96%            | -31.52% |    -0.55 |       62 | 34.28%     | ok               |
|          40 | -29.19%  | -29.96%            | -31.37% |    -0.57 |       58 | 28.95%     | ok               |
|          20 | -34.44%  | -29.96%            | -38.08% |    -0.64 |       84 | 47.59%     | ok               |
|          25 | -34.97%  | -29.96%            | -38.37% |    -0.68 |       76 | 44.26%     | ok               |
|          15 | -36.76%  | -29.96%            | -40.07% |    -0.69 |       86 | 51.41%     | ok               |

## USO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 22.23%   | 101.04%            | -43.31% |     0.43 |       75 | 37.94%     | ok               |
|          45 | 20.64%   | 101.04%            | -32.35% |     0.43 |       46 | 24.96%     | ok               |
|          25 | 17.41%   | 101.04%            | -42.99% |     0.38 |       69 | 35.11%     | ok               |
|          15 | 16.46%   | 101.04%            | -42.96% |     0.36 |       74 | 41.10%     | ok               |
|          30 | 12.34%   | 101.04%            | -41.71% |     0.31 |       70 | 31.95%     | ok               |

## VEA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 3.84%    | 50.37%             | -16.09% |     0.2  |       58 | 49.92%     | ok               |
|          20 | -1.07%   | 50.37%             | -17.70% |     0.01 |       61 | 47.09%     | ok               |
|          25 | -4.15%   | 50.37%             | -17.79% |    -0.11 |       57 | 45.26%     | ok               |
|          30 | -4.31%   | 50.37%             | -17.93% |    -0.13 |       58 | 43.09%     | ok               |
|          35 | -5.38%   | 50.37%             | -16.79% |    -0.17 |       56 | 42.10%     | ok               |

## VIXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -55.17%  | -69.73%            | -69.78% |    -0.63 |       40 | 10.82%     | ok               |
|          15 | -75.80%  | -69.73%            | -89.47% |    -0.75 |       97 | 45.59%     | ok               |
|          45 | -64.78%  | -69.73%            | -75.03% |    -0.84 |       60 | 15.81%     | ok               |
|          30 | -78.35%  | -69.73%            | -88.17% |    -0.94 |      100 | 34.61%     | ok               |
|          20 | -80.65%  | -69.73%            | -90.29% |    -0.94 |       93 | 41.60%     | ok               |

## VNQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -9.92%   | 19.72%             | -19.07% |    -0.44 |       60 | 28.79%     | ok               |
|          50 | -10.35%  | 19.72%             | -17.13% |    -0.48 |       56 | 26.29%     | ok               |
|          25 | -13.01%  | 19.72%             | -22.34% |    -0.5  |       71 | 41.43%     | ok               |
|          40 | -14.34%  | 19.72%             | -24.84% |    -0.63 |       74 | 32.61%     | ok               |
|          20 | -17.27%  | 19.72%             | -24.00% |    -0.68 |       76 | 44.59%     | ok               |

## VTI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 14.24%   | 51.01%             | -13.96% |     0.51 |       64 | 56.07%     | ok               |
|          15 | 9.25%    | 51.01%             | -15.70% |     0.35 |       63 | 58.74%     | ok               |
|          25 | 1.65%    | 51.01%             | -15.00% |     0.12 |       60 | 53.74%     | ok               |
|          30 | -5.97%   | 51.01%             | -17.64% |    -0.16 |       70 | 51.75%     | ok               |
|          40 | -7.10%   | 51.01%             | -19.77% |    -0.22 |       74 | 44.26%     | ok               |

## VWO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -7.95%   | 46.16%             | -21.68% |    -0.29 |       56 | 29.78%     | ok               |
|          45 | -9.75%   | 46.16%             | -23.75% |    -0.36 |       58 | 32.28%     | ok               |
|          15 | -11.71%  | 46.16%             | -24.01% |    -0.36 |       74 | 47.92%     | ok               |
|          40 | -10.21%  | 46.16%             | -23.57% |    -0.37 |       68 | 35.11%     | ok               |
|          20 | -13.11%  | 46.16%             | -26.14% |    -0.43 |       71 | 45.59%     | ok               |

## VZ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 1.31%    | 24.52%             | -12.55% |     0.11 |       52 | 27.29%     | ok               |
|          45 | -10.35%  | 24.52%             | -21.44% |    -0.28 |       66 | 31.11%     | ok               |
|          25 | -12.74%  | 24.52%             | -22.13% |    -0.3  |       79 | 44.93%     | ok               |
|          35 | -11.63%  | 24.52%             | -22.73% |    -0.31 |       61 | 36.94%     | ok               |
|          40 | -16.57%  | 24.52%             | -24.21% |    -0.5  |       66 | 34.28%     | ok               |

## WFC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -7.48%   | 52.28%             | -21.57% |    -0.09 |       77 | 43.76%     | ok               |
|          50 | -4.95%   | 52.28%             | -18.29% |    -0.09 |       58 | 32.28%     | ok               |
|          20 | -18.09%  | 52.28%             | -29.87% |    -0.26 |       77 | 52.41%     | ok               |
|          30 | -17.12%  | 52.28%             | -28.90% |    -0.28 |       80 | 46.92%     | ok               |
|          40 | -13.20%  | 52.28%             | -23.94% |    -0.31 |       72 | 40.43%     | ok               |

## WIF-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 34.71%   | -39.28%            | -40.67% |     0.53 |       65 | 44.06%     | ok               |
|          15 | 5.27%    | -39.28%            | -46.21% |     0.36 |       75 | 47.32%     | ok               |
|          25 | -30.82%  | -39.28%            | -52.98% |     0.01 |       69 | 40.04%     | ok               |
|          30 | -49.89%  | -39.28%            | -61.76% |    -0.31 |       66 | 36.21%     | ok               |
|          50 | -28.12%  | -39.28%            | -37.87% |    -0.31 |       38 | 12.26%     | ok               |

## WMT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 38.72%   | 78.42%             | -11.62% |     1.11 |       40 | 39.10%     | ok               |
|          50 | 33.90%   | 78.42%             | -12.19% |     1.05 |       32 | 36.77%     | ok               |
|          35 | 29.02%   | 78.42%             | -16.55% |     0.83 |       56 | 45.26%     | ok               |
|          40 | 27.36%   | 78.42%             | -15.99% |     0.82 |       48 | 40.60%     | ok               |
|          15 | 14.75%   | 78.42%             | -25.74% |     0.41 |       72 | 58.24%     | ok               |

## XBI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 11.48%   | 87.85%             | -16.08% |     0.35 |       58 | 37.44%     | ok               |
|          45 | 10.67%   | 87.85%             | -15.46% |     0.34 |       52 | 34.28%     | ok               |
|          35 | 2.70%    | 87.85%             | -16.96% |     0.15 |       64 | 41.10%     | ok               |
|          50 | 2.21%    | 87.85%             | -15.97% |     0.14 |       54 | 30.78%     | ok               |
|          30 | 0.56%    | 87.85%             | -18.30% |     0.1  |       66 | 42.60%     | ok               |

## XLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -2.33%   | 14.03%             | -18.27% |    -0.04 |       54 | 26.79%     | ok               |
|          50 | -4.33%   | 14.03%             | -17.40% |    -0.13 |       36 | 22.46%     | ok               |
|          35 | -5.65%   | 14.03%             | -21.38% |    -0.16 |       54 | 30.28%     | ok               |
|          45 | -6.09%   | 14.03%             | -19.08% |    -0.21 |       40 | 23.79%     | ok               |
|          25 | -10.56%  | 14.03%             | -23.37% |    -0.35 |       62 | 35.61%     | ok               |

## XLC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 14.20%   | 38.77%             | -12.33% |     0.52 |       63 | 50.58%     | ok               |
|          25 | 13.65%   | 38.77%             | -12.31% |     0.5  |       62 | 52.75%     | ok               |
|          50 | 7.28%    | 38.77%             | -11.12% |     0.38 |       66 | 38.60%     | ok               |
|          40 | 7.86%    | 38.77%             | -13.38% |     0.34 |       64 | 44.09%     | ok               |
|          35 | 7.13%    | 38.77%             | -13.38% |     0.31 |       62 | 47.92%     | ok               |

## XLE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -1.52%   | 38.38%             | -25.98% |     0.03 |       58 | 35.27%     | ok               |
|          35 | -8.85%   | 38.38%             | -30.47% |    -0.15 |       71 | 41.93%     | ok               |
|          25 | -10.87%  | 38.38%             | -34.18% |    -0.19 |       85 | 47.42%     | ok               |
|          45 | -9.24%   | 38.38%             | -30.18% |    -0.19 |       66 | 37.44%     | ok               |
|          15 | -12.05%  | 38.38%             | -36.64% |    -0.21 |       96 | 52.91%     | ok               |

## XLF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -3.58%   | 42.78%             | -18.63% |    -0.06 |       70 | 51.58%     | ok               |
|          15 | -7.64%   | 42.78%             | -20.19% |    -0.2  |       78 | 53.91%     | ok               |
|          25 | -9.62%   | 42.78%             | -23.22% |    -0.29 |       79 | 48.25%     | ok               |
|          30 | -9.66%   | 42.78%             | -23.61% |    -0.3  |       80 | 45.92%     | ok               |
|          35 | -16.69%  | 42.78%             | -24.48% |    -0.65 |       70 | 42.26%     | ok               |

## XLI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 8.41%    | 41.31%             | -10.01% |     0.34 |       84 | 49.08%     | ok               |
|          20 | 3.54%    | 41.31%             | -12.74% |     0.19 |       71 | 43.59%     | ok               |
|          25 | -2.89%   | 41.31%             | -14.41% |    -0.06 |       68 | 41.76%     | ok               |
|          45 | -2.86%   | 41.31%             | -16.29% |    -0.08 |       64 | 33.11%     | ok               |
|          30 | -3.48%   | 41.31%             | -14.12% |    -0.09 |       70 | 40.77%     | ok               |

## XLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 81.20%   | 88.44%             | -14.75% |     1.33 |       46 | 50.92%     | ok               |
|          25 | 77.51%   | 88.44%             | -14.75% |     1.33 |       40 | 48.75%     | ok               |
|          15 | 85.33%   | 88.44%             | -14.75% |     1.32 |       46 | 52.91%     | ok               |
|          30 | 66.88%   | 88.44%             | -14.75% |     1.23 |       40 | 47.42%     | ok               |
|          35 | 46.23%   | 88.44%             | -13.61% |     0.96 |       54 | 44.59%     | ok               |

## XLM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -15.33%  | -20.10%            | -49.14% |     0.05 |       71 | 50.77%     | ok               |
|          45 | -14.77%  | -20.10%            | -51.28% |    -0.01 |       56 | 31.99%     | ok               |
|          30 | -19.59%  | -20.10%            | -54.58% |    -0.01 |       67 | 47.70%     | ok               |
|          50 | -15.27%  | -20.10%            | -48.81% |    -0.03 |       46 | 26.63%     | ok               |
|          40 | -23.56%  | -20.10%            | -47.28% |    -0.1  |       53 | 37.55%     | ok               |

## XLP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 11.62%   | 12.71%             | -5.66%  |     0.73 |       50 | 30.78%     | ok               |
|          40 | 9.37%    | 12.71%             | -7.77%  |     0.57 |       66 | 34.94%     | ok               |
|          50 | 8.19%    | 12.71%             | -6.08%  |     0.54 |       54 | 28.95%     | ok               |
|          35 | 8.42%    | 12.71%             | -9.73%  |     0.51 |       62 | 37.94%     | ok               |
|          30 | 7.54%    | 12.71%             | -10.28% |     0.46 |       64 | 39.60%     | ok               |

## XLU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 4.79%    | 31.97%             | -13.94% |     0.27 |       52 | 30.28%     | ok               |
|          45 | 3.64%    | 31.97%             | -14.88% |     0.22 |       56 | 31.45%     | ok               |
|          40 | 0.51%    | 31.97%             | -16.41% |     0.07 |       62 | 33.28%     | ok               |
|          35 | -2.16%   | 31.97%             | -19.71% |    -0.05 |       62 | 35.94%     | ok               |
|          30 | -3.52%   | 31.97%             | -20.40% |    -0.11 |       67 | 39.27%     | ok               |

## XLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -16.57%  | 19.67%             | -21.14% |    -0.75 |       70 | 39.43%     | ok               |
|          30 | -16.95%  | 19.67%             | -20.62% |    -0.78 |       70 | 37.77%     | ok               |
|          15 | -20.28%  | 19.67%             | -24.43% |    -0.91 |       79 | 44.09%     | ok               |
|          20 | -19.84%  | 19.67%             | -24.51% |    -0.91 |       73 | 41.10%     | ok               |
|          35 | -21.29%  | 19.67%             | -24.56% |    -1.06 |       68 | 35.27%     | ok               |

## XLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -2.35%   | 30.75%             | -15.77% |     0.01 |       80 | 52.58%     | ok               |
|          30 | -6.85%   | 30.75%             | -17.23% |    -0.15 |       79 | 46.09%     | ok               |
|          20 | -7.51%   | 30.75%             | -19.25% |    -0.15 |       76 | 49.25%     | ok               |
|          25 | -9.58%   | 30.75%             | -19.25% |    -0.22 |       73 | 47.75%     | ok               |
|          50 | -7.29%   | 30.75%             | -14.40% |    -0.26 |       60 | 30.95%     | ok               |

## XOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 2.96%    | 39.41%             | -21.35% |     0.16 |       38 | 27.79%     | ok               |
|          25 | 0.95%    | 39.41%             | -19.90% |     0.1  |       59 | 36.11%     | ok               |
|          30 | -0.05%   | 39.41%             | -20.29% |     0.08 |       59 | 35.44%     | ok               |
|          45 | -3.68%   | 39.41%             | -23.33% |    -0.04 |       44 | 29.28%     | ok               |
|          20 | -4.79%   | 39.41%             | -25.56% |    -0.05 |       66 | 38.44%     | ok               |

## XRP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 17.27%   | -25.03%            | -31.38% |     0.39 |       70 | 43.10%     | ok               |
|          40 | 5.78%    | -25.03%            | -33.91% |     0.27 |       58 | 36.40%     | ok               |
|          30 | -1.25%   | -25.03%            | -31.82% |     0.2  |       65 | 47.89%     | ok               |
|          45 | -5.04%   | -25.03%            | -36.27% |     0.13 |       56 | 31.99%     | ok               |
|          20 | -14.63%  | -25.03%            | -38.12% |     0.05 |       77 | 56.13%     | ok               |

## YFI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -51.01%  | -51.23%            | -50.18% |    -0.88 |       58 | 27.39%     | ok               |
|          45 | -51.21%  | -51.23%            | -50.38% |    -1.12 |       70 | 21.84%     | ok               |
|          35 | -65.23%  | -51.23%            | -64.69% |    -1.18 |       69 | 35.06%     | ok               |
|          30 | -69.75%  | -51.23%            | -72.54% |    -1.27 |       81 | 39.46%     | ok               |
|          15 | -73.49%  | -51.23%            | -76.52% |    -1.27 |       85 | 52.11%     | ok               |

## ZEC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 156.34%  | 2635.86%           | -30.64% |     0.98 |       46 | 29.12%     | ok               |
|          35 | 120.09%  | 2635.86%           | -50.84% |     0.85 |       54 | 35.63%     | ok               |
|          25 | 109.73%  | 2635.86%           | -58.07% |     0.81 |       58 | 42.72%     | ok               |
|          30 | 95.71%   | 2635.86%           | -56.50% |     0.77 |       66 | 39.85%     | ok               |
|          50 | 76.21%   | 2635.86%           | -41.34% |     0.7  |       48 | 26.63%     | ok               |
