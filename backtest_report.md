# Market Tracker Backtest Report

_Generated: 2026-11-18T07:14:58+00:00_

## Data Sources

- Crypto: Kraken -> Coinbase -> CoinGecko OHLC -> CoinPaprika fallback chain.
- Stocks / ETFs / indices: Stooq -> Yahoo Finance fallback chain.
- Data rows are generated from real market APIs. Mock OHLCV rows are not generated.

## Data Freshness

- Rows: **92,798**
- Symbols: **161**
- Date range: **2024-06-27** to **2026-11-18**

## Latest Signals

| symbol     | date                |         close |   composite_score | signal   | data_source   |
|:-----------|:--------------------|--------------:|------------------:|:---------|:--------------|
| AMGN       | 2026-11-17 00:00:00 |   457.93      |         48.5833   | LONG     | Yahoo Finance |
| BLK        | 2026-11-17 00:00:00 |  1180.67      |         56.0833   | LONG     | Yahoo Finance |
| CL         | 2026-11-17 00:00:00 |    99.61      |         59.25     | LONG     | Yahoo Finance |
| CMCSA      | 2026-11-17 00:00:00 |    25.31      |         36        | LONG     | Yahoo Finance |
| COST       | 2026-11-17 00:00:00 |  1110.08      |         61.75     | LONG     | Yahoo Finance |
| DIS        | 2026-11-17 00:00:00 |   116.94      |         76.25     | LONG     | Yahoo Finance |
| DXY-INDEX  | 2026-11-18 00:00:00 |   103.686     |         72.8495   | LONG     | Yahoo Finance |
| EOG        | 2026-11-17 00:00:00 |   154.91      |         39.5833   | LONG     | Yahoo Finance |
| GE         | 2026-11-17 00:00:00 |   326.4       |         65.1667   | LONG     | Yahoo Finance |
| HD         | 2026-11-17 00:00:00 |   339.01      |         55.0833   | LONG     | Yahoo Finance |
| JNJ        | 2026-11-17 00:00:00 |   278.7       |         55.9167   | LONG     | Yahoo Finance |
| KO         | 2026-11-17 00:00:00 |    98.79      |         74.75     | LONG     | Yahoo Finance |
| LIN        | 2026-11-17 00:00:00 |   515.11      |         30.0833   | LONG     | Yahoo Finance |
| LLY        | 2026-11-17 00:00:00 |  1415.55      |         52.0833   | LONG     | Yahoo Finance |
| MCD        | 2026-11-17 00:00:00 |   275.82      |         58.8333   | LONG     | Yahoo Finance |
| PEP        | 2026-11-17 00:00:00 |   142.02      |         64.6667   | LONG     | Yahoo Finance |
| PG         | 2026-11-17 00:00:00 |   171.72      |         72.75     | LONG     | Yahoo Finance |
| SBUX       | 2026-11-17 00:00:00 |   107.49      |         33.5833   | LONG     | Yahoo Finance |
| TGT        | 2026-11-17 00:00:00 |   159.53      |         72.0833   | LONG     | Yahoo Finance |
| UPS        | 2026-11-17 00:00:00 |   110.31      |         33.5833   | LONG     | Yahoo Finance |
| VIXY       | 2026-11-17 00:00:00 |    21.01      |         32.4167   | LONG     | Yahoo Finance |
| VNQ        | 2026-11-17 00:00:00 |    94.89      |         33.6667   | LONG     | Yahoo Finance |
| WMT        | 2026-11-17 00:00:00 |   127.52      |         35.25     | LONG     | Yahoo Finance |
| XLF        | 2026-11-17 00:00:00 |    57.07      |         39.3333   | LONG     | Yahoo Finance |
| XLP        | 2026-11-17 00:00:00 |    91.46      |         53.9167   | LONG     | Yahoo Finance |
| XLU        | 2026-11-17 00:00:00 |    43.42      |         39.3333   | LONG     | Yahoo Finance |
| XLV        | 2026-11-17 00:00:00 |   185.24      |         51.5833   | LONG     | Yahoo Finance |
| AAPL       | 2026-11-17 00:00:00 |   351.91      |         59.1667   | NEUTRAL  | Yahoo Finance |
| ABBV       | 2026-11-17 00:00:00 |   292.82      |         42.5      | NEUTRAL  | Yahoo Finance |
| ADBE       | 2026-11-17 00:00:00 |   235.55      |        -41.5833   | NEUTRAL  | Yahoo Finance |
| AMD        | 2026-11-17 00:00:00 |   503.41      |          2.08333  | NEUTRAL  | Yahoo Finance |
| AMZN       | 2026-11-17 00:00:00 |   257.89      |         42.6667   | NEUTRAL  | Yahoo Finance |
| ARB-USD    | 2026-11-18 00:00:00 |     0.1309    |        -61.9167   | NEUTRAL  | Kraken API    |
| ATOM-USD   | 2026-11-18 00:00:00 |     1.3105    |        -20.6667   | NEUTRAL  | Kraken API    |
| AVAX-USD   | 2026-11-18 00:00:00 |     7.177     |        -61.25     | NEUTRAL  | Kraken API    |
| AVGO       | 2026-11-17 00:00:00 |   341.6       |         -3.91667  | NEUTRAL  | Yahoo Finance |
| BAC        | 2026-11-17 00:00:00 |    49.44      |        -25.9167   | NEUTRAL  | Yahoo Finance |
| C          | 2026-11-17 00:00:00 |   119.94      |        -45.75     | NEUTRAL  | Yahoo Finance |
| COP        | 2026-11-17 00:00:00 |   139.48      |         16.4167   | NEUTRAL  | Yahoo Finance |
| CVX        | 2026-11-17 00:00:00 |   216.13      |        -17.25     | NEUTRAL  | Yahoo Finance |
| DE         | 2026-11-17 00:00:00 |   649.23      |         -2.08333  | NEUTRAL  | Yahoo Finance |
| DIA        | 2026-11-17 00:00:00 |   507.31      |        -39.25     | NEUTRAL  | Yahoo Finance |
| EFA        | 2026-11-17 00:00:00 |   101.35      |        -61.75     | NEUTRAL  | Yahoo Finance |
| FXI        | 2026-11-17 00:00:00 |    32.88      |        -23.5833   | NEUTRAL  | Yahoo Finance |
| GDX        | 2026-11-17 00:00:00 |    79.57      |        -62.8333   | NEUTRAL  | Yahoo Finance |
| GDXJ       | 2026-11-17 00:00:00 |    95.84      |        -61.5      | NEUTRAL  | Yahoo Finance |
| GLD        | 2026-11-17 00:00:00 |   352.48      |        -67.3333   | NEUTRAL  | Yahoo Finance |
| GRT-USD    | 2026-11-18 00:00:00 |     0.01742   |        -20.6667   | NEUTRAL  | Kraken API    |
| GS         | 2026-11-17 00:00:00 |   877.52      |        -42.6667   | NEUTRAL  | Yahoo Finance |
| HBAR-USD   | 2026-11-18 00:00:00 |     0.05743   |        -64.5833   | NEUTRAL  | Kraken API    |
| HON        | 2026-11-17 00:00:00 |   218.96      |        -32.3333   | NEUTRAL  | Yahoo Finance |
| IBM        | 2026-11-17 00:00:00 |   231.09      |        -29.0833   | NEUTRAL  | Yahoo Finance |
| ICP-USD    | 2026-11-18 00:00:00 |     2.309     |        -28.4167   | NEUTRAL  | Kraken API    |
| INJ-USD    | 2026-11-18 00:00:00 |     7.346     |        -21.6667   | NEUTRAL  | Kraken API    |
| INTU       | 2026-11-17 00:00:00 |   320.79      |        -21.5833   | NEUTRAL  | Yahoo Finance |
| ITA        | 2026-11-17 00:00:00 |    69.6       |        -27.1667   | NEUTRAL  | Yahoo Finance |
| IWM        | 2026-11-17 00:00:00 |   269.05      |        -61.25     | NEUTRAL  | Yahoo Finance |
| JPM        | 2026-11-17 00:00:00 |   329.96      |          6.91667  | NEUTRAL  | Yahoo Finance |
| META       | 2026-11-17 00:00:00 |   618.87      |         -8.58333  | NEUTRAL  | Yahoo Finance |
| MPC        | 2026-11-17 00:00:00 |   395.61      |        -20.0833   | NEUTRAL  | Yahoo Finance |
| MRK        | 2026-11-17 00:00:00 |   143.37      |          8.58333  | NEUTRAL  | Yahoo Finance |
| MS         | 2026-11-17 00:00:00 |   183.53      |        -38.4167   | NEUTRAL  | Yahoo Finance |
| MSFT       | 2026-11-17 00:00:00 |   506.24      |        -27.3333   | NEUTRAL  | Yahoo Finance |
| NEAR-USD   | 2026-11-18 00:00:00 |     3.3846    |        -16.25     | NEUTRAL  | Kraken API    |
| NEM        | 2026-11-17 00:00:00 |   111.26      |        -32.0833   | NEUTRAL  | Yahoo Finance |
| ORCL       | 2026-11-17 00:00:00 |   115         |        -61.3333   | NEUTRAL  | Yahoo Finance |
| PFE        | 2026-11-17 00:00:00 |    28.47      |        -12.5      | NEUTRAL  | Yahoo Finance |
| PM         | 2026-11-17 00:00:00 |   194.38      |        -19.5      | NEUTRAL  | Yahoo Finance |
| QCOM       | 2026-11-17 00:00:00 |   166.67      |        -44.6667   | NEUTRAL  | Yahoo Finance |
| RENDER-USD | 2026-11-18 00:00:00 |     1.434     |        -45.25     | NEUTRAL  | Kraken API    |
| RTX        | 2026-11-17 00:00:00 |   198         |         21.0833   | NEUTRAL  | Yahoo Finance |
| SCHW       | 2026-11-17 00:00:00 |    91.84      |          5.41667  | NEUTRAL  | Yahoo Finance |
| SHY        | 2026-11-17 00:00:00 |    81.32      |        -55.75     | NEUTRAL  | Yahoo Finance |
| SNX-USD    | 2026-11-18 00:00:00 |     0.1533    |        -20.9167   | NEUTRAL  | Kraken API    |
| SPY        | 2026-11-17 00:00:00 |   732.44      |        -54        | NEUTRAL  | Yahoo Finance |
| T          | 2026-11-17 00:00:00 |    22.29      |         -0.916667 | NEUTRAL  | Yahoo Finance |
| TMO        | 2026-11-17 00:00:00 |   686.79      |         -3.83333  | NEUTRAL  | Yahoo Finance |
| TMUS       | 2026-11-17 00:00:00 |   167.9       |         21        | NEUTRAL  | Yahoo Finance |
| TSLA       | 2026-11-17 00:00:00 |   380.11      |        -12.8333   | NEUTRAL  | Yahoo Finance |
| TXN        | 2026-11-17 00:00:00 |   295.86      |        -12.8333   | NEUTRAL  | Yahoo Finance |
| UNH        | 2026-11-17 00:00:00 |   389.68      |        -15.0833   | NEUTRAL  | Yahoo Finance |
| VEA        | 2026-11-17 00:00:00 |    67.41      |        -63.75     | NEUTRAL  | Yahoo Finance |
| VTI        | 2026-11-17 00:00:00 |   360.19      |        -54        | NEUTRAL  | Yahoo Finance |
| VZ         | 2026-11-17 00:00:00 |    45.93      |         15.75     | NEUTRAL  | Yahoo Finance |
| WFC        | 2026-11-17 00:00:00 |    82.69      |         -8.83333  | NEUTRAL  | Yahoo Finance |
| XBI        | 2026-11-17 00:00:00 |   145.28      |        -24.75     | NEUTRAL  | Yahoo Finance |
| XLB        | 2026-11-17 00:00:00 |    50.84      |        -16.3333   | NEUTRAL  | Yahoo Finance |
| XLC        | 2026-11-17 00:00:00 |   105.26      |        -16.0833   | NEUTRAL  | Yahoo Finance |
| XLI        | 2026-11-17 00:00:00 |   164.75      |        -55.5      | NEUTRAL  | Yahoo Finance |
| XLY        | 2026-11-17 00:00:00 |   117.1       |         21.0833   | NEUTRAL  | Yahoo Finance |
| ZEC-USD    | 2026-11-18 00:00:00 |   955.74      |        -24.5833   | NEUTRAL  | Kraken API    |
| AAVE-USD   | 2026-11-18 00:00:00 |   110.7       |        -41.25     | SHORT    | Kraken API    |
| ADA-USD    | 2026-11-18 00:00:00 |     0.153922  |        -51.3333   | SHORT    | Kraken API    |
| AGG        | 2026-11-17 00:00:00 |    95.26      |        -47.25     | SHORT    | Yahoo Finance |
| ALGO-USD   | 2026-11-18 00:00:00 |     0.07914   |        -53.3333   | SHORT    | Kraken API    |
| AMAT       | 2026-11-17 00:00:00 |   349.23      |        -38.9167   | SHORT    | Yahoo Finance |
| APT-USD    | 2026-11-18 00:00:00 |     0.4431    |        -57.3333   | SHORT    | Kraken API    |
| ARKK       | 2026-11-17 00:00:00 |    70.84      |        -51.8333   | SHORT    | Yahoo Finance |
| BA         | 2026-11-17 00:00:00 |   163.91      |        -51.0833   | SHORT    | Yahoo Finance |
| BCH-USD    | 2026-11-18 00:00:00 |   208.37      |        -53.3333   | SHORT    | Kraken API    |
| BITO       | 2026-11-17 00:00:00 |     8.49      |        -50.0833   | SHORT    | Yahoo Finance |
| BND        | 2026-11-17 00:00:00 |    70.71      |        -47.25     | SHORT    | Yahoo Finance |
| BONK-USD   | 2026-11-18 00:00:00 |     2.38e-06  |        -51.3333   | SHORT    | Kraken API    |
| BTC-USD    | 2026-11-18 00:00:00 | 64646.1       |        -49.3333   | SHORT    | Kraken API    |
| CAT        | 2026-11-17 00:00:00 |   570.79      |        -50.0833   | SHORT    | Yahoo Finance |
| COMP-USD   | 2026-11-18 00:00:00 |    18.12      |        -31.5833   | SHORT    | Kraken API    |
| CRM        | 2026-11-17 00:00:00 |   194.52      |        -48.0833   | SHORT    | Yahoo Finance |
| CRV-USD    | 2026-11-18 00:00:00 |     0.2052    |        -43.3333   | SHORT    | Kraken API    |
| CSCO       | 2026-11-17 00:00:00 |    95.11      |        -57.4167   | SHORT    | Yahoo Finance |
| DASH-USD   | 2026-11-18 00:00:00 |    37.866     |        -57.3333   | SHORT    | Kraken API    |
| DBC        | 2026-11-17 00:00:00 |    30.19      |        -32.8333   | SHORT    | Yahoo Finance |
| DOGE-USD   | 2026-11-18 00:00:00 |     0.0594431 |        -51.3333   | SHORT    | Kraken API    |
| DOT-USD    | 2026-11-18 00:00:00 |     0.7315    |        -53.3333   | SHORT    | Kraken API    |
| EEM        | 2026-11-17 00:00:00 |    58.27      |        -52.0833   | SHORT    | Yahoo Finance |
| ETC-USD    | 2026-11-18 00:00:00 |     5.987     |        -51.3333   | SHORT    | Kraken API    |
| ETH-USD    | 2026-11-18 00:00:00 |  1811.99      |        -49.6667   | SHORT    | Kraken API    |
| EWJ        | 2026-11-17 00:00:00 |    88.69      |        -52.8333   | SHORT    | Yahoo Finance |
| FCX        | 2026-11-17 00:00:00 |    55.3       |        -61.4167   | SHORT    | Yahoo Finance |
| FET-USD    | 2026-11-18 00:00:00 |     0.1311    |        -35        | SHORT    | Kraken API    |
| FIL-USD    | 2026-11-18 00:00:00 |     0.602     |        -55.3333   | SHORT    | Kraken API    |
| GOOGL      | 2026-11-17 00:00:00 |   280.2       |        -43.5833   | SHORT    | Yahoo Finance |
| HYG        | 2026-11-17 00:00:00 |    76.63      |        -49.75     | SHORT    | Yahoo Finance |
| IBIT       | 2026-11-17 00:00:00 |    36.14      |        -50.0833   | SHORT    | Yahoo Finance |
| IEF        | 2026-11-17 00:00:00 |    90.41      |        -46.75     | SHORT    | Yahoo Finance |
| IEMG       | 2026-11-17 00:00:00 |    71.08      |        -52.0833   | SHORT    | Yahoo Finance |
| INTC       | 2026-11-17 00:00:00 |    55.17      |        -69.0833   | SHORT    | Yahoo Finance |
| LDO-USD    | 2026-11-18 00:00:00 |     0.275     |        -53.3333   | SHORT    | Kraken API    |
| LINK-USD   | 2026-11-18 00:00:00 |     9.24909   |        -49.6667   | SHORT    | Kraken API    |
| LRCX       | 2026-11-17 00:00:00 |   210.69      |        -42.9167   | SHORT    | Yahoo Finance |
| LTC-USD    | 2026-11-18 00:00:00 |    44.59      |        -53.3333   | SHORT    | Kraken API    |
| MU         | 2026-11-17 00:00:00 |   712.42      |        -51.8333   | SHORT    | Yahoo Finance |
| NFLX       | 2026-11-17 00:00:00 |    59.68      |        -39.5833   | SHORT    | Yahoo Finance |
| NKE        | 2026-11-17 00:00:00 |    35.85      |        -30.8333   | SHORT    | Yahoo Finance |
| NOW        | 2026-11-17 00:00:00 |    92.9       |        -52.0833   | SHORT    | Yahoo Finance |
| NVDA       | 2026-11-17 00:00:00 |   155.46      |        -66.8333   | SHORT    | Yahoo Finance |
| OP-USD     | 2026-11-18 00:00:00 |     0.0775    |        -57.3333   | SHORT    | Kraken API    |
| OXY        | 2026-11-17 00:00:00 |    56.52      |        -35.3333   | SHORT    | Yahoo Finance |
| PEPE-USD   | 2026-11-18 00:00:00 |     3.768e-06 |        -57.3333   | SHORT    | Kraken API    |
| POL-USD    | 2026-11-18 00:00:00 |     0.08145   |        -51.3333   | SHORT    | Kraken API    |
| QQQ        | 2026-11-17 00:00:00 |   656.95      |        -39.3333   | SHORT    | Yahoo Finance |
| SHIB-USD   | 2026-11-18 00:00:00 |     3.85e-06  |        -51.3333   | SHORT    | Kraken API    |
| SKY-USD    | 2026-11-18 00:00:00 |     0.05231   |        -53.3333   | SHORT    | Kraken API    |
| SLB        | 2026-11-17 00:00:00 |    48.95      |        -57.0833   | SHORT    | Yahoo Finance |
| SLV        | 2026-11-17 00:00:00 |    42.64      |        -49.5833   | SHORT    | Yahoo Finance |
| SMH        | 2026-11-17 00:00:00 |   460.1       |        -65.0833   | SHORT    | Yahoo Finance |
| SOL-USD    | 2026-11-18 00:00:00 |    74.8       |        -49.6667   | SHORT    | Kraken API    |
| SOXX       | 2026-11-17 00:00:00 |   141.46      |        -61.75     | SHORT    | Yahoo Finance |
| SUSHI-USD  | 2026-11-18 00:00:00 |     0.1545    |        -51.6667   | SHORT    | Kraken API    |
| TIA-USD    | 2026-11-18 00:00:00 |     0.3538    |        -49        | SHORT    | Kraken API    |
| TLT        | 2026-11-17 00:00:00 |    79.55      |        -47.25     | SHORT    | Yahoo Finance |
| TRX-USD    | 2026-11-18 00:00:00 |     0.309147  |        -52.6667   | SHORT    | Kraken API    |
| UNI-USD    | 2026-11-18 00:00:00 |     5.2068    |        -57.3333   | SHORT    | Kraken API    |
| USO        | 2026-11-17 00:00:00 |   140.24      |        -40.5833   | SHORT    | Yahoo Finance |
| VWO        | 2026-11-17 00:00:00 |    54.3       |        -48.75     | SHORT    | Yahoo Finance |
| WIF-USD    | 2026-11-18 00:00:00 |     0.1347    |        -53.6667   | SHORT    | Kraken API    |
| XLE        | 2026-11-17 00:00:00 |    63.36      |        -31.5      | SHORT    | Yahoo Finance |
| XLK        | 2026-11-17 00:00:00 |   163.26      |        -44.3333   | SHORT    | Yahoo Finance |
| XLM-USD    | 2026-11-18 00:00:00 |     0.141288  |        -36.3333   | SHORT    | Kraken API    |
| XOM        | 2026-11-17 00:00:00 |   167.21      |        -31.5      | SHORT    | Yahoo Finance |
| XRP-USD    | 2026-11-18 00:00:00 |     0.98799   |        -49.6667   | SHORT    | Kraken API    |
| YFI-USD    | 2026-11-18 00:00:00 |  1758.7       |        -48        | SHORT    | Kraken API    |

## Edge Summary

- Symbols with trades: **161** of 161
- Beat buy-and-hold: **37.27%** of traded symbols
- Positive return: **31.68%** of traded symbols
- Median strategy return: **-7.16%** (benchmark **15.10%**)
- Median excess vs benchmark: **-19.92%**
- Median Sharpe: **-0.05**
- Median exposure: **44.43%**

> Edge is real only if both _beat buy-and-hold_ and _median excess_ are convincingly positive across many symbols. Treat a single high-return symbol as noise.

## Portfolio Backtest

Actual capital-allocation books (not per-symbol averages). Benchmarks: `equal_weight_buyhold` (whole tracked universe), `spy_buyhold` (100% SPY), and `sixty_forty` (60% SPY / 40% AGG). `high_conf_voltarget` inverse-vol-weights the HIGH-confidence book; `conviction_long_short` is market-neutral. Judge on **Sharpe** and **max_drawdown** out-of-sample, not raw return: a fully-invested long book wins on return in a bull market but carries all the risk.

| strategy              | scope         | ann_return   | ann_vol   |   sharpe | max_drawdown   | total_return   |   avg_gross_exposure |
|:----------------------|:--------------|:-------------|:----------|---------:|:---------------|:---------------|---------------------:|
| equal_weight_buyhold  | full          | 4.64%        | 28.46%    |     0.16 | -39.53%        | 1.82%          |                 1    |
| equal_weight_buyhold  | out_of_sample | 19.86%       | 26.32%    |     0.75 | -20.82%        | 19.07%         |                 1    |
| all_signals_ew        | full          | -11.30%      | 24.30%    |    -0.46 | -52.23%        | -35.17%        |                 1    |
| all_signals_ew        | out_of_sample | -9.51%       | 21.65%    |    -0.44 | -22.91%        | -11.84%        |                 1    |
| high_conf_ew          | full          | -9.81%       | 29.94%    |    -0.33 | -47.57%        | -35.18%        |                 0.89 |
| high_conf_ew          | out_of_sample | 2.22%        | 24.85%    |     0.09 | -27.67%        | -0.91%         |                 0.89 |
| high_conf_voltarget   | full          | -10.87%      | 26.69%    |    -0.41 | -42.08%        | -35.44%        |                 0.89 |
| high_conf_voltarget   | out_of_sample | -0.85%       | 19.94%    |    -0.04 | -23.51%        | -2.99%         |                 0.89 |
| conviction_long_short | full          | -15.30%      | 22.10%    |    -0.69 | -52.36%        | -41.72%        |                 0.96 |
| conviction_long_short | out_of_sample | -11.22%      | 17.08%    |    -0.66 | -23.15%        | -12.61%        |                 0.96 |
| spy_buyhold           | full          | 2.17%        | 14.01%    |     0.16 | -19.00%        | 3.71%          |                 0.79 |
| spy_buyhold           | out_of_sample | -4.84%       | 10.93%    |    -0.44 | -11.45%        | -5.62%         |                 0.79 |
| sixty_forty           | full          | 0.71%        | 8.79%     |     0.08 | -11.86%        | 0.99%          |                 0.79 |
| sixty_forty           | out_of_sample | -5.29%       | 7.22%     |    -0.73 | -8.19%         | -5.73%         |                 0.79 |

## Walk-Forward Robustness

Each book measured across contiguous time folds (each a different regime). A book has durable edge only if `mean_sharpe` is positive, `min_sharpe` isn't deeply negative, and `pct_positive_folds` is high — a single great fold doesn't count. `fold_sharpes` lists each fold oldest-to-newest.

| strategy              |   n_folds |   mean_sharpe |   median_sharpe |   min_sharpe | pct_positive_folds   | mean_return   | fold_sharpes                 |
|:----------------------|----------:|--------------:|----------------:|-------------:|:---------------------|:--------------|:-----------------------------|
| equal_weight_buyhold  |         5 |          0.36 |            0.2  |        -0.62 | 60.00%               | 1.34%         | 1.34;1.34;-0.45;-0.62;0.20   |
| all_signals_ew        |         5 |         -0.48 |           -0.35 |        -2.05 | 20.00%               | -6.80%        | -1.08;-0.35;-2.05;1.12;-0.06 |
| high_conf_ew          |         5 |         -0.2  |           -0.43 |        -1.89 | 40.00%               | -6.54%        | 0.89;-1.89;-0.43;1.29;-0.87  |
| high_conf_voltarget   |         5 |         -0.34 |           -0.28 |        -2.1  | 40.00%               | -7.36%        | 0.98;-2.10;-0.28;0.77;-1.09  |
| conviction_long_short |         5 |         -0.67 |           -0.23 |        -1.93 | 20.00%               | -9.74%        | -1.93;-0.23;-1.16;0.04;-0.05 |
| spy_buyhold           |         5 |          0.06 |            0.14 |        -0.99 | 60.00%               | 0.88%         | 1.30;0.14;-0.35;0.20;-0.99   |
| sixty_forty           |         5 |         -0.02 |           -0    |        -1.25 | 40.00%               | 0.27%         | 1.24;0.12;-0.23;-0.00;-1.25  |

## Strategy Comparison

Each decision rule backtested over the same data. `out_of_sample` is the most recent ~35% of each symbol's history (unseen tail). A rule has real edge only if `median_excess` and `beat_benchmark_pct` stay positive out-of-sample, not just full-sample.

| strategy        | scope         |   symbols | beat_benchmark_pct   | positive_pct   | median_return   | median_benchmark   | median_excess   |   median_sharpe |   total_trades |
|:----------------|:--------------|----------:|:---------------------|:---------------|:----------------|:-------------------|:----------------|----------------:|---------------:|
| trend           | full          |       161 | 37.27%               | 31.68%         | -7.16%          | 15.10%             | -19.92%         |           -0.05 |          11349 |
| trend           | out_of_sample |       161 | 48.45%               | 53.42%         | 0.90%           | -1.79%             | -0.93%          |            0.17 |           3876 |
| mean_reversion  | full          |       159 | 40.88%               | 46.54%         | -0.16%          | 15.10%             | -13.89%         |           -0.02 |           1294 |
| mean_reversion  | out_of_sample |       131 | 55.73%               | 59.54%         | 0.43%           | -3.91%             | 2.84%           |            0.54 |            446 |
| regime_adaptive | full          |       161 | 36.65%               | 29.81%         | -8.05%          | 15.10%             | -20.07%         |           -0.04 |          11615 |
| regime_adaptive | out_of_sample |       161 | 47.83%               | 53.42%         | 0.73%           | -1.79%             | -0.59%          |            0.16 |           3979 |

## Signal Calibration

Realized forward return in the signal's direction, grouped by confidence. HIGH should outrank LOW for the confidence score to be meaningful.

| confidence_level   |   horizon |     n | mean_return   | median_return   | win_rate   |
|:-------------------|----------:|------:|:--------------|:----------------|:-----------|
| HIGH               |         5 |  7817 | 0.19%         | 0.07%           | 51.18%     |
| MEDIUM             |         5 | 29348 | 0.13%         | 0.08%           | 50.90%     |
| LOW                |         5 |  3683 | -0.21%        | -0.25%          | 47.57%     |
| ALL                |         5 | 40848 | 0.11%         | 0.05%           | 50.65%     |
| HIGH               |        10 |  7709 | 0.45%         | 0.08%           | 50.97%     |
| MEDIUM             |        10 | 29018 | 0.24%         | 0.08%           | 50.60%     |
| LOW                |        10 |  3649 | -0.38%        | -0.22%          | 48.31%     |
| ALL                |        10 | 40376 | 0.22%         | 0.06%           | 50.47%     |
| HIGH               |        20 |  7555 | 0.94%         | 0.20%           | 51.61%     |
| MEDIUM             |        20 | 28376 | 0.74%         | 0.46%           | 52.56%     |
| LOW                |        20 |  3568 | -0.17%        | -0.39%          | 48.12%     |
| ALL                |        20 | 39499 | 0.70%         | 0.34%           | 51.98%     |

## Backtest Summary

### Data Quality / Signal Availability

- **ok**: 161 symbols

| symbol     |   trades | return   | benchmark_return   | mdd     |   sharpe | exposure   | skipped_reason   |
|:-----------|---------:|:---------|:-------------------|:--------|---------:|:-----------|:-----------------|
| AAPL       |       67 | -7.89%   | 64.37%             | -20.65% |    -0.06 | 47.75%     | ok               |
| AAVE-USD   |       69 | -46.29%  | -59.67%            | -64.31% |    -0.38 | 39.66%     | ok               |
| ABBV       |       68 | -15.51%  | 73.28%             | -30.52% |    -0.28 | 49.92%     | ok               |
| ADA-USD    |       74 | -15.47%  | -75.69%            | -52.70% |     0.05 | 50.00%     | ok               |
| ADBE       |       74 | -0.23%   | -56.92%            | -31.20% |     0.14 | 54.24%     | ok               |
| AGG        |       65 | -6.54%   | -2.35%             | -10.74% |    -1    | 34.61%     | ok               |
| ALGO-USD   |       80 | -25.93%  | -55.16%            | -46.91% |    -0.11 | 42.53%     | ok               |
| AMAT       |       73 | -31.48%  | 50.19%             | -53.91% |    -0.2  | 51.41%     | ok               |
| AMD        |       54 | 23.48%   | 215.68%            | -38.64% |     0.42 | 36.44%     | ok               |
| AMGN       |       63 | -5.31%   | 45.98%             | -34.19% |    -0.02 | 53.58%     | ok               |
| AMZN       |       84 | -58.73%  | 30.35%             | -59.16% |    -1.73 | 41.60%     | ok               |
| APT-USD    |       76 | -21.88%  | -90.23%            | -56.73% |     0.02 | 40.61%     | ok               |
| ARB-USD    |       75 | 0.46%    | -60.10%            | -42.38% |     0.28 | 42.53%     | ok               |
| ARKK       |       85 | -22.96%  | 60.96%             | -35.78% |    -0.28 | 44.43%     | ok               |
| ATOM-USD   |       80 | -56.33%  | -67.98%            | -61.74% |    -0.82 | 45.98%     | ok               |
| AVAX-USD   |       66 | -35.36%  | -62.44%            | -46.76% |    -0.29 | 41.00%     | ok               |
| AVGO       |       68 | -6.34%   | 115.30%            | -44.82% |     0.09 | 39.77%     | ok               |
| BA         |       65 | 19.49%   | -10.19%            | -24.47% |     0.42 | 52.91%     | ok               |
| BAC        |       78 | -7.42%   | 25.96%             | -23.14% |    -0.12 | 49.08%     | ok               |
| BCH-USD    |       82 | -6.45%   | -54.76%            | -54.04% |     0.14 | 48.85%     | ok               |
| BITO       |       83 | -10.24%  | -63.23%            | -43.13% |     0.04 | 41.76%     | ok               |
| BLK        |       79 | -7.82%   | 51.15%             | -26.90% |    -0.13 | 47.25%     | ok               |
| BND        |       68 | -6.75%   | -2.32%             | -10.80% |    -1.02 | 35.61%     | ok               |
| BONK-USD   |       70 | 44.17%   | -84.18%            | -53.62% |     0.59 | 45.21%     | ok               |
| BTC-USD    |       79 | 2.15%    | -38.77%            | -25.52% |     0.17 | 52.49%     | ok               |
| C          |       81 | -35.42%  | 94.87%             | -39.84% |    -0.77 | 46.92%     | ok               |
| CAT        |       70 | 32.76%   | 74.31%             | -21.87% |     0.57 | 51.75%     | ok               |
| CL         |       60 | 7.06%    | 1.47%              | -14.32% |     0.28 | 40.27%     | ok               |
| CMCSA      |       82 | -33.95%  | -29.45%            | -45.88% |    -0.79 | 44.26%     | ok               |
| COMP-USD   |       95 | -42.71%  | -65.66%            | -52.17% |    -0.33 | 48.47%     | ok               |
| COP        |       66 | -15.39%  | 22.38%             | -38.80% |    -0.19 | 43.76%     | ok               |
| COST       |       60 | 6.41%    | 30.50%             | -31.32% |     0.26 | 41.10%     | ok               |
| CRM        |       69 | -22.44%  | -23.07%            | -39.41% |    -0.24 | 46.42%     | ok               |
| CRV-USD    |       62 | 67.35%   | -65.52%            | -39.89% |     0.74 | 38.12%     | ok               |
| CSCO       |       67 | 2.19%    | 100.44%            | -28.16% |     0.16 | 52.08%     | ok               |
| CVX        |       69 | -13.66%  | 38.26%             | -26.75% |    -0.28 | 43.59%     | ok               |
| DASH-USD   |       59 | -18.64%  | 88.21%             | -64.43% |     0.26 | 30.46%     | ok               |
| DBC        |       70 | -11.66%  | 29.40%             | -24.10% |    -0.33 | 36.27%     | ok               |
| DE         |       72 | -6.90%   | 72.31%             | -21.16% |    -0.05 | 44.43%     | ok               |
| DIA        |       72 | -9.51%   | 29.56%             | -16.20% |    -0.48 | 43.93%     | ok               |
| DIS        |       62 | -0.96%   | 14.46%             | -27.81% |     0.08 | 46.92%     | ok               |
| DOGE-USD   |       68 | -10.85%  | -66.13%            | -61.52% |     0.1  | 47.70%     | ok               |
| DOT-USD    |       76 | -54.66%  | -80.85%            | -67.54% |    -0.55 | 41.76%     | ok               |
| DXY-INDEX  |       40 | -0.56%   | -4.05%             | -5.13%  |    -0.08 | 30.52%     | ok               |
| EEM        |       68 | -6.33%   | 37.07%             | -24.14% |    -0.12 | 42.10%     | ok               |
| EFA        |       64 | -11.02%  | 29.54%             | -13.32% |    -0.45 | 38.77%     | ok               |
| EOG        |       76 | -28.34%  | 24.38%             | -47.65% |    -0.58 | 44.26%     | ok               |
| ETC-USD    |       56 | 2.33%    | -64.06%            | -46.79% |     0.21 | 36.59%     | ok               |
| ETH-USD    |       63 | 135.47%  | -28.86%            | -30.11% |     1.24 | 48.08%     | ok               |
| EWJ        |       70 | -24.95%  | 31.10%             | -29.40% |    -0.85 | 38.27%     | ok               |
| FCX        |       67 | -19.70%  | 14.45%             | -46.84% |    -0.13 | 46.09%     | ok               |
| FET-USD    |       77 | -43.60%  | -81.22%            | -66.52% |    -0.24 | 44.06%     | ok               |
| FIL-USD    |       67 | -8.40%   | -75.10%            | -58.54% |     0.14 | 39.66%     | ok               |
| FXI        |       46 | -4.25%   | 27.00%             | -23.91% |    -0.02 | 30.45%     | ok               |
| GDX        |       68 | -6.36%   | 132.46%            | -34.29% |     0.04 | 45.09%     | ok               |
| GDXJ       |       70 | -30.10%  | 126.04%            | -36.01% |    -0.32 | 44.43%     | ok               |
| GE         |       80 | -14.33%  | 103.36%            | -27.82% |    -0.16 | 48.92%     | ok               |
| GLD        |       52 | 11.67%   | 63.95%             | -14.15% |     0.35 | 46.09%     | ok               |
| GOOGL      |       57 | 78.50%   | 51.12%             | -16.84% |     1.17 | 49.42%     | ok               |
| GRT-USD    |       71 | 74.85%   | -79.89%            | -38.70% |     0.8  | 47.32%     | ok               |
| GS         |       68 | -2.77%   | 96.77%             | -21.94% |     0.04 | 47.42%     | ok               |
| HBAR-USD   |       42 | -23.19%  | -44.31%            | -56.47% |    -0.25 | 42.28%     | ok               |
| HD         |       69 | 7.26%    | -0.73%             | -17.15% |     0.26 | 44.93%     | ok               |
| HON        |       89 | -28.80%  | 3.33%              | -32.97% |    -0.74 | 52.41%     | ok               |
| HYG        |       91 | -7.28%   | -0.91%             | -10.59% |    -0.81 | 39.27%     | ok               |
| IBIT       |       46 | 51.81%   | -4.92%             | -18.95% |     0.82 | 35.98%     | ok               |
| IBM        |       71 | -20.31%  | 35.26%             | -48.94% |    -0.2  | 50.58%     | ok               |
| ICP-USD    |       74 | 3.73%    | -58.15%            | -43.17% |     0.3  | 40.42%     | ok               |
| IEF        |       78 | -9.89%   | -3.97%             | -12.21% |    -1.3  | 35.27%     | ok               |
| IEMG       |       64 | -3.15%   | 33.11%             | -24.73% |    -0.03 | 41.93%     | ok               |
| INJ-USD    |       55 | -12.40%  | -35.80%            | -61.35% |     0.13 | 38.70%     | ok               |
| INTC       |       72 | 65.65%   | 80.35%             | -60.60% |     0.66 | 50.08%     | ok               |
| INTU       |       73 | -8.33%   | -50.76%            | -37.18% |     0.01 | 47.42%     | ok               |
| ITA        |       72 | 0.52%    | 57.26%             | -22.33% |     0.09 | 47.09%     | ok               |
| IWM        |       56 | 10.39%   | 33.15%             | -8.62%  |     0.42 | 34.44%     | ok               |
| JNJ        |       60 | 13.37%   | 91.15%             | -17.51% |     0.5  | 47.75%     | ok               |
| JPM        |       77 | -28.79%  | 65.67%             | -32.74% |    -0.85 | 44.93%     | ok               |
| KO         |       54 | 28.92%   | 54.58%             | -8.64%  |     0.96 | 39.77%     | ok               |
| LDO-USD    |       68 | 94.63%   | -66.26%            | -47.94% |     0.85 | 48.28%     | ok               |
| LIN        |       70 | -5.06%   | 17.01%             | -20.61% |    -0.11 | 42.26%     | ok               |
| LINK-USD   |       72 | 34.06%   | -30.45%            | -35.01% |     0.54 | 43.10%     | ok               |
| LLY        |       82 | -33.00%  | 55.72%             | -53.34% |    -0.5  | 49.75%     | ok               |
| LRCX       |       86 | -23.67%  | 99.55%             | -61.08% |    -0.08 | 45.26%     | ok               |
| LTC-USD    |       67 | 32.55%   | -48.35%            | -30.78% |     0.55 | 51.15%     | ok               |
| MCD        |       77 | 7.75%    | 6.84%              | -22.20% |     0.32 | 41.10%     | ok               |
| META       |       72 | -34.31%  | 19.11%             | -44.90% |    -0.53 | 49.92%     | ok               |
| MPC        |       70 | 11.57%   | 128.80%            | -33.74% |     0.31 | 53.41%     | ok               |
| MRK        |       67 | -24.79%  | 10.44%             | -35.95% |    -0.48 | 43.59%     | ok               |
| MS         |       73 | -4.92%   | 91.64%             | -27.79% |    -0.03 | 47.42%     | ok               |
| MSFT       |       81 | -27.63%  | 11.79%             | -38.06% |    -0.61 | 50.58%     | ok               |
| MU         |       55 | 85.07%   | 438.77%            | -64.76% |     0.77 | 49.42%     | ok               |
| NEAR-USD   |       65 | 177.42%  | 51.91%             | -46.60% |     1.13 | 43.49%     | ok               |
| NEM        |       70 | -25.86%  | 165.92%            | -39.56% |    -0.25 | 49.75%     | ok               |
| NFLX       |       84 | -6.76%   | -12.79%            | -27.17% |    -0.04 | 50.58%     | ok               |
| NKE        |       87 | -33.77%  | -61.94%            | -55.35% |    -0.42 | 47.42%     | ok               |
| NOW        |       79 | -5.75%   | -40.00%            | -42.66% |     0.15 | 51.75%     | ok               |
| NVDA       |       82 | -36.11%  | 20.17%             | -50.87% |    -0.44 | 55.79%     | ok               |
| OP-USD     |       72 | -16.12%  | -86.94%            | -57.66% |     0.06 | 36.02%     | ok               |
| ORCL       |       60 | 61.25%   | -17.96%            | -31.06% |     0.67 | 50.08%     | ok               |
| OXY        |       67 | 3.84%    | -9.84%             | -28.48% |     0.19 | 43.43%     | ok               |
| PEP        |       70 | 3.12%    | -14.58%            | -21.35% |     0.16 | 45.92%     | ok               |
| PEPE-USD   |       74 | -31.09%  | -66.10%            | -60.19% |    -0.04 | 47.13%     | ok               |
| PFE        |       79 | -33.58%  | 2.41%              | -42.77% |    -1.02 | 37.60%     | ok               |
| PG         |       60 | -16.08%  | 3.06%              | -24.25% |    -0.53 | 37.10%     | ok               |
| PM         |       77 | -6.67%   | 91.38%             | -38.30% |    -0.06 | 47.59%     | ok               |
| POL-USD    |       85 | -0.25%   | -59.05%            | -46.25% |     0.21 | 49.23%     | ok               |
| QCOM       |       77 | -35.78%  | -14.59%            | -50.90% |    -0.37 | 40.10%     | ok               |
| QQQ        |       72 | -3.64%   | 36.41%             | -15.84% |    -0.02 | 43.26%     | ok               |
| RENDER-USD |       86 | -43.34%  | -58.60%            | -54.95% |    -0.26 | 46.93%     | ok               |
| RTX        |       73 | 16.35%   | 96.78%             | -16.99% |     0.43 | 52.91%     | ok               |
| SBUX       |       66 | -8.91%   | 35.65%             | -29.22% |    -0.09 | 40.60%     | ok               |
| SCHW       |       84 | -16.47%  | 24.85%             | -31.92% |    -0.34 | 48.09%     | ok               |
| SHIB-USD   |       79 | -29.64%  | -68.02%            | -52.76% |    -0.24 | 52.11%     | ok               |
| SHY        |       56 | -2.37%   | -0.39%             | -3.30%  |    -0.76 | 39.10%     | ok               |
| SKY-USD    |       85 | -50.34%  | -40.83%            | -63.39% |    -0.66 | 45.98%     | ok               |
| SLB        |       75 | -40.86%  | 4.13%              | -54.38% |    -0.8  | 48.25%     | ok               |
| SLV        |       66 | 41.29%   | 61.21%             | -37.05% |     0.61 | 42.26%     | ok               |
| SMH        |       50 | 60.66%   | 77.74%             | -33.66% |     0.88 | 41.93%     | ok               |
| SNX-USD    |       62 | -7.27%   | -74.91%            | -50.74% |     0.13 | 36.97%     | ok               |
| SOL-USD    |       73 | 11.83%   | -51.08%            | -44.96% |     0.35 | 58.81%     | ok               |
| SOXX       |       58 | 63.12%   | 73.81%             | -40.14% |     0.85 | 41.10%     | ok               |
| SPY        |       63 | -5.56%   | 34.06%             | -15.53% |    -0.13 | 47.09%     | ok               |
| SUSHI-USD  |       89 | -59.52%  | -75.14%            | -78.98% |    -0.65 | 44.25%     | ok               |
| T          |       68 | 52.21%   | 18.88%             | -17.01% |     0.94 | 57.57%     | ok               |
| TGT        |       60 | -10.00%  | 8.73%              | -32.83% |    -0.14 | 37.60%     | ok               |
| TIA-USD    |       85 | -43.74%  | -79.87%            | -74.75% |    -0.18 | 44.25%     | ok               |
| TLT        |       68 | -20.81%  | -14.94%            | -22.01% |    -1.57 | 34.78%     | ok               |
| TMO        |       67 | 38.81%   | 24.69%             | -18.85% |     0.74 | 56.41%     | ok               |
| TMUS       |       74 | -7.16%   | -5.37%             | -33.05% |    -0.06 | 46.09%     | ok               |
| TRX-USD    |       60 | 11.17%   | 12.79%             | -22.90% |     0.4  | 48.85%     | ok               |
| TSLA       |       74 | -35.79%  | 92.54%             | -58.36% |    -0.24 | 41.93%     | ok               |
| TXN        |       83 | -30.18%  | 52.95%             | -46.56% |    -0.35 | 48.75%     | ok               |
| UNH        |       75 | 38.77%   | -19.89%            | -26.31% |     0.61 | 48.42%     | ok               |
| UNI-USD    |       80 | 5.39%    | -27.35%            | -60.31% |     0.33 | 49.81%     | ok               |
| UPS        |       71 | -35.53%  | -18.79%            | -41.37% |    -0.67 | 44.09%     | ok               |
| USO        |       68 | -12.93%  | 75.48%             | -42.74% |    -0.05 | 33.78%     | ok               |
| VEA        |       64 | -7.02%   | 36.51%             | -18.84% |    -0.25 | 41.26%     | ok               |
| VIXY       |       98 | -84.50%  | -50.82%            | -91.45% |    -1.18 | 31.78%     | ok               |
| VNQ        |       71 | -12.05%  | 12.79%             | -24.92% |    -0.45 | 40.43%     | ok               |
| VTI        |       67 | -12.25%  | 33.71%             | -17.64% |    -0.39 | 47.09%     | ok               |
| VWO        |       80 | -15.13%  | 24.40%             | -25.20% |    -0.52 | 41.76%     | ok               |
| VZ         |       86 | -27.73%  | 12.52%             | -31.67% |    -0.84 | 43.26%     | ok               |
| WFC        |       80 | -19.98%  | 44.01%             | -30.92% |    -0.35 | 46.76%     | ok               |
| WIF-USD    |       66 | 1.52%    | -84.17%            | -52.76% |     0.29 | 43.87%     | ok               |
| WMT        |       69 | 7.65%    | 87.86%             | -25.96% |     0.27 | 48.42%     | ok               |
| XBI        |       60 | 0.63%    | 56.45%             | -17.66% |     0.1  | 37.77%     | ok               |
| XLB        |       64 | -11.32%  | 15.10%             | -24.18% |    -0.36 | 34.78%     | ok               |
| XLC        |       61 | 3.14%    | 21.76%             | -12.33% |     0.17 | 48.75%     | ok               |
| XLE        |       72 | -8.02%   | 39.56%             | -34.77% |    -0.13 | 47.59%     | ok               |
| XLF        |       78 | -4.07%   | 39.30%             | -23.61% |    -0.08 | 49.58%     | ok               |
| XLI        |       82 | -9.35%   | 35.24%             | -18.27% |    -0.32 | 42.76%     | ok               |
| XLK        |       44 | 35.21%   | 44.25%             | -19.09% |     0.76 | 43.93%     | ok               |
| XLM-USD    |       77 | -0.05%   | -45.42%            | -56.32% |     0.22 | 49.62%     | ok               |
| XLP        |       63 | 15.02%   | 18.90%             | -8.96%  |     0.73 | 41.10%     | ok               |
| XLU        |       69 | -0.87%   | 26.02%             | -20.40% |     0.01 | 41.10%     | ok               |
| XLV        |       74 | -19.21%  | 26.99%             | -22.82% |    -0.85 | 37.77%     | ok               |
| XLY        |       77 | -6.72%   | 26.97%             | -18.44% |    -0.13 | 47.75%     | ok               |
| XOM        |       59 | -1.09%   | 45.53%             | -20.29% |     0.05 | 36.61%     | ok               |
| XRP-USD    |       74 | 4.21%    | -54.40%            | -32.16% |     0.24 | 36.78%     | ok               |
| YFI-USD    |       74 | -48.97%  | -65.28%            | -58.28% |    -0.7  | 40.61%     | ok               |
| ZEC-USD    |       54 | 126.43%  | 2104.20%           | -56.50% |     0.87 | 36.97%     | ok               |

## AAPL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -2.13%   | 64.37%             | -21.71% |     0.07 |       76 | 52.58%     | ok               |
|          15 | -6.46%   | 64.37%             | -23.86% |    -0.01 |       85 | 60.07%     | ok               |
|          30 | -7.89%   | 64.37%             | -20.65% |    -0.06 |       67 | 47.75%     | ok               |
|          35 | -9.21%   | 64.37%             | -22.04% |    -0.09 |       67 | 46.42%     | ok               |
|          25 | -11.62%  | 64.37%             | -22.37% |    -0.14 |       77 | 49.92%     | ok               |

## AAVE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -7.29%   | -59.67%            | -43.61% |     0.14 |       45 | 34.10%     | ok               |
|          50 | -11.92%  | -59.67%            | -45.47% |     0.03 |       42 | 21.84%     | ok               |
|          35 | -18.24%  | -59.67%            | -48.79% |     0.01 |       55 | 37.55%     | ok               |
|          45 | -18.57%  | -59.67%            | -49.19% |    -0.03 |       50 | 28.74%     | ok               |
|          15 | -40.26%  | -59.67%            | -59.76% |    -0.17 |       80 | 54.02%     | ok               |

## ABBV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -6.70%   | 73.28%             | -27.91% |    -0.08 |       54 | 37.77%     | ok               |
|          20 | -12.19%  | 73.28%             | -28.73% |    -0.18 |       64 | 53.24%     | ok               |
|          25 | -12.30%  | 73.28%             | -30.04% |    -0.19 |       67 | 51.75%     | ok               |
|          30 | -15.51%  | 73.28%             | -30.52% |    -0.28 |       68 | 49.92%     | ok               |
|          40 | -15.56%  | 73.28%             | -27.36% |    -0.31 |       70 | 42.93%     | ok               |

## ADA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 2.88%    | -75.69%            | -47.22% |     0.3  |       67 | 64.56%     | ok               |
|          35 | -1.16%   | -75.69%            | -44.07% |     0.21 |       64 | 44.06%     | ok               |
|          50 | -2.31%   | -75.69%            | -32.89% |     0.14 |       50 | 24.90%     | ok               |
|          40 | -6.34%   | -75.69%            | -41.68% |     0.13 |       58 | 39.46%     | ok               |
|          20 | -17.38%  | -75.69%            | -53.45% |     0.09 |       83 | 58.81%     | ok               |

## ADBE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 17.20%   | -56.92%            | -29.07% |     0.38 |       57 | 58.74%     | ok               |
|          20 | 1.01%    | -56.92%            | -31.52% |     0.16 |       65 | 62.06%     | ok               |
|          30 | -0.23%   | -56.92%            | -31.20% |     0.14 |       74 | 54.24%     | ok               |
|          15 | -6.27%   | -56.92%            | -34.98% |     0.06 |       65 | 64.56%     | ok               |
|          35 | -6.24%   | -56.92%            | -32.89% |     0.02 |       77 | 45.76%     | ok               |

## AGG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -6.54%   | -2.35%             | -10.74% |    -1    |       65 | 34.61%     | ok               |
|          45 | -6.08%   | -2.35%             | -9.39%  |    -1.12 |       60 | 23.96%     | ok               |
|          20 | -8.40%   | -2.35%             | -11.89% |    -1.18 |       70 | 40.27%     | ok               |
|          25 | -8.16%   | -2.35%             | -12.28% |    -1.19 |       71 | 38.10%     | ok               |
|          35 | -7.81%   | -2.35%             | -11.53% |    -1.25 |       66 | 31.28%     | ok               |

## ALGO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -22.17%  | -55.16%            | -51.07% |    -0.04 |       84 | 46.93%     | ok               |
|          30 | -25.93%  | -55.16%            | -46.91% |    -0.11 |       80 | 42.53%     | ok               |
|          15 | -37.11%  | -55.16%            | -54.92% |    -0.22 |       82 | 53.45%     | ok               |
|          20 | -39.98%  | -55.16%            | -56.98% |    -0.29 |       83 | 49.81%     | ok               |
|          35 | -42.43%  | -55.16%            | -52.80% |    -0.47 |       68 | 36.97%     | ok               |

## AMAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -30.52%  | 50.19%             | -53.90% |    -0.15 |       76 | 60.40%     | ok               |
|          30 | -31.48%  | 50.19%             | -53.91% |    -0.2  |       73 | 51.41%     | ok               |
|          50 | -30.37%  | 50.19%             | -44.88% |    -0.24 |       50 | 35.77%     | ok               |
|          35 | -33.03%  | 50.19%             | -51.27% |    -0.24 |       73 | 48.75%     | ok               |
|          25 | -41.19%  | 50.19%             | -56.61% |    -0.35 |       75 | 54.08%     | ok               |

## AMD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 39.99%   | 215.68%            | -37.12% |     0.56 |       52 | 31.61%     | ok               |
|          40 | 23.48%   | 215.68%            | -38.64% |     0.42 |       54 | 36.44%     | ok               |
|          35 | 13.24%   | 215.68%            | -40.22% |     0.34 |       62 | 37.94%     | ok               |
|          45 | 11.74%   | 215.68%            | -42.84% |     0.32 |       58 | 34.44%     | ok               |
|          30 | -3.80%   | 215.68%            | -47.20% |     0.19 |       65 | 40.60%     | ok               |

## AMGN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -0.31%   | 45.98%             | -26.65% |     0.1  |       62 | 58.90%     | ok               |
|          35 | -2.92%   | 45.98%             | -31.29% |     0.03 |       65 | 50.25%     | ok               |
|          30 | -5.31%   | 45.98%             | -34.19% |    -0.02 |       63 | 53.58%     | ok               |
|          15 | -7.69%   | 45.98%             | -27.98% |    -0.05 |       61 | 62.90%     | ok               |
|          25 | -7.25%   | 45.98%             | -33.47% |    -0.06 |       59 | 55.74%     | ok               |

## AMZN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -33.87%  | 30.35%             | -34.72% |    -1.06 |       62 | 30.45%     | ok               |
|          50 | -34.90%  | 30.35%             | -35.58% |    -1.27 |       52 | 22.96%     | ok               |
|          45 | -41.25%  | 30.35%             | -41.87% |    -1.49 |       62 | 26.79%     | ok               |
|          35 | -55.92%  | 30.35%             | -56.38% |    -1.69 |       79 | 35.77%     | ok               |
|          30 | -58.73%  | 30.35%             | -59.16% |    -1.73 |       84 | 41.60%     | ok               |

## APT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 51.40%   | -90.23%            | -25.96% |     0.85 |       44 | 16.67%     | ok               |
|          20 | 13.17%   | -90.23%            | -56.22% |     0.39 |       84 | 51.53%     | ok               |
|          45 | 13.17%   | -90.23%            | -52.49% |     0.35 |       64 | 24.14%     | ok               |
|          15 | -10.06%  | -90.23%            | -58.22% |     0.21 |       79 | 57.85%     | ok               |
|          35 | -9.01%   | -90.23%            | -49.10% |     0.14 |       74 | 36.02%     | ok               |

## ARB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 81.02%   | -60.10%            | -33.86% |     0.8  |       58 | 26.25%     | ok               |
|          40 | 47.12%   | -60.10%            | -38.69% |     0.6  |       55 | 33.72%     | ok               |
|          35 | 41.73%   | -60.10%            | -37.63% |     0.57 |       69 | 37.74%     | ok               |
|          50 | 35.87%   | -60.10%            | -33.86% |     0.53 |       50 | 18.39%     | ok               |
|          15 | 23.76%   | -60.10%            | -55.99% |     0.47 |       95 | 58.05%     | ok               |

## ARKK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -6.40%   | 60.96%             | -37.76% |     0.06 |       87 | 55.41%     | ok               |
|          20 | -15.76%  | 60.96%             | -35.06% |    -0.11 |       87 | 50.75%     | ok               |
|          30 | -22.96%  | 60.96%             | -35.78% |    -0.28 |       85 | 44.43%     | ok               |
|          35 | -29.98%  | 60.96%             | -40.36% |    -0.47 |       90 | 41.43%     | ok               |
|          25 | -34.06%  | 60.96%             | -45.03% |    -0.51 |       95 | 46.92%     | ok               |

## ATOM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -45.97%  | -67.98%            | -57.59% |    -0.44 |       82 | 65.71%     | ok               |
|          25 | -46.54%  | -67.98%            | -54.33% |    -0.53 |       82 | 52.11%     | ok               |
|          20 | -50.99%  | -67.98%            | -61.00% |    -0.58 |       88 | 57.28%     | ok               |
|          45 | -46.58%  | -67.98%            | -53.91% |    -0.68 |       66 | 31.23%     | ok               |
|          40 | -52.72%  | -67.98%            | -61.33% |    -0.8  |       66 | 36.02%     | ok               |

## AVAX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 59.41%   | -62.44%            | -22.06% |     0.89 |       36 | 19.16%     | ok               |
|          40 | 33.88%   | -62.44%            | -26.27% |     0.58 |       40 | 29.50%     | ok               |
|          45 | 29.37%   | -62.44%            | -24.48% |     0.54 |       36 | 25.29%     | ok               |
|          35 | 5.55%    | -62.44%            | -33.05% |     0.26 |       52 | 35.63%     | ok               |
|          15 | -10.14%  | -62.44%            | -43.71% |     0.12 |       71 | 52.49%     | ok               |

## AVGO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -6.34%   | 115.30%            | -44.82% |     0.09 |       68 | 39.77%     | ok               |
|          25 | -7.42%   | 115.30%            | -45.43% |     0.08 |       72 | 42.60%     | ok               |
|          20 | -14.57%  | 115.30%            | -45.92% |     0.01 |       81 | 46.42%     | ok               |
|          50 | -13.43%  | 115.30%            | -44.23% |    -0.03 |       62 | 27.62%     | ok               |
|          35 | -15.40%  | 115.30%            | -48.57% |    -0.03 |       78 | 36.94%     | ok               |

## BA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 28.10%   | -10.19%            | -13.34% |     0.67 |       46 | 35.61%     | ok               |
|          35 | 34.12%   | -10.19%            | -18.09% |     0.63 |       68 | 49.58%     | ok               |
|          40 | 26.72%   | -10.19%            | -23.87% |     0.56 |       48 | 43.93%     | ok               |
|          25 | 29.51%   | -10.19%            | -26.02% |     0.55 |       66 | 56.24%     | ok               |
|          30 | 19.49%   | -10.19%            | -24.47% |     0.42 |       65 | 52.91%     | ok               |

## BAC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 1.15%    | 25.96%             | -16.89% |     0.11 |       86 | 55.24%     | ok               |
|          35 | -2.14%   | 25.96%             | -24.72% |     0.01 |       70 | 44.43%     | ok               |
|          25 | -3.52%   | 25.96%             | -22.06% |    -0.01 |       84 | 52.41%     | ok               |
|          15 | -5.49%   | 25.96%             | -21.05% |    -0.04 |       90 | 61.90%     | ok               |
|          45 | -4.65%   | 25.96%             | -17.62% |    -0.08 |       58 | 34.44%     | ok               |

## BCH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 14.95%   | -54.76%            | -45.64% |     0.37 |       79 | 57.66%     | ok               |
|          20 | 11.96%   | -54.76%            | -45.52% |     0.34 |       74 | 54.41%     | ok               |
|          35 | -0.83%   | -54.76%            | -57.75% |     0.2  |       72 | 45.02%     | ok               |
|          25 | -3.87%   | -54.76%            | -48.42% |     0.18 |       78 | 50.77%     | ok               |
|          30 | -6.45%   | -54.76%            | -54.04% |     0.14 |       82 | 48.85%     | ok               |

## BITO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 0.03%    | -63.23%            | -31.98% |     0.14 |       54 | 24.29%     | ok               |
|          45 | -4.28%   | -63.23%            | -32.05% |     0.08 |       58 | 27.79%     | ok               |
|          30 | -10.24%  | -63.23%            | -43.13% |     0.04 |       83 | 41.76%     | ok               |
|          35 | -11.86%  | -63.23%            | -42.80% |     0    |       74 | 37.44%     | ok               |
|          40 | -11.58%  | -63.23%            | -40.13% |    -0.01 |       68 | 32.78%     | ok               |

## BLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 1.63%    | 51.15%             | -20.79% |     0.12 |       86 | 43.76%     | ok               |
|          20 | -1.93%   | 51.15%             | -21.48% |     0.04 |       82 | 51.91%     | ok               |
|          25 | -3.33%   | 51.15%             | -24.62% |    -0    |       75 | 49.75%     | ok               |
|          40 | -2.79%   | 51.15%             | -22.83% |    -0    |       78 | 39.27%     | ok               |
|          30 | -7.82%   | 51.15%             | -26.90% |    -0.13 |       79 | 47.25%     | ok               |

## BND Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -7.17%   | -2.32%             | -10.72% |    -1.01 |       65 | 41.43%     | ok               |
|          25 | -6.97%   | -2.32%             | -11.16% |    -1.01 |       70 | 39.27%     | ok               |
|          30 | -6.75%   | -2.32%             | -10.80% |    -1.02 |       68 | 35.61%     | ok               |
|          40 | -6.81%   | -2.32%             | -11.24% |    -1.14 |       60 | 29.28%     | ok               |
|          15 | -8.54%   | -2.32%             | -12.04% |    -1.19 |       77 | 43.76%     | ok               |

## BONK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 141.65%  | -84.18%            | -23.92% |     1.23 |       38 | 17.43%     | ok               |
|          40 | 125.80%  | -84.18%            | -42.38% |     1.03 |       64 | 34.67%     | ok               |
|          45 | 93.95%   | -84.18%            | -31.97% |     0.92 |       64 | 23.95%     | ok               |
|          35 | 79.12%   | -84.18%            | -48.89% |     0.79 |       62 | 40.80%     | ok               |
|          15 | 60.80%   | -84.18%            | -56.51% |     0.67 |       65 | 60.92%     | ok               |

## BTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 55.79%   | -38.77%            | -21.12% |     0.99 |       60 | 41.95%     | ok               |
|          40 | 48.91%   | -38.77%            | -17.26% |     0.93 |       48 | 35.44%     | ok               |
|          45 | 40.89%   | -38.77%            | -12.58% |     0.85 |       40 | 30.65%     | ok               |
|          50 | 17.82%   | -38.77%            | -20.16% |     0.49 |       34 | 25.10%     | ok               |
|          30 | 20.76%   | -38.77%            | -22.34% |     0.47 |       72 | 47.70%     | ok               |

## C Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -12.20%  | 94.87%             | -22.72% |    -0.29 |       68 | 30.62%     | ok               |
|          45 | -22.43%  | 94.87%             | -30.69% |    -0.57 |       78 | 35.94%     | ok               |
|          40 | -27.31%  | 94.87%             | -35.05% |    -0.67 |       74 | 38.44%     | ok               |
|          25 | -34.46%  | 94.87%             | -37.53% |    -0.73 |       71 | 49.58%     | ok               |
|          20 | -36.51%  | 94.87%             | -39.30% |    -0.77 |       77 | 52.25%     | ok               |

## CAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 49.71%   | 74.31%             | -21.80% |     0.73 |       69 | 62.23%     | ok               |
|          25 | 42.20%   | 74.31%             | -21.79% |     0.67 |       66 | 54.08%     | ok               |
|          30 | 32.76%   | 74.31%             | -21.87% |     0.57 |       70 | 51.75%     | ok               |
|          20 | 29.59%   | 74.31%             | -24.56% |     0.53 |       70 | 56.41%     | ok               |
|          45 | 27.19%   | 74.31%             | -23.56% |     0.52 |       56 | 40.10%     | ok               |

## CL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 13.11%   | 1.47%              | -10.72% |     0.5  |       44 | 24.96%     | ok               |
|          45 | 8.81%    | 1.47%              | -10.96% |     0.35 |       46 | 28.12%     | ok               |
|          30 | 7.06%    | 1.47%              | -14.32% |     0.28 |       60 | 40.27%     | ok               |
|          40 | 3.60%    | 1.47%              | -15.09% |     0.18 |       52 | 31.45%     | ok               |
|          35 | 2.79%    | 1.47%              | -15.39% |     0.15 |       60 | 36.44%     | ok               |

## CMCSA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -18.85%  | -29.45%            | -28.74% |    -0.63 |       50 | 16.64%     | ok               |
|          15 | -34.51%  | -29.45%            | -43.53% |    -0.7  |       90 | 58.90%     | ok               |
|          45 | -24.08%  | -29.45%            | -35.43% |    -0.76 |       64 | 21.30%     | ok               |
|          30 | -33.95%  | -29.45%            | -45.88% |    -0.79 |       82 | 44.26%     | ok               |
|          35 | -33.21%  | -29.45%            | -46.34% |    -0.83 |       93 | 39.27%     | ok               |

## COMP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -28.90%  | -65.66%            | -39.83% |    -0.27 |       44 | 21.65%     | ok               |
|          30 | -42.71%  | -65.66%            | -52.17% |    -0.33 |       95 | 48.47%     | ok               |
|          20 | -57.92%  | -65.66%            | -64.98% |    -0.58 |      108 | 63.03%     | ok               |
|          15 | -61.18%  | -65.66%            | -70.31% |    -0.6  |      104 | 67.82%     | ok               |
|          25 | -58.50%  | -65.66%            | -62.74% |    -0.63 |      104 | 56.70%     | ok               |

## COP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -12.17%  | 22.38%             | -35.99% |    -0.17 |       50 | 31.28%     | ok               |
|          30 | -15.39%  | 22.38%             | -38.80% |    -0.19 |       66 | 43.76%     | ok               |
|          35 | -15.25%  | 22.38%             | -41.20% |    -0.19 |       67 | 40.93%     | ok               |
|          45 | -17.00%  | 22.38%             | -41.02% |    -0.27 |       60 | 34.78%     | ok               |
|          40 | -23.27%  | 22.38%             | -47.45% |    -0.41 |       66 | 37.77%     | ok               |

## COST Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 21.42%   | 30.50%             | -24.32% |     0.63 |       62 | 47.09%     | ok               |
|          25 | 17.92%   | 30.50%             | -24.93% |     0.56 |       59 | 44.26%     | ok               |
|          35 | 11.11%   | 30.50%             | -30.16% |     0.41 |       58 | 38.60%     | ok               |
|          30 | 6.41%    | 30.50%             | -31.32% |     0.26 |       60 | 41.10%     | ok               |
|          15 | 4.96%    | 30.50%             | -27.30% |     0.21 |       67 | 50.75%     | ok               |

## CRM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -10.10%  | -23.07%            | -26.69% |    -0.04 |       66 | 41.60%     | ok               |
|          40 | -13.47%  | -23.07%            | -32.67% |    -0.11 |       72 | 37.44%     | ok               |
|          15 | -20.70%  | -23.07%            | -47.54% |    -0.16 |       94 | 58.57%     | ok               |
|          30 | -22.44%  | -23.07%            | -39.41% |    -0.24 |       69 | 46.42%     | ok               |
|          25 | -24.53%  | -23.07%            | -43.32% |    -0.27 |       72 | 49.25%     | ok               |

## CRV-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 117.87%  | -65.52%            | -37.78% |     1.02 |       60 | 33.72%     | ok               |
|          40 | 95.33%   | -65.52%            | -38.86% |     0.92 |       52 | 29.89%     | ok               |
|          45 | 66.12%   | -65.52%            | -42.29% |     0.77 |       56 | 23.56%     | ok               |
|          30 | 67.35%   | -65.52%            | -39.89% |     0.74 |       62 | 38.12%     | ok               |
|          50 | 38.14%   | -65.52%            | -30.73% |     0.58 |       52 | 18.97%     | ok               |

## CSCO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 29.60%   | 100.44%            | -21.30% |     0.62 |       54 | 41.60%     | ok               |
|          50 | 28.79%   | 100.44%            | -19.34% |     0.62 |       54 | 39.77%     | ok               |
|          40 | 13.41%   | 100.44%            | -27.48% |     0.35 |       58 | 44.76%     | ok               |
|          35 | 9.79%    | 100.44%            | -26.96% |     0.29 |       62 | 48.42%     | ok               |
|          20 | 7.93%    | 100.44%            | -29.33% |     0.25 |       73 | 55.07%     | ok               |

## CVX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -8.74%   | 38.26%             | -27.82% |    -0.17 |       63 | 35.94%     | ok               |
|          40 | -9.92%   | 38.26%             | -25.79% |    -0.19 |       73 | 39.60%     | ok               |
|          25 | -11.08%  | 38.26%             | -23.25% |    -0.2  |       73 | 46.42%     | ok               |
|          50 | -8.62%   | 38.26%             | -29.71% |    -0.2  |       56 | 31.45%     | ok               |
|          30 | -13.66%  | 38.26%             | -26.75% |    -0.28 |       69 | 43.59%     | ok               |

## DASH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 102.91%  | 88.21%             | -43.46% |     0.83 |       42 | 17.24%     | ok               |
|          40 | 77.26%   | 88.21%             | -42.64% |     0.71 |       50 | 24.14%     | ok               |
|          45 | 49.78%   | 88.21%             | -46.93% |     0.59 |       46 | 20.50%     | ok               |
|          25 | -14.62%  | 88.21%             | -64.14% |     0.29 |       69 | 32.76%     | ok               |
|          30 | -18.64%  | 88.21%             | -64.43% |     0.26 |       59 | 30.46%     | ok               |

## DBC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -2.39%   | 29.40%             | -26.01% |    -0    |       83 | 43.59%     | ok               |
|          20 | -8.70%   | 29.40%             | -25.69% |    -0.22 |       75 | 40.77%     | ok               |
|          25 | -8.88%   | 29.40%             | -24.84% |    -0.23 |       70 | 38.60%     | ok               |
|          50 | -8.86%   | 29.40%             | -18.84% |    -0.28 |       48 | 25.29%     | ok               |
|          45 | -10.62%  | 29.40%             | -20.02% |    -0.32 |       60 | 28.62%     | ok               |

## DE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -2.14%   | 72.31%             | -19.95% |     0.06 |       63 | 48.59%     | ok               |
|          25 | -3.56%   | 72.31%             | -20.14% |     0.02 |       70 | 46.59%     | ok               |
|          30 | -6.90%   | 72.31%             | -21.16% |    -0.05 |       72 | 44.43%     | ok               |
|          50 | -5.12%   | 72.31%             | -17.97% |    -0.06 |       62 | 30.45%     | ok               |
|          45 | -8.39%   | 72.31%             | -22.07% |    -0.12 |       62 | 34.11%     | ok               |

## DIA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -7.42%   | 29.56%             | -13.58% |    -0.36 |       66 | 45.09%     | ok               |
|          20 | -9.53%   | 29.56%             | -15.48% |    -0.46 |       68 | 47.42%     | ok               |
|          35 | -9.11%   | 29.56%             | -16.94% |    -0.47 |       74 | 40.77%     | ok               |
|          30 | -9.51%   | 29.56%             | -16.20% |    -0.48 |       72 | 43.93%     | ok               |
|          40 | -11.70%  | 29.56%             | -18.41% |    -0.66 |       76 | 37.27%     | ok               |

## DIS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 41.46%   | 14.46%             | -10.17% |     1.18 |       50 | 29.45%     | ok               |
|          40 | 12.13%   | 14.46%             | -18.75% |     0.36 |       65 | 37.60%     | ok               |
|          45 | 9.53%    | 14.46%             | -16.54% |     0.32 |       51 | 33.11%     | ok               |
|          15 | 3.72%    | 14.46%             | -32.73% |     0.18 |       79 | 56.57%     | ok               |
|          35 | 1.34%    | 14.46%             | -25.30% |     0.12 |       73 | 43.59%     | ok               |

## DOGE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 0.03%    | -66.13%            | -51.01% |     0.19 |       58 | 21.07%     | ok               |
|          15 | -8.64%   | -66.13%            | -60.29% |     0.17 |       81 | 62.64%     | ok               |
|          30 | -10.85%  | -66.13%            | -61.52% |     0.1  |       68 | 47.70%     | ok               |
|          20 | -13.38%  | -66.13%            | -60.01% |     0.1  |       79 | 57.09%     | ok               |
|          25 | -15.65%  | -66.13%            | -60.53% |     0.06 |       72 | 52.68%     | ok               |

## DOT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -53.37%  | -80.85%            | -70.04% |    -0.44 |       90 | 52.87%     | ok               |
|          50 | -35.25%  | -80.85%            | -53.14% |    -0.46 |       54 | 20.31%     | ok               |
|          15 | -60.27%  | -80.85%            | -76.85% |    -0.49 |       81 | 57.28%     | ok               |
|          30 | -54.66%  | -80.85%            | -67.54% |    -0.55 |       76 | 41.76%     | ok               |
|          35 | -53.93%  | -80.85%            | -63.75% |    -0.55 |       70 | 37.93%     | ok               |

## DXY-INDEX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.56%   | -4.05%             | -5.13%  |    -0.08 |       40 | 30.52%     | ok               |
|          40 | -2.93%   | -4.05%             | -6.56%  |    -0.4  |       68 | 46.32%     | ok               |
|          45 | -2.91%   | -4.05%             | -6.67%  |    -0.43 |       62 | 37.23%     | ok               |
|          15 | -7.29%   | -4.05%             | -11.34% |    -0.73 |       97 | 72.29%     | ok               |
|          30 | -6.11%   | -4.05%             | -9.45%  |    -0.78 |       78 | 56.49%     | ok               |

## EEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -1.91%   | 37.07%             | -25.18% |     0.02 |       67 | 45.59%     | ok               |
|          25 | -2.99%   | 37.07%             | -23.69% |    -0.01 |       67 | 43.93%     | ok               |
|          15 | -4.74%   | 37.07%             | -26.83% |    -0.06 |       73 | 49.42%     | ok               |
|          30 | -6.33%   | 37.07%             | -24.14% |    -0.12 |       68 | 42.10%     | ok               |
|          35 | -8.21%   | 37.07%             | -23.88% |    -0.19 |       72 | 39.93%     | ok               |

## EFA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -3.08%   | 29.54%             | -10.10% |    -0.06 |       62 | 48.92%     | ok               |
|          20 | -10.05%  | 29.54%             | -13.60% |    -0.37 |       67 | 46.09%     | ok               |
|          30 | -11.02%  | 29.54%             | -13.32% |    -0.45 |       64 | 38.77%     | ok               |
|          25 | -11.46%  | 29.54%             | -15.57% |    -0.45 |       68 | 42.43%     | ok               |
|          40 | -10.91%  | 29.54%             | -15.01% |    -0.49 |       60 | 34.28%     | ok               |

## EOG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -12.96%  | 24.38%             | -34.41% |    -0.23 |       46 | 32.11%     | ok               |
|          40 | -17.04%  | 24.38%             | -36.18% |    -0.33 |       60 | 35.44%     | ok               |
|          35 | -20.21%  | 24.38%             | -38.93% |    -0.39 |       73 | 39.77%     | ok               |
|          50 | -20.56%  | 24.38%             | -35.63% |    -0.46 |       50 | 29.62%     | ok               |
|          30 | -28.34%  | 24.38%             | -47.65% |    -0.58 |       76 | 44.26%     | ok               |

## ETC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 5.70%    | -64.06%            | -43.95% |     0.25 |       48 | 33.33%     | ok               |
|          30 | 2.33%    | -64.06%            | -46.79% |     0.21 |       56 | 36.59%     | ok               |
|          50 | -6.28%   | -64.06%            | -30.03% |     0.02 |       30 | 18.39%     | ok               |
|          40 | -12.02%  | -64.06%            | -41.85% |    -0.04 |       52 | 27.20%     | ok               |
|          45 | -11.22%  | -64.06%            | -35.44% |    -0.05 |       36 | 22.03%     | ok               |

## ETH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 135.47%  | -28.86%            | -30.11% |     1.24 |       63 | 48.08%     | ok               |
|          30 | 97.78%   | -28.86%            | -32.89% |     0.99 |       65 | 55.94%     | ok               |
|          40 | 76.05%   | -28.86%            | -33.11% |     0.93 |       64 | 40.23%     | ok               |
|          25 | 74.09%   | -28.86%            | -40.90% |     0.84 |       63 | 59.77%     | ok               |
|          45 | 53.13%   | -28.86%            | -34.50% |     0.76 |       68 | 36.59%     | ok               |

## EWJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -19.12%  | 31.10%             | -30.00% |    -0.56 |       58 | 40.77%     | ok               |
|          15 | -23.00%  | 31.10%             | -31.15% |    -0.66 |       69 | 44.09%     | ok               |
|          25 | -23.35%  | 31.10%             | -29.85% |    -0.73 |       62 | 39.60%     | ok               |
|          30 | -24.95%  | 31.10%             | -29.40% |    -0.85 |       70 | 38.27%     | ok               |
|          45 | -25.67%  | 31.10%             | -28.91% |    -1.02 |       66 | 29.62%     | ok               |

## FCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 8.05%    | 14.45%             | -30.39% |     0.26 |       54 | 33.61%     | ok               |
|          50 | 1.94%    | 14.45%             | -26.57% |     0.17 |       58 | 29.78%     | ok               |
|          40 | -3.06%   | 14.45%             | -42.89% |     0.1  |       64 | 38.60%     | ok               |
|          30 | -19.70%  | 14.45%             | -46.84% |    -0.13 |       67 | 46.09%     | ok               |
|          35 | -23.74%  | 14.45%             | -50.12% |    -0.21 |       69 | 43.76%     | ok               |

## FET-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 17.24%   | -81.22%            | -59.58% |     0.43 |       69 | 58.24%     | ok               |
|          20 | -24.04%  | -81.22%            | -66.17% |     0.07 |       82 | 54.41%     | ok               |
|          25 | -29.56%  | -81.22%            | -65.31% |    -0.01 |       79 | 48.47%     | ok               |
|          30 | -43.60%  | -81.22%            | -66.52% |    -0.24 |       77 | 44.06%     | ok               |
|          45 | -36.75%  | -81.22%            | -51.19% |    -0.38 |       50 | 22.22%     | ok               |

## FIL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -8.40%   | -75.10%            | -58.54% |     0.14 |       67 | 39.66%     | ok               |
|          40 | -22.52%  | -75.10%            | -57.60% |    -0.08 |       52 | 31.23%     | ok               |
|          35 | -31.71%  | -75.10%            | -65.35% |    -0.2  |       64 | 34.48%     | ok               |
|          25 | -38.23%  | -75.10%            | -70.65% |    -0.23 |       78 | 42.72%     | ok               |
|          15 | -42.13%  | -75.10%            | -72.01% |    -0.23 |       91 | 52.11%     | ok               |

## FXI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -0.88%   | 27.00%             | -21.68% |     0.07 |       48 | 34.78%     | ok               |
|          25 | -2.11%   | 27.00%             | -22.57% |     0.03 |       48 | 31.78%     | ok               |
|          30 | -4.25%   | 27.00%             | -23.91% |    -0.02 |       46 | 30.45%     | ok               |
|          20 | -4.96%   | 27.00%             | -24.53% |    -0.04 |       46 | 32.95%     | ok               |
|          35 | -6.68%   | 27.00%             | -27.53% |    -0.09 |       48 | 27.79%     | ok               |

## GDX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -2.80%   | 132.46%            | -31.05% |     0.12 |       82 | 51.25%     | ok               |
|          40 | -4.94%   | 132.46%            | -34.42% |     0.05 |       66 | 38.94%     | ok               |
|          30 | -6.36%   | 132.46%            | -34.29% |     0.04 |       68 | 45.09%     | ok               |
|          35 | -10.44%  | 132.46%            | -38.67% |    -0.03 |       74 | 41.60%     | ok               |
|          25 | -15.19%  | 132.46%            | -42.42% |    -0.09 |       72 | 46.92%     | ok               |

## GDXJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -16.79%  | 126.04%            | -34.84% |    -0.05 |       72 | 51.58%     | ok               |
|          35 | -28.11%  | 126.04%            | -38.09% |    -0.29 |       70 | 41.76%     | ok               |
|          30 | -30.10%  | 126.04%            | -36.01% |    -0.32 |       70 | 44.43%     | ok               |
|          25 | -34.34%  | 126.04%            | -39.67% |    -0.37 |       75 | 47.59%     | ok               |
|          40 | -30.85%  | 126.04%            | -46.16% |    -0.38 |       64 | 39.27%     | ok               |

## GE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 3.44%    | 103.36%            | -21.25% |     0.17 |       62 | 34.28%     | ok               |
|          45 | -8.63%   | 103.36%            | -21.88% |    -0.08 |       74 | 37.27%     | ok               |
|          30 | -14.33%  | 103.36%            | -27.82% |    -0.16 |       80 | 48.92%     | ok               |
|          25 | -14.73%  | 103.36%            | -29.91% |    -0.17 |       76 | 50.75%     | ok               |
|          20 | -15.21%  | 103.36%            | -25.38% |    -0.17 |       76 | 53.41%     | ok               |

## GLD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 21.05%   | 63.95%             | -13.87% |     0.54 |       48 | 47.59%     | ok               |
|          20 | 19.41%   | 63.95%             | -13.87% |     0.51 |       49 | 49.25%     | ok               |
|          30 | 11.67%   | 63.95%             | -14.15% |     0.35 |       52 | 46.09%     | ok               |
|          35 | 8.96%    | 63.95%             | -15.57% |     0.3  |       52 | 43.43%     | ok               |
|          15 | 9.15%    | 63.95%             | -18.05% |     0.29 |       55 | 52.75%     | ok               |

## GOOGL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 81.37%   | 51.12%             | -17.38% |     1.23 |       59 | 45.59%     | ok               |
|          30 | 78.50%   | 51.12%             | -16.84% |     1.17 |       57 | 49.42%     | ok               |
|          25 | 75.77%   | 51.12%             | -16.16% |     1.13 |       57 | 51.91%     | ok               |
|          45 | 58.29%   | 51.12%             | -11.66% |     1.03 |       52 | 38.60%     | ok               |
|          20 | 66.31%   | 51.12%             | -17.62% |     1.02 |       65 | 53.91%     | ok               |

## GRT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 85.39%   | -79.89%            | -29.35% |     0.87 |       64 | 41.38%     | ok               |
|          45 | 75.74%   | -79.89%            | -37.14% |     0.86 |       50 | 27.39%     | ok               |
|          15 | 86.45%   | -79.89%            | -36.70% |     0.82 |       68 | 62.07%     | ok               |
|          30 | 74.85%   | -79.89%            | -38.70% |     0.8  |       71 | 47.32%     | ok               |
|          40 | 61.92%   | -79.89%            | -38.09% |     0.75 |       52 | 33.52%     | ok               |

## GS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 22.58%   | 96.77%             | -20.56% |     0.5  |       66 | 55.24%     | ok               |
|          40 | 7.27%    | 96.77%             | -16.16% |     0.25 |       64 | 40.93%     | ok               |
|          20 | 7.49%    | 96.77%             | -23.19% |     0.25 |       64 | 51.91%     | ok               |
|          25 | -0.60%   | 96.77%             | -23.32% |     0.09 |       66 | 49.92%     | ok               |
|          35 | -1.92%   | 96.77%             | -19.95% |     0.06 |       68 | 44.59%     | ok               |

## HBAR-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -20.86%  | -44.31%            | -58.64% |    -0.17 |       52 | 56.38%     | ok               |
|          30 | -23.19%  | -44.31%            | -56.47% |    -0.25 |       42 | 42.28%     | ok               |
|          45 | -22.53%  | -44.31%            | -49.09% |    -0.29 |       28 | 27.18%     | ok               |
|          40 | -24.21%  | -44.31%            | -51.16% |    -0.32 |       32 | 32.89%     | ok               |
|          20 | -29.56%  | -44.31%            | -63.19% |    -0.38 |       55 | 51.68%     | ok               |

## HD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 7.26%    | -0.73%             | -17.15% |     0.26 |       69 | 44.93%     | ok               |
|          35 | 5.84%    | -0.73%             | -15.36% |     0.23 |       70 | 40.27%     | ok               |
|          25 | 3.60%    | -0.73%             | -16.67% |     0.17 |       70 | 47.42%     | ok               |
|          40 | 2.28%    | -0.73%             | -14.18% |     0.14 |       72 | 35.11%     | ok               |
|          45 | 1.48%    | -0.73%             | -13.70% |     0.11 |       48 | 30.28%     | ok               |

## HON Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -11.49%  | 3.33%              | -20.43% |    -0.3  |       64 | 30.95%     | ok               |
|          45 | -15.09%  | 3.33%              | -22.88% |    -0.39 |       66 | 36.11%     | ok               |
|          35 | -27.17%  | 3.33%              | -31.30% |    -0.72 |       87 | 47.42%     | ok               |
|          30 | -28.80%  | 3.33%              | -32.97% |    -0.74 |       89 | 52.41%     | ok               |
|          40 | -27.36%  | 3.33%              | -31.84% |    -0.76 |       74 | 40.27%     | ok               |

## HYG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -4.80%   | -0.91%             | -8.00%  |    -0.55 |       72 | 33.94%     | ok               |
|          45 | -6.57%   | -0.91%             | -9.14%  |    -0.79 |       72 | 30.28%     | ok               |
|          20 | -7.48%   | -0.91%             | -11.59% |    -0.8  |       96 | 45.26%     | ok               |
|          25 | -7.47%   | -0.91%             | -11.22% |    -0.81 |       91 | 42.60%     | ok               |
|          35 | -7.01%   | -0.91%             | -9.76%  |    -0.81 |       81 | 35.77%     | ok               |

## IBIT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 85.38%   | -4.92%             | -19.20% |     1.08 |       48 | 43.33%     | ok               |
|          50 | 54.99%   | -4.92%             | -17.37% |     0.95 |       28 | 24.56%     | ok               |
|          45 | 53.42%   | -4.92%             | -17.37% |     0.9  |       34 | 26.11%     | ok               |
|          30 | 51.81%   | -4.92%             | -18.95% |     0.82 |       46 | 35.98%     | ok               |
|          40 | 41.36%   | -4.92%             | -22.57% |     0.74 |       42 | 29.21%     | ok               |

## IBM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -15.03%  | 35.26%             | -49.43% |    -0.07 |       87 | 62.40%     | ok               |
|          35 | -18.61%  | 35.26%             | -47.10% |    -0.17 |       65 | 47.42%     | ok               |
|          30 | -20.31%  | 35.26%             | -48.94% |    -0.2  |       71 | 50.58%     | ok               |
|          20 | -27.22%  | 35.26%             | -53.45% |    -0.3  |       73 | 55.41%     | ok               |
|          50 | -26.67%  | 35.26%             | -45.97% |    -0.37 |       46 | 36.27%     | ok               |

## ICP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 3.73%    | -58.15%            | -43.17% |     0.3  |       74 | 40.42%     | ok               |
|          35 | -4.59%   | -58.15%            | -52.30% |     0.18 |       68 | 35.25%     | ok               |
|          40 | -4.71%   | -58.15%            | -46.01% |     0.17 |       62 | 31.03%     | ok               |
|          20 | -35.11%  | -58.15%            | -67.59% |    -0.02 |       85 | 49.04%     | ok               |
|          15 | -37.83%  | -58.15%            | -65.54% |    -0.04 |       81 | 52.49%     | ok               |

## IEF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -5.56%   | -3.97%             | -10.18% |    -0.64 |       74 | 43.43%     | ok               |
|          15 | -6.80%   | -3.97%             | -10.91% |    -0.77 |       73 | 45.09%     | ok               |
|          40 | -7.97%   | -3.97%             | -10.34% |    -1.14 |       64 | 27.29%     | ok               |
|          45 | -7.92%   | -3.97%             | -10.45% |    -1.17 |       60 | 24.96%     | ok               |
|          25 | -9.82%   | -3.97%             | -11.95% |    -1.22 |       78 | 40.27%     | ok               |

## IEMG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 0.11%    | 33.11%             | -23.73% |     0.07 |       63 | 44.26%     | ok               |
|          20 | -1.58%   | 33.11%             | -25.26% |     0.02 |       61 | 45.92%     | ok               |
|          30 | -3.15%   | 33.11%             | -24.73% |    -0.03 |       64 | 41.93%     | ok               |
|          35 | -3.32%   | 33.11%             | -21.81% |    -0.04 |       69 | 40.60%     | ok               |
|          40 | -5.84%   | 33.11%             | -18.43% |    -0.14 |       66 | 38.10%     | ok               |

## INJ-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 33.68%   | -35.80%            | -42.48% |     0.53 |       52 | 35.63%     | ok               |
|          40 | 31.33%   | -35.80%            | -33.49% |     0.51 |       42 | 32.38%     | ok               |
|          45 | 13.61%   | -35.80%            | -39.58% |     0.35 |       48 | 26.05%     | ok               |
|          25 | -9.09%   | -35.80%            | -56.45% |     0.18 |       59 | 41.76%     | ok               |
|          15 | -11.08%  | -35.80%            | -64.35% |     0.18 |       68 | 46.74%     | ok               |

## INTC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 110.54%  | 80.35%             | -49.32% |     0.89 |       60 | 35.61%     | ok               |
|          50 | 104.00%  | 80.35%             | -48.35% |     0.87 |       64 | 31.78%     | ok               |
|          40 | 87.44%   | 80.35%             | -55.86% |     0.77 |       68 | 39.77%     | ok               |
|          15 | 90.94%   | 80.35%             | -53.65% |     0.76 |       76 | 60.40%     | ok               |
|          20 | 80.30%   | 80.35%             | -52.47% |     0.72 |       82 | 56.91%     | ok               |

## INTU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 9.48%    | -50.76%            | -34.18% |     0.28 |       67 | 28.95%     | ok               |
|          35 | 5.79%    | -50.76%            | -41.38% |     0.22 |       69 | 41.43%     | ok               |
|          45 | 3.88%    | -50.76%            | -36.15% |     0.19 |       65 | 33.11%     | ok               |
|          40 | 2.22%    | -50.76%            | -38.46% |     0.16 |       69 | 36.61%     | ok               |
|          25 | -2.49%   | -50.76%            | -35.24% |     0.1  |       71 | 50.42%     | ok               |

## ITA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 0.31%    | 57.26%             | -26.15% |     0.1  |       73 | 59.40%     | ok               |
|          30 | 0.52%    | 57.26%             | -22.33% |     0.09 |       72 | 47.09%     | ok               |
|          50 | -0.54%   | 57.26%             | -21.48% |     0.05 |       68 | 34.78%     | ok               |
|          35 | -4.77%   | 57.26%             | -22.44% |    -0.07 |       72 | 43.43%     | ok               |
|          20 | -5.79%   | 57.26%             | -26.56% |    -0.07 |       72 | 53.74%     | ok               |

## IWM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          25 | 17.32%   | 33.15%             | -8.02% |     0.64 |       52 | 35.77%     | ok               |
|          20 | 12.69%   | 33.15%             | -9.67% |     0.49 |       62 | 36.77%     | ok               |
|          30 | 10.39%   | 33.15%             | -8.62% |     0.42 |       56 | 34.44%     | ok               |
|          40 | 8.67%    | 33.15%             | -9.21% |     0.4  |       44 | 29.28%     | ok               |
|          35 | 8.33%    | 33.15%             | -9.25% |     0.36 |       52 | 31.95%     | ok               |

## JNJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 22.45%   | 91.15%             | -10.97% |     0.84 |       42 | 36.77%     | ok               |
|          15 | 18.47%   | 91.15%             | -18.02% |     0.62 |       58 | 54.24%     | ok               |
|          30 | 13.37%   | 91.15%             | -17.51% |     0.5  |       60 | 47.75%     | ok               |
|          45 | 11.98%   | 91.15%             | -13.35% |     0.48 |       48 | 40.43%     | ok               |
|          20 | 12.99%   | 91.15%             | -17.61% |     0.48 |       64 | 50.75%     | ok               |

## JPM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 0.07%    | 65.67%             | -15.90% |     0.06 |       52 | 32.11%     | ok               |
|          45 | -10.24%  | 65.67%             | -21.91% |    -0.27 |       56 | 34.78%     | ok               |
|          20 | -27.12%  | 65.67%             | -35.58% |    -0.64 |       88 | 49.25%     | ok               |
|          40 | -22.56%  | 65.67%             | -28.47% |    -0.69 |       68 | 37.44%     | ok               |
|          35 | -25.09%  | 65.67%             | -29.36% |    -0.76 |       78 | 41.10%     | ok               |

## KO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 28.92%   | 54.58%             | -8.64%  |     0.96 |       54 | 39.77%     | ok               |
|          40 | 24.02%   | 54.58%             | -9.28%  |     0.87 |       58 | 35.27%     | ok               |
|          35 | 24.54%   | 54.58%             | -8.73%  |     0.85 |       58 | 38.27%     | ok               |
|          25 | 22.65%   | 54.58%             | -10.61% |     0.78 |       60 | 42.43%     | ok               |
|          50 | 10.84%   | 54.58%             | -16.13% |     0.47 |       44 | 29.45%     | ok               |

## LDO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 223.33%  | -66.26%            | -38.70% |     1.23 |       76 | 60.34%     | ok               |
|          20 | 130.56%  | -66.26%            | -41.80% |     0.98 |       79 | 55.17%     | ok               |
|          30 | 94.63%   | -66.26%            | -47.94% |     0.85 |       68 | 48.28%     | ok               |
|          25 | 92.67%   | -66.26%            | -46.04% |     0.83 |       74 | 52.68%     | ok               |
|          35 | 11.29%   | -66.26%            | -58.88% |     0.35 |       80 | 41.19%     | ok               |

## LIN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -1.78%   | 17.01%             | -22.01% |     0.01 |       69 | 45.09%     | ok               |
|          20 | -2.55%   | 17.01%             | -23.00% |    -0.02 |       64 | 47.92%     | ok               |
|          15 | -4.43%   | 17.01%             | -23.68% |    -0.08 |       70 | 50.92%     | ok               |
|          45 | -3.83%   | 17.01%             | -17.04% |    -0.1  |       48 | 25.79%     | ok               |
|          30 | -5.06%   | 17.01%             | -20.61% |    -0.11 |       70 | 42.26%     | ok               |

## LINK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 39.21%   | -30.45%            | -34.21% |     0.58 |       64 | 38.70%     | ok               |
|          30 | 34.06%   | -30.45%            | -35.01% |     0.54 |       72 | 43.10%     | ok               |
|          40 | 32.32%   | -30.45%            | -36.88% |     0.53 |       56 | 33.14%     | ok               |
|          50 | 26.95%   | -30.45%            | -30.35% |     0.49 |       44 | 24.14%     | ok               |
|          45 | 27.13%   | -30.45%            | -34.16% |     0.49 |       52 | 29.69%     | ok               |

## LLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.95%   | 55.72%             | -39.36% |     0.1  |       52 | 35.61%     | ok               |
|          15 | -13.35%  | 55.72%             | -48.12% |    -0.06 |       70 | 60.23%     | ok               |
|          45 | -14.36%  | 55.72%             | -44.03% |    -0.16 |       62 | 39.43%     | ok               |
|          20 | -25.40%  | 55.72%             | -51.14% |    -0.3  |       77 | 55.41%     | ok               |
|          40 | -23.40%  | 55.72%             | -46.22% |    -0.32 |       72 | 42.60%     | ok               |

## LRCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -15.39%  | 99.55%             | -56.69% |     0.07 |       82 | 54.08%     | ok               |
|          50 | -10.42%  | 99.55%             | -48.71% |     0.06 |       76 | 35.94%     | ok               |
|          35 | -18.31%  | 99.55%             | -58.47% |    -0.01 |       82 | 44.59%     | ok               |
|          20 | -22.71%  | 99.55%             | -62.91% |    -0.03 |       87 | 49.92%     | ok               |
|          40 | -21.92%  | 99.55%             | -55.33% |    -0.06 |       74 | 42.26%     | ok               |

## LTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 39.18%   | -48.35%            | -34.94% |     0.62 |       66 | 44.64%     | ok               |
|          30 | 32.55%   | -48.35%            | -30.78% |     0.55 |       67 | 51.15%     | ok               |
|          25 | 31.01%   | -48.35%            | -34.22% |     0.53 |       67 | 53.83%     | ok               |
|          45 | 28.78%   | -48.35%            | -36.44% |     0.53 |       56 | 33.72%     | ok               |
|          40 | 13.62%   | -48.35%            | -40.31% |     0.35 |       56 | 39.66%     | ok               |

## MCD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 8.27%    | 6.84%              | -9.22%  |     0.39 |       50 | 25.79%     | ok               |
|          30 | 7.75%    | 6.84%              | -22.20% |     0.32 |       77 | 41.10%     | ok               |
|          35 | 6.28%    | 6.84%              | -16.97% |     0.28 |       69 | 38.27%     | ok               |
|          25 | 5.51%    | 6.84%              | -23.93% |     0.24 |       75 | 43.76%     | ok               |
|          20 | 1.21%    | 6.84%              | -24.58% |     0.1  |       77 | 46.92%     | ok               |

## META Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -20.10%  | 19.11%             | -37.54% |    -0.27 |       68 | 38.77%     | ok               |
|          40 | -23.47%  | 19.11%             | -40.90% |    -0.32 |       68 | 42.10%     | ok               |
|          50 | -24.49%  | 19.11%             | -39.33% |    -0.39 |       68 | 34.28%     | ok               |
|          30 | -34.31%  | 19.11%             | -44.90% |    -0.53 |       72 | 49.92%     | ok               |
|          35 | -34.37%  | 19.11%             | -41.21% |    -0.56 |       81 | 47.59%     | ok               |

## MPC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 20.28%   | 128.80%            | -18.24% |     0.45 |       52 | 41.43%     | ok               |
|          40 | 18.30%   | 128.80%            | -20.11% |     0.41 |       62 | 48.09%     | ok               |
|          35 | 17.46%   | 128.80%            | -30.41% |     0.39 |       68 | 50.75%     | ok               |
|          45 | 16.22%   | 128.80%            | -19.46% |     0.38 |       58 | 45.42%     | ok               |
|          30 | 11.57%   | 128.80%            | -33.74% |     0.31 |       70 | 53.41%     | ok               |

## MRK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -14.60%  | 10.44%             | -28.39% |    -0.19 |       85 | 53.08%     | ok               |
|          25 | -15.36%  | 10.44%             | -31.07% |    -0.23 |       72 | 45.26%     | ok               |
|          20 | -19.51%  | 10.44%             | -29.34% |    -0.33 |       77 | 48.59%     | ok               |
|          50 | -16.04%  | 10.44%             | -23.01% |    -0.34 |       58 | 29.62%     | ok               |
|          45 | -18.12%  | 10.44%             | -25.38% |    -0.37 |       59 | 32.95%     | ok               |

## MS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 2.22%    | 91.64%             | -19.99% |     0.14 |       66 | 38.44%     | ok               |
|          15 | 1.35%    | 91.64%             | -22.02% |     0.13 |       74 | 56.57%     | ok               |
|          20 | -0.91%   | 91.64%             | -25.68% |     0.07 |       73 | 52.41%     | ok               |
|          30 | -4.92%   | 91.64%             | -27.79% |    -0.03 |       73 | 47.42%     | ok               |
|          25 | -6.42%   | 91.64%             | -28.36% |    -0.06 |       71 | 49.58%     | ok               |

## MSFT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -16.31%  | 11.79%             | -24.64% |    -0.38 |       70 | 36.61%     | ok               |
|          50 | -19.70%  | 11.79%             | -25.48% |    -0.51 |       60 | 31.45%     | ok               |
|          35 | -25.87%  | 11.79%             | -35.51% |    -0.59 |       73 | 46.09%     | ok               |
|          40 | -25.52%  | 11.79%             | -34.92% |    -0.6  |       69 | 40.27%     | ok               |
|          30 | -27.63%  | 11.79%             | -38.06% |    -0.61 |       81 | 50.58%     | ok               |

## MU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 105.85%  | 438.77%            | -61.12% |     0.87 |       60 | 44.76%     | ok               |
|          45 | 93.79%   | 438.77%            | -62.28% |     0.84 |       60 | 41.93%     | ok               |
|          15 | 101.90%  | 438.77%            | -61.96% |     0.81 |       58 | 58.07%     | ok               |
|          30 | 85.07%   | 438.77%            | -64.76% |     0.77 |       55 | 49.42%     | ok               |
|          35 | 79.96%   | 438.77%            | -65.13% |     0.75 |       67 | 47.09%     | ok               |

## NEAR-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 246.37%  | 51.91%             | -41.76% |     1.37 |       42 | 32.76%     | ok               |
|          50 | 207.33%  | 51.91%             | -43.09% |     1.36 |       32 | 22.61%     | ok               |
|          45 | 190.69%  | 51.91%             | -38.08% |     1.23 |       44 | 28.74%     | ok               |
|          35 | 168.71%  | 51.91%             | -51.21% |     1.14 |       62 | 36.59%     | ok               |
|          30 | 177.42%  | 51.91%             | -46.60% |     1.13 |       65 | 43.49%     | ok               |

## NEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -4.57%   | 165.92%            | -30.50% |     0.1  |       71 | 54.08%     | ok               |
|          15 | -7.30%   | 165.92%            | -35.45% |     0.08 |       66 | 58.74%     | ok               |
|          50 | -12.51%  | 165.92%            | -33.03% |    -0.06 |       48 | 37.77%     | ok               |
|          25 | -19.14%  | 165.92%            | -39.51% |    -0.12 |       68 | 51.75%     | ok               |
|          30 | -25.86%  | 165.92%            | -39.56% |    -0.25 |       70 | 49.75%     | ok               |

## NFLX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 17.23%   | -12.79%            | -20.78% |     0.47 |       54 | 38.27%     | ok               |
|          50 | 14.62%   | -12.79%            | -16.28% |     0.44 |       44 | 29.95%     | ok               |
|          35 | 11.84%   | -12.79%            | -18.30% |     0.34 |       80 | 43.26%     | ok               |
|          15 | 5.70%    | -12.79%            | -26.59% |     0.22 |       76 | 63.89%     | ok               |
|          45 | 3.17%    | -12.79%            | -18.06% |     0.16 |       58 | 34.28%     | ok               |

## NKE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -19.26%  | -61.94%            | -42.13% |    -0.21 |       73 | 39.60%     | ok               |
|          25 | -29.33%  | -61.94%            | -51.20% |    -0.32 |       85 | 52.25%     | ok               |
|          20 | -31.42%  | -61.94%            | -49.69% |    -0.35 |       89 | 55.24%     | ok               |
|          30 | -33.77%  | -61.94%            | -55.35% |    -0.42 |       87 | 47.42%     | ok               |
|          40 | -24.14%  | -61.94%            | -33.81% |    -0.44 |       67 | 32.45%     | ok               |

## NOW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -5.75%   | -40.00%            | -42.66% |     0.15 |       79 | 51.75%     | ok               |
|          20 | -8.95%   | -40.00%            | -49.77% |     0.12 |       73 | 57.40%     | ok               |
|          25 | -12.51%  | -40.00%            | -47.93% |     0.07 |       71 | 55.07%     | ok               |
|          15 | -14.69%  | -40.00%            | -52.56% |     0.06 |       81 | 60.23%     | ok               |
|          35 | -18.55%  | -40.00%            | -48.24% |    -0.03 |       82 | 46.92%     | ok               |

## NVDA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -23.26%  | 20.17%             | -38.70% |    -0.21 |       76 | 51.52%     | ok               |
|          25 | -28.69%  | 20.17%             | -44.52% |    -0.34 |       81 | 47.59%     | ok               |
|          30 | -28.45%  | 20.17%             | -43.72% |    -0.35 |       82 | 44.74%     | ok               |
|          15 | -36.11%  | 20.17%             | -50.87% |    -0.44 |       82 | 55.79%     | ok               |
|          35 | -39.21%  | 20.17%             | -51.44% |    -0.61 |       92 | 41.89%     | ok               |

## OP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 47.07%   | -86.94%            | -33.09% |     0.75 |       44 | 11.49%     | ok               |
|          45 | 36.72%   | -86.94%            | -30.78% |     0.58 |       46 | 17.62%     | ok               |
|          40 | 13.40%   | -86.94%            | -43.68% |     0.35 |       50 | 25.86%     | ok               |
|          15 | -12.98%  | -86.94%            | -55.83% |     0.14 |       75 | 48.08%     | ok               |
|          30 | -16.12%  | -86.94%            | -57.66% |     0.06 |       72 | 36.02%     | ok               |

## ORCL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 129.87%  | -17.96%            | -37.59% |     0.99 |       67 | 59.73%     | ok               |
|          45 | 91.50%   | -17.96%            | -32.35% |     0.89 |       54 | 37.60%     | ok               |
|          25 | 84.82%   | -17.96%            | -31.06% |     0.79 |       59 | 52.25%     | ok               |
|          35 | 76.07%   | -17.96%            | -31.95% |     0.76 |       60 | 46.42%     | ok               |
|          20 | 79.67%   | -17.96%            | -32.60% |     0.76 |       68 | 55.41%     | ok               |

## OXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 3.84%    | -9.84%             | -28.48% |     0.19 |       67 | 43.43%     | ok               |
|          35 | 2.12%    | -9.84%             | -26.37% |     0.15 |       70 | 38.60%     | ok               |
|          40 | -1.50%   | -9.84%             | -28.30% |     0.09 |       58 | 35.27%     | ok               |
|          50 | -3.61%   | -9.84%             | -28.12% |     0.04 |       48 | 28.12%     | ok               |
|          25 | -10.64%  | -9.84%             | -38.51% |    -0.06 |       75 | 47.09%     | ok               |

## PEP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 17.05%   | -14.58%            | -11.62% |     0.69 |       40 | 26.62%     | ok               |
|          45 | 5.45%    | -14.58%            | -14.22% |     0.26 |       52 | 30.45%     | ok               |
|          30 | 3.12%    | -14.58%            | -21.35% |     0.16 |       70 | 45.92%     | ok               |
|          35 | 1.51%    | -14.58%            | -21.42% |     0.11 |       73 | 40.27%     | ok               |
|          40 | -1.36%   | -14.58%            | -18.04% |     0.01 |       68 | 35.61%     | ok               |

## PEPE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -31.09%  | -66.10%            | -60.19% |    -0.04 |       74 | 47.13%     | ok               |
|          15 | -40.23%  | -66.10%            | -65.61% |    -0.05 |       83 | 61.69%     | ok               |
|          20 | -36.66%  | -66.10%            | -63.56% |    -0.06 |       89 | 57.47%     | ok               |
|          35 | -37.32%  | -66.10%            | -60.83% |    -0.18 |       66 | 43.30%     | ok               |
|          25 | -48.59%  | -66.10%            | -64.37% |    -0.27 |       88 | 52.11%     | ok               |

## PFE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -15.07%  | 2.41%              | -25.81% |    -0.45 |       52 | 22.96%     | ok               |
|          50 | -14.14%  | 2.41%              | -27.79% |    -0.46 |       40 | 19.63%     | ok               |
|          40 | -18.08%  | 2.41%              | -30.60% |    -0.53 |       74 | 28.12%     | ok               |
|          35 | -25.97%  | 2.41%              | -36.12% |    -0.78 |       84 | 34.61%     | ok               |
|          30 | -33.58%  | 2.41%              | -42.77% |    -1.02 |       79 | 37.60%     | ok               |

## PG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -4.44%   | 3.06%              | -19.77% |    -0.11 |       50 | 30.45%     | ok               |
|          35 | -7.70%   | 3.06%              | -18.66% |    -0.23 |       58 | 33.94%     | ok               |
|          45 | -12.54%  | 3.06%              | -21.69% |    -0.45 |       50 | 28.12%     | ok               |
|          30 | -16.08%  | 3.06%              | -24.25% |    -0.53 |       60 | 37.10%     | ok               |
|          25 | -18.00%  | 3.06%              | -25.55% |    -0.61 |       72 | 38.60%     | ok               |

## PM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -3.64%   | 91.38%             | -35.28% |     0.01 |       82 | 44.09%     | ok               |
|          20 | -6.16%   | 91.38%             | -36.74% |    -0.04 |       81 | 52.75%     | ok               |
|          30 | -6.67%   | 91.38%             | -38.30% |    -0.06 |       77 | 47.59%     | ok               |
|          50 | -9.22%   | 91.38%             | -36.94% |    -0.16 |       66 | 35.44%     | ok               |
|          40 | -11.18%  | 91.38%             | -39.92% |    -0.2  |       76 | 40.60%     | ok               |

## POL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 9.75%    | -59.05%            | -30.34% |     0.3  |       52 | 20.69%     | ok               |
|          25 | 5.01%    | -59.05%            | -46.25% |     0.28 |       77 | 54.21%     | ok               |
|          20 | 4.56%    | -59.05%            | -48.58% |     0.28 |       87 | 58.05%     | ok               |
|          15 | -1.15%   | -59.05%            | -48.61% |     0.23 |       92 | 63.03%     | ok               |
|          30 | -0.25%   | -59.05%            | -46.25% |     0.21 |       85 | 49.23%     | ok               |

## QCOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -20.59%  | -14.59%            | -48.54% |    -0.09 |       71 | 41.93%     | ok               |
|          20 | -26.43%  | -14.59%            | -48.40% |    -0.18 |       67 | 45.26%     | ok               |
|          35 | -27.29%  | -14.59%            | -44.11% |    -0.23 |       79 | 37.60%     | ok               |
|          15 | -35.32%  | -14.59%            | -52.43% |    -0.31 |       69 | 47.92%     | ok               |
|          30 | -35.78%  | -14.59%            | -50.90% |    -0.37 |       77 | 40.10%     | ok               |

## QQQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 6.85%    | 36.41%             | -17.16% |     0.25 |       73 | 52.41%     | ok               |
|          25 | 3.33%    | 36.41%             | -14.05% |     0.17 |       67 | 45.26%     | ok               |
|          20 | 2.09%    | 36.41%             | -14.88% |     0.14 |       79 | 48.42%     | ok               |
|          30 | -3.64%   | 36.41%             | -15.84% |    -0.02 |       72 | 43.26%     | ok               |
|          35 | -14.18%  | 36.41%             | -20.59% |    -0.34 |       80 | 39.27%     | ok               |

## RENDER-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 5.28%    | -58.60%            | -44.12% |     0.34 |       88 | 63.03%     | ok               |
|          20 | -2.10%   | -58.60%            | -48.40% |     0.27 |       89 | 57.66%     | ok               |
|          25 | -4.38%   | -58.60%            | -48.19% |     0.24 |       83 | 52.68%     | ok               |
|          50 | -17.79%  | -58.60%            | -42.00% |    -0.12 |       54 | 18.20%     | ok               |
|          30 | -43.34%  | -58.60%            | -54.95% |    -0.26 |       86 | 46.93%     | ok               |

## RTX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 27.30%   | 96.78%             | -18.66% |     0.61 |       74 | 58.74%     | ok               |
|          25 | 23.72%   | 96.78%             | -18.59% |     0.55 |       64 | 55.91%     | ok               |
|          15 | 18.43%   | 96.78%             | -19.55% |     0.45 |       69 | 62.90%     | ok               |
|          50 | 13.31%   | 96.78%             | -18.42% |     0.43 |       62 | 39.77%     | ok               |
|          30 | 16.35%   | 96.78%             | -16.99% |     0.43 |       73 | 52.91%     | ok               |

## SBUX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 2.55%    | 35.65%             | -23.55% |     0.15 |       61 | 42.43%     | ok               |
|          40 | 1.20%    | 35.65%             | -25.43% |     0.12 |       60 | 34.28%     | ok               |
|          45 | -0.78%   | 35.65%             | -27.26% |     0.07 |       64 | 29.62%     | ok               |
|          35 | -2.28%   | 35.65%             | -26.54% |     0.05 |       64 | 37.60%     | ok               |
|          50 | -4.97%   | 35.65%             | -25.13% |    -0.04 |       50 | 24.96%     | ok               |

## SCHW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -1.47%   | 24.85%             | -29.24% |     0.06 |       71 | 52.58%     | ok               |
|          25 | -3.28%   | 24.85%             | -28.76% |     0.02 |       67 | 50.92%     | ok               |
|          45 | -3.45%   | 24.85%             | -16.53% |    -0.04 |       62 | 31.28%     | ok               |
|          50 | -3.90%   | 24.85%             | -13.28% |    -0.08 |       54 | 28.12%     | ok               |
|          15 | -8.22%   | 24.85%             | -31.37% |    -0.09 |       80 | 56.74%     | ok               |

## SHIB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -17.45%  | -68.02%            | -47.25% |    -0.01 |       85 | 65.71%     | ok               |
|          35 | -16.52%  | -68.02%            | -43.57% |    -0.04 |       75 | 46.17%     | ok               |
|          20 | -20.92%  | -68.02%            | -49.90% |    -0.06 |       78 | 61.11%     | ok               |
|          40 | -21.01%  | -68.02%            | -41.81% |    -0.14 |       62 | 37.36%     | ok               |
|          50 | -16.87%  | -68.02%            | -32.18% |    -0.15 |       50 | 21.07%     | ok               |

## SHY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          30 | -2.37%   | -0.39%             | -3.30% |    -0.76 |       56 | 39.10%     | ok               |
|          40 | -2.60%   | -0.39%             | -3.58% |    -0.87 |       60 | 35.44%     | ok               |
|          35 | -2.90%   | -0.39%             | -3.61% |    -0.96 |       58 | 36.94%     | ok               |
|          45 | -2.67%   | -0.39%             | -3.43% |    -0.98 |       58 | 28.79%     | ok               |
|          50 | -2.67%   | -0.39%             | -3.40% |    -1.03 |       48 | 24.79%     | ok               |

## SKY-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -47.54%  | -40.83%            | -63.51% |    -0.5  |       77 | 56.70%     | ok               |
|          30 | -50.34%  | -40.83%            | -63.39% |    -0.66 |       85 | 45.98%     | ok               |
|          35 | -49.26%  | -40.83%            | -62.59% |    -0.69 |       76 | 37.74%     | ok               |
|          25 | -55.95%  | -40.83%            | -66.70% |    -0.77 |       78 | 49.23%     | ok               |
|          20 | -60.34%  | -40.83%            | -70.01% |    -0.84 |       81 | 52.87%     | ok               |

## SLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -15.24%  | 4.13%              | -31.05% |    -0.22 |       52 | 35.11%     | ok               |
|          45 | -17.26%  | 4.13%              | -30.92% |    -0.28 |       58 | 32.11%     | ok               |
|          50 | -15.78%  | 4.13%              | -29.04% |    -0.3  |       46 | 25.46%     | ok               |
|          35 | -33.41%  | 4.13%              | -46.93% |    -0.64 |       74 | 42.76%     | ok               |
|          25 | -38.77%  | 4.13%              | -52.31% |    -0.72 |       88 | 51.91%     | ok               |

## SLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 65.52%   | 61.21%             | -28.72% |     0.85 |       52 | 31.61%     | ok               |
|          45 | 51.46%   | 61.21%             | -31.33% |     0.72 |       63 | 33.11%     | ok               |
|          20 | 53.83%   | 61.21%             | -37.05% |     0.71 |       70 | 46.09%     | ok               |
|          40 | 50.27%   | 61.21%             | -34.28% |     0.71 |       67 | 35.11%     | ok               |
|          15 | 51.26%   | 61.21%             | -47.98% |     0.67 |       71 | 50.75%     | ok               |

## SMH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 81.58%   | 77.74%             | -31.01% |     1.04 |       49 | 44.76%     | ok               |
|          25 | 65.16%   | 77.74%             | -32.94% |     0.92 |       46 | 43.26%     | ok               |
|          30 | 60.66%   | 77.74%             | -33.66% |     0.88 |       50 | 41.93%     | ok               |
|          35 | 48.70%   | 77.74%             | -34.03% |     0.77 |       56 | 39.93%     | ok               |
|          45 | 37.51%   | 77.74%             | -32.84% |     0.68 |       54 | 34.44%     | ok               |

## SNX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 22.08%   | -74.91%            | -29.01% |     0.45 |       46 | 26.25%     | ok               |
|          35 | 22.01%   | -74.91%            | -42.92% |     0.44 |       52 | 30.46%     | ok               |
|          20 | 4.01%    | -74.91%            | -53.03% |     0.28 |       72 | 46.55%     | ok               |
|          15 | -5.27%   | -74.91%            | -54.74% |     0.2  |       73 | 50.77%     | ok               |
|          45 | 0.76%    | -74.91%            | -34.25% |     0.16 |       46 | 21.26%     | ok               |

## SOL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 79.05%   | -51.08%            | -40.41% |     0.9  |       56 | 40.04%     | ok               |
|          45 | 37.29%   | -51.08%            | -47.42% |     0.6  |       54 | 33.33%     | ok               |
|          35 | 37.62%   | -51.08%            | -44.32% |     0.57 |       70 | 45.79%     | ok               |
|          25 | 24.12%   | -51.08%            | -39.39% |     0.46 |       67 | 56.32%     | ok               |
|          50 | 19.68%   | -51.08%            | -46.56% |     0.42 |       56 | 27.78%     | ok               |

## SOXX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 67.78%   | 73.81%             | -39.65% |     0.89 |       56 | 43.26%     | ok               |
|          30 | 63.12%   | 73.81%             | -40.14% |     0.85 |       58 | 41.10%     | ok               |
|          35 | 59.05%   | 73.81%             | -38.76% |     0.83 |       58 | 38.44%     | ok               |
|          20 | 55.11%   | 73.81%             | -38.67% |     0.77 |       61 | 44.09%     | ok               |
|          15 | 40.83%   | 73.81%             | -37.72% |     0.61 |       79 | 47.75%     | ok               |

## SPY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 3.53%    | 34.06%             | -14.25% |     0.18 |       62 | 50.75%     | ok               |
|          15 | 1.02%    | 34.06%             | -16.80% |     0.1  |       68 | 53.74%     | ok               |
|          25 | -0.71%   | 34.06%             | -14.25% |     0.04 |       60 | 49.58%     | ok               |
|          30 | -5.56%   | 34.06%             | -15.53% |    -0.13 |       63 | 47.09%     | ok               |
|          35 | -6.48%   | 34.06%             | -15.58% |    -0.18 |       61 | 43.93%     | ok               |

## SUSHI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -29.70%  | -75.14%            | -43.52% |    -0.34 |       60 | 17.62%     | ok               |
|          15 | -57.32%  | -75.14%            | -78.02% |    -0.47 |       83 | 54.41%     | ok               |
|          20 | -56.44%  | -75.14%            | -77.38% |    -0.51 |       84 | 50.77%     | ok               |
|          45 | -43.32%  | -75.14%            | -58.64% |    -0.54 |       64 | 24.14%     | ok               |
|          35 | -52.31%  | -75.14%            | -71.77% |    -0.58 |       77 | 37.74%     | ok               |

## T Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 66.55%   | 18.88%             | -15.08% |     1.06 |       71 | 66.39%     | ok               |
|          25 | 62.97%   | 18.88%             | -17.66% |     1.06 |       66 | 59.57%     | ok               |
|          20 | 62.44%   | 18.88%             | -18.13% |     1.04 |       66 | 61.90%     | ok               |
|          30 | 52.21%   | 18.88%             | -17.01% |     0.94 |       68 | 57.57%     | ok               |
|          35 | 34.31%   | 18.88%             | -14.49% |     0.71 |       76 | 52.91%     | ok               |

## TGT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -10.00%  | 8.73%              | -32.83% |    -0.14 |       60 | 37.60%     | ok               |
|          25 | -11.88%  | 8.73%              | -34.56% |    -0.17 |       68 | 40.77%     | ok               |
|          20 | -14.84%  | 8.73%              | -36.83% |    -0.2  |       86 | 45.26%     | ok               |
|          45 | -13.37%  | 8.73%              | -26.12% |    -0.27 |       50 | 29.12%     | ok               |
|          15 | -20.71%  | 8.73%              | -36.27% |    -0.32 |       72 | 50.08%     | ok               |

## TIA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -31.95%  | -79.87%            | -66.94% |     0.07 |       93 | 60.54%     | ok               |
|          20 | -37.55%  | -79.87%            | -68.67% |    -0.04 |       87 | 54.60%     | ok               |
|          25 | -35.64%  | -79.87%            | -69.36% |    -0.04 |       90 | 49.43%     | ok               |
|          35 | -27.70%  | -79.87%            | -65.55% |    -0.05 |       76 | 37.93%     | ok               |
|          30 | -43.74%  | -79.87%            | -74.75% |    -0.18 |       85 | 44.25%     | ok               |

## TLT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -7.83%   | -14.94%            | -12.51% |    -0.87 |       32 | 16.81%     | ok               |
|          40 | -13.27%  | -14.94%            | -17.65% |    -1.17 |       50 | 25.29%     | ok               |
|          45 | -12.18%  | -14.94%            | -15.17% |    -1.27 |       44 | 20.30%     | ok               |
|          30 | -20.81%  | -14.94%            | -22.01% |    -1.57 |       68 | 34.78%     | ok               |
|          35 | -19.83%  | -14.94%            | -21.03% |    -1.66 |       68 | 29.78%     | ok               |

## TMO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 45.90%   | 24.69%             | -8.17%  |     0.99 |       50 | 35.11%     | ok               |
|          45 | 44.88%   | 24.69%             | -9.69%  |     0.93 |       54 | 40.10%     | ok               |
|          40 | 37.94%   | 24.69%             | -11.54% |     0.8  |       59 | 45.26%     | ok               |
|          35 | 40.76%   | 24.69%             | -13.84% |     0.79 |       67 | 50.58%     | ok               |
|          20 | 41.41%   | 24.69%             | -22.89% |     0.75 |       75 | 62.40%     | ok               |

## TMUS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -5.89%   | -5.37%             | -41.04% |    -0.01 |       68 | 58.90%     | ok               |
|          30 | -7.16%   | -5.37%             | -33.05% |    -0.06 |       74 | 46.09%     | ok               |
|          25 | -9.79%   | -5.37%             | -39.29% |    -0.1  |       75 | 49.08%     | ok               |
|          20 | -11.32%  | -5.37%             | -39.79% |    -0.13 |       74 | 53.24%     | ok               |
|          50 | -10.15%  | -5.37%             | -32.38% |    -0.22 |       58 | 31.95%     | ok               |

## TRX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 20.50%   | 12.79%             | -18.79% |     0.69 |       52 | 39.27%     | ok               |
|          50 | 11.25%   | 12.79%             | -22.22% |     0.44 |       46 | 33.33%     | ok               |
|          35 | 12.34%   | 12.79%             | -21.77% |     0.44 |       60 | 46.36%     | ok               |
|          45 | 10.84%   | 12.79%             | -24.19% |     0.43 |       48 | 35.44%     | ok               |
|          30 | 11.17%   | 12.79%             | -22.90% |     0.4  |       60 | 48.85%     | ok               |

## TSLA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 47.27%   | 92.54%             | -30.57% |     0.66 |       62 | 29.95%     | ok               |
|          40 | 17.75%   | 92.54%             | -50.11% |     0.37 |       61 | 35.27%     | ok               |
|          45 | -6.85%   | 92.54%             | -52.01% |     0.11 |       67 | 32.45%     | ok               |
|          35 | -21.05%  | 92.54%             | -58.86% |    -0.04 |       72 | 37.60%     | ok               |
|          25 | -34.29%  | 92.54%             | -54.86% |    -0.21 |       70 | 44.59%     | ok               |

## TXN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -3.96%   | 52.95%             | -43.95% |     0.06 |       70 | 31.78%     | ok               |
|          35 | -17.67%  | 52.95%             | -42.08% |    -0.15 |       84 | 45.42%     | ok               |
|          20 | -23.53%  | 52.95%             | -37.19% |    -0.19 |       74 | 55.24%     | ok               |
|          15 | -25.27%  | 52.95%             | -38.02% |    -0.21 |       79 | 59.57%     | ok               |
|          40 | -22.70%  | 52.95%             | -44.52% |    -0.25 |       78 | 42.93%     | ok               |

## UNH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 38.77%   | -19.89%            | -26.31% |     0.61 |       75 | 48.42%     | ok               |
|          35 | 34.36%   | -19.89%            | -27.21% |     0.57 |       70 | 43.43%     | ok               |
|          50 | 31.84%   | -19.89%            | -36.71% |     0.56 |       50 | 29.78%     | ok               |
|          15 | 33.66%   | -19.89%            | -26.07% |     0.54 |       82 | 63.56%     | ok               |
|          20 | 31.22%   | -19.89%            | -26.96% |     0.52 |       77 | 57.24%     | ok               |

## UNI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 126.25%  | -27.35%            | -22.21% |     1.11 |       50 | 25.86%     | ok               |
|          45 | 108.22%  | -27.35%            | -30.17% |     0.98 |       58 | 33.52%     | ok               |
|          40 | 81.12%   | -27.35%            | -43.84% |     0.82 |       62 | 39.85%     | ok               |
|          35 | 66.37%   | -27.35%            | -48.64% |     0.73 |       64 | 45.02%     | ok               |
|          30 | 5.39%    | -27.35%            | -60.31% |     0.33 |       80 | 49.81%     | ok               |

## UPS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -16.76%  | -18.79%            | -24.11% |    -0.31 |       44 | 25.29%     | ok               |
|          40 | -18.69%  | -18.79%            | -25.98% |    -0.31 |       60 | 34.78%     | ok               |
|          20 | -26.32%  | -18.79%            | -33.47% |    -0.41 |       78 | 50.92%     | ok               |
|          15 | -28.74%  | -18.79%            | -35.66% |    -0.46 |       80 | 54.41%     | ok               |
|          25 | -30.03%  | -18.79%            | -36.37% |    -0.51 |       71 | 47.75%     | ok               |

## USO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 7.64%    | 75.48%             | -37.66% |     0.25 |       67 | 42.43%     | ok               |
|          20 | 6.10%    | 75.48%             | -40.99% |     0.23 |       73 | 38.77%     | ok               |
|          45 | 2.63%    | 75.48%             | -33.97% |     0.18 |       48 | 25.96%     | ok               |
|          25 | -5.57%   | 75.48%             | -42.17% |     0.07 |       71 | 36.11%     | ok               |
|          50 | -4.45%   | 75.48%             | -28.71% |     0.06 |       50 | 24.13%     | ok               |

## VEA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 2.17%    | 36.51%             | -17.27% |     0.14 |       58 | 49.92%     | ok               |
|          20 | -1.45%   | 36.51%             | -17.78% |    -0    |       59 | 47.42%     | ok               |
|          25 | -5.88%   | 36.51%             | -18.46% |    -0.19 |       59 | 45.26%     | ok               |
|          30 | -7.02%   | 36.51%             | -18.84% |    -0.25 |       64 | 41.26%     | ok               |
|          35 | -7.67%   | 36.51%             | -17.88% |    -0.29 |       50 | 38.77%     | ok               |

## VIXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -54.55%  | -50.82%            | -69.78% |    -0.63 |       34 | 8.65%      | ok               |
|          45 | -64.29%  | -50.82%            | -75.03% |    -0.84 |       54 | 13.64%     | ok               |
|          40 | -73.26%  | -50.82%            | -81.61% |    -1.01 |       70 | 17.80%     | ok               |
|          35 | -80.39%  | -50.82%            | -85.57% |    -1.17 |       96 | 24.63%     | ok               |
|          30 | -84.50%  | -50.82%            | -91.45% |    -1.18 |       98 | 31.78%     | ok               |

## VNQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -8.13%   | 12.79%             | -22.16% |    -0.27 |       69 | 43.43%     | ok               |
|          45 | -8.46%   | 12.79%             | -19.07% |    -0.35 |       60 | 28.62%     | ok               |
|          50 | -8.43%   | 12.79%             | -17.13% |    -0.37 |       50 | 25.46%     | ok               |
|          30 | -12.05%  | 12.79%             | -24.92% |    -0.45 |       71 | 40.43%     | ok               |
|          20 | -12.82%  | 12.79%             | -23.83% |    -0.46 |       74 | 46.09%     | ok               |

## VTI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 5.32%    | 33.71%             | -13.96% |     0.23 |       63 | 51.08%     | ok               |
|          15 | -2.38%   | 33.71%             | -15.70% |    -0.01 |       64 | 53.91%     | ok               |
|          25 | -5.13%   | 33.71%             | -15.00% |    -0.11 |       57 | 49.08%     | ok               |
|          40 | -9.30%   | 33.71%             | -19.77% |    -0.32 |       70 | 39.43%     | ok               |
|          35 | -11.29%  | 33.71%             | -20.22% |    -0.39 |       64 | 43.76%     | ok               |

## VWO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -8.00%   | 24.40%             | -24.01% |    -0.21 |       74 | 47.59%     | ok               |
|          20 | -8.02%   | 24.40%             | -26.14% |    -0.22 |       69 | 45.59%     | ok               |
|          50 | -8.00%   | 24.40%             | -21.68% |    -0.27 |       56 | 29.78%     | ok               |
|          45 | -9.79%   | 24.40%             | -23.75% |    -0.34 |       58 | 32.28%     | ok               |
|          40 | -10.07%  | 24.40%             | -23.57% |    -0.34 |       68 | 35.27%     | ok               |

## VZ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -2.64%   | 12.52%             | -12.55% |    -0.02 |       56 | 28.45%     | ok               |
|          20 | -22.26%  | 12.52%             | -35.02% |    -0.43 |       80 | 52.75%     | ok               |
|          25 | -19.09%  | 12.52%             | -26.32% |    -0.47 |       83 | 47.75%     | ok               |
|          35 | -18.88%  | 12.52%             | -26.97% |    -0.55 |       64 | 39.10%     | ok               |
|          45 | -18.61%  | 12.52%             | -26.23% |    -0.57 |       72 | 32.95%     | ok               |

## WFC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -8.35%   | 44.01%             | -24.87% |    -0.11 |       75 | 43.43%     | ok               |
|          50 | -8.91%   | 44.01%             | -20.06% |    -0.22 |       58 | 32.61%     | ok               |
|          40 | -14.02%  | 44.01%             | -25.21% |    -0.34 |       70 | 40.10%     | ok               |
|          30 | -19.98%  | 44.01%             | -30.92% |    -0.35 |       80 | 46.76%     | ok               |
|          20 | -22.39%  | 44.01%             | -32.30% |    -0.36 |       80 | 52.91%     | ok               |

## WIF-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 65.48%   | -84.17%            | -40.67% |     0.7  |       67 | 50.38%     | ok               |
|          15 | 29.32%   | -84.17%            | -46.21% |     0.5  |       77 | 53.64%     | ok               |
|          25 | 29.01%   | -84.17%            | -44.74% |     0.49 |       65 | 46.55%     | ok               |
|          30 | 1.52%    | -84.17%            | -52.76% |     0.29 |       66 | 43.87%     | ok               |
|          35 | -5.41%   | -84.17%            | -56.62% |     0.18 |       64 | 37.74%     | ok               |

## WMT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 37.97%   | 87.86%             | -12.87% |     1.1  |       36 | 35.77%     | ok               |
|          45 | 36.95%   | 87.86%             | -14.82% |     1.04 |       42 | 38.27%     | ok               |
|          35 | 28.86%   | 87.86%             | -18.90% |     0.8  |       58 | 45.26%     | ok               |
|          40 | 25.32%   | 87.86%             | -19.17% |     0.74 |       50 | 39.93%     | ok               |
|          15 | 9.95%    | 87.86%             | -26.82% |     0.31 |       82 | 59.23%     | ok               |

## XBI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 13.75%   | 56.45%             | -16.08% |     0.41 |       50 | 33.44%     | ok               |
|          45 | 9.43%    | 56.45%             | -15.46% |     0.32 |       48 | 30.95%     | ok               |
|          35 | 2.78%    | 56.45%             | -17.66% |     0.15 |       58 | 36.27%     | ok               |
|          30 | 0.63%    | 56.45%             | -17.66% |     0.1  |       60 | 37.77%     | ok               |
|          50 | 0.20%    | 56.45%             | -15.41% |     0.08 |       48 | 27.95%     | ok               |

## XLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 0.79%    | 15.10%             | -17.29% |     0.09 |       54 | 29.12%     | ok               |
|          50 | -0.40%   | 15.10%             | -16.47% |     0.04 |       40 | 24.63%     | ok               |
|          35 | -3.11%   | 15.10%             | -20.65% |    -0.06 |       54 | 32.45%     | ok               |
|          45 | -3.38%   | 15.10%             | -18.17% |    -0.08 |       42 | 26.46%     | ok               |
|          25 | -7.94%   | 15.10%             | -21.62% |    -0.22 |       62 | 38.60%     | ok               |

## XLC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 3.14%    | 21.76%             | -12.33% |     0.17 |       61 | 48.75%     | ok               |
|          50 | 0.67%    | 21.76%             | -12.48% |     0.08 |       64 | 36.77%     | ok               |
|          25 | -0.22%   | 21.76%             | -12.31% |     0.06 |       64 | 51.25%     | ok               |
|          40 | -1.27%   | 21.76%             | -13.38% |     0.01 |       62 | 42.43%     | ok               |
|          35 | -1.94%   | 21.76%             | -13.38% |    -0.01 |       60 | 46.26%     | ok               |

## XLE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.76%   | 39.56%             | -25.98% |     0.06 |       58 | 38.60%     | ok               |
|          45 | -2.44%   | 39.56%             | -28.46% |     0.01 |       60 | 41.10%     | ok               |
|          30 | -8.02%   | 39.56%             | -34.77% |    -0.13 |       72 | 47.59%     | ok               |
|          20 | -10.21%  | 39.56%             | -33.39% |    -0.15 |       80 | 52.58%     | ok               |
|          15 | -11.37%  | 39.56%             | -35.59% |    -0.17 |       96 | 56.57%     | ok               |

## XLF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 4.44%    | 39.30%             | -20.19% |     0.2  |       70 | 57.40%     | ok               |
|          20 | 3.80%    | 39.30%             | -18.63% |     0.18 |       70 | 54.74%     | ok               |
|          25 | -3.44%   | 39.30%             | -23.22% |    -0.05 |       77 | 51.58%     | ok               |
|          30 | -4.07%   | 39.30%             | -23.61% |    -0.08 |       78 | 49.58%     | ok               |
|          35 | -11.93%  | 39.30%             | -24.48% |    -0.4  |       70 | 46.09%     | ok               |

## XLI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 5.38%    | 35.24%             | -11.06% |     0.24 |       85 | 51.58%     | ok               |
|          20 | 0.03%    | 35.24%             | -12.74% |     0.06 |       77 | 46.59%     | ok               |
|          25 | -8.77%   | 35.24%             | -17.60% |    -0.29 |       78 | 44.43%     | ok               |
|          45 | -7.67%   | 35.24%             | -16.29% |    -0.31 |       72 | 33.11%     | ok               |
|          30 | -9.35%   | 35.24%             | -18.27% |    -0.32 |       82 | 42.76%     | ok               |

## XLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 51.83%   | 44.25%             | -18.51% |     0.91 |       54 | 50.75%     | ok               |
|          25 | 43.82%   | 44.25%             | -15.06% |     0.87 |       44 | 45.26%     | ok               |
|          20 | 44.38%   | 44.25%             | -19.61% |     0.85 |       54 | 47.75%     | ok               |
|          30 | 35.21%   | 44.25%             | -19.09% |     0.76 |       44 | 43.93%     | ok               |
|          35 | 17.06%   | 44.25%             | -21.79% |     0.45 |       60 | 40.93%     | ok               |

## XLM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 16.07%   | -45.42%            | -61.51% |     0.39 |       74 | 61.11%     | ok               |
|          25 | 14.75%   | -45.42%            | -53.31% |     0.37 |       77 | 52.11%     | ok               |
|          40 | 10.03%   | -45.42%            | -53.39% |     0.31 |       68 | 36.78%     | ok               |
|          45 | 9.93%    | -45.42%            | -49.94% |     0.31 |       64 | 28.54%     | ok               |
|          35 | 0.91%    | -45.42%            | -57.36% |     0.23 |       76 | 45.02%     | ok               |

## XLP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          45 | 22.19%   | 18.90%             | -5.66% |     1.08 |       48 | 33.11%     | ok               |
|          50 | 19.31%   | 18.90%             | -6.08% |     0.97 |       54 | 31.28%     | ok               |
|          40 | 19.92%   | 18.90%             | -7.32% |     0.97 |       64 | 36.44%     | ok               |
|          35 | 18.44%   | 18.90%             | -8.39% |     0.89 |       62 | 39.27%     | ok               |
|          30 | 15.02%   | 18.90%             | -8.96% |     0.73 |       63 | 41.10%     | ok               |

## XLU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 4.84%    | 26.02%             | -14.03% |     0.28 |       56 | 30.45%     | ok               |
|          45 | 3.69%    | 26.02%             | -14.97% |     0.22 |       60 | 31.61%     | ok               |
|          35 | 3.61%    | 26.02%             | -19.71% |     0.21 |       64 | 37.60%     | ok               |
|          40 | 1.17%    | 26.02%             | -16.41% |     0.1  |       70 | 34.28%     | ok               |
|          30 | -0.87%   | 26.02%             | -20.40% |     0.01 |       69 | 41.10%     | ok               |

## XLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -18.84%  | 26.99%             | -22.46% |    -0.82 |       74 | 39.43%     | ok               |
|          30 | -19.21%  | 26.99%             | -22.82% |    -0.85 |       74 | 37.77%     | ok               |
|          15 | -21.58%  | 26.99%             | -24.77% |    -0.93 |       81 | 43.43%     | ok               |
|          20 | -21.41%  | 26.99%             | -24.61% |    -0.94 |       77 | 40.93%     | ok               |
|          35 | -23.23%  | 26.99%             | -26.64% |    -1.11 |       68 | 34.78%     | ok               |

## XLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -3.36%   | 26.97%             | -16.52% |    -0.01 |       78 | 54.41%     | ok               |
|          30 | -6.72%   | 26.97%             | -18.44% |    -0.13 |       77 | 47.75%     | ok               |
|          20 | -8.48%   | 26.97%             | -20.14% |    -0.16 |       74 | 51.08%     | ok               |
|          25 | -10.52%  | 26.97%             | -21.01% |    -0.23 |       71 | 49.58%     | ok               |
|          35 | -12.11%  | 26.97%             | -20.89% |    -0.33 |       77 | 45.09%     | ok               |

## XOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 3.48%    | 45.53%             | -21.35% |     0.17 |       40 | 29.28%     | ok               |
|          25 | -0.10%   | 45.53%             | -19.90% |     0.08 |       59 | 37.27%     | ok               |
|          30 | -1.09%   | 45.53%             | -20.29% |     0.05 |       59 | 36.61%     | ok               |
|          45 | -1.68%   | 45.53%             | -23.33% |     0.03 |       44 | 30.45%     | ok               |
|          40 | -3.14%   | 45.53%             | -21.45% |    -0.01 |       54 | 33.78%     | ok               |

## XRP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 14.26%   | -54.40%            | -33.31% |     0.36 |       80 | 44.44%     | ok               |
|          40 | 4.21%    | -54.40%            | -32.16% |     0.24 |       74 | 36.78%     | ok               |
|          30 | -3.28%   | -54.40%            | -35.19% |     0.17 |       69 | 49.43%     | ok               |
|          20 | -8.00%   | -54.40%            | -37.79% |     0.12 |       74 | 55.94%     | ok               |
|          45 | -5.37%   | -54.40%            | -34.70% |     0.12 |       66 | 30.84%     | ok               |

## YFI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -41.47%  | -65.28%            | -44.76% |    -0.64 |       58 | 27.59%     | ok               |
|          30 | -48.97%  | -65.28%            | -58.28% |    -0.7  |       74 | 40.61%     | ok               |
|          35 | -47.42%  | -65.28%            | -52.87% |    -0.72 |       62 | 35.82%     | ok               |
|          25 | -51.92%  | -65.28%            | -60.71% |    -0.75 |       73 | 45.02%     | ok               |
|          15 | -59.38%  | -65.28%            | -67.95% |    -0.87 |       81 | 53.45%     | ok               |

## ZEC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 196.35%  | 2104.20%           | -30.64% |     1.07 |       46 | 28.35%     | ok               |
|          35 | 162.09%  | 2104.20%           | -50.84% |     0.97 |       52 | 34.10%     | ok               |
|          40 | 138.59%  | 2104.20%           | -54.22% |     0.91 |       52 | 32.38%     | ok               |
|          30 | 126.43%  | 2104.20%           | -56.50% |     0.87 |       54 | 36.97%     | ok               |
|          50 | 115.00%  | 2104.20%           | -41.34% |     0.85 |       42 | 24.52%     | ok               |
