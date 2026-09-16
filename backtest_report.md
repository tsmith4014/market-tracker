# Market Tracker Backtest Report

_Generated: 2026-09-16T04:56:43+00:00_

## Data Sources

- Crypto: Kraken -> Coinbase -> CoinGecko OHLC -> CoinPaprika fallback chain.
- Stocks / ETFs / indices: Stooq -> Yahoo Finance fallback chain.
- Data rows are generated from real market APIs. Mock OHLCV rows are not generated.

## Data Freshness

- Rows: **92,684**
- Symbols: **161**
- Date range: **2024-04-23** to **2026-09-16**

## Latest Signals

| symbol     | date                |         close |   composite_score | signal   | data_source   |
|:-----------|:--------------------|--------------:|------------------:|:---------|:--------------|
| AAPL       | 2026-09-15 00:00:00 |   331.34      |         70.4167   | LONG     | Yahoo Finance |
| ABBV       | 2026-09-15 00:00:00 |   263.04      |         32.5833   | LONG     | Yahoo Finance |
| COP        | 2026-09-15 00:00:00 |   141.22      |         66.25     | LONG     | Yahoo Finance |
| CRM        | 2026-09-15 00:00:00 |   255.65      |         56.25     | LONG     | Yahoo Finance |
| CVX        | 2026-09-15 00:00:00 |   217.77      |         71.25     | LONG     | Yahoo Finance |
| DBC        | 2026-09-15 00:00:00 |    33.68      |         77.75     | LONG     | Yahoo Finance |
| DE         | 2026-09-15 00:00:00 |   684.04      |         75.25     | LONG     | Yahoo Finance |
| DXY-INDEX  | 2026-09-16 00:00:00 |    99.62      |         56.7204   | LONG     | Yahoo Finance |
| FIL-USD    | 2026-09-16 00:00:00 |     0.82      |         35.8333   | LONG     | Kraken API    |
| IBIT       | 2026-09-15 00:00:00 |    43.11      |         41.4167   | LONG     | Yahoo Finance |
| INJ-USD    | 2026-09-16 00:00:00 |     5.421     |         38.5833   | LONG     | Kraken API    |
| INTC       | 2026-09-15 00:00:00 |    97.14      |         65.1667   | LONG     | Yahoo Finance |
| META       | 2026-09-15 00:00:00 |   670.24      |         50.75     | LONG     | Yahoo Finance |
| MPC        | 2026-09-15 00:00:00 |   410.84      |         71.25     | LONG     | Yahoo Finance |
| MSFT       | 2026-09-15 00:00:00 |   497.12      |         53.25     | LONG     | Yahoo Finance |
| NEAR-USD   | 2026-09-16 00:00:00 |     2.3524    |         68.9167   | LONG     | Kraken API    |
| NOW        | 2026-09-15 00:00:00 |   141.9       |         53.75     | LONG     | Yahoo Finance |
| QCOM       | 2026-09-15 00:00:00 |   187.8       |         79.5      | LONG     | Yahoo Finance |
| SOL-USD    | 2026-09-16 00:00:00 |    97.32      |         23.8333   | LONG     | Kraken API    |
| T          | 2026-09-15 00:00:00 |    26.72      |         38.25     | LONG     | Yahoo Finance |
| TMO        | 2026-09-15 00:00:00 |   641.39      |         59.75     | LONG     | Yahoo Finance |
| TXN        | 2026-09-15 00:00:00 |   263.43      |         35.1667   | LONG     | Yahoo Finance |
| UNI-USD    | 2026-09-16 00:00:00 |     6.4336    |         42.3333   | LONG     | Kraken API    |
| USO        | 2026-09-15 00:00:00 |   161.86      |         73.75     | LONG     | Yahoo Finance |
| VZ         | 2026-09-15 00:00:00 |    51.45      |         57.75     | LONG     | Yahoo Finance |
| XLE        | 2026-09-15 00:00:00 |    65.93      |         54.9167   | LONG     | Yahoo Finance |
| ZEC-USD    | 2026-09-16 00:00:00 |  1147         |         44.3333   | LONG     | Kraken API    |
| AAVE-USD   | 2026-09-16 00:00:00 |   121.14      |         12.6667   | NEUTRAL  | Kraken API    |
| ADA-USD    | 2026-09-16 00:00:00 |     0.195855  |        -30.6667   | NEUTRAL  | Kraken API    |
| ADBE       | 2026-09-15 00:00:00 |   257.76      |        -22.3333   | NEUTRAL  | Yahoo Finance |
| ALGO-USD   | 2026-09-16 00:00:00 |     0.08938   |        -43.5833   | NEUTRAL  | Kraken API    |
| AMD        | 2026-09-15 00:00:00 |   504.2       |         61.6667   | NEUTRAL  | Yahoo Finance |
| AMGN       | 2026-09-15 00:00:00 |   375.65      |         -8.33333  | NEUTRAL  | Yahoo Finance |
| AMZN       | 2026-09-15 00:00:00 |   248.42      |        -11.25     | NEUTRAL  | Yahoo Finance |
| APT-USD    | 2026-09-16 00:00:00 |     0.5478    |        -28.5      | NEUTRAL  | Kraken API    |
| ARB-USD    | 2026-09-16 00:00:00 |     0.1586    |         44.3333   | NEUTRAL  | Kraken API    |
| ARKK       | 2026-09-15 00:00:00 |    83.49      |         16.4167   | NEUTRAL  | Yahoo Finance |
| ATOM-USD   | 2026-09-16 00:00:00 |     1.5073    |         -6.16667  | NEUTRAL  | Kraken API    |
| AVAX-USD   | 2026-09-16 00:00:00 |     7.322     |         -7.75     | NEUTRAL  | Kraken API    |
| BA         | 2026-09-15 00:00:00 |   209.69      |        -27.5      | NEUTRAL  | Yahoo Finance |
| BAC        | 2026-09-15 00:00:00 |    59.52      |        -30.25     | NEUTRAL  | Yahoo Finance |
| BCH-USD    | 2026-09-16 00:00:00 |   219.86      |        -64.5833   | NEUTRAL  | Kraken API    |
| BITO       | 2026-09-15 00:00:00 |    10.23      |         10.6667   | NEUTRAL  | Yahoo Finance |
| BONK-USD   | 2026-09-16 00:00:00 |     2.564e-06 |        -56.25     | NEUTRAL  | Kraken API    |
| BTC-USD    | 2026-09-16 00:00:00 | 75859.7       |         23.8333   | NEUTRAL  | Kraken API    |
| C          | 2026-09-15 00:00:00 |   136.17      |         52.1667   | NEUTRAL  | Yahoo Finance |
| CAT        | 2026-09-15 00:00:00 |   783.54      |        -15.4167   | NEUTRAL  | Yahoo Finance |
| CL         | 2026-09-15 00:00:00 |    87         |        -53.5833   | NEUTRAL  | Yahoo Finance |
| COMP-USD   | 2026-09-16 00:00:00 |    18.84      |         -4.83333  | NEUTRAL  | Kraken API    |
| COST       | 2026-09-15 00:00:00 |   901.35      |        -66.3333   | NEUTRAL  | Yahoo Finance |
| CRV-USD    | 2026-09-16 00:00:00 |     0.31481   |         -0.833333 | NEUTRAL  | Kraken API    |
| CSCO       | 2026-09-15 00:00:00 |   110.07      |         14.0833   | NEUTRAL  | Yahoo Finance |
| DASH-USD   | 2026-09-16 00:00:00 |    50.762     |         24.5833   | NEUTRAL  | Kraken API    |
| DIA        | 2026-09-15 00:00:00 |   521.23      |        -25        | NEUTRAL  | Yahoo Finance |
| DIS        | 2026-09-15 00:00:00 |   106.42      |         22.6667   | NEUTRAL  | Yahoo Finance |
| DOGE-USD   | 2026-09-16 00:00:00 |     0.0804316 |        -30.6667   | NEUTRAL  | Kraken API    |
| DOT-USD    | 2026-09-16 00:00:00 |     0.9555    |          8.25     | NEUTRAL  | Kraken API    |
| EEM        | 2026-09-15 00:00:00 |    65.76      |        -10.8333   | NEUTRAL  | Yahoo Finance |
| EFA        | 2026-09-15 00:00:00 |   105.4       |        -33.5      | NEUTRAL  | Yahoo Finance |
| EOG        | 2026-09-15 00:00:00 |   153.74      |         60        | NEUTRAL  | Yahoo Finance |
| ETC-USD    | 2026-09-16 00:00:00 |     7.258     |        -19.4167   | NEUTRAL  | Kraken API    |
| ETH-USD    | 2026-09-16 00:00:00 |  2403.83      |         27        | NEUTRAL  | Kraken API    |
| EWJ        | 2026-09-15 00:00:00 |    96.92      |         65.1667   | NEUTRAL  | Yahoo Finance |
| FCX        | 2026-09-15 00:00:00 |    69.38      |        -20.9167   | NEUTRAL  | Yahoo Finance |
| FET-USD    | 2026-09-16 00:00:00 |     0.1564    |         -9.75     | NEUTRAL  | Kraken API    |
| FXI        | 2026-09-15 00:00:00 |    34.4       |        -63        | NEUTRAL  | Yahoo Finance |
| GDX        | 2026-09-15 00:00:00 |    94.13      |          0.416667 | NEUTRAL  | Yahoo Finance |
| GDXJ       | 2026-09-15 00:00:00 |   120.31      |         -1.58333  | NEUTRAL  | Yahoo Finance |
| GLD        | 2026-09-15 00:00:00 |   394.15      |        -63.8333   | NEUTRAL  | Yahoo Finance |
| GOOGL      | 2026-09-15 00:00:00 |   344.98      |         15.25     | NEUTRAL  | Yahoo Finance |
| GRT-USD    | 2026-09-16 00:00:00 |     0.01724   |          3.25     | NEUTRAL  | Kraken API    |
| GS         | 2026-09-15 00:00:00 |   976.67      |        -46.0833   | NEUTRAL  | Yahoo Finance |
| HBAR-USD   | 2026-09-16 00:00:00 |     0.07462   |          3.5      | NEUTRAL  | Kraken API    |
| IBM        | 2026-09-15 00:00:00 |   248.37      |         26.8333   | NEUTRAL  | Yahoo Finance |
| ICP-USD    | 2026-09-16 00:00:00 |     2.516     |         -2.16667  | NEUTRAL  | Kraken API    |
| IEMG       | 2026-09-15 00:00:00 |    80.1       |        -12.5833   | NEUTRAL  | Yahoo Finance |
| INTU       | 2026-09-15 00:00:00 |   329.27      |        -63.3333   | NEUTRAL  | Yahoo Finance |
| IWM        | 2026-09-15 00:00:00 |   285.14      |        -19.0833   | NEUTRAL  | Yahoo Finance |
| JNJ        | 2026-09-15 00:00:00 |   267.2       |        -21.8333   | NEUTRAL  | Yahoo Finance |
| JPM        | 2026-09-15 00:00:00 |   352.49      |          2.08333  | NEUTRAL  | Yahoo Finance |
| KO         | 2026-09-15 00:00:00 |    88.71      |         25.1667   | NEUTRAL  | Yahoo Finance |
| LDO-USD    | 2026-09-16 00:00:00 |     0.338     |        -21.0833   | NEUTRAL  | Kraken API    |
| LIN        | 2026-09-15 00:00:00 |   462.96      |        -56.8333   | NEUTRAL  | Yahoo Finance |
| LINK-USD   | 2026-09-16 00:00:00 |    10.8341    |         23.9167   | NEUTRAL  | Kraken API    |
| LRCX       | 2026-09-15 00:00:00 |   270.87      |        -29        | NEUTRAL  | Yahoo Finance |
| LTC-USD    | 2026-09-16 00:00:00 |    51.21      |          7.25     | NEUTRAL  | Kraken API    |
| MRK        | 2026-09-15 00:00:00 |   143.79      |         13.0833   | NEUTRAL  | Yahoo Finance |
| MS         | 2026-09-15 00:00:00 |   206.28      |        -19        | NEUTRAL  | Yahoo Finance |
| MU         | 2026-09-15 00:00:00 |   927.6       |         -3.33333  | NEUTRAL  | Yahoo Finance |
| NEM        | 2026-09-15 00:00:00 |   124.19      |         18.9167   | NEUTRAL  | Yahoo Finance |
| NFLX       | 2026-09-15 00:00:00 |    77.9       |        -40.3333   | NEUTRAL  | Yahoo Finance |
| NVDA       | 2026-09-15 00:00:00 |   212.17      |          1.66667  | NEUTRAL  | Yahoo Finance |
| OP-USD     | 2026-09-16 00:00:00 |     0.0941    |        -40.4167   | NEUTRAL  | Kraken API    |
| ORCL       | 2026-09-15 00:00:00 |   140.35      |        -24.1667   | NEUTRAL  | Yahoo Finance |
| OXY        | 2026-09-15 00:00:00 |    63.52      |         60        | NEUTRAL  | Yahoo Finance |
| PEP        | 2026-09-15 00:00:00 |   135.5       |        -65.8333   | NEUTRAL  | Yahoo Finance |
| PEPE-USD   | 2026-09-16 00:00:00 |     3.407e-06 |        -10.6667   | NEUTRAL  | Kraken API    |
| PFE        | 2026-09-15 00:00:00 |    27.55      |          0.416667 | NEUTRAL  | Yahoo Finance |
| PG         | 2026-09-15 00:00:00 |   146.67      |         24        | NEUTRAL  | Yahoo Finance |
| PM         | 2026-09-15 00:00:00 |   194.11      |         46.8333   | NEUTRAL  | Yahoo Finance |
| POL-USD    | 2026-09-16 00:00:00 |     0.09194   |         -8.91667  | NEUTRAL  | Kraken API    |
| QQQ        | 2026-09-15 00:00:00 |   704.54      |        -10.5      | NEUTRAL  | Yahoo Finance |
| RENDER-USD | 2026-09-16 00:00:00 |     1.312     |        -50.25     | NEUTRAL  | Kraken API    |
| RTX        | 2026-09-15 00:00:00 |   195.5       |        -29.1667   | NEUTRAL  | Yahoo Finance |
| SCHW       | 2026-09-15 00:00:00 |   107.79      |         -1.83333  | NEUTRAL  | Yahoo Finance |
| SHIB-USD   | 2026-09-16 00:00:00 |     4.931e-06 |        -38.1667   | NEUTRAL  | Kraken API    |
| SLB        | 2026-09-15 00:00:00 |    54.2       |         14.5833   | NEUTRAL  | Yahoo Finance |
| SLV        | 2026-09-15 00:00:00 |    57.53      |        -55.3333   | NEUTRAL  | Yahoo Finance |
| SMH        | 2026-09-15 00:00:00 |   542.11      |         -8.75     | NEUTRAL  | Yahoo Finance |
| SNX-USD    | 2026-09-16 00:00:00 |     0.1986    |        -48.5833   | NEUTRAL  | Kraken API    |
| SOXX       | 2026-09-15 00:00:00 |   498.85      |         -8.75     | NEUTRAL  | Yahoo Finance |
| SPY        | 2026-09-15 00:00:00 |   757.39      |        -16.6667   | NEUTRAL  | Yahoo Finance |
| SUSHI-USD  | 2026-09-16 00:00:00 |     0.2077    |         -0.75     | NEUTRAL  | Kraken API    |
| TGT        | 2026-09-15 00:00:00 |   154.4       |         15.9167   | NEUTRAL  | Yahoo Finance |
| TLT        | 2026-09-15 00:00:00 |    80.71      |        -63.8333   | NEUTRAL  | Yahoo Finance |
| TMUS       | 2026-09-15 00:00:00 |   180.47      |        -45.3333   | NEUTRAL  | Yahoo Finance |
| TRX-USD    | 2026-09-16 00:00:00 |     0.334163  |         20.75     | NEUTRAL  | Kraken API    |
| TSLA       | 2026-09-15 00:00:00 |   356.58      |        -19.0833   | NEUTRAL  | Yahoo Finance |
| UNH        | 2026-09-15 00:00:00 |   375.93      |        -16.25     | NEUTRAL  | Yahoo Finance |
| UPS        | 2026-09-15 00:00:00 |   102.35      |        -47.1667   | NEUTRAL  | Yahoo Finance |
| VEA        | 2026-09-15 00:00:00 |    71.53      |        -26.8333   | NEUTRAL  | Yahoo Finance |
| VIXY       | 2026-09-15 00:00:00 |    17.53      |        -17.5      | NEUTRAL  | Yahoo Finance |
| VTI        | 2026-09-15 00:00:00 |   372.84      |        -23.3333   | NEUTRAL  | Yahoo Finance |
| VWO        | 2026-09-15 00:00:00 |    59.22      |        -27.3333   | NEUTRAL  | Yahoo Finance |
| WFC        | 2026-09-15 00:00:00 |    89.72      |         43.1667   | NEUTRAL  | Yahoo Finance |
| WMT        | 2026-09-15 00:00:00 |   108.09      |         12.9167   | NEUTRAL  | Yahoo Finance |
| XBI        | 2026-09-15 00:00:00 |   154.03      |        -21.0833   | NEUTRAL  | Yahoo Finance |
| XLB        | 2026-09-15 00:00:00 |    50.73      |        -33.0833   | NEUTRAL  | Yahoo Finance |
| XLC        | 2026-09-15 00:00:00 |   114.03      |         54.5833   | NEUTRAL  | Yahoo Finance |
| XLF        | 2026-09-15 00:00:00 |    56.85      |         -6.5      | NEUTRAL  | Yahoo Finance |
| XLK        | 2026-09-15 00:00:00 |   183.74      |         37.3333   | NEUTRAL  | Yahoo Finance |
| XLM-USD    | 2026-09-16 00:00:00 |     0.177502  |        -27.75     | NEUTRAL  | Kraken API    |
| XLP        | 2026-09-15 00:00:00 |    83.73      |        -23.25     | NEUTRAL  | Yahoo Finance |
| XLU        | 2026-09-15 00:00:00 |    41.32      |        -70.8333   | NEUTRAL  | Yahoo Finance |
| XLV        | 2026-09-15 00:00:00 |   167.66      |          6.08333  | NEUTRAL  | Yahoo Finance |
| XOM        | 2026-09-15 00:00:00 |   169.32      |         42        | NEUTRAL  | Yahoo Finance |
| XRP-USD    | 2026-09-16 00:00:00 |     1.30851   |        -12.6667   | NEUTRAL  | Kraken API    |
| YFI-USD    | 2026-09-16 00:00:00 |  2033.9       |        -48.25     | NEUTRAL  | Kraken API    |
| AGG        | 2026-09-15 00:00:00 |    95.85      |        -57.0833   | SHORT    | Yahoo Finance |
| AMAT       | 2026-09-15 00:00:00 |   421.17      |        -45.9167   | SHORT    | Yahoo Finance |
| AVGO       | 2026-09-15 00:00:00 |   339.27      |        -48.75     | SHORT    | Yahoo Finance |
| BLK        | 2026-09-15 00:00:00 |  1058.66      |        -43.8333   | SHORT    | Yahoo Finance |
| BND        | 2026-09-15 00:00:00 |    71.15      |        -57.0833   | SHORT    | Yahoo Finance |
| CMCSA      | 2026-09-15 00:00:00 |    24.42      |        -57.0833   | SHORT    | Yahoo Finance |
| GE         | 2026-09-15 00:00:00 |   307.05      |        -63.3333   | SHORT    | Yahoo Finance |
| HD         | 2026-09-15 00:00:00 |   305.48      |        -59.5833   | SHORT    | Yahoo Finance |
| HON        | 2026-09-15 00:00:00 |   203.44      |        -44.0833   | SHORT    | Yahoo Finance |
| HYG        | 2026-09-15 00:00:00 |    78.38      |        -57.5833   | SHORT    | Yahoo Finance |
| IEF        | 2026-09-15 00:00:00 |    90.82      |        -57.0833   | SHORT    | Yahoo Finance |
| ITA        | 2026-09-15 00:00:00 |   214         |        -59.6667   | SHORT    | Yahoo Finance |
| LLY        | 2026-09-15 00:00:00 |  1136.11      |        -36.9167   | SHORT    | Yahoo Finance |
| MCD        | 2026-09-15 00:00:00 |   252.78      |        -57.9167   | SHORT    | Yahoo Finance |
| NKE        | 2026-09-15 00:00:00 |    36.22      |        -61.5833   | SHORT    | Yahoo Finance |
| SBUX       | 2026-09-15 00:00:00 |    96.58      |        -44.3333   | SHORT    | Yahoo Finance |
| SHY        | 2026-09-15 00:00:00 |    81.31      |        -57.0833   | SHORT    | Yahoo Finance |
| SKY-USD    | 2026-09-16 00:00:00 |     0.06082   |        -51.5833   | SHORT    | Kraken API    |
| TIA-USD    | 2026-09-16 00:00:00 |     0.3288    |        -35.8333   | SHORT    | Kraken API    |
| VNQ        | 2026-09-15 00:00:00 |    94.1       |        -41.8333   | SHORT    | Yahoo Finance |
| WIF-USD    | 2026-09-16 00:00:00 |     0.18      |        -30.5833   | SHORT    | Kraken API    |
| XLI        | 2026-09-15 00:00:00 |   168.85      |        -50.3333   | SHORT    | Yahoo Finance |
| XLY        | 2026-09-15 00:00:00 |   110.88      |        -61.3333   | SHORT    | Yahoo Finance |

## Edge Summary

- Symbols with trades: **160** of 160
- Beat buy-and-hold: **30.00%** of traded symbols
- Positive return: **29.38%** of traded symbols
- Median strategy return: **-10.36%** (benchmark **21.24%**)
- Median excess vs benchmark: **-27.08%**
- Median Sharpe: **-0.16**
- Median exposure: **44.34%**

> Edge is real only if both _beat buy-and-hold_ and _median excess_ are convincingly positive across many symbols. Treat a single high-return symbol as noise.

## Portfolio Backtest

Actual capital-allocation books (not per-symbol averages). Benchmarks: `equal_weight_buyhold` (whole tracked universe), `spy_buyhold` (100% SPY), and `sixty_forty` (60% SPY / 40% AGG). `high_conf_voltarget` inverse-vol-weights the HIGH-confidence book; `conviction_long_short` is market-neutral. Judge on **Sharpe** and **max_drawdown** out-of-sample, not raw return: a fully-invested long book wins on return in a bull market but carries all the risk.

| strategy              | scope         | ann_return   | ann_vol   |   sharpe | max_drawdown   | total_return   |   avg_gross_exposure |
|:----------------------|:--------------|:-------------|:----------|---------:|:---------------|:---------------|---------------------:|
| equal_weight_buyhold  | full          | 10.43%       | 28.24%    |     0.37 | -39.63%        | 21.68%         |                 1    |
| equal_weight_buyhold  | out_of_sample | 9.61%        | 27.89%    |     0.34 | -29.33%        | 6.33%          |                 1    |
| all_signals_ew        | full          | -20.64%      | 23.79%    |    -0.87 | -62.93%        | -51.09%        |                 1    |
| all_signals_ew        | out_of_sample | 7.54%        | 23.12%    |     0.33 | -22.53%        | 5.37%          |                 1    |
| high_conf_ew          | full          | -1.79%       | 30.52%    |    -0.06 | -43.23%        | -17.66%        |                 0.89 |
| high_conf_ew          | out_of_sample | 25.24%       | 26.50%    |     0.95 | -22.85%        | 26.05%         |                 0.89 |
| high_conf_voltarget   | full          | -1.12%       | 27.42%    |    -0.04 | -36.51%        | -13.61%        |                 0.89 |
| high_conf_voltarget   | out_of_sample | 15.60%       | 22.52%    |     0.69 | -16.94%        | 14.90%         |                 0.89 |
| conviction_long_short | full          | -18.23%      | 22.36%    |    -0.82 | -49.88%        | -46.87%        |                 0.97 |
| conviction_long_short | out_of_sample | -14.12%      | 20.25%    |    -0.7  | -26.12%        | -15.86%        |                 0.97 |
| spy_buyhold           | full          | 6.39%        | 13.47%    |     0.47 | -19.00%        | 18.19%         |                 0.78 |
| spy_buyhold           | out_of_sample | 1.46%        | 9.84%     |     0.15 | -12.06%        | 1.05%          |                 0.78 |
| sixty_forty           | full          | 3.68%        | 8.51%     |     0.43 | -11.66%        | 10.62%         |                 0.78 |
| sixty_forty           | out_of_sample | -1.00%       | 6.58%     |    -0.15 | -8.26%         | -1.29%         |                 0.78 |

## Walk-Forward Robustness

Each book measured across contiguous time folds (each a different regime). A book has durable edge only if `mean_sharpe` is positive, `min_sharpe` isn't deeply negative, and `pct_positive_folds` is high — a single great fold doesn't count. `fold_sharpes` lists each fold oldest-to-newest.

| strategy              |   n_folds |   mean_sharpe |   median_sharpe |   min_sharpe | pct_positive_folds   | mean_return   | fold_sharpes                  |
|:----------------------|----------:|--------------:|----------------:|-------------:|:---------------------|:--------------|:------------------------------|
| equal_weight_buyhold  |         5 |          0.63 |            0.66 |        -1.06 | 80.00%               | 5.02%         | 1.86;0.66;0.66;-1.06;1.03     |
| all_signals_ew        |         5 |         -0.91 |           -0.86 |        -2.35 | 20.00%               | -10.41%       | -0.86;-2.35;-2.35;1.60;-0.60  |
| high_conf_ew          |         5 |         -0.08 |           -0.15 |        -1.93 | 40.00%               | -2.43%        | -0.22;-1.93;-0.15;1.07;0.85   |
| high_conf_voltarget   |         5 |         -0.04 |            0.31 |        -2.07 | 60.00%               | -2.20%        | 0.31;-2.07;-0.05;0.55;1.04    |
| conviction_long_short |         5 |         -0.87 |           -0.84 |        -1.98 | 0.00%                | -11.63%       | -1.98;-0.94;-0.84;-0.06;-0.54 |
| spy_buyhold           |         5 |          0.58 |            0.36 |        -0.19 | 60.00%               | 3.70%         | 2.31;-0.19;0.36;-0.16;0.58    |
| sixty_forty           |         5 |          0.51 |            0.21 |        -0.34 | 60.00%               | 2.18%         | 2.47;-0.23;0.47;-0.34;0.21    |

## Strategy Comparison

Each decision rule backtested over the same data. `out_of_sample` is the most recent ~35% of each symbol's history (unseen tail). A rule has real edge only if `median_excess` and `beat_benchmark_pct` stay positive out-of-sample, not just full-sample.

| strategy        | scope         |   symbols | beat_benchmark_pct   | positive_pct   | median_return   | median_benchmark   | median_excess   |   median_sharpe |   total_trades |
|:----------------|:--------------|----------:|:---------------------|:---------------|:----------------|:-------------------|:----------------|----------------:|---------------:|
| trend           | full          |       160 | 30.00%               | 29.38%         | -10.36%         | 21.24%             | -27.08%         |           -0.16 |          11338 |
| trend           | out_of_sample |       160 | 30.63%               | 45.62%         | -1.42%          | 7.15%              | -8.63%          |           -0.03 |           3741 |
| mean_reversion  | full          |       156 | 35.90%               | 48.08%         | -0.22%          | 17.83%             | -19.17%         |           -0.01 |           1272 |
| mean_reversion  | out_of_sample |       119 | 36.13%               | 56.30%         | 0.39%           | 4.37%              | -7.19%          |            0.22 |            490 |
| regime_adaptive | full          |       160 | 29.38%               | 30.00%         | -11.20%         | 21.24%             | -27.00%         |           -0.15 |          11599 |
| regime_adaptive | out_of_sample |       160 | 30.63%               | 45.62%         | -1.97%          | 7.15%              | -8.14%          |           -0.01 |           3869 |

## Signal Calibration

Realized forward return in the signal's direction, grouped by confidence. HIGH should outrank LOW for the confidence score to be meaningful.

| confidence_level   |   horizon |     n | mean_return   | median_return   | win_rate   |
|:-------------------|----------:|------:|:--------------|:----------------|:-----------|
| HIGH               |         5 |  7915 | 0.12%         | 0.07%           | 51.14%     |
| MEDIUM             |         5 | 28912 | -0.04%        | 0.01%           | 50.06%     |
| LOW                |         5 |  3595 | -0.50%        | -0.51%          | 45.34%     |
| ALL                |         5 | 40422 | -0.05%        | 0.00%           | 49.85%     |
| HIGH               |        10 |  7859 | 0.39%         | 0.10%           | 51.14%     |
| MEDIUM             |        10 | 28665 | 0.07%         | 0.04%           | 50.34%     |
| LOW                |        10 |  3547 | -0.82%        | -0.62%          | 46.04%     |
| ALL                |        10 | 40071 | 0.05%         | 0.01%           | 50.12%     |
| HIGH               |        20 |  7707 | 0.89%         | 0.34%           | 52.90%     |
| MEDIUM             |        20 | 28142 | 0.68%         | 0.51%           | 52.88%     |
| LOW                |        20 |  3433 | -0.90%        | -0.60%          | 47.04%     |
| ALL                |        20 | 39282 | 0.58%         | 0.41%           | 52.38%     |

## Backtest Summary

### Data Quality / Signal Availability

- **ok**: 160 symbols

| symbol     |   trades | return   | benchmark_return   | mdd     |   sharpe | exposure   | skipped_reason   |
|:-----------|---------:|:---------|:-------------------|:--------|---------:|:-----------|:-----------------|
| AAPL       |       62 | 8.57%    | 98.53%             | -23.09% |     0.27 | 49.58%     | ok               |
| AAVE-USD   |       73 | -35.31%  | -12.89%            | -66.17% |    -0.2  | 41.95%     | ok               |
| ABBV       |       72 | -26.75%  | 55.15%             | -31.23% |    -0.61 | 47.75%     | ok               |
| ADA-USD    |       79 | -36.78%  | -69.26%            | -45.96% |    -0.28 | 46.93%     | ok               |
| ADBE       |       69 | -14.39%  | -45.49%            | -31.20% |    -0.08 | 55.91%     | ok               |
| AGG        |       69 | -7.70%   | 0.22%              | -10.95% |    -1.26 | 32.61%     | ok               |
| ALGO-USD   |       80 | -34.91%  | -51.12%            | -43.00% |    -0.29 | 39.27%     | ok               |
| AMAT       |       65 | -31.93%  | 117.95%            | -57.08% |    -0.28 | 49.25%     | ok               |
| AMD        |       52 | 11.68%   | 231.12%            | -41.09% |     0.32 | 34.44%     | ok               |
| AMGN       |       69 | -8.10%   | 37.33%             | -34.19% |    -0.07 | 50.75%     | ok               |
| AMZN       |       84 | -56.13%  | 38.36%             | -57.22% |    -1.6  | 41.60%     | ok               |
| APT-USD    |       78 | -39.42%  | -88.64%            | -65.32% |    -0.23 | 40.61%     | ok               |
| ARB-USD    |       77 | -12.85%  | -47.24%            | -58.79% |     0.16 | 42.72%     | ok               |
| ARKK       |       89 | -30.79%  | 90.31%             | -33.41% |    -0.47 | 44.26%     | ok               |
| ATOM-USD   |       88 | -60.00%  | -63.67%            | -61.22% |    -0.89 | 46.74%     | ok               |
| AVAX-USD   |       72 | -37.60%  | -62.57%            | -45.19% |    -0.38 | 38.12%     | ok               |
| AVGO       |       64 | 26.59%   | 171.59%            | -36.08% |     0.45 | 41.43%     | ok               |
| BA         |       69 | -0.98%   | 23.94%             | -27.11% |     0.11 | 49.58%     | ok               |
| BAC        |       78 | -15.01%  | 55.12%             | -27.55% |    -0.35 | 48.59%     | ok               |
| BCH-USD    |       78 | 23.02%   | -35.90%            | -53.87% |     0.44 | 49.04%     | ok               |
| BITO       |       76 | -14.59%  | -64.74%            | -39.47% |    -0.03 | 39.93%     | ok               |
| BLK        |       81 | -7.64%   | 38.09%             | -26.90% |    -0.14 | 48.09%     | ok               |
| BND        |       71 | -8.03%   | 0.28%              | -10.70% |    -1.27 | 34.61%     | ok               |
| BONK-USD   |       74 | 8.63%    | -79.61%            | -48.17% |     0.36 | 44.44%     | ok               |
| BTC-USD    |       66 | 21.05%   | -9.39%             | -23.38% |     0.47 | 52.11%     | ok               |
| C          |       77 | -33.68%  | 117.28%            | -39.51% |    -0.71 | 47.92%     | ok               |
| CAT        |       70 | 10.17%   | 115.70%            | -18.88% |     0.29 | 49.58%     | ok               |
| CL         |       60 | 5.11%    | -1.78%             | -14.32% |     0.23 | 41.10%     | ok               |
| CMCSA      |       82 | -43.76%  | -35.44%            | -49.38% |    -1.14 | 42.26%     | ok               |
| COMP-USD   |       97 | -46.68%  | -53.56%            | -56.58% |    -0.37 | 47.89%     | ok               |
| COP        |       70 | -14.68%  | 8.76%              | -43.40% |    -0.19 | 43.93%     | ok               |
| COST       |       60 | 2.04%    | 24.72%             | -29.73% |     0.13 | 41.93%     | ok               |
| CRM        |       67 | -26.81%  | -7.60%             | -45.51% |    -0.34 | 46.09%     | ok               |
| CRV-USD    |       68 | 37.75%   | -47.27%            | -39.89% |     0.55 | 41.57%     | ok               |
| CSCO       |       60 | 15.86%   | 127.79%            | -21.79% |     0.39 | 47.75%     | ok               |
| CVX        |       73 | -7.76%   | 33.72%             | -29.13% |    -0.13 | 41.26%     | ok               |
| DASH-USD   |       57 | -3.96%   | 146.57%            | -64.43% |     0.35 | 29.69%     | ok               |
| DBC        |       64 | -2.94%   | 43.08%             | -25.02% |    -0.03 | 34.44%     | ok               |
| DE         |       74 | -10.06%  | 72.21%             | -22.93% |    -0.13 | 44.26%     | ok               |
| DIA        |       66 | -5.37%   | 35.38%             | -12.94% |    -0.26 | 44.76%     | ok               |
| DIS        |       64 | -14.03%  | -6.41%             | -28.17% |    -0.22 | 43.59%     | ok               |
| DOGE-USD   |       71 | -27.56%  | -50.49%            | -60.95% |    -0.06 | 49.04%     | ok               |
| DOT-USD    |       92 | -64.28%  | -73.92%            | -66.16% |    -0.73 | 48.08%     | ok               |
| DXY-INDEX  |       40 | -4.11%   | -6.44%             | -6.28%  |    -0.66 | 29.44%     | ok               |
| EEM        |       64 | -10.43%  | 62.49%             | -25.67% |    -0.28 | 41.76%     | ok               |
| EFA        |       58 | -10.29%  | 35.39%             | -12.96% |    -0.4  | 41.26%     | ok               |
| EOG        |       83 | -32.39%  | 14.05%             | -47.57% |    -0.72 | 45.59%     | ok               |
| ETC-USD    |       60 | -28.64%  | -52.24%            | -45.54% |    -0.36 | 28.16%     | ok               |
| ETH-USD    |       58 | 154.67%  | 50.55%             | -30.11% |     1.34 | 45.98%     | ok               |
| EWJ        |       64 | -23.51%  | 43.97%             | -29.40% |    -0.82 | 37.10%     | ok               |
| FCX        |       65 | -30.08%  | 44.57%             | -47.67% |    -0.34 | 44.43%     | ok               |
| FET-USD    |       73 | -34.49%  | -68.49%            | -60.12% |    -0.14 | 39.27%     | ok               |
| FIL-USD    |       69 | -60.37%  | -67.13%            | -60.56% |    -0.92 | 32.57%     | ok               |
| FXI        |       46 | -4.88%   | 38.71%             | -23.91% |    -0.04 | 32.11%     | ok               |
| GDX        |       60 | 2.69%    | 184.81%            | -34.99% |     0.18 | 45.26%     | ok               |
| GDXJ       |       68 | -34.03%  | 192.23%            | -44.61% |    -0.42 | 43.26%     | ok               |
| GE         |       80 | -13.68%  | 88.81%             | -27.82% |    -0.15 | 47.75%     | ok               |
| GLD        |       54 | 8.88%    | 83.29%             | -14.86% |     0.29 | 45.26%     | ok               |
| GOOGL      |       55 | 61.75%   | 117.98%            | -20.41% |     1.02 | 47.75%     | ok               |
| GRT-USD    |       83 | -29.70%  | -78.00%            | -53.91% |    -0.21 | 41.95%     | ok               |
| GS         |       66 | -3.01%   | 130.35%            | -22.13% |     0.03 | 47.42%     | ok               |
| HD         |       73 | -3.88%   | -9.89%             | -18.07% |    -0.02 | 42.60%     | ok               |
| HON        |       92 | -21.68%  | 4.92%              | -33.57% |    -0.5  | 55.74%     | ok               |
| HYG        |       89 | -9.20%   | 2.18%              | -10.59% |    -1.07 | 35.61%     | ok               |
| IBIT       |       36 | 29.08%   | 13.42%             | -18.95% |     0.6  | 32.63%     | ok               |
| IBM        |       73 | -25.87%  | 36.32%             | -48.94% |    -0.31 | 50.75%     | ok               |
| ICP-USD    |       75 | -7.84%   | -49.73%            | -47.52% |     0.18 | 36.40%     | ok               |
| IEF        |       84 | -12.28%  | -1.14%             | -13.06% |    -1.75 | 32.78%     | ok               |
| IEMG       |       60 | -7.71%   | 57.15%             | -26.84% |    -0.2  | 41.43%     | ok               |
| INJ-USD    |       71 | -51.30%  | -32.06%            | -74.43% |    -0.46 | 37.93%     | ok               |
| INTC       |       68 | 35.30%   | 183.37%            | -60.60% |     0.5  | 48.25%     | ok               |
| INTU       |       71 | -17.93%  | -47.81%            | -42.15% |    -0.18 | 44.59%     | ok               |
| ITA        |       72 | -0.83%   | 65.42%             | -23.75% |     0.05 | 48.59%     | ok               |
| IWM        |       54 | 11.41%   | 43.60%             | -12.65% |     0.46 | 36.44%     | ok               |
| JNJ        |       68 | 1.05%    | 78.66%             | -17.51% |     0.1  | 47.75%     | ok               |
| JPM        |       73 | -20.40%  | 83.45%             | -32.74% |    -0.53 | 48.09%     | ok               |
| KO         |       54 | 28.06%   | 46.29%             | -8.64%  |     0.96 | 40.27%     | ok               |
| LDO-USD    |       74 | -0.29%   | -53.06%            | -63.49% |     0.28 | 46.55%     | ok               |
| LIN        |       70 | -10.87%  | 4.02%              | -20.61% |    -0.35 | 36.27%     | ok               |
| LINK-USD   |       72 | 43.06%   | -14.15%            | -33.64% |     0.6  | 45.79%     | ok               |
| LLY        |       71 | -29.59%  | 52.36%             | -53.34% |    -0.45 | 48.25%     | ok               |
| LRCX       |       84 | -25.21%  | 205.23%            | -61.08% |    -0.15 | 42.43%     | ok               |
| LTC-USD    |       70 | -8.16%   | -34.14%            | -33.94% |     0.08 | 51.72%     | ok               |
| MCD        |       77 | -6.44%   | -8.70%             | -21.88% |    -0.21 | 37.44%     | ok               |
| META       |       80 | -33.87%  | 35.10%             | -44.90% |    -0.59 | 48.09%     | ok               |
| MPC        |       67 | 9.62%    | 105.78%            | -37.91% |     0.28 | 49.92%     | ok               |
| MRK        |       65 | -23.79%  | 13.33%             | -35.95% |    -0.46 | 44.09%     | ok               |
| MS         |       77 | -11.95%  | 120.01%            | -27.79% |    -0.22 | 47.75%     | ok               |
| MSFT       |       79 | -29.20%  | 21.97%             | -38.06% |    -0.67 | 49.42%     | ok               |
| MU         |       49 | 164.65%  | 724.83%            | -68.76% |     1.08 | 53.91%     | ok               |
| NEAR-USD   |       73 | 4.36%    | 12.13%             | -60.10% |     0.29 | 42.34%     | ok               |
| NEM        |       66 | -15.52%  | 229.33%            | -39.56% |    -0.06 | 53.08%     | ok               |
| NFLX       |       76 | 12.79%   | 34.83%             | -21.09% |     0.35 | 53.24%     | ok               |
| NKE        |       79 | -27.89%  | -61.48%            | -55.35% |    -0.32 | 43.76%     | ok               |
| NOW        |       86 | 11.46%   | -4.24%             | -30.43% |     0.3  | 50.08%     | ok               |
| NVDA       |       77 | -47.12%  | 62.23%             | -52.37% |    -0.61 | 57.40%     | ok               |
| OP-USD     |       70 | -41.65%  | -85.98%            | -68.74% |    -0.33 | 33.14%     | ok               |
| ORCL       |       64 | 93.16%   | 21.95%             | -30.61% |     0.84 | 54.41%     | ok               |
| OXY        |       73 | -5.65%   | -5.74%             | -31.20% |     0.03 | 44.09%     | ok               |
| PEP        |       74 | -3.96%   | -20.86%            | -21.35% |    -0.05 | 45.76%     | ok               |
| PEPE-USD   |       89 | -39.87%  | -53.17%            | -57.66% |    -0.17 | 47.70%     | ok               |
| PFE        |       83 | -35.79%  | 4.67%              | -43.50% |    -1.05 | 39.60%     | ok               |
| PG         |       64 | -21.45%  | -9.18%             | -24.25% |    -0.84 | 37.10%     | ok               |
| PM         |       79 | -5.31%   | 98.76%             | -35.15% |    -0.03 | 53.58%     | ok               |
| POL-USD    |       85 | 16.20%   | -49.37%            | -45.67% |     0.38 | 49.23%     | ok               |
| QCOM       |       75 | -15.16%  | 16.39%             | -56.59% |    -0.04 | 42.93%     | ok               |
| QQQ        |       66 | 13.22%   | 65.75%             | -14.20% |     0.41 | 46.42%     | ok               |
| RENDER-USD |      100 | -40.65%  | -65.27%            | -46.98% |    -0.21 | 45.59%     | ok               |
| RTX        |       58 | 33.40%   | 92.84%             | -16.99% |     0.75 | 52.91%     | ok               |
| SBUX       |       58 | -14.93%  | 9.91%              | -29.22% |    -0.25 | 37.77%     | ok               |
| SCHW       |       78 | -16.21%  | 43.28%             | -31.92% |    -0.33 | 47.59%     | ok               |
| SHIB-USD   |       84 | -41.62%  | -59.11%            | -45.01% |    -0.43 | 52.30%     | ok               |
| SHY        |       48 | -2.10%   | 0.04%              | -3.30%  |    -0.72 | 34.61%     | ok               |
| SKY-USD    |       82 | -35.73%  | 5.17%              | -48.30% |    -0.41 | 45.35%     | ok               |
| SLB        |       77 | -36.39%  | 9.38%              | -56.91% |    -0.68 | 50.42%     | ok               |
| SLV        |       70 | 13.89%   | 130.21%            | -42.66% |     0.34 | 41.76%     | ok               |
| SMH        |       48 | 67.47%   | 160.88%            | -34.29% |     0.99 | 44.93%     | ok               |
| SNX-USD    |       62 | -19.67%  | -68.58%            | -47.16% |    -0.02 | 33.14%     | ok               |
| SOL-USD    |       68 | -15.20%  | -24.12%            | -44.99% |     0.05 | 59.39%     | ok               |
| SOXX       |       58 | 68.55%   | 142.31%            | -40.14% |     0.94 | 43.43%     | ok               |
| SPY        |       64 | 3.49%    | 49.79%             | -15.53% |     0.18 | 51.58%     | ok               |
| SUSHI-USD  |      102 | -82.04%  | -62.71%            | -82.74% |    -1.42 | 37.74%     | ok               |
| T          |       70 | 47.42%   | 61.94%             | -17.01% |     0.97 | 58.24%     | ok               |
| TGT        |       58 | -11.96%  | -7.27%             | -35.83% |    -0.19 | 37.60%     | ok               |
| TIA-USD    |       87 | -59.88%  | -86.36%            | -72.44% |    -0.55 | 41.19%     | ok               |
| TLT        |       74 | -19.18%  | -9.35%             | -22.03% |    -1.4  | 34.28%     | ok               |
| TMO        |       65 | 24.66%   | 11.63%             | -18.85% |     0.54 | 54.08%     | ok               |
| TMUS       |       76 | 2.41%    | 10.55%             | -27.06% |     0.15 | 48.25%     | ok               |
| TRX-USD    |       68 | 10.93%   | 31.25%             | -22.90% |     0.38 | 52.30%     | ok               |
| TSLA       |       80 | -35.03%  | 146.46%            | -58.36% |    -0.22 | 43.09%     | ok               |
| TXN        |       73 | -19.79%  | 59.20%             | -46.98% |    -0.17 | 49.58%     | ok               |
| UNH        |       72 | 35.31%   | -22.68%            | -26.31% |     0.58 | 50.08%     | ok               |
| UNI-USD    |       94 | -64.80%  | 20.52%             | -78.80% |    -0.63 | 48.66%     | ok               |
| UPS        |       70 | -34.92%  | -31.25%            | -38.32% |    -0.69 | 40.10%     | ok               |
| USO        |       70 | 14.81%   | 102.38%            | -41.71% |     0.35 | 32.45%     | ok               |
| VEA        |       60 | -6.17%   | 46.37%             | -19.52% |    -0.21 | 42.93%     | ok               |
| VIXY       |       98 | -77.12%  | -67.82%            | -88.17% |    -0.9  | 34.28%     | ok               |
| VNQ        |       75 | -16.81%  | 17.00%             | -24.92% |    -0.7  | 38.60%     | ok               |
| VTI        |       70 | -5.97%   | 48.78%             | -17.64% |    -0.16 | 51.75%     | ok               |
| VWO        |       80 | -16.62%  | 42.42%             | -25.20% |    -0.61 | 41.76%     | ok               |
| VZ         |       83 | -17.37%  | 29.60%             | -25.90% |    -0.5  | 40.93%     | ok               |
| WFC        |       80 | -18.14%  | 47.23%             | -29.78% |    -0.3  | 46.76%     | ok               |
| WIF-USD    |       66 | -25.46%  | -59.70%            | -52.76% |     0    | 35.63%     | ok               |
| WMT        |       65 | 10.38%   | 82.92%             | -21.98% |     0.35 | 48.09%     | ok               |
| XBI        |       66 | 2.05%    | 81.88%             | -18.30% |     0.14 | 42.10%     | ok               |
| XLB        |       60 | -12.29%  | 14.93%             | -25.04% |    -0.43 | 31.95%     | ok               |
| XLC        |       63 | 14.20%   | 41.14%             | -12.33% |     0.52 | 50.58%     | ok               |
| XLE        |       75 | -12.75%  | 37.18%             | -35.77% |    -0.25 | 45.09%     | ok               |
| XLF        |       80 | -9.66%   | 38.22%             | -23.61% |    -0.3  | 45.92%     | ok               |
| XLI        |       76 | -5.32%   | 37.20%             | -14.16% |    -0.16 | 41.26%     | ok               |
| XLK        |       40 | 66.88%   | 86.42%             | -14.75% |     1.23 | 47.42%     | ok               |
| XLM-USD    |       67 | -12.03%  | -25.46%            | -54.58% |     0.08 | 46.74%     | ok               |
| XLP        |       64 | 8.83%    | 11.11%             | -8.96%  |     0.53 | 39.27%     | ok               |
| XLU        |       67 | -3.52%   | 24.57%             | -20.40% |    -0.11 | 39.27%     | ok               |
| XLV        |       68 | -15.65%  | 18.66%             | -19.39% |    -0.71 | 37.27%     | ok               |
| XLY        |       79 | -6.85%   | 28.53%             | -17.23% |    -0.15 | 46.09%     | ok               |
| XOM        |       59 | -2.13%   | 39.90%             | -20.29% |     0.02 | 34.94%     | ok               |
| XRP-USD    |       60 | 9.21%    | -38.21%            | -33.91% |     0.3  | 36.59%     | ok               |
| YFI-USD    |       79 | -66.69%  | -55.26%            | -72.54% |    -1.18 | 38.70%     | ok               |
| ZEC-USD    |       64 | 109.88%  | 3033.88%           | -56.50% |     0.82 | 41.00%     | ok               |

## AAPL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 15.36%   | 98.53%             | -22.53% |     0.38 |       71 | 54.41%     | ok               |
|          15 | 11.19%   | 98.53%             | -24.50% |     0.31 |       82 | 61.56%     | ok               |
|          40 | 8.67%    | 98.53%             | -28.08% |     0.28 |       56 | 44.26%     | ok               |
|          30 | 8.57%    | 98.53%             | -23.09% |     0.27 |       62 | 49.58%     | ok               |
|          35 | 7.01%    | 98.53%             | -24.45% |     0.24 |       62 | 48.25%     | ok               |

## AAVE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 41.68%   | -12.89%            | -43.61% |     0.59 |       43 | 35.06%     | ok               |
|          45 | 28.48%   | -12.89%            | -49.19% |     0.49 |       48 | 29.89%     | ok               |
|          35 | 23.59%   | -12.89%            | -48.79% |     0.45 |       51 | 38.12%     | ok               |
|          50 | 10.25%   | -12.89%            | -45.07% |     0.31 |       44 | 22.03%     | ok               |
|          15 | -25.72%  | -12.89%            | -61.76% |     0.02 |       76 | 56.13%     | ok               |

## ABBV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -14.35%  | 55.15%             | -26.55% |    -0.31 |       52 | 35.44%     | ok               |
|          40 | -24.31%  | 55.15%             | -27.36% |    -0.59 |       68 | 39.93%     | ok               |
|          45 | -24.40%  | 55.15%             | -27.66% |    -0.6  |       60 | 37.10%     | ok               |
|          30 | -26.75%  | 55.15%             | -31.23% |    -0.61 |       72 | 47.75%     | ok               |
|          25 | -30.26%  | 55.15%             | -35.52% |    -0.69 |       71 | 50.42%     | ok               |

## ADA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 18.28%   | -69.26%            | -35.54% |     0.41 |       48 | 25.67%     | ok               |
|          45 | 7.00%    | -69.26%            | -34.64% |     0.28 |       51 | 30.65%     | ok               |
|          40 | -12.03%  | -69.26%            | -40.73% |     0.06 |       63 | 36.78%     | ok               |
|          35 | -17.94%  | -69.26%            | -42.89% |    -0    |       67 | 41.38%     | ok               |
|          15 | -31.89%  | -69.26%            | -47.27% |    -0.06 |       73 | 63.41%     | ok               |

## ADBE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 2.81%    | -45.49%            | -29.07% |     0.19 |       53 | 59.73%     | ok               |
|          35 | -4.62%   | -45.49%            | -30.52% |     0.05 |       76 | 47.25%     | ok               |
|          20 | -12.46%  | -45.49%            | -31.52% |    -0.03 |       59 | 62.90%     | ok               |
|          30 | -14.39%  | -45.49%            | -31.20% |    -0.08 |       69 | 55.91%     | ok               |
|          15 | -20.84%  | -45.49%            | -34.98% |    -0.16 |       66 | 64.56%     | ok               |

## AGG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -5.06%   | 0.22%              | -7.92%  |    -1.1  |       50 | 18.47%     | ok               |
|          30 | -7.70%   | 0.22%              | -10.95% |    -1.26 |       69 | 32.61%     | ok               |
|          20 | -8.77%   | 0.22%              | -11.83% |    -1.3  |       72 | 37.94%     | ok               |
|          25 | -8.69%   | 0.22%              | -12.22% |    -1.34 |       71 | 36.11%     | ok               |
|          45 | -7.13%   | 0.22%              | -9.11%  |    -1.36 |       60 | 23.13%     | ok               |

## ALGO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -34.91%  | -51.12%            | -43.00% |    -0.29 |       80 | 39.27%     | ok               |
|          15 | -40.56%  | -51.12%            | -51.70% |    -0.3  |       80 | 50.19%     | ok               |
|          25 | -44.02%  | -51.12%            | -59.19% |    -0.41 |       80 | 44.83%     | ok               |
|          20 | -46.81%  | -51.12%            | -55.13% |    -0.44 |       82 | 47.70%     | ok               |
|          35 | -46.20%  | -51.12%            | -49.75% |    -0.62 |       62 | 32.76%     | ok               |

## AMAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -24.77%  | 117.95%            | -53.90% |    -0.12 |       68 | 58.40%     | ok               |
|          30 | -31.93%  | 117.95%            | -57.08% |    -0.28 |       65 | 49.25%     | ok               |
|          35 | -31.65%  | 117.95%            | -54.63% |    -0.29 |       65 | 46.76%     | ok               |
|          50 | -29.89%  | 117.95%            | -47.29% |    -0.3  |       46 | 35.11%     | ok               |
|          40 | -35.34%  | 117.95%            | -55.84% |    -0.37 |       63 | 42.10%     | ok               |

## AMD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 14.50%   | 231.12%            | -40.05% |     0.34 |       56 | 29.45%     | ok               |
|          40 | 11.68%   | 231.12%            | -41.09% |     0.32 |       52 | 34.44%     | ok               |
|          35 | 9.37%    | 231.12%            | -43.15% |     0.3  |       60 | 35.94%     | ok               |
|          30 | 0.73%    | 231.12%            | -46.73% |     0.22 |       61 | 38.60%     | ok               |
|          25 | -6.18%   | 231.12%            | -52.51% |     0.16 |       61 | 41.26%     | ok               |

## AMGN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -2.11%   | 37.33%             | -26.65% |     0.07 |       65 | 56.41%     | ok               |
|          35 | -4.38%   | 37.33%             | -31.29% |     0.01 |       67 | 47.09%     | ok               |
|          15 | -6.10%   | 37.33%             | -27.98% |    -0.01 |       62 | 60.40%     | ok               |
|          30 | -8.10%   | 37.33%             | -34.19% |    -0.07 |       69 | 50.75%     | ok               |
|          25 | -10.12%  | 37.33%             | -33.47% |    -0.11 |       63 | 53.08%     | ok               |

## AMZN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -25.14%  | 38.36%             | -27.34% |    -0.75 |       54 | 30.45%     | ok               |
|          50 | -29.72%  | 38.36%             | -32.41% |    -1.07 |       50 | 23.46%     | ok               |
|          45 | -35.00%  | 38.36%             | -36.26% |    -1.23 |       56 | 26.96%     | ok               |
|          35 | -51.09%  | 38.36%             | -51.92% |    -1.48 |       77 | 35.61%     | ok               |
|          30 | -56.13%  | 38.36%             | -57.22% |    -1.6  |       84 | 41.60%     | ok               |

## APT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -3.75%   | -88.64%            | -41.46% |     0.1  |       42 | 16.86%     | ok               |
|          45 | -23.29%  | -88.64%            | -58.83% |    -0.13 |       58 | 23.18%     | ok               |
|          20 | -37.13%  | -88.64%            | -66.07% |    -0.17 |       81 | 49.23%     | ok               |
|          35 | -32.07%  | -88.64%            | -57.66% |    -0.18 |       72 | 34.10%     | ok               |
|          25 | -38.91%  | -88.64%            | -65.88% |    -0.22 |       74 | 44.64%     | ok               |

## ARB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 64.25%   | -47.24%            | -45.20% |     0.68 |       83 | 59.58%     | ok               |
|          45 | 44.75%   | -47.24%            | -35.92% |     0.59 |       56 | 25.10%     | ok               |
|          50 | 32.94%   | -47.24%            | -30.72% |     0.51 |       42 | 17.82%     | ok               |
|          40 | 29.82%   | -47.24%            | -39.80% |     0.49 |       57 | 32.95%     | ok               |
|          20 | 26.26%   | -47.24%            | -53.77% |     0.48 |       69 | 53.45%     | ok               |

## ARKK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -21.03%  | 90.31%             | -37.76% |    -0.19 |       93 | 56.07%     | ok               |
|          20 | -25.37%  | 90.31%             | -34.82% |    -0.29 |       91 | 51.58%     | ok               |
|          30 | -30.79%  | 90.31%             | -33.41% |    -0.47 |       89 | 44.26%     | ok               |
|          35 | -36.24%  | 90.31%             | -37.00% |    -0.63 |       90 | 41.60%     | ok               |
|          40 | -35.38%  | 90.31%             | -40.75% |    -0.64 |       80 | 36.77%     | ok               |

## ATOM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -42.12%  | -63.67%            | -48.20% |    -0.36 |       86 | 63.98%     | ok               |
|          25 | -49.57%  | -63.67%            | -52.95% |    -0.56 |       90 | 52.87%     | ok               |
|          20 | -57.02%  | -63.67%            | -59.03% |    -0.72 |       94 | 56.70%     | ok               |
|          30 | -60.00%  | -63.67%            | -61.22% |    -0.89 |       88 | 46.74%     | ok               |
|          45 | -56.83%  | -63.67%            | -57.44% |    -1    |       76 | 31.61%     | ok               |

## AVAX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 26.00%   | -62.57%            | -22.06% |     0.53 |       30 | 17.05%     | ok               |
|          40 | 18.88%   | -62.57%            | -26.27% |     0.42 |       32 | 24.14%     | ok               |
|          45 | 15.54%   | -62.57%            | -23.19% |     0.38 |       26 | 21.07%     | ok               |
|          35 | -2.83%   | -62.57%            | -33.05% |     0.14 |       52 | 30.46%     | ok               |
|          15 | -12.08%  | -62.57%            | -42.39% |     0.1  |       74 | 52.30%     | ok               |

## AVGO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 30.23%   | 171.59%            | -38.01% |     0.49 |       68 | 44.09%     | ok               |
|          30 | 26.59%   | 171.59%            | -36.08% |     0.45 |       64 | 41.43%     | ok               |
|          20 | 15.29%   | 171.59%            | -39.42% |     0.34 |       77 | 47.25%     | ok               |
|          40 | 13.18%   | 171.59%            | -40.70% |     0.32 |       66 | 35.11%     | ok               |
|          35 | 13.06%   | 171.59%            | -37.55% |     0.32 |       74 | 38.27%     | ok               |

## BA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 26.02%   | 23.94%             | -13.34% |     0.66 |       44 | 32.95%     | ok               |
|          35 | 20.07%   | 23.94%             | -21.02% |     0.45 |       70 | 45.59%     | ok               |
|          40 | 14.26%   | 23.94%             | -23.87% |     0.37 |       48 | 40.43%     | ok               |
|          25 | 2.07%    | 23.94%             | -29.13% |     0.16 |       72 | 53.08%     | ok               |
|          30 | -0.98%   | 23.94%             | -27.11% |     0.11 |       69 | 49.58%     | ok               |

## BAC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -4.91%   | 55.12%             | -18.41% |    -0.03 |       80 | 53.24%     | ok               |
|          15 | -10.08%  | 55.12%             | -21.05% |    -0.16 |       82 | 58.57%     | ok               |
|          45 | -7.14%   | 55.12%             | -19.71% |    -0.16 |       64 | 36.44%     | ok               |
|          25 | -9.60%   | 55.12%             | -24.29% |    -0.18 |       80 | 51.25%     | ok               |
|          50 | -8.24%   | 55.12%             | -16.81% |    -0.22 |       64 | 32.78%     | ok               |

## BCH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 73.30%   | -35.90%            | -45.51% |     0.78 |       73 | 58.62%     | ok               |
|          20 | 43.28%   | -35.90%            | -45.82% |     0.59 |       69 | 55.17%     | ok               |
|          30 | 23.02%   | -35.90%            | -53.87% |     0.44 |       78 | 49.04%     | ok               |
|          25 | 22.42%   | -35.90%            | -51.09% |     0.43 |       70 | 51.72%     | ok               |
|          35 | 0.42%    | -35.90%            | -57.99% |     0.22 |       72 | 44.64%     | ok               |

## BITO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -3.95%   | -64.74%            | -31.98% |     0.08 |       54 | 24.13%     | ok               |
|          30 | -14.59%  | -64.74%            | -39.47% |    -0.03 |       76 | 39.93%     | ok               |
|          15 | -22.80%  | -64.74%            | -48.38% |    -0.09 |       85 | 48.92%     | ok               |
|          35 | -18.76%  | -64.74%            | -41.51% |    -0.1  |       68 | 35.77%     | ok               |
|          45 | -17.19%  | -64.74%            | -36.67% |    -0.12 |       60 | 27.62%     | ok               |

## BLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -1.73%   | 38.09%             | -21.48% |     0.04 |       84 | 52.75%     | ok               |
|          35 | -1.28%   | 38.09%             | -20.79% |     0.04 |       88 | 44.43%     | ok               |
|          40 | -2.11%   | 38.09%             | -22.83% |     0.01 |       76 | 39.77%     | ok               |
|          25 | -3.14%   | 38.09%             | -24.62% |    -0    |       77 | 50.58%     | ok               |
|          30 | -7.64%   | 38.09%             | -26.90% |    -0.14 |       81 | 48.09%     | ok               |

## BND Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.95%   | 0.28%              | -10.21% |    -1    |       66 | 40.10%     | ok               |
|          25 | -7.59%   | 0.28%              | -11.27% |    -1.14 |       69 | 38.10%     | ok               |
|          15 | -8.65%   | 0.28%              | -11.52% |    -1.23 |       77 | 42.76%     | ok               |
|          30 | -8.03%   | 0.28%              | -10.70% |    -1.27 |       71 | 34.61%     | ok               |
|          40 | -9.42%   | 0.28%              | -11.70% |    -1.68 |       64 | 27.62%     | ok               |

## BONK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 139.43%  | -79.61%            | -35.57% |     1.13 |       44 | 21.84%     | ok               |
|          15 | 101.57%  | -79.61%            | -62.48% |     0.82 |       68 | 59.58%     | ok               |
|          25 | 71.50%   | -79.61%            | -51.34% |     0.72 |       71 | 51.15%     | ok               |
|          20 | 70.13%   | -79.61%            | -58.35% |     0.71 |       65 | 55.75%     | ok               |
|          45 | 39.98%   | -79.61%            | -47.53% |     0.57 |       64 | 27.59%     | ok               |

## BTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 65.88%   | -9.39%             | -12.20% |     1.17 |       38 | 32.18%     | ok               |
|          35 | 64.02%   | -9.39%             | -21.56% |     1.09 |       60 | 41.95%     | ok               |
|          40 | 60.40%   | -9.39%             | -14.50% |     1.08 |       42 | 36.02%     | ok               |
|          50 | 31.38%   | -9.39%             | -19.38% |     0.73 |       38 | 26.63%     | ok               |
|          30 | 35.58%   | -9.39%             | -21.75% |     0.68 |       66 | 47.89%     | ok               |

## C Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -10.42%  | 117.28%            | -21.80% |    -0.23 |       66 | 33.11%     | ok               |
|          45 | -21.42%  | 117.28%            | -29.60% |    -0.53 |       76 | 37.44%     | ok               |
|          25 | -30.32%  | 117.28%            | -36.44% |    -0.61 |       69 | 49.75%     | ok               |
|          40 | -26.93%  | 117.28%            | -35.11% |    -0.66 |       76 | 39.77%     | ok               |
|          15 | -34.40%  | 117.28%            | -38.43% |    -0.67 |       74 | 56.74%     | ok               |

## CAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 10.27%   | 115.70%            | -22.07% |     0.29 |       66 | 52.41%     | ok               |
|          30 | 10.17%   | 115.70%            | -18.88% |     0.29 |       70 | 49.58%     | ok               |
|          15 | 6.70%    | 115.70%            | -26.40% |     0.24 |       75 | 63.23%     | ok               |
|          20 | 5.21%    | 115.70%            | -21.30% |     0.21 |       78 | 56.07%     | ok               |
|          45 | 2.71%    | 115.70%            | -26.22% |     0.16 |       56 | 38.27%     | ok               |

## CL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 4.72%    | -1.78%             | -12.98% |     0.24 |       42 | 25.62%     | ok               |
|          30 | 5.11%    | -1.78%             | -14.32% |     0.23 |       60 | 41.10%     | ok               |
|          45 | 1.03%    | -1.78%             | -13.51% |     0.09 |       46 | 28.29%     | ok               |
|          35 | 0.39%    | -1.78%             | -13.83% |     0.07 |       62 | 37.60%     | ok               |
|          40 | -2.52%   | -1.78%             | -12.70% |    -0.04 |       56 | 32.28%     | ok               |

## CMCSA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -42.64%  | -35.44%            | -48.37% |    -0.96 |       91 | 56.91%     | ok               |
|          30 | -43.76%  | -35.44%            | -49.38% |    -1.14 |       82 | 42.26%     | ok               |
|          35 | -43.58%  | -35.44%            | -49.22% |    -1.22 |       93 | 36.94%     | ok               |
|          25 | -47.24%  | -35.44%            | -52.51% |    -1.25 |       89 | 47.59%     | ok               |
|          50 | -31.71%  | -35.44%            | -31.71% |    -1.27 |       48 | 13.48%     | ok               |

## COMP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -5.51%   | -53.56%            | -38.71% |     0.13 |       44 | 21.65%     | ok               |
|          30 | -46.68%  | -53.56%            | -56.58% |    -0.37 |       97 | 47.89%     | ok               |
|          25 | -51.95%  | -53.56%            | -55.45% |    -0.45 |       96 | 55.75%     | ok               |
|          40 | -47.85%  | -53.56%            | -53.14% |    -0.49 |       70 | 35.25%     | ok               |
|          45 | -47.75%  | -53.56%            | -55.45% |    -0.52 |       62 | 29.69%     | ok               |

## COP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -2.92%   | 8.76%              | -34.21% |     0.03 |       50 | 29.62%     | ok               |
|          35 | -10.97%  | 8.76%              | -43.58% |    -0.12 |       69 | 40.77%     | ok               |
|          45 | -9.62%   | 8.76%              | -40.57% |    -0.12 |       60 | 33.78%     | ok               |
|          30 | -14.68%  | 8.76%              | -43.40% |    -0.19 |       70 | 43.93%     | ok               |
|          40 | -15.32%  | 8.76%              | -46.34% |    -0.24 |       66 | 36.94%     | ok               |

## COST Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 14.02%   | 24.72%             | -24.32% |     0.47 |       62 | 47.75%     | ok               |
|          25 | 10.99%   | 24.72%             | -24.73% |     0.39 |       61 | 44.93%     | ok               |
|          35 | 7.34%    | 24.72%             | -27.39% |     0.31 |       56 | 39.27%     | ok               |
|          30 | 2.04%    | 24.72%             | -29.73% |     0.13 |       60 | 41.93%     | ok               |
|          15 | -0.87%   | 24.72%             | -27.30% |     0.05 |       65 | 51.25%     | ok               |

## CRM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -18.91%  | -7.60%             | -34.84% |    -0.21 |       64 | 41.10%     | ok               |
|          15 | -24.40%  | -7.60%             | -47.54% |    -0.23 |       92 | 57.57%     | ok               |
|          40 | -22.84%  | -7.60%             | -40.30% |    -0.31 |       70 | 36.94%     | ok               |
|          30 | -26.81%  | -7.60%             | -45.51% |    -0.34 |       67 | 46.09%     | ok               |
|          25 | -27.97%  | -7.60%             | -48.12% |    -0.35 |       68 | 48.75%     | ok               |

## CRV-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 76.24%   | -47.27%            | -37.78% |     0.79 |       68 | 36.78%     | ok               |
|          40 | 46.02%   | -47.27%            | -38.86% |     0.61 |       58 | 32.38%     | ok               |
|          30 | 37.75%   | -47.27%            | -39.89% |     0.55 |       68 | 41.57%     | ok               |
|          45 | 35.94%   | -47.27%            | -42.29% |     0.55 |       58 | 25.29%     | ok               |
|          50 | 35.01%   | -47.27%            | -30.73% |     0.54 |       50 | 21.26%     | ok               |

## CSCO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 31.56%   | 127.79%            | -19.34% |     0.68 |       48 | 36.77%     | ok               |
|          45 | 27.11%   | 127.79%            | -19.34% |     0.59 |       50 | 38.44%     | ok               |
|          25 | 22.29%   | 127.79%            | -23.28% |     0.49 |       57 | 49.08%     | ok               |
|          35 | 18.25%   | 127.79%            | -23.68% |     0.43 |       54 | 45.26%     | ok               |
|          20 | 16.35%   | 127.79%            | -22.32% |     0.39 |       67 | 51.41%     | ok               |

## CVX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -2.27%   | 33.72%             | -27.34% |     0.01 |       75 | 36.44%     | ok               |
|          25 | -3.09%   | 33.72%             | -24.33% |     0    |       73 | 43.76%     | ok               |
|          45 | -2.69%   | 33.72%             | -28.83% |    -0.01 |       67 | 33.11%     | ok               |
|          35 | -5.72%   | 33.72%             | -28.85% |    -0.08 |       69 | 38.44%     | ok               |
|          50 | -5.28%   | 33.72%             | -30.69% |    -0.11 |       60 | 28.79%     | ok               |

## DASH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 245.37%  | 146.57%            | -21.09% |     1.24 |       36 | 16.67%     | ok               |
|          40 | 158.23%  | 146.57%            | -25.22% |     1    |       42 | 22.99%     | ok               |
|          45 | 156.18%  | 146.57%            | -26.87% |     1    |       38 | 18.58%     | ok               |
|          35 | -2.24%   | 146.57%            | -63.41% |     0.36 |       65 | 27.39%     | ok               |
|          30 | -3.96%   | 146.57%            | -64.43% |     0.35 |       57 | 29.69%     | ok               |

## DBC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 2.96%    | 43.08%             | -26.32% |     0.16 |       79 | 39.60%     | ok               |
|          25 | -0.45%   | 43.08%             | -25.43% |     0.05 |       66 | 36.27%     | ok               |
|          20 | -1.57%   | 43.08%             | -25.96% |     0.01 |       71 | 37.94%     | ok               |
|          50 | -1.89%   | 43.08%             | -20.31% |    -0.02 |       46 | 23.96%     | ok               |
|          30 | -2.94%   | 43.08%             | -25.02% |    -0.03 |       64 | 34.44%     | ok               |

## DE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 3.91%    | 72.21%             | -17.97% |     0.18 |       58 | 29.28%     | ok               |
|          45 | -2.61%   | 72.21%             | -19.56% |     0.02 |       62 | 33.94%     | ok               |
|          20 | -5.79%   | 72.21%             | -24.13% |    -0.02 |       69 | 49.08%     | ok               |
|          25 | -9.02%   | 72.21%             | -24.31% |    -0.1  |       75 | 47.09%     | ok               |
|          30 | -10.06%  | 72.21%             | -22.93% |    -0.13 |       74 | 44.26%     | ok               |

## DIA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -2.74%   | 35.38%             | -11.28% |    -0.11 |       62 | 46.26%     | ok               |
|          35 | -2.75%   | 35.38%             | -13.15% |    -0.12 |       64 | 41.93%     | ok               |
|          30 | -5.37%   | 35.38%             | -12.94% |    -0.26 |       66 | 44.76%     | ok               |
|          20 | -6.13%   | 35.38%             | -13.85% |    -0.28 |       68 | 48.75%     | ok               |
|          40 | -6.68%   | 35.38%             | -15.06% |    -0.36 |       70 | 39.27%     | ok               |

## DIS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 20.23%   | -6.41%             | -13.06% |     0.63 |       46 | 25.46%     | ok               |
|          40 | -3.91%   | -6.41%             | -18.75% |     0    |       61 | 33.94%     | ok               |
|          45 | -6.91%   | -6.41%             | -16.54% |    -0.09 |       47 | 29.12%     | ok               |
|          15 | -13.22%  | -6.41%             | -32.73% |    -0.16 |       89 | 55.24%     | ok               |
|          35 | -12.04%  | -6.41%             | -25.70% |    -0.18 |       75 | 40.27%     | ok               |

## DOGE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 0.31%    | -50.49%            | -57.89% |     0.28 |       77 | 64.37%     | ok               |
|          20 | -2.21%   | -50.49%            | -55.83% |     0.25 |       78 | 59.20%     | ok               |
|          25 | -10.67%  | -50.49%            | -53.72% |     0.16 |       70 | 55.17%     | ok               |
|          30 | -27.56%  | -50.49%            | -60.95% |    -0.06 |       71 | 49.04%     | ok               |
|          50 | -35.28%  | -50.49%            | -56.78% |    -0.33 |       58 | 23.56%     | ok               |

## DOT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -44.57%  | -73.92%            | -53.23% |    -0.58 |       54 | 30.27%     | ok               |
|          50 | -42.49%  | -73.92%            | -48.78% |    -0.59 |       60 | 24.71%     | ok               |
|          15 | -67.28%  | -73.92%            | -72.06% |    -0.63 |       83 | 63.79%     | ok               |
|          20 | -63.89%  | -73.92%            | -68.06% |    -0.64 |       93 | 59.96%     | ok               |
|          35 | -60.23%  | -73.92%            | -61.93% |    -0.65 |       84 | 41.57%     | ok               |

## DXY-INDEX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -4.11%   | -6.44%             | -6.28%  |    -0.66 |       40 | 29.44%     | ok               |
|          40 | -5.77%   | -6.44%             | -7.30%  |    -0.78 |       72 | 45.89%     | ok               |
|          15 | -8.90%   | -6.44%             | -11.61% |    -0.87 |       93 | 72.94%     | ok               |
|          45 | -6.41%   | -6.44%             | -8.40%  |    -0.94 |       62 | 35.28%     | ok               |
|          25 | -9.21%   | -6.44%             | -12.10% |    -1.06 |       86 | 62.77%     | ok               |

## EEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -5.41%   | 62.49%             | -15.88% |    -0.14 |       54 | 34.11%     | ok               |
|          45 | -6.13%   | 62.49%             | -17.36% |    -0.16 |       54 | 35.77%     | ok               |
|          40 | -6.47%   | 62.49%             | -19.52% |    -0.17 |       66 | 37.94%     | ok               |
|          35 | -7.12%   | 62.49%             | -23.88% |    -0.17 |       68 | 39.93%     | ok               |
|          30 | -10.43%  | 62.49%             | -25.67% |    -0.28 |       64 | 41.76%     | ok               |

## EFA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -4.79%   | 35.39%             | -10.10% |    -0.11 |       62 | 49.75%     | ok               |
|          30 | -10.29%  | 35.39%             | -12.96% |    -0.4  |       58 | 41.26%     | ok               |
|          20 | -11.69%  | 35.39%             | -12.73% |    -0.43 |       69 | 46.92%     | ok               |
|          25 | -13.03%  | 35.39%             | -15.23% |    -0.51 |       66 | 44.26%     | ok               |
|          40 | -12.48%  | 35.39%             | -14.85% |    -0.54 |       64 | 37.27%     | ok               |

## EOG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -26.42%  | 14.05%             | -38.89% |    -0.63 |       56 | 32.28%     | ok               |
|          30 | -32.39%  | 14.05%             | -47.57% |    -0.72 |       83 | 45.59%     | ok               |
|          40 | -30.54%  | 14.05%             | -41.11% |    -0.74 |       66 | 35.61%     | ok               |
|          35 | -32.38%  | 14.05%             | -44.81% |    -0.77 |       79 | 40.43%     | ok               |
|          25 | -35.82%  | 14.05%             | -51.99% |    -0.79 |       84 | 48.59%     | ok               |

## ETC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -3.34%   | -52.24%            | -27.89% |     0.06 |       24 | 15.33%     | ok               |
|          45 | -5.35%   | -52.24%            | -35.44% |     0.04 |       24 | 17.24%     | ok               |
|          40 | -15.45%  | -52.24%            | -40.48% |    -0.14 |       34 | 20.11%     | ok               |
|          35 | -18.94%  | -52.24%            | -42.62% |    -0.18 |       46 | 24.33%     | ok               |
|          30 | -28.64%  | -52.24%            | -45.54% |    -0.36 |       60 | 28.16%     | ok               |

## ETH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 154.67%  | 50.55%             | -30.11% |     1.34 |       58 | 45.98%     | ok               |
|          30 | 122.59%  | 50.55%             | -32.89% |     1.13 |       62 | 53.45%     | ok               |
|          25 | 81.74%   | 50.55%             | -40.90% |     0.89 |       60 | 57.66%     | ok               |
|          20 | 65.84%   | 50.55%             | -39.10% |     0.78 |       80 | 61.69%     | ok               |
|          40 | 55.54%   | 50.55%             | -33.11% |     0.77 |       62 | 38.12%     | ok               |

## EWJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -24.14%  | 43.97%             | -30.00% |    -0.82 |       58 | 39.27%     | ok               |
|          30 | -23.51%  | 43.97%             | -29.40% |    -0.82 |       64 | 37.10%     | ok               |
|          25 | -26.33%  | 43.97%             | -29.85% |    -0.92 |       58 | 38.27%     | ok               |
|          15 | -28.45%  | 43.97%             | -31.15% |    -0.93 |       71 | 42.76%     | ok               |
|          45 | -24.13%  | 43.97%             | -27.35% |    -0.98 |       62 | 28.95%     | ok               |

## FCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -4.33%   | 44.57%             | -34.75% |     0.07 |       56 | 32.78%     | ok               |
|          50 | -6.62%   | 44.57%             | -27.30% |     0.02 |       56 | 28.79%     | ok               |
|          40 | -16.59%  | 44.57%             | -43.78% |    -0.12 |       66 | 37.44%     | ok               |
|          30 | -30.08%  | 44.57%             | -47.67% |    -0.34 |       65 | 44.43%     | ok               |
|          35 | -34.39%  | 44.57%             | -50.89% |    -0.44 |       71 | 42.60%     | ok               |

## FET-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -24.20%  | -68.49%            | -64.89% |     0.05 |       88 | 51.15%     | ok               |
|          15 | -32.31%  | -68.49%            | -59.58% |    -0.02 |       82 | 55.94%     | ok               |
|          25 | -31.89%  | -68.49%            | -65.31% |    -0.08 |       81 | 44.25%     | ok               |
|          30 | -34.49%  | -68.49%            | -60.12% |    -0.14 |       73 | 39.27%     | ok               |
|          50 | -33.37%  | -68.49%            | -40.07% |    -0.53 |       40 | 11.49%     | ok               |

## FIL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -50.06%  | -67.13%            | -56.67% |    -0.78 |       48 | 22.03%     | ok               |
|          50 | -46.25%  | -67.13%            | -46.77% |    -0.86 |       34 | 12.07%     | ok               |
|          30 | -60.37%  | -67.13%            | -60.56% |    -0.92 |       69 | 32.57%     | ok               |
|          15 | -71.56%  | -67.13%            | -71.70% |    -1.03 |       94 | 45.59%     | ok               |
|          35 | -64.03%  | -67.13%            | -64.21% |    -1.15 |       62 | 26.05%     | ok               |

## FXI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -4.62%   | 38.71%             | -22.57% |    -0.03 |       48 | 33.61%     | ok               |
|          30 | -4.88%   | 38.71%             | -23.91% |    -0.04 |       46 | 32.11%     | ok               |
|          15 | -7.71%   | 38.71%             | -21.68% |    -0.09 |       52 | 37.60%     | ok               |
|          20 | -8.25%   | 38.71%             | -24.53% |    -0.12 |       50 | 35.44%     | ok               |
|          35 | -8.56%   | 38.71%             | -27.53% |    -0.14 |       48 | 29.62%     | ok               |

## GDX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 7.53%    | 184.81%            | -35.59% |     0.25 |       74 | 49.58%     | ok               |
|          40 | 5.29%    | 184.81%            | -31.37% |     0.21 |       62 | 39.27%     | ok               |
|          30 | 2.69%    | 184.81%            | -34.99% |     0.18 |       60 | 45.26%     | ok               |
|          35 | -1.22%   | 184.81%            | -31.88% |     0.11 |       70 | 42.10%     | ok               |
|          25 | -2.76%   | 184.81%            | -38.90% |     0.1  |       64 | 46.42%     | ok               |

## GDXJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -23.78%  | 192.23%            | -44.73% |    -0.18 |       70 | 49.25%     | ok               |
|          50 | -26.72%  | 192.23%            | -46.83% |    -0.35 |       58 | 34.94%     | ok               |
|          30 | -34.03%  | 192.23%            | -44.61% |    -0.42 |       68 | 43.26%     | ok               |
|          35 | -35.74%  | 192.23%            | -41.76% |    -0.47 |       70 | 40.77%     | ok               |
|          25 | -38.44%  | 192.23%            | -46.95% |    -0.48 |       73 | 46.09%     | ok               |

## GE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.24%   | 88.81%             | -22.16% |     0.1  |       64 | 34.61%     | ok               |
|          45 | -8.31%   | 88.81%             | -25.56% |    -0.07 |       76 | 37.27%     | ok               |
|          20 | -10.62%  | 88.81%             | -25.05% |    -0.08 |       77 | 51.91%     | ok               |
|          30 | -13.68%  | 88.81%             | -27.82% |    -0.15 |       80 | 47.75%     | ok               |
|          35 | -14.29%  | 88.81%             | -27.11% |    -0.18 |       82 | 42.60%     | ok               |

## GLD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 14.32%   | 83.29%             | -13.87% |     0.41 |       52 | 46.42%     | ok               |
|          20 | 12.35%   | 83.29%             | -13.87% |     0.36 |       55 | 48.25%     | ok               |
|          30 | 8.88%    | 83.29%             | -14.86% |     0.29 |       54 | 45.26%     | ok               |
|          35 | 6.00%    | 83.29%             | -15.53% |     0.23 |       56 | 42.93%     | ok               |
|          15 | 5.47%    | 83.29%             | -17.54% |     0.21 |       57 | 52.41%     | ok               |

## GOOGL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 64.43%   | 117.98%            | -18.90% |     1.07 |       59 | 44.09%     | ok               |
|          30 | 61.75%   | 117.98%            | -20.41% |     1.02 |       55 | 47.75%     | ok               |
|          45 | 52.73%   | 117.98%            | -14.82% |     0.99 |       52 | 37.60%     | ok               |
|          25 | 59.28%   | 117.98%            | -19.76% |     0.98 |       55 | 50.25%     | ok               |
|          50 | 46.19%   | 117.98%            | -15.58% |     0.92 |       48 | 32.78%     | ok               |

## GRT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 24.13%   | -78.00%            | -25.60% |     0.51 |       38 | 17.62%     | ok               |
|          15 | 1.51%    | -78.00%            | -45.50% |     0.26 |       74 | 61.11%     | ok               |
|          20 | -6.95%   | -78.00%            | -42.04% |     0.17 |       81 | 55.36%     | ok               |
|          25 | -19.59%  | -78.00%            | -51.18% |    -0    |       82 | 50.77%     | ok               |
|          45 | -10.46%  | -78.00%            | -47.52% |    -0.01 |       44 | 23.75%     | ok               |

## GS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 22.06%   | 130.35%            | -20.56% |     0.49 |       66 | 55.57%     | ok               |
|          20 | 3.31%    | 130.35%            | -23.19% |     0.17 |       66 | 52.25%     | ok               |
|          40 | 3.29%    | 130.35%            | -17.88% |     0.16 |       64 | 41.76%     | ok               |
|          25 | -1.92%   | 130.35%            | -23.32% |     0.06 |       66 | 49.75%     | ok               |
|          30 | -3.01%   | 130.35%            | -22.13% |     0.03 |       66 | 47.42%     | ok               |

## HD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -3.88%   | -9.89%             | -18.07% |    -0.02 |       73 | 42.60%     | ok               |
|          25 | -4.63%   | -9.89%             | -18.89% |    -0.04 |       72 | 44.59%     | ok               |
|          35 | -7.84%   | -9.89%             | -19.91% |    -0.15 |       78 | 38.77%     | ok               |
|          45 | -7.58%   | -9.89%             | -16.42% |    -0.19 |       52 | 27.95%     | ok               |
|          40 | -9.44%   | -9.89%             | -18.06% |    -0.23 |       80 | 33.11%     | ok               |

## HON Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -11.31%  | 4.92%              | -23.16% |    -0.28 |       72 | 35.11%     | ok               |
|          45 | -14.22%  | 4.92%              | -25.06% |    -0.35 |       72 | 40.93%     | ok               |
|          30 | -21.68%  | 4.92%              | -33.57% |    -0.5  |       92 | 55.74%     | ok               |
|          35 | -21.30%  | 4.92%              | -31.82% |    -0.52 |       88 | 51.41%     | ok               |
|          40 | -22.95%  | 4.92%              | -33.77% |    -0.59 |       76 | 45.09%     | ok               |

## HYG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -7.43%   | 2.18%              | -8.10%  |    -0.89 |       70 | 30.28%     | ok               |
|          15 | -9.77%   | 2.18%              | -11.48% |    -1.05 |       96 | 43.43%     | ok               |
|          30 | -9.20%   | 2.18%              | -10.59% |    -1.07 |       89 | 35.61%     | ok               |
|          45 | -8.58%   | 2.18%              | -9.24%  |    -1.07 |       70 | 26.96%     | ok               |
|          35 | -8.99%   | 2.18%              | -9.90%  |    -1.07 |       81 | 32.28%     | ok               |

## IBIT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 51.68%   | 13.42%             | -17.37% |     0.96 |       24 | 23.73%     | ok               |
|          15 | 54.82%   | 13.42%             | -19.20% |     0.87 |       42 | 39.62%     | ok               |
|          45 | 42.35%   | 13.42%             | -17.37% |     0.82 |       28 | 25.00%     | ok               |
|          40 | 36.20%   | 13.42%             | -17.78% |     0.73 |       28 | 26.69%     | ok               |
|          30 | 29.08%   | 13.42%             | -18.95% |     0.6  |       36 | 32.63%     | ok               |

## IBM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -20.22%  | 36.32%             | -49.43% |    -0.16 |       91 | 63.06%     | ok               |
|          35 | -24.24%  | 36.32%             | -47.10% |    -0.29 |       69 | 46.59%     | ok               |
|          30 | -25.87%  | 36.32%             | -48.94% |    -0.31 |       73 | 50.75%     | ok               |
|          20 | -30.94%  | 36.32%             | -53.45% |    -0.38 |       73 | 55.41%     | ok               |
|          50 | -29.24%  | 36.32%             | -45.88% |    -0.44 |       46 | 34.44%     | ok               |

## ICP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -7.84%   | -49.73%            | -47.52% |     0.18 |       75 | 36.40%     | ok               |
|          35 | -11.51%  | -49.73%            | -47.24% |     0.07 |       68 | 30.46%     | ok               |
|          40 | -15.60%  | -49.73%            | -40.71% |    -0    |       58 | 25.67%     | ok               |
|          15 | -36.05%  | -49.73%            | -58.26% |    -0.04 |       73 | 48.85%     | ok               |
|          20 | -38.30%  | -49.73%            | -61.47% |    -0.09 |       82 | 45.98%     | ok               |

## IEF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -7.05%   | -1.14%             | -10.18% |    -0.85 |       72 | 41.60%     | ok               |
|          15 | -7.60%   | -1.14%             | -10.91% |    -0.91 |       71 | 43.09%     | ok               |
|          25 | -10.60%  | -1.14%             | -11.68% |    -1.37 |       76 | 38.94%     | ok               |
|          50 | -7.73%   | -1.14%             | -9.11%  |    -1.38 |       54 | 20.13%     | ok               |
|          40 | -9.29%   | -1.14%             | -10.95% |    -1.43 |       64 | 25.12%     | ok               |

## IEMG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.89%   | 57.15%             | -13.87% |     0.02 |       54 | 32.61%     | ok               |
|          45 | -1.70%   | 57.15%             | -14.87% |    -0.01 |       50 | 35.11%     | ok               |
|          35 | -2.63%   | 57.15%             | -22.13% |    -0.03 |       65 | 40.43%     | ok               |
|          40 | -3.22%   | 57.15%             | -18.39% |    -0.06 |       62 | 38.10%     | ok               |
|          25 | -6.92%   | 57.15%             | -25.58% |    -0.17 |       61 | 43.26%     | ok               |

## INJ-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -21.36%  | -32.06%            | -54.35% |    -0.02 |       60 | 33.14%     | ok               |
|          40 | -23.62%  | -32.06%            | -49.77% |    -0.08 |       50 | 30.08%     | ok               |
|          45 | -21.64%  | -32.06%            | -47.58% |    -0.09 |       50 | 24.52%     | ok               |
|          15 | -54.65%  | -32.06%            | -80.00% |    -0.38 |       82 | 49.43%     | ok               |
|          20 | -53.53%  | -32.06%            | -77.07% |    -0.41 |       80 | 46.17%     | ok               |

## INTC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 56.08%   | 183.37%            | -53.65% |     0.61 |       80 | 59.90%     | ok               |
|          45 | 51.38%   | 183.37%            | -49.32% |     0.61 |       60 | 33.11%     | ok               |
|          50 | 50.37%   | 183.37%            | -48.35% |     0.6  |       62 | 28.95%     | ok               |
|          40 | 52.13%   | 183.37%            | -55.86% |     0.6  |       66 | 37.44%     | ok               |
|          25 | 40.44%   | 183.37%            | -56.41% |     0.53 |       79 | 50.75%     | ok               |

## INTU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 1.23%    | -47.81%            | -39.84% |     0.14 |       67 | 27.12%     | ok               |
|          45 | -0.74%   | -47.81%            | -40.88% |     0.11 |       65 | 31.11%     | ok               |
|          40 | -6.98%   | -47.81%            | -44.15% |    -0.01 |       67 | 34.78%     | ok               |
|          25 | -9.57%   | -47.81%            | -39.21% |    -0.02 |       68 | 47.42%     | ok               |
|          15 | -13.56%  | -47.81%            | -43.23% |    -0.08 |       79 | 52.91%     | ok               |

## ITA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 3.41%    | 65.42%             | -21.48% |     0.17 |       72 | 38.44%     | ok               |
|          15 | -1.25%   | 65.42%             | -28.06% |     0.06 |       85 | 60.73%     | ok               |
|          30 | -0.83%   | 65.42%             | -23.75% |     0.05 |       72 | 48.59%     | ok               |
|          35 | -2.90%   | 65.42%             | -23.16% |    -0.01 |       74 | 46.26%     | ok               |
|          40 | -3.08%   | 65.42%             | -20.58% |    -0.02 |       74 | 42.93%     | ok               |

## IWM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 12.90%   | 43.60%             | -13.94% |     0.55 |       48 | 32.11%     | ok               |
|          25 | 12.85%   | 43.60%             | -12.34% |     0.5  |       54 | 37.27%     | ok               |
|          35 | 11.49%   | 43.60%             | -13.94% |     0.47 |       52 | 34.44%     | ok               |
|          30 | 11.41%   | 43.60%             | -12.65% |     0.46 |       54 | 36.44%     | ok               |
|          20 | 11.36%   | 43.60%             | -12.12% |     0.44 |       60 | 38.27%     | ok               |

## JNJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 16.00%   | 78.66%             | -10.57% |     0.67 |       48 | 34.78%     | ok               |
|          15 | 10.31%   | 78.66%             | -18.02% |     0.38 |       64 | 54.74%     | ok               |
|          45 | 5.14%    | 78.66%             | -13.35% |     0.25 |       50 | 38.77%     | ok               |
|          20 | 5.21%    | 78.66%             | -17.61% |     0.23 |       70 | 51.25%     | ok               |
|          40 | 1.61%    | 78.66%             | -14.77% |     0.12 |       58 | 43.09%     | ok               |

## JPM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 6.98%    | 83.45%             | -15.90% |     0.29 |       52 | 35.27%     | ok               |
|          45 | -3.18%   | 83.45%             | -21.91% |    -0.03 |       54 | 38.27%     | ok               |
|          20 | -18.31%  | 83.45%             | -35.58% |    -0.37 |       82 | 52.25%     | ok               |
|          35 | -15.95%  | 83.45%             | -27.43% |    -0.42 |       74 | 44.59%     | ok               |
|          40 | -16.47%  | 83.45%             | -28.47% |    -0.44 |       66 | 40.93%     | ok               |

## KO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 28.06%   | 46.29%             | -8.64%  |     0.96 |       54 | 40.27%     | ok               |
|          35 | 23.71%   | 46.29%             | -8.21%  |     0.85 |       58 | 38.77%     | ok               |
|          40 | 20.73%   | 46.29%             | -9.28%  |     0.8  |       60 | 35.44%     | ok               |
|          25 | 21.65%   | 46.29%             | -10.16% |     0.77 |       60 | 43.09%     | ok               |
|          20 | 8.22%    | 46.29%             | -15.99% |     0.33 |       77 | 47.25%     | ok               |

## LDO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 37.85%   | -53.06%            | -48.17% |     0.56 |       78 | 59.96%     | ok               |
|          20 | 27.11%   | -53.06%            | -48.55% |     0.49 |       82 | 55.36%     | ok               |
|          30 | -0.29%   | -53.06%            | -63.49% |     0.28 |       74 | 46.55%     | ok               |
|          25 | -4.37%   | -53.06%            | -59.45% |     0.26 |       83 | 52.30%     | ok               |
|          35 | -12.27%  | -53.06%            | -64.26% |     0.13 |       78 | 38.31%     | ok               |

## LIN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -6.82%   | 4.02%              | -23.68% |    -0.17 |       70 | 46.09%     | ok               |
|          20 | -6.99%   | 4.02%              | -23.00% |    -0.18 |       64 | 41.93%     | ok               |
|          25 | -6.94%   | 4.02%              | -22.01% |    -0.19 |       67 | 39.10%     | ok               |
|          30 | -10.87%  | 4.02%              | -20.61% |    -0.35 |       70 | 36.27%     | ok               |
|          45 | -10.54%  | 4.02%              | -17.04% |    -0.42 |       42 | 20.47%     | ok               |

## LINK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 43.06%   | -14.15%            | -33.64% |     0.6  |       72 | 45.79%     | ok               |
|          45 | 36.13%   | -14.15%            | -33.71% |     0.57 |       52 | 30.65%     | ok               |
|          35 | 22.51%   | -14.15%            | -34.21% |     0.44 |       60 | 40.42%     | ok               |
|          40 | 15.79%   | -14.15%            | -34.00% |     0.38 |       56 | 34.67%     | ok               |
|          50 | 14.59%   | -14.15%            | -27.44% |     0.36 |       44 | 24.52%     | ok               |

## LLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 2.05%    | 52.36%             | -38.23% |     0.15 |       46 | 35.44%     | ok               |
|          15 | -8.43%   | 52.36%             | -48.12% |     0.01 |       65 | 58.74%     | ok               |
|          45 | -9.72%   | 52.36%             | -42.66% |    -0.08 |       52 | 38.77%     | ok               |
|          20 | -20.97%  | 52.36%             | -51.34% |    -0.23 |       72 | 53.91%     | ok               |
|          25 | -22.28%  | 52.36%             | -53.47% |    -0.27 |       68 | 51.25%     | ok               |

## LRCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -13.68%  | 205.23%            | -48.71% |    -0.02 |       76 | 33.61%     | ok               |
|          40 | -18.39%  | 205.23%            | -55.33% |    -0.06 |       72 | 39.60%     | ok               |
|          35 | -19.96%  | 205.23%            | -58.47% |    -0.08 |       80 | 41.76%     | ok               |
|          15 | -28.92%  | 205.23%            | -56.69% |    -0.14 |       85 | 51.91%     | ok               |
|          30 | -25.21%  | 205.23%            | -61.08% |    -0.15 |       84 | 42.43%     | ok               |

## LTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -1.14%   | -34.14%            | -34.94% |     0.16 |       68 | 44.06%     | ok               |
|          45 | -2.72%   | -34.14%            | -37.29% |     0.12 |       58 | 32.95%     | ok               |
|          30 | -8.16%   | -34.14%            | -33.94% |     0.08 |       70 | 51.72%     | ok               |
|          25 | -14.72%  | -34.14%            | -34.22% |    -0.01 |       74 | 54.41%     | ok               |
|          40 | -12.48%  | -34.14%            | -40.31% |    -0.02 |       56 | 38.51%     | ok               |

## MCD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 4.02%    | -8.70%             | -9.22%  |     0.24 |       46 | 22.30%     | ok               |
|          45 | -4.71%   | -8.70%             | -16.79% |    -0.18 |       52 | 26.12%     | ok               |
|          30 | -6.44%   | -8.70%             | -21.88% |    -0.21 |       77 | 37.44%     | ok               |
|          40 | -5.98%   | -8.70%             | -18.49% |    -0.23 |       67 | 29.45%     | ok               |
|          25 | -7.44%   | -8.70%             | -23.62% |    -0.24 |       77 | 40.10%     | ok               |

## META Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -18.41%  | 35.10%             | -37.54% |    -0.28 |       70 | 37.10%     | ok               |
|          40 | -23.69%  | 35.10%             | -40.90% |    -0.38 |       72 | 40.60%     | ok               |
|          50 | -27.50%  | 35.10%             | -39.33% |    -0.53 |       72 | 32.95%     | ok               |
|          25 | -33.85%  | 35.10%             | -45.70% |    -0.57 |       77 | 51.08%     | ok               |
|          30 | -33.87%  | 35.10%             | -44.90% |    -0.59 |       80 | 48.09%     | ok               |

## MPC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 42.48%   | 105.78%            | -18.24% |     0.78 |       48 | 39.10%     | ok               |
|          45 | 33.45%   | 105.78%            | -19.46% |     0.65 |       54 | 42.76%     | ok               |
|          40 | 28.41%   | 105.78%            | -20.11% |     0.57 |       56 | 44.93%     | ok               |
|          35 | 24.44%   | 105.78%            | -31.08% |     0.5  |       64 | 47.42%     | ok               |
|          30 | 9.62%    | 105.78%            | -37.91% |     0.28 |       67 | 49.92%     | ok               |

## MRK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -12.18%  | 13.33%             | -28.87% |    -0.14 |       83 | 53.74%     | ok               |
|          25 | -11.64%  | 13.33%             | -31.07% |    -0.14 |       70 | 46.09%     | ok               |
|          20 | -15.97%  | 13.33%             | -29.34% |    -0.24 |       75 | 49.42%     | ok               |
|          50 | -15.53%  | 13.33%             | -24.92% |    -0.32 |       58 | 30.45%     | ok               |
|          45 | -17.63%  | 13.33%             | -25.38% |    -0.36 |       59 | 33.78%     | ok               |

## MS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -0.91%   | 120.01%            | -19.99% |     0.06 |       70 | 39.27%     | ok               |
|          15 | -6.91%   | 120.01%            | -22.02% |    -0.06 |       74 | 56.57%     | ok               |
|          20 | -7.13%   | 120.01%            | -25.68% |    -0.08 |       77 | 52.58%     | ok               |
|          30 | -11.95%  | 120.01%            | -27.79% |    -0.22 |       77 | 47.75%     | ok               |
|          35 | -11.88%  | 120.01%            | -26.58% |    -0.23 |       78 | 44.26%     | ok               |

## MSFT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -13.16%  | 21.97%             | -24.64% |    -0.29 |       66 | 35.94%     | ok               |
|          50 | -19.58%  | 21.97%             | -25.48% |    -0.51 |       60 | 30.62%     | ok               |
|          35 | -26.29%  | 21.97%             | -35.51% |    -0.61 |       69 | 45.09%     | ok               |
|          40 | -26.32%  | 21.97%             | -34.92% |    -0.64 |       67 | 39.77%     | ok               |
|          30 | -29.20%  | 21.97%             | -38.06% |    -0.67 |       79 | 49.42%     | ok               |

## MU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 200.69%  | 724.83%            | -64.07% |     1.21 |       54 | 49.25%     | ok               |
|          15 | 239.12%  | 724.83%            | -61.96% |     1.2  |       49 | 61.90%     | ok               |
|          25 | 175.56%  | 724.83%            | -67.90% |     1.1  |       49 | 55.57%     | ok               |
|          30 | 164.65%  | 724.83%            | -68.76% |     1.08 |       49 | 53.91%     | ok               |
|          35 | 158.86%  | 724.83%            | -69.15% |     1.07 |       61 | 51.75%     | ok               |

## NEAR-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 63.15%   | 12.13%             | -52.22% |     0.75 |       40 | 30.27%     | ok               |
|          45 | 61.96%   | 12.13%             | -43.08% |     0.74 |       40 | 26.25%     | ok               |
|          50 | 39.14%   | 12.13%             | -48.72% |     0.59 |       32 | 21.26%     | ok               |
|          35 | 24.28%   | 12.13%             | -59.02% |     0.46 |       58 | 34.29%     | ok               |
|          30 | 4.36%    | 12.13%             | -60.10% |     0.29 |       73 | 42.34%     | ok               |

## NEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 21.29%   | 229.33%            | -31.25% |     0.41 |       56 | 60.73%     | ok               |
|          20 | 14.99%   | 229.33%            | -30.50% |     0.34 |       64 | 56.57%     | ok               |
|          25 | -3.41%   | 229.33%            | -39.51% |     0.12 |       62 | 54.74%     | ok               |
|          30 | -15.52%  | 229.33%            | -39.56% |    -0.06 |       66 | 53.08%     | ok               |
|          50 | -16.52%  | 229.33%            | -33.24% |    -0.12 |       56 | 40.93%     | ok               |

## NFLX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 41.22%   | 34.83%             | -13.37% |     0.91 |       48 | 42.43%     | ok               |
|          50 | 37.08%   | 34.83%             | -16.28% |     0.89 |       44 | 34.78%     | ok               |
|          35 | 41.25%   | 34.83%             | -18.30% |     0.86 |       70 | 46.92%     | ok               |
|          45 | 25.95%   | 34.83%             | -15.48% |     0.65 |       54 | 38.94%     | ok               |
|          15 | 17.50%   | 34.83%             | -26.59% |     0.41 |       71 | 65.39%     | ok               |

## NKE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -16.43%  | -61.48%            | -42.13% |    -0.16 |       69 | 38.10%     | ok               |
|          20 | -21.01%  | -61.48%            | -49.34% |    -0.18 |       83 | 50.42%     | ok               |
|          25 | -24.28%  | -61.48%            | -51.20% |    -0.24 |       83 | 47.75%     | ok               |
|          15 | -26.10%  | -61.48%            | -54.28% |    -0.26 |       86 | 54.24%     | ok               |
|          40 | -18.11%  | -61.48%            | -31.79% |    -0.29 |       63 | 30.12%     | ok               |

## NOW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 11.46%   | -4.24%             | -30.43% |     0.3  |       86 | 50.08%     | ok               |
|          20 | 10.00%   | -4.24%             | -39.71% |     0.29 |       81 | 56.57%     | ok               |
|          25 | 6.21%    | -4.24%             | -37.51% |     0.25 |       78 | 53.58%     | ok               |
|          15 | 1.96%    | -4.24%             | -43.06% |     0.21 |       89 | 59.57%     | ok               |
|          40 | 2.59%    | -4.24%             | -36.21% |     0.19 |       78 | 39.60%     | ok               |

## NVDA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -40.70%  | 62.23%             | -45.26% |    -0.51 |       76 | 54.19%     | ok               |
|          30 | -35.98%  | 62.23%             | -41.21% |    -0.52 |       78 | 45.99%     | ok               |
|          25 | -40.61%  | 62.23%             | -45.17% |    -0.56 |       77 | 49.20%     | ok               |
|          15 | -47.12%  | 62.23%             | -52.37% |    -0.61 |       77 | 57.40%     | ok               |
|          35 | -46.38%  | 62.23%             | -48.32% |    -0.81 |       88 | 42.96%     | ok               |

## OP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 28.55%   | -85.98%            | -31.68% |     0.55 |       30 | 9.39%      | ok               |
|          45 | -8.14%   | -85.98%            | -51.17% |     0.06 |       34 | 13.98%     | ok               |
|          40 | -20.87%  | -85.98%            | -60.08% |    -0.09 |       48 | 22.03%     | ok               |
|          30 | -41.65%  | -85.98%            | -68.74% |    -0.33 |       70 | 33.14%     | ok               |
|          35 | -40.09%  | -85.98%            | -63.95% |    -0.38 |       56 | 27.01%     | ok               |

## ORCL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 169.65%  | 21.95%             | -32.54% |     1.12 |       73 | 64.23%     | ok               |
|          25 | 121.41%  | 21.95%             | -27.76% |     0.96 |       63 | 56.57%     | ok               |
|          45 | 102.05%  | 21.95%             | -32.35% |     0.93 |       60 | 41.10%     | ok               |
|          20 | 115.23%  | 21.95%             | -29.32% |     0.93 |       72 | 59.73%     | ok               |
|          35 | 102.78%  | 21.95%             | -31.95% |     0.9  |       68 | 50.42%     | ok               |

## OXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -2.82%   | -5.74%             | -26.54% |     0.06 |       74 | 38.94%     | ok               |
|          30 | -5.65%   | -5.74%             | -31.20% |     0.03 |       73 | 44.09%     | ok               |
|          50 | -5.03%   | -5.74%             | -27.00% |     0    |       48 | 27.12%     | ok               |
|          40 | -8.27%   | -5.74%             | -28.30% |    -0.05 |       64 | 34.28%     | ok               |
|          45 | -16.24%  | -5.74%             | -32.45% |    -0.24 |       54 | 29.45%     | ok               |

## PEP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 13.77%   | -20.86%            | -11.62% |     0.62 |       36 | 25.62%     | ok               |
|          45 | 6.50%    | -20.86%            | -14.22% |     0.32 |       52 | 29.62%     | ok               |
|          35 | 1.51%    | -20.86%            | -21.42% |     0.11 |       73 | 39.77%     | ok               |
|          40 | -0.67%   | -20.86%            | -18.04% |     0.03 |       66 | 35.11%     | ok               |
|          30 | -3.96%   | -20.86%            | -21.35% |    -0.05 |       74 | 45.76%     | ok               |

## PEPE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -43.08%  | -53.17%            | -64.84% |    -0.08 |       82 | 62.84%     | ok               |
|          30 | -39.87%  | -53.17%            | -57.66% |    -0.17 |       89 | 47.70%     | ok               |
|          25 | -41.37%  | -53.17%            | -53.88% |    -0.17 |       93 | 53.64%     | ok               |
|          35 | -38.97%  | -53.17%            | -54.42% |    -0.22 |       72 | 41.76%     | ok               |
|          20 | -48.68%  | -53.17%            | -64.07% |    -0.23 |       88 | 59.39%     | ok               |

## PFE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -17.03%  | 4.67%              | -23.37% |    -0.54 |       56 | 22.30%     | ok               |
|          50 | -17.66%  | 4.67%              | -26.41% |    -0.62 |       42 | 18.80%     | ok               |
|          40 | -23.53%  | 4.67%              | -30.50% |    -0.73 |       76 | 27.45%     | ok               |
|          35 | -26.98%  | 4.67%              | -35.77% |    -0.79 |       88 | 34.94%     | ok               |
|          30 | -35.79%  | 4.67%              | -43.50% |    -1.05 |       83 | 39.60%     | ok               |

## PG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -10.55%  | -9.18%             | -19.77% |    -0.41 |       54 | 30.45%     | ok               |
|          35 | -13.60%  | -9.18%             | -18.66% |    -0.53 |       62 | 33.94%     | ok               |
|          30 | -21.45%  | -9.18%             | -24.25% |    -0.84 |       64 | 37.10%     | ok               |
|          45 | -19.29%  | -9.18%             | -22.13% |    -0.87 |       54 | 27.95%     | ok               |
|          25 | -23.24%  | -9.18%             | -25.94% |    -0.92 |       76 | 38.60%     | ok               |

## PM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -2.24%   | 98.76%             | -32.20% |     0.04 |       84 | 50.08%     | ok               |
|          20 | -4.80%   | 98.76%             | -33.51% |    -0.01 |       83 | 58.74%     | ok               |
|          30 | -5.31%   | 98.76%             | -35.15% |    -0.03 |       79 | 53.58%     | ok               |
|          40 | -9.71%   | 98.76%             | -37.94% |    -0.16 |       78 | 46.09%     | ok               |
|          50 | -9.23%   | 98.76%             | -35.70% |    -0.16 |       68 | 40.27%     | ok               |

## POL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 16.20%   | -49.37%            | -45.67% |     0.38 |       85 | 49.23%     | ok               |
|          25 | 8.13%    | -49.37%            | -46.72% |     0.31 |       72 | 55.94%     | ok               |
|          20 | -7.73%   | -49.37%            | -52.88% |     0.16 |       80 | 60.15%     | ok               |
|          50 | -2.90%   | -49.37%            | -26.14% |     0.1  |       46 | 19.54%     | ok               |
|          40 | -10.63%  | -49.37%            | -40.38% |     0.04 |       54 | 30.08%     | ok               |

## QCOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 2.78%    | 16.39%             | -54.50% |     0.21 |       71 | 44.93%     | ok               |
|          35 | -4.96%   | 16.39%             | -50.58% |     0.1  |       77 | 40.60%     | ok               |
|          20 | -6.27%   | 16.39%             | -54.38% |     0.1  |       69 | 48.09%     | ok               |
|          30 | -15.16%  | 16.39%             | -56.59% |    -0.04 |       75 | 42.93%     | ok               |
|          15 | -18.81%  | 16.39%             | -57.94% |    -0.07 |       73 | 50.92%     | ok               |

## QQQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 27.72%   | 65.75%             | -14.17% |     0.67 |       65 | 54.58%     | ok               |
|          25 | 19.05%   | 65.75%             | -12.88% |     0.53 |       63 | 48.59%     | ok               |
|          20 | 17.83%   | 65.75%             | -12.98% |     0.49 |       71 | 51.25%     | ok               |
|          30 | 13.22%   | 65.75%             | -14.20% |     0.41 |       66 | 46.42%     | ok               |
|          35 | 1.58%    | 65.75%             | -20.59% |     0.12 |       72 | 42.60%     | ok               |

## RENDER-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 20.46%   | -65.27%            | -44.59% |     0.45 |       86 | 61.11%     | ok               |
|          20 | 19.57%   | -65.27%            | -43.43% |     0.44 |       91 | 57.47%     | ok               |
|          25 | 6.03%    | -65.27%            | -40.60% |     0.33 |       91 | 52.49%     | ok               |
|          30 | -40.65%  | -65.27%            | -46.98% |    -0.21 |      100 | 45.59%     | ok               |
|          35 | -36.81%  | -65.27%            | -47.98% |    -0.22 |       82 | 37.74%     | ok               |

## RTX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 42.69%   | 92.84%             | -18.66% |     0.89 |       74 | 57.24%     | ok               |
|          25 | 37.81%   | 92.84%             | -18.59% |     0.82 |       62 | 54.58%     | ok               |
|          30 | 33.40%   | 92.84%             | -16.99% |     0.75 |       58 | 52.91%     | ok               |
|          15 | 34.90%   | 92.84%             | -19.55% |     0.75 |       69 | 62.06%     | ok               |
|          35 | 27.39%   | 92.84%             | -18.00% |     0.7  |       52 | 50.08%     | ok               |

## SBUX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -5.04%   | 9.91%              | -23.55% |    -0.01 |       55 | 39.93%     | ok               |
|          40 | -10.28%  | 9.91%              | -25.43% |    -0.16 |       60 | 32.45%     | ok               |
|          45 | -10.72%  | 9.91%              | -27.26% |    -0.2  |       62 | 28.79%     | ok               |
|          30 | -14.93%  | 9.91%              | -29.22% |    -0.25 |       58 | 37.77%     | ok               |
|          35 | -16.40%  | 9.91%              | -27.15% |    -0.3  |       58 | 35.61%     | ok               |

## SCHW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -1.47%   | 43.28%             | -16.53% |     0.03 |       62 | 33.61%     | ok               |
|          25 | -3.61%   | 43.28%             | -28.76% |     0.01 |       65 | 49.92%     | ok               |
|          20 | -7.07%   | 43.28%             | -29.24% |    -0.07 |       73 | 52.41%     | ok               |
|          50 | -7.09%   | 43.28%             | -13.28% |    -0.19 |       58 | 30.62%     | ok               |
|          40 | -10.75%  | 43.28%             | -23.35% |    -0.23 |       68 | 37.10%     | ok               |

## SHIB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -33.46%  | -59.11%            | -40.35% |    -0.23 |       79 | 60.15%     | ok               |
|          15 | -35.94%  | -59.11%            | -45.04% |    -0.25 |       87 | 68.58%     | ok               |
|          20 | -38.83%  | -59.11%            | -43.97% |    -0.31 |       81 | 63.60%     | ok               |
|          35 | -35.00%  | -59.11%            | -48.18% |    -0.33 |       74 | 45.59%     | ok               |
|          30 | -41.62%  | -59.11%            | -45.01% |    -0.43 |       84 | 52.30%     | ok               |

## SHY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          30 | -2.10%   | 0.04%              | -3.30% |    -0.72 |       48 | 34.61%     | ok               |
|          45 | -2.35%   | 0.04%              | -3.43% |    -0.88 |       50 | 26.79%     | ok               |
|          35 | -2.63%   | 0.04%              | -3.61% |    -0.93 |       52 | 32.95%     | ok               |
|          40 | -2.65%   | 0.04%              | -3.58% |    -0.94 |       54 | 31.61%     | ok               |
|          50 | -2.52%   | 0.04%              | -3.40% |    -0.99 |       46 | 23.29%     | ok               |

## SKY-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -35.73%  | 5.17%              | -48.30% |    -0.41 |       82 | 45.35%     | ok               |
|          15 | -42.53%  | 5.17%              | -56.39% |    -0.46 |       68 | 54.65%     | ok               |
|          25 | -42.79%  | 5.17%              | -53.98% |    -0.54 |       75 | 48.84%     | ok               |
|          35 | -41.26%  | 5.17%              | -49.68% |    -0.61 |       76 | 37.79%     | ok               |
|          20 | -50.77%  | 5.17%              | -61.80% |    -0.67 |       70 | 52.13%     | ok               |

## SLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 15.52%   | 9.38%              | -22.99% |     0.4  |       58 | 33.94%     | ok               |
|          40 | 13.89%   | 9.38%              | -25.51% |     0.36 |       50 | 37.60%     | ok               |
|          50 | -1.90%   | 9.38%              | -29.84% |     0.05 |       52 | 29.62%     | ok               |
|          35 | -16.08%  | 9.38%              | -44.39% |    -0.22 |       72 | 44.26%     | ok               |
|          30 | -36.39%  | 9.38%              | -56.91% |    -0.68 |       77 | 50.42%     | ok               |

## SLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 43.81%   | 130.21%            | -34.10% |     0.66 |       56 | 30.95%     | ok               |
|          45 | 32.52%   | 130.21%            | -31.82% |     0.54 |       65 | 32.61%     | ok               |
|          40 | 30.94%   | 130.21%            | -34.28% |     0.53 |       71 | 34.78%     | ok               |
|          15 | 20.65%   | 130.21%            | -47.98% |     0.41 |       75 | 51.25%     | ok               |
|          20 | 19.82%   | 130.21%            | -42.66% |     0.4  |       74 | 45.92%     | ok               |

## SMH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 86.99%   | 160.88%            | -31.66% |     1.13 |       49 | 47.92%     | ok               |
|          35 | 70.33%   | 160.88%            | -34.65% |     1.02 |       54 | 43.26%     | ok               |
|          25 | 69.26%   | 160.88%            | -33.57% |     1    |       46 | 46.59%     | ok               |
|          30 | 67.47%   | 160.88%            | -34.29% |     0.99 |       48 | 44.93%     | ok               |
|          45 | 55.28%   | 160.88%            | -33.35% |     0.93 |       54 | 37.44%     | ok               |

## SNX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -7.45%   | -68.58%            | -37.62% |     0.12 |       56 | 26.44%     | ok               |
|          20 | -14.67%  | -68.58%            | -47.56% |     0.09 |       71 | 43.49%     | ok               |
|          40 | -11.21%  | -68.58%            | -36.94% |     0.01 |       46 | 21.65%     | ok               |
|          30 | -19.67%  | -68.58%            | -47.16% |    -0.02 |       62 | 33.14%     | ok               |
|          15 | -40.46%  | -68.58%            | -49.47% |    -0.23 |       81 | 48.47%     | ok               |

## SOL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 38.63%   | -24.12%            | -38.17% |     0.6  |       54 | 37.93%     | ok               |
|          35 | 15.52%   | -24.12%            | -43.70% |     0.38 |       66 | 44.44%     | ok               |
|          45 | 8.98%    | -24.12%            | -46.83% |     0.3  |       56 | 32.57%     | ok               |
|          25 | -5.28%   | -24.12%            | -41.09% |     0.17 |       70 | 57.47%     | ok               |
|          50 | -1.68%   | -24.12%            | -46.56% |     0.15 |       58 | 26.63%     | ok               |

## SOXX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 74.69%   | 142.31%            | -39.65% |     0.99 |       56 | 45.76%     | ok               |
|          35 | 70.38%   | 142.31%            | -38.76% |     0.97 |       58 | 40.93%     | ok               |
|          30 | 68.55%   | 142.31%            | -40.14% |     0.94 |       58 | 43.43%     | ok               |
|          20 | 61.49%   | 142.31%            | -38.67% |     0.86 |       61 | 46.59%     | ok               |
|          40 | 48.85%   | 142.31%            | -41.03% |     0.78 |       58 | 38.77%     | ok               |

## SPY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 13.55%   | 49.79%             | -14.25% |     0.49 |       61 | 55.57%     | ok               |
|          15 | 13.00%   | 49.79%             | -16.80% |     0.46 |       65 | 58.24%     | ok               |
|          25 | 8.06%    | 49.79%             | -14.25% |     0.33 |       61 | 54.41%     | ok               |
|          30 | 3.49%    | 49.79%             | -15.53% |     0.18 |       64 | 51.58%     | ok               |
|          35 | 2.49%    | 49.79%             | -15.58% |     0.15 |       62 | 48.42%     | ok               |

## SUSHI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -14.68%  | -62.71%            | -34.75% |    -0.07 |       54 | 14.56%     | ok               |
|          45 | -64.10%  | -62.71%            | -64.10% |    -0.99 |       58 | 18.97%     | ok               |
|          40 | -66.84%  | -62.71%            | -66.53% |    -1    |       63 | 25.29%     | ok               |
|          35 | -74.64%  | -62.71%            | -74.40% |    -1.18 |       86 | 30.65%     | ok               |
|          15 | -82.41%  | -62.71%            | -83.03% |    -1.19 |       90 | 48.85%     | ok               |

## T Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 74.47%   | 61.94%             | -15.08% |     1.26 |       71 | 67.05%     | ok               |
|          20 | 70.17%   | 61.94%             | -18.13% |     1.25 |       66 | 62.56%     | ok               |
|          25 | 65.56%   | 61.94%             | -17.66% |     1.2  |       66 | 60.23%     | ok               |
|          30 | 47.42%   | 61.94%             | -17.01% |     0.97 |       70 | 58.24%     | ok               |
|          35 | 31.35%   | 61.94%             | -14.49% |     0.74 |       76 | 53.91%     | ok               |

## TGT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -11.96%  | -7.27%             | -35.83% |    -0.19 |       58 | 37.60%     | ok               |
|          25 | -13.01%  | -7.27%             | -39.14% |    -0.19 |       64 | 40.27%     | ok               |
|          20 | -15.49%  | -7.27%             | -40.95% |    -0.22 |       84 | 45.09%     | ok               |
|          45 | -13.22%  | -7.27%             | -26.91% |    -0.26 |       50 | 28.79%     | ok               |
|          35 | -17.70%  | -7.27%             | -33.32% |    -0.36 |       60 | 33.94%     | ok               |

## TIA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -45.89%  | -86.36%            | -63.05% |    -0.15 |       94 | 58.43%     | ok               |
|          35 | -35.23%  | -86.36%            | -60.24% |    -0.19 |       68 | 35.25%     | ok               |
|          45 | -35.89%  | -86.36%            | -58.20% |    -0.38 |       58 | 19.54%     | ok               |
|          40 | -45.33%  | -86.36%            | -62.54% |    -0.4  |       74 | 29.31%     | ok               |
|          20 | -60.63%  | -86.36%            | -64.15% |    -0.45 |       90 | 52.87%     | ok               |

## TLT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -19.18%  | -9.35%             | -22.03% |    -1.4  |       74 | 34.28%     | ok               |
|          50 | -13.43%  | -9.35%             | -14.46% |    -1.55 |       36 | 15.81%     | ok               |
|          40 | -17.68%  | -9.35%             | -18.31% |    -1.58 |       56 | 24.29%     | ok               |
|          15 | -24.88%  | -9.35%             | -27.91% |    -1.67 |       81 | 42.43%     | ok               |
|          35 | -20.97%  | -9.35%             | -22.12% |    -1.75 |       68 | 28.45%     | ok               |

## TMO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 48.61%   | 11.63%             | -8.17%  |     1.06 |       44 | 33.61%     | ok               |
|          45 | 42.82%   | 11.63%             | -9.69%  |     0.92 |       48 | 38.44%     | ok               |
|          40 | 38.64%   | 11.63%             | -9.91%  |     0.83 |       53 | 43.26%     | ok               |
|          35 | 33.32%   | 11.63%             | -13.84% |     0.7  |       65 | 48.59%     | ok               |
|          20 | 27.03%   | 11.63%             | -22.89% |     0.56 |       76 | 60.07%     | ok               |

## TMUS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 2.41%    | 10.55%             | -27.06% |     0.15 |       76 | 48.25%     | ok               |
|          15 | -1.02%   | 10.55%             | -34.48% |     0.08 |       68 | 60.90%     | ok               |
|          25 | -5.27%   | 10.55%             | -32.65% |    -0.01 |       79 | 51.08%     | ok               |
|          20 | -6.73%   | 10.55%             | -33.09% |    -0.04 |       74 | 55.24%     | ok               |
|          50 | -6.53%   | 10.55%             | -29.49% |    -0.11 |       60 | 34.94%     | ok               |

## TRX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 19.40%   | 31.25%             | -18.79% |     0.62 |       54 | 40.42%     | ok               |
|          35 | 12.97%   | 31.25%             | -21.77% |     0.43 |       68 | 49.23%     | ok               |
|          20 | 12.33%   | 31.25%             | -25.45% |     0.39 |       61 | 59.39%     | ok               |
|          30 | 10.93%   | 31.25%             | -22.90% |     0.38 |       68 | 52.30%     | ok               |
|          25 | 8.24%    | 31.25%             | -26.84% |     0.3  |       66 | 55.94%     | ok               |

## TSLA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 41.91%   | 146.46%            | -30.57% |     0.61 |       62 | 29.78%     | ok               |
|          40 | 14.07%   | 146.46%            | -50.11% |     0.34 |       61 | 35.27%     | ok               |
|          45 | -10.25%  | 146.46%            | -52.01% |     0.07 |       67 | 32.28%     | ok               |
|          35 | -17.74%  | 146.46%            | -58.86% |     0    |       72 | 37.94%     | ok               |
|          30 | -35.03%  | 146.46%            | -58.36% |    -0.22 |       80 | 43.09%     | ok               |

## TXN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 12.55%   | 59.20%             | -45.45% |     0.32 |       62 | 32.28%     | ok               |
|          35 | -6.23%   | 59.20%             | -43.38% |     0.03 |       70 | 46.42%     | ok               |
|          40 | -8.21%   | 59.20%             | -45.67% |    -0    |       68 | 44.43%     | ok               |
|          20 | -13.52%  | 59.20%             | -38.98% |    -0.04 |       66 | 56.24%     | ok               |
|          45 | -11.69%  | 59.20%             | -46.24% |    -0.07 |       76 | 38.60%     | ok               |

## UNH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 35.31%   | -22.68%            | -26.31% |     0.58 |       72 | 50.08%     | ok               |
|          50 | 28.37%   | -22.68%            | -36.71% |     0.53 |       52 | 29.28%     | ok               |
|          35 | 28.38%   | -22.68%            | -27.21% |     0.51 |       66 | 44.76%     | ok               |
|          15 | 24.85%   | -22.68%            | -29.48% |     0.45 |       79 | 65.56%     | ok               |
|          20 | 22.57%   | -22.68%            | -30.79% |     0.43 |       76 | 59.23%     | ok               |

## UNI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 25.73%   | 20.52%             | -45.09% |     0.48 |       50 | 24.14%     | ok               |
|          45 | 2.26%    | 20.52%             | -51.70% |     0.26 |       58 | 31.80%     | ok               |
|          40 | -9.94%   | 20.52%             | -61.16% |     0.13 |       64 | 36.40%     | ok               |
|          35 | -22.87%  | 20.52%             | -65.47% |     0.01 |       76 | 42.34%     | ok               |
|          20 | -63.87%  | 20.52%             | -80.78% |    -0.51 |       97 | 58.24%     | ok               |

## UPS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -29.07%  | -31.25%            | -31.52% |    -0.55 |       62 | 34.28%     | ok               |
|          40 | -29.19%  | -31.25%            | -31.37% |    -0.57 |       58 | 28.95%     | ok               |
|          20 | -33.88%  | -31.25%            | -37.54% |    -0.63 |       84 | 47.42%     | ok               |
|          25 | -34.41%  | -31.25%            | -37.83% |    -0.66 |       76 | 44.09%     | ok               |
|          15 | -36.22%  | -31.25%            | -39.55% |    -0.68 |       86 | 51.25%     | ok               |

## USO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 23.29%   | 102.38%            | -32.35% |     0.46 |       46 | 25.46%     | ok               |
|          20 | 20.74%   | 102.38%            | -45.20% |     0.41 |       76 | 38.27%     | ok               |
|          25 | 15.98%   | 102.38%            | -44.90% |     0.36 |       70 | 35.44%     | ok               |
|          30 | 14.81%   | 102.38%            | -41.71% |     0.35 |       70 | 32.45%     | ok               |
|          15 | 15.04%   | 102.38%            | -44.86% |     0.34 |       75 | 41.43%     | ok               |

## VEA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 5.04%    | 46.37%             | -15.99% |     0.24 |       56 | 49.75%     | ok               |
|          20 | -1.07%   | 46.37%             | -17.70% |     0.01 |       61 | 47.09%     | ok               |
|          25 | -6.01%   | 46.37%             | -19.39% |    -0.19 |       59 | 45.09%     | ok               |
|          30 | -6.17%   | 46.37%             | -19.52% |    -0.21 |       60 | 42.93%     | ok               |
|          35 | -7.21%   | 46.37%             | -18.40% |    -0.26 |       58 | 41.93%     | ok               |

## VIXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -55.17%  | -67.82%            | -69.78% |    -0.63 |       40 | 10.82%     | ok               |
|          15 | -75.65%  | -67.82%            | -89.47% |    -0.75 |       97 | 45.42%     | ok               |
|          45 | -64.78%  | -67.82%            | -75.03% |    -0.84 |       60 | 15.81%     | ok               |
|          30 | -77.12%  | -67.82%            | -88.17% |    -0.9  |       98 | 34.28%     | ok               |
|          20 | -80.53%  | -67.82%            | -90.58% |    -0.93 |       93 | 41.43%     | ok               |

## VNQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -9.92%   | 17.00%             | -19.07% |    -0.44 |       60 | 28.79%     | ok               |
|          50 | -10.35%  | 17.00%             | -17.13% |    -0.48 |       56 | 26.29%     | ok               |
|          25 | -13.00%  | 17.00%             | -22.34% |    -0.5  |       71 | 41.93%     | ok               |
|          40 | -14.80%  | 17.00%             | -24.84% |    -0.65 |       76 | 32.95%     | ok               |
|          20 | -17.26%  | 17.00%             | -24.00% |    -0.67 |       76 | 45.09%     | ok               |

## VTI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 14.24%   | 48.78%             | -13.96% |     0.51 |       64 | 56.07%     | ok               |
|          15 | 9.54%    | 48.78%             | -15.70% |     0.36 |       61 | 58.40%     | ok               |
|          25 | 1.65%    | 48.78%             | -15.00% |     0.12 |       60 | 53.74%     | ok               |
|          30 | -5.97%   | 48.78%             | -17.64% |    -0.16 |       70 | 51.75%     | ok               |
|          40 | -7.10%   | 48.78%             | -19.77% |    -0.22 |       74 | 44.26%     | ok               |

## VWO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -7.95%   | 42.42%             | -21.68% |    -0.29 |       56 | 29.78%     | ok               |
|          45 | -9.75%   | 42.42%             | -23.75% |    -0.36 |       58 | 32.28%     | ok               |
|          15 | -11.71%  | 42.42%             | -24.01% |    -0.36 |       74 | 47.92%     | ok               |
|          40 | -10.21%  | 42.42%             | -23.57% |    -0.37 |       68 | 35.11%     | ok               |
|          20 | -13.11%  | 42.42%             | -26.14% |    -0.43 |       71 | 45.59%     | ok               |

## VZ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 4.28%    | 29.60%             | -12.55% |     0.2  |       54 | 27.79%     | ok               |
|          45 | -7.69%   | 29.60%             | -21.44% |    -0.19 |       66 | 31.61%     | ok               |
|          25 | -10.15%  | 29.60%             | -22.13% |    -0.22 |       79 | 45.42%     | ok               |
|          35 | -9.01%   | 29.60%             | -22.73% |    -0.22 |       61 | 37.44%     | ok               |
|          40 | -14.10%  | 29.60%             | -24.21% |    -0.41 |       66 | 34.78%     | ok               |

## WFC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -8.62%   | 47.23%             | -22.54% |    -0.12 |       77 | 43.59%     | ok               |
|          50 | -7.22%   | 47.23%             | -18.29% |    -0.17 |       58 | 31.95%     | ok               |
|          20 | -18.09%  | 47.23%             | -29.87% |    -0.26 |       77 | 52.41%     | ok               |
|          30 | -18.14%  | 47.23%             | -29.78% |    -0.3  |       80 | 46.76%     | ok               |
|          40 | -14.27%  | 47.23%             | -24.88% |    -0.35 |       72 | 40.27%     | ok               |

## WIF-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 73.98%   | -59.70%            | -40.67% |     0.72 |       65 | 43.68%     | ok               |
|          15 | 35.96%   | -59.70%            | -46.21% |     0.54 |       75 | 46.93%     | ok               |
|          25 | 2.92%    | -59.70%            | -44.74% |     0.31 |       69 | 39.46%     | ok               |
|          30 | -25.46%  | -59.70%            | -52.76% |     0    |       66 | 35.63%     | ok               |
|          50 | -15.28%  | -59.70%            | -34.40% |    -0.09 |       34 | 11.49%     | ok               |

## WMT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 38.72%   | 82.92%             | -11.62% |     1.11 |       40 | 39.10%     | ok               |
|          50 | 33.90%   | 82.92%             | -12.19% |     1.05 |       32 | 36.77%     | ok               |
|          35 | 29.02%   | 82.92%             | -16.55% |     0.83 |       56 | 45.26%     | ok               |
|          40 | 27.36%   | 82.92%             | -15.99% |     0.82 |       48 | 40.60%     | ok               |
|          15 | 12.08%   | 82.92%             | -25.74% |     0.35 |       76 | 58.57%     | ok               |

## XBI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 13.20%   | 81.88%             | -16.08% |     0.39 |       56 | 36.94%     | ok               |
|          45 | 10.67%   | 81.88%             | -15.46% |     0.34 |       52 | 34.28%     | ok               |
|          35 | 4.23%    | 81.88%             | -16.96% |     0.19 |       64 | 40.60%     | ok               |
|          50 | 2.21%    | 81.88%             | -15.97% |     0.14 |       54 | 30.78%     | ok               |
|          30 | 2.05%    | 81.88%             | -18.30% |     0.14 |       66 | 42.10%     | ok               |

## XLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -2.33%   | 14.93%             | -18.27% |    -0.04 |       54 | 26.79%     | ok               |
|          50 | -4.33%   | 14.93%             | -17.40% |    -0.13 |       36 | 22.46%     | ok               |
|          35 | -5.65%   | 14.93%             | -21.38% |    -0.16 |       54 | 30.28%     | ok               |
|          45 | -6.09%   | 14.93%             | -19.08% |    -0.21 |       40 | 23.79%     | ok               |
|          25 | -10.56%  | 14.93%             | -23.37% |    -0.35 |       62 | 35.61%     | ok               |

## XLC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 14.20%   | 41.14%             | -12.33% |     0.52 |       63 | 50.58%     | ok               |
|          25 | 13.65%   | 41.14%             | -12.31% |     0.5  |       62 | 52.75%     | ok               |
|          50 | 7.28%    | 41.14%             | -11.12% |     0.38 |       66 | 38.60%     | ok               |
|          40 | 7.86%    | 41.14%             | -13.38% |     0.34 |       64 | 44.09%     | ok               |
|          35 | 7.13%    | 41.14%             | -13.38% |     0.31 |       62 | 47.92%     | ok               |

## XLE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.01%   | 37.18%             | -25.98% |     0.07 |       58 | 35.77%     | ok               |
|          35 | -8.15%   | 37.18%             | -31.29% |    -0.13 |       71 | 42.76%     | ok               |
|          45 | -7.48%   | 37.18%             | -30.20% |    -0.14 |       68 | 38.10%     | ok               |
|          30 | -12.75%  | 37.18%             | -35.77% |    -0.25 |       75 | 45.09%     | ok               |
|          25 | -13.34%  | 37.18%             | -36.21% |    -0.25 |       83 | 47.92%     | ok               |

## XLF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -4.19%   | 38.22%             | -18.63% |    -0.08 |       70 | 51.41%     | ok               |
|          15 | -6.88%   | 38.22%             | -20.19% |    -0.17 |       76 | 53.58%     | ok               |
|          25 | -9.62%   | 38.22%             | -23.22% |    -0.29 |       79 | 48.25%     | ok               |
|          30 | -9.66%   | 38.22%             | -23.61% |    -0.3  |       80 | 45.92%     | ok               |
|          35 | -16.69%  | 38.22%             | -24.48% |    -0.65 |       70 | 42.26%     | ok               |

## XLI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 10.13%   | 37.20%             | -10.01% |     0.39 |       84 | 49.25%     | ok               |
|          20 | 4.51%    | 37.20%             | -12.74% |     0.22 |       73 | 44.09%     | ok               |
|          25 | -4.74%   | 37.20%             | -15.60% |    -0.13 |       74 | 42.26%     | ok               |
|          50 | -4.22%   | 37.20%             | -14.94% |    -0.15 |       60 | 31.28%     | ok               |
|          30 | -5.32%   | 37.20%             | -14.16% |    -0.16 |       76 | 41.26%     | ok               |

## XLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 81.20%   | 86.42%             | -14.75% |     1.33 |       46 | 50.92%     | ok               |
|          25 | 77.51%   | 86.42%             | -14.75% |     1.33 |       40 | 48.75%     | ok               |
|          15 | 85.33%   | 86.42%             | -14.75% |     1.32 |       46 | 52.91%     | ok               |
|          30 | 66.88%   | 86.42%             | -14.75% |     1.23 |       40 | 47.42%     | ok               |
|          35 | 46.23%   | 86.42%             | -13.61% |     0.96 |       54 | 44.59%     | ok               |

## XLM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -8.27%   | -25.46%            | -49.14% |     0.13 |       71 | 49.81%     | ok               |
|          45 | -6.76%   | -25.46%            | -51.28% |     0.1  |       56 | 31.03%     | ok               |
|          50 | -7.30%   | -25.46%            | -48.81% |     0.08 |       46 | 25.67%     | ok               |
|          30 | -12.03%  | -25.46%            | -54.58% |     0.08 |       67 | 46.74%     | ok               |
|          40 | -16.37%  | -25.46%            | -47.28% |    -0    |       53 | 36.59%     | ok               |

## XLP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          45 | 11.31%   | 11.11%             | -5.66% |     0.71 |       50 | 30.62%     | ok               |
|          40 | 10.68%   | 11.11%             | -7.32% |     0.65 |       66 | 34.61%     | ok               |
|          35 | 9.72%    | 11.11%             | -8.39% |     0.59 |       62 | 37.60%     | ok               |
|          50 | 8.56%    | 11.11%             | -6.08% |     0.56 |       54 | 29.12%     | ok               |
|          30 | 8.83%    | 11.11%             | -8.96% |     0.53 |       64 | 39.27%     | ok               |

## XLU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 4.79%    | 24.57%             | -13.94% |     0.27 |       52 | 30.28%     | ok               |
|          45 | 3.64%    | 24.57%             | -14.88% |     0.22 |       56 | 31.45%     | ok               |
|          40 | 0.51%    | 24.57%             | -16.41% |     0.07 |       62 | 33.28%     | ok               |
|          35 | -2.16%   | 24.57%             | -19.71% |    -0.05 |       62 | 35.94%     | ok               |
|          30 | -3.52%   | 24.57%             | -20.40% |    -0.11 |       67 | 39.27%     | ok               |

## XLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -15.65%  | 18.66%             | -19.39% |    -0.71 |       68 | 37.27%     | ok               |
|          25 | -16.57%  | 18.66%             | -21.14% |    -0.75 |       70 | 39.43%     | ok               |
|          20 | -19.84%  | 18.66%             | -24.51% |    -0.91 |       73 | 41.10%     | ok               |
|          15 | -20.36%  | 18.66%             | -24.84% |    -0.91 |       79 | 43.76%     | ok               |
|          35 | -20.06%  | 18.66%             | -23.39% |    -1    |       66 | 34.78%     | ok               |

## XLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -2.35%   | 28.53%             | -15.77% |     0.01 |       80 | 52.58%     | ok               |
|          30 | -6.85%   | 28.53%             | -17.23% |    -0.15 |       79 | 46.09%     | ok               |
|          20 | -7.51%   | 28.53%             | -19.25% |    -0.15 |       76 | 49.25%     | ok               |
|          25 | -9.58%   | 28.53%             | -19.25% |    -0.22 |       73 | 47.75%     | ok               |
|          50 | -7.29%   | 28.53%             | -14.40% |    -0.26 |       60 | 30.95%     | ok               |

## XOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 0.82%    | 39.90%             | -21.35% |     0.1  |       38 | 27.29%     | ok               |
|          25 | -1.15%   | 39.90%             | -19.90% |     0.05 |       59 | 35.61%     | ok               |
|          30 | -2.13%   | 39.90%             | -20.29% |     0.02 |       59 | 34.94%     | ok               |
|          45 | -5.68%   | 39.90%             | -23.33% |    -0.1  |       44 | 28.79%     | ok               |
|          40 | -7.07%   | 39.90%             | -21.45% |    -0.13 |       54 | 32.11%     | ok               |

## XRP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 21.07%   | -38.21%            | -31.38% |     0.43 |       72 | 43.30%     | ok               |
|          40 | 9.21%    | -38.21%            | -33.91% |     0.3  |       60 | 36.59%     | ok               |
|          30 | 1.95%    | -38.21%            | -31.82% |     0.23 |       67 | 48.08%     | ok               |
|          45 | -1.97%   | -38.21%            | -36.27% |     0.16 |       58 | 32.18%     | ok               |
|          20 | -9.50%   | -38.21%            | -38.12% |     0.11 |       79 | 56.32%     | ok               |

## YFI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -48.52%  | -55.26%            | -50.05% |    -0.83 |       58 | 26.82%     | ok               |
|          45 | -48.73%  | -55.26%            | -50.13% |    -1.08 |       70 | 21.26%     | ok               |
|          35 | -63.46%  | -55.26%            | -66.31% |    -1.14 |       69 | 34.48%     | ok               |
|          30 | -66.69%  | -55.26%            | -72.54% |    -1.18 |       79 | 38.70%     | ok               |
|          15 | -72.62%  | -55.26%            | -76.87% |    -1.27 |       85 | 51.15%     | ok               |

## ZEC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 172.14%  | 3033.88%           | -30.64% |     1.02 |       46 | 30.08%     | ok               |
|          35 | 136.03%  | 3033.88%           | -50.84% |     0.9  |       52 | 36.78%     | ok               |
|          25 | 124.91%  | 3033.88%           | -58.07% |     0.86 |       56 | 43.87%     | ok               |
|          30 | 109.88%  | 3033.88%           | -56.50% |     0.82 |       64 | 41.00%     | ok               |
|          20 | 94.07%   | 3033.88%           | -62.70% |     0.76 |       64 | 45.79%     | ok               |
