# Market Tracker Backtest Report

_Generated: 2026-06-29T01:34:00+00:00_

## Data Sources

- Crypto: Kraken -> Coinbase -> CoinGecko OHLC -> CoinPaprika fallback chain.
- Stocks / ETFs / indices: Stooq -> Yahoo Finance fallback chain.
- Data rows are generated from real market APIs. Mock OHLCV rows are not generated.

## Data Freshness

- Rows: **92,442**
- Symbols: **161**
- Date range: **2024-02-02** to **2026-06-29**

## Latest Signals

| symbol     | date                |         close |   composite_score | signal   | data_source   |
|:-----------|:--------------------|--------------:|------------------:|:---------|:--------------|
| AAVE-USD   | 2026-06-29 00:00:00 |    90.75      |          43.3333  | LONG     | Kraken API    |
| AMAT       | 2026-06-26 00:00:00 |   626.84      |          70.5833  | LONG     | Yahoo Finance |
| BAC        | 2026-06-26 00:00:00 |    57.88      |          58.0833  | LONG     | Yahoo Finance |
| C          | 2026-06-26 00:00:00 |   141.76      |          72.75    | LONG     | Yahoo Finance |
| CAT        | 2026-06-26 00:00:00 |   997.47      |          73.4167  | LONG     | Yahoo Finance |
| DE         | 2026-06-26 00:00:00 |   613.24      |          78.4167  | LONG     | Yahoo Finance |
| DXY-INDEX  | 2026-06-28 00:00:00 |   101.36      |          80.914   | LONG     | Yahoo Finance |
| GE         | 2026-06-26 00:00:00 |   369         |          58.25    | LONG     | Yahoo Finance |
| HD         | 2026-06-26 00:00:00 |   348.86      |          66       | LONG     | Yahoo Finance |
| HON        | 2026-06-26 00:00:00 |   464.42      |          74.75    | LONG     | Yahoo Finance |
| ITA        | 2026-06-26 00:00:00 |   236.78      |          44.75    | LONG     | Yahoo Finance |
| JPM        | 2026-06-26 00:00:00 |   329.05      |          61.0833  | LONG     | Yahoo Finance |
| LLY        | 2026-06-26 00:00:00 |  1208.12      |          41.75    | LONG     | Yahoo Finance |
| LRCX       | 2026-06-26 00:00:00 |   379.09      |          73.9167  | LONG     | Yahoo Finance |
| MS         | 2026-06-26 00:00:00 |   212.03      |          30.0833  | LONG     | Yahoo Finance |
| PG         | 2026-06-26 00:00:00 |   149.02      |          56.6667  | LONG     | Yahoo Finance |
| RTX        | 2026-06-26 00:00:00 |   187.99      |          63.8333  | LONG     | Yahoo Finance |
| SBUX       | 2026-06-26 00:00:00 |   104.6       |          74.75    | LONG     | Yahoo Finance |
| TIA-USD    | 2026-06-29 00:00:00 |     0.3742    |          37.75    | LONG     | Kraken API    |
| TMO        | 2026-06-26 00:00:00 |   513.03      |          56.25    | LONG     | Yahoo Finance |
| UNH        | 2026-06-26 00:00:00 |   427.89      |          72.9167  | LONG     | Yahoo Finance |
| UPS        | 2026-06-26 00:00:00 |   108.14      |          37.9167  | LONG     | Yahoo Finance |
| VZ         | 2026-06-26 00:00:00 |    46.54      |          53.6667  | LONG     | Yahoo Finance |
| WFC        | 2026-06-26 00:00:00 |    83.86      |          55.9167  | LONG     | Yahoo Finance |
| XBI        | 2026-06-26 00:00:00 |   155.38      |          75.75    | LONG     | Yahoo Finance |
| XLF        | 2026-06-26 00:00:00 |    53.57      |          63.4167  | LONG     | Yahoo Finance |
| AAPL       | 2026-06-26 00:00:00 |   283.78      |         -29.5833  | NEUTRAL  | Yahoo Finance |
| ABBV       | 2026-06-26 00:00:00 |   253.35      |          51.1667  | NEUTRAL  | Yahoo Finance |
| AGG        | 2026-06-26 00:00:00 |    99.34      |          58.25    | NEUTRAL  | Yahoo Finance |
| ALGO-USD   | 2026-06-29 00:00:00 |     0.08804   |         -29.9167  | NEUTRAL  | Kraken API    |
| AMD        | 2026-06-26 00:00:00 |   521.58      |          47.3333  | NEUTRAL  | Yahoo Finance |
| AMGN       | 2026-06-26 00:00:00 |   358.33      |          55.3333  | NEUTRAL  | Yahoo Finance |
| APT-USD    | 2026-06-29 00:00:00 |     0.5698    |         -25.6667  | NEUTRAL  | Kraken API    |
| ARB-USD    | 2026-06-29 00:00:00 |     0.0735    |         -38.25    | NEUTRAL  | Kraken API    |
| ARKK       | 2026-06-26 00:00:00 |    78.13      |          26.75    | NEUTRAL  | Yahoo Finance |
| AVAX-USD   | 2026-06-29 00:00:00 |     6.417     |         -15.1667  | NEUTRAL  | Kraken API    |
| BA         | 2026-06-26 00:00:00 |   217.25      |         -43.3333  | NEUTRAL  | Yahoo Finance |
| BCH-USD    | 2026-06-29 00:00:00 |   190.37      |         -58.25    | NEUTRAL  | Kraken API    |
| BLK        | 2026-06-26 00:00:00 |   964.71      |         -61.25    | NEUTRAL  | Yahoo Finance |
| BND        | 2026-06-26 00:00:00 |    73.67      |          34.5833  | NEUTRAL  | Yahoo Finance |
| BONK-USD   | 2026-06-29 00:00:00 |     4.125e-06 |         -40.25    | NEUTRAL  | Kraken API    |
| CL         | 2026-06-26 00:00:00 |    92.07      |          65.6667  | NEUTRAL  | Yahoo Finance |
| CMCSA      | 2026-06-26 00:00:00 |    23.17      |         -21.75    | NEUTRAL  | Yahoo Finance |
| COST       | 2026-06-26 00:00:00 |   952.54      |         -23.75    | NEUTRAL  | Yahoo Finance |
| CSCO       | 2026-06-26 00:00:00 |   113.77      |          14.1667  | NEUTRAL  | Yahoo Finance |
| DASH-USD   | 2026-06-29 00:00:00 |    32.119     |         -76.0833  | NEUTRAL  | Kraken API    |
| DBC        | 2026-06-26 00:00:00 |    26.57      |         -13.6667  | NEUTRAL  | Yahoo Finance |
| DIA        | 2026-06-26 00:00:00 |   517.75      |          28.5     | NEUTRAL  | Yahoo Finance |
| EEM        | 2026-06-26 00:00:00 |    67.19      |           9.5     | NEUTRAL  | Yahoo Finance |
| EFA        | 2026-06-26 00:00:00 |   102.54      |         -23.4167  | NEUTRAL  | Yahoo Finance |
| EOG        | 2026-06-26 00:00:00 |   132.6       |         -23.0833  | NEUTRAL  | Yahoo Finance |
| ETC-USD    | 2026-06-29 00:00:00 |     7.004     |         -33.5833  | NEUTRAL  | Kraken API    |
| ETH-USD    | 2026-06-29 00:00:00 |  1558.62      |         -67.9167  | NEUTRAL  | Kraken API    |
| EWJ        | 2026-06-26 00:00:00 |    92.8       |           9.33333 | NEUTRAL  | Yahoo Finance |
| FCX        | 2026-06-26 00:00:00 |    62.45      |         -19.5833  | NEUTRAL  | Yahoo Finance |
| FIL-USD    | 2026-06-29 00:00:00 |     0.71      |         -53.5833  | NEUTRAL  | Kraken API    |
| GDX        | 2026-06-26 00:00:00 |    77         |         -63.5     | NEUTRAL  | Yahoo Finance |
| GDXJ       | 2026-06-26 00:00:00 |   100.29      |         -56.3333  | NEUTRAL  | Yahoo Finance |
| GRT-USD    | 2026-06-29 00:00:00 |     0.01756   |         -40.25    | NEUTRAL  | Kraken API    |
| GS         | 2026-06-26 00:00:00 |  1019.61      |          -3.83333 | NEUTRAL  | Yahoo Finance |
| HYG        | 2026-06-26 00:00:00 |    79.83      |         -22.5833  | NEUTRAL  | Yahoo Finance |
| IBM        | 2026-06-26 00:00:00 |   271.63      |          22.3333  | NEUTRAL  | Yahoo Finance |
| ICP-USD    | 2026-06-29 00:00:00 |     2.143     |         -53.5833  | NEUTRAL  | Kraken API    |
| IEF        | 2026-06-26 00:00:00 |    95.03      |          35.0833  | NEUTRAL  | Yahoo Finance |
| IEMG       | 2026-06-26 00:00:00 |    81.3       |           9.5     | NEUTRAL  | Yahoo Finance |
| INJ-USD    | 2026-06-29 00:00:00 |     4.577     |         -64.8333  | NEUTRAL  | Kraken API    |
| INTC       | 2026-06-26 00:00:00 |   128.32      |          52.8333  | NEUTRAL  | Yahoo Finance |
| IWM        | 2026-06-26 00:00:00 |   299.83      |          59.5     | NEUTRAL  | Yahoo Finance |
| JNJ        | 2026-06-26 00:00:00 |   254.66      |          68       | NEUTRAL  | Yahoo Finance |
| KO         | 2026-06-26 00:00:00 |    82.63      |          73.3333  | NEUTRAL  | Yahoo Finance |
| LDO-USD    | 2026-06-29 00:00:00 |     0.246     |         -38.25    | NEUTRAL  | Kraken API    |
| LIN        | 2026-06-26 00:00:00 |   519.62      |          59.1667  | NEUTRAL  | Yahoo Finance |
| LINK-USD   | 2026-06-29 00:00:00 |     7.2196    |         -60.5833  | NEUTRAL  | Kraken API    |
| LTC-USD    | 2026-06-29 00:00:00 |    42.56      |         -32.9167  | NEUTRAL  | Kraken API    |
| MCD        | 2026-06-26 00:00:00 |   269.76      |         -64.25    | NEUTRAL  | Yahoo Finance |
| META       | 2026-06-26 00:00:00 |   550.25      |         -65.3333  | NEUTRAL  | Yahoo Finance |
| MPC        | 2026-06-26 00:00:00 |   254.06      |           9.41667 | NEUTRAL  | Yahoo Finance |
| MRK        | 2026-06-26 00:00:00 |   128.66      |          64.5     | NEUTRAL  | Yahoo Finance |
| MU         | 2026-06-26 00:00:00 |  1132.33      |          50.6667  | NEUTRAL  | Yahoo Finance |
| NEAR-USD   | 2026-06-29 00:00:00 |     1.8167    |         -37.8333  | NEUTRAL  | Kraken API    |
| NEM        | 2026-06-26 00:00:00 |    96.13      |         -62       | NEUTRAL  | Yahoo Finance |
| NKE        | 2026-06-26 00:00:00 |    40.75      |         -62.8333  | NEUTRAL  | Yahoo Finance |
| OP-USD     | 2026-06-29 00:00:00 |     0.0995    |         -36.9167  | NEUTRAL  | Kraken API    |
| PEP        | 2026-06-26 00:00:00 |   141.39      |         -40.5     | NEUTRAL  | Yahoo Finance |
| PFE        | 2026-06-26 00:00:00 |    24.29      |         -53       | NEUTRAL  | Yahoo Finance |
| PM         | 2026-06-26 00:00:00 |   180.77      |          44.75    | NEUTRAL  | Yahoo Finance |
| POL-USD    | 2026-06-29 00:00:00 |     0.07108   |         -51.5833  | NEUTRAL  | Kraken API    |
| QCOM       | 2026-06-26 00:00:00 |   189.39      |         -24.3333  | NEUTRAL  | Yahoo Finance |
| QQQ        | 2026-06-26 00:00:00 |   706.52      |           7.83333 | NEUTRAL  | Yahoo Finance |
| SCHW       | 2026-06-26 00:00:00 |    90.67      |          18.4167  | NEUTRAL  | Yahoo Finance |
| SHY        | 2026-06-26 00:00:00 |    82.19      |          17.9167  | NEUTRAL  | Yahoo Finance |
| SMH        | 2026-06-26 00:00:00 |   611.61      |          14.3333  | NEUTRAL  | Yahoo Finance |
| SNX-USD    | 2026-06-29 00:00:00 |     0.2189    |         -37.9167  | NEUTRAL  | Kraken API    |
| SOL-USD    | 2026-06-29 00:00:00 |    70.9       |         -30.0833  | NEUTRAL  | Kraken API    |
| SOXX       | 2026-06-26 00:00:00 |   589.94      |          14.5     | NEUTRAL  | Yahoo Finance |
| SUSHI-USD  | 2026-06-29 00:00:00 |     0.1482    |         -64.5833  | NEUTRAL  | Kraken API    |
| TGT        | 2026-06-26 00:00:00 |   140.39      |          57.5     | NEUTRAL  | Yahoo Finance |
| TLT        | 2026-06-26 00:00:00 |    87.36      |          56.25    | NEUTRAL  | Yahoo Finance |
| TMUS       | 2026-06-26 00:00:00 |   182.68      |          -8.08333 | NEUTRAL  | Yahoo Finance |
| TRX-USD    | 2026-06-29 00:00:00 |     0.321597  |          22.1667  | NEUTRAL  | Kraken API    |
| TXN        | 2026-06-26 00:00:00 |   285.43      |          -5.41667 | NEUTRAL  | Yahoo Finance |
| UNI-USD    | 2026-06-29 00:00:00 |     2.9255    |           5.83333 | NEUTRAL  | Kraken API    |
| USO        | 2026-06-26 00:00:00 |   105.48      |         -19.6667  | NEUTRAL  | Yahoo Finance |
| VEA        | 2026-06-26 00:00:00 |    70.56      |          11       | NEUTRAL  | Yahoo Finance |
| VIXY       | 2026-06-26 00:00:00 |    22.62      |         -20.6667  | NEUTRAL  | Yahoo Finance |
| VNQ        | 2026-06-26 00:00:00 |    98.67      |          60.3333  | NEUTRAL  | Yahoo Finance |
| VTI        | 2026-06-26 00:00:00 |   362.22      |          -6.91667 | NEUTRAL  | Yahoo Finance |
| VWO        | 2026-06-26 00:00:00 |    58.58      |         -24.5     | NEUTRAL  | Yahoo Finance |
| WIF-USD    | 2026-06-29 00:00:00 |     0.173     |           5.75    | NEUTRAL  | Kraken API    |
| WMT        | 2026-06-26 00:00:00 |   115.69      |         -42.4167  | NEUTRAL  | Yahoo Finance |
| XLB        | 2026-06-26 00:00:00 |    51.6       |          61.1667  | NEUTRAL  | Yahoo Finance |
| XLE        | 2026-06-26 00:00:00 |    53.84      |          -9.83333 | NEUTRAL  | Yahoo Finance |
| XLI        | 2026-06-26 00:00:00 |   181.2       |          63.1667  | NEUTRAL  | Yahoo Finance |
| XLK        | 2026-06-26 00:00:00 |   181.11      |           4.5     | NEUTRAL  | Yahoo Finance |
| XLM-USD    | 2026-06-29 00:00:00 |     0.171047  |         -55.5833  | NEUTRAL  | Kraken API    |
| XLP        | 2026-06-26 00:00:00 |    84.71      |          56       | NEUTRAL  | Yahoo Finance |
| XLU        | 2026-06-26 00:00:00 |    46.2       |          47.3333  | NEUTRAL  | Yahoo Finance |
| XLV        | 2026-06-26 00:00:00 |   160.34      |          53       | NEUTRAL  | Yahoo Finance |
| XLY        | 2026-06-26 00:00:00 |   114.37      |         -49.0833  | NEUTRAL  | Yahoo Finance |
| XRP-USD    | 2026-06-29 00:00:00 |     1.03849   |         -60.5833  | NEUTRAL  | Kraken API    |
| YFI-USD    | 2026-06-29 00:00:00 |  1633         |         -64.5833  | NEUTRAL  | Kraken API    |
| ZEC-USD    | 2026-06-29 00:00:00 |   373.19      |         -68.5833  | NEUTRAL  | Kraken API    |
| ADA-USD    | 2026-06-29 00:00:00 |     0.142939  |         -31       | SHORT    | Kraken API    |
| ADBE       | 2026-06-26 00:00:00 |   202.73      |         -58.9167  | SHORT    | Yahoo Finance |
| AMZN       | 2026-06-26 00:00:00 |   232.69      |         -33.0833  | SHORT    | Yahoo Finance |
| ATOM-USD   | 2026-06-29 00:00:00 |     1.567     |         -53.3333  | SHORT    | Kraken API    |
| AVGO       | 2026-06-26 00:00:00 |   365.02      |         -33.0833  | SHORT    | Yahoo Finance |
| BITO       | 2026-06-26 00:00:00 |     8.12      |         -44.5833  | SHORT    | Yahoo Finance |
| BTC-USD    | 2026-06-29 00:00:00 | 59165.6       |         -60.5833  | SHORT    | Kraken API    |
| COMP-USD   | 2026-06-29 00:00:00 |    15.53      |         -51.3333  | SHORT    | Kraken API    |
| COP        | 2026-06-26 00:00:00 |   105.96      |         -40.5     | SHORT    | Yahoo Finance |
| CRM        | 2026-06-26 00:00:00 |   158.37      |         -58.9167  | SHORT    | Yahoo Finance |
| CRV-USD    | 2026-06-29 00:00:00 |     0.19034   |         -51.3333  | SHORT    | Kraken API    |
| CVX        | 2026-06-26 00:00:00 |   171.06      |         -47.5833  | SHORT    | Yahoo Finance |
| DIS        | 2026-06-26 00:00:00 |    98.79      |         -48.25    | SHORT    | Yahoo Finance |
| DOGE-USD   | 2026-06-29 00:00:00 |     0.0725631 |         -51.3333  | SHORT    | Kraken API    |
| DOT-USD    | 2026-06-29 00:00:00 |     0.8131    |         -51.3333  | SHORT    | Kraken API    |
| FET-USD    | 2026-06-29 00:00:00 |     0.1764    |         -51.3333  | SHORT    | Kraken API    |
| FXI        | 2026-06-26 00:00:00 |    31.59      |         -59.0833  | SHORT    | Yahoo Finance |
| GLD        | 2026-06-26 00:00:00 |   373.63      |         -50.25    | SHORT    | Yahoo Finance |
| GOOGL      | 2026-06-26 00:00:00 |   337.39      |         -37.0833  | SHORT    | Yahoo Finance |
| HBAR-USD   | 2026-06-29 00:00:00 |     0.07108   |         -47.3333  | SHORT    | Kraken API    |
| IBIT       | 2026-06-26 00:00:00 |    33.85      |         -44.5833  | SHORT    | Yahoo Finance |
| INTU       | 2026-06-26 00:00:00 |   267.72      |         -40.6667  | SHORT    | Yahoo Finance |
| MSFT       | 2026-06-26 00:00:00 |   372.97      |         -57.3333  | SHORT    | Yahoo Finance |
| NFLX       | 2026-06-26 00:00:00 |    73.81      |         -57       | SHORT    | Yahoo Finance |
| NOW        | 2026-06-26 00:00:00 |    98.34      |         -53.0833  | SHORT    | Yahoo Finance |
| NVDA       | 2026-06-26 00:00:00 |   192.53      |         -26.5     | SHORT    | Yahoo Finance |
| ORCL       | 2026-06-26 00:00:00 |   148.53      |         -65.5833  | SHORT    | Yahoo Finance |
| OXY        | 2026-06-26 00:00:00 |    49.99      |         -44.3333  | SHORT    | Yahoo Finance |
| PEPE-USD   | 2026-06-29 00:00:00 |     2.342e-06 |         -53.3333  | SHORT    | Kraken API    |
| RENDER-USD | 2026-06-29 00:00:00 |     1.526     |         -42.3333  | SHORT    | Kraken API    |
| SHIB-USD   | 2026-06-29 00:00:00 |     4.151e-06 |         -51.3333  | SHORT    | Kraken API    |
| SKY-USD    | 2026-06-29 00:00:00 |     0.04938   |         -62.8333  | SHORT    | Kraken API    |
| SLB        | 2026-06-26 00:00:00 |    47         |         -45.8333  | SHORT    | Yahoo Finance |
| SLV        | 2026-06-26 00:00:00 |    53.28      |         -57.5833  | SHORT    | Yahoo Finance |
| SPY        | 2026-06-26 00:00:00 |   728.99      |         -32.0833  | SHORT    | Yahoo Finance |
| T          | 2026-06-26 00:00:00 |    22.72      |         -30.75    | SHORT    | Yahoo Finance |
| TSLA       | 2026-06-26 00:00:00 |   379.71      |         -50.25    | SHORT    | Yahoo Finance |
| XLC        | 2026-06-26 00:00:00 |   106.18      |         -55.4167  | SHORT    | Yahoo Finance |
| XOM        | 2026-06-26 00:00:00 |   136.54      |         -43.8333  | SHORT    | Yahoo Finance |

## Edge Summary

- Symbols with trades: **160** of 160
- Beat buy-and-hold: **36.25%** of traded symbols
- Positive return: **33.75%** of traded symbols
- Median strategy return: **-9.30%** (benchmark **13.57%**)
- Median excess vs benchmark: **-26.29%**
- Median Sharpe: **-0.04**
- Median exposure: **44.51%**

> Edge is real only if both _beat buy-and-hold_ and _median excess_ are convincingly positive across many symbols. Treat a single high-return symbol as noise.

## Portfolio Backtest

Actual capital-allocation books (not per-symbol averages). Benchmarks: `equal_weight_buyhold` (whole tracked universe), `spy_buyhold` (100% SPY), and `sixty_forty` (60% SPY / 40% AGG). `high_conf_voltarget` inverse-vol-weights the HIGH-confidence book; `conviction_long_short` is market-neutral. Judge on **Sharpe** and **max_drawdown** out-of-sample, not raw return: a fully-invested long book wins on return in a bull market but carries all the risk.

| strategy              | scope         | ann_return   | ann_vol   |   sharpe | max_drawdown   | total_return   |   avg_gross_exposure |
|:----------------------|:--------------|:-------------|:----------|---------:|:---------------|:---------------|---------------------:|
| equal_weight_buyhold  | full          | -9.70%       | 33.38%    |    -0.29 | -54.94%        | -37.32%        |                 1    |
| equal_weight_buyhold  | out_of_sample | -13.80%      | 34.16%    |    -0.4  | -39.63%        | -18.90%        |                 1    |
| all_signals_ew        | full          | -9.48%       | 28.15%    |    -0.34 | -59.82%        | -33.63%        |                 1    |
| all_signals_ew        | out_of_sample | 8.42%        | 28.59%    |     0.29 | -23.70%        | 4.77%          |                 1    |
| high_conf_ew          | full          | 5.68%        | 32.25%    |     0.18 | -44.63%        | 1.70%          |                 0.88 |
| high_conf_ew          | out_of_sample | 12.27%       | 35.11%    |     0.35 | -20.80%        | 6.91%          |                 0.88 |
| high_conf_voltarget   | full          | 6.40%        | 29.82%    |     0.21 | -36.61%        | 6.39%          |                 0.88 |
| high_conf_voltarget   | out_of_sample | 7.80%        | 32.78%    |     0.24 | -16.98%        | 2.78%          |                 0.88 |
| conviction_long_short | full          | -12.44%      | 23.46%    |    -0.53 | -41.32%        | -37.09%        |                 0.97 |
| conviction_long_short | out_of_sample | -11.96%      | 26.88%    |    -0.44 | -21.04%        | -15.34%        |                 0.97 |
| spy_buyhold           | full          | 7.17%        | 13.36%    |     0.54 | -17.81%        | 21.09%         |                 0.78 |
| spy_buyhold           | out_of_sample | -5.29%       | 10.10%    |    -0.52 | -14.83%        | -6.00%         |                 0.78 |
| sixty_forty           | full          | 4.21%        | 8.48%     |     0.5  | -10.80%        | 12.43%         |                 0.78 |
| sixty_forty           | out_of_sample | -3.89%       | 6.56%     |    -0.59 | -10.06%        | -4.29%         |                 0.78 |

## Walk-Forward Robustness

Each book measured across contiguous time folds (each a different regime). A book has durable edge only if `mean_sharpe` is positive, `min_sharpe` isn't deeply negative, and `pct_positive_folds` is high — a single great fold doesn't count. `fold_sharpes` lists each fold oldest-to-newest.

| strategy              |   n_folds |   mean_sharpe |   median_sharpe |   min_sharpe | pct_positive_folds   | mean_return   | fold_sharpes                  |
|:----------------------|----------:|--------------:|----------------:|-------------:|:---------------------|:--------------|:------------------------------|
| equal_weight_buyhold  |         5 |         -0.04 |           -0.21 |        -1.35 | 40.00%               | -7.59%        | 1.48;-1.35;0.40;-0.51;-0.21   |
| all_signals_ew        |         5 |         -0.23 |            0.13 |        -1.31 | 60.00%               | -6.97%        | 0.13;0.18;-1.31;-0.77;0.63    |
| high_conf_ew          |         5 |          0.39 |            0.45 |        -0.93 | 80.00%               | 1.25%         | 1.37;0.45;-0.93;0.34;0.73     |
| high_conf_voltarget   |         5 |          0.51 |            0.47 |        -1.02 | 80.00%               | 2.18%         | 2.10;0.73;-1.02;0.47;0.25     |
| conviction_long_short |         5 |         -0.58 |           -0.6  |        -1.41 | 0.00%                | -8.72%        | -1.41;-0.69;-0.19;-0.60;-0.01 |
| spy_buyhold           |         5 |          0.5  |            0.47 |        -0.4  | 60.00%               | 4.05%         | 1.62;0.93;0.47;-0.11;-0.40    |
| sixty_forty           |         5 |          0.44 |            0.52 |        -0.51 | 60.00%               | 2.45%         | 1.72;0.55;0.52;-0.07;-0.51    |

## Strategy Comparison

Each decision rule backtested over the same data. `out_of_sample` is the most recent ~35% of each symbol's history (unseen tail). A rule has real edge only if `median_excess` and `beat_benchmark_pct` stay positive out-of-sample, not just full-sample.

| strategy        | scope         |   symbols | beat_benchmark_pct   | positive_pct   | median_return   | median_benchmark   | median_excess   |   median_sharpe |   total_trades |
|:----------------|:--------------|----------:|:---------------------|:---------------|:----------------|:-------------------|:----------------|----------------:|---------------:|
| trend           | full          |       160 | 36.25%               | 33.75%         | -9.30%          | 13.57%             | -26.29%         |           -0.04 |          11235 |
| trend           | out_of_sample |       160 | 40.62%               | 55.62%         | 3.66%           | 3.95%              | -4.14%          |            0.34 |           3908 |
| mean_reversion  | full          |       157 | 41.40%               | 49.68%         | -0.03%          | 12.92%             | -16.30%         |            0.01 |           1250 |
| mean_reversion  | out_of_sample |       127 | 47.24%               | 58.27%         | 0.33%           | 1.16%              | -1.94%          |            0.65 |            476 |
| regime_adaptive | full          |       160 | 36.88%               | 33.75%         | -8.75%          | 13.57%             | -26.40%         |           -0.05 |          11504 |
| regime_adaptive | out_of_sample |       160 | 41.25%               | 56.25%         | 3.66%           | 3.95%              | -5.15%          |            0.34 |           4005 |

## Signal Calibration

Realized forward return in the signal's direction, grouped by confidence. HIGH should outrank LOW for the confidence score to be meaningful.

| confidence_level   |   horizon |     n | mean_return   | median_return   | win_rate   |
|:-------------------|----------:|------:|:--------------|:----------------|:-----------|
| HIGH               |         5 |  8112 | 0.19%         | 0.13%           | 52.24%     |
| MEDIUM             |         5 | 29224 | 0.09%         | 0.11%           | 51.21%     |
| LOW                |         5 |  3278 | -0.58%        | -0.51%          | 44.97%     |
| ALL                |         5 | 40614 | 0.05%         | 0.07%           | 50.92%     |
| HIGH               |        10 |  8067 | 0.49%         | 0.18%           | 52.14%     |
| MEDIUM             |        10 | 29067 | 0.26%         | 0.17%           | 51.41%     |
| LOW                |        10 |  3270 | -0.93%        | -0.75%          | 45.11%     |
| ALL                |        10 | 40404 | 0.21%         | 0.12%           | 51.04%     |
| HIGH               |        20 |  7990 | 0.93%         | 0.47%           | 53.64%     |
| MEDIUM             |        20 | 28614 | 0.96%         | 0.67%           | 53.87%     |
| LOW                |        20 |  3231 | -0.68%        | -0.50%          | 47.17%     |
| ALL                |        20 | 39835 | 0.82%         | 0.55%           | 53.28%     |

## Backtest Summary

### Data Quality / Signal Availability

- **ok**: 160 symbols

| symbol     |   trades | return   | benchmark_return   | mdd     |   sharpe | exposure   | skipped_reason   |
|:-----------|---------:|:---------|:-------------------|:--------|---------:|:-----------|:-----------------|
| AAPL       |       63 | 12.35%   | 52.69%             | -20.65% |     0.34 | 48.59%     | ok               |
| AAVE-USD   |       76 | -52.24%  | -72.91%            | -68.26% |    -0.51 | 36.40%     | ok               |
| ABBV       |       64 | -16.28%  | 50.20%             | -30.55% |    -0.33 | 47.75%     | ok               |
| ADA-USD    |       88 | -81.96%  | -85.29%            | -89.12% |    -0.63 | 46.55%     | ok               |
| ADBE       |       68 | -26.18%  | -68.06%            | -37.59% |    -0.3  | 57.40%     | ok               |
| AGG        |       67 | -6.37%   | 0.89%              | -9.93%  |    -1.06 | 30.95%     | ok               |
| ALGO-USD   |       86 | -50.43%  | -78.01%            | -53.13% |    -0.57 | 38.12%     | ok               |
| AMAT       |       69 | -13.89%  | 272.72%            | -57.21% |    -0    | 53.41%     | ok               |
| AMD        |       56 | 0.99%    | 193.58%            | -45.32% |     0.22 | 37.10%     | ok               |
| AMGN       |       71 | -22.76%  | 10.87%             | -34.14% |    -0.48 | 46.92%     | ok               |
| AMZN       |       78 | -35.92%  | 35.43%             | -42.48% |    -1.06 | 38.60%     | ok               |
| APT-USD    |       76 | -26.57%  | -93.06%            | -69.96% |    -0    | 44.25%     | ok               |
| ARB-USD    |       68 | -0.31%   | -89.47%            | -62.67% |     0.24 | 39.27%     | ok               |
| ARKK       |       81 | -32.67%  | 67.45%             | -35.19% |    -0.57 | 38.94%     | ok               |
| ATOM-USD   |       90 | -67.07%  | -74.78%            | -73.34% |    -1.09 | 45.02%     | ok               |
| AVAX-USD   |       74 | -34.19%  | -81.84%            | -60.45% |    -0.24 | 39.66%     | ok               |
| AVGO       |       60 | 30.11%   | 198.14%            | -35.76% |     0.49 | 44.43%     | ok               |
| BA         |       67 | 7.60%    | 3.76%              | -30.56% |     0.25 | 49.25%     | ok               |
| BAC        |       78 | -11.45%  | 72.93%             | -26.76% |    -0.24 | 47.42%     | ok               |
| BCH-USD    |       78 | -10.24%  | -55.95%            | -54.90% |     0.09 | 50.00%     | ok               |
| BITO       |       78 | 12.36%   | -60.10%            | -42.82% |     0.31 | 41.43%     | ok               |
| BLK        |       75 | -11.50%  | 22.43%             | -24.29% |    -0.28 | 43.43%     | ok               |
| BND        |       65 | -7.32%   | 0.92%              | -9.89%  |    -1.18 | 32.28%     | ok               |
| BONK-USD   |       70 | 70.45%   | -86.12%            | -45.22% |     0.72 | 41.95%     | ok               |
| BTC-USD    |       72 | 8.02%    | -43.57%            | -23.38% |     0.27 | 51.53%     | ok               |
| C          |       83 | -26.73%  | 155.24%            | -38.66% |    -0.51 | 51.58%     | ok               |
| CAT        |       72 | 32.89%   | 216.57%            | -21.02% |     0.6  | 57.07%     | ok               |
| CL         |       60 | 12.58%   | 8.80%              | -14.32% |     0.46 | 47.09%     | ok               |
| CMCSA      |       82 | -40.57%  | -45.17%            | -40.26% |    -1.08 | 44.09%     | ok               |
| COMP-USD   |       91 | -36.37%  | -79.57%            | -58.43% |    -0.2  | 45.79%     | ok               |
| COP        |       73 | -22.02%  | -4.22%             | -43.77% |    -0.39 | 40.43%     | ok               |
| COST       |       60 | 2.26%    | 34.26%             | -29.73% |     0.14 | 45.76%     | ok               |
| CRM        |       67 | -37.40%  | -44.56%            | -40.31% |    -0.77 | 43.59%     | ok               |
| CRV-USD    |       64 | 1.71%    | -76.09%            | -39.89% |     0.25 | 35.25%     | ok               |
| CSCO       |       59 | 27.07%   | 126.72%            | -21.79% |     0.57 | 50.58%     | ok               |
| CVX        |       69 | -14.47%  | 12.36%             | -26.75% |    -0.36 | 40.93%     | ok               |
| DASH-USD   |       63 | -37.83%  | -7.89%             | -64.43% |     0.03 | 31.61%     | ok               |
| DBC        |       58 | -12.57%  | 21.82%             | -25.35% |    -0.43 | 32.78%     | ok               |
| DE         |       72 | -4.40%   | 56.20%             | -25.24% |     0    | 46.09%     | ok               |
| DIA        |       60 | -2.42%   | 33.99%             | -12.94% |    -0.09 | 45.92%     | ok               |
| DIS        |       68 | -7.40%   | 1.71%              | -28.17% |    -0.04 | 47.75%     | ok               |
| DOGE-USD   |       78 | -18.89%  | -79.31%            | -62.31% |     0.06 | 49.81%     | ok               |
| DOT-USD    |       92 | -45.47%  | -87.12%            | -61.52% |    -0.32 | 48.85%     | ok               |
| DXY-INDEX  |       44 | -2.01%   | 0.27%              | -6.06%  |    -0.3  | 30.80%     | ok               |
| EEM        |       64 | -9.40%   | 73.84%             | -25.67% |    -0.25 | 43.43%     | ok               |
| EFA        |       62 | -9.39%   | 36.45%             | -14.87% |    -0.35 | 44.59%     | ok               |
| EOG        |       79 | -25.51%  | 19.62%             | -48.13% |    -0.56 | 46.42%     | ok               |
| ETC-USD    |       64 | -35.69%  | -74.40%            | -48.16% |    -0.51 | 31.23%     | ok               |
| ETH-USD    |       62 | 166.33%  | -52.91%            | -30.11% |     1.32 | 45.02%     | ok               |
| EWJ        |       64 | -18.06%  | 39.53%             | -30.73% |    -0.58 | 39.93%     | ok               |
| FCX        |       67 | -31.31%  | 55.74%             | -46.84% |    -0.38 | 45.59%     | ok               |
| FET-USD    |       83 | -13.59%  | -85.60%            | -54.02% |     0.16 | 40.80%     | ok               |
| FIL-USD    |       68 | -28.94%  | -85.83%            | -45.42% |    -0.21 | 33.33%     | ok               |
| FXI        |       46 | -1.76%   | 47.55%             | -24.33% |     0.04 | 29.12%     | ok               |
| GDX        |       60 | 11.28%   | 174.80%            | -34.99% |     0.3  | 48.09%     | ok               |
| GDXJ       |       68 | -23.10%  | 194.97%            | -44.93% |    -0.22 | 46.42%     | ok               |
| GE         |       74 | 23.82%   | 238.62%            | -27.82% |     0.48 | 53.08%     | ok               |
| GLD        |       48 | 26.82%   | 98.10%             | -16.63% |     0.68 | 45.59%     | ok               |
| GOOGL      |       63 | 86.92%   | 136.96%            | -20.41% |     1.26 | 53.58%     | ok               |
| GRT-USD    |       85 | -3.45%   | -90.41%            | -54.83% |     0.19 | 42.72%     | ok               |
| GS         |       76 | -2.38%   | 162.88%            | -22.13% |     0.05 | 52.08%     | ok               |
| HD         |       75 | -5.67%   | -2.34%             | -18.58% |    -0.08 | 43.43%     | ok               |
| HON        |       92 | -27.38%  | 136.82%            | -30.98% |    -0.73 | 49.42%     | ok               |
| HYG        |       81 | -9.52%   | 3.42%              | -9.59%  |    -1.11 | 34.28%     | ok               |
| IBIT       |       32 | 42.51%   | -10.94%            | -18.95% |     0.85 | 31.65%     | ok               |
| IBM        |       76 | 0.33%    | 46.20%             | -27.52% |     0.11 | 50.08%     | ok               |
| ICP-USD    |       85 | -5.39%   | -76.31%            | -57.53% |     0.21 | 39.08%     | ok               |
| IEF        |       76 | -10.90%  | -0.55%             | -11.70% |    -1.54 | 32.78%     | ok               |
| IEMG       |       58 | -5.52%   | 66.80%             | -26.84% |    -0.12 | 43.59%     | ok               |
| INJ-USD    |       77 | -54.85%  | -77.91%            | -76.97% |    -0.54 | 38.31%     | ok               |
| INTC       |       70 | 55.82%   | 201.22%            | -60.60% |     0.62 | 49.25%     | ok               |
| INTU       |       67 | -15.84%  | -58.14%            | -43.77% |    -0.15 | 42.60%     | ok               |
| ITA        |       74 | -2.78%   | 91.52%             | -23.75% |    -0.01 | 47.59%     | ok               |
| IWM        |       48 | 9.40%    | 54.23%             | -12.83% |     0.39 | 35.77%     | ok               |
| JNJ        |       72 | 5.96%    | 62.61%             | -17.51% |     0.27 | 50.42%     | ok               |
| JPM        |       73 | -18.80%  | 88.32%             | -33.16% |    -0.45 | 53.41%     | ok               |
| KO         |       49 | 28.93%   | 36.49%             | -8.07%  |     1.03 | 37.77%     | ok               |
| LDO-USD    |       76 | -2.99%   | -87.68%            | -60.93% |     0.24 | 38.31%     | ok               |
| LIN        |       64 | 0.44%    | 27.64%             | -21.53% |     0.08 | 38.60%     | ok               |
| LINK-USD   |       69 | -11.40%  | -71.34%            | -49.35% |     0.12 | 41.57%     | ok               |
| LLY        |       69 | -16.35%  | 80.95%             | -53.34% |    -0.15 | 51.25%     | ok               |
| LRCX       |       80 | -11.95%  | 352.00%            | -63.56% |     0.03 | 46.26%     | ok               |
| LTC-USD    |       66 | -34.00%  | -64.14%            | -53.76% |    -0.29 | 48.47%     | ok               |
| MCD        |       75 | -2.55%   | -9.19%             | -18.81% |    -0.05 | 38.10%     | ok               |
| META       |       72 | -29.40%  | 15.84%             | -38.96% |    -0.49 | 49.75%     | ok               |
| MPC        |       71 | -13.74%  | 52.74%             | -44.76% |    -0.14 | 49.92%     | ok               |
| MRK        |       67 | -30.24%  | 1.78%              | -34.46% |    -0.73 | 45.76%     | ok               |
| MS         |       79 | -17.10%  | 142.96%            | -27.79% |    -0.35 | 49.42%     | ok               |
| MSFT       |       83 | -36.25%  | -9.30%             | -39.34% |    -0.94 | 48.25%     | ok               |
| MU         |       51 | 270.20%  | 1209.35%           | -68.76% |     1.34 | 59.90%     | ok               |
| NEAR-USD   |       89 | -7.13%   | -63.68%            | -61.57% |     0.19 | 42.53%     | ok               |
| NEM        |       74 | -29.57%  | 179.37%            | -38.49% |    -0.3  | 54.08%     | ok               |
| NFLX       |       62 | 36.97%   | 30.72%             | -21.09% |     0.77 | 54.74%     | ok               |
| NKE        |       91 | -48.19%  | -59.54%            | -57.25% |    -0.9  | 43.59%     | ok               |
| NOW        |       80 | 17.95%   | -37.07%            | -30.25% |     0.38 | 45.92%     | ok               |
| NVDA       |       76 | -25.40%  | 115.23%            | -45.02% |    -0.17 | 58.29%     | ok               |
| OP-USD     |       74 | 3.40%    | -94.19%            | -70.27% |     0.28 | 35.63%     | ok               |
| ORCL       |       74 | 84.52%   | 28.28%             | -29.47% |     0.81 | 53.58%     | ok               |
| OXY        |       63 | 8.90%    | -12.36%            | -29.70% |     0.27 | 43.43%     | ok               |
| PEP        |       85 | -8.13%   | -17.30%            | -21.35% |    -0.17 | 50.25%     | ok               |
| PEPE-USD   |       77 | 20.61%   | -84.32%            | -57.66% |     0.44 | 44.06%     | ok               |
| PFE        |       77 | -40.64%  | -9.80%             | -42.29% |    -1.31 | 35.27%     | ok               |
| PG         |       62 | -13.00%  | -5.74%             | -21.65% |    -0.46 | 41.43%     | ok               |
| PM         |       81 | -0.35%   | 94.40%             | -33.68% |     0.09 | 57.24%     | ok               |
| POL-USD    |       81 | 82.79%   | -83.54%            | -46.45% |     0.88 | 51.53%     | ok               |
| QCOM       |       77 | -9.21%   | 33.67%             | -56.59% |     0.05 | 47.09%     | ok               |
| QQQ        |       62 | 18.71%   | 64.69%             | -12.88% |     0.54 | 45.59%     | ok               |
| RENDER-USD |       98 | -15.32%  | -63.32%            | -45.00% |     0.14 | 43.72%     | ok               |
| RTX        |       58 | 19.42%   | 104.38%            | -16.99% |     0.52 | 51.58%     | ok               |
| SBUX       |       64 | -22.19%  | 12.49%             | -29.34% |    -0.44 | 39.43%     | ok               |
| SCHW       |       76 | -24.21%  | 44.06%             | -31.92% |    -0.58 | 45.92%     | ok               |
| SHIB-USD   |       78 | -21.39%  | -79.18%            | -47.96% |    -0.04 | 52.87%     | ok               |
| SHY        |       48 | -2.24%   | 0.33%              | -2.85%  |    -0.79 | 34.28%     | ok               |
| SKY-USD    |       70 | -24.31%  | -14.61%            | -43.98% |    -0.26 | 41.19%     | ok               |
| SLB        |       77 | -26.14%  | -4.08%             | -55.49% |    -0.46 | 49.92%     | ok               |
| SLV        |       58 | 49.00%   | 156.77%            | -42.66% |     0.69 | 41.26%     | ok               |
| SMH        |       48 | 95.49%   | 219.85%            | -33.99% |     1.2  | 49.92%     | ok               |
| SNX-USD    |       62 | -7.32%   | -86.08%            | -34.76% |     0.18 | 39.46%     | ok               |
| SOL-USD    |       68 | -42.41%  | -72.01%            | -56.90% |    -0.22 | 59.96%     | ok               |
| SOXX       |       55 | 86.65%   | 196.72%            | -40.34% |     1.07 | 48.92%     | ok               |
| SPY        |       60 | 5.76%    | 47.46%             | -16.47% |     0.26 | 50.42%     | ok               |
| SUSHI-USD  |       90 | -79.45%  | -88.65%            | -84.18% |    -1.18 | 35.63%     | ok               |
| T          |       62 | 33.06%   | 27.43%             | -17.01% |     0.78 | 51.41%     | ok               |
| TGT        |       56 | -10.02%  | -3.51%             | -40.57% |    -0.12 | 38.44%     | ok               |
| TIA-USD    |       86 | -28.34%  | -91.76%            | -62.78% |    -0.07 | 35.06%     | ok               |
| TLT        |       72 | -20.93%  | -9.07%             | -20.85% |    -1.6  | 31.61%     | ok               |
| TMO        |       59 | 10.52%   | -7.03%             | -18.11% |     0.31 | 47.92%     | ok               |
| TMUS       |       68 | 15.42%   | 12.92%             | -24.50% |     0.41 | 47.59%     | ok               |
| TRX-USD    |       74 | -4.73%   | 26.55%             | -22.90% |    -0.04 | 49.81%     | ok               |
| TSLA       |       68 | 3.12%    | 102.07%            | -54.91% |     0.24 | 41.93%     | ok               |
| TXN        |       77 | -15.83%  | 79.29%             | -46.98% |    -0.1  | 53.41%     | ok               |
| UNH        |       76 | 30.58%   | -16.14%            | -27.93% |     0.53 | 52.41%     | ok               |
| UNI-USD    |       88 | -72.81%  | -76.53%            | -80.61% |    -0.89 | 41.76%     | ok               |
| UPS        |       74 | -38.18%  | -23.76%            | -39.98% |    -0.77 | 39.60%     | ok               |
| USO        |       66 | 8.43%    | 56.24%             | -43.35% |     0.26 | 34.11%     | ok               |
| VEA        |       58 | -0.98%   | 48.42%             | -17.93% |     0.01 | 44.09%     | ok               |
| VIXY       |       96 | -80.86%  | -62.05%            | -88.16% |    -1.03 | 32.78%     | ok               |
| VNQ        |       75 | -16.77%  | 16.98%             | -24.92% |    -0.7  | 37.60%     | ok               |
| VTI        |       66 | -1.07%   | 47.74%             | -18.77% |     0.02 | 51.41%     | ok               |
| VWO        |       76 | -13.41%  | 47.82%             | -25.20% |    -0.47 | 44.09%     | ok               |
| VZ         |       85 | -27.08%  | 10.47%             | -30.05% |    -0.94 | 37.10%     | ok               |
| WFC        |       82 | -17.88%  | 70.59%             | -29.78% |    -0.3  | 48.92%     | ok               |
| WIF-USD    |       68 | -43.81%  | -86.53%            | -57.06% |    -0.24 | 32.18%     | ok               |
| WMT        |       59 | 19.98%   | 104.68%            | -21.31% |     0.58 | 51.25%     | ok               |
| XBI        |       62 | 4.25%    | 76.63%             | -19.80% |     0.19 | 40.10%     | ok               |
| XLB        |       68 | -13.16%  | 24.20%             | -26.57% |    -0.45 | 37.27%     | ok               |
| XLC        |       65 | 15.65%   | 33.16%             | -12.33% |     0.55 | 55.57%     | ok               |
| XLE        |       71 | -9.48%   | 28.93%             | -36.18% |    -0.17 | 46.59%     | ok               |
| XLF        |       76 | -12.03%  | 37.43%             | -23.61% |    -0.4  | 48.25%     | ok               |
| XLI        |       64 | 3.12%    | 56.77%             | -11.38% |     0.18 | 45.92%     | ok               |
| XLK        |       42 | 64.31%   | 79.10%             | -14.75% |     1.2  | 47.42%     | ok               |
| XLM-USD    |       69 | 0.26%    | -60.29%            | -50.36% |     0.22 | 45.59%     | ok               |
| XLP        |       68 | 6.56%    | 14.21%             | -11.16% |     0.4  | 42.93%     | ok               |
| XLU        |       67 | -1.66%   | 50.27%             | -18.15% |    -0.03 | 38.10%     | ok               |
| XLV        |       66 | -12.12%  | 12.92%             | -16.83% |    -0.59 | 35.61%     | ok               |
| XLY        |       70 | 3.26%    | 29.00%             | -14.01% |     0.17 | 44.43%     | ok               |
| XOM        |       58 | 4.54%    | 33.90%             | -20.29% |     0.2  | 36.44%     | ok               |
| XRP-USD    |       62 | -32.87%  | -66.53%            | -45.79% |    -0.31 | 34.67%     | ok               |
| YFI-USD    |       81 | -52.55%  | -78.15%            | -67.78% |    -0.75 | 40.80%     | ok               |
| ZEC-USD    |       67 | 52.90%   | 707.07%            | -47.68% |     0.6  | 36.40%     | ok               |

## AAPL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 22.34%   | 52.69%             | -21.71% |     0.51 |       67 | 52.41%     | ok               |
|          15 | 17.34%   | 52.69%             | -23.86% |     0.42 |       76 | 59.73%     | ok               |
|          25 | 16.50%   | 52.69%             | -20.03% |     0.42 |       65 | 50.25%     | ok               |
|          30 | 12.35%   | 52.69%             | -20.65% |     0.34 |       63 | 48.59%     | ok               |
|          35 | 7.97%    | 52.69%             | -22.04% |     0.26 |       61 | 46.59%     | ok               |

## AAVE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 10.58%   | -72.91%            | -43.61% |     0.33 |       40 | 29.69%     | ok               |
|          45 | 2.34%    | -72.91%            | -46.87% |     0.23 |       40 | 25.67%     | ok               |
|          35 | -9.05%   | -72.91%            | -51.96% |     0.12 |       52 | 32.38%     | ok               |
|          50 | -31.15%  | -72.91%            | -43.73% |    -0.32 |       44 | 19.73%     | ok               |
|          15 | -53.20%  | -72.91%            | -61.76% |    -0.36 |       82 | 50.57%     | ok               |

## ABBV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.41%   | 50.20%             | -23.85% |     0.07 |       50 | 37.27%     | ok               |
|          40 | -12.81%  | 50.20%             | -26.61% |    -0.25 |       64 | 42.10%     | ok               |
|          35 | -14.05%  | 50.20%             | -27.83% |    -0.28 |       66 | 44.93%     | ok               |
|          30 | -16.28%  | 50.20%             | -30.55% |    -0.33 |       64 | 47.75%     | ok               |
|          45 | -15.52%  | 50.20%             | -29.59% |    -0.34 |       54 | 39.43%     | ok               |

## ADA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -80.49%  | -85.29%            | -91.26% |    -0.46 |       78 | 63.22%     | ok               |
|          20 | -82.02%  | -85.29%            | -91.79% |    -0.54 |       88 | 57.47%     | ok               |
|          50 | -78.05%  | -85.29%            | -86.04% |    -0.6  |       55 | 27.01%     | ok               |
|          25 | -83.78%  | -85.29%            | -91.94% |    -0.62 |       83 | 53.45%     | ok               |
|          45 | -80.39%  | -85.29%            | -88.08% |    -0.63 |       58 | 31.80%     | ok               |

## ADBE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 5.63%    | -68.06%            | -21.34% |     0.22 |       78 | 49.75%     | ok               |
|          25 | -11.52%  | -68.06%            | -30.83% |    -0.03 |       52 | 61.56%     | ok               |
|          40 | -8.00%   | -68.06%            | -20.88% |    -0.03 |       74 | 42.76%     | ok               |
|          15 | -20.96%  | -68.06%            | -31.45% |    -0.17 |       63 | 66.22%     | ok               |
|          20 | -22.51%  | -68.06%            | -33.98% |    -0.21 |       52 | 63.73%     | ok               |

## AGG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -6.37%   | 0.89%              | -9.93%  |    -1.06 |       67 | 30.95%     | ok               |
|          20 | -7.71%   | 0.89%              | -10.80% |    -1.13 |       69 | 36.27%     | ok               |
|          45 | -5.75%   | 0.89%              | -7.89%  |    -1.16 |       52 | 20.47%     | ok               |
|          25 | -7.88%   | 0.89%              | -11.32% |    -1.21 |       69 | 34.61%     | ok               |
|          50 | -5.57%   | 0.89%              | -7.92%  |    -1.25 |       46 | 16.97%     | ok               |

## ALGO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -50.43%  | -78.01%            | -53.13% |    -0.57 |       86 | 38.12%     | ok               |
|          15 | -61.07%  | -78.01%            | -69.47% |    -0.66 |       88 | 50.57%     | ok               |
|          25 | -61.32%  | -78.01%            | -73.33% |    -0.72 |       88 | 45.21%     | ok               |
|          20 | -65.02%  | -78.01%            | -72.09% |    -0.78 |       90 | 48.28%     | ok               |
|          50 | -45.64%  | -78.01%            | -48.43% |    -0.81 |       42 | 16.86%     | ok               |

## AMAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 2.89%    | 272.72%            | -54.05% |     0.22 |       66 | 62.06%     | ok               |
|          30 | -13.89%  | 272.72%            | -57.21% |    -0    |       69 | 53.41%     | ok               |
|          20 | -20.18%  | 272.72%            | -60.16% |    -0.07 |       72 | 58.57%     | ok               |
|          50 | -18.00%  | 272.72%            | -48.72% |    -0.1  |       52 | 39.27%     | ok               |
|          35 | -20.02%  | 272.72%            | -55.26% |    -0.1  |       71 | 51.25%     | ok               |

## AMD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 0.99%    | 193.58%            | -45.32% |     0.22 |       56 | 37.10%     | ok               |
|          50 | -0.79%   | 193.58%            | -46.99% |     0.19 |       60 | 31.45%     | ok               |
|          35 | -11.89%  | 193.58%            | -54.16% |     0.09 |       62 | 39.10%     | ok               |
|          45 | -19.32%  | 193.58%            | -54.69% |    -0.02 |       64 | 34.44%     | ok               |
|          30 | -23.51%  | 193.58%            | -59.51% |    -0.04 |       63 | 41.60%     | ok               |

## AMGN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -17.66%  | 10.87%             | -26.64% |    -0.31 |       73 | 53.08%     | ok               |
|          15 | -20.57%  | 10.87%             | -27.92% |    -0.36 |       71 | 58.74%     | ok               |
|          35 | -19.02%  | 10.87%             | -31.23% |    -0.38 |       69 | 43.09%     | ok               |
|          30 | -22.76%  | 10.87%             | -34.14% |    -0.48 |       71 | 46.92%     | ok               |
|          25 | -25.90%  | 10.87%             | -33.41% |    -0.55 |       67 | 49.25%     | ok               |

## AMZN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -19.91%  | 35.43%             | -28.70% |    -0.59 |       52 | 29.95%     | ok               |
|          50 | -25.03%  | 35.43%             | -35.48% |    -0.88 |       48 | 24.13%     | ok               |
|          45 | -27.77%  | 35.43%             | -35.47% |    -0.96 |       52 | 27.12%     | ok               |
|          35 | -31.91%  | 35.43%             | -38.29% |    -1    |       66 | 33.28%     | ok               |
|          30 | -35.92%  | 35.43%             | -42.48% |    -1.06 |       78 | 38.60%     | ok               |

## APT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 51.21%   | -93.06%            | -46.73% |     0.73 |       44 | 20.69%     | ok               |
|          45 | 14.97%   | -93.06%            | -63.86% |     0.37 |       60 | 26.82%     | ok               |
|          40 | -7.11%   | -93.06%            | -63.33% |     0.16 |       66 | 32.38%     | ok               |
|          20 | -13.84%  | -93.06%            | -70.51% |     0.16 |       73 | 52.68%     | ok               |
|          35 | -13.92%  | -93.06%            | -64.45% |     0.11 |       70 | 38.12%     | ok               |

## ARB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 72.02%   | -89.47%            | -53.74% |     0.72 |       87 | 56.70%     | ok               |
|          40 | 45.76%   | -89.47%            | -47.60% |     0.62 |       50 | 30.27%     | ok               |
|          35 | 31.50%   | -89.47%            | -56.00% |     0.51 |       60 | 33.72%     | ok               |
|          20 | 29.27%   | -89.47%            | -60.40% |     0.5  |       75 | 50.19%     | ok               |
|          45 | 24.86%   | -89.47%            | -50.83% |     0.46 |       56 | 23.37%     | ok               |

## ARKK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -24.32%  | 67.45%             | -34.75% |    -0.28 |       90 | 50.25%     | ok               |
|          20 | -28.79%  | 67.45%             | -34.66% |    -0.4  |       85 | 45.59%     | ok               |
|          30 | -32.67%  | 67.45%             | -35.19% |    -0.57 |       81 | 38.94%     | ok               |
|          35 | -33.82%  | 67.45%             | -36.30% |    -0.63 |       80 | 36.61%     | ok               |
|          40 | -35.22%  | 67.45%             | -36.71% |    -0.71 |       72 | 31.78%     | ok               |

## ATOM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -63.11%  | -74.78%            | -69.81% |    -0.9  |       93 | 51.34%     | ok               |
|          15 | -68.17%  | -74.78%            | -71.82% |    -0.97 |       93 | 60.73%     | ok               |
|          45 | -57.53%  | -74.78%            | -63.84% |    -1.03 |       76 | 29.31%     | ok               |
|          30 | -67.07%  | -74.78%            | -73.34% |    -1.09 |       90 | 45.02%     | ok               |
|          20 | -71.51%  | -74.78%            | -74.51% |    -1.13 |      101 | 54.98%     | ok               |

## AVAX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 18.71%   | -81.84%            | -32.41% |     0.41 |       36 | 19.35%     | ok               |
|          45 | 7.44%    | -81.84%            | -39.20% |     0.27 |       38 | 23.37%     | ok               |
|          15 | 0.52%    | -81.84%            | -52.46% |     0.26 |       65 | 53.83%     | ok               |
|          40 | -7.64%   | -81.84%            | -46.32% |     0.08 |       44 | 26.44%     | ok               |
|          25 | -16.70%  | -81.84%            | -52.93% |     0.04 |       73 | 44.44%     | ok               |

## AVGO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 30.11%   | 198.14%            | -35.76% |     0.49 |       60 | 44.43%     | ok               |
|          25 | 25.49%   | 198.14%            | -38.01% |     0.44 |       64 | 45.09%     | ok               |
|          35 | 21.26%   | 198.14%            | -36.19% |     0.4  |       70 | 41.76%     | ok               |
|          40 | 20.85%   | 198.14%            | -40.70% |     0.4  |       60 | 38.60%     | ok               |
|          50 | 14.88%   | 198.14%            | -35.84% |     0.34 |       62 | 32.45%     | ok               |

## BA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 27.46%   | 3.76%              | -13.34% |     0.7  |       42 | 31.61%     | ok               |
|          35 | 30.46%   | 3.76%              | -23.77% |     0.59 |       72 | 44.59%     | ok               |
|          40 | 21.47%   | 3.76%              | -23.87% |     0.49 |       46 | 38.77%     | ok               |
|          25 | 10.59%   | 3.76%              | -32.48% |     0.29 |       70 | 52.58%     | ok               |
|          30 | 7.60%    | 3.76%              | -30.56% |     0.25 |       67 | 49.25%     | ok               |

## BAC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -4.42%   | 72.93%             | -22.31% |    -0.08 |       60 | 36.61%     | ok               |
|          20 | -7.66%   | 72.93%             | -22.24% |    -0.1  |       82 | 52.08%     | ok               |
|          35 | -6.76%   | 72.93%             | -28.27% |    -0.13 |       70 | 43.59%     | ok               |
|          50 | -5.98%   | 72.93%             | -20.84% |    -0.14 |       58 | 33.44%     | ok               |
|          25 | -10.28%  | 72.93%             | -26.26% |    -0.2  |       80 | 50.08%     | ok               |

## BCH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -14.50%  | -55.95%            | -58.01% |     0.09 |       76 | 60.34%     | ok               |
|          30 | -10.24%  | -55.95%            | -54.90% |     0.09 |       78 | 50.00%     | ok               |
|          20 | -19.73%  | -55.95%            | -59.67% |     0.02 |       72 | 56.32%     | ok               |
|          40 | -21.22%  | -55.95%            | -61.24% |    -0.09 |       71 | 40.80%     | ok               |
|          25 | -29.75%  | -55.95%            | -64.70% |    -0.12 |       73 | 52.30%     | ok               |

## BITO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 21.07%   | -60.10%            | -32.29% |     0.41 |       54 | 25.96%     | ok               |
|          30 | 12.36%   | -60.10%            | -42.82% |     0.31 |       78 | 41.43%     | ok               |
|          15 | 5.31%    | -60.10%            | -48.38% |     0.26 |       87 | 50.25%     | ok               |
|          25 | 3.47%    | -60.10%            | -41.73% |     0.22 |       82 | 44.43%     | ok               |
|          35 | 0.37%    | -60.10%            | -47.25% |     0.18 |       70 | 37.60%     | ok               |

## BLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -5.80%   | 22.43%             | -21.48% |    -0.09 |       80 | 47.59%     | ok               |
|          35 | -5.42%   | 22.43%             | -17.97% |    -0.1  |       82 | 39.77%     | ok               |
|          40 | -7.21%   | 22.43%             | -20.08% |    -0.18 |       74 | 35.44%     | ok               |
|          25 | -10.52%  | 22.43%             | -23.36% |    -0.24 |       75 | 45.59%     | ok               |
|          30 | -11.50%  | 22.43%             | -24.29% |    -0.28 |       75 | 43.43%     | ok               |

## BND Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.45%   | 0.92%              | -9.32%  |    -0.94 |       63 | 37.94%     | ok               |
|          25 | -7.14%   | 0.92%              | -10.40% |    -1.09 |       67 | 35.94%     | ok               |
|          30 | -7.32%   | 0.92%              | -9.89%  |    -1.18 |       65 | 32.28%     | ok               |
|          15 | -8.65%   | 0.92%              | -10.85% |    -1.25 |       73 | 40.77%     | ok               |
|          45 | -7.22%   | 0.92%              | -9.57%  |    -1.39 |       50 | 22.13%     | ok               |

## BONK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 169.29%  | -86.12%            | -35.57% |     1.24 |       44 | 22.03%     | ok               |
|          25 | 155.05%  | -86.12%            | -47.99% |     1    |       65 | 48.28%     | ok               |
|          20 | 140.65%  | -86.12%            | -55.43% |     0.95 |       66 | 52.87%     | ok               |
|          15 | 146.15%  | -86.12%            | -63.45% |     0.94 |       69 | 57.85%     | ok               |
|          45 | 88.02%   | -86.12%            | -42.36% |     0.85 |       56 | 26.44%     | ok               |

## BTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 51.83%   | -43.57%            | -14.50% |     0.95 |       44 | 34.10%     | ok               |
|          45 | 41.09%   | -43.57%            | -15.18% |     0.81 |       44 | 30.65%     | ok               |
|          35 | 36.01%   | -43.57%            | -22.12% |     0.7  |       68 | 41.00%     | ok               |
|          30 | 19.68%   | -43.57%            | -21.75% |     0.45 |       72 | 47.70%     | ok               |
|          50 | 14.18%   | -43.57%            | -16.15% |     0.4  |       42 | 25.29%     | ok               |

## C Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -7.27%   | 155.24%            | -22.28% |    -0.13 |       66 | 36.44%     | ok               |
|          45 | -14.17%  | 155.24%            | -28.12% |    -0.3  |       78 | 40.43%     | ok               |
|          15 | -22.79%  | 155.24%            | -34.52% |    -0.37 |       75 | 59.90%     | ok               |
|          25 | -23.38%  | 155.24%            | -35.86% |    -0.42 |       73 | 53.58%     | ok               |
|          40 | -20.24%  | 155.24%            | -33.20% |    -0.45 |       82 | 42.93%     | ok               |

## CAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 32.89%   | 216.57%            | -21.02% |     0.6  |       72 | 57.07%     | ok               |
|          25 | 33.01%   | 216.57%            | -26.37% |     0.59 |       68 | 59.90%     | ok               |
|          20 | 30.32%   | 216.57%            | -25.65% |     0.55 |       78 | 63.23%     | ok               |
|          45 | 21.41%   | 216.57%            | -28.85% |     0.46 |       58 | 45.92%     | ok               |
|          15 | 20.21%   | 216.57%            | -30.60% |     0.42 |       71 | 69.22%     | ok               |

## CL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 13.07%   | 8.80%              | -12.98% |     0.56 |       42 | 31.11%     | ok               |
|          30 | 12.58%   | 8.80%              | -14.32% |     0.46 |       60 | 47.09%     | ok               |
|          45 | 7.91%    | 8.80%              | -13.51% |     0.36 |       46 | 34.11%     | ok               |
|          35 | 7.23%    | 8.80%              | -13.83% |     0.3  |       62 | 43.43%     | ok               |
|          40 | 4.12%    | 8.80%              | -12.70% |     0.21 |       56 | 38.10%     | ok               |

## CMCSA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -36.34%  | -45.17%            | -48.09% |    -0.81 |       88 | 58.57%     | ok               |
|          30 | -40.57%  | -45.17%            | -40.26% |    -1.08 |       82 | 44.09%     | ok               |
|          50 | -31.05%  | -45.17%            | -31.12% |    -1.21 |       52 | 15.97%     | ok               |
|          25 | -45.71%  | -45.17%            | -45.42% |    -1.24 |       90 | 49.42%     | ok               |
|          20 | -47.27%  | -45.17%            | -46.99% |    -1.27 |       94 | 54.58%     | ok               |

## COMP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -2.94%   | -79.57%            | -38.71% |     0.16 |       48 | 20.88%     | ok               |
|          25 | -37.52%  | -79.57%            | -60.58% |    -0.19 |       89 | 50.77%     | ok               |
|          30 | -36.37%  | -79.57%            | -58.43% |    -0.2  |       91 | 45.79%     | ok               |
|          15 | -45.82%  | -79.57%            | -65.55% |    -0.27 |      103 | 62.26%     | ok               |
|          40 | -40.82%  | -79.57%            | -47.89% |    -0.37 |       76 | 33.91%     | ok               |

## COP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -11.98%  | -4.22%             | -35.08% |    -0.2  |       50 | 27.45%     | ok               |
|          45 | -17.74%  | -4.22%             | -41.35% |    -0.35 |       60 | 30.28%     | ok               |
|          35 | -21.48%  | -4.22%             | -43.58% |    -0.39 |       75 | 37.27%     | ok               |
|          30 | -22.02%  | -4.22%             | -43.77% |    -0.39 |       73 | 40.43%     | ok               |
|          40 | -25.09%  | -4.22%             | -47.05% |    -0.54 |       70 | 33.11%     | ok               |

## COST Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 13.42%   | 34.26%             | -24.32% |     0.43 |       66 | 52.08%     | ok               |
|          25 | 12.43%   | 34.26%             | -24.73% |     0.41 |       63 | 49.42%     | ok               |
|          35 | 7.17%    | 34.26%             | -26.58% |     0.28 |       54 | 42.76%     | ok               |
|          30 | 2.26%    | 34.26%             | -29.73% |     0.14 |       60 | 45.76%     | ok               |
|          40 | 0.59%    | 34.26%             | -28.41% |     0.08 |       56 | 39.77%     | ok               |

## CRM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -32.66%  | -44.56%            | -41.65% |    -0.49 |       92 | 55.41%     | ok               |
|          35 | -27.12%  | -44.56%            | -35.48% |    -0.52 |       64 | 38.77%     | ok               |
|          30 | -37.40%  | -44.56%            | -40.31% |    -0.77 |       67 | 43.59%     | ok               |
|          40 | -33.70%  | -44.56%            | -41.30% |    -0.77 |       70 | 34.94%     | ok               |
|          20 | -42.59%  | -44.56%            | -43.99% |    -0.81 |       80 | 49.08%     | ok               |

## CRV-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 28.08%   | -76.09%            | -37.78% |     0.49 |       66 | 30.65%     | ok               |
|          50 | 12.53%   | -76.09%            | -29.30% |     0.33 |       44 | 17.24%     | ok               |
|          45 | 8.02%    | -76.09%            | -42.29% |     0.29 |       54 | 20.31%     | ok               |
|          30 | 1.71%    | -76.09%            | -39.89% |     0.25 |       64 | 35.25%     | ok               |
|          40 | 1.99%    | -76.09%            | -38.86% |     0.23 |       58 | 26.63%     | ok               |

## CSCO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 33.52%   | 126.72%            | -19.34% |     0.72 |       56 | 38.77%     | ok               |
|          45 | 31.32%   | 126.72%            | -19.34% |     0.67 |       51 | 41.43%     | ok               |
|          25 | 27.66%   | 126.72%            | -23.28% |     0.58 |       63 | 52.58%     | ok               |
|          35 | 27.06%   | 126.72%            | -23.68% |     0.57 |       51 | 48.09%     | ok               |
|          30 | 27.07%   | 126.72%            | -21.79% |     0.57 |       59 | 50.58%     | ok               |

## CVX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -8.49%   | 12.36%             | -28.32% |    -0.21 |       57 | 30.28%     | ok               |
|          20 | -13.07%  | 12.36%             | -26.07% |    -0.29 |       71 | 45.26%     | ok               |
|          25 | -13.44%  | 12.36%             | -25.65% |    -0.3  |       75 | 44.09%     | ok               |
|          35 | -12.64%  | 12.36%             | -27.83% |    -0.31 |       67 | 37.60%     | ok               |
|          40 | -12.30%  | 12.36%             | -26.30% |    -0.33 |       73 | 34.28%     | ok               |

## DASH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 129.69%  | -7.89%             | -31.38% |     0.96 |       40 | 17.05%     | ok               |
|          40 | 75.62%   | -7.89%             | -34.44% |     0.72 |       46 | 23.75%     | ok               |
|          45 | 65.87%   | -7.89%             | -39.58% |     0.68 |       44 | 19.35%     | ok               |
|          25 | -32.35%  | -7.89%             | -64.14% |     0.1  |       69 | 34.48%     | ok               |
|          35 | -32.14%  | -7.89%             | -63.23% |     0.09 |       69 | 28.16%     | ok               |

## DBC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -10.12%  | 21.82%             | -27.30% |    -0.31 |       71 | 37.60%     | ok               |
|          35 | -9.68%   | 21.82%             | -23.38% |    -0.31 |       60 | 31.61%     | ok               |
|          50 | -8.54%   | 21.82%             | -19.91% |    -0.32 |       42 | 21.13%     | ok               |
|          45 | -9.90%   | 21.82%             | -21.08% |    -0.35 |       54 | 24.46%     | ok               |
|          30 | -12.57%  | 21.82%             | -25.35% |    -0.43 |       58 | 32.78%     | ok               |

## DE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -3.50%   | 56.20%             | -28.94% |     0.02 |       72 | 51.41%     | ok               |
|          30 | -4.40%   | 56.20%             | -25.24% |     0    |       72 | 46.09%     | ok               |
|          25 | -5.89%   | 56.20%             | -26.67% |    -0.03 |       74 | 48.75%     | ok               |
|          50 | -5.20%   | 56.20%             | -23.74% |    -0.06 |       66 | 31.28%     | ok               |
|          45 | -6.59%   | 56.20%             | -26.94% |    -0.08 |       68 | 35.44%     | ok               |

## DIA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -0.36%   | 33.99%             | -13.15% |     0.02 |       60 | 43.76%     | ok               |
|          25 | -0.90%   | 33.99%             | -11.28% |    -0.01 |       60 | 47.09%     | ok               |
|          30 | -2.42%   | 33.99%             | -12.94% |    -0.09 |       60 | 45.92%     | ok               |
|          20 | -4.29%   | 33.99%             | -13.85% |    -0.18 |       64 | 49.42%     | ok               |
|          40 | -4.39%   | 33.99%             | -15.06% |    -0.22 |       66 | 41.10%     | ok               |

## DIS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 32.77%   | 1.71%              | -14.24% |     0.82 |       50 | 29.78%     | ok               |
|          45 | 4.92%    | 1.71%              | -16.54% |     0.2  |       51 | 33.28%     | ok               |
|          40 | 3.97%    | 1.71%              | -22.77% |     0.18 |       63 | 38.44%     | ok               |
|          35 | -2.95%   | 1.71%              | -25.70% |     0.05 |       75 | 44.59%     | ok               |
|          15 | -5.43%   | 1.71%              | -31.15% |     0.02 |       89 | 58.90%     | ok               |

## DOGE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 18.84%   | -79.31%            | -59.36% |     0.43 |       82 | 65.13%     | ok               |
|          20 | 1.47%    | -79.31%            | -57.37% |     0.29 |       85 | 60.34%     | ok               |
|          25 | -2.74%   | -79.31%            | -55.33% |     0.24 |       75 | 54.98%     | ok               |
|          30 | -18.89%  | -79.31%            | -62.31% |     0.06 |       78 | 49.81%     | ok               |
|          35 | -42.92%  | -79.31%            | -61.79% |    -0.33 |       74 | 43.49%     | ok               |

## DOT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -19.31%  | -87.12%            | -44.94% |    -0.11 |       58 | 26.44%     | ok               |
|          45 | -27.72%  | -87.12%            | -52.43% |    -0.23 |       52 | 31.03%     | ok               |
|          20 | -45.76%  | -87.12%            | -65.30% |    -0.27 |       92 | 60.73%     | ok               |
|          30 | -45.47%  | -87.12%            | -61.52% |    -0.32 |       92 | 48.85%     | ok               |
|          35 | -44.41%  | -87.12%            | -63.05% |    -0.32 |       82 | 42.15%     | ok               |

## DXY-INDEX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -2.01%   | 0.27%              | -6.06%  |    -0.3  |       44 | 30.80%     | ok               |
|          40 | -3.46%   | 0.27%              | -7.30%  |    -0.43 |       68 | 47.94%     | ok               |
|          30 | -4.38%   | 0.27%              | -9.98%  |    -0.5  |       70 | 58.57%     | ok               |
|          15 | -5.52%   | 0.27%              | -11.57% |    -0.51 |       90 | 75.70%     | ok               |
|          45 | -4.06%   | 0.27%              | -8.12%  |    -0.55 |       64 | 37.96%     | ok               |

## EEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -2.91%   | 73.84%             | -15.88% |    -0.04 |       50 | 36.11%     | ok               |
|          45 | -4.62%   | 73.84%             | -17.36% |    -0.11 |       52 | 37.60%     | ok               |
|          40 | -4.96%   | 73.84%             | -19.52% |    -0.11 |       64 | 39.77%     | ok               |
|          35 | -5.62%   | 73.84%             | -23.88% |    -0.12 |       66 | 41.76%     | ok               |
|          30 | -9.40%   | 73.84%             | -25.67% |    -0.25 |       64 | 43.43%     | ok               |

## EFA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -1.25%   | 36.45%             | -10.80% |     0.02 |       58 | 52.08%     | ok               |
|          20 | -8.10%   | 36.45%             | -12.49% |    -0.27 |       65 | 49.08%     | ok               |
|          30 | -9.39%   | 36.45%             | -14.87% |    -0.35 |       62 | 44.59%     | ok               |
|          50 | -9.07%   | 36.45%             | -17.56% |    -0.4  |       54 | 36.27%     | ok               |
|          25 | -10.84%  | 36.45%             | -16.11% |    -0.4  |       62 | 46.42%     | ok               |

## EOG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -20.10%  | 19.62%             | -39.69% |    -0.48 |       54 | 32.28%     | ok               |
|          50 | -21.27%  | 19.62%             | -40.57% |    -0.53 |       58 | 29.45%     | ok               |
|          30 | -25.51%  | 19.62%             | -48.13% |    -0.56 |       79 | 46.42%     | ok               |
|          40 | -24.83%  | 19.62%             | -43.26% |    -0.61 |       62 | 35.61%     | ok               |
|          35 | -26.33%  | 19.62%             | -46.26% |    -0.63 |       77 | 41.10%     | ok               |

## ETC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -7.93%   | -74.40%            | -27.89% |    -0.02 |       28 | 17.05%     | ok               |
|          35 | -15.03%  | -74.40%            | -42.62% |    -0.11 |       44 | 27.01%     | ok               |
|          45 | -16.07%  | -74.40%            | -35.44% |    -0.17 |       26 | 18.97%     | ok               |
|          40 | -21.04%  | -74.40%            | -40.48% |    -0.26 |       42 | 22.80%     | ok               |
|          30 | -35.69%  | -74.40%            | -48.16% |    -0.51 |       64 | 31.23%     | ok               |

## ETH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 166.33%  | -52.91%            | -30.11% |     1.32 |       62 | 45.02%     | ok               |
|          30 | 146.26%  | -52.91%            | -32.89% |     1.18 |       64 | 53.83%     | ok               |
|          40 | 63.12%   | -52.91%            | -33.11% |     0.8  |       58 | 37.55%     | ok               |
|          15 | 47.43%   | -52.91%            | -42.74% |     0.62 |       78 | 69.35%     | ok               |
|          45 | 38.98%   | -52.91%            | -34.50% |     0.61 |       52 | 33.72%     | ok               |

## EWJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -18.06%  | 39.53%             | -30.73% |    -0.58 |       64 | 39.93%     | ok               |
|          20 | -19.45%  | 39.53%             | -31.32% |    -0.62 |       60 | 41.93%     | ok               |
|          45 | -18.85%  | 39.53%             | -27.68% |    -0.71 |       60 | 32.11%     | ok               |
|          25 | -21.77%  | 39.53%             | -31.18% |    -0.72 |       60 | 40.93%     | ok               |
|          35 | -21.99%  | 39.53%             | -32.54% |    -0.75 |       70 | 38.27%     | ok               |

## FCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -6.29%   | 55.74%             | -26.57% |     0.03 |       56 | 29.45%     | ok               |
|          45 | -11.01%  | 55.74%             | -32.99% |    -0.04 |       56 | 33.78%     | ok               |
|          40 | -23.26%  | 55.74%             | -42.89% |    -0.26 |       66 | 38.94%     | ok               |
|          30 | -31.31%  | 55.74%             | -46.84% |    -0.38 |       67 | 45.59%     | ok               |
|          20 | -39.06%  | 55.74%             | -56.63% |    -0.49 |       74 | 52.58%     | ok               |

## FET-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 39.98%   | -85.60%            | -57.24% |     0.57 |       90 | 50.96%     | ok               |
|          15 | 4.69%    | -85.60%            | -59.58% |     0.36 |       86 | 54.02%     | ok               |
|          25 | -8.42%   | -85.60%            | -57.82% |     0.23 |       93 | 44.64%     | ok               |
|          30 | -13.59%  | -85.60%            | -54.02% |     0.16 |       83 | 40.80%     | ok               |
|          35 | -36.35%  | -85.60%            | -62.73% |    -0.17 |       71 | 34.29%     | ok               |

## FIL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -2.45%   | -85.83%            | -36.87% |     0.14 |       48 | 23.56%     | ok               |
|          35 | -22.29%  | -85.83%            | -41.69% |    -0.12 |       56 | 27.97%     | ok               |
|          30 | -28.94%  | -85.83%            | -45.42% |    -0.21 |       68 | 33.33%     | ok               |
|          45 | -24.61%  | -85.83%            | -41.68% |    -0.23 |       46 | 17.82%     | ok               |
|          50 | -26.52%  | -85.83%            | -44.97% |    -0.32 |       38 | 13.03%     | ok               |

## FXI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -1.19%   | 47.55%             | -22.99% |     0.06 |       46 | 30.28%     | ok               |
|          30 | -1.76%   | 47.55%             | -24.33% |     0.04 |       46 | 29.12%     | ok               |
|          15 | -3.60%   | 47.55%             | -21.68% |     0.01 |       52 | 33.44%     | ok               |
|          45 | -3.74%   | 47.55%             | -26.75% |    -0.02 |       44 | 23.63%     | ok               |
|          20 | -5.18%   | 47.55%             | -24.94% |    -0.04 |       52 | 31.45%     | ok               |

## GDX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 18.06%   | 174.80%            | -35.59% |     0.39 |       73 | 52.91%     | ok               |
|          40 | 13.85%   | 174.80%            | -31.87% |     0.35 |       64 | 42.93%     | ok               |
|          30 | 11.28%   | 174.80%            | -34.99% |     0.3  |       60 | 48.09%     | ok               |
|          35 | 8.95%    | 174.80%            | -32.37% |     0.27 |       68 | 45.26%     | ok               |
|          25 | 6.77%    | 174.80%            | -38.90% |     0.24 |       63 | 49.75%     | ok               |

## GDXJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -7.87%   | 194.97%            | -45.05% |     0.06 |       67 | 53.24%     | ok               |
|          30 | -23.10%  | 194.97%            | -44.93% |    -0.22 |       68 | 46.42%     | ok               |
|          50 | -20.20%  | 194.97%            | -44.92% |    -0.22 |       58 | 37.77%     | ok               |
|          25 | -26.52%  | 194.97%            | -47.26% |    -0.25 |       72 | 49.92%     | ok               |
|          35 | -26.73%  | 194.97%            | -43.49% |    -0.3  |       70 | 44.09%     | ok               |

## GE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 41.60%   | 238.62%            | -22.29% |     0.77 |       66 | 39.93%     | ok               |
|          45 | 30.91%   | 238.62%            | -25.68% |     0.61 |       74 | 42.76%     | ok               |
|          20 | 29.94%   | 238.62%            | -26.63% |     0.56 |       69 | 56.57%     | ok               |
|          35 | 24.11%   | 238.62%            | -27.11% |     0.5  |       80 | 48.09%     | ok               |
|          40 | 23.17%   | 238.62%            | -26.97% |     0.49 |       76 | 44.26%     | ok               |

## GLD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 33.16%   | 98.10%             | -14.61% |     0.79 |       46 | 46.76%     | ok               |
|          20 | 31.17%   | 98.10%             | -14.61% |     0.75 |       48 | 48.09%     | ok               |
|          30 | 26.82%   | 98.10%             | -16.63% |     0.68 |       48 | 45.59%     | ok               |
|          15 | 23.14%   | 98.10%             | -17.54% |     0.57 |       50 | 52.25%     | ok               |
|          35 | 20.63%   | 98.10%             | -17.29% |     0.56 |       50 | 44.93%     | ok               |

## GOOGL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 92.66%   | 136.96%            | -19.76% |     1.3  |       57 | 56.24%     | ok               |
|          30 | 86.92%   | 136.96%            | -20.41% |     1.26 |       63 | 53.58%     | ok               |
|          20 | 78.11%   | 136.96%            | -20.57% |     1.15 |       68 | 58.57%     | ok               |
|          35 | 68.78%   | 136.96%            | -22.85% |     1.14 |       69 | 48.42%     | ok               |
|          15 | 81.71%   | 136.96%            | -13.59% |     1.14 |       71 | 63.89%     | ok               |

## GRT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 37.41%   | -90.41%            | -35.66% |     0.62 |       44 | 22.03%     | ok               |
|          15 | 14.49%   | -90.41%            | -49.67% |     0.39 |       75 | 61.88%     | ok               |
|          20 | 10.52%   | -90.41%            | -46.47% |     0.35 |       83 | 56.32%     | ok               |
|          45 | 10.67%   | -90.41%            | -46.59% |     0.32 |       52 | 27.59%     | ok               |
|          35 | 6.17%    | -90.41%            | -48.22% |     0.28 |       62 | 36.40%     | ok               |

## GS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 21.15%   | 162.88%            | -20.56% |     0.47 |       74 | 61.06%     | ok               |
|          20 | 4.62%    | 162.88%            | -23.19% |     0.19 |       74 | 57.07%     | ok               |
|          40 | 0.08%    | 162.88%            | -17.88% |     0.09 |       72 | 45.26%     | ok               |
|          25 | -0.67%   | 162.88%            | -23.32% |     0.09 |       74 | 54.58%     | ok               |
|          30 | -2.38%   | 162.88%            | -22.13% |     0.05 |       76 | 52.08%     | ok               |

## HD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -5.67%   | -2.34%             | -18.58% |    -0.08 |       75 | 43.43%     | ok               |
|          25 | -6.41%   | -2.34%             | -19.40% |    -0.09 |       74 | 45.42%     | ok               |
|          45 | -10.35%  | -2.34%             | -19.30% |    -0.29 |       58 | 27.95%     | ok               |
|          15 | -15.26%  | -2.34%             | -27.26% |    -0.31 |      109 | 54.08%     | ok               |
|          35 | -14.15%  | -2.34%             | -22.43% |    -0.35 |       82 | 39.60%     | ok               |

## HON Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -14.65%  | 136.82%            | -24.48% |    -0.43 |       66 | 29.28%     | ok               |
|          45 | -16.86%  | 136.82%            | -23.50% |    -0.48 |       68 | 34.11%     | ok               |
|          30 | -27.38%  | 136.82%            | -30.98% |    -0.73 |       92 | 49.42%     | ok               |
|          40 | -26.89%  | 136.82%            | -30.97% |    -0.78 |       74 | 37.94%     | ok               |
|          35 | -28.63%  | 136.82%            | -32.01% |    -0.8  |       91 | 44.09%     | ok               |

## HYG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -7.92%   | 3.42%              | -7.92%  |    -0.96 |       70 | 29.45%     | ok               |
|          15 | -9.71%   | 3.42%              | -10.06% |    -1.05 |       88 | 41.43%     | ok               |
|          20 | -9.69%   | 3.42%              | -10.29% |    -1.08 |       86 | 39.10%     | ok               |
|          45 | -8.60%   | 3.42%              | -8.60%  |    -1.08 |       66 | 26.29%     | ok               |
|          30 | -9.52%   | 3.42%              | -9.59%  |    -1.11 |       81 | 34.28%     | ok               |

## IBIT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 72.96%   | -10.94%            | -19.20% |     1.15 |       38 | 39.33%     | ok               |
|          50 | 53.73%   | -10.94%            | -17.37% |     1.08 |       22 | 23.02%     | ok               |
|          45 | 43.80%   | -10.94%            | -17.37% |     0.91 |       24 | 23.98%     | ok               |
|          30 | 42.51%   | -10.94%            | -18.95% |     0.85 |       32 | 31.65%     | ok               |
|          40 | 38.87%   | -10.94%            | -17.78% |     0.83 |       26 | 25.66%     | ok               |

## IBM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 9.23%    | 46.20%             | -28.20% |     0.27 |       91 | 62.06%     | ok               |
|          30 | 0.33%    | 46.20%             | -27.52% |     0.11 |       76 | 50.08%     | ok               |
|          35 | -4.04%   | 46.20%             | -27.52% |     0.02 |       72 | 45.59%     | ok               |
|          50 | -4.49%   | 46.20%             | -22.50% |    -0.02 |       54 | 32.95%     | ok               |
|          20 | -7.35%   | 46.20%             | -34.12% |    -0.03 |       75 | 54.41%     | ok               |

## ICP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 20.56%   | -76.31%            | -32.85% |     0.42 |       60 | 27.20%     | ok               |
|          35 | 4.54%    | -76.31%            | -48.44% |     0.27 |       72 | 32.95%     | ok               |
|          50 | 5.02%    | -76.31%            | -43.65% |     0.25 |       42 | 17.05%     | ok               |
|          30 | -5.39%   | -76.31%            | -57.53% |     0.21 |       85 | 39.08%     | ok               |
|          45 | -8.63%   | -76.31%            | -40.57% |     0.08 |       60 | 21.26%     | ok               |

## IEF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -7.23%   | -0.55%             | -10.09% |    -0.87 |       70 | 42.10%     | ok               |
|          15 | -7.78%   | -0.55%             | -10.82% |    -0.92 |       69 | 43.59%     | ok               |
|          40 | -8.39%   | -0.55%             | -9.67%  |    -1.31 |       60 | 24.79%     | ok               |
|          45 | -8.07%   | -0.55%             | -9.73%  |    -1.33 |       50 | 22.80%     | ok               |
|          25 | -10.80%  | -0.55%             | -11.49% |    -1.38 |       76 | 39.27%     | ok               |

## IEMG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.10%   | 66.80%             | -13.91% |     0.05 |       52 | 34.44%     | ok               |
|          35 | -0.32%   | 66.80%             | -22.13% |     0.05 |       63 | 42.60%     | ok               |
|          45 | -0.91%   | 66.80%             | -14.92% |     0.02 |       48 | 36.94%     | ok               |
|          40 | -2.44%   | 66.80%             | -18.43% |    -0.03 |       60 | 39.93%     | ok               |
|          25 | -4.72%   | 66.80%             | -25.58% |    -0.09 |       59 | 45.42%     | ok               |

## INJ-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -12.91%  | -77.91%            | -55.31% |     0.02 |       44 | 22.41%     | ok               |
|          35 | -18.57%  | -77.91%            | -60.42% |     0.01 |       60 | 32.57%     | ok               |
|          50 | -22.38%  | -77.91%            | -51.00% |    -0.14 |       48 | 19.35%     | ok               |
|          40 | -26.93%  | -77.91%            | -57.21% |    -0.15 |       50 | 28.74%     | ok               |
|          15 | -61.63%  | -77.91%            | -83.89% |    -0.51 |       82 | 50.77%     | ok               |

## INTC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 76.11%   | 201.22%            | -49.32% |     0.74 |       60 | 34.28%     | ok               |
|          15 | 82.95%   | 201.22%            | -53.65% |     0.74 |       84 | 61.23%     | ok               |
|          25 | 75.50%   | 201.22%            | -56.41% |     0.72 |       75 | 51.58%     | ok               |
|          40 | 70.33%   | 201.22%            | -55.86% |     0.7  |       68 | 38.60%     | ok               |
|          20 | 72.70%   | 201.22%            | -52.47% |     0.7  |       82 | 56.57%     | ok               |

## INTU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.62%   | -58.14%            | -42.60% |     0.11 |       73 | 28.95%     | ok               |
|          45 | -4.02%   | -58.14%            | -44.44% |     0.05 |       71 | 33.11%     | ok               |
|          40 | -11.26%  | -58.14%            | -48.15% |    -0.09 |       73 | 35.77%     | ok               |
|          25 | -12.80%  | -58.14%            | -42.24% |    -0.09 |       66 | 45.26%     | ok               |
|          15 | -13.83%  | -58.14%            | -46.90% |    -0.1  |       81 | 50.75%     | ok               |

## ITA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 1.77%    | 91.52%             | -21.48% |     0.12 |       76 | 37.77%     | ok               |
|          15 | -2.71%   | 91.52%             | -28.17% |     0.02 |       86 | 59.23%     | ok               |
|          30 | -2.78%   | 91.52%             | -23.75% |    -0.01 |       74 | 47.59%     | ok               |
|          35 | -4.85%   | 91.52%             | -23.16% |    -0.08 |       78 | 45.92%     | ok               |
|          40 | -5.94%   | 91.52%             | -20.58% |    -0.12 |       80 | 42.43%     | ok               |

## IWM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 9.83%    | 54.23%             | -13.30% |     0.4  |       50 | 36.77%     | ok               |
|          40 | 8.60%    | 54.23%             | -14.08% |     0.39 |       42 | 31.28%     | ok               |
|          30 | 9.40%    | 54.23%             | -12.83% |     0.39 |       48 | 35.77%     | ok               |
|          35 | 8.35%    | 54.23%             | -14.11% |     0.36 |       48 | 33.61%     | ok               |
|          20 | 5.50%    | 54.23%             | -13.83% |     0.25 |       60 | 37.77%     | ok               |

## JNJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 20.41%   | 62.61%             | -10.57% |     0.87 |       58 | 36.94%     | ok               |
|          15 | 15.46%   | 62.61%             | -18.02% |     0.55 |       66 | 57.07%     | ok               |
|          45 | 11.38%   | 62.61%             | -13.35% |     0.5  |       60 | 42.10%     | ok               |
|          20 | 11.54%   | 62.61%             | -17.61% |     0.45 |       70 | 53.74%     | ok               |
|          40 | 8.95%    | 62.61%             | -14.77% |     0.39 |       66 | 46.26%     | ok               |

## JPM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 19.97%   | 88.32%             | -15.90% |     0.66 |       52 | 41.10%     | ok               |
|          45 | 8.58%    | 88.32%             | -21.91% |     0.31 |       54 | 44.09%     | ok               |
|          40 | -5.76%   | 88.32%             | -28.47% |    -0.09 |       66 | 46.59%     | ok               |
|          20 | -12.79%  | 88.32%             | -33.59% |    -0.2  |       84 | 57.90%     | ok               |
|          35 | -11.03%  | 88.32%             | -27.43% |    -0.23 |       72 | 50.25%     | ok               |

## KO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 28.93%   | 36.49%             | -8.07%  |     1.03 |       49 | 37.77%     | ok               |
|          35 | 24.98%   | 36.49%             | -8.07%  |     0.93 |       52 | 36.44%     | ok               |
|          40 | 22.37%   | 36.49%             | -9.28%  |     0.9  |       54 | 33.28%     | ok               |
|          25 | 23.60%   | 36.49%             | -9.37%  |     0.86 |       55 | 40.43%     | ok               |
|          50 | 14.81%   | 36.49%             | -11.40% |     0.68 |       36 | 26.79%     | ok               |

## LDO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 24.99%   | -87.68%            | -46.95% |     0.48 |       81 | 51.92%     | ok               |
|          20 | 13.39%   | -87.68%            | -44.97% |     0.4  |       85 | 47.32%     | ok               |
|          50 | 15.22%   | -87.68%            | -48.04% |     0.37 |       46 | 16.86%     | ok               |
|          30 | -2.99%   | -87.68%            | -60.93% |     0.24 |       76 | 38.31%     | ok               |
|          35 | -5.15%   | -87.68%            | -62.61% |     0.2  |       74 | 31.42%     | ok               |

## LIN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 5.16%    | 27.64%             | -23.68% |     0.23 |       62 | 49.42%     | ok               |
|          25 | 4.87%    | 27.64%             | -22.01% |     0.23 |       61 | 41.43%     | ok               |
|          20 | 2.62%    | 27.64%             | -23.00% |     0.15 |       60 | 44.59%     | ok               |
|          35 | 1.08%    | 27.64%             | -21.18% |     0.1  |       60 | 32.11%     | ok               |
|          30 | 0.44%    | 27.64%             | -21.53% |     0.08 |       64 | 38.60%     | ok               |

## LINK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -11.40%  | -71.34%            | -49.35% |     0.12 |       69 | 41.57%     | ok               |
|          45 | -13.28%  | -71.34%            | -38.11% |     0.05 |       50 | 26.63%     | ok               |
|          50 | -12.86%  | -71.34%            | -36.52% |     0.03 |       40 | 21.26%     | ok               |
|          35 | -24.33%  | -71.34%            | -49.18% |    -0.05 |       59 | 36.78%     | ok               |
|          25 | -34.06%  | -71.34%            | -46.32% |    -0.12 |       68 | 47.13%     | ok               |

## LLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 21.22%   | 80.95%             | -38.23% |     0.48 |       44 | 38.44%     | ok               |
|          15 | 11.88%   | 80.95%             | -48.12% |     0.31 |       63 | 61.90%     | ok               |
|          45 | 8.27%    | 80.95%             | -42.66% |     0.26 |       52 | 41.76%     | ok               |
|          20 | -6.14%   | 80.95%             | -51.34% |     0.04 |       72 | 56.91%     | ok               |
|          25 | -7.69%   | 80.95%             | -53.47% |     0.01 |       68 | 54.24%     | ok               |

## LRCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 8.43%    | 352.00%            | -60.45% |     0.28 |       83 | 55.57%     | ok               |
|          50 | 2.18%    | 352.00%            | -50.39% |     0.19 |       80 | 37.44%     | ok               |
|          40 | -0.88%   | 352.00%            | -56.86% |     0.16 |       72 | 43.26%     | ok               |
|          35 | -7.32%   | 352.00%            | -61.76% |     0.09 |       80 | 45.26%     | ok               |
|          20 | -10.01%  | 352.00%            | -67.64% |     0.06 |       87 | 51.25%     | ok               |

## LTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -12.22%  | -64.14%            | -44.78% |    -0    |       56 | 31.80%     | ok               |
|          35 | -22.47%  | -64.14%            | -54.86% |    -0.13 |       66 | 42.91%     | ok               |
|          30 | -34.00%  | -64.14%            | -53.76% |    -0.29 |       66 | 48.47%     | ok               |
|          40 | -31.40%  | -64.14%            | -56.10% |    -0.3  |       58 | 38.12%     | ok               |
|          25 | -36.79%  | -64.14%            | -54.26% |    -0.33 |       74 | 50.96%     | ok               |

## MCD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 2.85%    | -9.19%             | -9.22%  |     0.19 |       42 | 20.63%     | ok               |
|          30 | -2.55%   | -9.19%             | -18.81% |    -0.05 |       75 | 38.10%     | ok               |
|          25 | -3.59%   | -9.19%             | -20.47% |    -0.09 |       75 | 40.77%     | ok               |
|          35 | -7.68%   | -9.19%             | -15.45% |    -0.29 |       67 | 34.44%     | ok               |
|          40 | -7.95%   | -9.19%             | -16.86% |    -0.33 |       71 | 28.79%     | ok               |

## META Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -9.57%   | 15.84%             | -31.03% |    -0.09 |       66 | 39.27%     | ok               |
|          40 | -19.51%  | 15.84%             | -35.11% |    -0.29 |       66 | 42.26%     | ok               |
|          25 | -27.45%  | 15.84%             | -39.84% |    -0.43 |       67 | 52.91%     | ok               |
|          50 | -23.37%  | 15.84%             | -34.00% |    -0.43 |       70 | 35.44%     | ok               |
|          30 | -29.40%  | 15.84%             | -38.96% |    -0.49 |       72 | 49.75%     | ok               |

## MPC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 14.51%   | 52.74%             | -23.96% |     0.37 |       52 | 38.60%     | ok               |
|          45 | 7.25%    | 52.74%             | -25.09% |     0.24 |       58 | 42.26%     | ok               |
|          40 | 5.62%    | 52.74%             | -25.70% |     0.22 |       60 | 44.59%     | ok               |
|          35 | 2.36%    | 52.74%             | -35.90% |     0.16 |       68 | 47.09%     | ok               |
|          30 | -13.74%  | 52.74%             | -44.76% |    -0.14 |       71 | 49.92%     | ok               |

## MRK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -21.19%  | 1.78%              | -30.12% |    -0.4  |       87 | 56.74%     | ok               |
|          25 | -20.81%  | 1.78%              | -31.07% |    -0.42 |       72 | 48.75%     | ok               |
|          20 | -24.69%  | 1.78%              | -29.59% |    -0.52 |       77 | 52.08%     | ok               |
|          45 | -23.63%  | 1.78%              | -26.02% |    -0.63 |       57 | 34.94%     | ok               |
|          50 | -23.28%  | 1.78%              | -25.69% |    -0.67 |       56 | 31.95%     | ok               |

## MS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -4.19%   | 142.96%            | -19.99% |    -0.02 |       70 | 41.10%     | ok               |
|          35 | -10.87%  | 142.96%            | -25.26% |    -0.19 |       74 | 45.76%     | ok               |
|          15 | -15.38%  | 142.96%            | -23.25% |    -0.25 |       78 | 57.90%     | ok               |
|          20 | -15.48%  | 142.96%            | -25.68% |    -0.29 |       82 | 54.08%     | ok               |
|          30 | -17.10%  | 142.96%            | -27.79% |    -0.35 |       79 | 49.42%     | ok               |

## MSFT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -19.51%  | -9.30%             | -26.27% |    -0.53 |       66 | 35.27%     | ok               |
|          50 | -23.14%  | -9.30%             | -28.83% |    -0.67 |       64 | 30.62%     | ok               |
|          35 | -32.52%  | -9.30%             | -35.08% |    -0.86 |       75 | 43.76%     | ok               |
|          40 | -31.88%  | -9.30%             | -34.46% |    -0.87 |       71 | 38.60%     | ok               |
|          25 | -35.81%  | -9.30%             | -38.91% |    -0.9  |       87 | 51.41%     | ok               |

## MU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 421.65%  | 1209.35%           | -61.96% |     1.55 |       48 | 68.05%     | ok               |
|          25 | 334.60%  | 1209.35%           | -67.90% |     1.46 |       49 | 61.73%     | ok               |
|          40 | 290.77%  | 1209.35%           | -64.07% |     1.4  |       56 | 55.24%     | ok               |
|          20 | 297.89%  | 1209.35%           | -67.25% |     1.37 |       55 | 63.89%     | ok               |
|          30 | 270.20%  | 1209.35%           | -68.76% |     1.34 |       51 | 59.90%     | ok               |

## NEAR-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 99.44%   | -63.68%            | -48.95% |     0.97 |       44 | 23.18%     | ok               |
|          50 | 70.90%   | -63.68%            | -53.13% |     0.82 |       38 | 18.39%     | ok               |
|          40 | 57.99%   | -63.68%            | -57.15% |     0.71 |       48 | 27.59%     | ok               |
|          35 | 30.22%   | -63.68%            | -61.02% |     0.5  |       72 | 33.14%     | ok               |
|          15 | 2.55%    | -63.68%            | -54.94% |     0.32 |       87 | 57.09%     | ok               |

## NEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 5.59%    | 179.37%            | -29.41% |     0.24 |       64 | 62.40%     | ok               |
|          20 | -5.71%   | 179.37%            | -30.47% |     0.1  |       74 | 57.90%     | ok               |
|          25 | -19.47%  | 179.37%            | -37.89% |    -0.11 |       70 | 55.74%     | ok               |
|          50 | -25.02%  | 179.37%            | -33.36% |    -0.27 |       58 | 40.43%     | ok               |
|          30 | -29.57%  | 179.37%            | -38.49% |    -0.3  |       74 | 54.08%     | ok               |

## NFLX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 61.67%   | 30.72%             | -11.94% |     1.21 |       46 | 47.25%     | ok               |
|          50 | 47.93%   | 30.72%             | -16.28% |     1.06 |       48 | 39.77%     | ok               |
|          35 | 53.36%   | 30.72%             | -18.30% |     1.04 |       60 | 50.75%     | ok               |
|          45 | 44.19%   | 30.72%             | -15.48% |     0.96 |       52 | 43.59%     | ok               |
|          25 | 42.51%   | 30.72%             | -21.09% |     0.84 |       60 | 57.24%     | ok               |

## NKE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -33.86%  | -59.54%            | -50.44% |    -0.42 |       93 | 52.58%     | ok               |
|          15 | -37.79%  | -59.54%            | -55.52% |    -0.5  |       93 | 57.07%     | ok               |
|          40 | -26.46%  | -59.54%            | -31.19% |    -0.5  |       63 | 30.12%     | ok               |
|          25 | -45.09%  | -59.54%            | -52.84% |    -0.79 |       91 | 48.59%     | ok               |
|          35 | -39.10%  | -59.54%            | -43.08% |    -0.8  |       75 | 37.10%     | ok               |

## NOW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 18.47%   | -37.07%            | -26.36% |     0.38 |       79 | 51.91%     | ok               |
|          30 | 17.95%   | -37.07%            | -30.25% |     0.38 |       80 | 45.92%     | ok               |
|          15 | 12.06%   | -37.07%            | -26.36% |     0.31 |       87 | 55.24%     | ok               |
|          25 | 11.24%   | -37.07%            | -25.70% |     0.3  |       72 | 49.25%     | ok               |
|          35 | 10.33%   | -37.07%            | -29.30% |     0.29 |       81 | 40.60%     | ok               |

## NVDA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -3.45%   | 115.23%            | -33.22% |     0.12 |       70 | 50.27%     | ok               |
|          30 | -5.26%   | 115.23%            | -35.26% |     0.08 |       72 | 47.95%     | ok               |
|          20 | -9.86%   | 115.23%            | -40.59% |     0.04 |       73 | 54.72%     | ok               |
|          50 | -14.29%  | 115.23%            | -40.84% |    -0.11 |       56 | 32.09%     | ok               |
|          35 | -17.64%  | 115.23%            | -41.25% |    -0.13 |       80 | 44.92%     | ok               |

## OP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 66.86%   | -94.19%            | -36.11% |     0.86 |       34 | 12.45%     | ok               |
|          45 | 73.33%   | -94.19%            | -45.76% |     0.86 |       36 | 17.24%     | ok               |
|          40 | 51.97%   | -94.19%            | -53.61% |     0.67 |       50 | 26.05%     | ok               |
|          35 | 26.48%   | -94.19%            | -58.33% |     0.47 |       58 | 29.12%     | ok               |
|          30 | 3.40%    | -94.19%            | -70.27% |     0.28 |       74 | 35.63%     | ok               |

## ORCL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 186.63%  | 28.28%             | -29.32% |     1.21 |       74 | 65.22%     | ok               |
|          25 | 115.02%  | 28.28%             | -27.76% |     0.95 |       75 | 57.74%     | ok               |
|          20 | 111.33%  | 28.28%             | -29.32% |     0.93 |       77 | 60.90%     | ok               |
|          35 | 84.36%   | 28.28%             | -31.95% |     0.82 |       68 | 49.42%     | ok               |
|          30 | 84.52%   | 28.28%             | -29.47% |     0.81 |       74 | 53.58%     | ok               |

## OXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 8.90%    | -12.36%            | -29.70% |     0.27 |       63 | 43.43%     | ok               |
|          35 | 3.85%    | -12.36%            | -30.50% |     0.18 |       68 | 38.77%     | ok               |
|          40 | 1.31%    | -12.36%            | -32.21% |     0.13 |       56 | 34.78%     | ok               |
|          50 | 0.87%    | -12.36%            | -31.07% |     0.12 |       36 | 27.79%     | ok               |
|          25 | -6.17%   | -12.36%            | -39.43% |     0.01 |       71 | 46.92%     | ok               |

## PEP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 9.33%    | -17.30%            | -11.62% |     0.43 |       48 | 27.62%     | ok               |
|          45 | 0.13%    | -17.30%            | -14.22% |     0.06 |       72 | 32.61%     | ok               |
|          40 | -2.19%   | -17.30%            | -18.04% |    -0.02 |       80 | 38.60%     | ok               |
|          35 | -3.00%   | -17.30%            | -21.42% |    -0.03 |       87 | 43.59%     | ok               |
|          30 | -8.13%   | -17.30%            | -21.35% |    -0.17 |       85 | 50.25%     | ok               |

## PEPE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 20.65%   | -84.32%            | -61.96% |     0.47 |       76 | 59.58%     | ok               |
|          30 | 20.61%   | -84.32%            | -57.66% |     0.44 |       77 | 44.06%     | ok               |
|          35 | 13.73%   | -84.32%            | -51.35% |     0.38 |       62 | 38.70%     | ok               |
|          25 | -1.29%   | -84.32%            | -53.88% |     0.27 |       83 | 49.23%     | ok               |
|          20 | -5.94%   | -84.32%            | -61.13% |     0.25 |       82 | 55.94%     | ok               |

## PFE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -27.05%  | -9.80%             | -27.99% |    -1    |       52 | 19.47%     | ok               |
|          35 | -34.58%  | -9.80%             | -36.39% |    -1.13 |       82 | 31.78%     | ok               |
|          50 | -28.29%  | -9.80%             | -29.22% |    -1.15 |       42 | 15.81%     | ok               |
|          40 | -33.23%  | -9.80%             | -34.09% |    -1.18 |       76 | 24.29%     | ok               |
|          30 | -40.64%  | -9.80%             | -42.29% |    -1.31 |       77 | 35.27%     | ok               |

## PG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -2.13%   | -5.74%             | -19.77% |    -0.04 |       52 | 34.94%     | ok               |
|          35 | -4.30%   | -5.74%             | -18.66% |    -0.12 |       60 | 38.27%     | ok               |
|          30 | -13.00%  | -5.74%             | -21.65% |    -0.46 |       62 | 41.43%     | ok               |
|          45 | -11.69%  | -5.74%             | -20.43% |    -0.48 |       52 | 32.45%     | ok               |
|          25 | -14.04%  | -5.74%             | -22.55% |    -0.5  |       72 | 42.60%     | ok               |

## PM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 2.96%    | 94.40%             | -32.20% |     0.16 |       88 | 53.24%     | ok               |
|          30 | -0.35%   | 94.40%             | -33.68% |     0.09 |       81 | 57.24%     | ok               |
|          20 | -2.55%   | 94.40%             | -31.89% |     0.05 |       87 | 62.06%     | ok               |
|          40 | -7.31%   | 94.40%             | -37.94% |    -0.09 |       82 | 48.75%     | ok               |
|          50 | -6.95%   | 94.40%             | -35.70% |    -0.09 |       74 | 42.10%     | ok               |

## POL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 82.79%   | -83.54%            | -46.45% |     0.88 |       81 | 51.53%     | ok               |
|          25 | 86.16%   | -83.54%            | -46.72% |     0.86 |       66 | 59.39%     | ok               |
|          20 | 71.84%   | -83.54%            | -52.88% |     0.77 |       72 | 63.60%     | ok               |
|          15 | 53.35%   | -83.54%            | -58.42% |     0.65 |       74 | 68.39%     | ok               |
|          50 | 18.38%   | -83.54%            | -22.86% |     0.42 |       52 | 20.88%     | ok               |

## QCOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 4.37%    | 33.67%             | -54.50% |     0.22 |       73 | 49.08%     | ok               |
|          35 | 2.40%    | 33.67%             | -50.58% |     0.19 |       81 | 44.59%     | ok               |
|          20 | 0.14%    | 33.67%             | -54.38% |     0.18 |       69 | 51.91%     | ok               |
|          30 | -9.21%   | 33.67%             | -56.59% |     0.05 |       77 | 47.09%     | ok               |
|          15 | -16.51%  | 33.67%             | -57.94% |    -0.04 |       73 | 55.07%     | ok               |

## QQQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 22.72%   | 64.69%             | -12.88% |     0.62 |       57 | 48.42%     | ok               |
|          15 | 23.25%   | 64.69%             | -14.17% |     0.59 |       61 | 53.91%     | ok               |
|          30 | 18.71%   | 64.69%             | -12.88% |     0.54 |       62 | 45.59%     | ok               |
|          20 | 19.75%   | 64.69%             | -12.98% |     0.53 |       65 | 51.08%     | ok               |
|          35 | 6.57%    | 64.69%             | -18.29% |     0.26 |       68 | 41.93%     | ok               |

## RENDER-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 53.85%   | -63.32%            | -43.43% |     0.67 |       86 | 53.85%     | ok               |
|          15 | 35.99%   | -63.32%            | -44.59% |     0.57 |       86 | 56.88%     | ok               |
|          25 | 23.37%   | -63.32%            | -40.60% |     0.48 |       90 | 50.00%     | ok               |
|          30 | -15.32%  | -63.32%            | -45.00% |     0.14 |       98 | 43.72%     | ok               |
|          35 | -28.57%  | -63.32%            | -41.33% |    -0.08 |       84 | 35.22%     | ok               |

## RTX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 25.73%   | 104.38%            | -18.66% |     0.64 |       78 | 56.24%     | ok               |
|          25 | 21.26%   | 104.38%            | -18.59% |     0.55 |       64 | 52.75%     | ok               |
|          30 | 19.42%   | 104.38%            | -16.99% |     0.52 |       58 | 51.58%     | ok               |
|          35 | 16.89%   | 104.38%            | -18.00% |     0.51 |       56 | 49.75%     | ok               |
|          50 | 15.59%   | 104.38%            | -18.42% |     0.51 |       60 | 41.93%     | ok               |

## SBUX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -14.92%  | 12.49%             | -23.55% |    -0.24 |       65 | 41.76%     | ok               |
|          45 | -17.75%  | 12.49%             | -27.26% |    -0.4  |       68 | 29.62%     | ok               |
|          40 | -19.74%  | 12.49%             | -27.00% |    -0.42 |       62 | 33.61%     | ok               |
|          30 | -22.19%  | 12.49%             | -29.34% |    -0.44 |       64 | 39.43%     | ok               |
|          20 | -27.00%  | 12.49%             | -34.85% |    -0.51 |       70 | 43.76%     | ok               |

## SCHW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 0.79%    | 44.06%             | -16.53% |     0.09 |       54 | 33.28%     | ok               |
|          50 | -4.29%   | 44.06%             | -13.28% |    -0.09 |       50 | 30.95%     | ok               |
|          40 | -9.67%   | 44.06%             | -23.35% |    -0.2  |       62 | 36.27%     | ok               |
|          25 | -12.81%  | 44.06%             | -28.76% |    -0.23 |       63 | 48.25%     | ok               |
|          20 | -14.44%  | 44.06%             | -29.24% |    -0.26 |       71 | 50.92%     | ok               |

## SHIB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 2.65%    | -79.18%            | -49.21% |     0.27 |       80 | 68.77%     | ok               |
|          25 | -5.18%   | -79.18%            | -43.85% |     0.18 |       77 | 59.58%     | ok               |
|          20 | -9.75%   | -79.18%            | -46.38% |     0.14 |       79 | 63.98%     | ok               |
|          35 | -8.51%   | -79.18%            | -53.32% |     0.11 |       66 | 46.74%     | ok               |
|          40 | -15.17%  | -79.18%            | -49.96% |     0.01 |       56 | 39.08%     | ok               |

## SHY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          30 | -2.24%   | 0.33%              | -2.85% |    -0.79 |       48 | 34.28%     | ok               |
|          35 | -2.36%   | 0.33%              | -3.27% |    -0.84 |       50 | 32.45%     | ok               |
|          40 | -2.47%   | 0.33%              | -3.33% |    -0.89 |       50 | 30.62%     | ok               |
|          45 | -2.45%   | 0.33%              | -3.23% |    -0.9  |       48 | 27.45%     | ok               |
|          50 | -2.62%   | 0.33%              | -3.40% |    -1.01 |       44 | 24.63%     | ok               |

## SKY-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -24.31%  | -14.61%            | -43.98% |    -0.26 |       70 | 41.19%     | ok               |
|          15 | -28.94%  | -14.61%            | -56.39% |    -0.27 |       60 | 51.49%     | ok               |
|          25 | -28.19%  | -14.61%            | -48.09% |    -0.32 |       65 | 44.85%     | ok               |
|          20 | -39.13%  | -14.61%            | -58.40% |    -0.52 |       62 | 48.51%     | ok               |
|          35 | -36.19%  | -14.61%            | -49.68% |    -0.61 |       64 | 34.78%     | ok               |

## SLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 18.91%   | -4.08%             | -24.10% |     0.47 |       48 | 35.77%     | ok               |
|          45 | 16.09%   | -4.08%             | -21.53% |     0.43 |       54 | 32.28%     | ok               |
|          50 | -2.98%   | -4.08%             | -29.84% |     0.01 |       52 | 28.45%     | ok               |
|          35 | -11.93%  | -4.08%             | -43.22% |    -0.15 |       74 | 43.59%     | ok               |
|          30 | -26.14%  | -4.08%             | -55.49% |    -0.46 |       77 | 49.92%     | ok               |

## SLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 76.66%   | 156.77%            | -34.10% |     0.93 |       52 | 33.94%     | ok               |
|          45 | 73.86%   | 156.77%            | -31.82% |     0.9  |       56 | 34.78%     | ok               |
|          40 | 71.78%   | 156.77%            | -31.93% |     0.88 |       62 | 36.94%     | ok               |
|          35 | 58.19%   | 156.77%            | -36.89% |     0.77 |       64 | 39.10%     | ok               |
|          30 | 49.00%   | 156.77%            | -42.66% |     0.69 |       58 | 41.26%     | ok               |

## SMH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 121.21%  | 219.85%            | -30.17% |     1.35 |       47 | 52.75%     | ok               |
|          35 | 97.97%   | 219.85%            | -34.36% |     1.23 |       54 | 48.59%     | ok               |
|          25 | 97.83%   | 219.85%            | -32.94% |     1.21 |       46 | 51.58%     | ok               |
|          30 | 95.49%   | 219.85%            | -33.99% |     1.2  |       48 | 49.92%     | ok               |
|          45 | 81.27%   | 219.85%            | -32.75% |     1.16 |       52 | 42.76%     | ok               |

## SNX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 23.22%   | -86.08%            | -43.20% |     0.46 |       73 | 49.62%     | ok               |
|          35 | 2.52%    | -86.08%            | -30.08% |     0.27 |       66 | 32.38%     | ok               |
|          30 | -7.32%   | -86.08%            | -34.76% |     0.18 |       62 | 39.46%     | ok               |
|          25 | -12.80%  | -86.08%            | -38.88% |     0.14 |       74 | 44.06%     | ok               |
|          15 | -17.01%  | -86.08%            | -44.00% |     0.13 |       83 | 54.21%     | ok               |

## SOL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -18.53%  | -72.01%            | -54.68% |     0.03 |       64 | 39.08%     | ok               |
|          25 | -32.75%  | -72.01%            | -53.21% |    -0.1  |       72 | 57.47%     | ok               |
|          35 | -33.71%  | -72.01%            | -61.96% |    -0.13 |       72 | 46.55%     | ok               |
|          15 | -38.03%  | -72.01%            | -59.14% |    -0.14 |       74 | 64.56%     | ok               |
|          20 | -42.41%  | -72.01%            | -56.90% |    -0.22 |       68 | 59.96%     | ok               |

## SOXX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 101.62%  | 196.72%            | -38.67% |     1.18 |       53 | 51.41%     | ok               |
|          25 | 97.76%   | 196.72%            | -39.85% |     1.15 |       51 | 51.08%     | ok               |
|          35 | 92.23%   | 196.72%            | -38.63% |     1.13 |       59 | 46.42%     | ok               |
|          15 | 96.56%   | 196.72%            | -37.72% |     1.11 |       66 | 54.24%     | ok               |
|          30 | 86.65%   | 196.72%            | -40.34% |     1.07 |       55 | 48.92%     | ok               |

## SPY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 17.00%   | 47.46%             | -14.25% |     0.59 |       58 | 53.91%     | ok               |
|          15 | 15.40%   | 47.46%             | -16.80% |     0.53 |       67 | 57.07%     | ok               |
|          25 | 9.72%    | 47.46%             | -15.22% |     0.38 |       58 | 52.91%     | ok               |
|          30 | 5.76%    | 47.46%             | -16.47% |     0.26 |       60 | 50.42%     | ok               |
|          35 | 3.20%    | 47.46%             | -16.72% |     0.17 |       58 | 47.75%     | ok               |

## SUSHI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -23.49%  | -88.65%            | -40.08% |    -0.19 |       52 | 14.75%     | ok               |
|          45 | -55.77%  | -88.65%            | -64.27% |    -0.7  |       54 | 18.01%     | ok               |
|          40 | -58.91%  | -88.65%            | -66.57% |    -0.7  |       61 | 24.52%     | ok               |
|          15 | -76.99%  | -88.65%            | -78.98% |    -0.89 |       87 | 46.93%     | ok               |
|          35 | -71.87%  | -88.65%            | -78.94% |    -0.97 |       76 | 30.08%     | ok               |

## T Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 55.80%   | 27.43%             | -18.13% |     1.12 |       55 | 55.91%     | ok               |
|          25 | 47.81%   | 27.43%             | -17.66% |     1.01 |       60 | 53.58%     | ok               |
|          15 | 47.29%   | 27.43%             | -15.08% |     0.97 |       64 | 59.73%     | ok               |
|          30 | 33.06%   | 27.43%             | -17.01% |     0.78 |       62 | 51.41%     | ok               |
|          35 | 30.55%   | 27.43%             | -14.49% |     0.75 |       62 | 48.25%     | ok               |

## TGT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -8.23%   | -3.51%             | -41.89% |    -0.05 |       79 | 46.09%     | ok               |
|          25 | -9.14%   | -3.51%             | -42.39% |    -0.09 |       61 | 41.10%     | ok               |
|          15 | -11.23%  | -3.51%             | -39.76% |    -0.1  |       69 | 50.58%     | ok               |
|          45 | -8.37%   | -3.51%             | -29.07% |    -0.12 |       50 | 28.79%     | ok               |
|          30 | -10.02%  | -3.51%             | -40.57% |    -0.12 |       56 | 38.44%     | ok               |

## TIA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 37.89%   | -91.76%            | -33.58% |     0.56 |       62 | 26.05%     | ok               |
|          35 | 31.88%   | -91.76%            | -39.93% |     0.51 |       62 | 30.84%     | ok               |
|          45 | 24.80%   | -91.76%            | -39.83% |     0.46 |       54 | 19.35%     | ok               |
|          50 | 17.56%   | -91.76%            | -43.05% |     0.41 |       34 | 11.69%     | ok               |
|          15 | -32.88%  | -91.76%            | -50.83% |    -0.01 |       99 | 51.53%     | ok               |

## TLT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -20.93%  | -9.07%             | -20.85% |    -1.6  |       72 | 31.61%     | ok               |
|          50 | -13.94%  | -9.07%             | -15.73% |    -1.69 |       30 | 13.98%     | ok               |
|          15 | -27.45%  | -9.07%             | -27.29% |    -1.92 |       77 | 39.60%     | ok               |
|          35 | -22.16%  | -9.07%             | -21.48% |    -1.94 |       66 | 25.62%     | ok               |
|          40 | -20.71%  | -9.07%             | -19.91% |    -1.97 |       58 | 20.80%     | ok               |

## TMO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 46.24%   | -7.03%             | -8.17%  |     1.05 |       38 | 30.12%     | ok               |
|          45 | 38.44%   | -7.03%             | -10.13% |     0.87 |       46 | 35.11%     | ok               |
|          40 | 36.40%   | -7.03%             | -9.91%  |     0.82 |       49 | 39.60%     | ok               |
|          35 | 20.68%   | -7.03%             | -14.06% |     0.52 |       59 | 43.93%     | ok               |
|          30 | 10.52%   | -7.03%             | -18.11% |     0.31 |       59 | 47.92%     | ok               |

## TMUS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 15.42%   | 12.92%             | -24.50% |     0.41 |       68 | 47.59%     | ok               |
|          15 | 15.88%   | 12.92%             | -26.87% |     0.41 |       69 | 59.73%     | ok               |
|          20 | 6.52%    | 12.92%             | -25.10% |     0.23 |       73 | 53.91%     | ok               |
|          25 | 5.57%    | 12.92%             | -26.30% |     0.22 |       75 | 50.25%     | ok               |
|          50 | 4.50%    | 12.92%             | -22.71% |     0.2  |       58 | 35.77%     | ok               |

## TRX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 0.82%    | 26.55%             | -18.79% |     0.11 |       54 | 37.93%     | ok               |
|          50 | -2.54%   | 26.55%             | -18.49% |    -0    |       46 | 32.38%     | ok               |
|          30 | -4.73%   | 26.55%             | -22.90% |    -0.04 |       74 | 49.81%     | ok               |
|          35 | -5.52%   | 26.55%             | -21.77% |    -0.07 |       70 | 46.55%     | ok               |
|          25 | -6.44%   | 26.55%             | -26.84% |    -0.08 |       70 | 53.07%     | ok               |

## TSLA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 68.66%   | 102.07%            | -32.60% |     0.83 |       66 | 30.28%     | ok               |
|          40 | 62.75%   | 102.07%            | -45.90% |     0.73 |       61 | 34.61%     | ok               |
|          45 | 37.88%   | 102.07%            | -46.86% |     0.55 |       65 | 31.95%     | ok               |
|          35 | 27.07%   | 102.07%            | -51.29% |     0.45 |       72 | 37.44%     | ok               |
|          30 | 3.12%    | 102.07%            | -54.91% |     0.24 |       68 | 41.93%     | ok               |

## TXN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 13.38%   | 79.29%             | -45.45% |     0.33 |       72 | 35.77%     | ok               |
|          20 | 2.88%    | 79.29%             | -38.98% |     0.19 |       62 | 59.90%     | ok               |
|          15 | 0.75%    | 79.29%             | -39.48% |     0.17 |       65 | 64.06%     | ok               |
|          35 | -5.44%   | 79.29%             | -43.38% |     0.05 |       78 | 50.42%     | ok               |
|          40 | -6.08%   | 79.29%             | -45.67% |     0.04 |       76 | 48.25%     | ok               |

## UNH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 34.21%   | -16.14%            | -37.02% |     0.59 |       52 | 29.95%     | ok               |
|          30 | 30.58%   | -16.14%            | -27.93% |     0.53 |       76 | 52.41%     | ok               |
|          35 | 27.02%   | -16.14%            | -29.28% |     0.49 |       68 | 47.25%     | ok               |
|          15 | 27.05%   | -16.14%            | -32.14% |     0.47 |       76 | 67.55%     | ok               |
|          40 | 22.59%   | -16.14%            | -35.94% |     0.44 |       60 | 42.10%     | ok               |

## UNI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -18.07%  | -76.53%            | -58.49% |    -0    |       54 | 25.67%     | ok               |
|          40 | -23.44%  | -76.53%            | -63.75% |    -0.05 |       56 | 30.65%     | ok               |
|          50 | -25.51%  | -76.53%            | -57.60% |    -0.14 |       52 | 21.07%     | ok               |
|          35 | -35.75%  | -76.53%            | -68.71% |    -0.18 |       70 | 35.63%     | ok               |
|          20 | -73.62%  | -76.53%            | -81.22% |    -0.77 |      102 | 52.30%     | ok               |

## UPS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -33.22%  | -23.76%            | -37.38% |    -0.66 |       62 | 33.11%     | ok               |
|          40 | -32.97%  | -23.76%            | -37.64% |    -0.67 |       50 | 27.95%     | ok               |
|          20 | -38.45%  | -23.76%            | -47.26% |    -0.74 |       87 | 48.42%     | ok               |
|          25 | -38.67%  | -23.76%            | -43.14% |    -0.76 |       80 | 44.43%     | ok               |
|          30 | -38.18%  | -23.76%            | -39.98% |    -0.77 |       74 | 39.60%     | ok               |

## USO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 16.31%   | 56.24%             | -33.25% |     0.38 |       48 | 26.62%     | ok               |
|          30 | 8.43%    | 56.24%             | -43.35% |     0.26 |       66 | 34.11%     | ok               |
|          15 | 6.29%    | 56.24%             | -45.94% |     0.23 |       71 | 41.43%     | ok               |
|          20 | 5.29%    | 56.24%             | -45.77% |     0.21 |       74 | 39.27%     | ok               |
|          40 | 4.41%    | 56.24%             | -41.14% |     0.2  |       59 | 29.28%     | ok               |

## VEA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 5.44%    | 48.42%             | -16.28% |     0.25 |       60 | 50.58%     | ok               |
|          20 | 1.19%    | 48.42%             | -17.70% |     0.1  |       61 | 47.92%     | ok               |
|          25 | -0.82%   | 48.42%             | -17.79% |     0.02 |       57 | 46.26%     | ok               |
|          30 | -0.98%   | 48.42%             | -17.93% |     0.01 |       58 | 44.09%     | ok               |
|          35 | -2.09%   | 48.42%             | -16.79% |    -0.03 |       56 | 43.09%     | ok               |

## VIXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -48.04%  | -62.05%            | -69.78% |    -0.43 |       46 | 10.48%     | ok               |
|          45 | -59.37%  | -62.05%            | -75.03% |    -0.61 |       60 | 16.64%     | ok               |
|          40 | -67.66%  | -62.05%            | -80.72% |    -0.74 |       76 | 21.46%     | ok               |
|          35 | -70.62%  | -62.05%            | -84.37% |    -0.76 |       90 | 26.79%     | ok               |
|          15 | -77.15%  | -62.05%            | -89.47% |    -0.77 |      101 | 44.76%     | ok               |

## VNQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -8.60%   | 16.98%             | -19.07% |    -0.37 |       60 | 28.62%     | ok               |
|          50 | -9.03%   | 16.98%             | -17.13% |    -0.41 |       56 | 26.12%     | ok               |
|          25 | -13.12%  | 16.98%             | -22.34% |    -0.51 |       69 | 40.77%     | ok               |
|          15 | -15.60%  | 16.98%             | -24.90% |    -0.58 |       71 | 45.09%     | ok               |
|          40 | -14.13%  | 16.98%             | -24.84% |    -0.62 |       74 | 32.11%     | ok               |

## VTI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 18.87%   | 47.74%             | -13.96% |     0.63 |       62 | 55.07%     | ok               |
|          15 | 12.78%   | 47.74%             | -15.70% |     0.45 |       65 | 57.57%     | ok               |
|          25 | 5.97%    | 47.74%             | -16.10% |     0.26 |       58 | 53.24%     | ok               |
|          30 | -1.07%   | 47.74%             | -18.77% |     0.02 |       66 | 51.41%     | ok               |
|          40 | -3.29%   | 47.74%             | -20.44% |    -0.07 |       68 | 44.76%     | ok               |

## VWO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -9.03%   | 47.82%             | -24.01% |    -0.26 |       69 | 49.42%     | ok               |
|          50 | -7.89%   | 47.82%             | -21.68% |    -0.28 |       60 | 32.45%     | ok               |
|          20 | -10.06%  | 47.82%             | -26.14% |    -0.31 |       67 | 47.25%     | ok               |
|          40 | -8.98%   | 47.82%             | -23.57% |    -0.31 |       70 | 37.94%     | ok               |
|          45 | -9.69%   | 47.82%             | -23.75% |    -0.35 |       62 | 34.94%     | ok               |

## VZ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -5.64%   | 10.47%             | -14.76% |    -0.16 |       50 | 24.63%     | ok               |
|          45 | -14.10%  | 10.47%             | -19.37% |    -0.46 |       58 | 27.62%     | ok               |
|          35 | -19.19%  | 10.47%             | -22.66% |    -0.64 |       61 | 33.11%     | ok               |
|          25 | -24.58%  | 10.47%             | -26.93% |    -0.77 |       80 | 41.26%     | ok               |
|          40 | -21.98%  | 10.47%             | -24.76% |    -0.78 |       64 | 30.12%     | ok               |

## WFC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.96%   | 70.59%             | -18.29% |     0.04 |       58 | 33.94%     | ok               |
|          35 | -4.61%   | 70.59%             | -22.53% |    -0.02 |       77 | 45.92%     | ok               |
|          45 | -8.98%   | 70.59%             | -24.02% |    -0.19 |       66 | 38.77%     | ok               |
|          20 | -16.79%  | 70.59%             | -29.87% |    -0.24 |       79 | 54.74%     | ok               |
|          40 | -11.31%  | 70.59%             | -24.88% |    -0.26 |       74 | 42.26%     | ok               |

## WIF-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 60.65%   | -86.53%            | -46.21% |     0.66 |       71 | 41.38%     | ok               |
|          20 | 54.98%   | -86.53%            | -40.67% |     0.64 |       65 | 38.70%     | ok               |
|          25 | -11.37%  | -86.53%            | -52.41% |     0.2  |       67 | 36.21%     | ok               |
|          50 | -20.06%  | -86.53%            | -37.87% |    -0.14 |       40 | 12.07%     | ok               |
|          30 | -43.81%  | -86.53%            | -57.06% |    -0.24 |       68 | 32.18%     | ok               |

## WMT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 56.76%   | 104.68%            | -9.18%  |     1.49 |       36 | 43.26%     | ok               |
|          50 | 50.39%   | 104.68%            | -12.19% |     1.42 |       30 | 41.10%     | ok               |
|          40 | 46.96%   | 104.68%            | -9.18%  |     1.26 |       40 | 44.43%     | ok               |
|          35 | 44.19%   | 104.68%            | -10.48% |     1.17 |       52 | 48.59%     | ok               |
|          30 | 19.98%   | 104.68%            | -21.31% |     0.58 |       59 | 51.25%     | ok               |

## XBI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 6.71%    | 76.63%             | -16.56% |     0.25 |       62 | 34.94%     | ok               |
|          45 | 5.89%    | 76.63%             | -16.74% |     0.23 |       54 | 31.78%     | ok               |
|          35 | 5.42%    | 76.63%             | -18.84% |     0.21 |       62 | 38.44%     | ok               |
|          30 | 4.25%    | 76.63%             | -19.80% |     0.19 |       62 | 40.10%     | ok               |
|          25 | -0.55%   | 76.63%             | -23.66% |     0.08 |       70 | 42.10%     | ok               |

## XLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -4.11%   | 24.20%             | -20.60% |    -0.1  |       60 | 31.95%     | ok               |
|          50 | -4.05%   | 24.20%             | -17.40% |    -0.11 |       44 | 27.62%     | ok               |
|          35 | -7.36%   | 24.20%             | -23.62% |    -0.22 |       60 | 35.44%     | ok               |
|          45 | -6.89%   | 24.20%             | -20.61% |    -0.23 |       44 | 29.12%     | ok               |
|          25 | -10.57%  | 24.20%             | -23.73% |    -0.33 |       68 | 41.10%     | ok               |

## XLC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 15.65%   | 33.16%             | -12.33% |     0.55 |       65 | 55.57%     | ok               |
|          25 | 13.48%   | 33.16%             | -12.31% |     0.48 |       62 | 57.40%     | ok               |
|          40 | 10.40%   | 33.16%             | -13.38% |     0.42 |       68 | 48.09%     | ok               |
|          35 | 10.38%   | 33.16%             | -13.38% |     0.41 |       64 | 52.58%     | ok               |
|          20 | 5.50%    | 33.16%             | -13.78% |     0.23 |       70 | 60.07%     | ok               |

## XLE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -1.92%   | 28.93%             | -25.98% |     0.02 |       56 | 36.77%     | ok               |
|          35 | -3.79%   | 28.93%             | -32.17% |    -0.02 |       65 | 44.59%     | ok               |
|          45 | -5.17%   | 28.93%             | -30.88% |    -0.07 |       62 | 39.60%     | ok               |
|          25 | -9.45%   | 28.93%             | -36.16% |    -0.15 |       79 | 49.75%     | ok               |
|          30 | -9.48%   | 28.93%             | -36.18% |    -0.17 |       71 | 46.59%     | ok               |

## XLF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.97%   | 37.43%             | -18.63% |    -0.18 |       68 | 53.74%     | ok               |
|          15 | -10.82%  | 37.43%             | -20.19% |    -0.31 |       76 | 56.57%     | ok               |
|          30 | -12.03%  | 37.43%             | -23.61% |    -0.4  |       76 | 48.25%     | ok               |
|          25 | -12.79%  | 37.43%             | -23.22% |    -0.42 |       77 | 50.42%     | ok               |
|          35 | -18.07%  | 37.43%             | -25.31% |    -0.71 |       66 | 44.76%     | ok               |

## XLI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 8.26%    | 56.77%             | -10.61% |     0.34 |       72 | 52.91%     | ok               |
|          20 | 5.43%    | 56.77%             | -12.74% |     0.26 |       63 | 48.42%     | ok               |
|          30 | 3.12%    | 56.77%             | -11.38% |     0.18 |       64 | 45.92%     | ok               |
|          50 | 2.53%    | 56.77%             | -9.25%  |     0.16 |       56 | 35.27%     | ok               |
|          45 | 2.53%    | 56.77%             | -12.27% |     0.16 |       62 | 37.10%     | ok               |

## XLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 84.37%   | 79.10%             | -14.75% |     1.35 |       41 | 52.91%     | ok               |
|          20 | 69.95%   | 79.10%             | -14.75% |     1.21 |       48 | 50.75%     | ok               |
|          25 | 66.48%   | 79.10%             | -14.75% |     1.2  |       42 | 48.59%     | ok               |
|          30 | 64.31%   | 79.10%             | -14.75% |     1.2  |       42 | 47.42%     | ok               |
|          35 | 45.98%   | 79.10%             | -13.61% |     0.96 |       54 | 44.76%     | ok               |

## XLM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 26.14%   | -60.29%            | -38.97% |     0.48 |       44 | 27.39%     | ok               |
|          45 | 22.34%   | -60.29%            | -43.99% |     0.44 |       50 | 31.03%     | ok               |
|          30 | 0.26%    | -60.29%            | -50.36% |     0.22 |       69 | 45.59%     | ok               |
|          40 | -3.03%   | -60.29%            | -43.80% |     0.17 |       49 | 35.25%     | ok               |
|          35 | -8.51%   | -60.29%            | -50.42% |     0.12 |       69 | 41.57%     | ok               |

## XLP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 11.69%   | 14.21%             | -5.66%  |     0.71 |       54 | 34.28%     | ok               |
|          50 | 9.69%    | 14.21%             | -6.08%  |     0.61 |       58 | 31.78%     | ok               |
|          40 | 9.44%    | 14.21%             | -7.77%  |     0.57 |       70 | 38.44%     | ok               |
|          35 | 8.49%    | 14.21%             | -9.73%  |     0.51 |       66 | 41.43%     | ok               |
|          30 | 6.56%    | 14.21%             | -11.16% |     0.4  |       68 | 42.93%     | ok               |

## XLU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 10.52%   | 50.27%             | -9.11%  |     0.55 |       48 | 29.95%     | ok               |
|          45 | 8.24%    | 50.27%             | -10.56% |     0.44 |       52 | 30.95%     | ok               |
|          40 | 4.79%    | 50.27%             | -11.94% |     0.27 |       58 | 32.61%     | ok               |
|          35 | 0.74%    | 50.27%             | -16.24% |     0.08 |       62 | 34.94%     | ok               |
|          30 | -1.66%   | 50.27%             | -18.15% |    -0.03 |       67 | 38.10%     | ok               |

## XLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -12.12%  | 12.92%             | -16.83% |    -0.59 |       66 | 35.61%     | ok               |
|          25 | -13.41%  | 12.92%             | -18.06% |    -0.66 |       68 | 36.94%     | ok               |
|          15 | -17.34%  | 12.92%             | -21.47% |    -0.84 |       79 | 41.76%     | ok               |
|          20 | -17.27%  | 12.92%             | -21.56% |    -0.86 |       73 | 38.60%     | ok               |
|          50 | -14.45%  | 12.92%             | -18.24% |    -0.87 |       54 | 24.29%     | ok               |

## XLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 5.14%    | 29.00%             | -12.94% |     0.23 |       70 | 41.43%     | ok               |
|          30 | 3.26%    | 29.00%             | -14.01% |     0.17 |       70 | 44.43%     | ok               |
|          50 | 1.64%    | 29.00%             | -11.49% |     0.12 |       50 | 29.45%     | ok               |
|          15 | 1.20%    | 29.00%             | -15.77% |     0.11 |       74 | 51.25%     | ok               |
|          45 | -1.43%   | 29.00%             | -13.48% |    -0    |       54 | 32.11%     | ok               |

## XOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 5.58%    | 33.90%             | -19.90% |     0.23 |       58 | 37.10%     | ok               |
|          30 | 4.54%    | 33.90%             | -20.29% |     0.2  |       58 | 36.44%     | ok               |
|          50 | 1.92%    | 33.90%             | -21.35% |     0.13 |       46 | 29.95%     | ok               |
|          20 | 1.68%    | 33.90%             | -25.56% |     0.12 |       63 | 39.60%     | ok               |
|          35 | 0.09%    | 33.90%             | -20.93% |     0.08 |       60 | 35.27%     | ok               |

## XRP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -26.00%  | -66.53%            | -47.57% |    -0.16 |       70 | 40.80%     | ok               |
|          40 | -32.87%  | -66.53%            | -45.79% |    -0.31 |       62 | 34.67%     | ok               |
|          30 | -39.88%  | -66.53%            | -56.67% |    -0.38 |       74 | 45.21%     | ok               |
|          45 | -40.43%  | -66.53%            | -47.76% |    -0.47 |       62 | 30.27%     | ok               |
|          50 | -37.86%  | -66.53%            | -39.26% |    -0.53 |       64 | 22.61%     | ok               |

## YFI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -32.83%  | -78.15%            | -52.37% |    -0.46 |       62 | 27.20%     | ok               |
|          45 | -38.27%  | -78.15%            | -54.04% |    -0.66 |       64 | 22.61%     | ok               |
|          35 | -49.34%  | -78.15%            | -64.08% |    -0.73 |       73 | 34.67%     | ok               |
|          30 | -52.55%  | -78.15%            | -67.78% |    -0.75 |       81 | 40.80%     | ok               |
|          50 | -41.48%  | -78.15%            | -51.80% |    -0.84 |       52 | 17.43%     | ok               |

## ZEC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 124.17%  | 707.07%            | -24.66% |     0.9  |       50 | 23.18%     | ok               |
|          35 | 98.51%   | 707.07%            | -44.34% |     0.79 |       58 | 30.84%     | ok               |
|          25 | 70.20%   | 707.07%            | -48.59% |     0.68 |       59 | 39.85%     | ok               |
|          30 | 52.90%   | 707.07%            | -47.68% |     0.6  |       67 | 36.40%     | ok               |
|          50 | 54.10%   | 707.07%            | -37.94% |     0.6  |       52 | 20.69%     | ok               |
