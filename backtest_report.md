# Market Tracker Backtest Report

_Generated: 2026-10-16T04:38:18+00:00_

## Data Sources

- Crypto: Kraken -> Coinbase -> CoinGecko OHLC -> CoinPaprika fallback chain.
- Stocks / ETFs / indices: Stooq -> Yahoo Finance fallback chain.
- Data rows are generated from real market APIs. Mock OHLCV rows are not generated.

## Data Freshness

- Rows: **92,742**
- Symbols: **161**
- Date range: **2024-05-23** to **2026-10-16**

## Latest Signals

| symbol     | date                |         close |   composite_score | signal   | data_source   |
|:-----------|:--------------------|--------------:|------------------:|:---------|:--------------|
| ABBV       | 2026-10-15 00:00:00 |   283.4       |         77.0833   | LONG     | Yahoo Finance |
| AMGN       | 2026-10-15 00:00:00 |   434.03      |         72.9167   | LONG     | Yahoo Finance |
| ARB-USD    | 2026-10-16 00:00:00 |     0.1929    |         30.3333   | LONG     | Kraken API    |
| CL         | 2026-10-15 00:00:00 |    92.67      |         58.25     | LONG     | Yahoo Finance |
| COP        | 2026-10-15 00:00:00 |   141.73      |         68.75     | LONG     | Yahoo Finance |
| COST       | 2026-10-15 00:00:00 |   978.01      |         65.8333   | LONG     | Yahoo Finance |
| CRM        | 2026-10-15 00:00:00 |   246.74      |         74.5833   | LONG     | Yahoo Finance |
| CSCO       | 2026-10-15 00:00:00 |   109.85      |         39.4167   | LONG     | Yahoo Finance |
| CVX        | 2026-10-15 00:00:00 |   219.32      |         52.25     | LONG     | Yahoo Finance |
| DIS        | 2026-10-15 00:00:00 |   110.68      |         76.5833   | LONG     | Yahoo Finance |
| DXY-INDEX  | 2026-10-16 00:00:00 |   101.862     |         60.2151   | LONG     | Yahoo Finance |
| EOG        | 2026-10-15 00:00:00 |   152.62      |         68.25     | LONG     | Yahoo Finance |
| INTU       | 2026-10-15 00:00:00 |   330.17      |         37.5833   | LONG     | Yahoo Finance |
| KO         | 2026-10-15 00:00:00 |    92         |         72.75     | LONG     | Yahoo Finance |
| LIN        | 2026-10-15 00:00:00 |   493.22      |         67.5      | LONG     | Yahoo Finance |
| LLY        | 2026-10-15 00:00:00 |  1251.61      |         76.4167   | LONG     | Yahoo Finance |
| META       | 2026-10-15 00:00:00 |   736.72      |         39.5833   | LONG     | Yahoo Finance |
| MPC        | 2026-10-15 00:00:00 |   476.92      |         70.75     | LONG     | Yahoo Finance |
| MSFT       | 2026-10-15 00:00:00 |   539.44      |         72.4167   | LONG     | Yahoo Finance |
| OXY        | 2026-10-15 00:00:00 |    60.67      |         71.5833   | LONG     | Yahoo Finance |
| PG         | 2026-10-15 00:00:00 |   157.08      |         80.75     | LONG     | Yahoo Finance |
| TIA-USD    | 2026-10-16 00:00:00 |     0.6082    |         68.8333   | LONG     | Kraken API    |
| TMO        | 2026-10-15 00:00:00 |   696.49      |         50.75     | LONG     | Yahoo Finance |
| TXN        | 2026-10-15 00:00:00 |   279.12      |         34.0833   | LONG     | Yahoo Finance |
| UNH        | 2026-10-15 00:00:00 |   406.67      |         74.75     | LONG     | Yahoo Finance |
| XLB        | 2026-10-15 00:00:00 |    50.56      |         57.6667   | LONG     | Yahoo Finance |
| XLE        | 2026-10-15 00:00:00 |    66.56      |         70.25     | LONG     | Yahoo Finance |
| XLF        | 2026-10-15 00:00:00 |    55.27      |         51.9167   | LONG     | Yahoo Finance |
| XLP        | 2026-10-15 00:00:00 |    86.68      |         58.75     | LONG     | Yahoo Finance |
| XOM        | 2026-10-15 00:00:00 |   174.68      |         52.25     | LONG     | Yahoo Finance |
| AAPL       | 2026-10-15 00:00:00 |   342         |         58.1667   | NEUTRAL  | Yahoo Finance |
| AAVE-USD   | 2026-10-16 00:00:00 |   158.4       |         14.6667   | NEUTRAL  | Kraken API    |
| ADA-USD    | 2026-10-16 00:00:00 |     0.229125  |        -41.5833   | NEUTRAL  | Kraken API    |
| ADBE       | 2026-10-15 00:00:00 |   251.67      |         33.4167   | NEUTRAL  | Yahoo Finance |
| AGG        | 2026-10-15 00:00:00 |    95.41      |          1.41667  | NEUTRAL  | Yahoo Finance |
| ALGO-USD   | 2026-10-16 00:00:00 |     0.11643   |         21.9167   | NEUTRAL  | Kraken API    |
| AMD        | 2026-10-15 00:00:00 |   562.23      |         16.4167   | NEUTRAL  | Yahoo Finance |
| AMZN       | 2026-10-15 00:00:00 |   254.76      |         41.1667   | NEUTRAL  | Yahoo Finance |
| APT-USD    | 2026-10-16 00:00:00 |     0.8495    |          3.91667  | NEUTRAL  | Kraken API    |
| ARKK       | 2026-10-15 00:00:00 |    85.69      |         -1.83333  | NEUTRAL  | Yahoo Finance |
| ATOM-USD   | 2026-10-16 00:00:00 |     1.7256    |         -0.666667 | NEUTRAL  | Kraken API    |
| AVAX-USD   | 2026-10-16 00:00:00 |    10.011     |          3.41667  | NEUTRAL  | Kraken API    |
| AVGO       | 2026-10-15 00:00:00 |   344.33      |        -62.8333   | NEUTRAL  | Yahoo Finance |
| BITO       | 2026-10-15 00:00:00 |    11         |         -6.91667  | NEUTRAL  | Yahoo Finance |
| BLK        | 2026-10-15 00:00:00 |  1120.78      |         60.1667   | NEUTRAL  | Yahoo Finance |
| BND        | 2026-10-15 00:00:00 |    70.81      |          1.41667  | NEUTRAL  | Yahoo Finance |
| BTC-USD    | 2026-10-16 00:00:00 | 81887.2       |         -3.58333  | NEUTRAL  | Kraken API    |
| CMCSA      | 2026-10-15 00:00:00 |    21.77      |        -19.75     | NEUTRAL  | Yahoo Finance |
| COMP-USD   | 2026-10-16 00:00:00 |    22.2       |         18.4167   | NEUTRAL  | Kraken API    |
| CRV-USD    | 2026-10-16 00:00:00 |     0.34883   |        -14.5833   | NEUTRAL  | Kraken API    |
| DASH-USD   | 2026-10-16 00:00:00 |    49.363     |        -22.6667   | NEUTRAL  | Kraken API    |
| DBC        | 2026-10-15 00:00:00 |    33.3       |         69.3333   | NEUTRAL  | Yahoo Finance |
| DE         | 2026-10-15 00:00:00 |   650.67      |        -24.8333   | NEUTRAL  | Yahoo Finance |
| DIA        | 2026-10-15 00:00:00 |   521.18      |         60.6667   | NEUTRAL  | Yahoo Finance |
| DOT-USD    | 2026-10-16 00:00:00 |     1.1478    |        -25.9167   | NEUTRAL  | Kraken API    |
| EFA        | 2026-10-15 00:00:00 |   103.67      |        -10.4167   | NEUTRAL  | Yahoo Finance |
| ETH-USD    | 2026-10-16 00:00:00 |  2435.23      |        -16.1667   | NEUTRAL  | Kraken API    |
| EWJ        | 2026-10-15 00:00:00 |    95.43      |        -24.5      | NEUTRAL  | Yahoo Finance |
| FCX        | 2026-10-15 00:00:00 |    70.06      |        -42.8333   | NEUTRAL  | Yahoo Finance |
| FET-USD    | 2026-10-16 00:00:00 |     0.202     |        -44.1667   | NEUTRAL  | Kraken API    |
| FIL-USD    | 2026-10-16 00:00:00 |     1.15      |         36.75     | NEUTRAL  | Kraken API    |
| FXI        | 2026-10-15 00:00:00 |    34.26      |         -4.33333  | NEUTRAL  | Yahoo Finance |
| GDX        | 2026-10-15 00:00:00 |    87.02      |        -22.3333   | NEUTRAL  | Yahoo Finance |
| GE         | 2026-10-15 00:00:00 |   312         |        -48.6667   | NEUTRAL  | Yahoo Finance |
| GOOGL      | 2026-10-15 00:00:00 |   349.22      |         53.9167   | NEUTRAL  | Yahoo Finance |
| GRT-USD    | 2026-10-16 00:00:00 |     0.02502   |         18.0833   | NEUTRAL  | Kraken API    |
| HD         | 2026-10-15 00:00:00 |   308.24      |         22.9167   | NEUTRAL  | Yahoo Finance |
| HON        | 2026-10-15 00:00:00 |   210.5       |        -23.4167   | NEUTRAL  | Yahoo Finance |
| HYG        | 2026-10-15 00:00:00 |    77.13      |        -26.75     | NEUTRAL  | Yahoo Finance |
| IBIT       | 2026-10-15 00:00:00 |    46.59      |         20.0833   | NEUTRAL  | Yahoo Finance |
| IBM        | 2026-10-15 00:00:00 |   234.12      |         20.6667   | NEUTRAL  | Yahoo Finance |
| ICP-USD    | 2026-10-16 00:00:00 |     3.027     |         -0.583333 | NEUTRAL  | Kraken API    |
| IEF        | 2026-10-15 00:00:00 |    90.35      |          1.41667  | NEUTRAL  | Yahoo Finance |
| INJ-USD    | 2026-10-16 00:00:00 |     9.103     |         59.3333   | NEUTRAL  | Kraken API    |
| INTC       | 2026-10-15 00:00:00 |    95.37      |        -12.3333   | NEUTRAL  | Yahoo Finance |
| ITA        | 2026-10-15 00:00:00 |   206.92      |        -28.75     | NEUTRAL  | Yahoo Finance |
| JNJ        | 2026-10-15 00:00:00 |   253.28      |        -39.0833   | NEUTRAL  | Yahoo Finance |
| JPM        | 2026-10-15 00:00:00 |   335.53      |         14.0833   | NEUTRAL  | Yahoo Finance |
| LDO-USD    | 2026-10-16 00:00:00 |     0.399     |        -19.5833   | NEUTRAL  | Kraken API    |
| LINK-USD   | 2026-10-16 00:00:00 |    12.39      |        -15.5833   | NEUTRAL  | Kraken API    |
| LRCX       | 2026-10-15 00:00:00 |   277.46      |        -26.75     | NEUTRAL  | Yahoo Finance |
| LTC-USD    | 2026-10-16 00:00:00 |    60.81      |         10.4167   | NEUTRAL  | Kraken API    |
| MCD        | 2026-10-15 00:00:00 |   242.5       |          6.91667  | NEUTRAL  | Yahoo Finance |
| MRK        | 2026-10-15 00:00:00 |   145.19      |          9.16667  | NEUTRAL  | Yahoo Finance |
| MU         | 2026-10-15 00:00:00 |   931.24      |        -11.5833   | NEUTRAL  | Yahoo Finance |
| NEAR-USD   | 2026-10-16 00:00:00 |     5.2151    |         36.75     | NEUTRAL  | Kraken API    |
| NEM        | 2026-10-15 00:00:00 |   115.79      |        -22.3333   | NEUTRAL  | Yahoo Finance |
| NFLX       | 2026-10-15 00:00:00 |    72.61      |         15.4167   | NEUTRAL  | Yahoo Finance |
| NKE        | 2026-10-15 00:00:00 |    37.14      |          4.91667  | NEUTRAL  | Yahoo Finance |
| NOW        | 2026-10-15 00:00:00 |   148.57      |         66.8333   | NEUTRAL  | Yahoo Finance |
| NVDA       | 2026-10-15 00:00:00 |   217.23      |        -11.0833   | NEUTRAL  | Yahoo Finance |
| OP-USD     | 2026-10-16 00:00:00 |     0.1361    |          4.25     | NEUTRAL  | Kraken API    |
| ORCL       | 2026-10-15 00:00:00 |   134.47      |        -48.8333   | NEUTRAL  | Yahoo Finance |
| PEP        | 2026-10-15 00:00:00 |   128.38      |        -22.25     | NEUTRAL  | Yahoo Finance |
| PEPE-USD   | 2026-10-16 00:00:00 |     4.096e-06 |         -0.166667 | NEUTRAL  | Kraken API    |
| PFE        | 2026-10-15 00:00:00 |    29.44      |         63.1667   | NEUTRAL  | Yahoo Finance |
| PM         | 2026-10-15 00:00:00 |   199.9       |         63.3333   | NEUTRAL  | Yahoo Finance |
| POL-USD    | 2026-10-16 00:00:00 |     0.09567   |        -53.8333   | NEUTRAL  | Kraken API    |
| QCOM       | 2026-10-15 00:00:00 |   178.4       |        -16.5833   | NEUTRAL  | Yahoo Finance |
| QQQ        | 2026-10-15 00:00:00 |   728         |          0.416667 | NEUTRAL  | Yahoo Finance |
| RENDER-USD | 2026-10-16 00:00:00 |     1.916     |          4.91667  | NEUTRAL  | Kraken API    |
| RTX        | 2026-10-15 00:00:00 |   186.95      |        -29.25     | NEUTRAL  | Yahoo Finance |
| SBUX       | 2026-10-15 00:00:00 |    96.88      |         12.1667   | NEUTRAL  | Yahoo Finance |
| SHY        | 2026-10-15 00:00:00 |    81.29      |         14.6667   | NEUTRAL  | Yahoo Finance |
| SKY-USD    | 2026-10-16 00:00:00 |     0.07111   |        -12.25     | NEUTRAL  | Kraken API    |
| SMH        | 2026-10-15 00:00:00 |   558.84      |         -6.66667  | NEUTRAL  | Yahoo Finance |
| SOXX       | 2026-10-15 00:00:00 |   514.71      |         -9.58333  | NEUTRAL  | Yahoo Finance |
| SPY        | 2026-10-15 00:00:00 |   771.79      |         39.3333   | NEUTRAL  | Yahoo Finance |
| SUSHI-USD  | 2026-10-16 00:00:00 |     0.229     |        -13.5833   | NEUTRAL  | Kraken API    |
| TGT        | 2026-10-15 00:00:00 |   156.63      |         27.1667   | NEUTRAL  | Yahoo Finance |
| TLT        | 2026-10-15 00:00:00 |    79.97      |          2.91667  | NEUTRAL  | Yahoo Finance |
| TRX-USD    | 2026-10-16 00:00:00 |     0.335405  |         31.9167   | NEUTRAL  | Kraken API    |
| TSLA       | 2026-10-15 00:00:00 |   362.44      |        -58.3333   | NEUTRAL  | Yahoo Finance |
| UNI-USD    | 2026-10-16 00:00:00 |     7.3647    |          2.41667  | NEUTRAL  | Kraken API    |
| UPS        | 2026-10-15 00:00:00 |    97.83      |          6.91667  | NEUTRAL  | Yahoo Finance |
| USO        | 2026-10-15 00:00:00 |   157.31      |         67.8333   | NEUTRAL  | Yahoo Finance |
| VIXY       | 2026-10-15 00:00:00 |    16.4       |        -29.75     | NEUTRAL  | Yahoo Finance |
| VNQ        | 2026-10-15 00:00:00 |    91.44      |          6.91667  | NEUTRAL  | Yahoo Finance |
| VTI        | 2026-10-15 00:00:00 |   378.42      |          5.66667  | NEUTRAL  | Yahoo Finance |
| VWO        | 2026-10-15 00:00:00 |    58.79      |        -44.25     | NEUTRAL  | Yahoo Finance |
| WFC        | 2026-10-15 00:00:00 |    82.75      |         -5.5      | NEUTRAL  | Yahoo Finance |
| WMT        | 2026-10-15 00:00:00 |   117.87      |         54.75     | NEUTRAL  | Yahoo Finance |
| XBI        | 2026-10-15 00:00:00 |   149.78      |        -17.25     | NEUTRAL  | Yahoo Finance |
| XLC        | 2026-10-15 00:00:00 |   112.44      |         18.25     | NEUTRAL  | Yahoo Finance |
| XLI        | 2026-10-15 00:00:00 |   167.89      |        -40.1667   | NEUTRAL  | Yahoo Finance |
| XLK        | 2026-10-15 00:00:00 |   189.19      |         -1.33333  | NEUTRAL  | Yahoo Finance |
| XLU        | 2026-10-15 00:00:00 |    41.65      |          3.08333  | NEUTRAL  | Yahoo Finance |
| XLV        | 2026-10-15 00:00:00 |   177.19      |         65.3333   | NEUTRAL  | Yahoo Finance |
| XLY        | 2026-10-15 00:00:00 |   113.41      |         19.4167   | NEUTRAL  | Yahoo Finance |
| ZEC-USD    | 2026-10-16 00:00:00 |  1211.18      |         -0.333333 | NEUTRAL  | Kraken API    |
| AMAT       | 2026-10-15 00:00:00 |   430.01      |        -57.5      | SHORT    | Yahoo Finance |
| BA         | 2026-10-15 00:00:00 |   188.73      |        -30.75     | SHORT    | Yahoo Finance |
| BAC        | 2026-10-15 00:00:00 |    51.7       |        -31.5833   | SHORT    | Yahoo Finance |
| BCH-USD    | 2026-10-16 00:00:00 |   276.5       |        -33.5833   | SHORT    | Kraken API    |
| BONK-USD   | 2026-10-16 00:00:00 |     3.086e-06 |        -35.25     | SHORT    | Kraken API    |
| C          | 2026-10-15 00:00:00 |   123.21      |        -55.3333   | SHORT    | Yahoo Finance |
| CAT        | 2026-10-15 00:00:00 |   735.64      |        -58.8333   | SHORT    | Yahoo Finance |
| DOGE-USD   | 2026-10-16 00:00:00 |     0.0815858 |        -47.6667   | SHORT    | Kraken API    |
| EEM        | 2026-10-15 00:00:00 |    63.96      |        -33.3333   | SHORT    | Yahoo Finance |
| ETC-USD    | 2026-10-16 00:00:00 |     8.052     |        -38.5833   | SHORT    | Kraken API    |
| GDXJ       | 2026-10-15 00:00:00 |   109.61      |        -49.8333   | SHORT    | Yahoo Finance |
| GLD        | 2026-10-15 00:00:00 |   382.71      |        -33.25     | SHORT    | Yahoo Finance |
| GS         | 2026-10-15 00:00:00 |   891.28      |        -32.9167   | SHORT    | Yahoo Finance |
| HBAR-USD   | 2026-10-16 00:00:00 |     0.08464   |        -42.3333   | SHORT    | Kraken API    |
| IEMG       | 2026-10-15 00:00:00 |    78.09      |        -30        | SHORT    | Yahoo Finance |
| IWM        | 2026-10-15 00:00:00 |   275.08      |        -40        | SHORT    | Yahoo Finance |
| MS         | 2026-10-15 00:00:00 |   182.1       |        -49.5833   | SHORT    | Yahoo Finance |
| SCHW       | 2026-10-15 00:00:00 |    94.16      |        -32.5      | SHORT    | Yahoo Finance |
| SHIB-USD   | 2026-10-16 00:00:00 |     5.12e-06  |        -40.25     | SHORT    | Kraken API    |
| SLB        | 2026-10-15 00:00:00 |    48.37      |        -48.25     | SHORT    | Yahoo Finance |
| SLV        | 2026-10-15 00:00:00 |    51.92      |        -53.5833   | SHORT    | Yahoo Finance |
| SNX-USD    | 2026-10-16 00:00:00 |     0.2265    |        -37        | SHORT    | Kraken API    |
| SOL-USD    | 2026-10-16 00:00:00 |   105.09      |        -20.3333   | SHORT    | Kraken API    |
| T          | 2026-10-15 00:00:00 |    23.5       |        -49.8333   | SHORT    | Yahoo Finance |
| TMUS       | 2026-10-15 00:00:00 |   157.03      |        -46.25     | SHORT    | Yahoo Finance |
| VEA        | 2026-10-15 00:00:00 |    69.66      |        -30.75     | SHORT    | Yahoo Finance |
| VZ         | 2026-10-15 00:00:00 |    44.4       |        -45.3333   | SHORT    | Yahoo Finance |
| WIF-USD    | 2026-10-16 00:00:00 |     0.2004    |        -51.5833   | SHORT    | Kraken API    |
| XLM-USD    | 2026-10-16 00:00:00 |     0.18212   |        -42.3333   | SHORT    | Kraken API    |
| XRP-USD    | 2026-10-16 00:00:00 |     1.32949   |        -43.5833   | SHORT    | Kraken API    |
| YFI-USD    | 2026-10-16 00:00:00 |  2296         |        -33.25     | SHORT    | Kraken API    |

## Edge Summary

- Symbols with trades: **161** of 161
- Beat buy-and-hold: **32.92%** of traded symbols
- Positive return: **30.43%** of traded symbols
- Median strategy return: **-10.29%** (benchmark **19.05%**)
- Median excess vs benchmark: **-25.41%**
- Median Sharpe: **-0.13**
- Median exposure: **44.25%**

> Edge is real only if both _beat buy-and-hold_ and _median excess_ are convincingly positive across many symbols. Treat a single high-return symbol as noise.

## Portfolio Backtest

Actual capital-allocation books (not per-symbol averages). Benchmarks: `equal_weight_buyhold` (whole tracked universe), `spy_buyhold` (100% SPY), and `sixty_forty` (60% SPY / 40% AGG). `high_conf_voltarget` inverse-vol-weights the HIGH-confidence book; `conviction_long_short` is market-neutral. Judge on **Sharpe** and **max_drawdown** out-of-sample, not raw return: a fully-invested long book wins on return in a bull market but carries all the risk.

| strategy              | scope         | ann_return   | ann_vol   |   sharpe | max_drawdown   | total_return   |   avg_gross_exposure |
|:----------------------|:--------------|:-------------|:----------|---------:|:---------------|:---------------|---------------------:|
| equal_weight_buyhold  | full          | 11.03%       | 28.53%    |     0.39 | -39.53%        | 23.55%         |                 1    |
| equal_weight_buyhold  | out_of_sample | 15.34%       | 27.74%    |     0.55 | -19.75%        | 13.02%         |                 1    |
| all_signals_ew        | full          | -15.88%      | 24.37%    |    -0.65 | -57.37%        | -43.61%        |                 1    |
| all_signals_ew        | out_of_sample | 4.95%        | 23.59%    |     0.21 | -23.10%        | 2.35%          |                 1    |
| high_conf_ew          | full          | -3.66%       | 31.66%    |    -0.12 | -44.16%        | -23.02%        |                 0.9  |
| high_conf_ew          | out_of_sample | 10.70%       | 28.74%    |     0.37 | -22.85%        | 7.16%          |                 0.9  |
| high_conf_voltarget   | full          | -5.34%       | 28.40%    |    -0.19 | -39.64%        | -24.61%        |                 0.9  |
| high_conf_voltarget   | out_of_sample | 0.46%        | 23.99%    |     0.02 | -17.70%        | -2.62%         |                 0.9  |
| conviction_long_short | full          | -13.93%      | 22.24%    |    -0.63 | -46.44%        | -39.30%        |                 0.97 |
| conviction_long_short | out_of_sample | -1.94%       | 19.62%    |    -0.1  | -26.60%        | -4.03%         |                 0.97 |
| spy_buyhold           | full          | 5.73%        | 13.65%    |     0.42 | -19.00%        | 15.70%         |                 0.79 |
| spy_buyhold           | out_of_sample | 0.17%        | 9.92%     |     0.02 | -12.06%        | -0.34%         |                 0.79 |
| sixty_forty           | full          | 3.12%        | 8.61%     |     0.36 | -11.66%        | 8.70%          |                 0.79 |
| sixty_forty           | out_of_sample | -1.93%       | 6.67%     |    -0.29 | -8.26%         | -2.26%         |                 0.79 |

## Walk-Forward Robustness

Each book measured across contiguous time folds (each a different regime). A book has durable edge only if `mean_sharpe` is positive, `min_sharpe` isn't deeply negative, and `pct_positive_folds` is high — a single great fold doesn't count. `fold_sharpes` lists each fold oldest-to-newest.

| strategy              |   n_folds |   mean_sharpe |   median_sharpe |   min_sharpe | pct_positive_folds   | mean_return   | fold_sharpes                 |
|:----------------------|----------:|--------------:|----------------:|-------------:|:---------------------|:--------------|:-----------------------------|
| equal_weight_buyhold  |         5 |          0.58 |            0.93 |        -0.57 | 60.00%               | 5.51%         | 0.93;1.42;-0.57;-0.21;1.31   |
| all_signals_ew        |         5 |         -0.69 |           -0.78 |        -1.91 | 20.00%               | -9.37%        | -1.32;-0.78;-1.91;1.07;-0.49 |
| high_conf_ew          |         5 |          0.01 |           -0    |        -1.07 | 40.00%               | -3.71%        | 0.19;-0.26;-1.07;1.21;-0.00  |
| high_conf_voltarget   |         5 |         -0.04 |           -0.2  |        -0.93 | 40.00%               | -4.69%        | 0.44;-0.22;-0.93;0.74;-0.20  |
| conviction_long_short |         5 |         -0.6  |           -0.75 |        -1.83 | 40.00%               | -9.09%        | -1.83;0.10;-0.83;-0.75;0.31  |
| spy_buyhold           |         5 |          0.39 |            0.33 |        -0.3  | 80.00%               | 3.05%         | 1.37;0.33;0.01;0.54;-0.30    |
| sixty_forty           |         5 |          0.32 |            0.26 |        -0.51 | 80.00%               | 1.72%         | 1.33;0.35;0.26;0.17;-0.51    |

## Strategy Comparison

Each decision rule backtested over the same data. `out_of_sample` is the most recent ~35% of each symbol's history (unseen tail). A rule has real edge only if `median_excess` and `beat_benchmark_pct` stay positive out-of-sample, not just full-sample.

| strategy        | scope         |   symbols | beat_benchmark_pct   | positive_pct   | median_return   | median_benchmark   | median_excess   |   median_sharpe |   total_trades |
|:----------------|:--------------|----------:|:---------------------|:---------------|:----------------|:-------------------|:----------------|----------------:|---------------:|
| trend           | full          |       161 | 32.92%               | 30.43%         | -10.29%         | 19.05%             | -25.41%         |           -0.13 |          11344 |
| trend           | out_of_sample |       161 | 27.95%               | 50.31%         | 0.03%           | 6.78%              | -14.46%         |            0.09 |           3830 |
| mean_reversion  | full          |       157 | 37.58%               | 49.68%         | -0.02%          | 17.67%             | -15.88%         |            0.01 |           1220 |
| mean_reversion  | out_of_sample |       120 | 32.50%               | 53.33%         | 0.30%           | 4.33%              | -6.32%          |            0.16 |            474 |
| regime_adaptive | full          |       161 | 32.92%               | 31.68%         | -10.29%         | 19.05%             | -24.82%         |           -0.13 |          11612 |
| regime_adaptive | out_of_sample |       161 | 29.19%               | 49.69%         | -0.09%          | 6.78%              | -14.46%         |            0.07 |           3936 |

## Signal Calibration

Realized forward return in the signal's direction, grouped by confidence. HIGH should outrank LOW for the confidence score to be meaningful.

| confidence_level   |   horizon |     n | mean_return   | median_return   | win_rate   |
|:-------------------|----------:|------:|:--------------|:----------------|:-----------|
| HIGH               |         5 |  7888 | 0.20%         | 0.05%           | 50.91%     |
| MEDIUM             |         5 | 29147 | 0.04%         | 0.04%           | 50.34%     |
| LOW                |         5 |  3513 | -0.38%        | -0.41%          | 46.09%     |
| ALL                |         5 | 40548 | 0.04%         | 0.01%           | 50.08%     |
| HIGH               |        10 |  7859 | 0.44%         | 0.08%           | 50.88%     |
| MEDIUM             |        10 | 28898 | 0.17%         | 0.05%           | 50.40%     |
| LOW                |        10 |  3459 | -0.74%        | -0.54%          | 46.57%     |
| ALL                |        10 | 40216 | 0.14%         | 0.02%           | 50.17%     |
| HIGH               |        20 |  7731 | 1.04%         | 0.31%           | 52.46%     |
| MEDIUM             |        20 | 28280 | 0.90%         | 0.57%           | 53.22%     |
| LOW                |        20 |  3386 | -0.43%        | -0.53%          | 47.34%     |
| ALL                |        20 | 39397 | 0.81%         | 0.44%           | 52.57%     |

## Backtest Summary

### Data Quality / Signal Availability

- **ok**: 161 symbols

| symbol     |   trades | return   | benchmark_return   | mdd     |   sharpe | exposure   | skipped_reason   |
|:-----------|---------:|:---------|:-------------------|:--------|---------:|:-----------|:-----------------|
| AAPL       |       63 | 9.27%    | 83.01%             | -20.65% |     0.28 | 50.58%     | ok               |
| AAVE-USD   |       65 | -38.36%  | -32.95%            | -66.17% |    -0.24 | 41.95%     | ok               |
| ABBV       |       70 | -22.00%  | 79.07%             | -30.52% |    -0.46 | 48.25%     | ok               |
| ADA-USD    |       76 | -37.14%  | -72.42%            | -52.70% |    -0.29 | 45.79%     | ok               |
| ADBE       |       71 | -11.61%  | -47.93%            | -31.20% |    -0.03 | 56.91%     | ok               |
| AGG        |       65 | -6.56%   | -1.10%             | -11.01% |    -1.04 | 33.28%     | ok               |
| ALGO-USD   |       76 | -27.31%  | -53.08%            | -38.67% |    -0.15 | 40.04%     | ok               |
| AMAT       |       71 | -37.68%  | 97.30%             | -53.91% |    -0.36 | 51.41%     | ok               |
| AMD        |       56 | 17.30%   | 250.45%            | -41.09% |     0.37 | 37.27%     | ok               |
| AMGN       |       67 | -12.44%  | 41.61%             | -34.19% |    -0.2  | 50.92%     | ok               |
| AMZN       |       78 | -55.10%  | 40.71%             | -55.57% |    -1.58 | 41.10%     | ok               |
| APT-USD    |       70 | -23.20%  | -86.17%            | -56.73% |    -0    | 39.66%     | ok               |
| ARB-USD    |       75 | -4.93%   | -57.75%            | -48.19% |     0.23 | 43.10%     | ok               |
| ARKK       |       89 | -30.46%  | 96.49%             | -34.52% |    -0.47 | 43.59%     | ok               |
| ATOM-USD   |       92 | -58.27%  | -67.32%            | -58.27% |    -0.81 | 48.28%     | ok               |
| AVAX-USD   |       68 | -34.28%  | -61.11%            | -45.41% |    -0.28 | 39.85%     | ok               |
| AVGO       |       64 | 17.51%   | 147.13%            | -36.09% |     0.37 | 41.43%     | ok               |
| BA         |       67 | 11.91%   | 9.59%              | -24.47% |     0.31 | 51.08%     | ok               |
| BAC        |       74 | -6.03%   | 31.99%             | -22.11% |    -0.09 | 48.59%     | ok               |
| BCH-USD    |       76 | 0.83%    | -32.75%            | -53.87% |     0.22 | 48.66%     | ok               |
| BITO       |       79 | -21.78%  | -59.56%            | -43.10% |    -0.13 | 41.60%     | ok               |
| BLK        |       85 | -11.08%  | 42.86%             | -26.90% |    -0.25 | 46.76%     | ok               |
| BND        |       67 | -6.59%   | -1.09%             | -10.91% |    -1.01 | 35.44%     | ok               |
| BONK-USD   |       74 | 5.66%    | -86.84%            | -48.17% |     0.33 | 45.59%     | ok               |
| BTC-USD    |       72 | 2.37%    | -21.38%            | -23.38% |     0.18 | 51.92%     | ok               |
| C          |       79 | -33.43%  | 95.51%             | -39.51% |    -0.71 | 46.09%     | ok               |
| CAT        |       68 | 6.30%    | 109.76%            | -21.87% |     0.23 | 47.92%     | ok               |
| CL         |       66 | -1.88%   | -1.13%             | -14.32% |     0    | 38.60%     | ok               |
| CMCSA      |       84 | -37.47%  | -39.95%            | -46.39% |    -0.91 | 43.59%     | ok               |
| COMP-USD   |       97 | -33.51%  | -54.34%            | -52.81% |    -0.14 | 50.19%     | ok               |
| COP        |       68 | -12.05%  | 20.47%             | -41.35% |    -0.13 | 44.09%     | ok               |
| COST       |       60 | 0.14%    | 22.81%             | -31.32% |     0.07 | 41.10%     | ok               |
| CRM        |       67 | -29.58%  | -11.43%            | -44.41% |    -0.39 | 46.59%     | ok               |
| CRV-USD    |       66 | 29.43%   | -54.24%            | -39.89% |     0.49 | 36.78%     | ok               |
| CSCO       |       64 | 11.65%   | 135.73%            | -21.79% |     0.32 | 49.58%     | ok               |
| CVX        |       73 | -14.73%  | 39.75%             | -27.78% |    -0.33 | 41.93%     | ok               |
| DASH-USD   |       53 | -1.31%   | 91.89%             | -64.43% |     0.38 | 30.27%     | ok               |
| DBC        |       66 | -8.16%   | 42.55%             | -24.10% |    -0.21 | 35.27%     | ok               |
| DE         |       70 | -12.17%  | 71.57%             | -23.98% |    -0.18 | 44.26%     | ok               |
| DIA        |       66 | -4.99%   | 33.41%             | -12.94% |    -0.24 | 43.59%     | ok               |
| DIS        |       64 | -5.85%   | 9.95%              | -28.17% |    -0.04 | 43.43%     | ok               |
| DOGE-USD   |       69 | -29.86%  | -66.12%            | -60.95% |    -0.13 | 48.85%     | ok               |
| DOT-USD    |       86 | -52.69%  | -77.94%            | -63.33% |    -0.45 | 48.08%     | ok               |
| DXY-INDEX  |       40 | -0.82%   | -4.68%             | -6.02%  |    -0.11 | 32.25%     | ok               |
| EEM        |       62 | -11.37%  | 49.09%             | -24.04% |    -0.32 | 39.77%     | ok               |
| EFA        |       66 | -10.35%  | 28.96%             | -12.96% |    -0.4  | 41.10%     | ok               |
| EOG        |       80 | -30.65%  | 23.05%             | -47.87% |    -0.66 | 45.09%     | ok               |
| ETC-USD    |       60 | -25.33%  | -61.04%            | -47.84% |    -0.25 | 31.61%     | ok               |
| ETH-USD    |       58 | 129.82%  | -9.14%             | -30.11% |     1.23 | 47.89%     | ok               |
| EWJ        |       62 | -22.99%  | 40.92%             | -29.40% |    -0.8  | 36.44%     | ok               |
| FCX        |       65 | -29.37%  | 36.84%             | -46.84% |    -0.32 | 44.26%     | ok               |
| FET-USD    |       83 | -52.60%  | -77.35%            | -65.38% |    -0.39 | 42.72%     | ok               |
| FIL-USD    |       65 | -40.15%  | -64.30%            | -58.54% |    -0.34 | 37.16%     | ok               |
| FXI        |       50 | -5.30%   | 24.00%             | -24.33% |    -0.05 | 30.95%     | ok               |
| GDX        |       62 | 3.53%    | 150.42%            | -33.31% |     0.19 | 44.59%     | ok               |
| GDXJ       |       72 | -33.81%  | 149.68%            | -40.39% |    -0.41 | 43.09%     | ok               |
| GE         |       76 | -8.43%   | 88.79%             | -27.82% |    -0.04 | 48.09%     | ok               |
| GLD        |       50 | 13.20%   | 77.41%             | -13.87% |     0.39 | 45.76%     | ok               |
| GOOGL      |       57 | 58.85%   | 101.22%            | -17.54% |     1.03 | 47.25%     | ok               |
| GRT-USD    |       77 | 68.95%   | -80.49%            | -33.74% |     0.76 | 45.79%     | ok               |
| GS         |       70 | -3.31%   | 94.54%             | -21.94% |     0.03 | 48.09%     | ok               |
| HBAR-USD   |       40 | -42.75%  | -17.93%            | -56.47% |    -0.92 | 38.11%     | ok               |
| HD         |       67 | 1.72%    | -5.71%             | -17.15% |     0.13 | 43.59%     | ok               |
| HON        |       93 | -26.42%  | 6.80%              | -33.53% |    -0.66 | 54.91%     | ok               |
| HYG        |       85 | -6.75%   | 0.40%              | -10.59% |    -0.75 | 39.27%     | ok               |
| IBIT       |       40 | 36.51%   | 22.57%             | -18.95% |     0.67 | 35.02%     | ok               |
| IBM        |       69 | -25.03%  | 37.18%             | -48.94% |    -0.3  | 49.08%     | ok               |
| ICP-USD    |       79 | -17.76%  | -48.94%            | -46.42% |     0.09 | 39.46%     | ok               |
| IEF        |       78 | -10.32%  | -2.60%             | -13.49% |    -1.41 | 33.78%     | ok               |
| IEMG       |       60 | -10.98%  | 45.04%             | -27.43% |    -0.32 | 39.93%     | ok               |
| INJ-USD    |       63 | -27.85%  | -33.36%            | -68.17% |    -0.03 | 40.23%     | ok               |
| INTC       |       68 | 40.26%   | 217.05%            | -60.60% |     0.53 | 48.09%     | ok               |
| INTU       |       75 | -12.77%  | -50.14%            | -38.67% |    -0.08 | 46.42%     | ok               |
| ITA        |       78 | -2.36%   | 54.23%             | -23.75% |     0.01 | 48.42%     | ok               |
| IWM        |       56 | 8.08%    | 35.38%             | -10.95% |     0.35 | 34.11%     | ok               |
| JNJ        |       58 | 10.08%   | 69.19%             | -16.86% |     0.41 | 46.59%     | ok               |
| JPM        |       73 | -21.84%  | 70.39%             | -32.74% |    -0.6  | 44.76%     | ok               |
| KO         |       52 | 25.10%   | 48.17%             | -8.64%  |     0.89 | 36.61%     | ok               |
| LDO-USD    |       68 | 49.35%   | -65.06%            | -50.81% |     0.62 | 46.55%     | ok               |
| LIN        |       74 | -10.29%  | 14.09%             | -20.61% |    -0.32 | 38.60%     | ok               |
| LINK-USD   |       68 | 41.07%   | -28.79%            | -33.64% |     0.59 | 45.21%     | ok               |
| LLY        |       80 | -33.51%  | 54.82%             | -53.42% |    -0.54 | 49.25%     | ok               |
| LRCX       |       80 | -30.42%  | 189.58%            | -60.58% |    -0.24 | 42.60%     | ok               |
| LTC-USD    |       68 | -2.19%   | -41.26%            | -31.17% |     0.17 | 52.68%     | ok               |
| MCD        |       79 | -4.25%   | -5.98%             | -21.88% |    -0.1  | 40.60%     | ok               |
| META       |       72 | -25.15%  | 58.17%             | -44.52% |    -0.33 | 50.25%     | ok               |
| MPC        |       72 | 21.08%   | 170.12%            | -34.29% |     0.44 | 52.25%     | ok               |
| MRK        |       65 | -23.45%  | 10.76%             | -35.95% |    -0.45 | 42.43%     | ok               |
| MS         |       75 | -5.02%   | 84.09%             | -27.79% |    -0.04 | 48.25%     | ok               |
| MSFT       |       83 | -24.93%  | 26.33%             | -39.15% |    -0.52 | 51.41%     | ok               |
| MU         |       51 | 142.61%  | 637.50%            | -68.76% |     1.01 | 52.41%     | ok               |
| NEAR-USD   |       71 | 158.95%  | 62.36%             | -46.60% |     1.07 | 44.25%     | ok               |
| NEM        |       70 | -23.49%  | 180.84%            | -39.56% |    -0.21 | 50.08%     | ok               |
| NFLX       |       78 | 5.74%    | 14.23%             | -21.09% |     0.22 | 52.75%     | ok               |
| NKE        |       81 | -30.30%  | -59.37%            | -55.35% |    -0.36 | 47.09%     | ok               |
| NOW        |       80 | 9.63%    | -2.02%             | -30.43% |     0.29 | 50.08%     | ok               |
| NVDA       |       77 | -50.14%  | 77.20%             | -53.41% |    -0.72 | 55.61%     | ok               |
| OP-USD     |       70 | -43.71%  | -84.94%            | -60.45% |    -0.37 | 32.76%     | ok               |
| ORCL       |       62 | 86.30%   | 8.36%              | -30.61% |     0.81 | 51.91%     | ok               |
| OXY        |       73 | 0.23%    | -2.08%             | -28.48% |     0.13 | 42.76%     | ok               |
| PEP        |       76 | -0.55%   | -28.39%            | -21.35% |     0.05 | 45.59%     | ok               |
| PEPE-USD   |       83 | -56.54%  | -71.64%            | -61.29% |    -0.45 | 48.08%     | ok               |
| PFE        |       79 | -34.49%  | 2.61%              | -41.77% |    -1.08 | 36.44%     | ok               |
| PG         |       66 | -22.59%  | -5.08%             | -24.16% |    -0.91 | 34.44%     | ok               |
| PM         |       79 | -7.20%   | 100.60%            | -35.15% |    -0.07 | 49.92%     | ok               |
| POL-USD    |       77 | 52.93%   | -63.24%            | -38.69% |     0.68 | 49.62%     | ok               |
| QCOM       |       77 | -28.07%  | -11.58%            | -56.59% |    -0.23 | 43.26%     | ok               |
| QQQ        |       66 | 6.57%    | 60.47%             | -14.20% |     0.25 | 45.92%     | ok               |
| RENDER-USD |       90 | -24.34%  | -63.93%            | -45.62% |     0.01 | 47.32%     | ok               |
| RTX        |       66 | 27.97%   | 77.36%             | -16.99% |     0.65 | 51.91%     | ok               |
| SBUX       |       60 | -14.33%  | 23.71%             | -29.22% |    -0.23 | 38.60%     | ok               |
| SCHW       |       80 | -17.23%  | 30.16%             | -31.92% |    -0.38 | 46.09%     | ok               |
| SHIB-USD   |       81 | -35.00%  | -68.69%            | -47.15% |    -0.32 | 52.30%     | ok               |
| SHY        |       48 | -1.75%   | -0.06%             | -3.18%  |    -0.58 | 37.10%     | ok               |
| SKY-USD    |       89 | -64.06%  | -9.85%             | -64.20% |    -1.1  | 43.68%     | ok               |
| SLB        |       75 | -40.39%  | 4.43%              | -59.65% |    -0.78 | 49.25%     | ok               |
| SLV        |       68 | 14.15%   | 88.46%             | -42.60% |     0.34 | 40.10%     | ok               |
| SMH        |       48 | 46.32%   | 133.02%            | -33.66% |     0.76 | 43.59%     | ok               |
| SNX-USD    |       64 | -13.77%  | -75.59%            | -50.74% |     0.05 | 33.72%     | ok               |
| SOL-USD    |       71 | -20.11%  | -42.81%            | -44.99% |    -0.01 | 60.34%     | ok               |
| SOXX       |       56 | 58.38%   | 120.04%            | -40.14% |     0.85 | 42.93%     | ok               |
| SPY        |       64 | 0.61%    | 46.74%             | -15.53% |     0.08 | 49.25%     | ok               |
| SUSHI-USD  |       94 | -79.49%  | -73.94%            | -79.84% |    -1.33 | 39.46%     | ok               |
| T          |       72 | 41.44%   | 34.52%             | -17.01% |     0.83 | 56.74%     | ok               |
| TGT        |       60 | -11.06%  | 8.46%              | -34.42% |    -0.16 | 37.60%     | ok               |
| TIA-USD    |       93 | -47.52%  | -81.64%            | -75.93% |    -0.25 | 42.91%     | ok               |
| TLT        |       68 | -19.63%  | -12.23%            | -21.85% |    -1.47 | 33.61%     | ok               |
| TMO        |       69 | 30.81%   | 19.05%             | -18.85% |     0.63 | 55.24%     | ok               |
| TMUS       |       74 | -3.51%   | -4.81%             | -32.44% |     0.02 | 48.09%     | ok               |
| TRX-USD    |       66 | 1.77%    | 23.82%             | -22.90% |     0.13 | 50.57%     | ok               |
| TSLA       |       80 | -37.10%  | 108.61%            | -59.64% |    -0.26 | 42.93%     | ok               |
| TXN        |       77 | -25.59%  | 41.48%             | -46.62% |    -0.28 | 50.42%     | ok               |
| UNH        |       77 | 32.41%   | -21.31%            | -26.31% |     0.55 | 48.42%     | ok               |
| UNI-USD    |       90 | -41.70%  | 3.83%              | -69.96% |    -0.18 | 50.00%     | ok               |
| UPS        |       72 | -38.07%  | -29.67%            | -40.10% |    -0.78 | 42.60%     | ok               |
| USO        |       69 | -12.56%  | 111.30%            | -46.93% |    -0.06 | 33.44%     | ok               |
| VEA        |       62 | -3.22%   | 38.54%             | -17.27% |    -0.08 | 42.26%     | ok               |
| VIXY       |       94 | -77.98%  | -64.44%            | -88.17% |    -0.93 | 32.11%     | ok               |
| VNQ        |       73 | -13.63%  | 11.78%             | -24.92% |    -0.54 | 39.77%     | ok               |
| VTI        |       68 | -6.72%   | 45.55%             | -17.64% |    -0.19 | 49.25%     | ok               |
| VWO        |       80 | -17.76%  | 33.43%             | -25.20% |    -0.66 | 40.27%     | ok               |
| VZ         |       84 | -25.18%  | 12.60%             | -28.90% |    -0.77 | 41.93%     | ok               |
| WFC        |       80 | -17.86%  | 38.66%             | -28.90% |    -0.3  | 46.76%     | ok               |
| WIF-USD    |       68 | -30.58%  | -82.96%            | -52.76% |    -0.06 | 37.74%     | ok               |
| WMT        |       69 | 4.87%    | 81.79%             | -25.37% |     0.21 | 48.75%     | ok               |
| XBI        |       62 | 0.54%    | 67.69%             | -17.66% |     0.1  | 38.44%     | ok               |
| XLB        |       66 | -13.03%  | 11.65%             | -24.29% |    -0.46 | 31.61%     | ok               |
| XLC        |       61 | 13.91%   | 37.29%             | -12.33% |     0.51 | 50.08%     | ok               |
| XLE        |       69 | -3.66%   | 45.90%             | -29.67% |    -0    | 45.59%     | ok               |
| XLF        |       82 | -8.64%   | 33.63%             | -23.61% |    -0.26 | 46.42%     | ok               |
| XLI        |       82 | -10.04%  | 35.58%             | -17.79% |    -0.35 | 42.76%     | ok               |
| XLK        |       44 | 47.98%   | 77.32%             | -14.75% |     0.96 | 46.09%     | ok               |
| XLM-USD    |       68 | -5.07%   | -42.01%            | -54.58% |     0.16 | 47.51%     | ok               |
| XLP        |       67 | 7.71%    | 12.72%             | -10.28% |     0.45 | 38.44%     | ok               |
| XLU        |       69 | -4.25%   | 17.67%             | -20.40% |    -0.14 | 39.43%     | ok               |
| XLV        |       76 | -21.66%  | 22.28%             | -22.75% |    -1.04 | 36.61%     | ok               |
| XLY        |       75 | -4.15%   | 30.51%             | -18.35% |    -0.06 | 47.59%     | ok               |
| XOM        |       55 | 1.71%    | 53.89%             | -20.29% |     0.12 | 34.28%     | ok               |
| XRP-USD    |       66 | -2.44%   | -48.53%            | -33.91% |     0.16 | 36.40%     | ok               |
| YFI-USD    |       79 | -64.90%  | -63.69%            | -63.60% |    -1.28 | 37.55%     | ok               |
| ZEC-USD    |       59 | 137.88%  | 2676.03%           | -56.50% |     0.89 | 41.19%     | ok               |

## AAPL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 16.11%   | 83.01%             | -21.71% |     0.39 |       72 | 55.41%     | ok               |
|          15 | 13.12%   | 83.01%             | -23.86% |     0.34 |       81 | 62.73%     | ok               |
|          30 | 9.27%    | 83.01%             | -20.65% |     0.28 |       63 | 50.58%     | ok               |
|          35 | 7.70%    | 83.01%             | -22.04% |     0.26 |       63 | 49.25%     | ok               |
|          25 | 4.85%    | 83.01%             | -20.87% |     0.2  |       73 | 52.75%     | ok               |

## AAVE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 20.94%   | -32.95%            | -43.61% |     0.42 |       43 | 36.40%     | ok               |
|          45 | 9.67%    | -32.95%            | -49.19% |     0.31 |       48 | 31.23%     | ok               |
|          35 | 5.50%    | -32.95%            | -48.79% |     0.28 |       51 | 39.46%     | ok               |
|          50 | 4.75%    | -32.95%            | -45.07% |     0.25 |       46 | 23.56%     | ok               |
|          15 | -39.97%  | -32.95%            | -61.76% |    -0.17 |       72 | 54.79%     | ok               |

## ABBV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -9.27%   | 79.07%             | -26.16% |    -0.16 |       54 | 35.27%     | ok               |
|          20 | -18.94%  | 79.07%             | -28.73% |    -0.36 |       66 | 51.58%     | ok               |
|          25 | -19.04%  | 79.07%             | -30.04% |    -0.37 |       69 | 50.08%     | ok               |
|          40 | -19.83%  | 79.07%             | -27.36% |    -0.45 |       70 | 40.60%     | ok               |
|          30 | -22.00%  | 79.07%             | -30.52% |    -0.46 |       70 | 48.25%     | ok               |

## ADA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 13.88%   | -72.42%            | -34.05% |     0.36 |       46 | 31.61%     | ok               |
|          50 | 7.38%    | -72.42%            | -33.96% |     0.27 |       48 | 27.20%     | ok               |
|          40 | -5.48%   | -72.42%            | -40.73% |     0.14 |       56 | 37.55%     | ok               |
|          15 | -24.62%  | -72.42%            | -47.27% |     0.02 |       71 | 61.69%     | ok               |
|          35 | -16.97%  | -72.42%            | -44.07% |     0.01 |       62 | 41.38%     | ok               |

## ADBE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 8.07%    | -47.93%            | -29.07% |     0.26 |       53 | 60.90%     | ok               |
|          20 | -6.09%   | -47.93%            | -31.52% |     0.07 |       59 | 63.89%     | ok               |
|          35 | -3.98%   | -47.93%            | -31.73% |     0.06 |       78 | 48.25%     | ok               |
|          30 | -11.61%  | -47.93%            | -31.20% |    -0.03 |       71 | 56.91%     | ok               |
|          15 | -13.40%  | -47.93%            | -34.98% |    -0.04 |       64 | 65.56%     | ok               |

## AGG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -5.33%   | -1.10%             | -9.59%  |    -0.95 |       56 | 24.63%     | ok               |
|          50 | -4.73%   | -1.10%             | -8.07%  |    -1    |       54 | 19.63%     | ok               |
|          30 | -6.56%   | -1.10%             | -11.01% |    -1.04 |       65 | 33.28%     | ok               |
|          35 | -7.32%   | -1.10%             | -11.73% |    -1.19 |       62 | 29.95%     | ok               |
|          25 | -8.00%   | -1.10%             | -12.28% |    -1.2  |       71 | 36.61%     | ok               |

## ALGO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -27.31%  | -53.08%            | -38.67% |    -0.15 |       76 | 40.04%     | ok               |
|          15 | -38.19%  | -53.08%            | -51.37% |    -0.26 |       75 | 50.38%     | ok               |
|          25 | -36.61%  | -53.08%            | -51.92% |    -0.27 |       78 | 44.83%     | ok               |
|          20 | -46.26%  | -53.08%            | -53.23% |    -0.42 |       79 | 47.70%     | ok               |
|          35 | -40.02%  | -53.08%            | -52.35% |    -0.45 |       64 | 34.87%     | ok               |

## AMAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -33.46%  | 97.30%             | -53.90% |    -0.24 |       74 | 60.57%     | ok               |
|          50 | -30.29%  | 97.30%             | -41.04% |    -0.29 |       50 | 36.11%     | ok               |
|          35 | -33.05%  | 97.30%             | -47.88% |    -0.3  |       71 | 48.75%     | ok               |
|          30 | -37.68%  | 97.30%             | -53.91% |    -0.36 |       71 | 51.41%     | ok               |
|          40 | -38.50%  | 97.30%             | -50.74% |    -0.41 |       69 | 43.93%     | ok               |

## AMD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 27.96%   | 250.45%            | -39.92% |     0.46 |       56 | 32.28%     | ok               |
|          40 | 17.30%   | 250.45%            | -41.09% |     0.37 |       56 | 37.27%     | ok               |
|          35 | 12.27%   | 250.45%            | -43.15% |     0.33 |       64 | 38.94%     | ok               |
|          45 | 2.14%    | 250.45%            | -49.59% |     0.23 |       62 | 35.11%     | ok               |
|          30 | -2.54%   | 250.45%            | -49.79% |     0.2  |       65 | 41.43%     | ok               |

## AMGN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -7.52%   | 41.61%             | -26.65% |    -0.06 |       66 | 56.57%     | ok               |
|          35 | -10.23%  | 41.61%             | -31.29% |    -0.14 |       69 | 47.59%     | ok               |
|          15 | -12.98%  | 41.61%             | -27.98% |    -0.18 |       63 | 60.73%     | ok               |
|          30 | -12.44%  | 41.61%             | -34.19% |    -0.2  |       67 | 50.92%     | ok               |
|          25 | -14.24%  | 41.61%             | -33.47% |    -0.23 |       63 | 53.08%     | ok               |

## AMZN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -27.97%  | 40.71%             | -29.61% |    -0.85 |       56 | 29.95%     | ok               |
|          50 | -31.74%  | 40.71%             | -33.91% |    -1.16 |       50 | 22.80%     | ok               |
|          45 | -37.46%  | 40.71%             | -38.25% |    -1.34 |       58 | 26.46%     | ok               |
|          35 | -52.04%  | 40.71%             | -52.54% |    -1.53 |       77 | 35.27%     | ok               |
|          30 | -55.10%  | 40.71%             | -55.57% |    -1.58 |       78 | 41.10%     | ok               |

## APT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 37.70%   | -86.17%            | -27.79% |     0.67 |       42 | 16.48%     | ok               |
|          20 | 0.36%    | -86.17%            | -56.22% |     0.28 |       78 | 49.62%     | ok               |
|          45 | -1.29%   | -86.17%            | -53.47% |     0.18 |       58 | 23.18%     | ok               |
|          35 | -14.40%  | -86.17%            | -49.10% |     0.07 |       68 | 35.44%     | ok               |
|          25 | -22.50%  | -86.17%            | -55.69% |     0.03 |       70 | 44.25%     | ok               |

## ARB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 57.32%   | -57.75%            | -33.60% |     0.67 |       54 | 26.44%     | ok               |
|          50 | 46.51%   | -57.75%            | -30.72% |     0.61 |       42 | 19.35%     | ok               |
|          40 | 27.44%   | -57.75%            | -40.13% |     0.48 |       55 | 33.72%     | ok               |
|          15 | 24.05%   | -57.75%            | -44.26% |     0.47 |       90 | 59.20%     | ok               |
|          35 | 21.94%   | -57.75%            | -45.71% |     0.44 |       71 | 37.93%     | ok               |

## ARKK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -16.33%  | 96.49%             | -37.76% |    -0.11 |       90 | 54.74%     | ok               |
|          20 | -25.01%  | 96.49%             | -34.82% |    -0.29 |       91 | 50.08%     | ok               |
|          30 | -30.46%  | 96.49%             | -34.52% |    -0.47 |       89 | 43.59%     | ok               |
|          35 | -37.04%  | 96.49%             | -39.81% |    -0.66 |       90 | 40.77%     | ok               |
|          25 | -40.48%  | 96.49%             | -46.36% |    -0.69 |       99 | 46.09%     | ok               |

## ATOM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -41.59%  | -67.32%            | -48.20% |    -0.33 |       86 | 65.90%     | ok               |
|          25 | -48.34%  | -67.32%            | -49.45% |    -0.52 |       92 | 54.60%     | ok               |
|          20 | -55.70%  | -67.32%            | -57.28% |    -0.66 |       96 | 58.24%     | ok               |
|          30 | -58.27%  | -67.32%            | -58.27% |    -0.81 |       92 | 48.28%     | ok               |
|          35 | -58.92%  | -67.32%            | -61.18% |    -0.93 |       82 | 42.34%     | ok               |

## AVAX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 48.52%   | -61.11%            | -22.06% |     0.78 |       34 | 19.92%     | ok               |
|          40 | 9.52%    | -61.11%            | -30.70% |     0.3  |       40 | 27.78%     | ok               |
|          45 | 6.87%    | -61.11%            | -27.52% |     0.26 |       34 | 24.52%     | ok               |
|          35 | -10.72%  | -61.11%            | -37.03% |     0.05 |       54 | 33.91%     | ok               |
|          15 | -18.70%  | -61.11%            | -43.71% |     0.02 |       73 | 52.87%     | ok               |

## AVGO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 20.89%   | 147.13%            | -38.01% |     0.4  |       68 | 44.09%     | ok               |
|          30 | 17.51%   | 147.13%            | -36.09% |     0.37 |       64 | 41.43%     | ok               |
|          50 | 12.49%   | 147.13%            | -36.86% |     0.31 |       56 | 29.28%     | ok               |
|          35 | 8.98%    | 147.13%            | -40.43% |     0.27 |       74 | 38.44%     | ok               |
|          40 | 7.75%    | 147.13%            | -40.70% |     0.26 |       64 | 35.11%     | ok               |

## BA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 41.10%   | 9.59%              | -13.34% |     0.9  |       46 | 35.77%     | ok               |
|          40 | 35.35%   | 9.59%              | -23.87% |     0.68 |       46 | 43.59%     | ok               |
|          35 | 33.91%   | 9.59%              | -18.09% |     0.63 |       62 | 48.09%     | ok               |
|          25 | 22.30%   | 9.59%              | -26.02% |     0.46 |       68 | 54.58%     | ok               |
|          30 | 11.91%   | 9.59%              | -24.47% |     0.31 |       67 | 51.08%     | ok               |

## BAC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 1.37%    | 31.99%             | -16.89% |     0.12 |       83 | 53.58%     | ok               |
|          25 | 0.18%    | 31.99%             | -18.19% |     0.08 |       78 | 51.25%     | ok               |
|          35 | -1.51%   | 31.99%             | -24.07% |     0.03 |       66 | 45.09%     | ok               |
|          15 | -6.77%   | 31.99%             | -21.15% |    -0.07 |       90 | 60.73%     | ok               |
|          30 | -6.03%   | 31.99%             | -22.11% |    -0.09 |       74 | 48.59%     | ok               |

## BCH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 40.91%   | -32.75%            | -45.51% |     0.58 |       74 | 57.28%     | ok               |
|          20 | 16.80%   | -32.75%            | -45.82% |     0.39 |       68 | 54.02%     | ok               |
|          25 | 0.64%    | -32.75%            | -51.09% |     0.23 |       70 | 50.19%     | ok               |
|          30 | 0.83%    | -32.75%            | -53.87% |     0.22 |       76 | 48.66%     | ok               |
|          35 | -5.87%   | -32.75%            | -57.75% |     0.14 |       70 | 44.64%     | ok               |

## BITO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -5.36%   | -59.56%            | -31.98% |     0.05 |       54 | 25.12%     | ok               |
|          30 | -21.78%  | -59.56%            | -43.10% |    -0.13 |       79 | 41.60%     | ok               |
|          45 | -18.40%  | -59.56%            | -33.99% |    -0.15 |       60 | 28.62%     | ok               |
|          40 | -22.63%  | -59.56%            | -40.13% |    -0.19 |       62 | 32.95%     | ok               |
|          35 | -24.67%  | -59.56%            | -42.34% |    -0.2  |       70 | 37.10%     | ok               |

## BLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -2.02%   | 42.86%             | -20.79% |     0.01 |       90 | 42.93%     | ok               |
|          40 | -3.33%   | 42.86%             | -22.83% |    -0.03 |       78 | 38.10%     | ok               |
|          20 | -7.38%   | 42.86%             | -21.48% |    -0.12 |       88 | 51.58%     | ok               |
|          25 | -8.71%   | 42.86%             | -24.62% |    -0.16 |       81 | 49.42%     | ok               |
|          30 | -11.08%  | 42.86%             | -26.90% |    -0.25 |       85 | 46.76%     | ok               |

## BND Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.82%   | -1.09%             | -10.21% |    -0.95 |       66 | 40.77%     | ok               |
|          30 | -6.59%   | -1.09%             | -10.91% |    -1.01 |       67 | 35.44%     | ok               |
|          25 | -6.95%   | -1.09%             | -11.27% |    -1.02 |       69 | 38.60%     | ok               |
|          15 | -8.52%   | -1.09%             | -11.52% |    -1.19 |       77 | 43.43%     | ok               |
|          40 | -7.72%   | -1.09%             | -11.70% |    -1.3  |       60 | 29.45%     | ok               |

## BONK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 156.03%  | -86.84%            | -35.57% |     1.2  |       42 | 21.46%     | ok               |
|          15 | 60.08%   | -86.84%            | -62.48% |     0.67 |       72 | 59.77%     | ok               |
|          45 | 50.70%   | -86.84%            | -47.53% |     0.64 |       66 | 27.59%     | ok               |
|          20 | 24.71%   | -86.84%            | -58.35% |     0.48 |       69 | 55.75%     | ok               |
|          40 | 19.24%   | -86.84%            | -53.34% |     0.42 |       58 | 36.59%     | ok               |

## BTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 42.78%   | -21.38%            | -14.50% |     0.86 |       44 | 35.06%     | ok               |
|          45 | 38.31%   | -21.38%            | -12.20% |     0.82 |       42 | 31.03%     | ok               |
|          35 | 41.79%   | -21.38%            | -21.56% |     0.81 |       62 | 41.38%     | ok               |
|          50 | 16.51%   | -21.38%            | -20.63% |     0.46 |       38 | 26.25%     | ok               |
|          30 | 17.20%   | -21.38%            | -21.75% |     0.42 |       68 | 47.32%     | ok               |

## C Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -10.04%  | 95.51%             | -22.03% |    -0.22 |       66 | 30.95%     | ok               |
|          45 | -20.78%  | 95.51%             | -29.81% |    -0.52 |       74 | 35.11%     | ok               |
|          40 | -26.38%  | 95.51%             | -35.31% |    -0.65 |       76 | 37.44%     | ok               |
|          25 | -32.12%  | 95.51%             | -36.49% |    -0.66 |       71 | 48.25%     | ok               |
|          30 | -33.43%  | 95.51%             | -39.51% |    -0.71 |       79 | 46.09%     | ok               |

## CAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 18.14%   | 109.76%            | -21.80% |     0.39 |       71 | 60.40%     | ok               |
|          25 | 13.85%   | 109.76%            | -21.79% |     0.34 |       64 | 50.25%     | ok               |
|          45 | 6.94%    | 109.76%            | -23.56% |     0.24 |       52 | 36.44%     | ok               |
|          30 | 6.30%    | 109.76%            | -21.87% |     0.23 |       68 | 47.92%     | ok               |
|          20 | 4.61%    | 109.76%            | -24.56% |     0.2  |       74 | 53.41%     | ok               |

## CL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 1.90%    | -1.13%             | -12.98% |     0.13 |       44 | 22.46%     | ok               |
|          30 | -1.88%   | -1.13%             | -14.32% |     0    |       66 | 38.60%     | ok               |
|          45 | -4.01%   | -1.13%             | -13.13% |    -0.11 |       50 | 25.29%     | ok               |
|          35 | -5.79%   | -1.13%             | -15.39% |    -0.14 |       66 | 34.78%     | ok               |
|          15 | -10.68%  | -1.13%             | -19.00% |    -0.26 |       66 | 46.92%     | ok               |

## CMCSA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -18.53%  | -39.95%            | -28.41% |    -0.61 |       48 | 16.81%     | ok               |
|          45 | -23.79%  | -39.95%            | -35.13% |    -0.74 |       62 | 21.46%     | ok               |
|          15 | -37.98%  | -39.95%            | -46.99% |    -0.81 |       91 | 58.07%     | ok               |
|          40 | -31.58%  | -39.95%            | -42.51% |    -0.84 |       89 | 28.95%     | ok               |
|          30 | -37.47%  | -39.95%            | -46.39% |    -0.91 |       84 | 43.59%     | ok               |

## COMP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -2.05%   | -54.34%            | -38.71% |     0.18 |       52 | 25.10%     | ok               |
|          30 | -33.51%  | -54.34%            | -52.81% |    -0.14 |       97 | 50.19%     | ok               |
|          25 | -40.21%  | -54.34%            | -51.58% |    -0.22 |       96 | 58.24%     | ok               |
|          15 | -46.57%  | -54.34%            | -52.34% |    -0.3  |      100 | 68.77%     | ok               |
|          40 | -42.56%  | -54.34%            | -50.93% |    -0.36 |       70 | 38.70%     | ok               |

## COP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -5.94%   | 20.47%             | -34.61% |    -0.04 |       48 | 28.12%     | ok               |
|          35 | -9.71%   | 20.47%             | -42.05% |    -0.08 |       71 | 41.43%     | ok               |
|          30 | -12.05%  | 20.47%             | -41.35% |    -0.13 |       68 | 44.09%     | ok               |
|          45 | -13.34%  | 20.47%             | -41.10% |    -0.2  |       64 | 32.28%     | ok               |
|          40 | -21.04%  | 20.47%             | -47.54% |    -0.38 |       76 | 35.94%     | ok               |

## COST Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 14.27%   | 22.81%             | -24.32% |     0.47 |       62 | 47.09%     | ok               |
|          25 | 10.97%   | 22.81%             | -24.93% |     0.39 |       59 | 44.26%     | ok               |
|          35 | 4.56%    | 22.81%             | -30.16% |     0.21 |       58 | 38.60%     | ok               |
|          30 | 0.14%    | 22.81%             | -31.32% |     0.07 |       60 | 41.10%     | ok               |
|          15 | -1.22%   | 22.81%             | -27.30% |     0.04 |       67 | 50.75%     | ok               |

## CRM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -18.37%  | -11.43%            | -32.74% |    -0.19 |       64 | 41.76%     | ok               |
|          40 | -21.43%  | -11.43%            | -38.23% |    -0.27 |       70 | 37.60%     | ok               |
|          50 | -19.25%  | -11.43%            | -38.38% |    -0.32 |       60 | 24.96%     | ok               |
|          15 | -29.59%  | -11.43%            | -47.54% |    -0.32 |       92 | 57.40%     | ok               |
|          30 | -29.58%  | -11.43%            | -44.41% |    -0.39 |       67 | 46.59%     | ok               |

## CRV-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 61.03%   | -54.24%            | -37.78% |     0.72 |       66 | 32.18%     | ok               |
|          40 | 46.68%   | -54.24%            | -38.86% |     0.63 |       54 | 27.97%     | ok               |
|          45 | 37.10%   | -54.24%            | -42.29% |     0.57 |       54 | 21.46%     | ok               |
|          50 | 36.17%   | -54.24%            | -30.73% |     0.56 |       46 | 17.43%     | ok               |
|          30 | 29.43%   | -54.24%            | -39.89% |     0.49 |       66 | 36.78%     | ok               |

## CSCO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 29.58%   | 135.73%            | -19.34% |     0.63 |       50 | 38.60%     | ok               |
|          45 | 25.19%   | 135.73%            | -19.34% |     0.55 |       52 | 40.27%     | ok               |
|          25 | 17.85%   | 135.73%            | -23.28% |     0.41 |       61 | 50.92%     | ok               |
|          20 | 12.56%   | 135.73%            | -22.72% |     0.33 |       71 | 53.24%     | ok               |
|          30 | 11.65%   | 135.73%            | -21.79% |     0.32 |       64 | 49.58%     | ok               |

## CVX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -10.73%  | 39.75%             | -23.80% |    -0.2  |       75 | 44.76%     | ok               |
|          40 | -11.21%  | 39.75%             | -27.34% |    -0.25 |       75 | 36.77%     | ok               |
|          45 | -11.60%  | 39.75%             | -28.83% |    -0.27 |       67 | 33.44%     | ok               |
|          35 | -14.10%  | 39.75%             | -28.85% |    -0.32 |       69 | 38.77%     | ok               |
|          50 | -11.49%  | 39.75%             | -30.69% |    -0.33 |       60 | 28.95%     | ok               |

## DASH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 156.61%  | 91.89%             | -33.55% |     1.01 |       38 | 18.01%     | ok               |
|          40 | 125.75%  | 91.89%             | -33.20% |     0.89 |       42 | 24.33%     | ok               |
|          45 | 94.16%   | 91.89%             | -37.63% |     0.78 |       42 | 20.50%     | ok               |
|          30 | -1.31%   | 91.89%             | -64.43% |     0.38 |       53 | 30.27%     | ok               |
|          25 | -6.81%   | 91.89%             | -64.14% |     0.34 |       63 | 32.76%     | ok               |

## DBC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -0.09%   | 42.55%             | -26.05% |     0.07 |       77 | 41.26%     | ok               |
|          20 | -4.49%   | 42.55%             | -25.69% |    -0.08 |       69 | 39.60%     | ok               |
|          25 | -5.28%   | 42.55%             | -24.84% |    -0.11 |       66 | 37.60%     | ok               |
|          50 | -5.52%   | 42.55%             | -18.84% |    -0.15 |       48 | 24.63%     | ok               |
|          35 | -7.76%   | 42.55%             | -23.19% |    -0.2  |       66 | 34.28%     | ok               |

## DE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 2.13%    | 71.57%             | -17.97% |     0.13 |       56 | 29.62%     | ok               |
|          45 | -4.48%   | 71.57%             | -19.53% |    -0.02 |       60 | 34.11%     | ok               |
|          20 | -7.80%   | 71.57%             | -24.11% |    -0.07 |       65 | 48.59%     | ok               |
|          25 | -12.03%  | 71.57%             | -24.29% |    -0.17 |       71 | 46.92%     | ok               |
|          30 | -12.17%  | 71.57%             | -23.98% |    -0.18 |       70 | 44.26%     | ok               |

## DIA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -2.79%   | 33.41%             | -11.28% |    -0.11 |       60 | 44.76%     | ok               |
|          35 | -4.59%   | 33.41%             | -13.15% |    -0.23 |       68 | 40.43%     | ok               |
|          30 | -4.99%   | 33.41%             | -12.94% |    -0.24 |       66 | 43.59%     | ok               |
|          20 | -5.60%   | 33.41%             | -13.72% |    -0.26 |       66 | 46.76%     | ok               |
|          40 | -7.77%   | 33.41%             | -15.06% |    -0.44 |       72 | 37.10%     | ok               |

## DIS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 34.98%   | 9.95%              | -10.17% |     1.08 |       46 | 25.46%     | ok               |
|          40 | 7.85%    | 9.95%              | -18.75% |     0.27 |       61 | 33.94%     | ok               |
|          45 | 4.51%    | 9.95%              | -16.54% |     0.2  |       47 | 29.12%     | ok               |
|          35 | -3.67%   | 9.95%              | -25.70% |     0.01 |       75 | 40.10%     | ok               |
|          15 | -5.94%   | 9.95%              | -32.73% |    -0.02 |       85 | 54.24%     | ok               |

## DOGE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 0.74%    | -66.12%            | -57.89% |     0.27 |       73 | 64.18%     | ok               |
|          20 | -7.03%   | -66.12%            | -55.83% |     0.18 |       75 | 58.81%     | ok               |
|          25 | -13.69%  | -66.12%            | -53.72% |     0.1  |       67 | 54.98%     | ok               |
|          30 | -29.86%  | -66.12%            | -60.95% |    -0.13 |       69 | 48.85%     | ok               |
|          50 | -29.89%  | -66.12%            | -52.88% |    -0.25 |       62 | 24.33%     | ok               |

## DOT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -54.09%  | -77.94%            | -72.06% |    -0.35 |       74 | 63.03%     | ok               |
|          20 | -50.91%  | -77.94%            | -66.32% |    -0.36 |       86 | 59.00%     | ok               |
|          30 | -52.69%  | -77.94%            | -63.33% |    -0.45 |       86 | 48.08%     | ok               |
|          25 | -58.48%  | -77.94%            | -69.99% |    -0.53 |       77 | 54.02%     | ok               |
|          35 | -56.60%  | -77.94%            | -62.35% |    -0.56 |       82 | 42.72%     | ok               |

## DXY-INDEX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.82%   | -4.68%             | -6.02% |    -0.11 |       40 | 32.25%     | ok               |
|          40 | -2.18%   | -4.68%             | -7.30% |    -0.27 |       64 | 47.62%     | ok               |
|          45 | -2.18%   | -4.68%             | -8.14% |    -0.29 |       60 | 38.31%     | ok               |
|          30 | -5.08%   | -4.68%             | -9.83% |    -0.6  |       74 | 57.58%     | ok               |
|          35 | -5.24%   | -4.68%             | -9.97% |    -0.66 |       77 | 52.60%     | ok               |

## EEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -6.78%   | 49.09%             | -15.88% |    -0.19 |       54 | 32.28%     | ok               |
|          45 | -7.12%   | 49.09%             | -17.03% |    -0.2  |       52 | 33.78%     | ok               |
|          40 | -7.46%   | 49.09%             | -19.20% |    -0.21 |       64 | 35.94%     | ok               |
|          35 | -8.10%   | 49.09%             | -23.57% |    -0.21 |       66 | 37.94%     | ok               |
|          30 | -11.37%  | 49.09%             | -24.04% |    -0.32 |       62 | 39.77%     | ok               |

## EFA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -2.72%   | 28.96%             | -10.10% |    -0.04 |       64 | 51.41%     | ok               |
|          20 | -10.31%  | 28.96%             | -13.73% |    -0.36 |       71 | 48.42%     | ok               |
|          30 | -10.35%  | 28.96%             | -12.96% |    -0.4  |       66 | 41.10%     | ok               |
|          25 | -11.25%  | 28.96%             | -15.23% |    -0.42 |       70 | 44.59%     | ok               |
|          40 | -10.79%  | 28.96%             | -14.58% |    -0.46 |       62 | 36.27%     | ok               |

## EOG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -17.98%  | 23.05%             | -35.34% |    -0.38 |       56 | 30.95%     | ok               |
|          40 | -24.18%  | 23.05%             | -37.39% |    -0.55 |       72 | 34.94%     | ok               |
|          50 | -22.97%  | 23.05%             | -35.63% |    -0.56 |       54 | 27.95%     | ok               |
|          35 | -28.16%  | 23.05%             | -41.05% |    -0.65 |       85 | 39.93%     | ok               |
|          30 | -30.65%  | 23.05%             | -47.87% |    -0.66 |       80 | 45.09%     | ok               |

## ETC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -5.47%   | -61.04%            | -38.47% |     0.05 |       28 | 20.50%     | ok               |
|          50 | -4.94%   | -61.04%            | -31.28% |     0.05 |       28 | 18.20%     | ok               |
|          40 | -17.53%  | -61.04%            | -43.28% |    -0.16 |       40 | 23.75%     | ok               |
|          35 | -22.00%  | -61.04%            | -46.64% |    -0.21 |       46 | 27.59%     | ok               |
|          30 | -25.33%  | -61.04%            | -47.84% |    -0.25 |       60 | 31.61%     | ok               |

## ETH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 129.82%  | -9.14%             | -30.11% |     1.23 |       58 | 47.89%     | ok               |
|          30 | 93.87%   | -9.14%             | -32.89% |     0.98 |       60 | 55.56%     | ok               |
|          40 | 54.80%   | -9.14%             | -33.11% |     0.77 |       62 | 40.23%     | ok               |
|          25 | 58.70%   | -9.14%             | -40.90% |     0.74 |       60 | 59.39%     | ok               |
|          20 | 40.41%   | -9.14%             | -39.10% |     0.59 |       82 | 63.79%     | ok               |

## EWJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -22.99%  | 40.92%             | -29.40% |    -0.8  |       62 | 36.44%     | ok               |
|          20 | -23.95%  | 40.92%             | -30.00% |    -0.81 |       56 | 38.44%     | ok               |
|          25 | -25.82%  | 40.92%             | -29.85% |    -0.9  |       56 | 37.60%     | ok               |
|          15 | -27.60%  | 40.92%             | -31.15% |    -0.9  |       67 | 41.76%     | ok               |
|          45 | -23.95%  | 40.92%             | -27.68% |    -0.98 |       58 | 28.12%     | ok               |

## FCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 2.51%    | 36.84%             | -29.27% |     0.18 |       50 | 31.61%     | ok               |
|          50 | -0.09%   | 36.84%             | -26.57% |     0.13 |       52 | 27.95%     | ok               |
|          40 | -10.00%  | 36.84%             | -42.89% |    -0.01 |       62 | 36.94%     | ok               |
|          30 | -29.37%  | 36.84%             | -46.84% |    -0.32 |       65 | 44.26%     | ok               |
|          35 | -29.20%  | 36.84%             | -50.12% |    -0.34 |       67 | 42.10%     | ok               |

## FET-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -39.02%  | -77.35%            | -59.58% |    -0.08 |       82 | 57.09%     | ok               |
|          25 | -37.94%  | -77.35%            | -65.31% |    -0.11 |       85 | 47.32%     | ok               |
|          20 | -43.00%  | -77.35%            | -65.01% |    -0.16 |       92 | 52.87%     | ok               |
|          30 | -52.60%  | -77.35%            | -65.38% |    -0.39 |       83 | 42.72%     | ok               |
|          50 | -39.06%  | -77.35%            | -45.19% |    -0.53 |       46 | 14.37%     | ok               |

## FIL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -40.15%  | -64.30%            | -58.54% |    -0.34 |       65 | 37.16%     | ok               |
|          35 | -41.96%  | -64.30%            | -61.90% |    -0.42 |       58 | 31.23%     | ok               |
|          40 | -40.23%  | -64.30%            | -57.60% |    -0.44 |       48 | 26.82%     | ok               |
|          15 | -58.37%  | -64.30%            | -71.82% |    -0.57 |       91 | 49.04%     | ok               |
|          25 | -58.52%  | -64.30%            | -70.65% |    -0.66 |       76 | 40.04%     | ok               |

## FXI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -5.03%   | 24.00%             | -22.99% |    -0.04 |       52 | 32.45%     | ok               |
|          30 | -5.30%   | 24.00%             | -24.33% |    -0.05 |       50 | 30.95%     | ok               |
|          15 | -5.91%   | 24.00%             | -21.68% |    -0.05 |       54 | 36.44%     | ok               |
|          20 | -8.65%   | 24.00%             | -24.94% |    -0.13 |       54 | 34.28%     | ok               |
|          35 | -8.96%   | 24.00%             | -27.93% |    -0.16 |       52 | 28.45%     | ok               |

## GDX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 8.30%    | 150.42%            | -31.44% |     0.26 |       76 | 50.25%     | ok               |
|          40 | 4.42%    | 150.42%            | -28.04% |     0.2  |       62 | 38.27%     | ok               |
|          30 | 3.53%    | 150.42%            | -33.31% |     0.19 |       62 | 44.59%     | ok               |
|          35 | -1.62%   | 150.42%            | -32.05% |     0.11 |       70 | 40.93%     | ok               |
|          25 | -4.93%   | 150.42%            | -38.90% |     0.06 |       66 | 46.26%     | ok               |

## GDXJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -21.20%  | 149.68%            | -41.17% |    -0.13 |       74 | 50.25%     | ok               |
|          50 | -23.92%  | 149.68%            | -46.83% |    -0.29 |       60 | 34.44%     | ok               |
|          35 | -31.92%  | 149.68%            | -37.32% |    -0.39 |       72 | 40.43%     | ok               |
|          30 | -33.81%  | 149.68%            | -40.39% |    -0.41 |       72 | 43.09%     | ok               |
|          25 | -37.83%  | 149.68%            | -42.91% |    -0.46 |       77 | 46.26%     | ok               |

## GE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 4.89%    | 88.79%             | -21.25% |     0.2  |       60 | 33.78%     | ok               |
|          45 | -2.34%   | 88.79%             | -21.88% |     0.05 |       70 | 36.44%     | ok               |
|          20 | -8.34%   | 88.79%             | -25.05% |    -0.03 |       71 | 52.41%     | ok               |
|          30 | -8.43%   | 88.79%             | -27.82% |    -0.04 |       76 | 48.09%     | ok               |
|          25 | -8.86%   | 88.79%             | -29.91% |    -0.05 |       72 | 49.92%     | ok               |

## GLD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 18.86%   | 77.41%             | -13.87% |     0.5  |       48 | 46.92%     | ok               |
|          20 | 17.24%   | 77.41%             | -13.87% |     0.47 |       49 | 48.59%     | ok               |
|          30 | 13.20%   | 77.41%             | -13.87% |     0.39 |       50 | 45.76%     | ok               |
|          35 | 10.20%   | 77.41%             | -15.09% |     0.33 |       52 | 43.43%     | ok               |
|          15 | 6.47%    | 77.41%             | -18.05% |     0.23 |       57 | 51.91%     | ok               |

## GOOGL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 62.79%   | 101.22%            | -17.38% |     1.1  |       59 | 43.76%     | ok               |
|          30 | 58.85%   | 101.22%            | -17.54% |     1.03 |       57 | 47.25%     | ok               |
|          45 | 51.21%   | 101.22%            | -11.66% |     1.02 |       52 | 37.27%     | ok               |
|          25 | 56.43%   | 101.22%            | -16.87% |     0.98 |       57 | 49.75%     | ok               |
|          50 | 45.42%   | 101.22%            | -11.52% |     0.96 |       46 | 32.28%     | ok               |

## GRT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 68.95%   | -80.49%            | -33.74% |     0.76 |       77 | 45.79%     | ok               |
|          45 | 45.34%   | -80.49%            | -39.76% |     0.64 |       48 | 27.78%     | ok               |
|          15 | 40.10%   | -80.49%            | -39.66% |     0.57 |       69 | 62.45%     | ok               |
|          50 | 31.50%   | -80.49%            | -31.62% |     0.53 |       46 | 21.26%     | ok               |
|          25 | 31.70%   | -80.49%            | -37.25% |     0.51 |       78 | 52.11%     | ok               |

## GS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 23.02%   | 94.54%             | -20.56% |     0.51 |       68 | 56.41%     | ok               |
|          20 | 4.12%    | 94.54%             | -23.19% |     0.18 |       68 | 53.08%     | ok               |
|          40 | 4.13%    | 94.54%             | -16.24% |     0.18 |       70 | 42.10%     | ok               |
|          25 | -1.15%   | 94.54%             | -23.32% |     0.08 |       68 | 50.58%     | ok               |
|          30 | -3.31%   | 94.54%             | -21.94% |     0.03 |       70 | 48.09%     | ok               |

## HBAR-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -18.60%  | -17.93%            | -39.26% |    -0.27 |       18 | 17.74%     | ok               |
|          45 | -33.67%  | -17.93%            | -48.27% |    -0.69 |       22 | 23.77%     | ok               |
|          40 | -36.83%  | -17.93%            | -51.01% |    -0.78 |       28 | 29.06%     | ok               |
|          30 | -42.75%  | -17.93%            | -56.47% |    -0.92 |       40 | 38.11%     | ok               |
|          35 | -42.15%  | -17.93%            | -56.01% |    -0.93 |       30 | 33.58%     | ok               |

## HD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 1.72%    | -5.71%             | -17.15% |     0.13 |       67 | 43.59%     | ok               |
|          40 | 1.06%    | -5.71%             | -16.74% |     0.1  |       72 | 34.78%     | ok               |
|          35 | 0.84%    | -5.71%             | -17.81% |     0.1  |       70 | 39.60%     | ok               |
|          45 | 0.27%    | -5.71%             | -17.41% |     0.07 |       48 | 29.95%     | ok               |
|          25 | -1.38%   | -5.71%             | -18.17% |     0.05 |       66 | 45.92%     | ok               |

## HON Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -9.65%   | 6.80%              | -20.54% |    -0.23 |       70 | 32.78%     | ok               |
|          45 | -13.43%  | 6.80%              | -22.88% |    -0.33 |       72 | 38.27%     | ok               |
|          35 | -24.73%  | 6.80%              | -31.30% |    -0.63 |       91 | 49.92%     | ok               |
|          30 | -26.42%  | 6.80%              | -33.53% |    -0.66 |       93 | 54.91%     | ok               |
|          40 | -24.93%  | 6.80%              | -31.84% |    -0.67 |       78 | 42.76%     | ok               |

## HYG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -4.40%   | 0.40%              | -7.76%  |    -0.5  |       70 | 34.11%     | ok               |
|          45 | -6.17%   | 0.40%              | -8.86%  |    -0.74 |       70 | 30.45%     | ok               |
|          30 | -6.75%   | 0.40%              | -10.59% |    -0.75 |       85 | 39.27%     | ok               |
|          35 | -6.59%   | 0.40%              | -9.66%  |    -0.75 |       79 | 35.94%     | ok               |
|          15 | -7.94%   | 0.40%              | -11.25% |    -0.83 |       92 | 46.76%     | ok               |

## IBIT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 66.22%   | 22.57%             | -19.20% |     0.95 |       44 | 42.11%     | ok               |
|          50 | 52.34%   | 22.57%             | -17.37% |     0.94 |       26 | 25.51%     | ok               |
|          45 | 42.96%   | 22.57%             | -17.37% |     0.79 |       30 | 26.72%     | ok               |
|          30 | 36.51%   | 22.57%             | -18.95% |     0.67 |       40 | 35.02%     | ok               |
|          40 | 33.91%   | 22.57%             | -18.18% |     0.67 |       32 | 28.74%     | ok               |

## IBM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -18.80%  | 37.18%             | -49.43% |    -0.13 |       83 | 60.57%     | ok               |
|          35 | -22.90%  | 37.18%             | -47.10% |    -0.26 |       63 | 45.26%     | ok               |
|          30 | -25.03%  | 37.18%             | -48.94% |    -0.3  |       69 | 49.08%     | ok               |
|          20 | -30.45%  | 37.18%             | -53.45% |    -0.37 |       69 | 53.58%     | ok               |
|          50 | -27.21%  | 37.18%             | -45.88% |    -0.39 |       44 | 34.44%     | ok               |

## ICP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -17.76%  | -48.94%            | -46.42% |     0.09 |       79 | 39.46%     | ok               |
|          35 | -11.81%  | -48.94%            | -51.30% |     0.08 |       72 | 33.72%     | ok               |
|          40 | -12.44%  | -48.94%            | -45.75% |     0.06 |       64 | 28.93%     | ok               |
|          15 | -44.47%  | -48.94%            | -59.36% |    -0.13 |       79 | 50.38%     | ok               |
|          20 | -46.41%  | -48.94%            | -62.47% |    -0.18 |       88 | 47.51%     | ok               |

## IEF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.38%   | -2.60%             | -10.32% |    -0.75 |       72 | 42.26%     | ok               |
|          15 | -7.57%   | -2.60%             | -11.04% |    -0.88 |       71 | 43.93%     | ok               |
|          50 | -6.87%   | -2.60%             | -9.11%  |    -1.16 |       56 | 21.80%     | ok               |
|          40 | -8.10%   | -2.60%             | -11.39% |    -1.18 |       62 | 26.62%     | ok               |
|          45 | -8.07%   | -2.60%             | -11.30% |    -1.21 |       58 | 24.96%     | ok               |

## IEMG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -2.38%   | 45.04%             | -14.22% |    -0.04 |       54 | 31.11%     | ok               |
|          45 | -3.18%   | 45.04%             | -15.23% |    -0.07 |       50 | 33.61%     | ok               |
|          40 | -4.68%   | 45.04%             | -18.73% |    -0.12 |       62 | 36.61%     | ok               |
|          35 | -6.08%   | 45.04%             | -23.75% |    -0.15 |       65 | 38.94%     | ok               |
|          25 | -10.22%  | 45.04%             | -26.17% |    -0.29 |       60 | 41.76%     | ok               |

## INJ-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 6.03%    | -33.36%            | -51.11% |     0.31 |       60 | 37.16%     | ok               |
|          40 | 6.66%    | -33.36%            | -44.20% |     0.3  |       50 | 33.91%     | ok               |
|          45 | -2.08%   | -33.36%            | -42.01% |     0.2  |       54 | 28.35%     | ok               |
|          30 | -27.85%  | -33.36%            | -68.17% |    -0.03 |       63 | 40.23%     | ok               |
|          15 | -42.85%  | -33.36%            | -75.88% |    -0.17 |       77 | 50.96%     | ok               |

## INTC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 70.01%   | 217.05%            | -49.32% |     0.71 |       56 | 33.78%     | ok               |
|          50 | 64.73%   | 217.05%            | -48.35% |     0.68 |       60 | 29.95%     | ok               |
|          15 | 55.98%   | 217.05%            | -53.65% |     0.61 |       76 | 59.40%     | ok               |
|          40 | 51.36%   | 217.05%            | -55.86% |     0.59 |       64 | 37.94%     | ok               |
|          25 | 46.47%   | 217.05%            | -56.41% |     0.56 |       77 | 50.75%     | ok               |

## INTU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 10.17%   | -50.14%            | -34.35% |     0.29 |       65 | 28.45%     | ok               |
|          45 | -1.24%   | -50.14%            | -37.13% |     0.1  |       65 | 32.78%     | ok               |
|          25 | -6.35%   | -50.14%            | -35.05% |     0.04 |       72 | 49.42%     | ok               |
|          35 | -7.68%   | -50.14%            | -42.78% |    -0    |       73 | 40.43%     | ok               |
|          40 | -7.55%   | -50.14%            | -40.63% |    -0.01 |       69 | 36.61%     | ok               |

## ITA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -0.69%   | 54.23%             | -27.64% |     0.07 |       83 | 60.73%     | ok               |
|          50 | 0.06%    | 54.23%             | -21.48% |     0.07 |       76 | 36.61%     | ok               |
|          30 | -2.36%   | 54.23%             | -23.75% |     0.01 |       78 | 48.42%     | ok               |
|          20 | -7.03%   | 54.23%             | -27.64% |    -0.11 |       84 | 54.74%     | ok               |
|          40 | -5.75%   | 54.23%             | -20.54% |    -0.11 |       78 | 41.76%     | ok               |

## IWM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 13.97%   | 35.38%             | -10.63% |     0.54 |       54 | 34.94%     | ok               |
|          20 | 12.47%   | 35.38%             | -10.41% |     0.48 |       60 | 35.94%     | ok               |
|          40 | 10.06%   | 35.38%             | -12.26% |     0.45 |       48 | 29.62%     | ok               |
|          35 | 8.16%    | 35.38%             | -12.26% |     0.36 |       54 | 32.11%     | ok               |
|          15 | 9.01%    | 35.38%             | -12.11% |     0.36 |       78 | 41.76%     | ok               |

## JNJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 20.07%   | 69.19%             | -10.57% |     0.81 |       38 | 34.61%     | ok               |
|          15 | 15.04%   | 69.19%             | -17.37% |     0.54 |       56 | 53.08%     | ok               |
|          45 | 9.79%    | 69.19%             | -13.35% |     0.43 |       44 | 38.27%     | ok               |
|          30 | 10.08%   | 69.19%             | -16.86% |     0.41 |       58 | 46.59%     | ok               |
|          20 | 9.72%    | 69.19%             | -16.96% |     0.39 |       62 | 49.58%     | ok               |

## JPM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 5.41%    | 70.39%             | -15.90% |     0.25 |       50 | 32.78%     | ok               |
|          45 | -5.10%   | 70.39%             | -21.91% |    -0.1  |       54 | 35.44%     | ok               |
|          20 | -20.47%  | 70.39%             | -35.58% |    -0.44 |       86 | 48.92%     | ok               |
|          35 | -17.46%  | 70.39%             | -27.43% |    -0.49 |       74 | 41.26%     | ok               |
|          40 | -18.12%  | 70.39%             | -28.47% |    -0.52 |       66 | 38.10%     | ok               |

## KO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 25.10%   | 48.17%             | -8.64%  |     0.89 |       52 | 36.61%     | ok               |
|          35 | 20.85%   | 48.17%             | -8.21%  |     0.77 |       56 | 35.11%     | ok               |
|          40 | 17.94%   | 48.17%             | -9.28%  |     0.72 |       58 | 31.78%     | ok               |
|          25 | 18.77%   | 48.17%             | -10.16% |     0.69 |       60 | 39.43%     | ok               |
|          20 | 5.66%    | 48.17%             | -15.99% |     0.25 |       77 | 43.59%     | ok               |

## LDO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 64.16%   | -65.06%            | -39.01% |     0.69 |       77 | 58.81%     | ok               |
|          30 | 49.35%   | -65.06%            | -50.81% |     0.62 |       68 | 46.55%     | ok               |
|          20 | 48.30%   | -65.06%            | -41.22% |     0.61 |       79 | 54.21%     | ok               |
|          35 | 25.35%   | -65.06%            | -58.48% |     0.46 |       74 | 39.08%     | ok               |
|          25 | 20.07%   | -65.06%            | -47.69% |     0.43 |       78 | 51.15%     | ok               |

## LIN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -7.26%   | 14.09%             | -23.00% |    -0.19 |       66 | 44.43%     | ok               |
|          25 | -7.19%   | 14.09%             | -22.01% |    -0.19 |       73 | 41.43%     | ok               |
|          15 | -9.01%   | 14.09%             | -23.68% |    -0.24 |       72 | 47.75%     | ok               |
|          30 | -10.29%  | 14.09%             | -20.61% |    -0.32 |       74 | 38.60%     | ok               |
|          35 | -12.41%  | 14.09%             | -19.70% |    -0.44 |       72 | 31.61%     | ok               |

## LINK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 41.07%   | -28.79%            | -33.64% |     0.59 |       68 | 45.21%     | ok               |
|          45 | 20.20%   | -28.79%            | -33.71% |     0.42 |       52 | 31.61%     | ok               |
|          35 | 18.04%   | -28.79%            | -34.21% |     0.4  |       62 | 41.19%     | ok               |
|          40 | 10.41%   | -28.79%            | -34.00% |     0.32 |       58 | 35.63%     | ok               |
|          25 | -1.67%   | -28.79%            | -46.32% |     0.23 |       64 | 48.66%     | ok               |

## LLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 0.30%    | 54.82%             | -38.23% |     0.12 |       50 | 35.44%     | ok               |
|          15 | -13.85%  | 54.82%             | -48.12% |    -0.08 |       70 | 60.23%     | ok               |
|          45 | -12.92%  | 54.82%             | -42.75% |    -0.14 |       60 | 39.10%     | ok               |
|          40 | -23.98%  | 54.82%             | -46.32% |    -0.36 |       70 | 42.10%     | ok               |
|          20 | -27.61%  | 54.82%             | -52.31% |    -0.37 |       77 | 55.24%     | ok               |

## LRCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -19.19%  | 189.58%            | -48.71% |    -0.1  |       74 | 33.94%     | ok               |
|          15 | -28.00%  | 189.58%            | -55.17% |    -0.13 |       79 | 50.75%     | ok               |
|          40 | -25.05%  | 189.58%            | -55.33% |    -0.16 |       70 | 39.93%     | ok               |
|          35 | -26.49%  | 189.58%            | -58.47% |    -0.17 |       78 | 42.10%     | ok               |
|          30 | -30.42%  | 189.58%            | -60.58% |    -0.24 |       80 | 42.60%     | ok               |

## LTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 9.91%    | -41.26%            | -34.94% |     0.31 |       64 | 45.40%     | ok               |
|          45 | 8.42%    | -41.26%            | -37.29% |     0.29 |       58 | 35.63%     | ok               |
|          30 | -2.19%   | -41.26%            | -31.17% |     0.17 |       68 | 52.68%     | ok               |
|          25 | -5.70%   | -41.26%            | -34.22% |     0.13 |       70 | 54.98%     | ok               |
|          40 | -10.17%  | -41.26%            | -40.31% |     0.04 |       56 | 41.00%     | ok               |

## MCD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 11.66%   | -5.98%             | -9.22%  |     0.54 |       46 | 25.12%     | ok               |
|          45 | 2.23%    | -5.98%             | -16.79% |     0.14 |       54 | 28.95%     | ok               |
|          40 | 1.34%    | -5.98%             | -18.49% |     0.11 |       65 | 32.45%     | ok               |
|          35 | -3.01%   | -5.98%             | -16.63% |    -0.06 |       69 | 37.44%     | ok               |
|          30 | -4.25%   | -5.98%             | -21.88% |    -0.1  |       79 | 40.60%     | ok               |

## META Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -8.40%   | 58.17%             | -37.10% |    -0.03 |       66 | 39.93%     | ok               |
|          40 | -14.42%  | 58.17%             | -40.49% |    -0.14 |       68 | 42.93%     | ok               |
|          50 | -18.60%  | 58.17%             | -38.90% |    -0.25 |       68 | 35.77%     | ok               |
|          25 | -25.09%  | 58.17%             | -45.35% |    -0.32 |       75 | 52.91%     | ok               |
|          30 | -25.15%  | 58.17%             | -44.52% |    -0.33 |       72 | 50.25%     | ok               |

## MPC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 30.35%   | 170.12%            | -19.02% |     0.6  |       54 | 40.27%     | ok               |
|          40 | 28.20%   | 170.12%            | -20.88% |     0.56 |       64 | 46.92%     | ok               |
|          45 | 25.95%   | 170.12%            | -20.23% |     0.53 |       60 | 44.26%     | ok               |
|          35 | 27.30%   | 170.12%            | -31.08% |     0.53 |       70 | 49.58%     | ok               |
|          30 | 21.08%   | 170.12%            | -34.29% |     0.44 |       72 | 52.25%     | ok               |

## MRK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -13.09%  | 10.76%             | -28.39% |    -0.16 |       83 | 51.91%     | ok               |
|          25 | -13.85%  | 10.76%             | -31.07% |    -0.2  |       70 | 44.09%     | ok               |
|          20 | -18.07%  | 10.76%             | -29.34% |    -0.29 |       75 | 47.42%     | ok               |
|          50 | -14.54%  | 10.76%             | -23.01% |    -0.3  |       56 | 28.45%     | ok               |
|          45 | -16.67%  | 10.76%             | -25.38% |    -0.33 |       57 | 31.78%     | ok               |

## MS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 2.61%    | 84.09%             | -22.02% |     0.15 |       74 | 58.24%     | ok               |
|          40 | 1.96%    | 84.09%             | -19.99% |     0.13 |       74 | 39.27%     | ok               |
|          20 | 0.18%    | 84.09%             | -25.68% |     0.09 |       75 | 53.08%     | ok               |
|          30 | -5.02%   | 84.09%             | -27.79% |    -0.04 |       75 | 48.25%     | ok               |
|          25 | -6.48%   | 84.09%             | -28.36% |    -0.07 |       73 | 50.42%     | ok               |

## MSFT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -12.72%  | 26.33%             | -25.26% |    -0.27 |       74 | 37.60%     | ok               |
|          50 | -17.88%  | 26.33%             | -26.14% |    -0.45 |       66 | 31.95%     | ok               |
|          35 | -21.57%  | 26.33%             | -35.38% |    -0.46 |       75 | 46.59%     | ok               |
|          40 | -21.58%  | 26.33%             | -34.77% |    -0.48 |       73 | 41.26%     | ok               |
|          30 | -24.93%  | 26.33%             | -39.15% |    -0.52 |       83 | 51.41%     | ok               |

## MU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 167.47%  | 637.50%            | -64.26% |     1.1  |       58 | 47.92%     | ok               |
|          15 | 193.12%  | 637.50%            | -61.96% |     1.09 |       51 | 59.40%     | ok               |
|          30 | 142.61%  | 637.50%            | -68.76% |     1.01 |       51 | 52.41%     | ok               |
|          25 | 141.18%  | 637.50%            | -67.90% |     0.99 |       51 | 53.91%     | ok               |
|          35 | 133.97%  | 637.50%            | -69.35% |     0.98 |       63 | 50.25%     | ok               |

## NEAR-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 189.00%  | 62.36%             | -38.74% |     1.3  |       28 | 22.03%     | ok               |
|          40 | 196.86%  | 62.36%             | -42.59% |     1.24 |       42 | 31.23%     | ok               |
|          45 | 149.14%  | 62.36%             | -38.08% |     1.09 |       44 | 27.20%     | ok               |
|          30 | 158.95%  | 62.36%             | -46.60% |     1.07 |       71 | 44.25%     | ok               |
|          35 | 139.03%  | 62.36%             | -52.37% |     1.04 |       64 | 35.82%     | ok               |

## NEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 4.48%    | 180.84%            | -31.25% |     0.23 |       63 | 58.57%     | ok               |
|          20 | 3.70%    | 180.84%            | -30.50% |     0.21 |       70 | 54.08%     | ok               |
|          25 | -14.27%  | 180.84%            | -39.51% |    -0.04 |       66 | 51.91%     | ok               |
|          50 | -13.27%  | 180.84%            | -33.03% |    -0.07 |       50 | 38.10%     | ok               |
|          30 | -23.49%  | 180.84%            | -39.56% |    -0.21 |       70 | 50.08%     | ok               |

## NFLX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 31.99%   | 14.23%             | -16.28% |     0.8  |       44 | 33.11%     | ok               |
|          40 | 30.88%   | 14.23%             | -15.02% |     0.73 |       50 | 41.10%     | ok               |
|          35 | 26.43%   | 14.23%             | -18.30% |     0.62 |       74 | 45.76%     | ok               |
|          45 | 19.15%   | 14.23%             | -15.48% |     0.51 |       56 | 37.60%     | ok               |
|          15 | 9.41%    | 14.23%             | -26.59% |     0.28 |       71 | 65.06%     | ok               |

## NKE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -16.21%  | -59.37%            | -42.13% |    -0.15 |       71 | 40.43%     | ok               |
|          20 | -23.50%  | -59.37%            | -49.34% |    -0.22 |       83 | 54.08%     | ok               |
|          25 | -26.67%  | -59.37%            | -51.20% |    -0.28 |       83 | 51.41%     | ok               |
|          15 | -28.43%  | -59.37%            | -54.28% |    -0.3  |       86 | 57.90%     | ok               |
|          40 | -20.78%  | -59.37%            | -31.79% |    -0.35 |       65 | 32.28%     | ok               |

## NOW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 9.63%    | -2.02%             | -30.43% |     0.29 |       80 | 50.08%     | ok               |
|          20 | 8.52%    | -2.02%             | -39.71% |     0.28 |       75 | 56.57%     | ok               |
|          25 | 4.47%    | -2.02%             | -37.51% |     0.23 |       72 | 53.58%     | ok               |
|          15 | 0.58%    | -2.02%             | -43.06% |     0.19 |       83 | 59.57%     | ok               |
|          40 | -0.02%   | -2.02%             | -36.21% |     0.15 |       70 | 39.27%     | ok               |

## NVDA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -36.17%  | 77.20%             | -43.08% |    -0.55 |       78 | 44.21%     | ok               |
|          20 | -44.65%  | 77.20%             | -44.65% |    -0.63 |       78 | 52.23%     | ok               |
|          25 | -44.56%  | 77.20%             | -44.56% |    -0.69 |       79 | 47.24%     | ok               |
|          15 | -50.14%  | 77.20%             | -53.41% |    -0.72 |       77 | 55.61%     | ok               |
|          35 | -45.77%  | 77.20%             | -51.54% |    -0.82 |       88 | 41.35%     | ok               |

## OP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 23.99%   | -84.94%            | -30.20% |     0.5  |       32 | 9.20%      | ok               |
|          45 | 19.98%   | -84.94%            | -28.24% |     0.42 |       34 | 13.79%     | ok               |
|          40 | -5.98%   | -84.94%            | -43.36% |     0.11 |       46 | 22.03%     | ok               |
|          15 | -45.81%  | -84.94%            | -55.83% |    -0.3  |       72 | 44.25%     | ok               |
|          35 | -38.27%  | -84.94%            | -56.61% |    -0.36 |       56 | 26.63%     | ok               |

## ORCL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 165.59%  | 8.36%              | -32.54% |     1.11 |       69 | 61.56%     | ok               |
|          25 | 113.54%  | 8.36%              | -27.76% |     0.93 |       61 | 54.08%     | ok               |
|          45 | 98.52%   | 8.36%              | -32.35% |     0.91 |       58 | 39.60%     | ok               |
|          35 | 103.43%  | 8.36%              | -31.95% |     0.9  |       62 | 48.25%     | ok               |
|          20 | 107.58%  | 8.36%              | -29.32% |     0.89 |       70 | 57.24%     | ok               |

## OXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 0.23%    | -2.08%             | -28.48% |     0.13 |       73 | 42.76%     | ok               |
|          35 | -0.92%   | -2.08%             | -26.37% |     0.1  |       74 | 38.44%     | ok               |
|          50 | -3.22%   | -2.08%             | -26.34% |     0.04 |       46 | 27.45%     | ok               |
|          40 | -7.02%   | -2.08%             | -28.30% |    -0.02 |       64 | 34.28%     | ok               |
|          25 | -13.64%  | -2.08%             | -38.51% |    -0.12 |       79 | 46.42%     | ok               |

## PEP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 16.91%   | -28.39%            | -11.62% |     0.71 |       38 | 24.96%     | ok               |
|          45 | 9.44%    | -28.39%            | -14.22% |     0.42 |       54 | 28.95%     | ok               |
|          35 | 6.24%    | -28.39%            | -21.42% |     0.26 |       75 | 39.27%     | ok               |
|          40 | 3.95%    | -28.39%            | -18.04% |     0.2  |       68 | 34.61%     | ok               |
|          30 | -0.55%   | -28.39%            | -21.35% |     0.05 |       76 | 45.59%     | ok               |

## PEPE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -56.54%  | -71.64%            | -61.29% |    -0.45 |       83 | 48.08%     | ok               |
|          15 | -67.33%  | -71.64%            | -66.06% |    -0.49 |       80 | 62.45%     | ok               |
|          20 | -64.14%  | -71.64%            | -63.30% |    -0.52 |       86 | 59.00%     | ok               |
|          25 | -62.13%  | -71.64%            | -64.26% |    -0.55 |       93 | 53.07%     | ok               |
|          35 | -58.01%  | -71.64%            | -61.54% |    -0.59 |       72 | 43.10%     | ok               |

## PFE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -13.17%  | 2.61%              | -23.37% |    -0.4  |       50 | 21.46%     | ok               |
|          40 | -14.79%  | 2.61%              | -27.08% |    -0.44 |       70 | 26.46%     | ok               |
|          50 | -13.66%  | 2.61%              | -25.42% |    -0.47 |       38 | 18.30%     | ok               |
|          35 | -23.00%  | 2.61%              | -32.87% |    -0.7  |       80 | 32.95%     | ok               |
|          30 | -34.49%  | 2.61%              | -41.77% |    -1.08 |       79 | 36.44%     | ok               |

## PG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -9.46%   | -5.08%             | -17.50% |    -0.37 |       56 | 27.62%     | ok               |
|          35 | -14.85%  | -5.08%             | -18.57% |    -0.59 |       64 | 31.28%     | ok               |
|          45 | -18.73%  | -5.08%             | -19.90% |    -0.87 |       56 | 24.96%     | ok               |
|          30 | -22.59%  | -5.08%             | -24.16% |    -0.91 |       66 | 34.44%     | ok               |
|          25 | -24.40%  | -5.08%             | -25.50% |    -0.99 |       76 | 35.77%     | ok               |

## PM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -4.19%   | 100.60%            | -32.20% |    -0.01 |       84 | 46.42%     | ok               |
|          20 | -6.70%   | 100.60%            | -33.51% |    -0.05 |       83 | 55.07%     | ok               |
|          30 | -7.20%   | 100.60%            | -35.15% |    -0.07 |       79 | 49.92%     | ok               |
|          40 | -11.51%  | 100.60%            | -37.94% |    -0.21 |       78 | 42.43%     | ok               |
|          50 | -11.04%  | 100.60%            | -35.70% |    -0.22 |       68 | 36.61%     | ok               |

## POL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 52.93%   | -63.24%            | -38.69% |     0.68 |       77 | 49.62%     | ok               |
|          25 | 26.64%   | -63.24%            | -38.69% |     0.47 |       71 | 54.98%     | ok               |
|          20 | 16.70%   | -63.24%            | -42.81% |     0.39 |       79 | 58.24%     | ok               |
|          40 | 3.00%    | -63.24%            | -31.98% |     0.22 |       58 | 31.03%     | ok               |
|          15 | -9.27%   | -63.24%            | -47.86% |     0.14 |       84 | 61.88%     | ok               |

## QCOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -11.06%  | -11.58%            | -54.50% |     0.04 |       71 | 45.09%     | ok               |
|          20 | -17.60%  | -11.58%            | -54.38% |    -0.04 |       67 | 48.42%     | ok               |
|          35 | -18.57%  | -11.58%            | -50.58% |    -0.09 |       79 | 40.77%     | ok               |
|          15 | -27.55%  | -11.58%            | -57.94% |    -0.18 |       69 | 51.08%     | ok               |
|          30 | -28.07%  | -11.58%            | -56.59% |    -0.23 |       77 | 43.26%     | ok               |

## QQQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 22.49%   | 60.47%             | -14.17% |     0.57 |       63 | 54.08%     | ok               |
|          25 | 14.29%   | 60.47%             | -12.88% |     0.43 |       61 | 47.92%     | ok               |
|          20 | 13.12%   | 60.47%             | -12.98% |     0.39 |       69 | 50.58%     | ok               |
|          30 | 6.57%    | 60.47%             | -14.20% |     0.25 |       66 | 45.92%     | ok               |
|          35 | -4.38%   | 60.47%             | -20.59% |    -0.05 |       72 | 42.10%     | ok               |

## RENDER-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 27.03%   | -63.93%            | -44.59% |     0.49 |       82 | 61.69%     | ok               |
|          20 | 24.34%   | -63.93%            | -43.43% |     0.47 |       85 | 58.43%     | ok               |
|          25 | 18.59%   | -63.93%            | -41.13% |     0.43 |       85 | 53.45%     | ok               |
|          30 | -24.34%  | -63.93%            | -45.62% |     0.01 |       90 | 47.32%     | ok               |
|          35 | -34.81%  | -63.93%            | -47.84% |    -0.18 |       86 | 40.80%     | ok               |

## RTX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 43.10%   | 77.36%             | -18.66% |     0.89 |       74 | 57.24%     | ok               |
|          25 | 38.21%   | 77.36%             | -18.59% |     0.82 |       62 | 54.58%     | ok               |
|          15 | 34.45%   | 77.36%             | -19.55% |     0.74 |       67 | 61.73%     | ok               |
|          30 | 27.97%   | 77.36%             | -16.99% |     0.65 |       66 | 51.91%     | ok               |
|          35 | 22.84%   | 77.36%             | -18.00% |     0.61 |       58 | 48.59%     | ok               |

## SBUX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -3.34%   | 23.71%             | -23.55% |     0.03 |       55 | 40.60%     | ok               |
|          40 | -4.42%   | 23.71%             | -25.43% |    -0.02 |       58 | 32.11%     | ok               |
|          45 | -6.23%   | 23.71%             | -27.26% |    -0.08 |       64 | 27.29%     | ok               |
|          35 | -8.64%   | 23.71%             | -26.54% |    -0.1  |       58 | 35.44%     | ok               |
|          20 | -14.86%  | 23.71%             | -30.94% |    -0.2  |       58 | 42.60%     | ok               |

## SCHW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -3.62%   | 30.16%             | -28.76% |     0    |       65 | 48.59%     | ok               |
|          45 | -2.78%   | 30.16%             | -16.53% |    -0.02 |       60 | 30.62%     | ok               |
|          20 | -4.80%   | 30.16%             | -29.24% |    -0.02 |       73 | 50.92%     | ok               |
|          50 | -4.01%   | 30.16%             | -13.28% |    -0.09 |       52 | 27.62%     | ok               |
|          15 | -13.91%  | 30.16%             | -31.37% |    -0.24 |       83 | 55.57%     | ok               |

## SHIB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -21.65%  | -68.69%            | -41.14% |    -0.14 |       60 | 38.89%     | ok               |
|          35 | -23.69%  | -68.69%            | -44.56% |    -0.15 |       71 | 46.55%     | ok               |
|          15 | -32.67%  | -68.69%            | -45.04% |    -0.23 |       86 | 66.67%     | ok               |
|          25 | -33.49%  | -68.69%            | -45.06% |    -0.27 |       80 | 58.05%     | ok               |
|          20 | -35.00%  | -68.69%            | -47.68% |    -0.28 |       80 | 61.69%     | ok               |

## SHY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          30 | -1.75%   | -0.06%             | -3.18% |    -0.58 |       48 | 37.10%     | ok               |
|          35 | -2.27%   | -0.06%             | -3.49% |    -0.78 |       52 | 35.44%     | ok               |
|          40 | -2.41%   | -0.06%             | -3.58% |    -0.83 |       54 | 33.94%     | ok               |
|          45 | -2.40%   | -0.06%             | -3.43% |    -0.88 |       54 | 28.62%     | ok               |
|          25 | -3.05%   | -0.06%             | -4.32% |    -1.01 |       62 | 39.60%     | ok               |

## SKY-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -59.34%  | -9.85%             | -60.48% |    -1.01 |       82 | 36.21%     | ok               |
|          15 | -67.46%  | -9.85%             | -67.16% |    -1.05 |       77 | 53.83%     | ok               |
|          30 | -64.06%  | -9.85%             | -64.20% |    -1.1  |       89 | 43.68%     | ok               |
|          45 | -61.48%  | -9.85%             | -62.01% |    -1.18 |       76 | 27.78%     | ok               |
|          25 | -67.82%  | -9.85%             | -67.25% |    -1.19 |       82 | 46.93%     | ok               |

## SLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 0.95%    | 4.43%              | -28.36% |     0.13 |       50 | 35.61%     | ok               |
|          45 | 0.64%    | 4.43%              | -25.01% |     0.12 |       62 | 32.11%     | ok               |
|          50 | -4.69%   | 4.43%              | -26.78% |    -0.02 |       50 | 25.62%     | ok               |
|          35 | -24.80%  | 4.43%              | -48.21% |    -0.42 |       72 | 43.43%     | ok               |
|          25 | -35.15%  | 4.43%              | -55.67% |    -0.62 |       84 | 53.08%     | ok               |

## SLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 49.11%   | 88.46%             | -34.04% |     0.71 |       54 | 30.12%     | ok               |
|          45 | 36.45%   | 88.46%             | -31.75% |     0.58 |       65 | 31.61%     | ok               |
|          40 | 35.37%   | 88.46%             | -34.28% |     0.57 |       69 | 33.61%     | ok               |
|          20 | 24.28%   | 88.46%             | -42.60% |     0.45 |       72 | 43.93%     | ok               |
|          15 | 24.26%   | 88.46%             | -47.98% |     0.44 |       73 | 48.75%     | ok               |

## SMH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 65.37%   | 133.02%            | -31.01% |     0.94 |       47 | 46.42%     | ok               |
|          25 | 50.42%   | 133.02%            | -32.94% |     0.81 |       44 | 44.93%     | ok               |
|          35 | 48.82%   | 133.02%            | -34.03% |     0.8  |       54 | 41.93%     | ok               |
|          30 | 46.32%   | 133.02%            | -33.66% |     0.76 |       48 | 43.59%     | ok               |
|          45 | 34.38%   | 133.02%            | -33.35% |     0.66 |       54 | 36.27%     | ok               |

## SNX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 16.71%   | -75.59%            | -41.29% |     0.39 |       56 | 27.20%     | ok               |
|          40 | 15.94%   | -75.59%            | -28.61% |     0.38 |       42 | 22.03%     | ok               |
|          20 | -13.39%  | -75.59%            | -53.03% |     0.1  |       73 | 43.87%     | ok               |
|          30 | -13.77%  | -75.59%            | -50.74% |     0.05 |       64 | 33.72%     | ok               |
|          50 | -9.36%   | -75.59%            | -29.88% |    -0.04 |       38 | 13.79%     | ok               |

## SOL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 29.24%   | -42.81%            | -39.74% |     0.51 |       60 | 40.42%     | ok               |
|          35 | 7.70%    | -42.81%            | -43.70% |     0.3  |       72 | 46.93%     | ok               |
|          45 | 0.18%    | -42.81%            | -46.83% |     0.19 |       62 | 34.67%     | ok               |
|          15 | -8.36%   | -42.81%            | -46.84% |     0.15 |       72 | 63.98%     | ok               |
|          25 | -12.13%  | -42.81%            | -41.36% |     0.09 |       72 | 57.47%     | ok               |

## SOXX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 62.90%   | 120.04%            | -39.65% |     0.88 |       54 | 45.09%     | ok               |
|          35 | 60.10%   | 120.04%            | -38.76% |     0.88 |       56 | 40.43%     | ok               |
|          30 | 58.38%   | 120.04%            | -40.14% |     0.85 |       56 | 42.93%     | ok               |
|          20 | 50.60%   | 120.04%            | -38.67% |     0.75 |       59 | 45.92%     | ok               |
|          40 | 40.52%   | 120.04%            | -41.03% |     0.68 |       58 | 38.27%     | ok               |

## SPY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 11.83%   | 46.74%             | -14.25% |     0.44 |       59 | 52.91%     | ok               |
|          15 | 11.29%   | 46.74%             | -16.80% |     0.42 |       63 | 55.57%     | ok               |
|          25 | 6.80%    | 46.74%             | -14.25% |     0.29 |       59 | 51.91%     | ok               |
|          30 | 0.61%    | 46.74%             | -15.53% |     0.08 |       64 | 49.25%     | ok               |
|          35 | -0.37%   | 46.74%             | -15.58% |     0.05 |       62 | 46.09%     | ok               |

## SUSHI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -6.33%   | -73.94%            | -34.75% |     0.08 |       54 | 16.86%     | ok               |
|          45 | -41.81%  | -73.94%            | -57.99% |    -0.49 |       56 | 21.65%     | ok               |
|          40 | -46.31%  | -73.94%            | -60.82% |    -0.52 |       59 | 28.16%     | ok               |
|          35 | -64.61%  | -73.94%            | -72.78% |    -0.87 |       80 | 33.33%     | ok               |
|          15 | -74.72%  | -73.94%            | -75.07% |    -0.98 |       90 | 49.43%     | ok               |

## T Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 61.74%   | 34.52%             | -15.08% |     1.04 |       73 | 65.56%     | ok               |
|          20 | 57.75%   | 34.52%             | -18.13% |     1.03 |       68 | 61.06%     | ok               |
|          25 | 55.96%   | 34.52%             | -17.66% |     1.01 |       68 | 58.90%     | ok               |
|          30 | 41.44%   | 34.52%             | -17.01% |     0.83 |       72 | 56.74%     | ok               |
|          35 | 26.02%   | 34.52%             | -14.49% |     0.6  |       78 | 52.41%     | ok               |

## TGT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -11.06%  | 8.46%              | -34.42% |    -0.16 |       60 | 37.60%     | ok               |
|          45 | -11.97%  | 8.46%              | -25.85% |    -0.23 |       48 | 28.62%     | ok               |
|          20 | -16.69%  | 8.46%              | -38.96% |    -0.25 |       88 | 45.42%     | ok               |
|          25 | -15.22%  | 8.46%              | -37.81% |    -0.25 |       70 | 40.77%     | ok               |
|          35 | -17.42%  | 8.46%              | -32.35% |    -0.35 |       60 | 33.94%     | ok               |

## TIA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -31.38%  | -81.64%            | -67.23% |     0.06 |       97 | 59.20%     | ok               |
|          35 | -23.81%  | -81.64%            | -66.58% |    -0.03 |       74 | 35.63%     | ok               |
|          25 | -34.82%  | -81.64%            | -69.36% |    -0.04 |       94 | 48.47%     | ok               |
|          20 | -45.44%  | -81.64%            | -72.22% |    -0.14 |       92 | 53.83%     | ok               |
|          30 | -47.52%  | -81.64%            | -75.93% |    -0.25 |       93 | 42.91%     | ok               |

## TLT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -10.72%  | -12.23%            | -13.23% |    -1.16 |       34 | 17.47%     | ok               |
|          40 | -15.60%  | -12.23%            | -17.65% |    -1.36 |       52 | 24.96%     | ok               |
|          45 | -14.23%  | -12.23%            | -15.73% |    -1.45 |       44 | 20.47%     | ok               |
|          30 | -19.63%  | -12.23%            | -21.85% |    -1.47 |       68 | 33.61%     | ok               |
|          35 | -20.13%  | -12.23%            | -21.68% |    -1.67 |       66 | 28.79%     | ok               |

## TMO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 56.83%   | 19.05%             | -8.17%  |     1.17 |       48 | 34.78%     | ok               |
|          45 | 44.91%   | 19.05%             | -9.69%  |     0.94 |       54 | 39.60%     | ok               |
|          40 | 38.53%   | 19.05%             | -9.91%  |     0.82 |       59 | 44.59%     | ok               |
|          35 | 39.97%   | 19.05%             | -13.84% |     0.79 |       71 | 50.25%     | ok               |
|          20 | 37.99%   | 19.05%             | -22.89% |     0.71 |       78 | 61.40%     | ok               |

## TMUS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -3.51%   | -4.81%             | -32.44% |     0.02 |       74 | 48.09%     | ok               |
|          15 | -9.19%   | -4.81%             | -40.53% |    -0.08 |       68 | 60.73%     | ok               |
|          50 | -7.84%   | -4.81%             | -32.38% |    -0.14 |       60 | 34.44%     | ok               |
|          25 | -12.70%  | -4.81%             | -38.76% |    -0.18 |       77 | 51.08%     | ok               |
|          20 | -14.43%  | -4.81%             | -39.27% |    -0.21 |       74 | 55.07%     | ok               |

## TRX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 10.78%   | 23.82%             | -18.79% |     0.4  |       54 | 39.46%     | ok               |
|          35 | 4.27%    | 23.82%             | -21.77% |     0.21 |       66 | 47.70%     | ok               |
|          20 | 1.83%    | 23.82%             | -25.45% |     0.14 |       61 | 57.47%     | ok               |
|          30 | 1.77%    | 23.82%             | -22.90% |     0.13 |       66 | 50.57%     | ok               |
|          45 | 1.05%    | 23.82%             | -22.76% |     0.11 |       46 | 35.82%     | ok               |

## TSLA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 34.46%   | 108.61%            | -34.01% |     0.54 |       66 | 29.95%     | ok               |
|          40 | 8.08%    | 108.61%            | -52.58% |     0.28 |       65 | 35.44%     | ok               |
|          45 | -14.96%  | 108.61%            | -54.39% |     0.01 |       71 | 32.45%     | ok               |
|          35 | -20.51%  | 108.61%            | -60.12% |    -0.03 |       76 | 38.10%     | ok               |
|          30 | -37.10%  | 108.61%            | -59.64% |    -0.26 |       80 | 42.93%     | ok               |

## TXN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 6.99%    | 41.48%             | -44.65% |     0.24 |       68 | 32.61%     | ok               |
|          35 | -13.09%  | 41.48%             | -42.44% |    -0.08 |       78 | 47.25%     | ok               |
|          40 | -14.61%  | 41.48%             | -44.87% |    -0.11 |       74 | 44.93%     | ok               |
|          20 | -18.51%  | 41.48%             | -37.58% |    -0.12 |       68 | 56.91%     | ok               |
|          45 | -15.28%  | 41.48%             | -45.45% |    -0.13 |       82 | 38.60%     | ok               |

## UNH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 33.09%   | -21.31%            | -36.91% |     0.58 |       56 | 28.29%     | ok               |
|          30 | 32.41%   | -21.31%            | -26.31% |     0.55 |       77 | 48.42%     | ok               |
|          35 | 28.38%   | -21.31%            | -27.21% |     0.5  |       72 | 43.43%     | ok               |
|          20 | 28.20%   | -21.31%            | -26.96% |     0.49 |       80 | 57.74%     | ok               |
|          15 | 28.16%   | -21.31%            | -26.07% |     0.49 |       85 | 63.89%     | ok               |

## UNI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 92.10%   | 3.83%              | -25.49% |     0.95 |       50 | 26.44%     | ok               |
|          45 | 75.83%   | 3.83%              | -34.45% |     0.81 |       56 | 33.91%     | ok               |
|          40 | 51.27%   | 3.83%              | -47.29% |     0.65 |       60 | 38.89%     | ok               |
|          35 | 29.05%   | 3.83%              | -54.42% |     0.49 |       68 | 44.25%     | ok               |
|          20 | -40.16%  | 3.83%              | -72.76% |    -0.1  |       93 | 59.58%     | ok               |

## UPS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -28.34%  | -29.67%            | -31.52% |    -0.53 |       62 | 36.44%     | ok               |
|          40 | -28.13%  | -29.67%            | -31.55% |    -0.53 |       58 | 30.95%     | ok               |
|          20 | -36.68%  | -29.67%            | -38.76% |    -0.7  |       84 | 50.08%     | ok               |
|          25 | -37.18%  | -29.67%            | -39.25% |    -0.73 |       76 | 46.76%     | ok               |
|          15 | -38.92%  | -29.67%            | -40.92% |    -0.75 |       86 | 53.91%     | ok               |

## USO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 5.24%    | 111.30%            | -42.23% |     0.22 |       69 | 41.26%     | ok               |
|          20 | 4.37%    | 111.30%            | -43.60% |     0.21 |       74 | 37.77%     | ok               |
|          45 | 4.88%    | 111.30%            | -34.01% |     0.21 |       50 | 25.62%     | ok               |
|          25 | -3.80%   | 111.30%            | -45.63% |     0.09 |       68 | 35.44%     | ok               |
|          50 | -4.25%   | 111.30%            | -30.14% |     0.05 |       54 | 23.96%     | ok               |

## VEA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 8.48%    | 38.54%             | -15.99% |     0.35 |       54 | 50.08%     | ok               |
|          20 | 2.17%    | 38.54%             | -17.04% |     0.14 |       59 | 47.42%     | ok               |
|          25 | -1.73%   | 38.54%             | -17.13% |    -0.02 |       57 | 45.42%     | ok               |
|          30 | -3.22%   | 38.54%             | -17.27% |    -0.08 |       62 | 42.26%     | ok               |
|          35 | -3.92%   | 38.54%             | -16.11% |    -0.11 |       52 | 40.43%     | ok               |

## VIXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -55.90%  | -64.44%            | -69.78% |    -0.66 |       36 | 9.15%      | ok               |
|          15 | -77.32%  | -64.44%            | -89.47% |    -0.8  |       95 | 43.09%     | ok               |
|          45 | -65.36%  | -64.44%            | -75.03% |    -0.86 |       56 | 14.14%     | ok               |
|          30 | -77.98%  | -64.44%            | -88.17% |    -0.93 |       94 | 32.11%     | ok               |
|          40 | -72.82%  | -64.44%            | -80.72% |    -0.99 |       68 | 17.97%     | ok               |

## VNQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -7.58%   | 11.78%             | -19.07% |    -0.33 |       60 | 28.12%     | ok               |
|          50 | -8.50%   | 11.78%             | -17.13% |    -0.39 |       52 | 24.79%     | ok               |
|          25 | -10.88%  | 11.78%             | -22.34% |    -0.4  |       69 | 42.60%     | ok               |
|          40 | -12.47%  | 11.78%             | -24.84% |    -0.54 |       78 | 33.61%     | ok               |
|          30 | -13.63%  | 11.78%             | -24.92% |    -0.54 |       73 | 39.77%     | ok               |

## VTI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 12.89%   | 45.55%             | -13.96% |     0.47 |       62 | 53.41%     | ok               |
|          15 | 8.25%    | 45.55%             | -15.70% |     0.32 |       59 | 55.74%     | ok               |
|          25 | 0.84%    | 45.55%             | -15.00% |     0.09 |       58 | 51.25%     | ok               |
|          30 | -6.72%   | 45.55%             | -17.64% |    -0.19 |       68 | 49.25%     | ok               |
|          40 | -7.84%   | 45.55%             | -19.77% |    -0.26 |       72 | 41.76%     | ok               |

## VWO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -9.78%   | 33.43%             | -22.18% |    -0.37 |       56 | 28.12%     | ok               |
|          15 | -12.91%  | 33.43%             | -24.01% |    -0.41 |       74 | 46.42%     | ok               |
|          45 | -10.98%  | 33.43%             | -23.75% |    -0.42 |       58 | 30.78%     | ok               |
|          40 | -11.44%  | 33.43%             | -23.57% |    -0.43 |       68 | 33.61%     | ok               |
|          20 | -14.30%  | 33.43%             | -26.14% |    -0.48 |       71 | 44.09%     | ok               |

## VZ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -3.10%   | 12.60%             | -12.96% |    -0.04 |       56 | 28.62%     | ok               |
|          20 | -22.23%  | 12.60%             | -35.02% |    -0.45 |       78 | 51.25%     | ok               |
|          25 | -19.06%  | 12.60%             | -24.83% |    -0.5  |       81 | 46.26%     | ok               |
|          35 | -19.31%  | 12.60%             | -25.86% |    -0.57 |       64 | 38.60%     | ok               |
|          45 | -18.77%  | 12.60%             | -24.82% |    -0.57 |       70 | 32.78%     | ok               |

## WFC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -8.30%   | 38.66%             | -21.57% |    -0.11 |       77 | 43.59%     | ok               |
|          50 | -6.21%   | 38.66%             | -18.29% |    -0.13 |       58 | 32.61%     | ok               |
|          30 | -17.86%  | 38.66%             | -28.90% |    -0.3  |       80 | 46.76%     | ok               |
|          20 | -20.85%  | 38.66%             | -29.87% |    -0.32 |       79 | 52.58%     | ok               |
|          40 | -13.97%  | 38.66%             | -23.94% |    -0.34 |       72 | 40.27%     | ok               |

## WIF-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -1.77%   | -82.96%            | -40.67% |     0.27 |       69 | 44.44%     | ok               |
|          25 | -11.79%  | -82.96%            | -44.74% |     0.16 |       67 | 40.42%     | ok               |
|          15 | -23.23%  | -82.96%            | -46.21% |     0.07 |       79 | 47.70%     | ok               |
|          50 | -11.38%  | -82.96%            | -35.47% |    -0.02 |       36 | 13.60%     | ok               |
|          30 | -30.58%  | -82.96%            | -52.76% |    -0.06 |       68 | 37.74%     | ok               |

## WMT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 36.56%   | 81.79%             | -12.18% |     1.11 |       36 | 36.94%     | ok               |
|          45 | 35.42%   | 81.79%             | -14.14% |     1.03 |       42 | 39.27%     | ok               |
|          35 | 25.54%   | 81.79%             | -18.25% |     0.75 |       58 | 45.59%     | ok               |
|          40 | 23.92%   | 81.79%             | -18.53% |     0.73 |       50 | 40.93%     | ok               |
|          15 | 7.11%    | 81.79%             | -26.24% |     0.25 |       82 | 59.57%     | ok               |

## XBI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 13.65%   | 67.69%             | -16.08% |     0.41 |       52 | 34.11%     | ok               |
|          45 | 9.33%    | 67.69%             | -15.46% |     0.31 |       50 | 31.61%     | ok               |
|          35 | 2.68%    | 67.69%             | -17.66% |     0.15 |       60 | 36.94%     | ok               |
|          30 | 0.54%    | 67.69%             | -17.66% |     0.1  |       62 | 38.44%     | ok               |
|          50 | 0.10%    | 67.69%             | -15.41% |     0.08 |       50 | 28.62%     | ok               |

## XLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -2.11%   | 11.65%             | -15.73% |    -0.04 |       38 | 21.80%     | ok               |
|          40 | -3.01%   | 11.65%             | -17.29% |    -0.07 |       54 | 25.96%     | ok               |
|          45 | -5.62%   | 11.65%             | -17.09% |    -0.18 |       42 | 23.46%     | ok               |
|          35 | -6.36%   | 11.65%             | -20.65% |    -0.19 |       56 | 29.45%     | ok               |
|          25 | -10.72%  | 11.65%             | -22.60% |    -0.35 |       64 | 35.61%     | ok               |

## XLC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 13.91%   | 37.29%             | -12.33% |     0.51 |       61 | 50.08%     | ok               |
|          25 | 13.35%   | 37.29%             | -12.31% |     0.49 |       60 | 52.25%     | ok               |
|          20 | 12.72%   | 37.29%             | -11.04% |     0.45 |       63 | 54.74%     | ok               |
|          50 | 8.46%    | 37.29%             | -11.12% |     0.43 |       64 | 38.27%     | ok               |
|          40 | 9.04%    | 37.29%             | -13.38% |     0.38 |       62 | 43.76%     | ok               |

## XLE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 0.18%    | 45.90%             | -25.98% |     0.08 |       56 | 36.77%     | ok               |
|          35 | -2.05%   | 45.90%             | -26.89% |     0.03 |       65 | 43.43%     | ok               |
|          30 | -3.66%   | 45.90%             | -29.67% |    -0    |       69 | 45.59%     | ok               |
|          45 | -3.12%   | 45.90%             | -28.46% |    -0.01 |       60 | 38.94%     | ok               |
|          25 | -8.20%   | 45.90%             | -32.98% |    -0.11 |       79 | 48.75%     | ok               |

## XLF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -1.14%   | 33.63%             | -18.63% |     0.02 |       74 | 51.58%     | ok               |
|          15 | -1.32%   | 33.63%             | -20.19% |     0.02 |       78 | 54.58%     | ok               |
|          25 | -8.04%   | 33.63%             | -23.22% |    -0.23 |       81 | 48.42%     | ok               |
|          30 | -8.64%   | 33.63%             | -23.61% |    -0.26 |       82 | 46.42%     | ok               |
|          35 | -15.75%  | 33.63%             | -24.48% |    -0.6  |       72 | 42.76%     | ok               |

## XLI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 5.22%    | 35.58%             | -11.40% |     0.23 |       86 | 51.41%     | ok               |
|          20 | 1.42%    | 35.58%             | -12.74% |     0.11 |       75 | 46.42%     | ok               |
|          50 | -4.76%   | 35.58%             | -14.94% |    -0.18 |       60 | 31.78%     | ok               |
|          45 | -5.38%   | 35.58%             | -16.29% |    -0.19 |       70 | 34.28%     | ok               |
|          25 | -8.78%   | 35.58%             | -17.03% |    -0.29 |       78 | 44.43%     | ok               |

## XLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 69.60%   | 77.32%             | -14.75% |     1.15 |       45 | 51.75%     | ok               |
|          20 | 63.12%   | 77.32%             | -14.75% |     1.11 |       48 | 49.42%     | ok               |
|          25 | 57.40%   | 77.32%             | -14.75% |     1.07 |       44 | 47.42%     | ok               |
|          30 | 47.98%   | 77.32%             | -14.75% |     0.96 |       44 | 46.09%     | ok               |
|          35 | 31.47%   | 77.32%             | -14.71% |     0.72 |       56 | 43.43%     | ok               |

## XLM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 4.05%    | -42.01%            | -49.14% |     0.26 |       70 | 49.62%     | ok               |
|          40 | -1.54%   | -42.01%            | -47.28% |     0.19 |       52 | 36.78%     | ok               |
|          50 | 0.05%    | -42.01%            | -48.81% |     0.18 |       42 | 26.44%     | ok               |
|          30 | -5.07%   | -42.01%            | -54.58% |     0.16 |       68 | 47.51%     | ok               |
|          45 | -3.25%   | -42.01%            | -51.28% |     0.15 |       54 | 31.23%     | ok               |

## XLP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 14.26%   | 12.72%             | -5.66%  |     0.86 |       52 | 29.45%     | ok               |
|          40 | 11.89%   | 12.72%             | -7.77%  |     0.7  |       70 | 33.61%     | ok               |
|          50 | 10.42%   | 12.72%             | -6.08%  |     0.67 |       58 | 27.12%     | ok               |
|          35 | 10.92%   | 12.72%             | -9.73%  |     0.64 |       66 | 36.61%     | ok               |
|          30 | 7.71%    | 12.72%             | -10.28% |     0.45 |       67 | 38.44%     | ok               |

## XLU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 7.07%    | 17.67%             | -14.03% |     0.38 |       54 | 30.12%     | ok               |
|          45 | 5.90%    | 17.67%             | -14.97% |     0.32 |       58 | 31.28%     | ok               |
|          40 | 2.81%    | 17.67%             | -16.41% |     0.18 |       64 | 33.28%     | ok               |
|          35 | 0.08%    | 17.67%             | -19.71% |     0.05 |       64 | 35.94%     | ok               |
|          30 | -4.25%   | 17.67%             | -20.40% |    -0.14 |       69 | 39.43%     | ok               |

## XLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -21.30%  | 22.28%             | -22.40% |    -1.01 |       76 | 38.27%     | ok               |
|          30 | -21.66%  | 22.28%             | -22.75% |    -1.04 |       76 | 36.61%     | ok               |
|          15 | -24.55%  | 22.28%             | -24.70% |    -1.14 |       83 | 42.43%     | ok               |
|          20 | -24.39%  | 22.28%             | -24.54% |    -1.16 |       79 | 39.93%     | ok               |
|          35 | -25.56%  | 22.28%             | -26.58% |    -1.33 |       70 | 33.61%     | ok               |

## XLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -0.70%   | 30.51%             | -15.77% |     0.06 |       76 | 54.24%     | ok               |
|          30 | -4.15%   | 30.51%             | -18.35% |    -0.06 |       75 | 47.59%     | ok               |
|          20 | -5.95%   | 30.51%             | -19.25% |    -0.1  |       72 | 50.92%     | ok               |
|          25 | -8.05%   | 30.51%             | -19.98% |    -0.17 |       69 | 49.42%     | ok               |
|          50 | -6.34%   | 30.51%             | -15.82% |    -0.22 |       62 | 32.11%     | ok               |

## XOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 2.73%    | 53.89%             | -19.90% |     0.15 |       55 | 34.94%     | ok               |
|          50 | 1.92%    | 53.89%             | -21.35% |     0.13 |       38 | 27.12%     | ok               |
|          30 | 1.71%    | 53.89%             | -20.29% |     0.12 |       55 | 34.28%     | ok               |
|          20 | -3.12%   | 53.89%             | -25.56% |    -0.01 |       62 | 37.27%     | ok               |
|          45 | -3.17%   | 53.89%             | -23.33% |    -0.02 |       42 | 28.29%     | ok               |

## XRP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 15.50%   | -48.53%            | -31.38% |     0.37 |       72 | 42.91%     | ok               |
|          40 | -2.44%   | -48.53%            | -33.91% |     0.16 |       66 | 36.40%     | ok               |
|          30 | -13.67%  | -48.53%            | -31.82% |     0.03 |       67 | 47.89%     | ok               |
|          45 | -12.02%  | -48.53%            | -37.18% |     0.02 |       60 | 31.61%     | ok               |
|          50 | -15.75%  | -48.53%            | -39.26% |    -0.06 |       58 | 23.95%     | ok               |

## YFI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -48.35%  | -63.69%            | -45.92% |    -0.84 |       54 | 26.82%     | ok               |
|          45 | -44.22%  | -63.69%            | -41.59% |    -0.91 |       66 | 22.03%     | ok               |
|          35 | -57.22%  | -63.69%            | -55.21% |    -1.05 |       64 | 33.52%     | ok               |
|          50 | -46.31%  | -63.69%            | -46.31% |    -1.08 |       50 | 16.67%     | ok               |
|          30 | -64.90%  | -63.69%            | -63.60% |    -1.28 |       79 | 37.55%     | ok               |

## ZEC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 194.29%  | 2676.03%           | -30.64% |     1.06 |       46 | 32.18%     | ok               |
|          35 | 155.34%  | 2676.03%           | -50.84% |     0.94 |       52 | 37.74%     | ok               |
|          30 | 137.88%  | 2676.03%           | -56.50% |     0.89 |       59 | 41.19%     | ok               |
|          25 | 128.24%  | 2676.03%           | -58.07% |     0.86 |       57 | 43.68%     | ok               |
|          40 | 116.42%  | 2676.03%           | -54.22% |     0.84 |       54 | 35.63%     | ok               |
