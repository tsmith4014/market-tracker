# Market Tracker Backtest Report

_Generated: 2026-06-16T01:48:13+00:00_

## Data Sources

- Crypto: Kraken -> Coinbase -> CoinGecko OHLC -> CoinPaprika fallback chain.
- Stocks / ETFs / indices: Stooq -> Yahoo Finance fallback chain.
- Data rows are generated from real market APIs. Mock OHLCV rows are not generated.

## Data Freshness

- Rows: **92,395**
- Symbols: **161**
- Date range: **2024-01-23** to **2026-06-16**

## Latest Signals

| symbol     | date                |         close |   composite_score | signal   | data_source   |
|:-----------|:--------------------|--------------:|------------------:|:---------|:--------------|
| AMAT       | 2026-06-15 00:00:00 |   585.78      |         71.75     | LONG     | Yahoo Finance |
| ATOM-USD   | 2026-06-16 00:00:00 |     1.9507    |         32.6667   | LONG     | Kraken API    |
| BAC        | 2026-06-15 00:00:00 |    55.87      |         52.75     | LONG     | Yahoo Finance |
| C          | 2026-06-15 00:00:00 |   141.21      |         70.75     | LONG     | Yahoo Finance |
| CRV-USD    | 2026-06-16 00:00:00 |     0.24503   |         41.8333   | LONG     | Kraken API    |
| CSCO       | 2026-06-15 00:00:00 |   120.17      |         40.5833   | LONG     | Yahoo Finance |
| DE         | 2026-06-15 00:00:00 |   575.47      |         77.8333   | LONG     | Yahoo Finance |
| DXY-INDEX  | 2026-06-15 00:00:00 |    99.643     |         79.0323   | LONG     | Yahoo Finance |
| GE         | 2026-06-15 00:00:00 |   342.26      |         63.9167   | LONG     | Yahoo Finance |
| GS         | 2026-06-15 00:00:00 |  1076.17      |         47.25     | LONG     | Yahoo Finance |
| HD         | 2026-06-15 00:00:00 |   329.82      |         38.0833   | LONG     | Yahoo Finance |
| HON        | 2026-06-15 00:00:00 |   227.41      |         32        | LONG     | Yahoo Finance |
| ITA        | 2026-06-15 00:00:00 |   237.4       |         60.5833   | LONG     | Yahoo Finance |
| JPM        | 2026-06-15 00:00:00 |   319.4       |         56.0833   | LONG     | Yahoo Finance |
| LLY        | 2026-06-15 00:00:00 |  1129.35      |         56.5833   | LONG     | Yahoo Finance |
| LRCX       | 2026-06-15 00:00:00 |   388.92      |         75.0833   | LONG     | Yahoo Finance |
| MS         | 2026-06-15 00:00:00 |   217.98      |         47.25     | LONG     | Yahoo Finance |
| MU         | 2026-06-15 00:00:00 |  1087.99      |         50.5833   | LONG     | Yahoo Finance |
| PG         | 2026-06-15 00:00:00 |   150.46      |         82.8333   | LONG     | Yahoo Finance |
| PM         | 2026-06-15 00:00:00 |   181.81      |         46.25     | LONG     | Yahoo Finance |
| RTX        | 2026-06-15 00:00:00 |   183.64      |         54.8333   | LONG     | Yahoo Finance |
| SBUX       | 2026-06-15 00:00:00 |   101.59      |         55.9167   | LONG     | Yahoo Finance |
| SPY        | 2026-06-15 00:00:00 |   754.83      |         32.75     | LONG     | Yahoo Finance |
| TIA-USD    | 2026-06-16 00:00:00 |     0.3748    |         38.4167   | LONG     | Kraken API    |
| UNH        | 2026-06-15 00:00:00 |   411.04      |         75.75     | LONG     | Yahoo Finance |
| UPS        | 2026-06-15 00:00:00 |   108.83      |         76.9167   | LONG     | Yahoo Finance |
| WFC        | 2026-06-15 00:00:00 |    83.14      |         58.0833   | LONG     | Yahoo Finance |
| WMT        | 2026-06-15 00:00:00 |   120.82      |         35.1667   | LONG     | Yahoo Finance |
| XLK        | 2026-06-15 00:00:00 |   191.79      |         47.0833   | LONG     | Yahoo Finance |
| XLM-USD    | 2026-06-16 00:00:00 |     0.212995  |         39.5833   | LONG     | Kraken API    |
| AAPL       | 2026-06-15 00:00:00 |   296.42      |          0.916667 | NEUTRAL  | Yahoo Finance |
| AAVE-USD   | 2026-06-16 00:00:00 |    73.8       |          9.16667  | NEUTRAL  | Kraken API    |
| ABBV       | 2026-06-15 00:00:00 |   221.59      |         48.4167   | NEUTRAL  | Yahoo Finance |
| ADBE       | 2026-06-15 00:00:00 |   206.36      |        -66.5      | NEUTRAL  | Yahoo Finance |
| AGG        | 2026-06-15 00:00:00 |    98.85      |         -2.25     | NEUTRAL  | Yahoo Finance |
| AMD        | 2026-06-15 00:00:00 |   547.26      |         41        | NEUTRAL  | Yahoo Finance |
| AMGN       | 2026-06-15 00:00:00 |   350.53      |         63.1667   | NEUTRAL  | Yahoo Finance |
| AMZN       | 2026-06-15 00:00:00 |   246.02      |         -9.33333  | NEUTRAL  | Yahoo Finance |
| ARB-USD    | 2026-06-16 00:00:00 |     0.0863    |        -21        | NEUTRAL  | Kraken API    |
| ARKK       | 2026-06-15 00:00:00 |    79.63      |         18.4167   | NEUTRAL  | Yahoo Finance |
| AVGO       | 2026-06-15 00:00:00 |   393.94      |        -44.25     | NEUTRAL  | Yahoo Finance |
| BA         | 2026-06-15 00:00:00 |   228.95      |         38.6667   | NEUTRAL  | Yahoo Finance |
| BLK        | 2026-06-15 00:00:00 |  1042.87      |         -1.5      | NEUTRAL  | Yahoo Finance |
| BND        | 2026-06-15 00:00:00 |    73.3       |         -2.25     | NEUTRAL  | Yahoo Finance |
| BONK-USD   | 2026-06-16 00:00:00 |     4.773e-06 |        -17.5      | NEUTRAL  | Kraken API    |
| BTC-USD    | 2026-06-16 00:00:00 | 66316         |        -13.5      | NEUTRAL  | Kraken API    |
| CAT        | 2026-06-15 00:00:00 |   933.93      |         48.3333   | NEUTRAL  | Yahoo Finance |
| CL         | 2026-06-15 00:00:00 |    90.58      |         50.8333   | NEUTRAL  | Yahoo Finance |
| CMCSA      | 2026-06-15 00:00:00 |    23.97      |        -17.4167   | NEUTRAL  | Yahoo Finance |
| COMP-USD   | 2026-06-16 00:00:00 |    18.05      |         -1.33333  | NEUTRAL  | Kraken API    |
| COP        | 2026-06-15 00:00:00 |   112.26      |        -20.25     | NEUTRAL  | Yahoo Finance |
| COST       | 2026-06-15 00:00:00 |   979.45      |         -9.83333  | NEUTRAL  | Yahoo Finance |
| CRM        | 2026-06-15 00:00:00 |   164.55      |        -66.5      | NEUTRAL  | Yahoo Finance |
| CVX        | 2026-06-15 00:00:00 |   180.4       |        -20.25     | NEUTRAL  | Yahoo Finance |
| DASH-USD   | 2026-06-16 00:00:00 |    38.157     |        -10.8333   | NEUTRAL  | Kraken API    |
| DBC        | 2026-06-15 00:00:00 |    28.22      |        -14.0833   | NEUTRAL  | Yahoo Finance |
| DIA        | 2026-06-15 00:00:00 |   518.44      |         31        | NEUTRAL  | Yahoo Finance |
| DOGE-USD   | 2026-06-16 00:00:00 |     0.0879239 |        -21        | NEUTRAL  | Kraken API    |
| DOT-USD    | 2026-06-16 00:00:00 |     1.0137    |        -19        | NEUTRAL  | Kraken API    |
| EEM        | 2026-06-15 00:00:00 |    69.75      |         37.5      | NEUTRAL  | Yahoo Finance |
| EFA        | 2026-06-15 00:00:00 |   104.08      |          4.83333  | NEUTRAL  | Yahoo Finance |
| EOG        | 2026-06-15 00:00:00 |   131.98      |        -23.5833   | NEUTRAL  | Yahoo Finance |
| ETC-USD    | 2026-06-16 00:00:00 |     7.385     |        -19        | NEUTRAL  | Kraken API    |
| ETH-USD    | 2026-06-16 00:00:00 |  1794.09      |        -28.5      | NEUTRAL  | Kraken API    |
| EWJ        | 2026-06-15 00:00:00 |    94.06      |         21.5      | NEUTRAL  | Yahoo Finance |
| FCX        | 2026-06-15 00:00:00 |    70.13      |         60        | NEUTRAL  | Yahoo Finance |
| GDX        | 2026-06-15 00:00:00 |    85.27      |         -7.91667  | NEUTRAL  | Yahoo Finance |
| GDXJ       | 2026-06-15 00:00:00 |   111.88      |        -11.9167   | NEUTRAL  | Yahoo Finance |
| GOOGL      | 2026-06-15 00:00:00 |   369.35      |          4.91667  | NEUTRAL  | Yahoo Finance |
| HBAR-USD   | 2026-06-16 00:00:00 |     0.08301   |        -35.0833   | NEUTRAL  | Kraken API    |
| HYG        | 2026-06-15 00:00:00 |    80.04      |          0.25     | NEUTRAL  | Yahoo Finance |
| IBM        | 2026-06-15 00:00:00 |   268.71      |         12.3333   | NEUTRAL  | Yahoo Finance |
| ICP-USD    | 2026-06-16 00:00:00 |     2.415     |        -65.25     | NEUTRAL  | Kraken API    |
| IEF        | 2026-06-15 00:00:00 |    94.28      |        -13.75     | NEUTRAL  | Yahoo Finance |
| IEMG       | 2026-06-15 00:00:00 |    84.41      |         37.5      | NEUTRAL  | Yahoo Finance |
| INJ-USD    | 2026-06-16 00:00:00 |     5.578     |         15.4167   | NEUTRAL  | Kraken API    |
| INTC       | 2026-06-15 00:00:00 |   127.86      |         40.5      | NEUTRAL  | Yahoo Finance |
| IWM        | 2026-06-15 00:00:00 |   294.64      |         41.5      | NEUTRAL  | Yahoo Finance |
| JNJ        | 2026-06-15 00:00:00 |   235.66      |         63.1667   | NEUTRAL  | Yahoo Finance |
| KO         | 2026-06-15 00:00:00 |    80.91      |         47.8333   | NEUTRAL  | Yahoo Finance |
| LDO-USD    | 2026-06-16 00:00:00 |     0.275     |        -21        | NEUTRAL  | Kraken API    |
| LIN        | 2026-06-15 00:00:00 |   521.48      |         57.5      | NEUTRAL  | Yahoo Finance |
| LINK-USD   | 2026-06-16 00:00:00 |     8.27579   |        -17.5      | NEUTRAL  | Kraken API    |
| LTC-USD    | 2026-06-16 00:00:00 |    45.8       |        -13.5      | NEUTRAL  | Kraken API    |
| MCD        | 2026-06-15 00:00:00 |   286.12      |         -4.83333  | NEUTRAL  | Yahoo Finance |
| META       | 2026-06-15 00:00:00 |   593.48      |        -61.0833   | NEUTRAL  | Yahoo Finance |
| MPC        | 2026-06-15 00:00:00 |   250.86      |         23.8333   | NEUTRAL  | Yahoo Finance |
| MRK        | 2026-06-15 00:00:00 |   114.9       |         -2.08333  | NEUTRAL  | Yahoo Finance |
| MSFT       | 2026-06-15 00:00:00 |   399.76      |        -62        | NEUTRAL  | Yahoo Finance |
| NEAR-USD   | 2026-06-16 00:00:00 |     2.4102    |         28.0833   | NEUTRAL  | Kraken API    |
| NEM        | 2026-06-15 00:00:00 |   105.8       |         -4.16667  | NEUTRAL  | Yahoo Finance |
| NKE        | 2026-06-15 00:00:00 |    45.2       |          2.41667  | NEUTRAL  | Yahoo Finance |
| NVDA       | 2026-06-15 00:00:00 |   212.45      |         -6.33333  | NEUTRAL  | Yahoo Finance |
| OP-USD     | 2026-06-16 00:00:00 |     0.1089    |         -3.5      | NEUTRAL  | Kraken API    |
| ORCL       | 2026-06-15 00:00:00 |   192.64      |          4.16667  | NEUTRAL  | Yahoo Finance |
| OXY        | 2026-06-15 00:00:00 |    54.46      |        -23.5833   | NEUTRAL  | Yahoo Finance |
| PEP        | 2026-06-15 00:00:00 |   146.25      |         24.9167   | NEUTRAL  | Yahoo Finance |
| PEPE-USD   | 2026-06-16 00:00:00 |     2.951e-06 |        -17.5      | NEUTRAL  | Kraken API    |
| PFE        | 2026-06-15 00:00:00 |    26         |         14.75     | NEUTRAL  | Yahoo Finance |
| QCOM       | 2026-06-15 00:00:00 |   220.81      |         17.6667   | NEUTRAL  | Yahoo Finance |
| QQQ        | 2026-06-15 00:00:00 |   744         |         37.5      | NEUTRAL  | Yahoo Finance |
| RENDER-USD | 2026-06-16 00:00:00 |     1.777     |        -50.25     | NEUTRAL  | Kraken API    |
| SCHW       | 2026-06-15 00:00:00 |    90.95      |         11.1667   | NEUTRAL  | Yahoo Finance |
| SHIB-USD   | 2026-06-16 00:00:00 |     5.032e-06 |        -15.5      | NEUTRAL  | Kraken API    |
| SHY        | 2026-06-15 00:00:00 |    82.11      |        -19.25     | NEUTRAL  | Yahoo Finance |
| SLB        | 2026-06-15 00:00:00 |    53.71      |        -22.3333   | NEUTRAL  | Yahoo Finance |
| SMH        | 2026-06-15 00:00:00 |   647.1       |         45        | NEUTRAL  | Yahoo Finance |
| SNX-USD    | 2026-06-16 00:00:00 |     0.2543    |        -21        | NEUTRAL  | Kraken API    |
| SOL-USD    | 2026-06-16 00:00:00 |    74.2       |          9.16667  | NEUTRAL  | Kraken API    |
| SOXX       | 2026-06-15 00:00:00 |   628.45      |         41        | NEUTRAL  | Yahoo Finance |
| SUSHI-USD  | 2026-06-16 00:00:00 |     0.188     |        -18.9167   | NEUTRAL  | Kraken API    |
| TGT        | 2026-06-15 00:00:00 |   133.17      |         58.6667   | NEUTRAL  | Yahoo Finance |
| TLT        | 2026-06-15 00:00:00 |    85.72      |         29.1667   | NEUTRAL  | Yahoo Finance |
| TMO        | 2026-06-15 00:00:00 |   473.72      |         16.6667   | NEUTRAL  | Yahoo Finance |
| TMUS       | 2026-06-15 00:00:00 |   188.86      |         -9.75     | NEUTRAL  | Yahoo Finance |
| TRX-USD    | 2026-06-16 00:00:00 |     0.318833  |         -9.91667  | NEUTRAL  | Kraken API    |
| TSLA       | 2026-06-15 00:00:00 |   411.15      |          2.16667  | NEUTRAL  | Yahoo Finance |
| TXN        | 2026-06-15 00:00:00 |   313.34      |         29.1667   | NEUTRAL  | Yahoo Finance |
| UNI-USD    | 2026-06-16 00:00:00 |     2.9399    |         18.9167   | NEUTRAL  | Kraken API    |
| USO        | 2026-06-15 00:00:00 |   121.21      |        -27.3333   | NEUTRAL  | Yahoo Finance |
| VEA        | 2026-06-15 00:00:00 |    72.39      |         30.5      | NEUTRAL  | Yahoo Finance |
| VIXY       | 2026-06-15 00:00:00 |    21.7       |        -19.4167   | NEUTRAL  | Yahoo Finance |
| VNQ        | 2026-06-15 00:00:00 |    97.82      |         57.3333   | NEUTRAL  | Yahoo Finance |
| VTI        | 2026-06-15 00:00:00 |   372.53      |         21.5      | NEUTRAL  | Yahoo Finance |
| VWO        | 2026-06-15 00:00:00 |    60.84      |         12.5      | NEUTRAL  | Yahoo Finance |
| VZ         | 2026-06-15 00:00:00 |    47.07      |         24.25     | NEUTRAL  | Yahoo Finance |
| WIF-USD    | 2026-06-16 00:00:00 |     0.1681    |        -21        | NEUTRAL  | Kraken API    |
| XBI        | 2026-06-15 00:00:00 |   136.4       |         63.3333   | NEUTRAL  | Yahoo Finance |
| XLB        | 2026-06-15 00:00:00 |    52.5       |         63.1667   | NEUTRAL  | Yahoo Finance |
| XLE        | 2026-06-15 00:00:00 |    55.55      |        -27.3333   | NEUTRAL  | Yahoo Finance |
| XLF        | 2026-06-15 00:00:00 |    53.56      |         55.8333   | NEUTRAL  | Yahoo Finance |
| XLI        | 2026-06-15 00:00:00 |   178.68      |         63.6667   | NEUTRAL  | Yahoo Finance |
| XLP        | 2026-06-15 00:00:00 |    85.48      |         67.3333   | NEUTRAL  | Yahoo Finance |
| XLU        | 2026-06-15 00:00:00 |    44.74      |         10.5833   | NEUTRAL  | Yahoo Finance |
| XLV        | 2026-06-15 00:00:00 |   152.89      |         48.3333   | NEUTRAL  | Yahoo Finance |
| XLY        | 2026-06-15 00:00:00 |   118.57      |         -0.833333 | NEUTRAL  | Yahoo Finance |
| XOM        | 2026-06-15 00:00:00 |   140.92      |        -23.5833   | NEUTRAL  | Yahoo Finance |
| XRP-USD    | 2026-06-16 00:00:00 |     1.23205   |         16.6667   | NEUTRAL  | Kraken API    |
| YFI-USD    | 2026-06-16 00:00:00 |  2036.6       |        -19        | NEUTRAL  | Kraken API    |
| ZEC-USD    | 2026-06-16 00:00:00 |   513.22      |         11.5      | NEUTRAL  | Kraken API    |
| ADA-USD    | 2026-06-16 00:00:00 |     0.177748  |        -30        | SHORT    | Kraken API    |
| ALGO-USD   | 2026-06-16 00:00:00 |     0.09543   |        -35        | SHORT    | Kraken API    |
| APT-USD    | 2026-06-16 00:00:00 |     0.6791    |        -36.6667   | SHORT    | Kraken API    |
| AVAX-USD   | 2026-06-16 00:00:00 |     6.858     |        -36.6667   | SHORT    | Kraken API    |
| BCH-USD    | 2026-06-16 00:00:00 |   223.83      |        -41        | SHORT    | Kraken API    |
| BITO       | 2026-06-15 00:00:00 |     9.05      |        -50.5833   | SHORT    | Yahoo Finance |
| DIS        | 2026-06-15 00:00:00 |   101.69      |        -34.9167   | SHORT    | Yahoo Finance |
| FET-USD    | 2026-06-16 00:00:00 |     0.2121    |        -48.5833   | SHORT    | Kraken API    |
| FIL-USD    | 2026-06-16 00:00:00 |     0.795     |        -34        | SHORT    | Kraken API    |
| FXI        | 2026-06-15 00:00:00 |    35.11      |        -36.75     | SHORT    | Yahoo Finance |
| GLD        | 2026-06-15 00:00:00 |   396.55      |        -51.9167   | SHORT    | Yahoo Finance |
| GRT-USD    | 2026-06-16 00:00:00 |     0.02038   |        -35        | SHORT    | Kraken API    |
| IBIT       | 2026-06-15 00:00:00 |    37.74      |        -50.5833   | SHORT    | Yahoo Finance |
| INTU       | 2026-06-15 00:00:00 |   281.77      |        -52.5833   | SHORT    | Yahoo Finance |
| NFLX       | 2026-06-15 00:00:00 |    81.67      |        -57.4167   | SHORT    | Yahoo Finance |
| NOW        | 2026-06-15 00:00:00 |   104.15      |        -34.6667   | SHORT    | Yahoo Finance |
| POL-USD    | 2026-06-16 00:00:00 |     0.07825   |        -48        | SHORT    | Kraken API    |
| SKY-USD    | 2026-06-16 00:00:00 |     0.05731   |        -31        | SHORT    | Kraken API    |
| SLV        | 2026-06-15 00:00:00 |    63.47      |        -31.0833   | SHORT    | Yahoo Finance |
| T          | 2026-06-15 00:00:00 |    23.29      |        -56.0833   | SHORT    | Yahoo Finance |
| XLC        | 2026-06-15 00:00:00 |   112.19      |        -48.3333   | SHORT    | Yahoo Finance |

## Edge Summary

- Symbols with trades: **160** of 160
- Beat buy-and-hold: **33.12%** of traded symbols
- Positive return: **34.38%** of traded symbols
- Median strategy return: **-9.08%** (benchmark **16.64%**)
- Median excess vs benchmark: **-31.21%**
- Median Sharpe: **-0.09**
- Median exposure: **44.44%**

> Edge is real only if both _beat buy-and-hold_ and _median excess_ are convincingly positive across many symbols. Treat a single high-return symbol as noise.

## Portfolio Backtest

Actual capital-allocation books (not per-symbol averages). Benchmarks: `equal_weight_buyhold` (whole tracked universe), `spy_buyhold` (100% SPY), and `sixty_forty` (60% SPY / 40% AGG). `high_conf_voltarget` inverse-vol-weights the HIGH-confidence book; `conviction_long_short` is market-neutral. Judge on **Sharpe** and **max_drawdown** out-of-sample, not raw return: a fully-invested long book wins on return in a bull market but carries all the risk.

| strategy              | scope         | ann_return   | ann_vol   |   sharpe | max_drawdown   | total_return   |   avg_gross_exposure |
|:----------------------|:--------------|:-------------|:----------|---------:|:---------------|:---------------|---------------------:|
| equal_weight_buyhold  | full          | -9.88%       | 33.87%    |    -0.29 | -58.16%        | -37.98%        |                 1    |
| equal_weight_buyhold  | out_of_sample | -8.94%       | 34.83%    |    -0.26 | -39.63%        | -14.79%        |                 1    |
| all_signals_ew        | full          | -7.74%       | 28.19%    |    -0.27 | -59.69%        | -30.06%        |                 1    |
| all_signals_ew        | out_of_sample | 5.14%        | 28.62%    |     0.18 | -24.86%        | 1.15%          |                 1    |
| high_conf_ew          | full          | 3.18%        | 32.85%    |     0.1  | -44.51%        | -6.36%         |                 0.89 |
| high_conf_ew          | out_of_sample | 24.91%       | 36.89%    |     0.68 | -20.90%        | 21.52%         |                 0.89 |
| high_conf_voltarget   | full          | 3.89%        | 30.55%    |     0.13 | -36.25%        | -2.13%         |                 0.89 |
| high_conf_voltarget   | out_of_sample | 18.45%       | 35.14%    |     0.52 | -17.06%        | 14.21%         |                 0.89 |
| conviction_long_short | full          | -8.78%       | 23.49%    |    -0.37 | -35.78%        | -29.69%        |                 0.97 |
| conviction_long_short | out_of_sample | -4.05%       | 27.15%    |    -0.15 | -21.23%        | -7.94%         |                 0.97 |
| spy_buyhold           | full          | 8.48%        | 13.36%    |     0.63 | -17.81%        | 26.01%         |                 0.78 |
| spy_buyhold           | out_of_sample | -2.30%       | 9.91%     |    -0.23 | -14.83%        | -2.93%         |                 0.78 |
| sixty_forty           | full          | 4.92%        | 8.46%     |     0.58 | -10.80%        | 14.90%         |                 0.78 |
| sixty_forty           | out_of_sample | -2.46%       | 6.44%     |    -0.38 | -10.06%        | -2.81%         |                 0.78 |

## Walk-Forward Robustness

Each book measured across contiguous time folds (each a different regime). A book has durable edge only if `mean_sharpe` is positive, `min_sharpe` isn't deeply negative, and `pct_positive_folds` is high — a single great fold doesn't count. `fold_sharpes` lists each fold oldest-to-newest.

| strategy              |   n_folds |   mean_sharpe |   median_sharpe |   min_sharpe | pct_positive_folds   | mean_return   | fold_sharpes                 |
|:----------------------|----------:|--------------:|----------------:|-------------:|:---------------------|:--------------|:-----------------------------|
| equal_weight_buyhold  |         5 |          0.04 |           -0.37 |        -2.03 | 40.00%               | -5.76%        | 1.95;-2.03;1.18;-0.37;-0.54  |
| all_signals_ew        |         5 |         -0.07 |            0.63 |        -1.65 | 60.00%               | -4.89%        | 0.80;0.63;-1.26;-1.65;1.13   |
| high_conf_ew          |         5 |          0.41 |            0.09 |        -0.84 | 60.00%               | -0.07%        | 1.87;0.09;-0.84;-0.30;1.23   |
| high_conf_voltarget   |         5 |          0.53 |            0.26 |        -0.87 | 60.00%               | 0.39%         | 2.73;0.26;-0.87;-0.11;0.64   |
| conviction_long_short |         5 |         -0.35 |           -0.46 |        -1.03 | 20.00%               | -6.50%        | -0.46;-0.15;-0.49;-1.03;0.36 |
| spy_buyhold           |         5 |          0.6  |            0.45 |        -0.44 | 80.00%               | 4.91%         | 2.00;0.58;0.45;-0.44;0.39    |
| sixty_forty           |         5 |          0.52 |            0.32 |        -0.31 | 80.00%               | 2.89%         | 2.01;0.32;0.47;-0.31;0.12    |

## Strategy Comparison

Each decision rule backtested over the same data. `out_of_sample` is the most recent ~35% of each symbol's history (unseen tail). A rule has real edge only if `median_excess` and `beat_benchmark_pct` stay positive out-of-sample, not just full-sample.

| strategy        | scope         |   symbols | beat_benchmark_pct   | positive_pct   | median_return   | median_benchmark   | median_excess   |   median_sharpe |   total_trades |
|:----------------|:--------------|----------:|:---------------------|:---------------|:----------------|:-------------------|:----------------|----------------:|---------------:|
| trend           | full          |       160 | 33.12%               | 34.38%         | -9.08%          | 16.64%             | -31.21%         |           -0.09 |          11215 |
| trend           | out_of_sample |       160 | 35.00%               | 54.37%         | 3.05%           | 6.76%              | -9.01%          |            0.32 |           3926 |
| mean_reversion  | full          |       157 | 39.49%               | 49.04%         | -0.10%          | 15.34%             | -18.80%         |           -0.02 |           1244 |
| mean_reversion  | out_of_sample |       129 | 43.41%               | 58.14%         | 0.33%           | 4.20%              | -4.88%          |            0.7  |            476 |
| regime_adaptive | full          |       160 | 33.12%               | 33.12%         | -9.22%          | 16.64%             | -31.24%         |           -0.08 |          11490 |
| regime_adaptive | out_of_sample |       160 | 35.62%               | 55.62%         | 3.05%           | 6.76%              | -9.45%          |            0.33 |           4029 |

## Signal Calibration

Realized forward return in the signal's direction, grouped by confidence. HIGH should outrank LOW for the confidence score to be meaningful.

| confidence_level   |   horizon |     n | mean_return   | median_return   | win_rate   |
|:-------------------|----------:|------:|:--------------|:----------------|:-----------|
| HIGH               |         5 |  8164 | 0.19%         | 0.15%           | 52.47%     |
| MEDIUM             |         5 | 29168 | 0.07%         | 0.10%           | 51.11%     |
| LOW                |         5 |  3271 | -0.56%        | -0.45%          | 45.25%     |
| ALL                |         5 | 40603 | 0.05%         | 0.07%           | 50.91%     |
| HIGH               |        10 |  8131 | 0.51%         | 0.20%           | 52.39%     |
| MEDIUM             |        10 | 28893 | 0.26%         | 0.17%           | 51.39%     |
| LOW                |        10 |  3242 | -0.85%        | -0.70%          | 45.47%     |
| ALL                |        10 | 40266 | 0.22%         | 0.13%           | 51.12%     |
| HIGH               |        20 |  8029 | 0.97%         | 0.54%           | 54.07%     |
| MEDIUM             |        20 | 28319 | 0.86%         | 0.62%           | 53.58%     |
| LOW                |        20 |  3210 | -0.65%        | -0.51%          | 47.07%     |
| ALL                |        20 | 39558 | 0.76%         | 0.53%           | 53.15%     |

## Backtest Summary

### Data Quality / Signal Availability

- **ok**: 160 symbols

| symbol     |   trades | return   | benchmark_return   | mdd     |   sharpe | exposure   | skipped_reason   |
|:-----------|---------:|:---------|:-------------------|:--------|---------:|:-----------|:-----------------|
| AAPL       |       63 | 10.88%   | 51.87%             | -20.65% |     0.32 | 49.08%     | ok               |
| AAVE-USD   |       80 | -62.59%  | -74.32%            | -69.20% |    -0.76 | 36.97%     | ok               |
| ABBV       |       64 | -15.69%  | 32.29%             | -30.55% |    -0.31 | 49.08%     | ok               |
| ADA-USD    |       88 | -83.06%  | -82.13%            | -89.12% |    -0.68 | 46.55%     | ok               |
| ADBE       |       66 | -22.69%  | -65.44%            | -38.01% |    -0.23 | 56.91%     | ok               |
| AGG        |       69 | -6.61%   | 0.91%              | -10.16% |    -1.1  | 31.11%     | ok               |
| ALGO-USD   |       86 | -48.36%  | -74.73%            | -53.13% |    -0.53 | 37.93%     | ok               |
| AMAT       |       69 | -18.98%  | 250.66%            | -57.21% |    -0.1  | 53.41%     | ok               |
| AMD        |       56 | 6.53%    | 224.94%            | -47.17% |     0.28 | 38.44%     | ok               |
| AMGN       |       71 | -19.45%  | 13.11%             | -34.14% |    -0.38 | 48.25%     | ok               |
| AMZN       |       74 | -33.84%  | 57.68%             | -42.48% |    -0.99 | 38.27%     | ok               |
| APT-USD    |       76 | -30.41%  | -92.55%            | -69.96% |    -0.05 | 43.87%     | ok               |
| ARB-USD    |       70 | 3.32%    | -88.39%            | -62.67% |     0.28 | 39.46%     | ok               |
| ARKK       |       81 | -32.67%  | 68.07%             | -35.19% |    -0.57 | 38.94%     | ok               |
| ATOM-USD   |       88 | -66.75%  | -70.48%            | -72.89% |    -1.09 | 44.06%     | ok               |
| AVAX-USD   |       74 | -39.39%  | -81.52%            | -60.45% |    -0.34 | 38.89%     | ok               |
| AVGO       |       60 | 29.90%   | 221.24%            | -35.76% |     0.48 | 45.76%     | ok               |
| BA         |       69 | 7.64%    | 8.25%              | -30.56% |     0.25 | 50.42%     | ok               |
| BAC        |       80 | -15.06%  | 70.49%             | -27.64% |    -0.36 | 46.59%     | ok               |
| BCH-USD    |       76 | -10.60%  | -49.21%            | -53.87% |     0.08 | 46.55%     | ok               |
| BITO       |       78 | 1.25%    | -52.17%            | -42.82% |     0.19 | 40.10%     | ok               |
| BLK        |       75 | -6.68%   | 31.58%             | -21.47% |    -0.13 | 42.26%     | ok               |
| BND        |       65 | -7.32%   | 0.94%              | -9.89%  |    -1.18 | 32.28%     | ok               |
| BONK-USD   |       66 | 59.52%   | -83.01%            | -43.77% |     0.67 | 41.76%     | ok               |
| BTC-USD    |       70 | 6.41%    | -29.87%            | -23.38% |     0.25 | 51.15%     | ok               |
| C          |       83 | -24.59%  | 164.93%            | -37.02% |    -0.46 | 50.58%     | ok               |
| CAT        |       72 | 35.10%   | 223.35%            | -21.02% |     0.63 | 56.91%     | ok               |
| CL         |       60 | 17.02%   | 11.26%             | -14.32% |     0.58 | 48.42%     | ok               |
| CMCSA      |       80 | -36.24%  | -41.81%            | -40.02% |    -0.9  | 44.59%     | ok               |
| COMP-USD   |       89 | -36.73%  | -77.39%            | -58.43% |    -0.21 | 45.02%     | ok               |
| COP        |       75 | -27.06%  | 3.95%              | -43.77% |    -0.52 | 40.60%     | ok               |
| COST       |       62 | 5.55%    | 42.45%             | -29.73% |     0.23 | 46.92%     | ok               |
| CRM        |       65 | -35.46%  | -40.55%            | -41.46% |    -0.72 | 43.76%     | ok               |
| CRV-USD    |       64 | -5.05%   | -71.07%            | -39.89% |     0.18 | 34.10%     | ok               |
| CSCO       |       59 | 23.21%   | 132.17%            | -21.79% |     0.51 | 49.75%     | ok               |
| CVX        |       71 | -16.65%  | 26.96%             | -26.75% |    -0.43 | 41.60%     | ok               |
| DASH-USD   |       65 | -47.28%  | 2.34%              | -64.43% |    -0.08 | 31.61%     | ok               |
| DBC        |       58 | -12.57%  | 27.40%             | -25.35% |    -0.43 | 32.78%     | ok               |
| DE         |       72 | -8.25%   | 48.52%             | -25.29% |    -0.09 | 45.59%     | ok               |
| DIA        |       60 | -2.42%   | 36.78%             | -12.94% |    -0.09 | 45.92%     | ok               |
| DIS        |       63 | -5.57%   | 8.45%              | -24.86% |    -0.01 | 48.59%     | ok               |
| DOGE-USD   |       75 | -16.53%  | -74.21%            | -60.95% |     0.09 | 49.81%     | ok               |
| DOT-USD    |       90 | -47.22%  | -84.95%            | -61.09% |    -0.35 | 48.08%     | ok               |
| DXY-INDEX  |       44 | -3.67%   | -3.24%             | -6.06%  |    -0.59 | 28.85%     | ok               |
| EEM        |       64 | -9.40%   | 81.74%             | -25.67% |    -0.25 | 43.43%     | ok               |
| EFA        |       58 | -8.33%   | 40.74%             | -13.87% |    -0.3  | 43.93%     | ok               |
| EOG        |       81 | -28.94%  | 19.58%             | -48.13% |    -0.66 | 46.92%     | ok               |
| ETC-USD    |       64 | -35.69%  | -71.21%            | -48.16% |    -0.51 | 31.23%     | ok               |
| ETH-USD    |       60 | 157.31%  | -45.34%            | -30.11% |     1.28 | 44.83%     | ok               |
| EWJ        |       64 | -17.54%  | 42.32%             | -30.73% |    -0.56 | 41.26%     | ok               |
| FCX        |       71 | -36.27%  | 83.73%             | -48.09% |    -0.49 | 45.92%     | ok               |
| FET-USD    |       71 | -5.42%   | -83.91%            | -47.67% |     0.23 | 37.55%     | ok               |
| FIL-USD    |       70 | -33.21%  | -84.73%            | -48.33% |    -0.29 | 32.95%     | ok               |
| FXI        |       50 | -13.00%  | 58.80%             | -24.33% |    -0.26 | 28.12%     | ok               |
| GDX        |       62 | -0.20%   | 202.05%            | -34.99% |     0.13 | 48.59%     | ok               |
| GDXJ       |       68 | -27.50%  | 225.33%            | -44.93% |    -0.31 | 46.42%     | ok               |
| GE         |       74 | 14.85%   | 230.01%            | -27.82% |     0.36 | 51.75%     | ok               |
| GLD        |       48 | 19.74%   | 110.99%            | -16.63% |     0.54 | 44.26%     | ok               |
| GOOGL      |       61 | 77.16%   | 151.19%            | -20.41% |     1.14 | 54.58%     | ok               |
| GRT-USD    |       89 | -14.60%  | -90.09%            | -56.53% |     0.05 | 41.57%     | ok               |
| GS         |       76 | -1.33%   | 182.63%            | -22.13% |     0.07 | 50.92%     | ok               |
| HD         |       69 | -2.89%   | -5.98%             | -17.69% |    -0    | 43.76%     | ok               |
| HON        |       95 | -30.77%  | 18.89%             | -30.77% |    -0.86 | 52.75%     | ok               |
| HYG        |       81 | -9.52%   | 3.76%              | -9.59%  |    -1.11 | 34.28%     | ok               |
| IBIT       |       32 | 28.42%   | -0.71%             | -18.95% |     0.65 | 30.32%     | ok               |
| IBM        |       72 | 20.67%   | 54.48%             | -25.31% |     0.48 | 50.92%     | ok               |
| ICP-USD    |       83 | -1.35%   | -76.95%            | -55.67% |     0.25 | 38.70%     | ok               |
| IEF        |       76 | -10.90%  | -0.75%             | -11.70% |    -1.54 | 32.78%     | ok               |
| IEMG       |       58 | -5.52%   | 74.47%             | -26.84% |    -0.12 | 43.59%     | ok               |
| INJ-USD    |       75 | -52.18%  | -73.85%            | -77.42% |    -0.49 | 37.93%     | ok               |
| INTC       |       70 | 55.82%   | 161.53%            | -60.60% |     0.62 | 49.25%     | ok               |
| INTU       |       65 | -12.74%  | -55.68%            | -43.77% |    -0.1  | 42.76%     | ok               |
| ITA        |       74 | -1.29%   | 93.91%             | -23.75% |     0.04 | 46.76%     | ok               |
| IWM        |       50 | 9.03%    | 50.35%             | -12.83% |     0.37 | 36.94%     | ok               |
| JNJ        |       71 | 6.64%    | 47.46%             | -17.51% |     0.29 | 50.58%     | ok               |
| JPM        |       77 | -20.02%  | 89.01%             | -33.43% |    -0.5  | 52.75%     | ok               |
| KO         |       51 | 27.92%   | 35.19%             | -8.07%  |     1    | 37.94%     | ok               |
| LDO-USD    |       75 | -1.11%   | -82.72%            | -58.32% |     0.27 | 38.89%     | ok               |
| LIN        |       70 | -2.47%   | 27.85%             | -21.53% |    -0.03 | 39.10%     | ok               |
| LINK-USD   |       70 | -13.55%  | -59.01%            | -50.48% |     0.1  | 41.57%     | ok               |
| LLY        |       69 | -11.15%  | 79.35%             | -53.34% |    -0.05 | 51.41%     | ok               |
| LRCX       |       80 | -8.76%   | 368.36%            | -63.56% |     0.06 | 46.26%     | ok               |
| LTC-USD    |       66 | -34.00%  | -56.12%            | -53.76% |    -0.29 | 48.47%     | ok               |
| MCD        |       77 | -3.77%   | -4.64%             | -18.81% |    -0.1  | 38.27%     | ok               |
| META       |       72 | -12.94%  | 54.07%             | -38.96% |    -0.08 | 51.08%     | ok               |
| MPC        |       71 | -13.74%  | 62.93%             | -44.76% |    -0.14 | 49.92%     | ok               |
| MRK        |       67 | -26.39%  | -4.12%             | -34.44% |    -0.6  | 47.09%     | ok               |
| MS         |       79 | -14.76%  | 151.30%            | -27.79% |    -0.3  | 47.75%     | ok               |
| MSFT       |       81 | -34.86%  | 0.22%              | -39.34% |    -0.93 | 48.59%     | ok               |
| MU         |       51 | 255.29%  | 1142.99%           | -68.76% |     1.32 | 59.40%     | ok               |
| NEAR-USD   |       87 | 4.42%    | -52.57%            | -59.86% |     0.3  | 42.34%     | ok               |
| NEM        |       76 | -26.06%  | 199.21%            | -38.49% |    -0.23 | 55.24%     | ok               |
| NFLX       |       64 | 23.03%   | 65.93%             | -21.09% |     0.55 | 54.41%     | ok               |
| NKE        |       91 | -37.92%  | -55.64%            | -55.35% |    -0.53 | 43.93%     | ok               |
| NOW        |       80 | 17.57%   | -30.88%            | -30.25% |     0.37 | 45.92%     | ok               |
| NVDA       |       74 | -27.33%  | 135.08%            | -45.02% |    -0.2  | 59.54%     | ok               |
| OP-USD     |       72 | 5.00%    | -93.92%            | -70.11% |     0.3  | 36.02%     | ok               |
| ORCL       |       72 | 49.01%   | 72.26%             | -29.47% |     0.6  | 53.58%     | ok               |
| OXY        |       65 | 0.13%    | -4.00%             | -30.85% |     0.12 | 43.43%     | ok               |
| PEP        |       85 | -9.64%   | -12.76%            | -21.35% |    -0.22 | 50.25%     | ok               |
| PEPE-USD   |       77 | 10.36%   | -83.61%            | -57.66% |     0.36 | 43.87%     | ok               |
| PFE        |       77 | -37.43%  | -8.55%             | -42.29% |    -1.16 | 36.61%     | ok               |
| PG         |       62 | -9.81%   | -2.29%             | -21.65% |    -0.33 | 41.43%     | ok               |
| PM         |       81 | 0.05%    | 98.05%             | -33.68% |     0.1  | 57.24%     | ok               |
| POL-USD    |       79 | 63.75%   | -82.97%            | -46.45% |     0.76 | 49.43%     | ok               |
| QCOM       |       77 | -18.79%  | 43.85%             | -57.69% |    -0.09 | 48.09%     | ok               |
| QQQ        |       62 | 20.20%   | 75.69%             | -12.88% |     0.57 | 46.42%     | ok               |
| RENDER-USD |       96 | -17.59%  | -57.28%            | -45.00% |     0.11 | 44.28%     | ok               |
| RTX        |       58 | 19.82%   | 105.07%            | -16.99% |     0.54 | 51.58%     | ok               |
| SBUX       |       65 | -25.37%  | 10.46%             | -30.74% |    -0.53 | 38.77%     | ok               |
| SCHW       |       74 | -21.97%  | 42.29%             | -30.41% |    -0.52 | 45.42%     | ok               |
| SHIB-USD   |       76 | -25.73%  | -77.33%            | -48.95% |    -0.1  | 52.30%     | ok               |
| SHY        |       50 | -2.16%   | 0.06%              | -2.85%  |    -0.74 | 35.44%     | ok               |
| SKY-USD    |       68 | -29.10%  | -0.90%             | -43.98% |    -0.38 | 40.80%     | ok               |
| SLB        |       75 | -30.05%  | 6.53%              | -54.95% |    -0.54 | 49.92%     | ok               |
| SLV        |       60 | 23.86%   | 209.16%            | -42.66% |     0.45 | 40.27%     | ok               |
| SMH        |       48 | 94.32%   | 242.36%            | -33.99% |     1.19 | 51.08%     | ok               |
| SNX-USD    |       63 | 17.10%   | -86.04%            | -32.91% |     0.4  | 40.42%     | ok               |
| SOL-USD    |       68 | -40.50%  | -60.52%            | -55.52% |    -0.19 | 59.96%     | ok               |
| SOXX       |       55 | 80.72%   | 210.50%            | -40.34% |     1.02 | 50.08%     | ok               |
| SPY        |       58 | 7.21%    | 55.68%             | -16.47% |     0.31 | 50.75%     | ok               |
| SUSHI-USD  |       90 | -75.60%  | -87.31%            | -81.22% |    -1.06 | 35.44%     | ok               |
| T          |       64 | 26.25%   | 35.49%             | -17.01% |     0.66 | 50.25%     | ok               |
| TGT        |       56 | -11.79%  | -5.47%             | -41.74% |    -0.16 | 38.60%     | ok               |
| TIA-USD    |       82 | -19.62%  | -92.37%            | -56.27% |     0.04 | 33.72%     | ok               |
| TLT        |       70 | -22.51%  | -8.71%             | -23.75% |    -1.66 | 32.28%     | ok               |
| TMO        |       57 | 15.63%   | -13.98%            | -16.83% |     0.41 | 48.42%     | ok               |
| TMUS       |       70 | 11.56%   | 15.34%             | -24.50% |     0.34 | 48.42%     | ok               |
| TRX-USD    |       70 | 2.00%    | 32.35%             | -22.90% |     0.14 | 48.66%     | ok               |
| TSLA       |       68 | 3.29%    | 96.59%             | -57.89% |     0.24 | 43.09%     | ok               |
| TXN        |       77 | -15.83%  | 79.73%             | -46.98% |    -0.1  | 53.41%     | ok               |
| UNH        |       76 | 24.03%   | -20.27%            | -27.74% |     0.46 | 51.75%     | ok               |
| UNI-USD    |       90 | -66.39%  | -78.45%            | -81.03% |    -0.68 | 41.19%     | ok               |
| UPS        |       66 | -35.08%  | -32.01%            | -40.62% |    -0.69 | 39.60%     | ok               |
| USO        |       68 | 2.80%    | 74.00%             | -43.35% |     0.17 | 34.44%     | ok               |
| VEA        |       58 | -0.98%   | 54.61%             | -17.93% |     0.01 | 44.09%     | ok               |
| VIXY       |       92 | -78.16%  | -61.39%            | -87.63% |    -0.94 | 31.61%     | ok               |
| VNQ        |       75 | -16.77%  | 14.65%             | -24.92% |    -0.7  | 37.60%     | ok               |
| VTI        |       66 | -0.72%   | 54.56%             | -18.77% |     0.04 | 52.08%     | ok               |
| VWO        |       76 | -13.41%  | 53.87%             | -25.20% |    -0.47 | 44.09%     | ok               |
| VZ         |       85 | -27.23%  | 11.46%             | -31.88% |    -0.93 | 38.44%     | ok               |
| WFC        |       84 | -20.42%  | 69.26%             | -30.87% |    -0.37 | 47.25%     | ok               |
| WIF-USD    |       72 | -35.63%  | -89.34%            | -50.40% |    -0.11 | 32.95%     | ok               |
| WMT        |       55 | 31.99%   | 122.64%            | -21.31% |     0.84 | 51.91%     | ok               |
| XBI        |       62 | -4.13%   | 52.86%             | -21.75% |    -0.02 | 39.43%     | ok               |
| XLB        |       70 | -14.85%  | 26.90%             | -26.57% |    -0.51 | 37.60%     | ok               |
| XLC        |       63 | 15.48%   | 48.16%             | -12.33% |     0.54 | 55.57%     | ok               |
| XLE        |       73 | -11.37%  | 37.77%             | -37.51% |    -0.22 | 46.76%     | ok               |
| XLF        |       74 | -11.34%  | 40.32%             | -23.61% |    -0.37 | 48.59%     | ok               |
| XLI        |       64 | 5.37%    | 57.80%             | -11.38% |     0.26 | 46.76%     | ok               |
| XLK        |       42 | 69.39%   | 90.02%             | -14.75% |     1.26 | 48.59%     | ok               |
| XLM-USD    |       71 | 6.52%    | -52.20%            | -45.72% |     0.29 | 45.79%     | ok               |
| XLP        |       72 | 5.69%    | 17.94%             | -10.28% |     0.35 | 42.93%     | ok               |
| XLU        |       69 | -6.29%   | 47.22%             | -18.15% |    -0.24 | 38.77%     | ok               |
| XLV        |       68 | -10.10%  | 9.23%              | -15.55% |    -0.48 | 36.61%     | ok               |
| XLY        |       74 | 0.76%    | 36.52%             | -14.01% |     0.09 | 44.59%     | ok               |
| XOM        |       58 | 2.44%    | 43.93%             | -20.29% |     0.14 | 36.27%     | ok               |
| XRP-USD    |       62 | -36.21%  | -52.17%            | -48.42% |    -0.36 | 35.82%     | ok               |
| YFI-USD    |       83 | -54.99%  | -74.57%            | -67.78% |    -0.82 | 40.61%     | ok               |
| ZEC-USD    |       69 | 43.83%   | 954.71%            | -46.93% |     0.56 | 36.40%     | ok               |

## AAPL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 21.65%   | 51.87%             | -21.71% |     0.5  |       67 | 53.08%     | ok               |
|          25 | 15.84%   | 51.87%             | -20.03% |     0.4  |       65 | 50.92%     | ok               |
|          15 | 15.76%   | 51.87%             | -23.86% |     0.39 |       74 | 60.40%     | ok               |
|          30 | 10.88%   | 51.87%             | -20.65% |     0.32 |       63 | 49.08%     | ok               |
|          35 | 5.80%    | 51.87%             | -22.04% |     0.22 |       63 | 46.92%     | ok               |

## AAVE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 5.38%    | -74.32%            | -46.87% |     0.27 |       38 | 26.05%     | ok               |
|          40 | -0.24%   | -74.32%            | -43.61% |     0.21 |       38 | 29.69%     | ok               |
|          35 | -24.98%  | -74.32%            | -51.96% |    -0.1  |       52 | 32.38%     | ok               |
|          50 | -29.70%  | -74.32%            | -47.78% |    -0.27 |       42 | 20.31%     | ok               |
|          15 | -61.79%  | -74.32%            | -66.23% |    -0.54 |       82 | 50.77%     | ok               |

## ABBV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 0.29%    | 32.29%             | -23.85% |     0.09 |       50 | 38.60%     | ok               |
|          40 | -12.20%  | 32.29%             | -26.61% |    -0.23 |       64 | 43.43%     | ok               |
|          35 | -13.45%  | 32.29%             | -27.83% |    -0.26 |       66 | 46.26%     | ok               |
|          30 | -15.69%  | 32.29%             | -30.55% |    -0.31 |       64 | 49.08%     | ok               |
|          45 | -14.93%  | 32.29%             | -29.59% |    -0.32 |       54 | 40.77%     | ok               |

## ADA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -83.79%  | -82.13%            | -91.37% |    -0.58 |       80 | 61.49%     | ok               |
|          20 | -83.80%  | -82.13%            | -91.89% |    -0.6  |       84 | 56.70%     | ok               |
|          50 | -78.67%  | -82.13%            | -86.05% |    -0.62 |       57 | 27.20%     | ok               |
|          45 | -80.95%  | -82.13%            | -88.09% |    -0.65 |       60 | 31.99%     | ok               |
|          25 | -84.95%  | -82.13%            | -91.94% |    -0.67 |       83 | 53.45%     | ok               |

## ADBE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 10.63%   | -65.44%            | -21.34% |     0.3  |       76 | 49.25%     | ok               |
|          40 | -3.65%   | -65.44%            | -20.88% |     0.05 |       72 | 42.26%     | ok               |
|          25 | -7.34%   | -65.44%            | -31.29% |     0.04 |       50 | 61.06%     | ok               |
|          15 | -17.23%  | -65.44%            | -31.86% |    -0.11 |       61 | 65.72%     | ok               |
|          20 | -18.85%  | -65.44%            | -34.42% |    -0.14 |       50 | 63.23%     | ok               |

## AGG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -6.61%   | 0.91%              | -10.16% |    -1.1  |       69 | 31.11%     | ok               |
|          20 | -7.69%   | 0.91%              | -10.67% |    -1.13 |       73 | 36.77%     | ok               |
|          45 | -5.75%   | 0.91%              | -7.89%  |    -1.16 |       52 | 20.47%     | ok               |
|          25 | -7.87%   | 0.91%              | -11.31% |    -1.2  |       73 | 35.11%     | ok               |
|          50 | -5.57%   | 0.91%              | -7.92%  |    -1.25 |       46 | 16.97%     | ok               |

## ALGO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -48.36%  | -74.73%            | -53.13% |    -0.53 |       86 | 37.93%     | ok               |
|          15 | -57.31%  | -74.73%            | -69.47% |    -0.57 |       82 | 49.62%     | ok               |
|          25 | -59.70%  | -74.73%            | -73.33% |    -0.68 |       88 | 45.02%     | ok               |
|          20 | -61.83%  | -74.73%            | -72.09% |    -0.7  |       86 | 47.51%     | ok               |
|          50 | -42.79%  | -74.73%            | -45.74% |    -0.74 |       40 | 16.67%     | ok               |

## AMAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -3.20%   | 250.66%            | -54.05% |     0.14 |       66 | 62.06%     | ok               |
|          30 | -18.98%  | 250.66%            | -57.21% |    -0.1  |       69 | 53.41%     | ok               |
|          20 | -24.90%  | 250.66%            | -60.16% |    -0.17 |       72 | 58.57%     | ok               |
|          35 | -24.75%  | 250.66%            | -55.26% |    -0.2  |       71 | 51.25%     | ok               |
|          50 | -22.85%  | 250.66%            | -48.72% |    -0.21 |       52 | 39.27%     | ok               |

## AMD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 6.53%    | 224.94%            | -47.17% |     0.28 |       56 | 38.44%     | ok               |
|          50 | 4.65%    | 224.94%            | -48.79% |     0.25 |       60 | 32.78%     | ok               |
|          35 | -7.05%   | 224.94%            | -54.57% |     0.14 |       62 | 40.43%     | ok               |
|          45 | -14.89%  | 224.94%            | -56.22% |     0.04 |       64 | 35.77%     | ok               |
|          30 | -19.31%  | 224.94%            | -59.88% |     0.02 |       63 | 42.93%     | ok               |

## AMGN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -14.22%  | 13.11%             | -26.64% |    -0.22 |       74 | 54.41%     | ok               |
|          15 | -17.25%  | 13.11%             | -27.92% |    -0.27 |       72 | 60.07%     | ok               |
|          35 | -16.68%  | 13.11%             | -31.23% |    -0.31 |       69 | 44.59%     | ok               |
|          30 | -19.45%  | 13.11%             | -34.14% |    -0.38 |       71 | 48.25%     | ok               |
|          25 | -23.02%  | 13.11%             | -33.41% |    -0.46 |       69 | 50.75%     | ok               |

## AMZN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -17.83%  | 57.68%             | -28.70% |    -0.52 |       50 | 29.78%     | ok               |
|          50 | -25.03%  | 57.68%             | -35.48% |    -0.88 |       48 | 24.13%     | ok               |
|          45 | -25.89%  | 57.68%             | -35.47% |    -0.89 |       50 | 26.96%     | ok               |
|          35 | -29.70%  | 57.68%             | -38.29% |    -0.91 |       62 | 32.95%     | ok               |
|          30 | -33.84%  | 57.68%             | -42.48% |    -0.99 |       74 | 38.27%     | ok               |

## APT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 49.35%   | -92.55%            | -46.73% |     0.71 |       44 | 20.69%     | ok               |
|          45 | 13.56%   | -92.55%            | -63.86% |     0.36 |       60 | 26.82%     | ok               |
|          40 | -8.26%   | -92.55%            | -63.33% |     0.15 |       66 | 32.38%     | ok               |
|          20 | -19.27%  | -92.55%            | -70.51% |     0.1  |       71 | 51.53%     | ok               |
|          35 | -14.84%  | -92.55%            | -64.45% |     0.1  |       70 | 37.93%     | ok               |

## ARB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 64.33%   | -88.39%            | -53.74% |     0.69 |       85 | 55.75%     | ok               |
|          40 | 45.76%   | -88.39%            | -47.60% |     0.62 |       50 | 30.27%     | ok               |
|          35 | 36.29%   | -88.39%            | -56.00% |     0.55 |       62 | 33.91%     | ok               |
|          20 | 35.88%   | -88.39%            | -60.40% |     0.54 |       75 | 50.19%     | ok               |
|          45 | 24.86%   | -88.39%            | -50.83% |     0.46 |       56 | 23.37%     | ok               |

## ARKK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -26.33%  | 68.07%             | -34.90% |    -0.32 |       92 | 50.42%     | ok               |
|          20 | -30.68%  | 68.07%             | -34.90% |    -0.44 |       87 | 45.76%     | ok               |
|          30 | -32.67%  | 68.07%             | -35.19% |    -0.57 |       81 | 38.94%     | ok               |
|          35 | -33.82%  | 68.07%             | -36.30% |    -0.63 |       80 | 36.61%     | ok               |
|          40 | -35.22%  | 68.07%             | -36.71% |    -0.71 |       72 | 31.78%     | ok               |

## ATOM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -64.00%  | -70.48%            | -70.34% |    -0.93 |       93 | 50.77%     | ok               |
|          15 | -69.37%  | -70.48%            | -72.76% |    -1.01 |       95 | 60.73%     | ok               |
|          30 | -66.75%  | -70.48%            | -72.89% |    -1.09 |       88 | 44.06%     | ok               |
|          45 | -59.16%  | -70.48%            | -64.98% |    -1.09 |       72 | 28.35%     | ok               |
|          35 | -65.28%  | -70.48%            | -69.84% |    -1.16 |       76 | 38.31%     | ok               |

## AVAX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 15.04%   | -81.52%            | -34.50% |     0.37 |       38 | 19.54%     | ok               |
|          15 | 2.48%    | -81.52%            | -52.46% |     0.27 |       61 | 52.11%     | ok               |
|          45 | 4.12%    | -81.52%            | -41.07% |     0.23 |       40 | 23.56%     | ok               |
|          40 | -10.35%  | -81.52%            | -47.98% |     0.05 |       46 | 26.63%     | ok               |
|          35 | -16.71%  | -81.52%            | -48.82% |    -0.01 |       60 | 31.99%     | ok               |

## AVGO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 29.90%   | 221.24%            | -35.76% |     0.48 |       60 | 45.76%     | ok               |
|          25 | 25.29%   | 221.24%            | -38.01% |     0.44 |       64 | 46.42%     | ok               |
|          35 | 21.07%   | 221.24%            | -36.19% |     0.4  |       70 | 43.09%     | ok               |
|          40 | 20.66%   | 221.24%            | -40.70% |     0.4  |       60 | 39.93%     | ok               |
|          50 | 14.69%   | 221.24%            | -35.84% |     0.34 |       62 | 33.78%     | ok               |

## BA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 25.12%   | 8.25%              | -13.34% |     0.65 |       44 | 31.78%     | ok               |
|          35 | 30.49%   | 8.25%              | -23.77% |     0.58 |       74 | 45.76%     | ok               |
|          40 | 11.54%   | 8.25%              | -23.87% |     0.32 |       52 | 39.43%     | ok               |
|          25 | 10.85%   | 8.25%              | -32.48% |     0.3  |       72 | 53.91%     | ok               |
|          30 | 7.64%    | 8.25%              | -30.56% |     0.25 |       69 | 50.42%     | ok               |

## BAC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -4.03%   | 70.49%             | -20.40% |    -0.07 |       60 | 34.61%     | ok               |
|          20 | -8.60%   | 70.49%             | -20.73% |    -0.13 |       80 | 50.92%     | ok               |
|          50 | -7.29%   | 70.49%             | -20.35% |    -0.19 |       58 | 31.61%     | ok               |
|          35 | -8.92%   | 70.49%             | -27.83% |    -0.2  |       72 | 42.60%     | ok               |
|          15 | -12.93%  | 70.49%             | -22.24% |    -0.23 |       82 | 55.24%     | ok               |

## BCH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -10.60%  | -49.21%            | -53.87% |     0.08 |       76 | 46.55%     | ok               |
|          20 | -24.62%  | -49.21%            | -54.50% |    -0.05 |       72 | 53.26%     | ok               |
|          40 | -24.35%  | -49.21%            | -60.69% |    -0.14 |       63 | 39.46%     | ok               |
|          15 | -33.24%  | -49.21%            | -60.61% |    -0.15 |       81 | 57.85%     | ok               |
|          25 | -31.06%  | -49.21%            | -59.80% |    -0.16 |       72 | 48.85%     | ok               |

## BITO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 14.67%   | -52.17%            | -32.29% |     0.34 |       54 | 25.46%     | ok               |
|          30 | 1.25%    | -52.17%            | -42.82% |     0.19 |       78 | 40.10%     | ok               |
|          15 | -5.11%   | -52.17%            | -48.38% |     0.15 |       87 | 48.92%     | ok               |
|          25 | -6.76%   | -52.17%            | -41.73% |     0.1  |       82 | 43.09%     | ok               |
|          45 | -4.37%   | -52.17%            | -43.53% |     0.1  |       58 | 28.45%     | ok               |

## BLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -0.36%   | 31.58%             | -14.91% |     0.06 |       80 | 38.44%     | ok               |
|          40 | -1.71%   | 31.58%             | -16.69% |     0.01 |       70 | 34.28%     | ok               |
|          20 | -5.29%   | 31.58%             | -18.58% |    -0.08 |       77 | 46.76%     | ok               |
|          30 | -6.68%   | 31.58%             | -21.47% |    -0.13 |       75 | 42.26%     | ok               |
|          25 | -7.62%   | 31.58%             | -20.51% |    -0.15 |       75 | 44.59%     | ok               |

## BND Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.42%   | 0.94%              | -9.05%  |    -0.94 |       65 | 38.27%     | ok               |
|          25 | -6.87%   | 0.94%              | -10.14% |    -1.05 |       67 | 36.11%     | ok               |
|          30 | -7.32%   | 0.94%              | -9.89%  |    -1.18 |       65 | 32.28%     | ok               |
|          15 | -8.63%   | 0.94%              | -10.58% |    -1.24 |       75 | 41.10%     | ok               |
|          45 | -7.56%   | 0.94%              | -9.57%  |    -1.47 |       50 | 21.96%     | ok               |

## BONK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 170.78%  | -83.01%            | -35.57% |     1.24 |       48 | 22.41%     | ok               |
|          25 | 170.13%  | -83.01%            | -46.61% |     1.04 |       65 | 48.08%     | ok               |
|          20 | 154.87%  | -83.01%            | -54.25% |     0.99 |       66 | 52.68%     | ok               |
|          15 | 146.56%  | -83.01%            | -62.48% |     0.94 |       68 | 57.09%     | ok               |
|          45 | 85.63%   | -83.01%            | -42.36% |     0.84 |       56 | 27.20%     | ok               |

## BTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 51.83%   | -29.87%            | -14.50% |     0.95 |       44 | 34.10%     | ok               |
|          45 | 41.09%   | -29.87%            | -15.18% |     0.81 |       44 | 30.65%     | ok               |
|          35 | 36.01%   | -29.87%            | -22.12% |     0.7  |       68 | 41.00%     | ok               |
|          30 | 17.30%   | -29.87%            | -21.75% |     0.41 |       70 | 47.51%     | ok               |
|          50 | 14.18%   | -29.87%            | -16.15% |     0.4  |       42 | 25.29%     | ok               |

## C Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -7.75%   | 164.93%            | -22.28% |    -0.15 |       68 | 35.27%     | ok               |
|          25 | -21.19%  | 164.93%            | -34.18% |    -0.37 |       75 | 52.58%     | ok               |
|          45 | -16.57%  | 164.93%            | -30.30% |    -0.38 |       82 | 39.77%     | ok               |
|          15 | -23.20%  | 164.93%            | -35.02% |    -0.38 |       76 | 59.23%     | ok               |
|          20 | -23.83%  | 164.93%            | -35.56% |    -0.42 |       83 | 55.57%     | ok               |

## CAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 35.10%   | 223.35%            | -21.02% |     0.63 |       72 | 56.91%     | ok               |
|          25 | 35.22%   | 223.35%            | -26.37% |     0.63 |       68 | 59.73%     | ok               |
|          20 | 32.48%   | 223.35%            | -25.65% |     0.59 |       78 | 63.06%     | ok               |
|          45 | 25.70%   | 223.35%            | -27.12% |     0.53 |       54 | 45.76%     | ok               |
|          35 | 23.16%   | 223.35%            | -27.72% |     0.48 |       70 | 50.75%     | ok               |

## CL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 15.81%   | 11.26%             | -12.98% |     0.64 |       44 | 32.28%     | ok               |
|          30 | 17.02%   | 11.26%             | -14.32% |     0.58 |       60 | 48.42%     | ok               |
|          45 | 10.52%   | 11.26%             | -13.51% |     0.44 |       48 | 35.27%     | ok               |
|          35 | 9.82%    | 11.26%             | -13.83% |     0.38 |       64 | 44.59%     | ok               |
|          40 | 6.64%    | 11.26%             | -12.70% |     0.3  |       58 | 39.27%     | ok               |

## CMCSA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -35.24%  | -41.81%            | -49.03% |    -0.77 |       85 | 58.74%     | ok               |
|          30 | -36.24%  | -41.81%            | -40.02% |    -0.9  |       80 | 44.59%     | ok               |
|          25 | -41.75%  | -41.81%            | -45.20% |    -1.07 |       87 | 49.92%     | ok               |
|          50 | -29.51%  | -41.81%            | -33.68% |    -1.08 |       50 | 17.14%     | ok               |
|          20 | -43.43%  | -41.81%            | -47.23% |    -1.1  |       91 | 55.07%     | ok               |

## COMP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -3.83%   | -77.39%            | -38.71% |     0.15 |       46 | 20.69%     | ok               |
|          30 | -36.73%  | -77.39%            | -58.43% |    -0.21 |       89 | 45.02%     | ok               |
|          25 | -39.96%  | -77.39%            | -60.58% |    -0.22 |       89 | 50.19%     | ok               |
|          15 | -47.94%  | -77.39%            | -65.55% |    -0.31 |      103 | 61.69%     | ok               |
|          40 | -41.16%  | -77.39%            | -47.52% |    -0.37 |       74 | 33.14%     | ok               |

## COP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -9.77%   | 3.95%              | -34.21% |    -0.15 |       48 | 27.29%     | ok               |
|          45 | -17.04%  | 3.95%              | -40.57% |    -0.33 |       60 | 30.28%     | ok               |
|          35 | -26.56%  | 3.95%              | -43.58% |    -0.52 |       77 | 37.44%     | ok               |
|          30 | -27.06%  | 3.95%              | -43.77% |    -0.52 |       75 | 40.60%     | ok               |
|          40 | -28.99%  | 3.95%              | -46.34% |    -0.65 |       70 | 33.11%     | ok               |

## COST Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 17.43%   | 42.45%             | -24.73% |     0.53 |       61 | 50.42%     | ok               |
|          20 | 16.82%   | 42.45%             | -24.32% |     0.51 |       62 | 52.91%     | ok               |
|          35 | 11.83%   | 42.45%             | -26.58% |     0.41 |       54 | 43.76%     | ok               |
|          30 | 5.55%    | 42.45%             | -29.73% |     0.23 |       62 | 46.92%     | ok               |
|          40 | 4.97%    | 42.45%             | -28.41% |     0.22 |       56 | 40.77%     | ok               |

## CRM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -30.33%  | -40.55%            | -38.20% |    -0.44 |       90 | 55.24%     | ok               |
|          35 | -24.86%  | -40.55%            | -36.72% |    -0.47 |       62 | 38.94%     | ok               |
|          40 | -30.31%  | -40.55%            | -41.30% |    -0.68 |       68 | 34.94%     | ok               |
|          30 | -35.46%  | -40.55%            | -41.46% |    -0.72 |       65 | 43.76%     | ok               |
|          20 | -40.61%  | -40.55%            | -42.88% |    -0.76 |       78 | 48.92%     | ok               |

## CRV-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 19.56%   | -71.07%            | -37.78% |     0.41 |       66 | 29.50%     | ok               |
|          50 | 12.00%   | -71.07%            | -29.30% |     0.33 |       40 | 16.67%     | ok               |
|          40 | 8.36%    | -71.07%            | -38.86% |     0.3  |       56 | 25.29%     | ok               |
|          45 | 6.52%    | -71.07%            | -42.29% |     0.27 |       52 | 19.54%     | ok               |
|          30 | -5.05%   | -71.07%            | -39.89% |     0.18 |       64 | 34.10%     | ok               |

## CSCO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 28.18%   | 132.17%            | -19.34% |     0.63 |       58 | 38.94%     | ok               |
|          45 | 26.57%   | 132.17%            | -19.34% |     0.59 |       51 | 41.43%     | ok               |
|          25 | 23.78%   | 132.17%            | -23.28% |     0.52 |       63 | 51.75%     | ok               |
|          30 | 23.21%   | 132.17%            | -21.79% |     0.51 |       59 | 49.75%     | ok               |
|          35 | 20.89%   | 132.17%            | -23.68% |     0.47 |       51 | 47.42%     | ok               |

## CVX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -12.04%  | 26.96%             | -23.25% |    -0.26 |       72 | 44.09%     | ok               |
|          20 | -15.02%  | 26.96%             | -25.18% |    -0.35 |       72 | 45.42%     | ok               |
|          30 | -16.65%  | 26.96%             | -26.75% |    -0.43 |       71 | 41.60%     | ok               |
|          35 | -16.40%  | 26.96%             | -27.83% |    -0.43 |       71 | 38.60%     | ok               |
|          45 | -15.88%  | 26.96%             | -28.32% |    -0.47 |       61 | 30.12%     | ok               |

## DASH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 110.90%  | 2.34%              | -31.38% |     0.88 |       42 | 17.24%     | ok               |
|          40 | 57.71%   | 2.34%              | -34.44% |     0.64 |       46 | 23.75%     | ok               |
|          45 | 52.31%   | 2.34%              | -39.58% |     0.61 |       46 | 19.54%     | ok               |
|          25 | -42.64%  | 2.34%              | -64.14% |    -0.01 |       71 | 34.48%     | ok               |
|          35 | -42.46%  | 2.34%              | -63.23% |    -0.02 |       71 | 28.16%     | ok               |

## DBC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -9.68%   | 27.40%             | -23.38% |    -0.31 |       60 | 31.61%     | ok               |
|          50 | -8.54%   | 27.40%             | -19.91% |    -0.32 |       42 | 21.13%     | ok               |
|          15 | -10.79%  | 27.40%             | -27.30% |    -0.34 |       67 | 37.10%     | ok               |
|          45 | -9.90%   | 27.40%             | -21.08% |    -0.35 |       54 | 24.46%     | ok               |
|          30 | -12.57%  | 27.40%             | -25.35% |    -0.43 |       58 | 32.78%     | ok               |

## DE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -7.26%   | 48.52%             | -29.90% |    -0.06 |       74 | 51.25%     | ok               |
|          30 | -8.25%   | 48.52%             | -25.29% |    -0.09 |       72 | 45.59%     | ok               |
|          25 | -9.62%   | 48.52%             | -27.71% |    -0.12 |       76 | 48.42%     | ok               |
|          50 | -9.15%   | 48.52%             | -23.24% |    -0.18 |       68 | 30.78%     | ok               |
|          45 | -11.01%  | 48.52%             | -26.90% |    -0.21 |       68 | 35.27%     | ok               |

## DIA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -0.36%   | 36.78%             | -13.15% |     0.02 |       60 | 43.76%     | ok               |
|          25 | -0.90%   | 36.78%             | -11.28% |    -0.01 |       60 | 47.09%     | ok               |
|          30 | -2.42%   | 36.78%             | -12.94% |    -0.09 |       60 | 45.92%     | ok               |
|          20 | -4.29%   | 36.78%             | -13.85% |    -0.18 |       64 | 49.42%     | ok               |
|          40 | -4.42%   | 36.78%             | -15.06% |    -0.22 |       66 | 40.93%     | ok               |

## DIS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 37.56%   | 8.45%              | -14.24% |     0.91 |       50 | 31.11%     | ok               |
|          45 | 8.71%    | 8.45%              | -16.52% |     0.28 |       51 | 34.61%     | ok               |
|          40 | 7.01%    | 8.45%              | -23.29% |     0.24 |       63 | 39.93%     | ok               |
|          35 | 0.11%    | 8.45%              | -23.26% |     0.11 |       71 | 45.59%     | ok               |
|          15 | -2.08%   | 8.45%              | -27.62% |     0.08 |       86 | 59.23%     | ok               |

## DOGE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 14.54%   | -74.21%            | -57.89% |     0.4  |       81 | 64.75%     | ok               |
|          20 | 1.81%    | -74.21%            | -55.83% |     0.29 |       84 | 60.54%     | ok               |
|          25 | -0.84%   | -74.21%            | -53.72% |     0.26 |       72 | 54.98%     | ok               |
|          30 | -16.53%  | -74.21%            | -60.95% |     0.09 |       75 | 49.81%     | ok               |
|          35 | -45.34%  | -74.21%            | -63.16% |    -0.38 |       72 | 43.10%     | ok               |

## DOT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -19.10%  | -84.95%            | -44.94% |    -0.11 |       56 | 26.25%     | ok               |
|          45 | -25.17%  | -84.95%            | -50.75% |    -0.18 |       52 | 31.03%     | ok               |
|          40 | -33.33%  | -84.95%            | -50.61% |    -0.28 |       56 | 34.48%     | ok               |
|          35 | -44.41%  | -84.95%            | -61.39% |    -0.32 |       80 | 41.57%     | ok               |
|          30 | -47.22%  | -84.95%            | -61.09% |    -0.35 |       90 | 48.08%     | ok               |

## DXY-INDEX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -4.04%   | -3.24%             | -9.98%  |    -0.45 |       68 | 58.35%     | ok               |
|          15 | -5.40%   | -3.24%             | -11.57% |    -0.49 |       90 | 75.70%     | ok               |
|          40 | -4.06%   | -3.24%             | -7.30%  |    -0.51 |       68 | 47.51%     | ok               |
|          50 | -3.67%   | -3.24%             | -6.06%  |    -0.59 |       44 | 28.85%     | ok               |
|          35 | -4.98%   | -3.24%             | -10.12% |    -0.6  |       71 | 53.58%     | ok               |

## EEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -2.91%   | 81.74%             | -15.88% |    -0.04 |       50 | 36.11%     | ok               |
|          45 | -4.62%   | 81.74%             | -17.36% |    -0.11 |       52 | 37.60%     | ok               |
|          40 | -4.96%   | 81.74%             | -19.52% |    -0.11 |       64 | 39.77%     | ok               |
|          35 | -5.62%   | 81.74%             | -23.88% |    -0.12 |       66 | 41.76%     | ok               |
|          30 | -9.40%   | 81.74%             | -25.67% |    -0.25 |       64 | 43.43%     | ok               |

## EFA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -2.11%   | 40.74%             | -11.58% |    -0.02 |       60 | 51.91%     | ok               |
|          20 | -8.85%   | 40.74%             | -13.20% |    -0.3  |       65 | 48.92%     | ok               |
|          30 | -8.33%   | 40.74%             | -13.87% |    -0.3  |       58 | 43.93%     | ok               |
|          40 | -9.72%   | 40.74%             | -15.73% |    -0.39 |       62 | 40.10%     | ok               |
|          50 | -9.07%   | 40.74%             | -17.56% |    -0.4  |       54 | 36.27%     | ok               |

## EOG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -20.79%  | 19.58%             | -40.21% |    -0.52 |       58 | 29.62%     | ok               |
|          45 | -22.86%  | 19.58%             | -39.32% |    -0.56 |       56 | 32.78%     | ok               |
|          30 | -28.94%  | 19.58%             | -48.13% |    -0.66 |       81 | 46.92%     | ok               |
|          40 | -27.86%  | 19.58%             | -42.91% |    -0.71 |       64 | 36.27%     | ok               |
|          35 | -29.30%  | 19.58%             | -45.93% |    -0.72 |       79 | 41.76%     | ok               |

## ETC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -7.93%   | -71.21%            | -27.89% |    -0.02 |       28 | 17.05%     | ok               |
|          35 | -15.03%  | -71.21%            | -42.62% |    -0.11 |       44 | 27.01%     | ok               |
|          45 | -16.07%  | -71.21%            | -35.44% |    -0.17 |       26 | 18.97%     | ok               |
|          40 | -21.04%  | -71.21%            | -40.48% |    -0.26 |       42 | 22.80%     | ok               |
|          30 | -35.69%  | -71.21%            | -48.16% |    -0.51 |       64 | 31.23%     | ok               |

## ETH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 157.31%  | -45.34%            | -30.11% |     1.28 |       60 | 44.83%     | ok               |
|          30 | 138.57%  | -45.34%            | -32.89% |     1.15 |       64 | 52.87%     | ok               |
|          40 | 62.72%   | -45.34%            | -33.11% |     0.8  |       56 | 37.36%     | ok               |
|          45 | 34.50%   | -45.34%            | -34.50% |     0.57 |       52 | 33.33%     | ok               |
|          25 | 26.92%   | -45.34%            | -40.90% |     0.48 |       69 | 58.62%     | ok               |

## EWJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -17.54%  | 42.32%             | -30.73% |    -0.56 |       64 | 41.26%     | ok               |
|          20 | -18.94%  | 42.32%             | -31.32% |    -0.59 |       60 | 43.26%     | ok               |
|          25 | -21.28%  | 42.32%             | -31.18% |    -0.69 |       60 | 42.26%     | ok               |
|          35 | -21.49%  | 42.32%             | -32.54% |    -0.72 |       70 | 39.60%     | ok               |
|          15 | -24.30%  | 42.32%             | -32.24% |    -0.75 |       74 | 46.42%     | ok               |

## FCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -7.45%   | 83.73%             | -26.57% |     0    |       56 | 29.62%     | ok               |
|          45 | -12.11%  | 83.73%             | -33.82% |    -0.06 |       56 | 33.94%     | ok               |
|          40 | -25.21%  | 83.73%             | -44.23% |    -0.3  |       66 | 38.94%     | ok               |
|          30 | -36.27%  | 83.73%             | -48.09% |    -0.49 |       71 | 45.92%     | ok               |
|          35 | -37.18%  | 83.73%             | -51.29% |    -0.53 |       73 | 43.76%     | ok               |

## FET-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 62.34%   | -83.91%            | -57.24% |     0.68 |       86 | 48.85%     | ok               |
|          15 | 9.12%    | -83.91%            | -59.58% |     0.39 |       88 | 52.11%     | ok               |
|          25 | 4.65%    | -83.91%            | -57.82% |     0.33 |       85 | 41.76%     | ok               |
|          30 | -5.42%   | -83.91%            | -47.67% |     0.23 |       71 | 37.55%     | ok               |
|          45 | -19.33%  | -83.91%            | -45.02% |    -0.06 |       50 | 18.20%     | ok               |

## FIL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -6.35%   | -84.73%            | -39.40% |     0.09 |       48 | 23.37%     | ok               |
|          35 | -29.36%  | -84.73%            | -45.85% |    -0.25 |       58 | 27.59%     | ok               |
|          30 | -33.21%  | -84.73%            | -48.33% |    -0.29 |       70 | 32.95%     | ok               |
|          45 | -27.58%  | -84.73%            | -43.98% |    -0.29 |       44 | 17.62%     | ok               |
|          50 | -26.52%  | -84.73%            | -44.97% |    -0.32 |       38 | 13.03%     | ok               |

## FXI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -12.50%  | 58.80%             | -22.99% |    -0.24 |       50 | 29.28%     | ok               |
|          30 | -13.00%  | 58.80%             | -24.33% |    -0.26 |       50 | 28.12%     | ok               |
|          15 | -13.93%  | 58.80%             | -21.68% |    -0.26 |       54 | 32.78%     | ok               |
|          50 | -12.31%  | 58.80%             | -24.42% |    -0.27 |       42 | 20.13%     | ok               |
|          20 | -15.47%  | 58.80%             | -24.94% |    -0.32 |       56 | 30.62%     | ok               |

## GDX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 12.73%   | 202.05%            | -31.87% |     0.33 |       64 | 43.09%     | ok               |
|          20 | 9.57%    | 202.05%            | -35.59% |     0.28 |       73 | 53.24%     | ok               |
|          35 | 5.22%    | 202.05%            | -32.37% |     0.21 |       68 | 45.59%     | ok               |
|          30 | -0.20%   | 202.05%            | -34.99% |     0.13 |       62 | 48.59%     | ok               |
|          25 | -0.91%   | 202.05%            | -36.75% |     0.12 |       63 | 50.08%     | ok               |

## GDXJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -17.01%  | 225.33%            | -45.05% |    -0.07 |       67 | 53.41%     | ok               |
|          50 | -16.57%  | 225.33%            | -42.42% |    -0.15 |       56 | 37.44%     | ok               |
|          30 | -27.50%  | 225.33%            | -44.93% |    -0.31 |       68 | 46.42%     | ok               |
|          45 | -27.74%  | 225.33%            | -42.71% |    -0.36 |       60 | 39.77%     | ok               |
|          25 | -32.38%  | 225.33%            | -47.26% |    -0.36 |       73 | 49.75%     | ok               |

## GE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 31.33%   | 230.01%            | -22.29% |     0.63 |       66 | 38.60%     | ok               |
|          45 | 21.42%   | 230.01%            | -25.68% |     0.47 |       74 | 41.43%     | ok               |
|          20 | 20.52%   | 230.01%            | -26.63% |     0.44 |       69 | 55.24%     | ok               |
|          35 | 15.12%   | 230.01%            | -27.11% |     0.37 |       80 | 46.76%     | ok               |
|          15 | 15.38%   | 230.01%            | -28.62% |     0.36 |       68 | 57.57%     | ok               |

## GLD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 25.72%   | 110.99%            | -14.61% |     0.66 |       46 | 45.42%     | ok               |
|          20 | 23.85%   | 110.99%            | -14.61% |     0.62 |       48 | 46.76%     | ok               |
|          30 | 19.74%   | 110.99%            | -16.63% |     0.54 |       48 | 44.26%     | ok               |
|          15 | 16.26%   | 110.99%            | -17.54% |     0.44 |       50 | 50.92%     | ok               |
|          35 | 13.89%   | 110.99%            | -17.29% |     0.42 |       50 | 43.59%     | ok               |

## GOOGL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 80.02%   | 151.19%            | -19.12% |     1.2  |       63 | 49.92%     | ok               |
|          25 | 80.08%   | 151.19%            | -19.76% |     1.16 |       57 | 56.41%     | ok               |
|          30 | 77.16%   | 151.19%            | -20.41% |     1.14 |       61 | 54.58%     | ok               |
|          15 | 69.94%   | 151.19%            | -13.59% |     1.02 |       69 | 64.06%     | ok               |
|          20 | 66.48%   | 151.19%            | -20.57% |     1.01 |       68 | 58.74%     | ok               |

## GRT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 46.24%   | -90.09%            | -30.00% |     0.71 |       40 | 21.07%     | ok               |
|          15 | 7.53%    | -90.09%            | -49.67% |     0.33 |       77 | 60.34%     | ok               |
|          45 | 11.31%   | -90.09%            | -48.76% |     0.32 |       48 | 26.25%     | ok               |
|          20 | 6.93%    | -90.09%            | -46.47% |     0.31 |       85 | 55.36%     | ok               |
|          40 | 6.56%    | -90.09%            | -48.35% |     0.27 |       50 | 29.50%     | ok               |

## GS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 27.87%   | 182.63%            | -20.56% |     0.57 |       74 | 59.73%     | ok               |
|          20 | 10.43%   | 182.63%            | -23.19% |     0.3  |       74 | 55.74%     | ok               |
|          25 | 4.84%    | 182.63%            | -23.32% |     0.2  |       74 | 53.24%     | ok               |
|          40 | 0.05%    | 182.63%            | -17.88% |     0.09 |       72 | 44.26%     | ok               |
|          30 | -1.33%   | 182.63%            | -22.13% |     0.07 |       76 | 50.92%     | ok               |

## HD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -2.89%   | -5.98%             | -17.69% |    -0    |       69 | 43.76%     | ok               |
|          25 | -3.65%   | -5.98%             | -18.51% |    -0.02 |       68 | 45.76%     | ok               |
|          40 | -8.62%   | -5.98%             | -19.63% |    -0.21 |       80 | 33.94%     | ok               |
|          35 | -11.93%  | -5.98%             | -22.98% |    -0.28 |       76 | 40.10%     | ok               |
|          45 | -12.08%  | -5.98%             | -21.41% |    -0.35 |       62 | 28.79%     | ok               |

## HON Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -17.09%  | 18.89%             | -23.31% |    -0.53 |       74 | 32.11%     | ok               |
|          45 | -19.07%  | 18.89%             | -22.37% |    -0.56 |       78 | 37.27%     | ok               |
|          40 | -27.04%  | 18.89%             | -27.04% |    -0.79 |       80 | 41.60%     | ok               |
|          35 | -28.43%  | 18.89%             | -28.43% |    -0.81 |       95 | 47.92%     | ok               |
|          30 | -30.77%  | 18.89%             | -30.77% |    -0.86 |       95 | 52.75%     | ok               |

## HYG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -7.92%   | 3.76%              | -7.92%  |    -0.96 |       70 | 29.45%     | ok               |
|          15 | -9.71%   | 3.76%              | -10.06% |    -1.05 |       88 | 41.43%     | ok               |
|          20 | -9.69%   | 3.76%              | -10.29% |    -1.08 |       86 | 39.10%     | ok               |
|          45 | -8.60%   | 3.76%              | -8.60%  |    -1.08 |       66 | 26.29%     | ok               |
|          30 | -9.52%   | 3.76%              | -9.59%  |    -1.11 |       81 | 34.28%     | ok               |

## IBIT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 55.86%   | -0.71%             | -19.20% |     0.98 |       38 | 38.14%     | ok               |
|          50 | 43.90%   | -0.71%             | -17.37% |     0.95 |       20 | 22.49%     | ok               |
|          45 | 35.91%   | -0.71%             | -17.37% |     0.8  |       22 | 23.23%     | ok               |
|          40 | 34.56%   | -0.71%             | -17.78% |     0.78 |       24 | 24.69%     | ok               |
|          30 | 28.42%   | -0.71%             | -18.95% |     0.65 |       32 | 30.32%     | ok               |

## IBM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 25.06%   | 54.48%             | -28.20% |     0.51 |       87 | 62.73%     | ok               |
|          30 | 20.67%   | 54.48%             | -25.31% |     0.48 |       72 | 50.92%     | ok               |
|          35 | 18.25%   | 54.48%             | -25.15% |     0.44 |       68 | 46.59%     | ok               |
|          45 | 15.66%   | 54.48%             | -18.33% |     0.41 |       54 | 37.10%     | ok               |
|          40 | 12.22%   | 54.48%             | -24.66% |     0.34 |       64 | 41.10%     | ok               |

## ICP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 21.03%   | -76.95%            | -32.85% |     0.42 |       58 | 27.01%     | ok               |
|          35 | 9.43%    | -76.95%            | -45.97% |     0.32 |       68 | 32.38%     | ok               |
|          50 | 5.42%    | -76.95%            | -43.65% |     0.25 |       40 | 16.86%     | ok               |
|          30 | -1.35%   | -76.95%            | -55.67% |     0.25 |       83 | 38.70%     | ok               |
|          45 | -8.28%   | -76.95%            | -40.57% |     0.09 |       58 | 21.07%     | ok               |

## IEF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.92%   | -0.75%             | -9.79%  |    -0.82 |       70 | 42.26%     | ok               |
|          15 | -7.48%   | -0.75%             | -10.52% |    -0.88 |       69 | 43.76%     | ok               |
|          40 | -8.39%   | -0.75%             | -9.67%  |    -1.31 |       60 | 24.79%     | ok               |
|          45 | -8.07%   | -0.75%             | -9.73%  |    -1.33 |       50 | 22.80%     | ok               |
|          25 | -10.50%  | -0.75%             | -11.19% |    -1.34 |       76 | 39.43%     | ok               |

## IEMG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.10%   | 74.47%             | -13.91% |     0.05 |       52 | 34.44%     | ok               |
|          35 | -0.32%   | 74.47%             | -22.13% |     0.05 |       63 | 42.60%     | ok               |
|          45 | -0.91%   | 74.47%             | -14.92% |     0.02 |       48 | 36.94%     | ok               |
|          40 | -2.44%   | 74.47%             | -18.43% |    -0.03 |       60 | 39.93%     | ok               |
|          25 | -4.72%   | 74.47%             | -25.58% |    -0.09 |       59 | 45.42%     | ok               |

## INJ-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -12.91%  | -73.85%            | -55.31% |     0.02 |       44 | 22.41%     | ok               |
|          35 | -20.16%  | -73.85%            | -61.19% |    -0.01 |       60 | 32.38%     | ok               |
|          50 | -22.38%  | -73.85%            | -51.00% |    -0.14 |       48 | 19.35%     | ok               |
|          40 | -28.35%  | -73.85%            | -58.05% |    -0.17 |       50 | 28.54%     | ok               |
|          20 | -55.95%  | -73.85%            | -81.53% |    -0.45 |       82 | 47.13%     | ok               |

## INTC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 76.11%   | 161.53%            | -49.32% |     0.74 |       60 | 34.28%     | ok               |
|          15 | 82.95%   | 161.53%            | -53.65% |     0.74 |       84 | 61.23%     | ok               |
|          25 | 75.50%   | 161.53%            | -56.41% |     0.72 |       75 | 51.58%     | ok               |
|          40 | 70.33%   | 161.53%            | -55.86% |     0.7  |       68 | 38.60%     | ok               |
|          20 | 72.70%   | 161.53%            | -52.47% |     0.7  |       82 | 56.57%     | ok               |

## INTU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 3.04%    | -55.68%            | -42.60% |     0.17 |       71 | 29.12%     | ok               |
|          45 | -0.48%   | -55.68%            | -44.44% |     0.11 |       69 | 33.28%     | ok               |
|          40 | -7.99%   | -55.68%            | -48.15% |    -0.03 |       71 | 35.94%     | ok               |
|          25 | -9.59%   | -55.68%            | -42.24% |    -0.04 |       64 | 45.42%     | ok               |
|          15 | -10.66%  | -55.68%            | -46.90% |    -0.05 |       79 | 50.92%     | ok               |

## ITA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 2.85%    | 93.91%             | -21.48% |     0.16 |       76 | 36.77%     | ok               |
|          15 | -1.90%   | 93.91%             | -28.17% |     0.04 |       88 | 58.74%     | ok               |
|          30 | -1.29%   | 93.91%             | -23.75% |     0.04 |       74 | 46.76%     | ok               |
|          35 | -3.84%   | 93.91%             | -23.16% |    -0.05 |       78 | 44.93%     | ok               |
|          40 | -4.94%   | 93.91%             | -20.58% |    -0.09 |       80 | 41.43%     | ok               |

## IWM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 9.03%    | 50.35%             | -12.83% |     0.37 |       50 | 36.94%     | ok               |
|          25 | 9.14%    | 50.35%             | -14.87% |     0.37 |       52 | 38.10%     | ok               |
|          40 | 6.82%    | 50.35%             | -14.38% |     0.32 |       44 | 32.28%     | ok               |
|          35 | 6.57%    | 50.35%             | -14.41% |     0.3  |       50 | 34.61%     | ok               |
|          20 | 4.84%    | 50.35%             | -15.39% |     0.23 |       62 | 39.10%     | ok               |

## JNJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 21.36%   | 47.46%             | -10.57% |     0.9  |       56 | 37.10%     | ok               |
|          15 | 17.71%   | 47.46%             | -18.02% |     0.61 |       67 | 58.07%     | ok               |
|          45 | 12.26%   | 47.46%             | -13.35% |     0.53 |       58 | 42.26%     | ok               |
|          20 | 13.26%   | 47.46%             | -17.61% |     0.5  |       73 | 54.58%     | ok               |
|          40 | 9.81%    | 47.46%             | -14.77% |     0.42 |       64 | 46.42%     | ok               |

## JPM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 17.60%   | 89.01%             | -15.90% |     0.61 |       54 | 40.10%     | ok               |
|          45 | 7.38%    | 89.01%             | -21.91% |     0.29 |       56 | 43.26%     | ok               |
|          40 | -6.80%   | 89.01%             | -28.47% |    -0.13 |       68 | 45.76%     | ok               |
|          20 | -13.53%  | 89.01%             | -33.59% |    -0.23 |       88 | 57.07%     | ok               |
|          35 | -12.01%  | 89.01%             | -27.43% |    -0.27 |       74 | 49.42%     | ok               |

## KO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 27.92%   | 35.19%             | -8.07%  |     1    |       51 | 37.94%     | ok               |
|          35 | 24.00%   | 35.19%             | -8.07%  |     0.89 |       54 | 36.61%     | ok               |
|          40 | 21.41%   | 35.19%             | -9.28%  |     0.86 |       56 | 33.44%     | ok               |
|          25 | 21.82%   | 35.19%             | -9.37%  |     0.8  |       59 | 40.77%     | ok               |
|          50 | 14.81%   | 35.19%             | -11.40% |     0.68 |       36 | 26.79%     | ok               |

## LDO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 19.66%   | -82.72%            | -44.79% |     0.45 |       86 | 52.68%     | ok               |
|          20 | 7.39%    | -82.72%            | -43.71% |     0.36 |       88 | 48.08%     | ok               |
|          30 | -1.11%   | -82.72%            | -58.32% |     0.27 |       75 | 38.89%     | ok               |
|          25 | -17.48%  | -82.72%            | -54.80% |     0.14 |       84 | 44.25%     | ok               |
|          50 | -4.19%   | -82.72%            | -48.77% |     0.09 |       46 | 16.28%     | ok               |

## LIN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 3.11%    | 27.85%             | -23.70% |     0.16 |       65 | 49.92%     | ok               |
|          25 | 1.83%    | 27.85%             | -22.01% |     0.12 |       67 | 41.93%     | ok               |
|          20 | -0.35%   | 27.85%             | -23.00% |     0.05 |       66 | 45.09%     | ok               |
|          35 | -1.85%   | 27.85%             | -21.18% |    -0.01 |       66 | 32.61%     | ok               |
|          30 | -2.47%   | 27.85%             | -21.53% |    -0.03 |       70 | 39.10%     | ok               |

## LINK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -13.55%  | -59.01%            | -50.48% |     0.1  |       70 | 41.57%     | ok               |
|          45 | -16.95%  | -59.01%            | -38.56% |    -0    |       50 | 26.25%     | ok               |
|          50 | -16.55%  | -59.01%            | -36.98% |    -0.02 |       40 | 20.88%     | ok               |
|          35 | -27.53%  | -59.01%            | -49.56% |    -0.1  |       60 | 36.40%     | ok               |
|          40 | -31.51%  | -59.01%            | -50.91% |    -0.19 |       56 | 30.65%     | ok               |

## LLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 30.06%   | 79.35%             | -38.23% |     0.61 |       42 | 39.27%     | ok               |
|          45 | 17.59%   | 79.35%             | -42.66% |     0.41 |       50 | 42.43%     | ok               |
|          15 | 10.89%   | 79.35%             | -48.12% |     0.3  |       63 | 61.90%     | ok               |
|          40 | -0.01%   | 79.35%             | -46.23% |     0.13 |       62 | 44.93%     | ok               |
|          20 | -6.97%   | 79.35%             | -51.34% |     0.03 |       72 | 56.91%     | ok               |

## LRCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 12.35%   | 368.36%            | -60.45% |     0.32 |       83 | 55.57%     | ok               |
|          50 | 5.88%    | 368.36%            | -50.39% |     0.23 |       80 | 37.44%     | ok               |
|          40 | 2.70%    | 368.36%            | -56.86% |     0.2  |       72 | 43.26%     | ok               |
|          35 | -3.96%   | 368.36%            | -61.76% |     0.12 |       80 | 45.26%     | ok               |
|          20 | -6.75%   | 368.36%            | -67.64% |     0.09 |       87 | 51.25%     | ok               |

## LTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -12.22%  | -56.12%            | -44.78% |    -0    |       56 | 31.80%     | ok               |
|          35 | -22.47%  | -56.12%            | -54.86% |    -0.13 |       66 | 42.91%     | ok               |
|          30 | -34.00%  | -56.12%            | -53.76% |    -0.29 |       66 | 48.47%     | ok               |
|          40 | -31.40%  | -56.12%            | -56.10% |    -0.3  |       58 | 38.12%     | ok               |
|          25 | -36.79%  | -56.12%            | -54.26% |    -0.33 |       74 | 50.96%     | ok               |

## MCD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 3.90%    | -4.64%             | -9.22%  |     0.24 |       42 | 20.63%     | ok               |
|          30 | -3.77%   | -4.64%             | -18.81% |    -0.1  |       77 | 38.27%     | ok               |
|          25 | -4.80%   | -4.64%             | -20.47% |    -0.13 |       77 | 40.93%     | ok               |
|          40 | -6.63%   | -4.64%             | -16.86% |    -0.26 |       69 | 28.95%     | ok               |
|          35 | -8.84%   | -4.64%             | -15.45% |    -0.34 |       69 | 34.61%     | ok               |

## META Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 11.51%   | 54.07%             | -31.03% |     0.3  |       66 | 40.60%     | ok               |
|          40 | -0.74%   | 54.07%             | -35.11% |     0.11 |       66 | 43.59%     | ok               |
|          50 | -5.51%   | 54.07%             | -34.00% |     0.02 |       70 | 36.77%     | ok               |
|          25 | -10.54%  | 54.07%             | -39.84% |    -0.03 |       67 | 54.24%     | ok               |
|          35 | -12.14%  | 54.07%             | -34.87% |    -0.07 |       77 | 48.42%     | ok               |

## MPC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 14.51%   | 62.93%             | -23.96% |     0.37 |       52 | 38.60%     | ok               |
|          45 | 7.25%    | 62.93%             | -25.09% |     0.24 |       58 | 42.26%     | ok               |
|          40 | 5.62%    | 62.93%             | -25.70% |     0.22 |       60 | 44.59%     | ok               |
|          35 | 2.36%    | 62.93%             | -35.90% |     0.16 |       68 | 47.09%     | ok               |
|          30 | -13.74%  | 62.93%             | -44.76% |    -0.14 |       71 | 49.92%     | ok               |

## MRK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -16.61%  | -4.12%             | -29.92% |    -0.27 |       87 | 57.90%     | ok               |
|          25 | -16.21%  | -4.12%             | -31.07% |    -0.29 |       72 | 49.92%     | ok               |
|          20 | -20.32%  | -4.12%             | -29.39% |    -0.39 |       77 | 53.24%     | ok               |
|          50 | -19.17%  | -4.12%             | -25.67% |    -0.51 |       58 | 32.61%     | ok               |
|          45 | -20.76%  | -4.12%             | -26.00% |    -0.52 |       59 | 35.94%     | ok               |

## MS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -2.41%   | 151.30%            | -19.99% |     0.02 |       70 | 39.60%     | ok               |
|          35 | -9.26%   | 151.30%            | -25.26% |    -0.16 |       76 | 44.26%     | ok               |
|          15 | -12.90%  | 151.30%            | -23.50% |    -0.2  |       82 | 56.57%     | ok               |
|          20 | -13.37%  | 151.30%            | -25.68% |    -0.24 |       84 | 52.58%     | ok               |
|          30 | -14.76%  | 151.30%            | -27.79% |    -0.3  |       79 | 47.75%     | ok               |

## MSFT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -17.76%  | 0.22%              | -26.27% |    -0.5  |       64 | 35.61%     | ok               |
|          50 | -21.46%  | 0.22%              | -28.83% |    -0.65 |       62 | 30.95%     | ok               |
|          35 | -31.05%  | 0.22%              | -35.08% |    -0.84 |       73 | 44.09%     | ok               |
|          40 | -30.39%  | 0.22%              | -34.46% |    -0.85 |       69 | 38.94%     | ok               |
|          25 | -34.41%  | 0.22%              | -38.91% |    -0.89 |       85 | 51.75%     | ok               |

## MU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 400.64%  | 1142.99%           | -61.96% |     1.53 |       48 | 67.55%     | ok               |
|          25 | 317.09%  | 1142.99%           | -67.90% |     1.44 |       49 | 61.23%     | ok               |
|          40 | 272.03%  | 1142.99%           | -64.36% |     1.37 |       56 | 54.91%     | ok               |
|          20 | 281.86%  | 1142.99%           | -67.25% |     1.35 |       55 | 63.39%     | ok               |
|          30 | 255.29%  | 1142.99%           | -68.76% |     1.32 |       51 | 59.40%     | ok               |

## NEAR-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 103.12%  | -52.57%            | -48.01% |     0.99 |       44 | 23.37%     | ok               |
|          50 | 70.90%   | -52.57%            | -53.13% |     0.82 |       38 | 18.39%     | ok               |
|          40 | 60.91%   | -52.57%            | -56.35% |     0.73 |       48 | 27.78%     | ok               |
|          35 | 34.38%   | -52.57%            | -60.30% |     0.54 |       70 | 33.33%     | ok               |
|          15 | 12.86%   | -52.57%            | -54.94% |     0.4  |       89 | 56.32%     | ok               |

## NEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 25.87%   | 199.21%            | -26.18% |     0.45 |       60 | 64.39%     | ok               |
|          20 | 14.02%   | 199.21%            | -30.47% |     0.33 |       72 | 59.90%     | ok               |
|          25 | -13.27%  | 199.21%            | -36.21% |    -0.02 |       70 | 57.57%     | ok               |
|          50 | -13.08%  | 199.21%            | -33.36% |    -0.06 |       60 | 41.26%     | ok               |
|          30 | -26.06%  | 199.21%            | -38.49% |    -0.23 |       76 | 55.24%     | ok               |

## NFLX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 45.69%   | 65.93%             | -11.94% |     1    |       46 | 46.76%     | ok               |
|          50 | 33.30%   | 65.93%             | -16.28% |     0.83 |       48 | 39.27%     | ok               |
|          35 | 37.75%   | 65.93%             | -18.30% |     0.82 |       62 | 50.42%     | ok               |
|          45 | 29.93%   | 65.93%             | -15.48% |     0.74 |       52 | 43.09%     | ok               |
|          25 | 28.00%   | 65.93%             | -21.09% |     0.63 |       62 | 56.91%     | ok               |

## NKE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -27.03%  | -55.64%            | -42.13% |    -0.38 |       75 | 37.44%     | ok               |
|          20 | -36.18%  | -55.64%            | -50.44% |    -0.47 |       97 | 53.24%     | ok               |
|          25 | -37.10%  | -55.64%            | -51.20% |    -0.5  |       93 | 49.25%     | ok               |
|          40 | -26.37%  | -55.64%            | -31.11% |    -0.5  |       63 | 29.45%     | ok               |
|          30 | -37.92%  | -55.64%            | -55.35% |    -0.53 |       91 | 43.93%     | ok               |

## NOW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 18.09%   | -30.88%            | -26.36% |     0.38 |       79 | 51.91%     | ok               |
|          30 | 17.57%   | -30.88%            | -30.25% |     0.37 |       80 | 45.92%     | ok               |
|          35 | 13.02%   | -30.88%            | -29.30% |     0.32 |       79 | 40.77%     | ok               |
|          15 | 11.70%   | -30.88%            | -26.36% |     0.31 |       87 | 55.24%     | ok               |
|          25 | 10.89%   | -30.88%            | -25.70% |     0.3  |       72 | 49.25%     | ok               |

## NVDA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -5.95%   | 135.08%            | -33.22% |     0.09 |       68 | 51.52%     | ok               |
|          30 | -7.71%   | 135.08%            | -35.26% |     0.04 |       70 | 49.20%     | ok               |
|          20 | -12.19%  | 135.08%            | -40.59% |     0.01 |       71 | 55.97%     | ok               |
|          50 | -15.37%  | 135.08%            | -40.84% |    -0.12 |       60 | 33.33%     | ok               |
|          35 | -18.53%  | 135.08%            | -41.25% |    -0.15 |       82 | 46.35%     | ok               |

## OP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 74.65%   | -93.92%            | -45.76% |     0.86 |       36 | 17.43%     | ok               |
|          50 | 66.86%   | -93.92%            | -36.11% |     0.86 |       34 | 12.45%     | ok               |
|          40 | 59.18%   | -93.92%            | -53.61% |     0.72 |       48 | 26.05%     | ok               |
|          35 | 33.12%   | -93.92%            | -58.13% |     0.53 |       56 | 29.31%     | ok               |
|          30 | 5.00%    | -93.92%            | -70.11% |     0.3  |       72 | 36.02%     | ok               |

## ORCL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 131.48%  | 72.26%             | -29.29% |     1.01 |       72 | 65.22%     | ok               |
|          25 | 73.64%   | 72.26%             | -27.74% |     0.75 |       73 | 57.74%     | ok               |
|          20 | 70.66%   | 72.26%             | -29.29% |     0.72 |       75 | 60.90%     | ok               |
|          35 | 48.88%   | 72.26%             | -31.95% |     0.6  |       66 | 49.42%     | ok               |
|          30 | 49.01%   | 72.26%             | -29.47% |     0.6  |       72 | 53.58%     | ok               |

## OXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 0.13%    | -4.00%             | -30.85% |     0.12 |       65 | 43.43%     | ok               |
|          35 | -0.66%   | -4.00%             | -30.50% |     0.1  |       68 | 38.60%     | ok               |
|          50 | -1.47%   | -4.00%             | -31.07% |     0.07 |       38 | 27.95%     | ok               |
|          40 | -3.09%   | -4.00%             | -32.21% |     0.05 |       56 | 34.61%     | ok               |
|          25 | -13.72%  | -4.00%             | -40.42% |    -0.13 |       73 | 46.92%     | ok               |

## PEP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 9.33%    | -12.76%            | -11.62% |     0.43 |       48 | 27.62%     | ok               |
|          45 | 0.13%    | -12.76%            | -14.22% |     0.06 |       72 | 32.61%     | ok               |
|          40 | -3.39%   | -12.76%            | -18.04% |    -0.07 |       80 | 38.44%     | ok               |
|          35 | -4.60%   | -12.76%            | -21.42% |    -0.08 |       87 | 43.59%     | ok               |
|          30 | -9.64%   | -12.76%            | -21.35% |    -0.22 |       85 | 50.25%     | ok               |

## PEPE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 10.36%   | -83.61%            | -57.66% |     0.36 |       77 | 43.87%     | ok               |
|          35 | 4.07%    | -83.61%            | -51.35% |     0.29 |       62 | 38.51%     | ok               |
|          25 | -14.24%  | -83.61%            | -56.30% |     0.15 |       85 | 49.23%     | ok               |
|          15 | -30.70%  | -83.61%            | -65.75% |     0.07 |       81 | 59.00%     | ok               |
|          50 | -15.28%  | -83.61%            | -39.43% |     0.01 |       54 | 22.03%     | ok               |

## PFE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -20.60%  | -8.55%             | -25.65% |    -0.69 |       52 | 21.46%     | ok               |
|          50 | -23.01%  | -8.55%             | -26.92% |    -0.86 |       44 | 17.64%     | ok               |
|          40 | -27.33%  | -8.55%             | -31.95% |    -0.9  |       76 | 26.29%     | ok               |
|          35 | -31.03%  | -8.55%             | -36.39% |    -0.97 |       82 | 33.11%     | ok               |
|          30 | -37.43%  | -8.55%             | -42.29% |    -1.16 |       77 | 36.61%     | ok               |

## PG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 1.45%    | -2.29%             | -19.77% |     0.11 |       52 | 34.94%     | ok               |
|          35 | -0.80%   | -2.29%             | -18.66% |     0.02 |       60 | 38.27%     | ok               |
|          30 | -9.81%   | -2.29%             | -21.65% |    -0.33 |       62 | 41.43%     | ok               |
|          45 | -8.46%   | -2.29%             | -20.43% |    -0.34 |       52 | 32.45%     | ok               |
|          25 | -10.89%  | -2.29%             | -22.55% |    -0.38 |       72 | 42.60%     | ok               |

## PM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 3.37%    | 98.05%             | -32.20% |     0.17 |       88 | 53.24%     | ok               |
|          20 | 1.01%    | 98.05%             | -31.89% |     0.12 |       87 | 62.06%     | ok               |
|          30 | 0.05%    | 98.05%             | -33.68% |     0.1  |       81 | 57.24%     | ok               |
|          50 | -4.49%   | 98.05%             | -35.70% |    -0.03 |       72 | 41.93%     | ok               |
|          25 | -6.20%   | 98.05%             | -37.05% |    -0.04 |       81 | 59.40%     | ok               |

## POL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 63.75%   | -82.97%            | -46.45% |     0.76 |       79 | 49.43%     | ok               |
|          25 | 57.75%   | -82.97%            | -46.72% |     0.7  |       70 | 57.85%     | ok               |
|          20 | 47.12%   | -82.97%            | -52.88% |     0.62 |       78 | 63.03%     | ok               |
|          15 | 35.42%   | -82.97%            | -58.42% |     0.54 |       78 | 68.58%     | ok               |
|          50 | 20.67%   | -82.97%            | -22.86% |     0.45 |       50 | 20.69%     | ok               |

## QCOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -6.64%   | 43.85%             | -55.66% |     0.09 |       73 | 50.08%     | ok               |
|          35 | -8.83%   | 43.85%             | -51.84% |     0.05 |       83 | 45.42%     | ok               |
|          20 | -13.47%  | 43.85%             | -57.05% |     0    |       70 | 53.08%     | ok               |
|          30 | -18.79%  | 43.85%             | -57.69% |    -0.09 |       77 | 48.09%     | ok               |
|          15 | -27.85%  | 43.85%             | -60.40% |    -0.2  |       74 | 56.24%     | ok               |

## QQQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 24.26%   | 75.69%             | -12.88% |     0.64 |       57 | 49.25%     | ok               |
|          15 | 24.80%   | 75.69%             | -14.17% |     0.61 |       61 | 54.74%     | ok               |
|          30 | 20.20%   | 75.69%             | -12.88% |     0.57 |       62 | 46.42%     | ok               |
|          20 | 21.26%   | 75.69%             | -12.98% |     0.56 |       65 | 51.91%     | ok               |
|          35 | 7.91%    | 75.69%             | -18.29% |     0.29 |       68 | 42.76%     | ok               |

## RENDER-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 49.72%   | -57.28%            | -43.43% |     0.65 |       84 | 54.68%     | ok               |
|          15 | 32.34%   | -57.28%            | -44.59% |     0.55 |       84 | 57.80%     | ok               |
|          25 | 20.05%   | -57.28%            | -40.60% |     0.46 |       88 | 50.73%     | ok               |
|          30 | -17.59%  | -57.28%            | -45.00% |     0.11 |       96 | 44.28%     | ok               |
|          40 | -27.22%  | -57.28%            | -38.60% |    -0.1  |       70 | 29.52%     | ok               |

## RTX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 26.38%   | 105.07%            | -18.66% |     0.66 |       76 | 56.07%     | ok               |
|          50 | 18.90%   | 105.07%            | -18.42% |     0.61 |       56 | 41.93%     | ok               |
|          25 | 21.67%   | 105.07%            | -18.59% |     0.57 |       64 | 52.75%     | ok               |
|          30 | 19.82%   | 105.07%            | -16.99% |     0.54 |       58 | 51.58%     | ok               |
|          35 | 17.22%   | 105.07%            | -18.00% |     0.53 |       54 | 49.58%     | ok               |

## SBUX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -18.39%  | 10.46%             | -24.59% |    -0.33 |       66 | 41.10%     | ok               |
|          45 | -17.36%  | 10.46%             | -27.26% |    -0.4  |       62 | 28.12%     | ok               |
|          40 | -19.43%  | 10.46%             | -25.43% |    -0.42 |       60 | 32.11%     | ok               |
|          30 | -25.37%  | 10.46%             | -30.74% |    -0.53 |       65 | 38.77%     | ok               |
|          50 | -20.92%  | 10.46%             | -27.78% |    -0.54 |       50 | 24.29%     | ok               |

## SCHW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 2.59%    | 42.29%             | -15.92% |     0.15 |       54 | 33.44%     | ok               |
|          50 | -1.42%   | 42.29%             | -11.75% |     0.01 |       50 | 30.95%     | ok               |
|          40 | -8.05%   | 42.29%             | -21.81% |    -0.15 |       62 | 36.44%     | ok               |
|          25 | -10.23%  | 42.29%             | -28.76% |    -0.16 |       61 | 47.75%     | ok               |
|          20 | -11.91%  | 42.29%             | -29.24% |    -0.2  |       69 | 50.42%     | ok               |

## SHIB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -3.33%   | -77.33%            | -49.21% |     0.21 |       76 | 68.20%     | ok               |
|          25 | -10.40%  | -77.33%            | -43.85% |     0.12 |       75 | 59.00%     | ok               |
|          20 | -14.31%  | -77.33%            | -46.92% |     0.09 |       79 | 63.79%     | ok               |
|          35 | -13.56%  | -77.33%            | -53.32% |     0.05 |       64 | 46.17%     | ok               |
|          40 | -16.59%  | -77.33%            | -50.74% |    -0.01 |       54 | 38.70%     | ok               |

## SHY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          30 | -2.16%   | 0.06%              | -2.85% |    -0.74 |       50 | 35.44%     | ok               |
|          35 | -2.27%   | 0.06%              | -3.27% |    -0.79 |       52 | 33.61%     | ok               |
|          40 | -2.39%   | 0.06%              | -3.33% |    -0.84 |       52 | 31.78%     | ok               |
|          45 | -2.37%   | 0.06%              | -3.23% |    -0.86 |       50 | 28.62%     | ok               |
|          50 | -2.54%   | 0.06%              | -3.40% |    -0.96 |       46 | 25.79%     | ok               |

## SKY-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -33.20%  | -0.90%             | -56.39% |    -0.37 |       58 | 50.94%     | ok               |
|          30 | -29.10%  | -0.90%             | -43.98% |    -0.38 |       68 | 40.80%     | ok               |
|          25 | -32.74%  | -0.90%             | -48.09% |    -0.44 |       63 | 44.58%     | ok               |
|          20 | -42.99%  | -0.90%             | -58.40% |    -0.63 |       60 | 48.35%     | ok               |
|          35 | -39.64%  | -0.90%             | -49.68% |    -0.72 |       60 | 34.43%     | ok               |

## SLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 12.74%   | 6.53%              | -23.07% |     0.35 |       46 | 35.44%     | ok               |
|          45 | 11.08%   | 6.53%              | -20.46% |     0.33 |       52 | 32.11%     | ok               |
|          50 | -11.30%  | 6.53%              | -30.82% |    -0.19 |       54 | 28.62%     | ok               |
|          35 | -15.57%  | 6.53%              | -41.81% |    -0.22 |       74 | 43.43%     | ok               |
|          30 | -30.05%  | 6.53%              | -54.95% |    -0.54 |       75 | 49.92%     | ok               |

## SLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 56.72%   | 209.16%            | -34.10% |     0.78 |       50 | 32.95%     | ok               |
|          45 | 54.24%   | 209.16%            | -31.82% |     0.75 |       54 | 33.78%     | ok               |
|          40 | 52.44%   | 209.16%            | -31.91% |     0.73 |       60 | 35.94%     | ok               |
|          35 | 39.06%   | 209.16%            | -36.89% |     0.61 |       64 | 38.27%     | ok               |
|          30 | 23.86%   | 209.16%            | -42.66% |     0.45 |       60 | 40.27%     | ok               |

## SMH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 119.88%  | 242.36%            | -30.17% |     1.34 |       47 | 53.91%     | ok               |
|          35 | 96.79%   | 242.36%            | -34.36% |     1.22 |       54 | 49.75%     | ok               |
|          25 | 96.64%   | 242.36%            | -32.94% |     1.2  |       46 | 52.75%     | ok               |
|          30 | 94.32%   | 242.36%            | -33.99% |     1.19 |       48 | 51.08%     | ok               |
|          45 | 80.19%   | 242.36%            | -32.75% |     1.14 |       52 | 43.93%     | ok               |

## SNX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 27.47%   | -86.04%            | -28.28% |     0.49 |       68 | 32.95%     | ok               |
|          30 | 17.10%   | -86.04%            | -32.91% |     0.4  |       63 | 40.42%     | ok               |
|          20 | 10.14%   | -86.04%            | -43.20% |     0.36 |       73 | 50.77%     | ok               |
|          25 | -6.70%   | -86.04%            | -36.73% |     0.19 |       76 | 45.02%     | ok               |
|          15 | -25.71%  | -86.04%            | -47.56% |     0.03 |       83 | 54.79%     | ok               |

## SOL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -12.19%  | -60.52%            | -51.20% |     0.11 |       64 | 39.46%     | ok               |
|          35 | -28.55%  | -60.52%            | -59.05% |    -0.06 |       72 | 46.93%     | ok               |
|          25 | -30.52%  | -60.52%            | -51.71% |    -0.07 |       72 | 57.47%     | ok               |
|          15 | -37.72%  | -60.52%            | -57.85% |    -0.14 |       78 | 64.75%     | ok               |
|          30 | -37.62%  | -60.52%            | -58.80% |    -0.18 |       80 | 53.07%     | ok               |

## SOXX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 95.21%   | 210.50%            | -38.67% |     1.13 |       53 | 52.58%     | ok               |
|          25 | 91.48%   | 210.50%            | -39.85% |     1.1  |       51 | 52.25%     | ok               |
|          35 | 86.13%   | 210.50%            | -38.63% |     1.08 |       59 | 47.59%     | ok               |
|          15 | 90.31%   | 210.50%            | -37.72% |     1.06 |       66 | 55.41%     | ok               |
|          30 | 80.72%   | 210.50%            | -40.34% |     1.02 |       55 | 50.08%     | ok               |

## SPY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 20.07%   | 55.68%             | -14.25% |     0.67 |       58 | 54.08%     | ok               |
|          15 | 18.87%   | 55.68%             | -16.80% |     0.62 |       65 | 57.07%     | ok               |
|          25 | 11.22%   | 55.68%             | -15.22% |     0.42 |       56 | 53.24%     | ok               |
|          30 | 7.21%    | 55.68%             | -16.47% |     0.31 |       58 | 50.75%     | ok               |
|          35 | 3.93%    | 55.68%             | -16.72% |     0.2  |       58 | 48.25%     | ok               |

## SUSHI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -24.39%  | -87.31%            | -40.79% |    -0.2  |       52 | 14.56%     | ok               |
|          45 | -56.30%  | -87.31%            | -64.69% |    -0.71 |       54 | 17.82%     | ok               |
|          40 | -59.39%  | -87.31%            | -66.97% |    -0.72 |       61 | 24.33%     | ok               |
|          35 | -67.00%  | -87.31%            | -75.30% |    -0.85 |       76 | 29.69%     | ok               |
|          15 | -80.09%  | -87.31%            | -81.81% |    -0.99 |       88 | 47.13%     | ok               |

## T Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 47.82%   | 35.49%             | -18.13% |     1.01 |       57 | 54.74%     | ok               |
|          25 | 40.24%   | 35.49%             | -17.66% |     0.9  |       62 | 52.41%     | ok               |
|          15 | 39.75%   | 35.49%             | -15.08% |     0.86 |       66 | 58.57%     | ok               |
|          35 | 27.74%   | 35.49%             | -14.49% |     0.71 |       62 | 46.92%     | ok               |
|          30 | 26.25%   | 35.49%             | -17.01% |     0.66 |       64 | 50.25%     | ok               |

## TGT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.81%   | -5.47%             | -40.99% |    -0.02 |       77 | 45.92%     | ok               |
|          15 | -9.86%   | -5.47%             | -38.83% |    -0.07 |       67 | 50.42%     | ok               |
|          25 | -10.93%  | -5.47%             | -43.53% |    -0.13 |       61 | 41.26%     | ok               |
|          45 | -10.17%  | -5.47%             | -30.47% |    -0.16 |       50 | 28.95%     | ok               |
|          30 | -11.79%  | -5.47%             | -41.74% |    -0.16 |       56 | 38.60%     | ok               |

## TIA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 24.71%   | -92.37%            | -39.80% |     0.46 |       60 | 24.90%     | ok               |
|          35 | 23.20%   | -92.37%            | -40.13% |     0.44 |       60 | 29.12%     | ok               |
|          45 | 15.72%   | -92.37%            | -44.21% |     0.37 |       50 | 18.58%     | ok               |
|          50 | 13.81%   | -92.37%            | -44.86% |     0.36 |       32 | 11.49%     | ok               |
|          30 | -19.62%  | -92.37%            | -56.27% |     0.04 |       82 | 33.72%     | ok               |

## TLT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -12.40%  | -8.71%             | -16.02% |    -1.32 |       34 | 14.31%     | ok               |
|          30 | -22.51%  | -8.71%             | -23.75% |    -1.66 |       70 | 32.28%     | ok               |
|          45 | -16.54%  | -8.71%             | -19.55% |    -1.7  |       42 | 16.97%     | ok               |
|          40 | -18.95%  | -8.71%             | -20.25% |    -1.75 |       60 | 21.13%     | ok               |
|          35 | -21.97%  | -8.71%             | -23.22% |    -1.83 |       66 | 26.29%     | ok               |

## TMO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 40.59%   | -13.98%            | -10.55% |     0.93 |       38 | 30.28%     | ok               |
|          45 | 39.34%   | -13.98%            | -12.29% |     0.88 |       46 | 35.44%     | ok               |
|          40 | 37.28%   | -13.98%            | -12.07% |     0.83 |       49 | 39.93%     | ok               |
|          35 | 22.23%   | -13.98%            | -16.12% |     0.54 |       59 | 44.09%     | ok               |
|          30 | 15.63%   | -13.98%            | -16.83% |     0.41 |       57 | 48.42%     | ok               |

## TMUS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 12.92%   | 15.34%             | -26.87% |     0.36 |       69 | 60.07%     | ok               |
|          30 | 11.56%   | 15.34%             | -24.50% |     0.34 |       70 | 48.42%     | ok               |
|          20 | 5.99%    | 15.34%             | -24.82% |     0.22 |       71 | 54.41%     | ok               |
|          25 | 4.94%    | 15.34%             | -25.91% |     0.2  |       75 | 50.75%     | ok               |
|          50 | 3.33%    | 15.34%             | -22.71% |     0.17 |       60 | 35.94%     | ok               |

## TRX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 2.00%    | 32.35%             | -22.90% |     0.14 |       70 | 48.66%     | ok               |
|          40 | 1.22%    | 32.35%             | -18.79% |     0.12 |       52 | 37.74%     | ok               |
|          35 | 0.61%    | 32.35%             | -21.77% |     0.11 |       66 | 45.98%     | ok               |
|          25 | 0.17%    | 32.35%             | -26.84% |     0.1  |       66 | 51.92%     | ok               |
|          50 | -0.25%   | 32.35%             | -18.49% |     0.07 |       44 | 32.38%     | ok               |

## TSLA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 83.72%   | 96.59%             | -32.60% |     0.92 |       64 | 31.11%     | ok               |
|          40 | 74.47%   | 96.59%             | -45.90% |     0.8  |       61 | 35.61%     | ok               |
|          45 | 47.81%   | 96.59%             | -46.86% |     0.62 |       65 | 32.95%     | ok               |
|          35 | 27.21%   | 96.59%             | -54.51% |     0.45 |       74 | 38.60%     | ok               |
|          30 | 3.29%    | 96.59%             | -57.89% |     0.24 |       68 | 43.09%     | ok               |

## TXN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 13.38%   | 79.73%             | -45.45% |     0.33 |       72 | 35.77%     | ok               |
|          20 | 2.88%    | 79.73%             | -38.98% |     0.19 |       62 | 59.90%     | ok               |
|          15 | 0.75%    | 79.73%             | -39.48% |     0.17 |       65 | 64.06%     | ok               |
|          35 | -5.44%   | 79.73%             | -43.38% |     0.05 |       78 | 50.42%     | ok               |
|          40 | -6.08%   | 79.73%             | -45.67% |     0.04 |       76 | 48.25%     | ok               |

## UNH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 28.23%   | -20.27%            | -36.91% |     0.53 |       50 | 28.62%     | ok               |
|          30 | 24.03%   | -20.27%            | -27.74% |     0.46 |       76 | 51.75%     | ok               |
|          35 | 19.45%   | -20.27%            | -29.80% |     0.4  |       70 | 46.42%     | ok               |
|          15 | 19.66%   | -20.27%            | -31.43% |     0.4  |       79 | 66.72%     | ok               |
|          20 | 16.82%   | -20.27%            | -31.00% |     0.37 |       81 | 61.56%     | ok               |

## UNI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -1.77%   | -78.45%            | -57.12% |     0.21 |       52 | 25.10%     | ok               |
|          40 | -11.32%  | -78.45%            | -63.75% |     0.11 |       54 | 30.08%     | ok               |
|          50 | -10.68%  | -78.45%            | -54.53% |     0.08 |       50 | 20.50%     | ok               |
|          35 | -22.39%  | -78.45%            | -68.58% |     0.01 |       70 | 34.67%     | ok               |
|          20 | -69.84%  | -78.45%            | -80.81% |    -0.67 |       99 | 51.34%     | ok               |

## UPS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -33.71%  | -32.01%            | -42.25% |    -0.63 |       74 | 44.26%     | ok               |
|          35 | -32.60%  | -32.01%            | -40.47% |    -0.64 |       59 | 33.94%     | ok               |
|          20 | -34.82%  | -32.01%            | -45.77% |    -0.65 |       80 | 47.42%     | ok               |
|          30 | -35.08%  | -32.01%            | -40.62% |    -0.69 |       66 | 39.60%     | ok               |
|          40 | -33.95%  | -32.01%            | -42.12% |    -0.7  |       51 | 28.79%     | ok               |

## USO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 10.72%   | 74.00%             | -33.68% |     0.3  |       48 | 27.12%     | ok               |
|          30 | 2.80%    | 74.00%             | -43.35% |     0.17 |       68 | 34.44%     | ok               |
|          40 | -0.60%   | 74.00%             | -41.14% |     0.11 |       59 | 29.78%     | ok               |
|          25 | -1.49%   | 74.00%             | -45.72% |     0.11 |       70 | 37.10%     | ok               |
|          20 | -1.60%   | 74.00%             | -45.77% |     0.11 |       74 | 39.27%     | ok               |

## VEA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 5.44%    | 54.61%             | -16.28% |     0.25 |       60 | 50.58%     | ok               |
|          20 | 1.19%    | 54.61%             | -17.70% |     0.1  |       61 | 47.92%     | ok               |
|          25 | -0.82%   | 54.61%             | -17.79% |     0.02 |       57 | 46.26%     | ok               |
|          30 | -0.98%   | 54.61%             | -17.93% |     0.01 |       58 | 44.09%     | ok               |
|          35 | -2.09%   | 54.61%             | -16.79% |    -0.03 |       56 | 43.09%     | ok               |

## VIXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -46.17%  | -61.39%            | -68.69% |    -0.39 |       44 | 10.32%     | ok               |
|          45 | -56.13%  | -61.39%            | -74.13% |    -0.55 |       56 | 16.31%     | ok               |
|          40 | -64.59%  | -61.39%            | -80.10% |    -0.66 |       70 | 20.47%     | ok               |
|          35 | -68.29%  | -61.39%            | -83.87% |    -0.7  |       86 | 25.62%     | ok               |
|          15 | -77.05%  | -61.39%            | -89.47% |    -0.78 |      101 | 43.59%     | ok               |

## VNQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -8.60%   | 14.65%             | -19.07% |    -0.37 |       60 | 28.62%     | ok               |
|          50 | -9.03%   | 14.65%             | -17.13% |    -0.41 |       56 | 26.12%     | ok               |
|          25 | -13.12%  | 14.65%             | -22.34% |    -0.51 |       69 | 40.77%     | ok               |
|          40 | -14.13%  | 14.65%             | -24.84% |    -0.62 |       74 | 32.11%     | ok               |
|          20 | -16.52%  | 14.65%             | -23.79% |    -0.64 |       74 | 43.59%     | ok               |

## VTI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 19.32%   | 54.56%             | -13.96% |     0.64 |       62 | 55.74%     | ok               |
|          15 | 13.21%   | 54.56%             | -15.70% |     0.46 |       65 | 58.24%     | ok               |
|          25 | 6.34%    | 54.56%             | -16.10% |     0.27 |       58 | 53.91%     | ok               |
|          30 | -0.72%   | 54.56%             | -18.77% |     0.04 |       66 | 52.08%     | ok               |
|          40 | -2.95%   | 54.56%             | -20.44% |    -0.05 |       68 | 45.42%     | ok               |

## VWO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -9.03%   | 53.87%             | -24.01% |    -0.26 |       69 | 49.42%     | ok               |
|          50 | -7.89%   | 53.87%             | -21.68% |    -0.28 |       60 | 32.45%     | ok               |
|          20 | -10.06%  | 53.87%             | -26.14% |    -0.31 |       67 | 47.25%     | ok               |
|          40 | -8.98%   | 53.87%             | -23.57% |    -0.31 |       70 | 37.94%     | ok               |
|          45 | -9.69%   | 53.87%             | -23.75% |    -0.35 |       62 | 34.94%     | ok               |

## VZ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -5.86%   | 11.46%             | -16.98% |    -0.16 |       50 | 25.96%     | ok               |
|          45 | -14.28%  | 11.46%             | -20.38% |    -0.46 |       58 | 28.95%     | ok               |
|          35 | -19.35%  | 11.46%             | -24.68% |    -0.63 |       61 | 34.44%     | ok               |
|          25 | -22.37%  | 11.46%             | -28.84% |    -0.68 |       78 | 42.26%     | ok               |
|          40 | -22.14%  | 11.46%             | -26.72% |    -0.77 |       64 | 31.45%     | ok               |

## WFC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -1.81%   | 69.26%             | -18.29% |     0.01 |       58 | 32.61%     | ok               |
|          35 | -7.44%   | 69.26%             | -23.64% |    -0.09 |       79 | 44.09%     | ok               |
|          45 | -8.31%   | 69.26%             | -23.40% |    -0.18 |       64 | 36.94%     | ok               |
|          20 | -16.99%  | 69.26%             | -29.43% |    -0.24 |       79 | 53.41%     | ok               |
|          40 | -11.98%  | 69.26%             | -24.26% |    -0.29 |       74 | 40.27%     | ok               |

## WIF-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 46.07%   | -89.34%            | -46.21% |     0.6  |       73 | 42.34%     | ok               |
|          20 | 44.13%   | -89.34%            | -40.67% |     0.59 |       67 | 39.85%     | ok               |
|          25 | -4.96%   | -89.34%            | -45.19% |     0.26 |       73 | 37.16%     | ok               |
|          30 | -35.63%  | -89.34%            | -50.40% |    -0.11 |       72 | 32.95%     | ok               |
|          50 | -20.06%  | -89.34%            | -37.87% |    -0.14 |       40 | 12.07%     | ok               |

## WMT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 63.28%   | 122.64%            | -9.18%  |     1.6  |       36 | 44.59%     | ok               |
|          50 | 56.64%   | 122.64%            | -12.19% |     1.54 |       30 | 42.43%     | ok               |
|          40 | 53.07%   | 122.64%            | -9.18%  |     1.37 |       40 | 45.76%     | ok               |
|          35 | 54.34%   | 122.64%            | -9.11%  |     1.37 |       48 | 49.42%     | ok               |
|          30 | 31.99%   | 122.64%            | -21.31% |     0.84 |       55 | 51.91%     | ok               |

## XBI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 3.96%    | 52.86%             | -16.71% |     0.18 |       60 | 34.61%     | ok               |
|          45 | 3.16%    | 52.86%             | -16.88% |     0.16 |       52 | 31.45%     | ok               |
|          35 | -3.05%   | 52.86%             | -21.38% |     0.01 |       62 | 37.77%     | ok               |
|          30 | -4.13%   | 52.86%             | -21.75% |    -0.02 |       62 | 39.43%     | ok               |
|          50 | -5.14%   | 52.86%             | -16.83% |    -0.07 |       54 | 28.29%     | ok               |

## XLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -4.67%   | 26.90%             | -20.60% |    -0.12 |       60 | 32.11%     | ok               |
|          50 | -4.61%   | 26.90%             | -17.40% |    -0.14 |       44 | 27.79%     | ok               |
|          35 | -7.91%   | 26.90%             | -23.62% |    -0.24 |       60 | 35.61%     | ok               |
|          45 | -7.43%   | 26.90%             | -20.61% |    -0.25 |       44 | 29.28%     | ok               |
|          25 | -12.47%  | 26.90%             | -23.87% |    -0.4  |       68 | 41.26%     | ok               |

## XLC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 15.48%   | 48.16%             | -12.33% |     0.54 |       63 | 55.57%     | ok               |
|          25 | 13.31%   | 48.16%             | -12.31% |     0.47 |       60 | 57.40%     | ok               |
|          40 | 10.83%   | 48.16%             | -13.38% |     0.43 |       66 | 48.25%     | ok               |
|          35 | 10.21%   | 48.16%             | -13.38% |     0.4  |       62 | 52.58%     | ok               |
|          20 | 5.34%    | 48.16%             | -13.78% |     0.23 |       68 | 60.07%     | ok               |

## XLE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.02%   | 37.77%             | -25.98% |     0.07 |       54 | 36.94%     | ok               |
|          35 | -3.79%   | 37.77%             | -32.17% |    -0.02 |       65 | 44.59%     | ok               |
|          45 | -5.17%   | 37.77%             | -30.88% |    -0.07 |       62 | 39.60%     | ok               |
|          25 | -11.35%  | 37.77%             | -37.50% |    -0.2  |       81 | 49.92%     | ok               |
|          30 | -11.37%  | 37.77%             | -37.51% |    -0.22 |       73 | 46.76%     | ok               |

## XLF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -4.00%   | 40.32%             | -18.01% |    -0.07 |       66 | 54.58%     | ok               |
|          15 | -7.98%   | 40.32%             | -19.58% |    -0.21 |       74 | 57.40%     | ok               |
|          25 | -10.70%  | 40.32%             | -23.22% |    -0.33 |       75 | 51.08%     | ok               |
|          30 | -11.34%  | 40.32%             | -23.61% |    -0.37 |       74 | 48.59%     | ok               |
|          35 | -18.45%  | 40.32%             | -27.41% |    -0.73 |       64 | 44.43%     | ok               |

## XLI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 12.06%   | 57.80%             | -10.36% |     0.46 |       72 | 54.24%     | ok               |
|          50 | 6.67%    | 57.80%             | -9.25%  |     0.34 |       56 | 35.94%     | ok               |
|          20 | 7.73%    | 57.80%             | -12.74% |     0.34 |       63 | 49.25%     | ok               |
|          45 | 5.69%    | 57.80%             | -12.27% |     0.29 |       62 | 38.10%     | ok               |
|          30 | 5.37%    | 57.80%             | -11.38% |     0.26 |       64 | 46.76%     | ok               |

## XLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 90.08%   | 90.02%             | -14.75% |     1.41 |       41 | 54.08%     | ok               |
|          20 | 75.20%   | 90.02%             | -14.75% |     1.27 |       48 | 51.91%     | ok               |
|          25 | 71.64%   | 90.02%             | -14.75% |     1.27 |       42 | 49.75%     | ok               |
|          30 | 69.39%   | 90.02%             | -14.75% |     1.26 |       42 | 48.59%     | ok               |
|          35 | 50.49%   | 90.02%             | -13.61% |     1.03 |       54 | 45.92%     | ok               |

## XLM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 36.43%   | -52.20%            | -32.06% |     0.57 |       44 | 27.97%     | ok               |
|          45 | 32.33%   | -52.20%            | -37.64% |     0.53 |       50 | 31.61%     | ok               |
|          30 | 6.52%    | -52.20%            | -45.72% |     0.29 |       71 | 45.79%     | ok               |
|          40 | 0.71%    | -52.20%            | -39.92% |     0.22 |       49 | 35.63%     | ok               |
|          35 | -1.19%   | -52.20%            | -44.88% |     0.21 |       69 | 41.76%     | ok               |

## XLP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 11.12%   | 17.94%             | -5.66%  |     0.68 |       56 | 33.94%     | ok               |
|          50 | 9.69%    | 17.94%             | -6.08%  |     0.61 |       58 | 31.78%     | ok               |
|          40 | 8.89%    | 17.94%             | -7.77%  |     0.54 |       72 | 38.10%     | ok               |
|          35 | 7.94%    | 17.94%             | -9.73%  |     0.48 |       68 | 41.10%     | ok               |
|          30 | 5.69%    | 17.94%             | -10.28% |     0.35 |       72 | 42.93%     | ok               |

## XLU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 5.66%    | 47.22%             | -9.11%  |     0.31 |       50 | 30.95%     | ok               |
|          45 | 3.56%    | 47.22%             | -10.56% |     0.21 |       54 | 31.78%     | ok               |
|          40 | 0.70%    | 47.22%             | -11.94% |     0.08 |       58 | 33.28%     | ok               |
|          35 | -3.19%   | 47.22%             | -16.24% |    -0.1  |       62 | 35.61%     | ok               |
|          30 | -6.29%   | 47.22%             | -18.15% |    -0.24 |       69 | 38.77%     | ok               |

## XLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -10.10%  | 9.23%              | -15.55% |    -0.48 |       68 | 36.61%     | ok               |
|          25 | -11.42%  | 9.23%              | -16.79% |    -0.55 |       70 | 37.94%     | ok               |
|          15 | -14.91%  | 9.23%              | -20.26% |    -0.7  |       79 | 42.93%     | ok               |
|          20 | -14.84%  | 9.23%              | -20.35% |    -0.72 |       73 | 39.77%     | ok               |
|          35 | -14.80%  | 9.23%              | -19.74% |    -0.78 |       66 | 34.11%     | ok               |

## XLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 2.60%    | 36.52%             | -12.94% |     0.15 |       74 | 41.60%     | ok               |
|          30 | 0.76%    | 36.52%             | -14.01% |     0.09 |       74 | 44.59%     | ok               |
|          15 | -0.76%   | 36.52%             | -15.77% |     0.05 |       76 | 51.58%     | ok               |
|          50 | -0.60%   | 36.52%             | -11.79% |     0.03 |       52 | 29.78%     | ok               |
|          40 | -3.75%   | 36.52%             | -16.99% |    -0.07 |       70 | 37.27%     | ok               |

## XOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 3.46%    | 43.93%             | -19.90% |     0.17 |       58 | 36.94%     | ok               |
|          30 | 2.44%    | 43.93%             | -20.29% |     0.14 |       58 | 36.27%     | ok               |
|          50 | 2.44%    | 43.93%             | -21.35% |     0.14 |       44 | 29.62%     | ok               |
|          20 | -0.36%   | 43.93%             | -25.56% |     0.07 |       63 | 39.43%     | ok               |
|          40 | -1.70%   | 43.93%             | -21.45% |     0.02 |       54 | 33.61%     | ok               |

## XRP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -29.67%  | -52.17%            | -50.11% |    -0.21 |       70 | 41.95%     | ok               |
|          40 | -36.21%  | -52.17%            | -48.42% |    -0.36 |       62 | 35.82%     | ok               |
|          30 | -42.86%  | -52.17%            | -58.77% |    -0.42 |       74 | 46.36%     | ok               |
|          45 | -43.39%  | -52.17%            | -50.29% |    -0.52 |       62 | 31.42%     | ok               |
|          50 | -40.94%  | -52.17%            | -40.94% |    -0.58 |       64 | 23.75%     | ok               |

## YFI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -32.83%  | -74.57%            | -52.37% |    -0.46 |       62 | 27.20%     | ok               |
|          45 | -38.27%  | -74.57%            | -54.04% |    -0.66 |       64 | 22.61%     | ok               |
|          35 | -51.92%  | -74.57%            | -65.91% |    -0.81 |       73 | 34.48%     | ok               |
|          30 | -54.99%  | -74.57%            | -67.78% |    -0.82 |       83 | 40.61%     | ok               |
|          50 | -41.48%  | -74.57%            | -51.80% |    -0.84 |       52 | 17.43%     | ok               |

## ZEC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 124.17%  | 954.71%            | -24.66% |     0.9  |       50 | 23.18%     | ok               |
|          35 | 86.85%   | 954.71%            | -43.54% |     0.74 |       58 | 30.84%     | ok               |
|          25 | 73.54%   | 954.71%            | -46.61% |     0.69 |       61 | 39.66%     | ok               |
|          50 | 54.10%   | 954.71%            | -37.94% |     0.6  |       52 | 20.69%     | ok               |
|          30 | 43.83%   | 954.71%            | -46.93% |     0.56 |       69 | 36.40%     | ok               |
