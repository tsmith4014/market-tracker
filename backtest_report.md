# Market Tracker Backtest Report

_Generated: 2026-07-14T03:31:21+00:00_

## Data Sources

- Crypto: Kraken -> Coinbase -> CoinGecko OHLC -> CoinPaprika fallback chain.
- Stocks / ETFs / indices: Stooq -> Yahoo Finance fallback chain.
- Data rows are generated from real market APIs. Mock OHLCV rows are not generated.

## Data Freshness

- Rows: **92,497**
- Symbols: **161**
- Date range: **2024-02-16** to **2026-07-14**

## Latest Signals

| symbol     | date                |         close |   composite_score | signal   | data_source   |
|:-----------|:--------------------|--------------:|------------------:|:---------|:--------------|
| AAPL       | 2026-07-13 00:00:00 |   317.31      |        56.0833    | LONG     | Yahoo Finance |
| AAVE-USD   | 2026-07-14 00:00:00 |    95.56      |        41.6667    | LONG     | Kraken API    |
| ABBV       | 2026-07-13 00:00:00 |   248         |        44.6667    | LONG     | Yahoo Finance |
| AMZN       | 2026-07-13 00:00:00 |   247.31      |        67.4167    | LONG     | Yahoo Finance |
| ARB-USD    | 2026-07-14 00:00:00 |     0.0892    |        46.6667    | LONG     | Kraken API    |
| BAC        | 2026-07-13 00:00:00 |    59.5       |        36.0833    | LONG     | Yahoo Finance |
| C          | 2026-07-13 00:00:00 |   140.71      |        36.4167    | LONG     | Yahoo Finance |
| CL         | 2026-07-13 00:00:00 |    93.21      |        64.0833    | LONG     | Yahoo Finance |
| CMCSA      | 2026-07-13 00:00:00 |    23.97      |        31.9167    | LONG     | Yahoo Finance |
| COP        | 2026-07-13 00:00:00 |   112.85      |        53.6667    | LONG     | Yahoo Finance |
| CSCO       | 2026-07-13 00:00:00 |   119.25      |        30.5833    | LONG     | Yahoo Finance |
| CVX        | 2026-07-13 00:00:00 |   182.2       |        71.6667    | LONG     | Yahoo Finance |
| DBC        | 2026-07-13 00:00:00 |    28.33      |        69.9167    | LONG     | Yahoo Finance |
| DXY-INDEX  | 2026-07-13 00:00:00 |   101.201     |        64.2473    | LONG     | Yahoo Finance |
| EOG        | 2026-07-13 00:00:00 |   139.61      |        66.1667    | LONG     | Yahoo Finance |
| IBM        | 2026-07-13 00:00:00 |   290.23      |        58         | LONG     | Yahoo Finance |
| JNJ        | 2026-07-13 00:00:00 |   257.77      |        56.3333    | LONG     | Yahoo Finance |
| JPM        | 2026-07-13 00:00:00 |   334.53      |        33.5833    | LONG     | Yahoo Finance |
| LDO-USD    | 2026-07-14 00:00:00 |     0.311     |        47         | LONG     | Kraken API    |
| MPC        | 2026-07-13 00:00:00 |   296.88      |        71.25      | LONG     | Yahoo Finance |
| MRK        | 2026-07-13 00:00:00 |   124.03      |        61.8333    | LONG     | Yahoo Finance |
| NOW        | 2026-07-13 00:00:00 |   111.26      |        35         | LONG     | Yahoo Finance |
| NVDA       | 2026-07-13 00:00:00 |   203.53      |        16.8333    | LONG     | Yahoo Finance |
| OXY        | 2026-07-13 00:00:00 |    54.81      |        71.6667    | LONG     | Yahoo Finance |
| POL-USD    | 2026-07-14 00:00:00 |     0.08282   |        51         | LONG     | Kraken API    |
| RTX        | 2026-07-13 00:00:00 |   196.39      |        61.75      | LONG     | Yahoo Finance |
| SBUX       | 2026-07-13 00:00:00 |   107.34      |        71.25      | LONG     | Yahoo Finance |
| SCHW       | 2026-07-13 00:00:00 |   102.38      |        58         | LONG     | Yahoo Finance |
| SPY        | 2026-07-13 00:00:00 |   749.17      |        48.4167    | LONG     | Yahoo Finance |
| SUSHI-USD  | 2026-07-14 00:00:00 |     0.1652    |        30.1667    | LONG     | Kraken API    |
| TMO        | 2026-07-13 00:00:00 |   528.51      |        65.5       | LONG     | Yahoo Finance |
| UNH        | 2026-07-13 00:00:00 |   429.09      |        55.75      | LONG     | Yahoo Finance |
| UNI-USD    | 2026-07-14 00:00:00 |     3.5592    |        47         | LONG     | Kraken API    |
| USO        | 2026-07-13 00:00:00 |   117.79      |        57.1667    | LONG     | Yahoo Finance |
| WFC        | 2026-07-13 00:00:00 |    87.67      |        54.8333    | LONG     | Yahoo Finance |
| XBI        | 2026-07-13 00:00:00 |   155.34      |        67.4167    | LONG     | Yahoo Finance |
| XLE        | 2026-07-13 00:00:00 |    56.74      |        69.9167    | LONG     | Yahoo Finance |
| XLF        | 2026-07-13 00:00:00 |    56.07      |        62.5833    | LONG     | Yahoo Finance |
| XLU        | 2026-07-13 00:00:00 |    45.72      |        55.5833    | LONG     | Yahoo Finance |
| XLV        | 2026-07-13 00:00:00 |   161.41      |        63.75      | LONG     | Yahoo Finance |
| XOM        | 2026-07-13 00:00:00 |   144.51      |        53.6667    | LONG     | Yahoo Finance |
| YFI-USD    | 2026-07-14 00:00:00 |  2134.1       |        42.9167    | LONG     | Kraken API    |
| ZEC-USD    | 2026-07-14 00:00:00 |   498.43      |        61.3333    | LONG     | Kraken API    |
| ADA-USD    | 2026-07-14 00:00:00 |     0.156369  |       -12.8333    | NEUTRAL  | Kraken API    |
| ADBE       | 2026-07-13 00:00:00 |   230.61      |        19.5833    | NEUTRAL  | Yahoo Finance |
| ALGO-USD   | 2026-07-14 00:00:00 |     0.08305   |       -21.5833    | NEUTRAL  | Kraken API    |
| AMAT       | 2026-07-13 00:00:00 |   575.39      |         7.91667   | NEUTRAL  | Yahoo Finance |
| AMD        | 2026-07-13 00:00:00 |   534.39      |        22.6667    | NEUTRAL  | Yahoo Finance |
| AMGN       | 2026-07-13 00:00:00 |   360.45      |        36.3333    | NEUTRAL  | Yahoo Finance |
| APT-USD    | 2026-07-14 00:00:00 |     0.5926    |       -14.25      | NEUTRAL  | Kraken API    |
| ARKK       | 2026-07-13 00:00:00 |    78.24      |        10.4167    | NEUTRAL  | Yahoo Finance |
| ATOM-USD   | 2026-07-14 00:00:00 |     1.5222    |       -10.3333    | NEUTRAL  | Kraken API    |
| AVAX-USD   | 2026-07-14 00:00:00 |     6.419     |       -11.3333    | NEUTRAL  | Kraken API    |
| AVGO       | 2026-07-13 00:00:00 |   384.05      |        -4.66667   | NEUTRAL  | Yahoo Finance |
| BA         | 2026-07-13 00:00:00 |   215.51      |       -59.0833    | NEUTRAL  | Yahoo Finance |
| BCH-USD    | 2026-07-14 00:00:00 |   231.98      |         7.33333   | NEUTRAL  | Kraken API    |
| BITO       | 2026-07-13 00:00:00 |     8.44      |       -46.6667    | NEUTRAL  | Yahoo Finance |
| BLK        | 2026-07-13 00:00:00 |  1031.56      |        -6.25      | NEUTRAL  | Yahoo Finance |
| BONK-USD   | 2026-07-14 00:00:00 |     3.664e-06 |       -52.9167    | NEUTRAL  | Kraken API    |
| BTC-USD    | 2026-07-14 00:00:00 | 62310.9       |        -1.58333   | NEUTRAL  | Kraken API    |
| CAT        | 2026-07-13 00:00:00 |   931.47      |        -8.08333   | NEUTRAL  | Yahoo Finance |
| COMP-USD   | 2026-07-14 00:00:00 |    16.43      |         9.66667   | NEUTRAL  | Kraken API    |
| COST       | 2026-07-13 00:00:00 |   926.43      |       -51.3333    | NEUTRAL  | Yahoo Finance |
| CRM        | 2026-07-13 00:00:00 |   171.22      |         1.58333   | NEUTRAL  | Yahoo Finance |
| CRV-USD    | 2026-07-14 00:00:00 |     0.21106   |        11.0833    | NEUTRAL  | Kraken API    |
| DASH-USD   | 2026-07-14 00:00:00 |    32.474     |       -46.75      | NEUTRAL  | Kraken API    |
| DE         | 2026-07-13 00:00:00 |   585.64      |         9.66667   | NEUTRAL  | Yahoo Finance |
| DIA        | 2026-07-13 00:00:00 |   524.47      |        31.8333    | NEUTRAL  | Yahoo Finance |
| DIS        | 2026-07-13 00:00:00 |    96         |       -69         | NEUTRAL  | Yahoo Finance |
| DOGE-USD   | 2026-07-14 00:00:00 |     0.0714529 |       -17         | NEUTRAL  | Kraken API    |
| DOT-USD    | 2026-07-14 00:00:00 |     0.827     |         6.16667   | NEUTRAL  | Kraken API    |
| EEM        | 2026-07-13 00:00:00 |    64.5       |       -17.75      | NEUTRAL  | Yahoo Finance |
| EFA        | 2026-07-13 00:00:00 |   103.24      |       -16.6667    | NEUTRAL  | Yahoo Finance |
| ETC-USD    | 2026-07-14 00:00:00 |     6.851     |       -32.5833    | NEUTRAL  | Kraken API    |
| ETH-USD    | 2026-07-14 00:00:00 |  1774.57      |        31         | NEUTRAL  | Kraken API    |
| EWJ        | 2026-07-13 00:00:00 |    92.72      |        -2.33333   | NEUTRAL  | Yahoo Finance |
| FCX        | 2026-07-13 00:00:00 |    59.97      |       -21.4167    | NEUTRAL  | Yahoo Finance |
| FIL-USD    | 2026-07-14 00:00:00 |     0.753     |        -5.08333   | NEUTRAL  | Kraken API    |
| FXI        | 2026-07-13 00:00:00 |    33.44      |        -4.83333   | NEUTRAL  | Yahoo Finance |
| GDX        | 2026-07-13 00:00:00 |    73.37      |       -54.5       | NEUTRAL  | Yahoo Finance |
| GDXJ       | 2026-07-13 00:00:00 |    95.4       |       -54.5       | NEUTRAL  | Yahoo Finance |
| GE         | 2026-07-13 00:00:00 |   353.42      |        -2.08333   | NEUTRAL  | Yahoo Finance |
| GOOGL      | 2026-07-13 00:00:00 |   352.51      |       -13.0833    | NEUTRAL  | Yahoo Finance |
| GRT-USD    | 2026-07-14 00:00:00 |     0.01724   |       -28.25      | NEUTRAL  | Kraken API    |
| GS         | 2026-07-13 00:00:00 |  1045.91      |        22.6667    | NEUTRAL  | Yahoo Finance |
| HD         | 2026-07-13 00:00:00 |   337.11      |        -9.5       | NEUTRAL  | Yahoo Finance |
| HON        | 2026-07-13 00:00:00 |   222.25      |       -45         | NEUTRAL  | Yahoo Finance |
| HYG        | 2026-07-13 00:00:00 |    79.52      |       -58.75      | NEUTRAL  | Yahoo Finance |
| IBIT       | 2026-07-13 00:00:00 |    35.22      |       -43.1667    | NEUTRAL  | Yahoo Finance |
| ICP-USD    | 2026-07-14 00:00:00 |     2.168     |       -15.75      | NEUTRAL  | Kraken API    |
| IEF        | 2026-07-13 00:00:00 |    93.29      |       -61         | NEUTRAL  | Yahoo Finance |
| IEMG       | 2026-07-13 00:00:00 |    78.49      |       -17.75      | NEUTRAL  | Yahoo Finance |
| INJ-USD    | 2026-07-14 00:00:00 |     4.742     |       -10.5       | NEUTRAL  | Kraken API    |
| INTC       | 2026-07-13 00:00:00 |   103.12      |       -40.3333    | NEUTRAL  | Yahoo Finance |
| INTU       | 2026-07-13 00:00:00 |   289.76      |        -6.33333   | NEUTRAL  | Yahoo Finance |
| ITA        | 2026-07-13 00:00:00 |   235.05      |        -0.0833333 | NEUTRAL  | Yahoo Finance |
| IWM        | 2026-07-13 00:00:00 |   293.48      |        -0.333333  | NEUTRAL  | Yahoo Finance |
| KO         | 2026-07-13 00:00:00 |    84.25      |        63.3333    | NEUTRAL  | Yahoo Finance |
| LIN        | 2026-07-13 00:00:00 |   524.06      |        44.8333    | NEUTRAL  | Yahoo Finance |
| LINK-USD   | 2026-07-14 00:00:00 |     7.86842   |        16.4167    | NEUTRAL  | Kraken API    |
| LLY        | 2026-07-13 00:00:00 |  1181.87      |        35.0833    | NEUTRAL  | Yahoo Finance |
| LRCX       | 2026-07-13 00:00:00 |   329.92      |       -21.3333    | NEUTRAL  | Yahoo Finance |
| LTC-USD    | 2026-07-14 00:00:00 |    43.43      |         8         | NEUTRAL  | Kraken API    |
| MCD        | 2026-07-13 00:00:00 |   272.61      |       -21.3333    | NEUTRAL  | Yahoo Finance |
| META       | 2026-07-13 00:00:00 |   656.73      |        51.3333    | NEUTRAL  | Yahoo Finance |
| MS         | 2026-07-13 00:00:00 |   221.09      |        26.6667    | NEUTRAL  | Yahoo Finance |
| MSFT       | 2026-07-13 00:00:00 |   390.99      |         4.91667   | NEUTRAL  | Yahoo Finance |
| MU         | 2026-07-13 00:00:00 |   937         |       -12.3333    | NEUTRAL  | Yahoo Finance |
| NEAR-USD   | 2026-07-14 00:00:00 |     1.9436    |        20.1667    | NEUTRAL  | Kraken API    |
| NEM        | 2026-07-13 00:00:00 |    93.1       |       -54.5       | NEUTRAL  | Yahoo Finance |
| NFLX       | 2026-07-13 00:00:00 |    73.83      |       -19.0833    | NEUTRAL  | Yahoo Finance |
| NKE        | 2026-07-13 00:00:00 |    43.76      |        -9.08333   | NEUTRAL  | Yahoo Finance |
| OP-USD     | 2026-07-14 00:00:00 |     0.0983    |       -22.0833    | NEUTRAL  | Kraken API    |
| PEP        | 2026-07-13 00:00:00 |   138.49      |       -64.8333    | NEUTRAL  | Yahoo Finance |
| PEPE-USD   | 2026-07-14 00:00:00 |     2.705e-06 |        23.6667    | NEUTRAL  | Kraken API    |
| PG         | 2026-07-13 00:00:00 |   148.37      |       -11         | NEUTRAL  | Yahoo Finance |
| PM         | 2026-07-13 00:00:00 |   180.19      |        24.25      | NEUTRAL  | Yahoo Finance |
| QCOM       | 2026-07-13 00:00:00 |   183.98      |       -32.5833    | NEUTRAL  | Yahoo Finance |
| QQQ        | 2026-07-13 00:00:00 |   711.74      |        -4.33333   | NEUTRAL  | Yahoo Finance |
| RENDER-USD | 2026-07-14 00:00:00 |     1.478     |       -43.25      | NEUTRAL  | Kraken API    |
| SHIB-USD   | 2026-07-14 00:00:00 |     4.13e-06  |       -20.9167    | NEUTRAL  | Kraken API    |
| SHY        | 2026-07-13 00:00:00 |    81.79      |       -58.75      | NEUTRAL  | Yahoo Finance |
| SKY-USD    | 2026-07-14 00:00:00 |     0.05934   |        12.3333    | NEUTRAL  | Kraken API    |
| SLB        | 2026-07-13 00:00:00 |    47.36      |        -6.25      | NEUTRAL  | Yahoo Finance |
| SMH        | 2026-07-13 00:00:00 |   585.62      |        -6.33333   | NEUTRAL  | Yahoo Finance |
| SNX-USD    | 2026-07-14 00:00:00 |     0.2306    |        14.4167    | NEUTRAL  | Kraken API    |
| SOL-USD    | 2026-07-14 00:00:00 |    74.65      |       -12.8333    | NEUTRAL  | Kraken API    |
| SOXX       | 2026-07-13 00:00:00 |   553.61      |        -6.33333   | NEUTRAL  | Yahoo Finance |
| TGT        | 2026-07-13 00:00:00 |   134.77      |        44.5       | NEUTRAL  | Yahoo Finance |
| TIA-USD    | 2026-07-14 00:00:00 |     0.4007    |        44.8333    | NEUTRAL  | Kraken API    |
| TMUS       | 2026-07-13 00:00:00 |   188.41      |        20.1667    | NEUTRAL  | Yahoo Finance |
| TRX-USD    | 2026-07-14 00:00:00 |     0.324522  |        28.8333    | NEUTRAL  | Kraken API    |
| TSLA       | 2026-07-13 00:00:00 |   394.76      |       -44.9167    | NEUTRAL  | Yahoo Finance |
| TXN        | 2026-07-13 00:00:00 |   298.57      |        -6.33333   | NEUTRAL  | Yahoo Finance |
| UPS        | 2026-07-13 00:00:00 |   112.89      |        67.3333    | NEUTRAL  | Yahoo Finance |
| VEA        | 2026-07-13 00:00:00 |    69.76      |       -25         | NEUTRAL  | Yahoo Finance |
| VIXY       | 2026-07-13 00:00:00 |    21.02      |       -25.6667    | NEUTRAL  | Yahoo Finance |
| VNQ        | 2026-07-13 00:00:00 |    97.83      |        39.5       | NEUTRAL  | Yahoo Finance |
| VTI        | 2026-07-13 00:00:00 |   369.78      |        55.1667    | NEUTRAL  | Yahoo Finance |
| WIF-USD    | 2026-07-14 00:00:00 |     0.1529    |       -48.5833    | NEUTRAL  | Kraken API    |
| XLB        | 2026-07-13 00:00:00 |    50.58      |       -24.8333    | NEUTRAL  | Yahoo Finance |
| XLC        | 2026-07-13 00:00:00 |   111.59      |         8.16667   | NEUTRAL  | Yahoo Finance |
| XLI        | 2026-07-13 00:00:00 |   180.37      |         6.66667   | NEUTRAL  | Yahoo Finance |
| XLK        | 2026-07-13 00:00:00 |   181.28      |        -4.33333   | NEUTRAL  | Yahoo Finance |
| XLM-USD    | 2026-07-14 00:00:00 |     0.178007  |       -37.75      | NEUTRAL  | Kraken API    |
| XLP        | 2026-07-13 00:00:00 |    84.59      |        58.3333    | NEUTRAL  | Yahoo Finance |
| XLY        | 2026-07-13 00:00:00 |   116.04      |        -3.5       | NEUTRAL  | Yahoo Finance |
| XRP-USD    | 2026-07-14 00:00:00 |     1.06058   |        -5.08333   | NEUTRAL  | Kraken API    |
| AGG        | 2026-07-13 00:00:00 |    97.71      |       -49.75      | SHORT    | Yahoo Finance |
| BND        | 2026-07-13 00:00:00 |    72.5       |       -49.75      | SHORT    | Yahoo Finance |
| FET-USD    | 2026-07-14 00:00:00 |     0.1593    |       -32         | SHORT    | Kraken API    |
| GLD        | 2026-07-13 00:00:00 |   367.13      |       -35.4167    | SHORT    | Yahoo Finance |
| HBAR-USD   | 2026-07-14 00:00:00 |     0.06573   |       -32         | SHORT    | Kraken API    |
| ORCL       | 2026-07-13 00:00:00 |   131.54      |       -65.6667    | SHORT    | Yahoo Finance |
| PFE        | 2026-07-13 00:00:00 |    24.48      |       -35.25      | SHORT    | Yahoo Finance |
| SLV        | 2026-07-13 00:00:00 |    52.16      |       -37.4167    | SHORT    | Yahoo Finance |
| T          | 2026-07-13 00:00:00 |    21.55      |       -35.25      | SHORT    | Yahoo Finance |
| TLT        | 2026-07-13 00:00:00 |    83.97      |       -55.0833    | SHORT    | Yahoo Finance |
| VWO        | 2026-07-13 00:00:00 |    58.79      |       -31.75      | SHORT    | Yahoo Finance |
| VZ         | 2026-07-13 00:00:00 |    42.68      |       -36.75      | SHORT    | Yahoo Finance |
| WMT        | 2026-07-13 00:00:00 |   114.78      |       -36.5       | SHORT    | Yahoo Finance |

## Edge Summary

- Symbols with trades: **160** of 160
- Beat buy-and-hold: **32.50%** of traded symbols
- Positive return: **31.25%** of traded symbols
- Median strategy return: **-10.88%** (benchmark **17.64%**)
- Median excess vs benchmark: **-28.41%**
- Median Sharpe: **-0.12**
- Median exposure: **44.26%**

> Edge is real only if both _beat buy-and-hold_ and _median excess_ are convincingly positive across many symbols. Treat a single high-return symbol as noise.

## Portfolio Backtest

Actual capital-allocation books (not per-symbol averages). Benchmarks: `equal_weight_buyhold` (whole tracked universe), `spy_buyhold` (100% SPY), and `sixty_forty` (60% SPY / 40% AGG). `high_conf_voltarget` inverse-vol-weights the HIGH-confidence book; `conviction_long_short` is market-neutral. Judge on **Sharpe** and **max_drawdown** out-of-sample, not raw return: a fully-invested long book wins on return in a bull market but carries all the risk.

| strategy              | scope         | ann_return   | ann_vol   |   sharpe | max_drawdown   | total_return   |   avg_gross_exposure |
|:----------------------|:--------------|:-------------|:----------|---------:|:---------------|:---------------|---------------------:|
| equal_weight_buyhold  | full          | -3.38%       | 32.48%    |    -0.1  | -47.00%        | -23.31%        |                 1    |
| equal_weight_buyhold  | out_of_sample | -21.32%      | 31.14%    |    -0.68 | -39.63%        | -24.39%        |                 1    |
| all_signals_ew        | full          | -18.76%      | 27.26%    |    -0.69 | -62.95%        | -49.69%        |                 1    |
| all_signals_ew        | out_of_sample | 17.97%       | 26.83%    |     0.67 | -18.13%        | 16.64%         |                 1    |
| high_conf_ew          | full          | -1.45%       | 31.34%    |    -0.05 | -43.98%        | -17.48%        |                 0.88 |
| high_conf_ew          | out_of_sample | 19.55%       | 33.71%    |     0.58 | -17.35%        | 16.16%         |                 0.88 |
| high_conf_voltarget   | full          | 1.17%        | 28.94%    |     0.04 | -36.19%        | -8.58%         |                 0.88 |
| high_conf_voltarget   | out_of_sample | 14.91%       | 31.30%    |     0.48 | -16.94%        | 11.48%         |                 0.88 |
| conviction_long_short | full          | -18.88%      | 23.16%    |    -0.82 | -48.95%        | -48.24%        |                 0.97 |
| conviction_long_short | out_of_sample | -12.92%      | 26.28%    |    -0.49 | -23.82%        | -16.06%        |                 0.97 |
| spy_buyhold           | full          | 6.44%        | 13.35%    |     0.48 | -18.27%        | 18.46%         |                 0.78 |
| spy_buyhold           | out_of_sample | -1.98%       | 9.77%     |    -0.2  | -13.27%        | -2.58%         |                 0.78 |
| sixty_forty           | full          | 3.81%        | 8.44%     |     0.45 | -10.80%        | 11.09%         |                 0.78 |
| sixty_forty           | out_of_sample | -2.73%       | 6.44%     |    -0.42 | -9.26%         | -3.08%         |                 0.78 |

## Walk-Forward Robustness

Each book measured across contiguous time folds (each a different regime). A book has durable edge only if `mean_sharpe` is positive, `min_sharpe` isn't deeply negative, and `pct_positive_folds` is high — a single great fold doesn't count. `fold_sharpes` lists each fold oldest-to-newest.

| strategy              |   n_folds |   mean_sharpe |   median_sharpe |   min_sharpe | pct_positive_folds   | mean_return   | fold_sharpes                 |
|:----------------------|----------:|--------------:|----------------:|-------------:|:---------------------|:--------------|:-----------------------------|
| equal_weight_buyhold  |         5 |          0.28 |            0.46 |        -1.42 | 60.00%               | -1.66%        | 1.86;-1.42;1.63;-1.14;0.46   |
| all_signals_ew        |         5 |         -0.72 |           -0.4  |        -2.27 | 20.00%               | -11.91%       | -0.00;-0.40;-2.27;0.14;-1.05 |
| high_conf_ew          |         5 |          0.05 |           -0.52 |        -0.59 | 40.00%               | -3.11%        | 1.31;-0.55;-0.52;0.62;-0.59  |
| high_conf_voltarget   |         5 |          0.27 |           -0.32 |        -0.59 | 40.00%               | -1.23%        | 2.22;-0.32;-0.48;0.51;-0.59  |
| conviction_long_short |         5 |         -0.99 |           -1.25 |        -2.16 | 20.00%               | -11.76%       | -1.58;-1.25;-0.44;0.47;-2.16 |
| spy_buyhold           |         5 |          0.66 |           -0.05 |        -0.68 | 40.00%               | 3.86%         | 1.79;-0.42;2.67;-0.68;-0.05  |
| sixty_forty           |         5 |          0.62 |           -0.37 |        -0.74 | 40.00%               | 2.34%         | 1.98;-0.56;2.80;-0.74;-0.37  |

## Strategy Comparison

Each decision rule backtested over the same data. `out_of_sample` is the most recent ~35% of each symbol's history (unseen tail). A rule has real edge only if `median_excess` and `beat_benchmark_pct` stay positive out-of-sample, not just full-sample.

| strategy        | scope         |   symbols | beat_benchmark_pct   | positive_pct   | median_return   | median_benchmark   | median_excess   |   median_sharpe |   total_trades |
|:----------------|:--------------|----------:|:---------------------|:---------------|:----------------|:-------------------|:----------------|----------------:|---------------:|
| trend           | full          |       160 | 32.50%               | 31.25%         | -10.88%         | 17.64%             | -28.41%         |           -0.12 |          11250 |
| trend           | out_of_sample |       160 | 40.62%               | 54.37%         | 2.00%           | 5.78%              | -4.98%          |            0.24 |           3812 |
| mean_reversion  | full          |       157 | 40.13%               | 50.32%         | 0.01%           | 17.46%             | -17.53%         |            0.03 |           1262 |
| mean_reversion  | out_of_sample |       125 | 49.60%               | 58.40%         | 0.34%           | -1.35%             | -0.39%          |            0.63 |            432 |
| regime_adaptive | full          |       160 | 32.50%               | 32.50%         | -10.58%         | 17.64%             | -28.66%         |           -0.13 |          11524 |
| regime_adaptive | out_of_sample |       160 | 40.62%               | 53.75%         | 2.39%           | 5.78%              | -4.68%          |            0.29 |           3913 |

## Signal Calibration

Realized forward return in the signal's direction, grouped by confidence. HIGH should outrank LOW for the confidence score to be meaningful.

| confidence_level   |   horizon |     n | mean_return   | median_return   | win_rate   |
|:-------------------|----------:|------:|:--------------|:----------------|:-----------|
| HIGH               |         5 |  7920 | 0.12%         | 0.11%           | 51.88%     |
| MEDIUM             |         5 | 29228 | 0.02%         | 0.07%           | 50.82%     |
| LOW                |         5 |  3329 | -0.64%        | -0.56%          | 44.49%     |
| ALL                |         5 | 40477 | -0.01%        | 0.04%           | 50.51%     |
| HIGH               |        10 |  7878 | 0.41%         | 0.12%           | 51.45%     |
| MEDIUM             |        10 | 29050 | 0.18%         | 0.13%           | 51.06%     |
| LOW                |        10 |  3283 | -0.89%        | -0.73%          | 45.26%     |
| ALL                |        10 | 40211 | 0.14%         | 0.08%           | 50.67%     |
| HIGH               |        20 |  7791 | 0.77%         | 0.34%           | 52.84%     |
| MEDIUM             |        20 | 28653 | 0.85%         | 0.63%           | 53.62%     |
| LOW                |        20 |  3241 | -0.65%        | -0.49%          | 47.30%     |
| ALL                |        20 | 39685 | 0.72%         | 0.50%           | 52.95%     |

## Backtest Summary

### Data Quality / Signal Availability

- **ok**: 160 symbols

| symbol     |   trades | return   | benchmark_return   | mdd     |   sharpe | exposure   | skipped_reason   |
|:-----------|---------:|:---------|:-------------------|:--------|---------:|:-----------|:-----------------|
| AAPL       |       63 | 13.49%   | 74.05%             | -20.65% |     0.36 | 49.08%     | ok               |
| AAVE-USD   |       74 | -48.33%  | -59.99%            | -68.26% |    -0.41 | 39.08%     | ok               |
| ABBV       |       66 | -21.43%  | 39.73%             | -30.55% |    -0.47 | 47.25%     | ok               |
| ADA-USD    |       88 | -83.94%  | -77.69%            | -89.69% |    -0.71 | 46.74%     | ok               |
| ADBE       |       64 | -29.13%  | -57.81%            | -34.83% |    -0.35 | 57.57%     | ok               |
| AGG        |       69 | -6.61%   | 0.63%              | -10.16% |    -1.1  | 31.11%     | ok               |
| ALGO-USD   |       86 | -50.43%  | -69.91%            | -53.13% |    -0.57 | 38.12%     | ok               |
| AMAT       |       71 | -34.36%  | 188.31%            | -57.21% |    -0.3  | 52.91%     | ok               |
| AMD        |       54 | 2.81%    | 207.35%            | -45.60% |     0.24 | 35.94%     | ok               |
| AMGN       |       69 | -15.41%  | 27.05%             | -34.14% |    -0.29 | 46.26%     | ok               |
| AMZN       |       80 | -35.71%  | 45.90%             | -42.48% |    -1.06 | 38.27%     | ok               |
| APT-USD    |       74 | -42.40%  | -89.92%            | -69.96% |    -0.25 | 42.34%     | ok               |
| ARB-USD    |       68 | -24.16%  | -80.19%            | -62.34% |    -0.05 | 38.51%     | ok               |
| ARKK       |       83 | -34.93%  | 55.45%             | -36.42% |    -0.62 | 40.43%     | ok               |
| ATOM-USD   |       88 | -70.49%  | -66.70%            | -73.75% |    -1.23 | 45.59%     | ok               |
| AVAX-USD   |       66 | -29.16%  | -73.90%            | -53.72% |    -0.19 | 38.12%     | ok               |
| AVGO       |       64 | 19.86%   | 208.36%            | -35.76% |     0.39 | 43.26%     | ok               |
| BA         |       67 | 7.60%    | 5.70%              | -30.56% |     0.25 | 49.25%     | ok               |
| BAC        |       78 | -10.07%  | 74.54%             | -27.64% |    -0.2  | 49.42%     | ok               |
| BCH-USD    |       76 | 2.55%    | -28.29%            | -53.87% |     0.24 | 48.28%     | ok               |
| BITO       |       80 | -1.40%   | -65.71%            | -42.82% |     0.16 | 41.93%     | ok               |
| BLK        |       71 | -7.59%   | 29.92%             | -24.29% |    -0.16 | 42.43%     | ok               |
| BND        |       65 | -7.32%   | 0.69%              | -9.89%  |    -1.18 | 32.28%     | ok               |
| BONK-USD   |       72 | 37.52%   | -79.39%            | -45.22% |     0.55 | 41.95%     | ok               |
| BTC-USD    |       76 | -2.15%   | -35.43%            | -23.38% |     0.12 | 52.87%     | ok               |
| C          |       81 | -25.27%  | 156.54%            | -37.02% |    -0.47 | 51.58%     | ok               |
| CAT        |       72 | 22.56%   | 189.36%            | -21.02% |     0.46 | 56.41%     | ok               |
| CL         |       62 | 13.87%   | 11.66%             | -14.32% |     0.49 | 46.26%     | ok               |
| CMCSA      |       77 | -37.91%  | -37.98%            | -38.21% |    -0.99 | 42.43%     | ok               |
| COMP-USD   |       89 | -45.23%  | -67.74%            | -58.41% |    -0.35 | 46.36%     | ok               |
| COP        |       72 | -25.92%  | 2.06%              | -43.96% |    -0.48 | 41.43%     | ok               |
| COST       |       62 | -0.88%   | 27.96%             | -29.73% |     0.04 | 44.26%     | ok               |
| CRM        |       63 | -40.72%  | -40.90%            | -42.49% |    -0.86 | 42.93%     | ok               |
| CRV-USD    |       68 | -11.45%  | -58.78%            | -39.89% |     0.11 | 36.21%     | ok               |
| CSCO       |       61 | 24.85%   | 146.18%            | -21.79% |     0.54 | 49.42%     | ok               |
| CVX        |       75 | -18.59%  | 17.83%             | -29.13% |    -0.49 | 39.77%     | ok               |
| DASH-USD   |       63 | -46.45%  | 26.02%             | -64.43% |    -0.08 | 30.27%     | ok               |
| DBC        |       58 | -13.08%  | 28.60%             | -25.15% |    -0.45 | 33.11%     | ok               |
| DE         |       72 | -8.54%   | 62.37%             | -25.24% |    -0.09 | 47.59%     | ok               |
| DIA        |       60 | -2.36%   | 35.81%             | -12.94% |    -0.09 | 44.26%     | ok               |
| DIS        |       68 | -24.41%  | -13.98%            | -28.17% |    -0.49 | 46.42%     | ok               |
| DOGE-USD   |       75 | -23.93%  | -71.75%            | -60.95% |     0    | 50.57%     | ok               |
| DOT-USD    |       88 | -59.56%  | -82.59%            | -63.10% |    -0.65 | 48.08%     | ok               |
| DXY-INDEX  |       40 | -1.24%   | -0.47%             | -6.02%  |    -0.18 | 30.59%     | ok               |
| EEM        |       64 | -9.40%   | 60.93%             | -25.67% |    -0.25 | 43.43%     | ok               |
| EFA        |       60 | -7.42%   | 35.72%             | -13.02% |    -0.26 | 44.26%     | ok               |
| EOG        |       81 | -22.29%  | 22.94%             | -48.13% |    -0.46 | 46.59%     | ok               |
| ETC-USD    |       64 | -34.12%  | -66.02%            | -46.77% |    -0.47 | 30.84%     | ok               |
| ETH-USD    |       64 | 122.51%  | -32.60%            | -30.11% |     1.11 | 44.83%     | ok               |
| EWJ        |       62 | -18.16%  | 37.10%             | -30.73% |    -0.59 | 39.10%     | ok               |
| FCX        |       63 | -27.81%  | 54.44%             | -47.47% |    -0.31 | 45.26%     | ok               |
| FET-USD    |       83 | -38.66%  | -78.33%            | -54.02% |    -0.13 | 41.38%     | ok               |
| FIL-USD    |       70 | -46.58%  | -77.29%            | -50.22% |    -0.6  | 32.95%     | ok               |
| FXI        |       44 | -6.84%   | 44.95%             | -23.91% |    -0.09 | 30.12%     | ok               |
| GDX        |       60 | 11.28%   | 173.16%            | -34.99% |     0.3  | 48.09%     | ok               |
| GDXJ       |       68 | -23.13%  | 194.17%            | -44.93% |    -0.22 | 46.42%     | ok               |
| GE         |       76 | 14.57%   | 196.89%            | -27.82% |     0.35 | 53.58%     | ok               |
| GLD        |       48 | 28.84%   | 97.02%             | -16.63% |     0.71 | 47.25%     | ok               |
| GOOGL      |       61 | 76.69%   | 150.86%            | -20.41% |     1.15 | 52.91%     | ok               |
| GRT-USD    |       83 | -18.35%  | -86.77%            | -54.83% |    -0.01 | 42.15%     | ok               |
| GS         |       76 | -2.38%   | 172.06%            | -22.13% |     0.05 | 52.08%     | ok               |
| HD         |       71 | -7.53%   | -6.97%             | -17.69% |    -0.12 | 44.59%     | ok               |
| HON        |       94 | -29.10%  | 14.03%             | -31.48% |    -0.8  | 52.75%     | ok               |
| HYG        |       81 | -9.08%   | 3.39%              | -9.59%  |    -1.06 | 33.94%     | ok               |
| IBIT       |       34 | 30.82%   | -7.34%             | -18.95% |     0.67 | 32.32%     | ok               |
| IBM        |       78 | 4.29%    | 54.67%             | -27.54% |     0.19 | 49.58%     | ok               |
| ICP-USD    |       77 | -12.97%  | -69.09%            | -50.29% |     0.12 | 35.06%     | ok               |
| IEF        |       76 | -10.90%  | -0.48%             | -11.70% |    -1.54 | 32.78%     | ok               |
| IEMG       |       58 | -7.79%   | 55.61%             | -26.84% |    -0.21 | 43.09%     | ok               |
| INJ-USD    |       75 | -53.29%  | -65.65%            | -77.42% |    -0.51 | 37.74%     | ok               |
| INTC       |       70 | 55.82%   | 137.00%            | -60.60% |     0.62 | 49.25%     | ok               |
| INTU       |       69 | -20.79%  | -55.81%            | -42.17% |    -0.25 | 41.76%     | ok               |
| ITA        |       72 | -2.69%   | 87.08%             | -23.75% |    -0    | 48.42%     | ok               |
| IWM        |       48 | 9.40%    | 45.53%             | -12.83% |     0.39 | 35.77%     | ok               |
| JNJ        |       70 | 7.83%    | 64.66%             | -17.51% |     0.32 | 50.75%     | ok               |
| JPM        |       77 | -20.64%  | 86.86%             | -33.43% |    -0.5  | 53.91%     | ok               |
| KO         |       49 | 28.93%   | 41.86%             | -8.07%  |     1.03 | 37.77%     | ok               |
| LDO-USD    |       78 | 0.54%    | -79.67%            | -60.93% |     0.28 | 39.08%     | ok               |
| LIN        |       66 | -2.65%   | 21.41%             | -21.53% |    -0.03 | 39.43%     | ok               |
| LINK-USD   |       74 | -18.56%  | -57.34%            | -50.48% |     0.04 | 42.15%     | ok               |
| LLY        |       71 | -29.60%  | 51.12%             | -53.34% |    -0.44 | 50.08%     | ok               |
| LRCX       |       80 | -26.10%  | 256.27%            | -63.56% |    -0.16 | 45.26%     | ok               |
| LTC-USD    |       68 | -35.18%  | -58.53%            | -53.76% |    -0.31 | 48.85%     | ok               |
| MCD        |       75 | -2.55%   | -6.65%             | -18.81% |    -0.05 | 38.10%     | ok               |
| META       |       72 | -29.15%  | 38.75%             | -38.96% |    -0.5  | 48.09%     | ok               |
| MPC        |       73 | -11.56%  | 74.63%             | -44.76% |    -0.09 | 48.75%     | ok               |
| MRK        |       69 | -30.74%  | -2.94%             | -34.46% |    -0.75 | 44.26%     | ok               |
| MS         |       79 | -11.43%  | 155.60%            | -27.79% |    -0.19 | 49.75%     | ok               |
| MSFT       |       83 | -38.30%  | -3.23%             | -39.15% |    -1.02 | 47.42%     | ok               |
| MU         |       51 | 270.20%  | 1078.62%           | -68.76% |     1.34 | 59.90%     | ok               |
| NEAR-USD   |       85 | -15.24%  | -40.87%            | -60.07% |     0.09 | 41.00%     | ok               |
| NEM        |       72 | -31.13%  | 178.49%            | -38.49% |    -0.33 | 53.08%     | ok               |
| NFLX       |       64 | 28.82%   | 26.43%             | -21.09% |     0.63 | 54.58%     | ok               |
| NKE        |       91 | -48.19%  | -57.72%            | -57.25% |    -0.9  | 43.59%     | ok               |
| NOW        |       84 | 10.73%   | -27.28%            | -28.87% |     0.29 | 45.59%     | ok               |
| NVDA       |       75 | -26.67%  | 132.83%            | -45.02% |    -0.19 | 59.18%     | ok               |
| OP-USD     |       70 | -26.66%  | -90.75%            | -70.27% |    -0.07 | 33.72%     | ok               |
| ORCL       |       72 | 110.75%  | 18.17%             | -29.47% |     0.94 | 54.08%     | ok               |
| OXY        |       71 | 0.41%    | -9.43%             | -34.15% |     0.13 | 45.26%     | ok               |
| PEP        |       79 | -6.85%   | -16.73%            | -21.35% |    -0.14 | 48.75%     | ok               |
| PEPE-USD   |       79 | 0.11%    | -71.74%            | -57.66% |     0.28 | 44.83%     | ok               |
| PFE        |       77 | -40.21%  | -11.37%            | -41.06% |    -1.29 | 35.94%     | ok               |
| PG         |       68 | -18.12%  | -5.80%             | -24.55% |    -0.68 | 40.60%     | ok               |
| PM         |       85 | -4.27%   | 100.99%            | -33.68% |     0    | 56.07%     | ok               |
| POL-USD    |       79 | 39.71%   | -73.19%            | -46.45% |     0.6  | 46.74%     | ok               |
| QCOM       |       73 | -15.25%  | 20.49%             | -56.59% |    -0.04 | 46.09%     | ok               |
| QQQ        |       64 | 18.39%   | 65.30%             | -12.88% |     0.54 | 44.26%     | ok               |
| RENDER-USD |       98 | -19.07%  | -64.47%            | -45.00% |     0.1  | 43.03%     | ok               |
| RTX        |       58 | 26.08%   | 115.79%            | -16.99% |     0.65 | 51.58%     | ok               |
| SBUX       |       69 | -22.57%  | 15.15%             | -29.22% |    -0.45 | 40.93%     | ok               |
| SCHW       |       74 | -12.92%  | 58.98%             | -31.92% |    -0.24 | 47.25%     | ok               |
| SHIB-USD   |       78 | -35.51%  | -74.16%            | -47.96% |    -0.29 | 52.11%     | ok               |
| SHY        |       48 | -2.24%   | 0.16%              | -2.85%  |    -0.79 | 34.28%     | ok               |
| SKY-USD    |       70 | -28.56%  | 2.61%              | -43.98% |    -0.34 | 40.04%     | ok               |
| SLB        |       75 | -25.39%  | -2.49%             | -54.23% |    -0.43 | 51.25%     | ok               |
| SLV        |       58 | 51.45%   | 143.85%            | -42.66% |     0.7  | 42.93%     | ok               |
| SMH        |       48 | 85.29%   | 190.27%            | -33.99% |     1.12 | 48.25%     | ok               |
| SNX-USD    |       58 | -15.26%  | -76.30%            | -34.76% |     0.08 | 37.93%     | ok               |
| SOL-USD    |       68 | -33.02%  | -62.57%            | -56.90% |    -0.09 | 59.39%     | ok               |
| SOXX       |       57 | 73.45%   | 165.68%            | -41.89% |     0.97 | 47.09%     | ok               |
| SPY        |       64 | 3.32%    | 49.98%             | -16.47% |     0.18 | 50.08%     | ok               |
| SUSHI-USD  |       94 | -81.55%  | -80.59%            | -85.18% |    -1.27 | 36.40%     | ok               |
| T          |       64 | 40.41%   | 26.99%             | -17.01% |     0.89 | 52.75%     | ok               |
| TGT        |       60 | -11.04%  | -9.92%             | -40.57% |    -0.14 | 39.43%     | ok               |
| TIA-USD    |       89 | -42.33%  | -86.79%            | -66.21% |    -0.27 | 36.21%     | ok               |
| TLT        |       70 | -21.12%  | -9.48%             | -21.75% |    -1.63 | 31.95%     | ok               |
| TMO        |       61 | 15.04%   | -3.53%             | -18.85% |     0.39 | 50.08%     | ok               |
| TMUS       |       70 | 7.70%    | 17.46%             | -25.71% |     0.26 | 48.42%     | ok               |
| TRX-USD    |       72 | 0.99%    | 40.26%             | -22.90% |     0.12 | 49.04%     | ok               |
| TSLA       |       69 | 5.29%    | 97.43%             | -42.22% |     0.25 | 40.93%     | ok               |
| TXN        |       74 | -13.50%  | 86.16%             | -47.39% |    -0.06 | 53.41%     | ok               |
| UNH        |       74 | 30.65%   | -17.73%            | -27.86% |     0.53 | 52.58%     | ok               |
| UNI-USD    |       88 | -73.46%  | -61.06%            | -80.61% |    -0.9  | 43.68%     | ok               |
| UPS        |       70 | -35.48%  | -23.93%            | -37.08% |    -0.7  | 39.27%     | ok               |
| USO        |       66 | 5.74%    | 60.45%             | -43.35% |     0.22 | 33.44%     | ok               |
| VEA        |       58 | -0.98%   | 45.15%             | -17.93% |     0.01 | 44.09%     | ok               |
| VIXY       |       96 | -80.03%  | -63.33%            | -88.16% |    -1    | 32.28%     | ok               |
| VNQ        |       75 | -15.90%  | 15.95%             | -24.92% |    -0.66 | 37.44%     | ok               |
| VTI        |       72 | -3.73%   | 48.83%             | -18.77% |    -0.07 | 50.75%     | ok               |
| VWO        |       76 | -13.41%  | 43.08%             | -25.20% |    -0.47 | 44.09%     | ok               |
| VZ         |       85 | -27.83%  | 5.41%              | -27.83% |    -0.94 | 37.44%     | ok               |
| WFC        |       86 | -14.92%  | 68.89%             | -29.91% |    -0.22 | 50.25%     | ok               |
| WIF-USD    |       68 | -35.28%  | -78.71%            | -50.54% |    -0.13 | 31.99%     | ok               |
| WMT        |       61 | 16.25%   | 102.12%            | -21.31% |     0.49 | 50.58%     | ok               |
| XBI        |       62 | 4.17%    | 66.76%             | -19.80% |     0.19 | 41.10%     | ok               |
| XLB        |       64 | -10.86%  | 18.77%             | -26.57% |    -0.36 | 36.77%     | ok               |
| XLC        |       67 | 12.19%   | 41.34%             | -12.33% |     0.45 | 54.58%     | ok               |
| XLE        |       75 | -9.17%   | 32.62%             | -37.64% |    -0.16 | 45.26%     | ok               |
| XLF        |       76 | -10.86%  | 41.48%             | -23.61% |    -0.35 | 47.92%     | ok               |
| XLI        |       66 | -0.89%   | 52.82%             | -11.76% |     0.02 | 44.76%     | ok               |
| XLK        |       42 | 64.04%   | 78.98%             | -14.75% |     1.2  | 45.76%     | ok               |
| XLM-USD    |       69 | 5.21%    | -46.34%            | -50.36% |     0.28 | 45.79%     | ok               |
| XLP        |       68 | 6.32%    | 15.43%             | -11.16% |     0.39 | 42.10%     | ok               |
| XLU        |       67 | -4.17%   | 49.34%             | -20.40% |    -0.14 | 38.77%     | ok               |
| XLV        |       68 | -14.04%  | 10.84%             | -18.68% |    -0.7  | 36.11%     | ok               |
| XLY        |       72 | 2.75%    | 29.64%             | -14.01% |     0.15 | 44.26%     | ok               |
| XOM        |       59 | 2.87%    | 39.31%             | -20.29% |     0.15 | 36.27%     | ok               |
| XRP-USD    |       58 | -30.47%  | -56.17%            | -44.89% |    -0.26 | 33.72%     | ok               |
| YFI-USD    |       81 | -65.02%  | -63.09%            | -70.70% |    -1.06 | 40.80%     | ok               |
| ZEC-USD    |       64 | 34.74%   | 1459.06%           | -47.68% |     0.51 | 35.25%     | ok               |

## AAPL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 23.66%   | 74.05%             | -21.71% |     0.53 |       68 | 53.41%     | ok               |
|          15 | 19.86%   | 74.05%             | -23.86% |     0.46 |       75 | 60.57%     | ok               |
|          30 | 13.49%   | 74.05%             | -20.65% |     0.36 |       63 | 49.08%     | ok               |
|          25 | 12.31%   | 74.05%             | -20.03% |     0.34 |       67 | 51.08%     | ok               |
|          35 | 10.95%   | 74.05%             | -22.04% |     0.32 |       63 | 47.59%     | ok               |

## AAVE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 22.85%   | -59.99%            | -43.61% |     0.44 |       38 | 31.80%     | ok               |
|          45 | 5.36%    | -59.99%            | -46.87% |     0.27 |       42 | 26.82%     | ok               |
|          35 | -1.60%   | -59.99%            | -51.96% |     0.21 |       50 | 35.06%     | ok               |
|          50 | -29.26%  | -59.99%            | -43.73% |    -0.28 |       42 | 19.54%     | ok               |
|          15 | -49.36%  | -59.99%            | -61.76% |    -0.28 |       80 | 53.26%     | ok               |

## ABBV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -12.15%  | 39.73%             | -28.42% |    -0.24 |       52 | 37.10%     | ok               |
|          40 | -18.17%  | 39.73%             | -26.61% |    -0.4  |       66 | 41.60%     | ok               |
|          35 | -19.34%  | 39.73%             | -27.83% |    -0.43 |       68 | 44.43%     | ok               |
|          30 | -21.43%  | 39.73%             | -30.55% |    -0.47 |       66 | 47.25%     | ok               |
|          45 | -20.72%  | 39.73%             | -29.59% |    -0.49 |       56 | 38.77%     | ok               |

## ADA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -77.92%  | -77.69%            | -85.97% |    -0.59 |       55 | 26.82%     | ok               |
|          45 | -80.28%  | -77.69%            | -88.02% |    -0.62 |       58 | 31.61%     | ok               |
|          35 | -82.72%  | -77.69%            | -89.77% |    -0.67 |       78 | 42.34%     | ok               |
|          30 | -83.94%  | -77.69%            | -89.69% |    -0.71 |       88 | 46.74%     | ok               |
|          40 | -83.55%  | -77.69%            | -90.19% |    -0.72 |       74 | 36.97%     | ok               |

## ADBE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 2.79%    | -57.81%            | -21.34% |     0.17 |       72 | 49.25%     | ok               |
|          40 | -10.53%  | -57.81%            | -24.87% |    -0.08 |       70 | 42.26%     | ok               |
|          25 | -15.81%  | -57.81%            | -30.06% |    -0.1  |       48 | 61.73%     | ok               |
|          20 | -25.04%  | -57.81%            | -32.14% |    -0.25 |       48 | 63.73%     | ok               |
|          15 | -26.22%  | -57.81%            | -32.12% |    -0.27 |       55 | 66.06%     | ok               |

## AGG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -6.61%   | 0.63%              | -10.16% |    -1.1  |       69 | 31.11%     | ok               |
|          20 | -7.69%   | 0.63%              | -10.67% |    -1.13 |       73 | 36.77%     | ok               |
|          45 | -5.75%   | 0.63%              | -7.89%  |    -1.16 |       52 | 20.47%     | ok               |
|          25 | -7.87%   | 0.63%              | -11.31% |    -1.2  |       73 | 35.11%     | ok               |
|          50 | -5.57%   | 0.63%              | -7.92%  |    -1.25 |       46 | 16.97%     | ok               |

## ALGO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -50.43%  | -69.91%            | -53.13% |    -0.57 |       86 | 38.12%     | ok               |
|          15 | -61.64%  | -69.91%            | -68.50% |    -0.67 |       84 | 50.38%     | ok               |
|          25 | -61.89%  | -69.91%            | -72.48% |    -0.74 |       84 | 45.02%     | ok               |
|          20 | -65.54%  | -69.91%            | -71.20% |    -0.8  |       86 | 48.08%     | ok               |
|          50 | -45.64%  | -69.91%            | -48.43% |    -0.81 |       42 | 16.86%     | ok               |

## AMAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -22.69%  | 188.31%            | -54.05% |    -0.08 |       68 | 61.90%     | ok               |
|          30 | -34.36%  | 188.31%            | -57.21% |    -0.3  |       71 | 52.91%     | ok               |
|          35 | -34.82%  | 188.31%            | -55.26% |    -0.33 |       73 | 50.58%     | ok               |
|          50 | -34.67%  | 188.31%            | -48.72% |    -0.37 |       52 | 38.44%     | ok               |
|          20 | -41.87%  | 188.31%            | -60.16% |    -0.41 |       74 | 58.24%     | ok               |

## AMD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 6.74%    | 207.35%            | -44.26% |     0.27 |       54 | 30.62%     | ok               |
|          40 | 2.81%    | 207.35%            | -45.60% |     0.24 |       54 | 35.94%     | ok               |
|          35 | -12.57%  | 207.35%            | -52.13% |     0.08 |       64 | 37.60%     | ok               |
|          45 | -14.79%  | 207.35%            | -53.24% |     0.04 |       60 | 33.44%     | ok               |
|          30 | -26.23%  | 207.35%            | -58.91% |    -0.08 |       67 | 40.27%     | ok               |

## AMGN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -9.55%   | 27.05%             | -26.64% |    -0.12 |       71 | 52.25%     | ok               |
|          35 | -11.27%  | 27.05%             | -31.23% |    -0.18 |       65 | 42.43%     | ok               |
|          15 | -13.35%  | 27.05%             | -27.92% |    -0.19 |       70 | 58.07%     | ok               |
|          30 | -15.41%  | 27.05%             | -34.14% |    -0.29 |       69 | 46.26%     | ok               |
|          25 | -18.85%  | 27.05%             | -33.41% |    -0.37 |       65 | 48.59%     | ok               |

## AMZN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -17.32%  | 45.90%             | -28.70% |    -0.5  |       54 | 29.28%     | ok               |
|          50 | -23.70%  | 45.90%             | -35.48% |    -0.84 |       52 | 23.29%     | ok               |
|          35 | -29.43%  | 45.90%             | -38.29% |    -0.91 |       68 | 32.78%     | ok               |
|          45 | -26.51%  | 45.90%             | -35.47% |    -0.92 |       56 | 26.29%     | ok               |
|          30 | -35.71%  | 45.90%             | -42.48% |    -1.06 |       80 | 38.27%     | ok               |

## APT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 19.10%   | -89.92%            | -46.73% |     0.42 |       40 | 18.97%     | ok               |
|          45 | -9.82%   | -89.92%            | -63.86% |     0.08 |       58 | 24.90%     | ok               |
|          20 | -34.30%  | -89.92%            | -70.51% |    -0.1  |       71 | 51.15%     | ok               |
|          40 | -27.15%  | -89.92%            | -63.33% |    -0.11 |       64 | 30.46%     | ok               |
|          35 | -32.48%  | -89.92%            | -64.45% |    -0.16 |       68 | 36.21%     | ok               |

## ARB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 30.86%   | -80.19%            | -53.74% |     0.51 |       87 | 55.94%     | ok               |
|          40 | 10.89%   | -80.19%            | -45.73% |     0.33 |       50 | 29.50%     | ok               |
|          20 | -1.66%   | -80.19%            | -60.40% |     0.26 |       75 | 49.43%     | ok               |
|          35 | 0.04%    | -80.19%            | -54.43% |     0.23 |       60 | 32.95%     | ok               |
|          45 | -0.55%   | -80.19%            | -49.08% |     0.2  |       56 | 22.80%     | ok               |

## ARKK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -27.02%  | 55.45%             | -34.75% |    -0.34 |       91 | 50.92%     | ok               |
|          20 | -29.86%  | 55.45%             | -33.19% |    -0.43 |       86 | 46.26%     | ok               |
|          30 | -34.93%  | 55.45%             | -36.42% |    -0.62 |       83 | 40.43%     | ok               |
|          35 | -38.22%  | 55.45%             | -39.64% |    -0.75 |       86 | 37.60%     | ok               |
|          25 | -42.47%  | 55.45%             | -43.79% |    -0.81 |       91 | 42.43%     | ok               |

## ATOM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -66.76%  | -66.70%            | -70.28% |    -1.02 |       91 | 52.11%     | ok               |
|          15 | -71.28%  | -66.70%            | -71.91% |    -1.08 |       93 | 62.07%     | ok               |
|          45 | -62.51%  | -66.70%            | -64.33% |    -1.22 |       74 | 29.50%     | ok               |
|          30 | -70.49%  | -66.70%            | -73.75% |    -1.23 |       88 | 45.59%     | ok               |
|          20 | -74.34%  | -66.70%            | -74.86% |    -1.26 |       99 | 55.75%     | ok               |

## AVAX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 7.33%    | -73.90%            | -29.53% |     0.27 |       30 | 18.20%     | ok               |
|          40 | 5.29%    | -73.90%            | -32.96% |     0.24 |       36 | 24.71%     | ok               |
|          45 | 5.33%    | -73.90%            | -32.82% |     0.24 |       30 | 21.84%     | ok               |
|          35 | -2.29%   | -73.90%            | -36.30% |     0.16 |       54 | 30.08%     | ok               |
|          15 | -25.84%  | -73.90%            | -52.46% |    -0.04 |       69 | 52.87%     | ok               |

## AVGO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 19.86%   | 208.36%            | -35.76% |     0.39 |       64 | 43.26%     | ok               |
|          40 | 18.39%   | 208.36%            | -40.70% |     0.37 |       62 | 37.10%     | ok               |
|          25 | 15.87%   | 208.36%            | -38.01% |     0.35 |       70 | 44.59%     | ok               |
|          35 | 14.10%   | 208.36%            | -36.19% |     0.33 |       72 | 40.43%     | ok               |
|          50 | 13.95%   | 208.36%            | -35.84% |     0.33 |       60 | 30.95%     | ok               |

## BA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 26.03%   | 5.70%              | -13.34% |     0.67 |       42 | 31.45%     | ok               |
|          35 | 30.46%   | 5.70%              | -23.77% |     0.59 |       72 | 44.59%     | ok               |
|          40 | 20.11%   | 5.70%              | -23.90% |     0.47 |       46 | 38.60%     | ok               |
|          25 | 10.59%   | 5.70%              | -32.48% |     0.29 |       70 | 52.58%     | ok               |
|          30 | 7.60%    | 5.70%              | -30.56% |     0.25 |       67 | 49.25%     | ok               |

## BAC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 2.20%    | 74.54%             | -20.40% |     0.14 |       60 | 37.60%     | ok               |
|          20 | -3.23%   | 74.54%             | -20.73% |     0.01 |       78 | 53.74%     | ok               |
|          35 | -3.57%   | 74.54%             | -27.83% |    -0.03 |       70 | 45.42%     | ok               |
|          50 | -2.91%   | 74.54%             | -20.35% |    -0.03 |       60 | 34.44%     | ok               |
|          40 | -4.91%   | 74.54%             | -24.53% |    -0.08 |       64 | 40.60%     | ok               |

## BCH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 2.55%    | -28.29%            | -53.87% |     0.24 |       76 | 48.28%     | ok               |
|          20 | -9.73%   | -28.29%            | -52.88% |     0.14 |       72 | 55.17%     | ok               |
|          15 | -16.64%  | -28.29%            | -58.44% |     0.07 |       78 | 59.58%     | ok               |
|          25 | -20.81%  | -28.29%            | -58.63% |    -0.01 |       72 | 50.77%     | ok               |
|          35 | -19.32%  | -28.29%            | -64.08% |    -0.05 |       70 | 44.44%     | ok               |

## BITO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 20.09%   | -65.71%            | -31.98% |     0.4  |       54 | 25.29%     | ok               |
|          45 | 1.03%    | -65.71%            | -41.16% |     0.17 |       62 | 28.95%     | ok               |
|          30 | -1.40%   | -65.71%            | -42.82% |     0.16 |       80 | 41.93%     | ok               |
|          40 | -3.49%   | -65.71%            | -43.67% |     0.12 |       66 | 33.78%     | ok               |
|          15 | -8.67%   | -65.71%            | -48.38% |     0.11 |       89 | 50.92%     | ok               |

## BLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -1.34%   | 29.92%             | -17.97% |     0.03 |       76 | 38.60%     | ok               |
|          20 | -3.44%   | 29.92%             | -21.48% |    -0.02 |       76 | 47.25%     | ok               |
|          40 | -4.99%   | 29.92%             | -20.08% |    -0.1  |       70 | 34.61%     | ok               |
|          30 | -7.59%   | 29.92%             | -24.29% |    -0.16 |       71 | 42.43%     | ok               |
|          25 | -8.52%   | 29.92%             | -23.36% |    -0.18 |       71 | 44.76%     | ok               |

## BND Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.17%   | 0.69%              | -9.05%  |    -0.9  |       63 | 38.10%     | ok               |
|          25 | -6.87%   | 0.69%              | -10.14% |    -1.05 |       67 | 36.11%     | ok               |
|          30 | -7.32%   | 0.69%              | -9.89%  |    -1.18 |       65 | 32.28%     | ok               |
|          15 | -8.39%   | 0.69%              | -10.58% |    -1.21 |       73 | 40.93%     | ok               |
|          45 | -7.56%   | 0.69%              | -9.57%  |    -1.47 |       50 | 21.96%     | ok               |

## BONK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 169.29%  | -79.39%            | -35.57% |     1.24 |       44 | 22.03%     | ok               |
|          45 | 121.76%  | -79.39%            | -42.36% |     1.02 |       54 | 26.25%     | ok               |
|          20 | 133.74%  | -79.39%            | -55.43% |     0.93 |       68 | 53.07%     | ok               |
|          15 | 139.09%  | -79.39%            | -63.45% |     0.92 |       70 | 58.05%     | ok               |
|          25 | 105.78%  | -79.39%            | -47.99% |     0.85 |       67 | 48.28%     | ok               |

## BTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 46.18%   | -35.43%            | -14.53% |     0.84 |       46 | 34.87%     | ok               |
|          45 | 40.84%   | -35.43%            | -15.18% |     0.81 |       44 | 30.65%     | ok               |
|          35 | 28.81%   | -35.43%            | -26.34% |     0.58 |       70 | 41.76%     | ok               |
|          50 | 13.98%   | -35.43%            | -18.05% |     0.4  |       42 | 25.29%     | ok               |
|          30 | 13.35%   | -35.43%            | -21.75% |     0.35 |       74 | 48.47%     | ok               |

## C Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -6.29%   | 156.54%            | -22.28% |    -0.1  |       64 | 36.11%     | ok               |
|          15 | -22.27%  | 156.54%            | -34.71% |    -0.36 |       74 | 60.23%     | ok               |
|          25 | -21.48%  | 156.54%            | -33.83% |    -0.37 |       73 | 53.41%     | ok               |
|          45 | -17.76%  | 156.54%            | -30.30% |    -0.41 |       78 | 40.43%     | ok               |
|          20 | -24.12%  | 156.54%            | -35.21% |    -0.42 |       81 | 56.41%     | ok               |

## CAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 22.56%   | 189.36%            | -21.02% |     0.46 |       72 | 56.41%     | ok               |
|          25 | 22.67%   | 189.36%            | -26.37% |     0.46 |       68 | 59.23%     | ok               |
|          20 | 21.20%   | 189.36%            | -25.65% |     0.44 |       78 | 62.73%     | ok               |
|          45 | 17.54%   | 189.36%            | -27.12% |     0.4  |       56 | 45.09%     | ok               |
|          35 | 14.51%   | 189.36%            | -27.72% |     0.35 |       70 | 49.92%     | ok               |

## CL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 15.12%   | 11.66%             | -11.22% |     0.63 |       44 | 29.95%     | ok               |
|          30 | 13.87%   | 11.66%             | -14.32% |     0.49 |       62 | 46.26%     | ok               |
|          45 | 9.14%    | 11.66%             | -13.51% |     0.39 |       48 | 33.28%     | ok               |
|          35 | 8.45%    | 11.66%             | -13.83% |     0.34 |       64 | 42.60%     | ok               |
|          40 | 5.30%    | 11.66%             | -12.70% |     0.25 |       58 | 37.27%     | ok               |

## CMCSA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -36.11%  | -37.98%            | -44.10% |    -0.8  |       86 | 57.24%     | ok               |
|          30 | -37.91%  | -37.98%            | -38.21% |    -0.99 |       77 | 42.43%     | ok               |
|          25 | -41.71%  | -37.98%            | -41.09% |    -1.11 |       86 | 47.59%     | ok               |
|          20 | -47.08%  | -37.98%            | -46.52% |    -1.26 |       91 | 53.24%     | ok               |
|          50 | -32.37%  | -37.98%            | -32.51% |    -1.3  |       50 | 15.47%     | ok               |

## COMP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -12.82%  | -67.74%            | -38.71% |     0.02 |       48 | 20.88%     | ok               |
|          30 | -45.23%  | -67.74%            | -58.41% |    -0.35 |       89 | 46.36%     | ok               |
|          25 | -47.90%  | -67.74%            | -60.58% |    -0.36 |       89 | 52.11%     | ok               |
|          15 | -54.82%  | -67.74%            | -65.55% |    -0.43 |      103 | 63.60%     | ok               |
|          40 | -49.06%  | -67.74%            | -50.52% |    -0.53 |       74 | 34.48%     | ok               |

## COP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -7.75%   | 2.06%              | -34.93% |    -0.1  |       46 | 27.62%     | ok               |
|          35 | -20.39%  | 2.06%              | -43.40% |    -0.36 |       71 | 38.10%     | ok               |
|          45 | -18.64%  | 2.06%              | -40.95% |    -0.37 |       60 | 30.95%     | ok               |
|          30 | -25.92%  | 2.06%              | -43.96% |    -0.48 |       72 | 41.43%     | ok               |
|          40 | -23.78%  | 2.06%              | -46.69% |    -0.49 |       66 | 34.11%     | ok               |

## COST Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 10.64%   | 27.96%             | -24.32% |     0.36 |       66 | 50.75%     | ok               |
|          25 | 9.00%    | 27.96%             | -24.73% |     0.32 |       63 | 47.92%     | ok               |
|          35 | 5.02%    | 27.96%             | -26.58% |     0.22 |       54 | 41.10%     | ok               |
|          30 | -0.88%   | 27.96%             | -29.73% |     0.04 |       62 | 44.26%     | ok               |
|          40 | -1.43%   | 27.96%             | -28.41% |     0.02 |       56 | 38.10%     | ok               |

## CRM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -37.99%  | -40.90%            | -44.67% |    -0.62 |       92 | 54.58%     | ok               |
|          35 | -30.98%  | -40.90%            | -34.36% |    -0.62 |       60 | 38.10%     | ok               |
|          40 | -34.83%  | -40.90%            | -39.11% |    -0.8  |       66 | 33.94%     | ok               |
|          30 | -40.72%  | -40.90%            | -42.49% |    -0.86 |       63 | 42.93%     | ok               |
|          20 | -45.29%  | -40.90%            | -47.55% |    -0.88 |       76 | 48.25%     | ok               |

## CRV-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 11.50%   | -58.78%            | -37.78% |     0.34 |       70 | 31.61%     | ok               |
|          50 | -0.89%   | -58.78%            | -29.30% |     0.18 |       46 | 17.43%     | ok               |
|          45 | -2.16%   | -58.78%            | -42.29% |     0.17 |       56 | 20.88%     | ok               |
|          40 | -7.62%   | -58.78%            | -38.86% |     0.12 |       60 | 27.20%     | ok               |
|          30 | -11.45%  | -58.78%            | -39.89% |     0.11 |       68 | 36.21%     | ok               |

## CSCO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 32.74%   | 146.18%            | -19.34% |     0.71 |       54 | 37.94%     | ok               |
|          45 | 28.62%   | 146.18%            | -19.34% |     0.63 |       51 | 39.93%     | ok               |
|          25 | 25.43%   | 146.18%            | -23.28% |     0.54 |       65 | 51.41%     | ok               |
|          35 | 24.84%   | 146.18%            | -23.68% |     0.54 |       53 | 46.92%     | ok               |
|          30 | 24.85%   | 146.18%            | -21.79% |     0.54 |       61 | 49.42%     | ok               |

## CVX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -13.11%  | 17.83%             | -27.34% |    -0.35 |       77 | 34.78%     | ok               |
|          25 | -15.18%  | 17.83%             | -24.36% |    -0.35 |       75 | 42.43%     | ok               |
|          35 | -15.12%  | 17.83%             | -28.85% |    -0.39 |       69 | 36.94%     | ok               |
|          45 | -14.24%  | 17.83%             | -28.83% |    -0.4  |       67 | 30.95%     | ok               |
|          30 | -18.59%  | 17.83%             | -29.13% |    -0.49 |       75 | 39.77%     | ok               |

## DASH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 99.00%   | 26.02%             | -27.34% |     0.84 |       40 | 15.13%     | ok               |
|          40 | 56.73%   | 26.02%             | -28.66% |     0.63 |       48 | 22.22%     | ok               |
|          45 | 43.71%   | 26.02%             | -36.02% |     0.56 |       44 | 17.43%     | ok               |
|          35 | -41.56%  | 26.02%             | -63.23% |    -0.02 |       69 | 26.82%     | ok               |
|          25 | -46.87%  | 26.02%             | -64.14% |    -0.08 |       69 | 32.95%     | ok               |

## DBC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -7.93%   | 28.60%             | -26.53% |    -0.22 |       72 | 38.60%     | ok               |
|          50 | -7.75%   | 28.60%             | -20.31% |    -0.29 |       40 | 21.13%     | ok               |
|          35 | -10.41%  | 28.60%             | -23.35% |    -0.34 |       60 | 31.78%     | ok               |
|          25 | -10.88%  | 28.60%             | -25.55% |    -0.35 |       62 | 34.94%     | ok               |
|          45 | -10.30%  | 28.60%             | -21.46% |    -0.37 |       56 | 24.79%     | ok               |

## DE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -7.68%   | 62.37%             | -28.94% |    -0.06 |       72 | 52.91%     | ok               |
|          30 | -8.54%   | 62.37%             | -25.24% |    -0.09 |       72 | 47.59%     | ok               |
|          25 | -9.97%   | 62.37%             | -26.67% |    -0.12 |       74 | 50.25%     | ok               |
|          50 | -8.73%   | 62.37%             | -24.35% |    -0.15 |       72 | 32.28%     | ok               |
|          45 | -10.55%  | 62.37%             | -27.91% |    -0.18 |       70 | 36.77%     | ok               |

## DIA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -0.30%   | 35.81%             | -13.15% |     0.02 |       60 | 42.10%     | ok               |
|          25 | -0.84%   | 35.81%             | -11.28% |    -0.01 |       60 | 45.42%     | ok               |
|          30 | -2.36%   | 35.81%             | -12.94% |    -0.09 |       60 | 44.26%     | ok               |
|          20 | -4.23%   | 35.81%             | -13.85% |    -0.18 |       64 | 47.75%     | ok               |
|          40 | -4.36%   | 35.81%             | -15.06% |    -0.22 |       66 | 39.27%     | ok               |

## DIS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 15.55%   | -13.98%            | -14.24% |     0.5  |       50 | 28.12%     | ok               |
|          45 | -8.59%   | -13.98%            | -16.54% |    -0.13 |       53 | 31.78%     | ok               |
|          40 | -10.02%  | -13.98%            | -23.29% |    -0.14 |       65 | 37.10%     | ok               |
|          15 | -19.91%  | -13.98%            | -31.15% |    -0.31 |       88 | 57.74%     | ok               |
|          35 | -19.02%  | -13.98%            | -25.70% |    -0.36 |       75 | 43.09%     | ok               |

## DOGE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 7.80%    | -71.75%            | -57.89% |     0.35 |       83 | 67.05%     | ok               |
|          25 | -9.09%   | -71.75%            | -53.72% |     0.18 |       72 | 56.13%     | ok               |
|          20 | -11.58%  | -71.75%            | -55.83% |     0.17 |       84 | 61.30%     | ok               |
|          30 | -23.93%  | -71.75%            | -60.95% |     0    |       75 | 50.57%     | ok               |
|          35 | -50.19%  | -71.75%            | -63.16% |    -0.47 |       72 | 43.87%     | ok               |

## DOT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -32.99%  | -82.59%            | -46.17% |    -0.41 |       56 | 25.29%     | ok               |
|          45 | -36.71%  | -82.59%            | -52.51% |    -0.44 |       50 | 30.27%     | ok               |
|          35 | -55.28%  | -82.59%            | -61.83% |    -0.57 |       78 | 41.00%     | ok               |
|          20 | -62.26%  | -82.59%            | -65.30% |    -0.63 |       94 | 60.34%     | ok               |
|          40 | -48.03%  | -82.59%            | -52.18% |    -0.64 |       54 | 33.52%     | ok               |

## DXY-INDEX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -1.24%   | -0.47%             | -6.02%  |    -0.18 |       40 | 30.59%     | ok               |
|          15 | -2.63%   | -0.47%             | -11.37% |    -0.22 |       82 | 77.01%     | ok               |
|          40 | -3.77%   | -0.47%             | -7.30%  |    -0.47 |       74 | 50.33%     | ok               |
|          30 | -4.25%   | -0.47%             | -9.61%  |    -0.48 |       72 | 62.04%     | ok               |
|          25 | -5.22%   | -0.47%             | -12.10% |    -0.56 |       78 | 67.25%     | ok               |

## EEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -4.96%   | 60.93%             | -19.52% |    -0.11 |       64 | 39.77%     | ok               |
|          35 | -5.62%   | 60.93%             | -23.88% |    -0.12 |       66 | 41.76%     | ok               |
|          50 | -4.94%   | 60.93%             | -15.88% |    -0.12 |       52 | 35.77%     | ok               |
|          45 | -6.04%   | 60.93%             | -17.36% |    -0.16 |       54 | 37.44%     | ok               |
|          25 | -8.49%   | 60.93%             | -25.60% |    -0.21 |       65 | 44.76%     | ok               |

## EFA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -3.05%   | 35.72%             | -10.80% |    -0.05 |       62 | 52.41%     | ok               |
|          30 | -7.42%   | 35.72%             | -13.02% |    -0.26 |       60 | 44.26%     | ok               |
|          20 | -9.78%   | 35.72%             | -12.73% |    -0.34 |       69 | 49.42%     | ok               |
|          40 | -8.83%   | 35.72%             | -14.90% |    -0.35 |       64 | 40.43%     | ok               |
|          50 | -9.07%   | 35.72%             | -17.56% |    -0.4  |       54 | 36.27%     | ok               |

## EOG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -17.51%  | 22.94%             | -39.69% |    -0.39 |       58 | 32.78%     | ok               |
|          30 | -22.29%  | 22.94%             | -48.13% |    -0.46 |       81 | 46.59%     | ok               |
|          40 | -22.39%  | 22.94%             | -43.26% |    -0.52 |       66 | 36.11%     | ok               |
|          35 | -23.14%  | 22.94%             | -46.26% |    -0.52 |       79 | 41.26%     | ok               |
|          25 | -26.23%  | 22.94%             | -51.99% |    -0.54 |       82 | 49.58%     | ok               |

## ETC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -5.69%   | -66.02%            | -27.89% |     0.02 |       28 | 16.67%     | ok               |
|          35 | -12.96%  | -66.02%            | -42.62% |    -0.07 |       44 | 26.63%     | ok               |
|          45 | -14.03%  | -66.02%            | -35.44% |    -0.13 |       26 | 18.58%     | ok               |
|          40 | -19.12%  | -66.02%            | -40.48% |    -0.22 |       42 | 22.41%     | ok               |
|          30 | -34.12%  | -66.02%            | -46.77% |    -0.47 |       64 | 30.84%     | ok               |

## ETH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 122.51%  | -32.60%            | -30.11% |     1.11 |       64 | 44.83%     | ok               |
|          30 | 104.30%  | -32.60%            | -32.89% |     0.99 |       68 | 53.07%     | ok               |
|          40 | 35.95%   | -32.60%            | -33.11% |     0.57 |       62 | 36.97%     | ok               |
|          20 | 38.83%   | -32.60%            | -39.10% |     0.57 |       84 | 62.64%     | ok               |
|          25 | 37.80%   | -32.60%            | -40.90% |     0.56 |       68 | 58.43%     | ok               |

## EWJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -18.16%  | 37.10%             | -30.73% |    -0.59 |       62 | 39.10%     | ok               |
|          20 | -19.55%  | 37.10%             | -31.32% |    -0.62 |       58 | 41.10%     | ok               |
|          45 | -18.94%  | 37.10%             | -27.68% |    -0.72 |       58 | 31.28%     | ok               |
|          25 | -21.87%  | 37.10%             | -31.18% |    -0.72 |       58 | 40.10%     | ok               |
|          35 | -22.08%  | 37.10%             | -32.54% |    -0.75 |       68 | 37.44%     | ok               |

## FCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -4.31%   | 54.44%             | -27.70% |     0.06 |       52 | 29.78%     | ok               |
|          45 | -8.44%   | 54.44%             | -35.18% |    -0    |       52 | 34.28%     | ok               |
|          40 | -19.35%  | 54.44%             | -43.57% |    -0.19 |       62 | 38.60%     | ok               |
|          30 | -27.81%  | 54.44%             | -47.47% |    -0.31 |       63 | 45.26%     | ok               |
|          20 | -34.13%  | 54.44%             | -57.65% |    -0.39 |       70 | 51.91%     | ok               |

## FET-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -3.70%   | -78.33%            | -59.41% |     0.28 |       88 | 51.72%     | ok               |
|          15 | -18.09%  | -78.33%            | -59.58% |     0.17 |       84 | 55.56%     | ok               |
|          25 | -37.00%  | -78.33%            | -59.96% |    -0.08 |       91 | 45.40%     | ok               |
|          30 | -38.66%  | -78.33%            | -54.02% |    -0.13 |       83 | 41.38%     | ok               |
|          35 | -53.63%  | -78.33%            | -62.73% |    -0.5  |       69 | 33.72%     | ok               |

## FIL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -24.59%  | -77.29%            | -39.40% |    -0.23 |       48 | 23.18%     | ok               |
|          35 | -43.92%  | -77.29%            | -47.50% |    -0.59 |       58 | 27.39%     | ok               |
|          30 | -46.58%  | -77.29%            | -50.22% |    -0.6  |       70 | 32.95%     | ok               |
|          45 | -39.88%  | -77.29%            | -43.98% |    -0.61 |       42 | 17.24%     | ok               |
|          50 | -39.00%  | -77.29%            | -44.95% |    -0.69 |       36 | 12.64%     | ok               |

## FXI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -6.30%   | 44.95%             | -22.57% |    -0.07 |       44 | 31.28%     | ok               |
|          30 | -6.84%   | 44.95%             | -23.91% |    -0.09 |       44 | 30.12%     | ok               |
|          45 | -6.49%   | 44.95%             | -26.75% |    -0.09 |       44 | 24.63%     | ok               |
|          15 | -9.00%   | 44.95%             | -21.68% |    -0.13 |       52 | 34.78%     | ok               |
|          20 | -10.08%  | 44.95%             | -24.53% |    -0.16 |       50 | 32.45%     | ok               |

## GDX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 18.06%   | 173.16%            | -35.59% |     0.39 |       73 | 52.91%     | ok               |
|          40 | 13.85%   | 173.16%            | -31.87% |     0.35 |       64 | 42.93%     | ok               |
|          30 | 11.28%   | 173.16%            | -34.99% |     0.3  |       60 | 48.09%     | ok               |
|          35 | 8.95%    | 173.16%            | -32.37% |     0.27 |       68 | 45.26%     | ok               |
|          25 | 6.77%    | 173.16%            | -38.90% |     0.24 |       63 | 49.75%     | ok               |

## GDXJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -7.90%   | 194.17%            | -45.05% |     0.06 |       67 | 53.24%     | ok               |
|          30 | -23.13%  | 194.17%            | -44.93% |    -0.22 |       68 | 46.42%     | ok               |
|          50 | -20.22%  | 194.17%            | -44.94% |    -0.22 |       58 | 37.77%     | ok               |
|          25 | -26.54%  | 194.17%            | -47.26% |    -0.25 |       72 | 49.92%     | ok               |
|          35 | -26.76%  | 194.17%            | -43.49% |    -0.3  |       70 | 44.09%     | ok               |

## GE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 32.29%   | 196.89%            | -22.29% |     0.64 |       66 | 40.27%     | ok               |
|          45 | 22.31%   | 196.89%            | -25.68% |     0.49 |       74 | 43.09%     | ok               |
|          20 | 15.90%   | 196.89%            | -26.63% |     0.37 |       71 | 57.40%     | ok               |
|          35 | 14.83%   | 196.89%            | -27.11% |     0.36 |       80 | 48.42%     | ok               |
|          30 | 14.57%   | 196.89%            | -27.82% |     0.35 |       76 | 53.58%     | ok               |

## GLD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 35.28%   | 97.02%             | -14.61% |     0.82 |       46 | 48.42%     | ok               |
|          20 | 33.26%   | 97.02%             | -14.61% |     0.78 |       48 | 49.75%     | ok               |
|          30 | 28.84%   | 97.02%             | -16.63% |     0.71 |       48 | 47.25%     | ok               |
|          15 | 25.10%   | 97.02%             | -17.54% |     0.61 |       50 | 53.91%     | ok               |
|          35 | 18.77%   | 97.02%             | -17.29% |     0.51 |       52 | 45.92%     | ok               |

## GOOGL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 81.59%   | 150.86%            | -19.76% |     1.19 |       55 | 55.41%     | ok               |
|          30 | 76.69%   | 150.86%            | -20.41% |     1.15 |       61 | 52.91%     | ok               |
|          20 | 67.87%   | 150.86%            | -20.57% |     1.04 |       66 | 57.74%     | ok               |
|          35 | 59.50%   | 150.86%            | -22.85% |     1.03 |       69 | 47.75%     | ok               |
|          15 | 68.78%   | 150.86%            | -13.81% |     1.01 |       69 | 62.73%     | ok               |

## GRT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 16.20%   | -86.77%            | -35.66% |     0.39 |       42 | 21.46%     | ok               |
|          15 | -3.17%   | -86.77%            | -49.67% |     0.22 |       73 | 61.30%     | ok               |
|          45 | 2.68%    | -86.77%            | -46.59% |     0.21 |       48 | 26.82%     | ok               |
|          35 | -1.50%   | -86.77%            | -48.22% |     0.18 |       58 | 35.63%     | ok               |
|          20 | -6.53%   | -86.77%            | -46.47% |     0.18 |       81 | 55.75%     | ok               |

## GS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 21.11%   | 172.06%            | -20.56% |     0.47 |       74 | 61.06%     | ok               |
|          20 | 4.59%    | 172.06%            | -23.19% |     0.19 |       74 | 57.07%     | ok               |
|          40 | 0.08%    | 172.06%            | -17.88% |     0.09 |       72 | 45.26%     | ok               |
|          25 | -0.70%   | 172.06%            | -23.32% |     0.09 |       74 | 54.58%     | ok               |
|          30 | -2.38%   | 172.06%            | -22.13% |     0.05 |       76 | 52.08%     | ok               |

## HD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -7.53%   | -6.97%             | -17.69% |    -0.12 |       71 | 44.59%     | ok               |
|          25 | -8.25%   | -6.97%             | -18.51% |    -0.14 |       70 | 46.59%     | ok               |
|          45 | -12.36%  | -6.97%             | -20.74% |    -0.36 |       60 | 28.62%     | ok               |
|          15 | -17.44%  | -6.97%             | -27.26% |    -0.36 |      109 | 55.41%     | ok               |
|          35 | -15.13%  | -6.97%             | -22.98% |    -0.38 |       80 | 40.43%     | ok               |

## HON Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -13.43%  | 14.03%             | -21.17% |    -0.4  |       72 | 31.78%     | ok               |
|          45 | -15.16%  | 14.03%             | -19.99% |    -0.43 |       74 | 36.77%     | ok               |
|          40 | -23.52%  | 14.03%             | -26.29% |    -0.66 |       76 | 41.10%     | ok               |
|          35 | -26.77%  | 14.03%             | -29.07% |    -0.75 |       91 | 47.59%     | ok               |
|          30 | -29.10%  | 14.03%             | -31.48% |    -0.8  |       94 | 52.75%     | ok               |

## HYG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -7.98%   | 3.39%              | -7.98%  |    -0.96 |       70 | 29.28%     | ok               |
|          15 | -9.44%   | 3.39%              | -10.29% |    -1.02 |       88 | 41.10%     | ok               |
|          20 | -9.18%   | 3.39%              | -10.29% |    -1.03 |       86 | 38.94%     | ok               |
|          25 | -9.38%   | 3.39%              | -10.11% |    -1.06 |       83 | 36.61%     | ok               |
|          30 | -9.08%   | 3.39%              | -9.59%  |    -1.06 |       81 | 33.94%     | ok               |

## IBIT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 53.73%   | -7.34%             | -17.37% |     1.07 |       22 | 22.48%     | ok               |
|          15 | 56.91%   | -7.34%             | -19.20% |     0.96 |       40 | 40.05%     | ok               |
|          45 | 44.27%   | -7.34%             | -17.37% |     0.9  |       26 | 23.89%     | ok               |
|          40 | 38.04%   | -7.34%             | -17.78% |     0.81 |       26 | 25.76%     | ok               |
|          30 | 30.82%   | -7.34%             | -18.95% |     0.67 |       34 | 32.32%     | ok               |

## IBM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 17.55%   | 54.67%             | -28.20% |     0.4  |       92 | 61.90%     | ok               |
|          30 | 4.29%    | 54.67%             | -27.54% |     0.19 |       78 | 49.58%     | ok               |
|          35 | 1.60%    | 54.67%             | -27.54% |     0.13 |       72 | 45.26%     | ok               |
|          20 | -0.30%   | 54.67%             | -34.12% |     0.11 |       76 | 54.24%     | ok               |
|          50 | -1.96%   | 54.67%             | -22.50% |     0.05 |       54 | 32.78%     | ok               |

## ICP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -1.29%   | -69.09%            | -37.43% |     0.19 |       60 | 28.93%     | ok               |
|          30 | -12.97%  | -69.09%            | -50.29% |     0.12 |       77 | 35.06%     | ok               |
|          40 | -6.51%   | -69.09%            | -32.85% |     0.12 |       54 | 24.52%     | ok               |
|          50 | -19.17%  | -69.09%            | -43.65% |    -0.11 |       34 | 14.75%     | ok               |
|          20 | -45.00%  | -69.09%            | -58.71% |    -0.18 |       86 | 45.98%     | ok               |

## IEF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.92%   | -0.48%             | -9.79%  |    -0.82 |       70 | 42.26%     | ok               |
|          15 | -7.48%   | -0.48%             | -10.52% |    -0.88 |       69 | 43.76%     | ok               |
|          40 | -8.39%   | -0.48%             | -9.67%  |    -1.31 |       60 | 24.79%     | ok               |
|          45 | -8.07%   | -0.48%             | -9.73%  |    -1.33 |       50 | 22.80%     | ok               |
|          25 | -10.50%  | -0.48%             | -11.19% |    -1.34 |       76 | 39.43%     | ok               |

## IEMG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -2.71%   | 55.61%             | -22.13% |    -0.03 |       63 | 42.10%     | ok               |
|          50 | -3.60%   | 55.61%             | -14.40% |    -0.08 |       56 | 33.61%     | ok               |
|          40 | -3.90%   | 55.61%             | -18.89% |    -0.08 |       62 | 39.43%     | ok               |
|          45 | -3.81%   | 55.61%             | -15.40% |    -0.09 |       52 | 36.27%     | ok               |
|          25 | -7.00%   | 55.61%             | -25.58% |    -0.17 |       59 | 44.93%     | ok               |

## INJ-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -16.04%  | -65.65%            | -56.91% |    -0.02 |       44 | 22.22%     | ok               |
|          35 | -22.01%  | -65.65%            | -61.19% |    -0.04 |       60 | 32.18%     | ok               |
|          50 | -25.16%  | -65.65%            | -52.76% |    -0.19 |       48 | 19.16%     | ok               |
|          40 | -30.93%  | -65.65%            | -59.56% |    -0.21 |       50 | 28.35%     | ok               |
|          20 | -52.25%  | -65.65%            | -80.49% |    -0.39 |       78 | 46.55%     | ok               |

## INTC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 93.40%   | 137.00%            | -53.65% |     0.78 |       79 | 60.07%     | ok               |
|          45 | 76.11%   | 137.00%            | -49.32% |     0.74 |       60 | 34.28%     | ok               |
|          20 | 80.58%   | 137.00%            | -52.47% |     0.73 |       78 | 56.24%     | ok               |
|          25 | 75.50%   | 137.00%            | -56.41% |     0.72 |       75 | 51.58%     | ok               |
|          40 | 70.33%   | 137.00%            | -55.86% |     0.7  |       68 | 38.60%     | ok               |

## INTU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.28%   | -55.81%            | -40.73% |     0.11 |       69 | 27.95%     | ok               |
|          45 | -3.75%   | -55.81%            | -41.78% |     0.05 |       69 | 32.11%     | ok               |
|          40 | -10.06%  | -55.81%            | -45.16% |    -0.06 |       69 | 35.11%     | ok               |
|          35 | -16.93%  | -55.81%            | -46.77% |    -0.19 |       73 | 38.60%     | ok               |
|          25 | -20.70%  | -55.81%            | -40.60% |    -0.25 |       70 | 44.59%     | ok               |

## ITA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 0.81%    | 87.08%             | -21.48% |     0.09 |       76 | 38.44%     | ok               |
|          15 | -0.52%   | 87.08%             | -26.46% |     0.07 |       85 | 60.07%     | ok               |
|          30 | -2.69%   | 87.08%             | -23.75% |    -0    |       72 | 48.42%     | ok               |
|          35 | -4.76%   | 87.08%             | -23.16% |    -0.07 |       76 | 46.76%     | ok               |
|          40 | -5.85%   | 87.08%             | -20.58% |    -0.11 |       78 | 43.26%     | ok               |

## IWM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 9.59%    | 45.53%             | -13.48% |     0.39 |       50 | 37.10%     | ok               |
|          40 | 8.60%    | 45.53%             | -14.08% |     0.39 |       42 | 31.28%     | ok               |
|          30 | 9.40%    | 45.53%             | -12.83% |     0.39 |       48 | 35.77%     | ok               |
|          35 | 8.35%    | 45.53%             | -14.11% |     0.36 |       48 | 33.61%     | ok               |
|          20 | 5.27%    | 45.53%             | -14.01% |     0.24 |       60 | 38.10%     | ok               |

## JNJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 24.32%   | 64.66%             | -10.57% |     0.95 |       54 | 37.60%     | ok               |
|          45 | 14.41%   | 64.66%             | -13.35% |     0.59 |       56 | 42.60%     | ok               |
|          15 | 16.20%   | 64.66%             | -18.02% |     0.56 |       66 | 57.07%     | ok               |
|          40 | 11.91%   | 64.66%             | -14.77% |     0.48 |       62 | 46.76%     | ok               |
|          20 | 12.26%   | 64.66%             | -17.61% |     0.46 |       70 | 53.74%     | ok               |

## JPM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 18.09%   | 86.86%             | -15.90% |     0.61 |       52 | 41.10%     | ok               |
|          45 | 6.87%    | 86.86%             | -21.91% |     0.27 |       54 | 44.09%     | ok               |
|          40 | -7.24%   | 86.86%             | -28.47% |    -0.13 |       66 | 46.59%     | ok               |
|          20 | -13.48%  | 86.86%             | -33.59% |    -0.22 |       86 | 58.57%     | ok               |
|          35 | -12.70%  | 86.86%             | -27.43% |    -0.28 |       74 | 50.58%     | ok               |

## KO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 28.93%   | 41.86%             | -8.07%  |     1.03 |       49 | 37.77%     | ok               |
|          35 | 24.98%   | 41.86%             | -8.07%  |     0.93 |       52 | 36.44%     | ok               |
|          40 | 22.37%   | 41.86%             | -9.28%  |     0.9  |       54 | 33.28%     | ok               |
|          25 | 23.60%   | 41.86%             | -9.37%  |     0.86 |       55 | 40.43%     | ok               |
|          50 | 14.81%   | 41.86%             | -11.40% |     0.68 |       36 | 26.79%     | ok               |

## LDO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 29.54%   | -79.67%            | -46.95% |     0.51 |       83 | 52.68%     | ok               |
|          20 | 17.51%   | -79.67%            | -44.97% |     0.43 |       87 | 48.08%     | ok               |
|          50 | 18.61%   | -79.67%            | -48.04% |     0.41 |       48 | 17.05%     | ok               |
|          30 | 0.54%    | -79.67%            | -60.93% |     0.28 |       78 | 39.08%     | ok               |
|          35 | -1.70%   | -79.67%            | -62.61% |     0.23 |       76 | 32.18%     | ok               |

## LIN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 1.93%    | 21.41%             | -23.68% |     0.13 |       64 | 50.25%     | ok               |
|          25 | 1.65%    | 21.41%             | -22.01% |     0.12 |       63 | 42.26%     | ok               |
|          20 | -0.53%   | 21.41%             | -23.00% |     0.05 |       62 | 45.42%     | ok               |
|          35 | -2.02%   | 21.41%             | -21.18% |    -0.02 |       62 | 32.95%     | ok               |
|          30 | -2.65%   | 21.41%             | -21.53% |    -0.03 |       66 | 39.43%     | ok               |

## LINK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -18.56%  | -57.34%            | -50.48% |     0.04 |       74 | 42.15%     | ok               |
|          45 | -13.92%  | -57.34%            | -38.56% |     0.04 |       50 | 26.44%     | ok               |
|          50 | -13.50%  | -57.34%            | -36.98% |     0.02 |       40 | 21.07%     | ok               |
|          35 | -24.89%  | -57.34%            | -49.56% |    -0.06 |       60 | 36.59%     | ok               |
|          40 | -29.01%  | -57.34%            | -50.91% |    -0.15 |       56 | 30.84%     | ok               |

## LLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 3.37%    | 51.12%             | -38.23% |     0.18 |       46 | 37.27%     | ok               |
|          15 | -5.82%   | 51.12%             | -48.12% |     0.05 |       63 | 60.73%     | ok               |
|          45 | -8.26%   | 51.12%             | -42.66% |    -0.04 |       54 | 40.77%     | ok               |
|          20 | -20.98%  | 51.12%             | -51.34% |    -0.23 |       72 | 55.74%     | ok               |
|          25 | -22.29%  | 51.12%             | -53.47% |    -0.26 |       68 | 53.08%     | ok               |

## LRCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -9.31%   | 256.27%            | -60.45% |     0.09 |       83 | 54.74%     | ok               |
|          50 | -14.24%  | 256.27%            | -50.39% |    -0.02 |       80 | 36.44%     | ok               |
|          40 | -16.81%  | 256.27%            | -56.86% |    -0.03 |       72 | 42.26%     | ok               |
|          35 | -22.21%  | 256.27%            | -61.76% |    -0.1  |       80 | 44.26%     | ok               |
|          20 | -24.73%  | 256.27%            | -67.64% |    -0.12 |       87 | 50.42%     | ok               |

## LTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -12.22%  | -58.53%            | -44.78% |    -0    |       56 | 31.80%     | ok               |
|          35 | -22.47%  | -58.53%            | -54.86% |    -0.13 |       66 | 42.91%     | ok               |
|          40 | -31.40%  | -58.53%            | -56.10% |    -0.3  |       58 | 38.12%     | ok               |
|          30 | -35.18%  | -58.53%            | -53.76% |    -0.31 |       68 | 48.85%     | ok               |
|          25 | -37.91%  | -58.53%            | -54.26% |    -0.35 |       76 | 51.34%     | ok               |

## MCD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 2.85%    | -6.65%             | -9.22%  |     0.19 |       42 | 20.63%     | ok               |
|          30 | -2.55%   | -6.65%             | -18.81% |    -0.05 |       75 | 38.10%     | ok               |
|          25 | -3.59%   | -6.65%             | -20.47% |    -0.09 |       75 | 40.77%     | ok               |
|          35 | -7.68%   | -6.65%             | -15.45% |    -0.29 |       67 | 34.44%     | ok               |
|          40 | -7.95%   | -6.65%             | -16.86% |    -0.33 |       71 | 28.79%     | ok               |

## META Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -9.25%   | 38.75%             | -31.03% |    -0.09 |       66 | 37.60%     | ok               |
|          40 | -19.22%  | 38.75%             | -35.11% |    -0.3  |       66 | 40.60%     | ok               |
|          25 | -27.20%  | 38.75%             | -39.84% |    -0.43 |       67 | 51.25%     | ok               |
|          50 | -23.10%  | 38.75%             | -34.00% |    -0.44 |       70 | 33.78%     | ok               |
|          30 | -29.15%  | 38.75%             | -38.96% |    -0.5  |       72 | 48.09%     | ok               |

## MPC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 17.40%   | 74.63%             | -23.96% |     0.42 |       54 | 37.44%     | ok               |
|          45 | 9.96%    | 74.63%             | -25.09% |     0.29 |       60 | 41.10%     | ok               |
|          40 | 8.29%    | 74.63%             | -25.70% |     0.26 |       62 | 43.43%     | ok               |
|          35 | 4.94%    | 74.63%             | -35.90% |     0.2  |       70 | 45.92%     | ok               |
|          30 | -11.56%  | 74.63%             | -44.76% |    -0.09 |       73 | 48.75%     | ok               |

## MRK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -21.76%  | -2.94%             | -30.12% |    -0.41 |       89 | 55.24%     | ok               |
|          25 | -21.38%  | -2.94%             | -31.07% |    -0.44 |       74 | 47.25%     | ok               |
|          20 | -25.23%  | -2.94%             | -29.59% |    -0.54 |       79 | 50.58%     | ok               |
|          45 | -24.18%  | -2.94%             | -26.02% |    -0.65 |       59 | 33.44%     | ok               |
|          50 | -24.11%  | -2.94%             | -25.69% |    -0.7  |       56 | 30.28%     | ok               |

## MS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -3.32%   | 155.60%            | -19.99% |     0    |       72 | 41.43%     | ok               |
|          15 | -6.30%   | 155.60%            | -22.02% |    -0.04 |       75 | 58.40%     | ok               |
|          20 | -6.41%   | 155.60%            | -25.68% |    -0.06 |       79 | 54.58%     | ok               |
|          35 | -10.11%  | 155.60%            | -25.26% |    -0.17 |       78 | 46.09%     | ok               |
|          30 | -11.43%  | 155.60%            | -27.79% |    -0.19 |       79 | 49.75%     | ok               |

## MSFT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -22.13%  | -3.23%             | -25.26% |    -0.62 |       66 | 34.11%     | ok               |
|          50 | -23.55%  | -3.23%             | -26.14% |    -0.69 |       62 | 29.12%     | ok               |
|          35 | -34.48%  | -3.23%             | -35.38% |    -0.93 |       73 | 42.76%     | ok               |
|          40 | -33.86%  | -3.23%             | -34.77% |    -0.95 |       69 | 37.60%     | ok               |
|          25 | -37.88%  | -3.23%             | -40.21% |    -0.98 |       87 | 50.58%     | ok               |

## MU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 435.39%  | 1078.62%           | -61.96% |     1.57 |       47 | 67.39%     | ok               |
|          25 | 357.11%  | 1078.62%           | -67.90% |     1.51 |       47 | 61.56%     | ok               |
|          40 | 290.77%  | 1078.62%           | -64.07% |     1.4  |       56 | 55.24%     | ok               |
|          20 | 306.86%  | 1078.62%           | -67.25% |     1.39 |       53 | 63.39%     | ok               |
|          30 | 270.20%  | 1078.62%           | -68.76% |     1.34 |       51 | 59.90%     | ok               |

## NEAR-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 73.04%   | -40.87%            | -45.84% |     0.83 |       42 | 22.99%     | ok               |
|          50 | 45.50%   | -40.87%            | -51.20% |     0.65 |       38 | 18.01%     | ok               |
|          40 | 37.61%   | -40.87%            | -54.53% |     0.57 |       44 | 27.20%     | ok               |
|          35 | 15.68%   | -40.87%            | -58.86% |     0.38 |       68 | 32.38%     | ok               |
|          15 | -16.59%  | -40.87%            | -54.94% |     0.14 |       87 | 55.56%     | ok               |

## NEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 3.24%    | 178.49%            | -29.41% |     0.21 |       62 | 61.40%     | ok               |
|          20 | -7.81%   | 178.49%            | -30.47% |     0.07 |       72 | 56.91%     | ok               |
|          25 | -21.27%  | 178.49%            | -37.89% |    -0.14 |       68 | 54.74%     | ok               |
|          50 | -23.65%  | 178.49%            | -32.97% |    -0.25 |       56 | 40.77%     | ok               |
|          30 | -31.13%  | 178.49%            | -38.49% |    -0.33 |       72 | 53.08%     | ok               |

## NFLX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 45.70%   | 26.43%             | -16.28% |     1.03 |       48 | 38.44%     | ok               |
|          40 | 47.85%   | 26.43%             | -11.94% |     0.99 |       46 | 46.26%     | ok               |
|          35 | 40.25%   | 26.43%             | -18.30% |     0.83 |       60 | 49.75%     | ok               |
|          45 | 31.86%   | 26.43%             | -15.48% |     0.74 |       52 | 42.60%     | ok               |
|          25 | 34.03%   | 26.43%             | -21.09% |     0.71 |       62 | 57.07%     | ok               |

## NKE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -33.86%  | -57.72%            | -50.44% |    -0.42 |       93 | 52.58%     | ok               |
|          40 | -26.46%  | -57.72%            | -31.19% |    -0.5  |       63 | 30.12%     | ok               |
|          15 | -38.38%  | -57.72%            | -55.52% |    -0.51 |       91 | 56.91%     | ok               |
|          25 | -45.09%  | -57.72%            | -52.84% |    -0.79 |       91 | 48.59%     | ok               |
|          35 | -39.10%  | -57.72%            | -43.08% |    -0.8  |       75 | 37.10%     | ok               |

## NOW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 14.38%   | -27.28%            | -26.36% |     0.34 |       81 | 51.75%     | ok               |
|          30 | 10.73%   | -27.28%            | -28.87% |     0.29 |       84 | 45.59%     | ok               |
|          15 | 6.71%    | -27.28%            | -26.36% |     0.25 |       92 | 54.91%     | ok               |
|          25 | 4.01%    | -27.28%            | -25.99% |     0.22 |       76 | 49.08%     | ok               |
|          35 | 2.54%    | -27.28%            | -28.56% |     0.18 |       83 | 39.93%     | ok               |

## NVDA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -5.51%   | 132.83%            | -35.26% |     0.08 |       74 | 47.95%     | ok               |
|          20 | -11.01%  | 132.83%            | -40.59% |     0.03 |       70 | 55.97%     | ok               |
|          25 | -10.87%  | 132.83%            | -33.22% |     0.01 |       71 | 50.98%     | ok               |
|          50 | -14.29%  | 132.83%            | -40.84% |    -0.11 |       56 | 32.09%     | ok               |
|          35 | -18.28%  | 132.83%            | -41.25% |    -0.14 |       82 | 45.10%     | ok               |

## OP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 27.06%   | -90.75%            | -36.11% |     0.51 |       30 | 11.11%     | ok               |
|          45 | 26.15%   | -90.75%            | -45.76% |     0.48 |       32 | 15.71%     | ok               |
|          40 | 7.79%    | -90.75%            | -53.61% |     0.29 |       46 | 24.14%     | ok               |
|          35 | -10.29%  | -90.75%            | -58.33% |     0.09 |       54 | 27.20%     | ok               |
|          30 | -26.66%  | -90.75%            | -70.27% |    -0.07 |       70 | 33.72%     | ok               |

## ORCL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 230.00%  | 18.17%             | -29.32% |     1.34 |       72 | 65.39%     | ok               |
|          25 | 147.55%  | 18.17%             | -27.76% |     1.09 |       73 | 57.90%     | ok               |
|          20 | 143.30%  | 18.17%             | -29.32% |     1.06 |       75 | 61.06%     | ok               |
|          35 | 110.57%  | 18.17%             | -31.95% |     0.95 |       66 | 49.92%     | ok               |
|          30 | 110.75%  | 18.17%             | -29.47% |     0.94 |       72 | 54.08%     | ok               |

## OXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 5.91%    | -9.43%             | -29.57% |     0.22 |       38 | 27.79%     | ok               |
|          35 | 2.89%    | -9.43%             | -30.05% |     0.17 |       70 | 39.77%     | ok               |
|          30 | 0.41%    | -9.43%             | -34.15% |     0.13 |       71 | 45.26%     | ok               |
|          40 | 0.51%    | -9.43%             | -31.66% |     0.12 |       56 | 35.11%     | ok               |
|          45 | -6.60%   | -9.43%             | -34.84% |    -0.03 |       44 | 29.95%     | ok               |

## PEP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 11.74%   | -16.73%            | -11.62% |     0.53 |       44 | 26.79%     | ok               |
|          45 | 2.18%    | -16.73%            | -14.22% |     0.14 |       64 | 31.11%     | ok               |
|          35 | -1.13%   | -16.73%            | -21.42% |     0.03 |       83 | 42.10%     | ok               |
|          40 | -1.01%   | -16.73%            | -18.04% |     0.02 |       76 | 37.10%     | ok               |
|          30 | -6.85%   | -16.73%            | -21.35% |    -0.14 |       79 | 48.75%     | ok               |

## PEPE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 0.11%    | -71.74%            | -57.66% |     0.28 |       79 | 44.83%     | ok               |
|          15 | -10.45%  | -71.74%            | -64.84% |     0.26 |       82 | 60.92%     | ok               |
|          35 | -5.60%   | -71.74%            | -51.35% |     0.2  |       64 | 39.46%     | ok               |
|          25 | -19.56%  | -71.74%            | -53.88% |     0.1  |       89 | 50.57%     | ok               |
|          20 | -30.18%  | -71.74%            | -64.07% |     0.02 |       88 | 57.28%     | ok               |

## PFE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -24.41%  | -11.37%            | -25.61% |    -0.92 |       52 | 19.13%     | ok               |
|          50 | -26.23%  | -11.37%            | -27.28% |    -1.12 |       38 | 15.31%     | ok               |
|          40 | -31.46%  | -11.37%            | -32.57% |    -1.14 |       74 | 24.13%     | ok               |
|          35 | -35.66%  | -11.37%            | -36.57% |    -1.2  |       84 | 31.78%     | ok               |
|          30 | -40.21%  | -11.37%            | -41.06% |    -1.29 |       77 | 35.94%     | ok               |

## PG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -6.76%   | -5.80%             | -20.08% |    -0.23 |       58 | 33.94%     | ok               |
|          35 | -9.94%   | -5.80%             | -18.99% |    -0.35 |       66 | 37.44%     | ok               |
|          30 | -18.12%  | -5.80%             | -24.55% |    -0.68 |       68 | 40.60%     | ok               |
|          45 | -15.87%  | -5.80%             | -22.43% |    -0.68 |       58 | 31.45%     | ok               |
|          25 | -19.97%  | -5.80%             | -26.21% |    -0.75 |       80 | 42.10%     | ok               |

## PM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -1.37%   | 100.99%            | -32.20% |     0.06 |       88 | 52.41%     | ok               |
|          20 | -4.51%   | 100.99%            | -31.89% |     0    |       89 | 61.23%     | ok               |
|          30 | -4.27%   | 100.99%            | -33.68% |     0    |       85 | 56.07%     | ok               |
|          50 | -6.95%   | 100.99%            | -35.70% |    -0.09 |       74 | 42.10%     | ok               |
|          40 | -9.32%   | 100.99%            | -37.94% |    -0.14 |       82 | 48.59%     | ok               |

## POL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 39.71%   | -73.19%            | -46.45% |     0.6  |       79 | 46.74%     | ok               |
|          25 | 25.30%   | -73.19%            | -46.72% |     0.47 |       70 | 54.79%     | ok               |
|          20 | 14.35%   | -73.19%            | -52.88% |     0.37 |       80 | 60.15%     | ok               |
|          15 | -8.23%   | -73.19%            | -58.42% |     0.16 |       80 | 65.90%     | ok               |
|          50 | -2.42%   | -73.19%            | -22.81% |     0.09 |       52 | 18.77%     | ok               |

## QCOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -3.88%   | 20.49%             | -54.50% |     0.12 |       71 | 47.75%     | ok               |
|          35 | -4.42%   | 20.49%             | -50.58% |     0.11 |       77 | 43.59%     | ok               |
|          20 | -7.78%   | 20.49%             | -54.38% |     0.08 |       67 | 50.58%     | ok               |
|          30 | -15.25%  | 20.49%             | -56.59% |    -0.04 |       73 | 46.09%     | ok               |
|          15 | -23.11%  | 20.49%             | -57.94% |    -0.13 |       71 | 53.74%     | ok               |

## QQQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 22.38%   | 65.30%             | -12.88% |     0.61 |       59 | 47.09%     | ok               |
|          15 | 22.91%   | 65.30%             | -14.17% |     0.58 |       63 | 52.58%     | ok               |
|          30 | 18.39%   | 65.30%             | -12.88% |     0.54 |       64 | 44.26%     | ok               |
|          20 | 19.43%   | 65.30%             | -12.98% |     0.53 |       67 | 49.75%     | ok               |
|          35 | 6.28%    | 65.30%             | -18.29% |     0.25 |       70 | 40.60%     | ok               |

## RENDER-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 45.25%   | -64.47%            | -43.43% |     0.61 |       88 | 54.03%     | ok               |
|          15 | 34.05%   | -64.47%            | -44.59% |     0.55 |       88 | 57.37%     | ok               |
|          25 | 15.90%   | -64.47%            | -40.60% |     0.42 |       90 | 49.71%     | ok               |
|          30 | -19.07%  | -64.47%            | -45.00% |     0.1  |       98 | 43.03%     | ok               |
|          35 | -31.74%  | -64.47%            | -41.33% |    -0.12 |       84 | 34.77%     | ok               |

## RTX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 32.98%   | 115.79%            | -18.66% |     0.76 |       76 | 56.07%     | ok               |
|          25 | 28.03%   | 115.79%            | -18.59% |     0.68 |       64 | 52.75%     | ok               |
|          50 | 22.59%   | 115.79%            | -18.42% |     0.67 |       56 | 41.93%     | ok               |
|          35 | 23.35%   | 115.79%            | -18.00% |     0.65 |       54 | 49.58%     | ok               |
|          30 | 26.08%   | 115.79%            | -16.99% |     0.65 |       58 | 51.58%     | ok               |

## SBUX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -13.56%  | 15.15%             | -23.55% |    -0.21 |       66 | 43.09%     | ok               |
|          45 | -17.65%  | 15.15%             | -27.26% |    -0.4  |       72 | 30.12%     | ok               |
|          40 | -20.49%  | 15.15%             | -27.43% |    -0.45 |       68 | 33.94%     | ok               |
|          30 | -22.57%  | 15.15%             | -29.22% |    -0.45 |       69 | 40.93%     | ok               |
|          20 | -26.00%  | 15.15%             | -32.17% |    -0.48 |       71 | 44.76%     | ok               |

## SCHW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 10.61%   | 58.98%             | -16.53% |     0.36 |       56 | 34.61%     | ok               |
|          50 | 1.73%    | 58.98%             | -13.28% |     0.12 |       58 | 31.61%     | ok               |
|          25 | 0.18%    | 58.98%             | -28.76% |     0.1  |       61 | 49.58%     | ok               |
|          40 | -0.86%   | 58.98%             | -23.35% |     0.05 |       64 | 37.60%     | ok               |
|          20 | -4.04%   | 58.98%             | -29.24% |     0    |       71 | 51.91%     | ok               |

## SHIB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -12.93%  | -74.16%            | -49.21% |     0.1  |       80 | 68.97%     | ok               |
|          25 | -21.90%  | -74.16%            | -43.85% |    -0.04 |       77 | 59.20%     | ok               |
|          20 | -23.85%  | -74.16%            | -46.38% |    -0.05 |       81 | 63.98%     | ok               |
|          35 | -22.28%  | -74.16%            | -53.32% |    -0.1  |       66 | 45.79%     | ok               |
|          40 | -27.93%  | -74.16%            | -49.96% |    -0.21 |       56 | 38.12%     | ok               |

## SHY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          30 | -2.24%   | 0.16%              | -2.85% |    -0.79 |       48 | 34.28%     | ok               |
|          35 | -2.36%   | 0.16%              | -3.27% |    -0.84 |       50 | 32.45%     | ok               |
|          40 | -2.47%   | 0.16%              | -3.33% |    -0.89 |       50 | 30.62%     | ok               |
|          45 | -2.45%   | 0.16%              | -3.23% |    -0.9  |       48 | 27.45%     | ok               |
|          50 | -2.62%   | 0.16%              | -3.40% |    -1.01 |       44 | 24.63%     | ok               |

## SKY-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -28.56%  | 2.61%              | -43.98% |    -0.34 |       70 | 40.04%     | ok               |
|          15 | -32.92%  | 2.61%              | -56.39% |    -0.34 |       60 | 50.00%     | ok               |
|          25 | -32.22%  | 2.61%              | -48.09% |    -0.4  |       65 | 43.58%     | ok               |
|          20 | -42.55%  | 2.61%              | -58.40% |    -0.58 |       62 | 47.12%     | ok               |
|          35 | -39.77%  | 2.61%              | -49.68% |    -0.69 |       64 | 33.85%     | ok               |

## SLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 20.91%   | -2.49%             | -21.46% |     0.51 |       52 | 33.44%     | ok               |
|          40 | 17.22%   | -2.49%             | -25.33% |     0.44 |       48 | 37.10%     | ok               |
|          50 | -0.69%   | -2.49%             | -29.64% |     0.07 |       50 | 28.95%     | ok               |
|          35 | -13.95%  | -2.49%             | -43.52% |    -0.19 |       76 | 44.76%     | ok               |
|          30 | -25.39%  | -2.49%             | -54.23% |    -0.43 |       75 | 51.25%     | ok               |

## SLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 65.90%   | 143.85%            | -34.72% |     0.84 |       54 | 34.94%     | ok               |
|          45 | 63.89%   | 143.85%            | -32.46% |     0.82 |       60 | 36.11%     | ok               |
|          40 | 61.93%   | 143.85%            | -31.93% |     0.8  |       66 | 38.27%     | ok               |
|          35 | 55.47%   | 143.85%            | -36.89% |     0.74 |       68 | 40.43%     | ok               |
|          30 | 51.45%   | 143.85%            | -42.66% |     0.7  |       58 | 42.93%     | ok               |

## SMH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 109.66%  | 190.27%            | -30.17% |     1.28 |       47 | 51.08%     | ok               |
|          35 | 87.64%   | 190.27%            | -34.36% |     1.15 |       54 | 46.92%     | ok               |
|          25 | 87.50%   | 190.27%            | -32.94% |     1.13 |       46 | 49.92%     | ok               |
|          30 | 85.29%   | 190.27%            | -33.99% |     1.12 |       48 | 48.25%     | ok               |
|          45 | 71.81%   | 190.27%            | -32.75% |     1.07 |       52 | 41.10%     | ok               |

## SNX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 2.84%    | -76.30%            | -43.20% |     0.3  |       71 | 47.89%     | ok               |
|          35 | -6.26%   | -76.30%            | -30.08% |     0.17 |       62 | 30.84%     | ok               |
|          30 | -15.26%  | -76.30%            | -34.76% |     0.08 |       58 | 37.93%     | ok               |
|          15 | -30.74%  | -76.30%            | -44.00% |    -0.03 |       81 | 52.49%     | ok               |
|          40 | -18.26%  | -76.30%            | -40.36% |    -0.04 |       52 | 24.90%     | ok               |

## SOL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 9.10%    | -62.57%            | -51.50% |     0.33 |       60 | 37.36%     | ok               |
|          25 | -20.42%  | -62.57%            | -52.40% |     0.05 |       72 | 56.70%     | ok               |
|          45 | -16.39%  | -62.57%            | -59.86% |     0.03 |       62 | 31.80%     | ok               |
|          35 | -22.95%  | -62.57%            | -61.91% |     0    |       76 | 45.21%     | ok               |
|          15 | -27.74%  | -62.57%            | -59.14% |    -0.02 |       74 | 63.22%     | ok               |

## SOXX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 87.36%   | 165.68%            | -40.27% |     1.08 |       55 | 49.58%     | ok               |
|          35 | 83.42%   | 165.68%            | -38.63% |     1.07 |       59 | 44.76%     | ok               |
|          25 | 83.77%   | 165.68%            | -41.42% |     1.05 |       53 | 49.25%     | ok               |
|          15 | 82.65%   | 165.68%            | -39.35% |     1.01 |       68 | 52.41%     | ok               |
|          30 | 73.45%   | 165.68%            | -41.89% |     0.97 |       57 | 47.09%     | ok               |

## SPY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 15.04%   | 49.98%             | -14.25% |     0.53 |       61 | 53.91%     | ok               |
|          15 | 13.46%   | 49.98%             | -16.80% |     0.47 |       70 | 57.07%     | ok               |
|          25 | 7.88%    | 49.98%             | -15.22% |     0.32 |       61 | 52.91%     | ok               |
|          30 | 3.32%    | 49.98%             | -16.47% |     0.18 |       64 | 50.08%     | ok               |
|          35 | 2.70%    | 49.98%             | -16.72% |     0.16 |       60 | 47.09%     | ok               |

## SUSHI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -23.49%  | -80.59%            | -40.08% |    -0.19 |       52 | 14.75%     | ok               |
|          45 | -58.58%  | -80.59%            | -64.27% |    -0.77 |       56 | 18.20%     | ok               |
|          40 | -61.52%  | -80.59%            | -68.16% |    -0.77 |       63 | 24.71%     | ok               |
|          35 | -74.29%  | -80.59%            | -79.91% |    -1.05 |       80 | 30.46%     | ok               |
|          15 | -80.79%  | -80.59%            | -80.79% |    -1.05 |       91 | 47.51%     | ok               |

## T Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 62.74%   | 26.99%             | -18.13% |     1.19 |       58 | 56.91%     | ok               |
|          25 | 57.69%   | 26.99%             | -17.66% |     1.13 |       60 | 54.74%     | ok               |
|          15 | 53.85%   | 26.99%             | -15.08% |     1.04 |       67 | 60.73%     | ok               |
|          30 | 40.41%   | 26.99%             | -17.01% |     0.89 |       64 | 52.75%     | ok               |
|          35 | 25.97%   | 26.99%             | -14.49% |     0.66 |       66 | 49.25%     | ok               |

## TGT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -10.79%  | -9.92%             | -42.86% |    -0.1  |       83 | 47.25%     | ok               |
|          45 | -9.25%   | -9.92%             | -29.07% |    -0.14 |       54 | 29.45%     | ok               |
|          30 | -11.04%  | -9.92%             | -40.57% |    -0.14 |       60 | 39.43%     | ok               |
|          25 | -11.68%  | -9.92%             | -43.36% |    -0.14 |       65 | 42.26%     | ok               |
|          15 | -16.43%  | -9.92%             | -40.77% |    -0.2  |       73 | 51.91%     | ok               |

## TIA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 2.90%    | -86.79%            | -46.58% |     0.22 |       52 | 18.58%     | ok               |
|          35 | -2.69%   | -86.79%            | -49.70% |     0.2  |       64 | 30.65%     | ok               |
|          40 | -2.28%   | -86.79%            | -42.29% |     0.19 |       66 | 25.86%     | ok               |
|          50 | 1.89%    | -86.79%            | -46.02% |     0.18 |       32 | 11.49%     | ok               |
|          30 | -42.33%  | -86.79%            | -66.21% |    -0.27 |       89 | 36.21%     | ok               |

## TLT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -13.64%  | -9.48%             | -14.86% |    -1.58 |       34 | 14.48%     | ok               |
|          30 | -21.12%  | -9.48%             | -21.75% |    -1.63 |       70 | 31.95%     | ok               |
|          40 | -18.15%  | -9.48%             | -18.63% |    -1.79 |       60 | 20.97%     | ok               |
|          35 | -20.61%  | -9.48%             | -21.08% |    -1.85 |       68 | 25.96%     | ok               |
|          45 | -16.96%  | -9.48%             | -17.71% |    -1.88 |       42 | 16.97%     | ok               |

## TMO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 47.05%   | -3.53%             | -8.17%  |     1.05 |       40 | 31.61%     | ok               |
|          45 | 42.78%   | -3.53%             | -10.13% |     0.93 |       46 | 36.44%     | ok               |
|          40 | 40.67%   | -3.53%             | -9.91%  |     0.88 |       49 | 40.93%     | ok               |
|          35 | 22.76%   | -3.53%             | -14.06% |     0.55 |       61 | 45.42%     | ok               |
|          30 | 15.04%   | -3.53%             | -18.85% |     0.39 |       61 | 50.08%     | ok               |

## TMUS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 8.91%    | 17.46%             | -30.05% |     0.28 |       65 | 60.40%     | ok               |
|          30 | 7.70%    | 17.46%             | -25.71% |     0.26 |       70 | 48.42%     | ok               |
|          20 | 2.63%    | 17.46%             | -29.75% |     0.16 |       71 | 54.74%     | ok               |
|          25 | -0.81%   | 17.46%             | -31.45% |     0.08 |       75 | 50.92%     | ok               |
|          35 | -4.65%   | 17.46%             | -34.23% |    -0.01 |       70 | 45.26%     | ok               |

## TRX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 6.87%    | 40.26%             | -18.79% |     0.28 |       52 | 37.16%     | ok               |
|          30 | 0.99%    | 40.26%             | -22.90% |     0.12 |       72 | 49.04%     | ok               |
|          50 | 0.66%    | 40.26%             | -18.49% |     0.1  |       44 | 31.99%     | ok               |
|          20 | -0.08%   | 40.26%             | -25.45% |     0.1  |       63 | 55.94%     | ok               |
|          35 | 0.16%    | 40.26%             | -21.77% |     0.09 |       68 | 45.79%     | ok               |

## TSLA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 64.97%   | 97.43%             | -31.33% |     0.77 |       64 | 34.44%     | ok               |
|          50 | 48.84%   | 97.43%             | -33.23% |     0.67 |       64 | 29.78%     | ok               |
|          45 | 39.76%   | 97.43%             | -32.54% |     0.58 |       68 | 31.78%     | ok               |
|          35 | 27.32%   | 97.43%             | -37.58% |     0.46 |       71 | 36.94%     | ok               |
|          30 | 5.29%    | 97.43%             | -42.22% |     0.25 |       69 | 40.93%     | ok               |

## TXN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 16.55%   | 86.16%             | -45.45% |     0.38 |       66 | 34.78%     | ok               |
|          20 | 3.03%    | 86.16%             | -38.49% |     0.19 |       61 | 59.57%     | ok               |
|          35 | -0.62%   | 86.16%             | -43.28% |     0.13 |       76 | 49.92%     | ok               |
|          15 | -2.86%   | 86.16%             | -38.99% |     0.12 |       66 | 63.39%     | ok               |
|          40 | -2.67%   | 86.16%             | -45.67% |     0.09 |       70 | 47.42%     | ok               |

## UNH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 29.63%   | -17.73%            | -36.82% |     0.54 |       56 | 31.28%     | ok               |
|          30 | 30.65%   | -17.73%            | -27.86% |     0.53 |       74 | 52.58%     | ok               |
|          15 | 29.33%   | -17.73%            | -32.14% |     0.5  |       75 | 67.55%     | ok               |
|          35 | 27.09%   | -17.73%            | -29.20% |     0.49 |       66 | 47.42%     | ok               |
|          40 | 22.82%   | -17.73%            | -35.73% |     0.45 |       60 | 42.76%     | ok               |

## UNI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -21.52%  | -61.06%            | -58.49% |    -0.04 |       56 | 27.01%     | ok               |
|          40 | -26.27%  | -61.06%            | -63.75% |    -0.09 |       60 | 32.38%     | ok               |
|          50 | -29.10%  | -61.06%            | -57.60% |    -0.19 |       54 | 21.46%     | ok               |
|          35 | -38.78%  | -61.06%            | -68.71% |    -0.22 |       72 | 37.74%     | ok               |
|          30 | -73.46%  | -61.06%            | -80.61% |    -0.9  |       88 | 43.68%     | ok               |

## UPS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -32.05%  | -23.93%            | -43.07% |    -0.57 |       82 | 47.92%     | ok               |
|          25 | -33.13%  | -23.93%            | -39.04% |    -0.62 |       78 | 44.43%     | ok               |
|          35 | -31.83%  | -23.93%            | -37.47% |    -0.62 |       63 | 33.28%     | ok               |
|          15 | -36.18%  | -23.93%            | -43.86% |    -0.67 |       90 | 52.75%     | ok               |
|          30 | -35.48%  | -23.93%            | -37.08% |    -0.7  |       70 | 39.27%     | ok               |

## USO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 14.54%   | 60.45%             | -44.16% |     0.34 |       74 | 38.77%     | ok               |
|          45 | 13.53%   | 60.45%             | -33.18% |     0.34 |       50 | 25.79%     | ok               |
|          15 | 10.07%   | 60.45%             | -43.85% |     0.28 |       75 | 42.10%     | ok               |
|          30 | 5.74%    | 60.45%             | -43.35% |     0.22 |       66 | 33.44%     | ok               |
|          25 | 5.58%    | 60.45%             | -43.43% |     0.22 |       66 | 36.27%     | ok               |

## VEA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 5.44%    | 45.15%             | -16.28% |     0.25 |       60 | 50.58%     | ok               |
|          20 | 1.19%    | 45.15%             | -17.70% |     0.1  |       61 | 47.92%     | ok               |
|          25 | -0.82%   | 45.15%             | -17.79% |     0.02 |       57 | 46.26%     | ok               |
|          30 | -0.98%   | 45.15%             | -17.93% |     0.01 |       58 | 44.09%     | ok               |
|          35 | -2.09%   | 45.15%             | -16.79% |    -0.03 |       56 | 43.09%     | ok               |

## VIXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -46.17%  | -63.33%            | -68.69% |    -0.39 |       44 | 10.32%     | ok               |
|          45 | -56.13%  | -63.33%            | -74.13% |    -0.55 |       56 | 16.31%     | ok               |
|          40 | -65.03%  | -63.33%            | -80.03% |    -0.67 |       72 | 20.80%     | ok               |
|          35 | -68.25%  | -63.33%            | -83.81% |    -0.7  |       88 | 26.12%     | ok               |
|          15 | -77.15%  | -63.33%            | -89.47% |    -0.77 |      101 | 44.76%     | ok               |

## VNQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -7.59%   | 15.95%             | -19.07% |    -0.32 |       58 | 28.45%     | ok               |
|          50 | -8.03%   | 15.95%             | -17.13% |    -0.36 |       54 | 25.96%     | ok               |
|          25 | -12.21%  | 15.95%             | -22.34% |    -0.47 |       69 | 40.60%     | ok               |
|          20 | -13.82%  | 15.95%             | -23.79% |    -0.53 |       72 | 43.26%     | ok               |
|          15 | -14.61%  | 15.95%             | -24.90% |    -0.55 |       67 | 44.59%     | ok               |

## VTI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 18.11%   | 48.83%             | -13.96% |     0.62 |       64 | 54.91%     | ok               |
|          15 | 12.07%   | 48.83%             | -15.70% |     0.43 |       67 | 57.40%     | ok               |
|          25 | 4.46%    | 48.83%             | -16.10% |     0.21 |       60 | 52.91%     | ok               |
|          30 | -3.73%   | 48.83%             | -18.77% |    -0.07 |       72 | 50.75%     | ok               |
|          35 | -6.15%   | 48.83%             | -21.19% |    -0.17 |       66 | 47.59%     | ok               |

## VWO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -7.30%   | 43.08%             | -21.18% |    -0.25 |       60 | 32.61%     | ok               |
|          15 | -9.03%   | 43.08%             | -24.01% |    -0.26 |       69 | 49.42%     | ok               |
|          20 | -10.06%  | 43.08%             | -26.14% |    -0.31 |       67 | 47.25%     | ok               |
|          40 | -8.98%   | 43.08%             | -23.57% |    -0.31 |       70 | 37.94%     | ok               |
|          45 | -9.11%   | 43.08%             | -23.26% |    -0.33 |       62 | 35.11%     | ok               |

## VZ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -6.80%   | 5.41%              | -12.71% |    -0.19 |       50 | 24.29%     | ok               |
|          45 | -17.18%  | 5.41%              | -20.47% |    -0.57 |       62 | 27.79%     | ok               |
|          35 | -19.65%  | 5.41%              | -19.99% |    -0.63 |       61 | 33.78%     | ok               |
|          25 | -22.39%  | 5.41%              | -24.67% |    -0.65 |       79 | 41.76%     | ok               |
|          40 | -23.64%  | 5.41%              | -23.64% |    -0.81 |       66 | 31.11%     | ok               |

## WFC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 0.56%    | 68.89%             | -18.29% |     0.08 |       60 | 35.27%     | ok               |
|          35 | -4.84%   | 68.89%             | -22.53% |    -0.02 |       81 | 46.92%     | ok               |
|          20 | -13.12%  | 68.89%             | -29.96% |    -0.15 |       79 | 56.57%     | ok               |
|          45 | -7.83%   | 68.89%             | -24.02% |    -0.15 |       68 | 39.93%     | ok               |
|          30 | -14.92%  | 68.89%             | -29.91% |    -0.22 |       86 | 50.25%     | ok               |

## WIF-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 60.65%   | -78.71%            | -46.21% |     0.66 |       71 | 41.38%     | ok               |
|          20 | 54.98%   | -78.71%            | -40.67% |     0.64 |       65 | 38.70%     | ok               |
|          25 | 2.09%    | -78.71%            | -45.19% |     0.31 |       67 | 36.02%     | ok               |
|          50 | -12.13%  | -78.71%            | -33.04% |    -0.02 |       38 | 11.69%     | ok               |
|          30 | -35.28%  | -78.71%            | -50.54% |    -0.13 |       68 | 31.99%     | ok               |

## WMT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 53.02%   | 102.12%            | -9.18%  |     1.41 |       38 | 42.43%     | ok               |
|          50 | 45.57%   | 102.12%            | -12.19% |     1.31 |       34 | 40.10%     | ok               |
|          40 | 43.45%   | 102.12%            | -10.52% |     1.18 |       42 | 43.59%     | ok               |
|          35 | 39.71%   | 102.12%            | -12.86% |     1.07 |       54 | 47.92%     | ok               |
|          30 | 16.25%   | 102.12%            | -21.31% |     0.49 |       61 | 50.58%     | ok               |

## XBI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 9.60%    | 66.76%             | -16.56% |     0.31 |       60 | 36.11%     | ok               |
|          45 | 8.76%    | 66.76%             | -16.74% |     0.3  |       52 | 32.95%     | ok               |
|          35 | 5.34%    | 66.76%             | -18.84% |     0.21 |       62 | 39.43%     | ok               |
|          30 | 4.17%    | 66.76%             | -19.80% |     0.19 |       62 | 41.10%     | ok               |
|          25 | -0.52%   | 66.76%             | -23.66% |     0.08 |       72 | 43.26%     | ok               |

## XLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -1.68%   | 18.77%             | -20.68% |    -0.01 |       54 | 31.61%     | ok               |
|          50 | -1.74%   | 18.77%             | -17.59% |    -0.02 |       42 | 27.29%     | ok               |
|          35 | -4.92%   | 18.77%             | -23.62% |    -0.13 |       56 | 34.94%     | ok               |
|          45 | -4.65%   | 18.77%             | -20.79% |    -0.14 |       42 | 28.79%     | ok               |
|          25 | -8.37%   | 18.77%             | -23.87% |    -0.25 |       62 | 40.43%     | ok               |

## XLC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 12.19%   | 41.34%             | -12.33% |     0.45 |       67 | 54.58%     | ok               |
|          25 | 8.96%    | 41.34%             | -12.31% |     0.35 |       66 | 56.57%     | ok               |
|          40 | 7.76%    | 41.34%             | -13.38% |     0.33 |       68 | 46.92%     | ok               |
|          35 | 7.74%    | 41.34%             | -13.38% |     0.33 |       64 | 51.41%     | ok               |
|          20 | 1.49%    | 41.34%             | -13.78% |     0.11 |       72 | 59.40%     | ok               |

## XLE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 6.25%    | 32.62%             | -25.98% |     0.25 |       54 | 36.11%     | ok               |
|          45 | 1.89%    | 32.62%             | -29.68% |     0.13 |       60 | 38.10%     | ok               |
|          35 | -0.25%   | 32.62%             | -31.51% |     0.08 |       65 | 42.76%     | ok               |
|          25 | -6.86%   | 32.62%             | -36.05% |    -0.08 |       83 | 48.25%     | ok               |
|          40 | -6.75%   | 32.62%             | -34.51% |    -0.12 |       64 | 40.60%     | ok               |

## XLF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -3.76%   | 41.48%             | -18.01% |    -0.06 |       70 | 53.74%     | ok               |
|          15 | -7.75%   | 41.48%             | -19.58% |    -0.2  |       78 | 56.57%     | ok               |
|          25 | -10.22%  | 41.48%             | -23.22% |    -0.31 |       77 | 50.42%     | ok               |
|          30 | -10.86%  | 41.48%             | -23.61% |    -0.35 |       76 | 47.92%     | ok               |
|          35 | -18.02%  | 41.48%             | -27.41% |    -0.71 |       66 | 43.76%     | ok               |

## XLI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 5.33%    | 52.82%             | -10.36% |     0.24 |       74 | 51.91%     | ok               |
|          20 | 1.33%    | 52.82%             | -12.74% |     0.11 |       65 | 47.25%     | ok               |
|          50 | -0.33%   | 52.82%             | -11.03% |     0.03 |       62 | 33.94%     | ok               |
|          30 | -0.89%   | 52.82%             | -11.76% |     0.02 |       66 | 44.76%     | ok               |
|          45 | -1.56%   | 52.82%             | -13.99% |    -0.02 |       64 | 36.44%     | ok               |

## XLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 84.07%   | 78.98%             | -14.75% |     1.35 |       41 | 51.25%     | ok               |
|          20 | 69.67%   | 78.98%             | -14.75% |     1.21 |       48 | 49.08%     | ok               |
|          25 | 66.21%   | 78.98%             | -14.75% |     1.21 |       42 | 46.92%     | ok               |
|          30 | 64.04%   | 78.98%             | -14.75% |     1.2  |       42 | 45.76%     | ok               |
|          35 | 45.74%   | 78.98%             | -13.61% |     0.96 |       54 | 43.09%     | ok               |

## XLM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 26.14%   | -46.34%            | -38.97% |     0.48 |       44 | 27.39%     | ok               |
|          45 | 22.34%   | -46.34%            | -43.99% |     0.44 |       50 | 31.03%     | ok               |
|          30 | 5.21%    | -46.34%            | -50.36% |     0.28 |       69 | 45.79%     | ok               |
|          40 | 1.75%    | -46.34%            | -43.80% |     0.23 |       49 | 35.44%     | ok               |
|          35 | -4.00%   | -46.34%            | -50.42% |     0.17 |       69 | 41.76%     | ok               |

## XLP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 11.43%   | 15.43%             | -5.66%  |     0.71 |       54 | 33.44%     | ok               |
|          50 | 9.99%    | 15.43%             | -6.08%  |     0.63 |       56 | 31.28%     | ok               |
|          40 | 9.19%    | 15.43%             | -7.77%  |     0.56 |       70 | 37.60%     | ok               |
|          35 | 8.24%    | 15.43%             | -9.73%  |     0.5  |       66 | 40.60%     | ok               |
|          30 | 6.32%    | 15.43%             | -11.16% |     0.39 |       68 | 42.10%     | ok               |

## XLU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 7.05%    | 49.34%             | -12.55% |     0.38 |       52 | 30.95%     | ok               |
|          45 | 5.63%    | 49.34%             | -14.27% |     0.31 |       54 | 31.95%     | ok               |
|          40 | 2.72%    | 49.34%             | -15.59% |     0.17 |       58 | 33.44%     | ok               |
|          35 | -3.26%   | 49.34%             | -19.71% |    -0.11 |       62 | 35.61%     | ok               |
|          30 | -4.17%   | 49.34%             | -20.40% |    -0.14 |       67 | 38.77%     | ok               |

## XLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -14.04%  | 10.84%             | -18.68% |    -0.7  |       68 | 36.11%     | ok               |
|          25 | -15.31%  | 10.84%             | -19.87% |    -0.76 |       70 | 37.44%     | ok               |
|          15 | -19.15%  | 10.84%             | -23.21% |    -0.94 |       81 | 42.26%     | ok               |
|          20 | -19.08%  | 10.84%             | -23.30% |    -0.96 |       75 | 39.10%     | ok               |
|          50 | -16.33%  | 10.84%             | -20.05% |    -0.99 |       56 | 24.79%     | ok               |

## XLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 4.62%    | 29.64%             | -12.94% |     0.21 |       72 | 41.26%     | ok               |
|          30 | 2.75%    | 29.64%             | -14.01% |     0.15 |       72 | 44.26%     | ok               |
|          15 | 1.20%    | 29.64%             | -15.77% |     0.11 |       74 | 51.25%     | ok               |
|          50 | 1.30%    | 29.64%             | -11.79% |     0.1  |       50 | 29.62%     | ok               |
|          40 | -1.91%   | 29.64%             | -16.99% |    -0.01 |       68 | 37.10%     | ok               |

## XOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 3.46%    | 39.31%             | -19.90% |     0.17 |       59 | 37.60%     | ok               |
|          30 | 2.87%    | 39.31%             | -20.29% |     0.15 |       59 | 36.27%     | ok               |
|          50 | 2.64%    | 39.31%             | -21.35% |     0.15 |       36 | 28.62%     | ok               |
|          20 | -2.50%   | 39.31%             | -25.56% |     0.01 |       66 | 40.10%     | ok               |
|          35 | -2.98%   | 39.31%             | -20.93% |    -0.01 |       55 | 34.94%     | ok               |

## XRP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -25.11%  | -56.17%            | -46.87% |    -0.14 |       68 | 39.85%     | ok               |
|          40 | -30.47%  | -56.17%            | -44.89% |    -0.26 |       58 | 33.72%     | ok               |
|          30 | -37.23%  | -56.17%            | -54.70% |    -0.33 |       70 | 44.06%     | ok               |
|          45 | -38.24%  | -56.17%            | -46.06% |    -0.42 |       58 | 29.50%     | ok               |
|          50 | -34.88%  | -56.17%            | -38.03% |    -0.46 |       60 | 22.03%     | ok               |

## YFI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -52.02%  | -63.09%            | -53.91% |    -0.89 |       62 | 27.39%     | ok               |
|          45 | -48.45%  | -63.09%            | -54.59% |    -0.99 |       68 | 21.84%     | ok               |
|          30 | -65.02%  | -63.09%            | -70.70% |    -1.06 |       81 | 40.80%     | ok               |
|          35 | -63.79%  | -63.09%            | -65.22% |    -1.1  |       71 | 34.87%     | ok               |
|          25 | -68.58%  | -63.09%            | -71.76% |    -1.14 |       75 | 45.79%     | ok               |

## ZEC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 95.64%   | 1459.06%           | -24.66% |     0.8  |       46 | 22.99%     | ok               |
|          35 | 67.97%   | 1459.06%           | -44.34% |     0.67 |       54 | 29.50%     | ok               |
|          25 | 49.54%   | 1459.06%           | -48.59% |     0.59 |       60 | 38.70%     | ok               |
|          30 | 34.74%   | 1459.06%           | -47.68% |     0.51 |       64 | 35.25%     | ok               |
|          40 | 33.32%   | 1459.06%           | -48.16% |     0.49 |       56 | 26.82%     | ok               |
