# Backtest Report

_Generated: 2025-09-29T04:38:48.132838Z_

## Data Sources

This report uses real market data from the following sources:

- **Crypto Data**: Kraken API → Coinbase API → CoinGecko API (fallback chain)
- **Stock Data**: Stooq API → Yahoo Finance (fallback)
- **Index Data**: Yahoo Finance

All data sources are free, no API keys required for primary sources.

## Summary

| symbol    |   trades |      return |   mdd |   sharpe |   trend_s_mean |   momentum_s_mean |   strength_s_mean |   vol_s_mean |   fib_s_mean |   pivot_s_mean |
|:----------|---------:|------------:|------:|---------:|---------------:|------------------:|------------------:|-------------:|-------------:|---------------:|
| AAPL      |        1 | -0.00039992 |     0 |      nan |            5   |               2.5 |               0   |         0.25 |        -0.25 |           0.5  |
| AAVE-USD  |        0 |  0          |     0 |        0 |          nan   |             nan   |             nan   |       nan    |       nan    |         nan    |
| ADA-USD   |        0 |  0          |     0 |        0 |          nan   |             nan   |             nan   |       nan    |       nan    |         nan    |
| AMD       |        0 |  0          |     0 |        0 |          nan   |             nan   |             nan   |       nan    |       nan    |         nan    |
| AMZN      |        1 | -0.00040008 |     0 |      nan |           -2.5 |              -2.5 |              -1   |         0.25 |        -0.25 |           0.5  |
| AVAX-USD  |        0 |  0          |     0 |        0 |          nan   |             nan   |             nan   |       nan    |       nan    |         nan    |
| AVGO      |        0 |  0          |     0 |        0 |          nan   |             nan   |             nan   |       nan    |       nan    |         nan    |
| BTC-USD   |        0 |  0          |     0 |        0 |          nan   |             nan   |             nan   |       nan    |       nan    |         nan    |
| COMP-USD  |        1 | -0.00040008 |     0 |      nan |           -3.5 |              -2   |               0.5 |         0.25 |        -0.25 |           0.5  |
| CRV-USD   |        1 | -0.00040008 |     0 |      nan |           -3.5 |              -2   |               0.5 |        -0.75 |         1    |           0.5  |
| DIA       |        1 | -0.00039992 |     0 |      nan |            4.5 |               0.5 |               1.5 |         0.75 |        -0.25 |           0.75 |
| ETH-USD   |        0 |  0          |     0 |        0 |          nan   |             nan   |             nan   |       nan    |       nan    |         nan    |
| GOOGL     |        1 | -0.00039992 |     0 |      nan |            4.5 |               0.5 |               1.5 |         0.25 |        -0.25 |           0.5  |
| INTC      |        1 | -0.00039992 |     0 |      nan |            5   |               2   |               1.5 |         0    |        -0.25 |           0.75 |
| IWM       |        1 | -0.00039992 |     0 |      nan |            4.5 |               0.5 |               1.5 |         0.5  |        -0.25 |           0.75 |
| LINK-USD  |        0 |  0          |     0 |        0 |          nan   |             nan   |             nan   |       nan    |       nan    |         nan    |
| MATIC-USD |        1 | -0.00040008 |     0 |      nan |           -3.5 |              -2.5 |               0.5 |         0    |         1    |           0.5  |
| META      |        0 |  0          |     0 |        0 |          nan   |             nan   |             nan   |       nan    |       nan    |         nan    |
| MKR-USD   |        0 |  0          |     0 |        0 |          nan   |             nan   |             nan   |       nan    |       nan    |         nan    |
| MSFT      |        1 | -0.00039992 |     0 |      nan |            4.5 |               2.5 |               0   |         0.75 |        -0.25 |           0.75 |
| NFLX      |        0 |  0          |     0 |        0 |          nan   |             nan   |             nan   |       nan    |       nan    |         nan    |
| NVDA      |        1 | -0.00039992 |     0 |      nan |            4.5 |               2.5 |               0   |         0.25 |        -0.25 |           0.5  |
| QCOM      |        1 | -0.00039992 |     0 |      nan |            5   |               2.5 |               1.5 |         0.25 |        -0.25 |          -0.5  |
| QQQ       |        1 | -0.00039992 |     0 |      nan |            4.5 |               2   |               1.5 |         0.5  |        -0.25 |           0.5  |
| SOL-USD   |        0 |  0          |     0 |        0 |          nan   |             nan   |             nan   |       nan    |       nan    |         nan    |
| SPY       |        1 | -0.00039992 |     0 |      nan |            4.5 |               0.5 |               1.5 |         0.75 |        -0.25 |           0.75 |
| SUSHI-USD |        1 | -0.00040008 |     0 |      nan |           -3.5 |              -2   |               0.5 |        -0.25 |        -0.25 |           0.5  |
| TSLA      |        1 | -0.00039992 |     0 |      nan |            3.5 |               2   |               1.5 |         0    |        -0.25 |           0.75 |
| TXN       |        0 |  0          |     0 |        0 |          nan   |             nan   |             nan   |       nan    |       nan    |         nan    |
| UNI-USD   |        1 | -0.00040008 |     0 |      nan |           -3.5 |              -2.5 |               0.5 |        -0.25 |         1    |           0.5  |
| VTI       |        1 | -0.00039992 |     0 |      nan |            4.5 |               0.5 |               1.5 |         0.75 |        -0.25 |           0.75 |
| XRP-USD   |        0 |  0          |     0 |        0 |          nan   |             nan   |             nan   |       nan    |       nan    |         nan    |
| YFI-USD   |        0 |  0          |     0 |        0 |          nan   |             nan   |             nan   |       nan    |       nan    |         nan    |

## AAPL — Threshold Sweep

| symbol   |   threshold |   trades |      return |   mdd |   sharpe |   trend_s_mean |   momentum_s_mean |   strength_s_mean |   vol_s_mean |   fib_s_mean |   pivot_s_mean |
|:---------|------------:|---------:|------------:|------:|---------:|---------------:|------------------:|------------------:|-------------:|-------------:|---------------:|
| AAPL     |          15 |        1 | -0.00039992 |     0 |      nan |              5 |               2.5 |                 0 |         0.25 |        -0.25 |            0.5 |

Top 5 thresholds by Sharpe:
|   threshold |      return |   mdd |   sharpe |   trades |
|------------:|------------:|------:|---------:|---------:|
|          15 | -0.00039992 |     0 |      nan |        1 |
|          20 | -0.00039992 |     0 |      nan |        1 |
|          25 | -0.00039992 |     0 |      nan |        1 |
|          30 | -0.00039992 |     0 |      nan |        1 |
|          35 | -0.00039992 |     0 |      nan |        1 |

## AAVE-USD — Threshold Sweep

| symbol   |   threshold |   trades |   return |   mdd |   sharpe |
|:---------|------------:|---------:|---------:|------:|---------:|
| AAVE-USD |          15 |        0 |        0 |     0 |        0 |

Top 5 thresholds by Sharpe:
|   threshold |   return |   mdd |   sharpe |   trades |
|------------:|---------:|------:|---------:|---------:|
|          15 |        0 |     0 |        0 |        0 |
|          20 |        0 |     0 |        0 |        0 |
|          25 |        0 |     0 |        0 |        0 |
|          30 |        0 |     0 |        0 |        0 |
|          35 |        0 |     0 |        0 |        0 |

## ADA-USD — Threshold Sweep

| symbol   |   threshold |   trades |   return |   mdd |   sharpe |
|:---------|------------:|---------:|---------:|------:|---------:|
| ADA-USD  |          15 |        0 |        0 |     0 |        0 |

Top 5 thresholds by Sharpe:
|   threshold |   return |   mdd |   sharpe |   trades |
|------------:|---------:|------:|---------:|---------:|
|          15 |        0 |     0 |        0 |        0 |
|          20 |        0 |     0 |        0 |        0 |
|          25 |        0 |     0 |        0 |        0 |
|          30 |        0 |     0 |        0 |        0 |
|          35 |        0 |     0 |        0 |        0 |

## AMD — Threshold Sweep

| symbol   |   threshold |   trades |   return |   mdd |   sharpe |
|:---------|------------:|---------:|---------:|------:|---------:|
| AMD      |          15 |        0 |        0 |     0 |        0 |

Top 5 thresholds by Sharpe:
|   threshold |   return |   mdd |   sharpe |   trades |
|------------:|---------:|------:|---------:|---------:|
|          15 |        0 |     0 |        0 |        0 |
|          20 |        0 |     0 |        0 |        0 |
|          25 |        0 |     0 |        0 |        0 |
|          30 |        0 |     0 |        0 |        0 |
|          35 |        0 |     0 |        0 |        0 |

## AMZN — Threshold Sweep

| symbol   |   threshold |   trades |   return |   mdd |   sharpe |   trend_s_mean |   momentum_s_mean |   strength_s_mean |   vol_s_mean |   fib_s_mean |   pivot_s_mean |
|:---------|------------:|---------:|---------:|------:|---------:|---------------:|------------------:|------------------:|-------------:|-------------:|---------------:|
| AMZN     |          50 |        0 |        0 |     0 |        0 |            nan |               nan |               nan |          nan |          nan |            nan |

Top 5 thresholds by Sharpe:
|   threshold |      return |   mdd |   sharpe |   trades |
|------------:|------------:|------:|---------:|---------:|
|          50 |  0          |     0 |        0 |        0 |
|          15 | -0.00040008 |     0 |      nan |        1 |
|          20 | -0.00040008 |     0 |      nan |        1 |
|          25 | -0.00040008 |     0 |      nan |        1 |
|          30 | -0.00040008 |     0 |      nan |        1 |

## AVAX-USD — Threshold Sweep

| symbol   |   threshold |   trades |   return |   mdd |   sharpe |   trend_s_mean |   momentum_s_mean |   strength_s_mean |   vol_s_mean |   fib_s_mean |   pivot_s_mean |
|:---------|------------:|---------:|---------:|------:|---------:|---------------:|------------------:|------------------:|-------------:|-------------:|---------------:|
| AVAX-USD |          20 |        0 |        0 |     0 |        0 |            nan |               nan |               nan |          nan |          nan |            nan |

Top 5 thresholds by Sharpe:
|   threshold |   return |   mdd |   sharpe |   trades |
|------------:|---------:|------:|---------:|---------:|
|          20 |        0 |     0 |        0 |        0 |
|          25 |        0 |     0 |        0 |        0 |
|          30 |        0 |     0 |        0 |        0 |
|          35 |        0 |     0 |        0 |        0 |
|          40 |        0 |     0 |        0 |        0 |

## AVGO — Threshold Sweep

| symbol   |   threshold |   trades |   return |   mdd |   sharpe |   trend_s_mean |   momentum_s_mean |   strength_s_mean |   vol_s_mean |   fib_s_mean |   pivot_s_mean |
|:---------|------------:|---------:|---------:|------:|---------:|---------------:|------------------:|------------------:|-------------:|-------------:|---------------:|
| AVGO     |          25 |        0 |        0 |     0 |        0 |            nan |               nan |               nan |          nan |          nan |            nan |

Top 5 thresholds by Sharpe:
|   threshold |   return |   mdd |   sharpe |   trades |
|------------:|---------:|------:|---------:|---------:|
|          25 |        0 |     0 |        0 |        0 |
|          30 |        0 |     0 |        0 |        0 |
|          35 |        0 |     0 |        0 |        0 |
|          40 |        0 |     0 |        0 |        0 |
|          45 |        0 |     0 |        0 |        0 |

## BTC-USD — Threshold Sweep

| symbol   |   threshold |   trades |   return |   mdd |   sharpe |   trend_s_mean |   momentum_s_mean |   strength_s_mean |   vol_s_mean |   fib_s_mean |   pivot_s_mean |
|:---------|------------:|---------:|---------:|------:|---------:|---------------:|------------------:|------------------:|-------------:|-------------:|---------------:|
| BTC-USD  |          20 |        0 |        0 |     0 |        0 |            nan |               nan |               nan |          nan |          nan |            nan |

Top 5 thresholds by Sharpe:
|   threshold |   return |   mdd |   sharpe |   trades |
|------------:|---------:|------:|---------:|---------:|
|          20 |        0 |     0 |        0 |        0 |
|          25 |        0 |     0 |        0 |        0 |
|          30 |        0 |     0 |        0 |        0 |
|          35 |        0 |     0 |        0 |        0 |
|          40 |        0 |     0 |        0 |        0 |

## COMP-USD — Threshold Sweep

| symbol   |   threshold |   trades |   return |   mdd |   sharpe |   trend_s_mean |   momentum_s_mean |   strength_s_mean |   vol_s_mean |   fib_s_mean |   pivot_s_mean |
|:---------|------------:|---------:|---------:|------:|---------:|---------------:|------------------:|------------------:|-------------:|-------------:|---------------:|
| COMP-USD |          45 |        0 |        0 |     0 |        0 |            nan |               nan |               nan |          nan |          nan |            nan |

Top 5 thresholds by Sharpe:
|   threshold |      return |   mdd |   sharpe |   trades |
|------------:|------------:|------:|---------:|---------:|
|          45 |  0          |     0 |        0 |        0 |
|          50 |  0          |     0 |        0 |        0 |
|          15 | -0.00040008 |     0 |      nan |        1 |
|          20 | -0.00040008 |     0 |      nan |        1 |
|          25 | -0.00040008 |     0 |      nan |        1 |

## CRV-USD — Threshold Sweep

| symbol   |   threshold |   trades |   return |   mdd |   sharpe |   trend_s_mean |   momentum_s_mean |   strength_s_mean |   vol_s_mean |   fib_s_mean |   pivot_s_mean |
|:---------|------------:|---------:|---------:|------:|---------:|---------------:|------------------:|------------------:|-------------:|-------------:|---------------:|
| CRV-USD  |          45 |        0 |        0 |     0 |        0 |            nan |               nan |               nan |          nan |          nan |            nan |

Top 5 thresholds by Sharpe:
|   threshold |      return |   mdd |   sharpe |   trades |
|------------:|------------:|------:|---------:|---------:|
|          45 |  0          |     0 |        0 |        0 |
|          50 |  0          |     0 |        0 |        0 |
|          15 | -0.00040008 |     0 |      nan |        1 |
|          20 | -0.00040008 |     0 |      nan |        1 |
|          25 | -0.00040008 |     0 |      nan |        1 |

## DIA — Threshold Sweep

| symbol   |   threshold |   trades |      return |   mdd |   sharpe |   trend_s_mean |   momentum_s_mean |   strength_s_mean |   vol_s_mean |   fib_s_mean |   pivot_s_mean |
|:---------|------------:|---------:|------------:|------:|---------:|---------------:|------------------:|------------------:|-------------:|-------------:|---------------:|
| DIA      |          15 |        1 | -0.00039992 |     0 |      nan |            4.5 |               0.5 |               1.5 |         0.75 |        -0.25 |           0.75 |

Top 5 thresholds by Sharpe:
|   threshold |      return |   mdd |   sharpe |   trades |
|------------:|------------:|------:|---------:|---------:|
|          15 | -0.00039992 |     0 |      nan |        1 |
|          20 | -0.00039992 |     0 |      nan |        1 |
|          25 | -0.00039992 |     0 |      nan |        1 |
|          30 | -0.00039992 |     0 |      nan |        1 |
|          35 | -0.00039992 |     0 |      nan |        1 |

## ETH-USD — Threshold Sweep

| symbol   |   threshold |   trades |   return |   mdd |   sharpe |   trend_s_mean |   momentum_s_mean |   strength_s_mean |   vol_s_mean |   fib_s_mean |   pivot_s_mean |
|:---------|------------:|---------:|---------:|------:|---------:|---------------:|------------------:|------------------:|-------------:|-------------:|---------------:|
| ETH-USD  |          25 |        0 |        0 |     0 |        0 |            nan |               nan |               nan |          nan |          nan |            nan |

Top 5 thresholds by Sharpe:
|   threshold |   return |   mdd |   sharpe |   trades |
|------------:|---------:|------:|---------:|---------:|
|          25 |        0 |     0 |        0 |        0 |
|          30 |        0 |     0 |        0 |        0 |
|          35 |        0 |     0 |        0 |        0 |
|          40 |        0 |     0 |        0 |        0 |
|          45 |        0 |     0 |        0 |        0 |

## GOOGL — Threshold Sweep

| symbol   |   threshold |   trades |      return |   mdd |   sharpe |   trend_s_mean |   momentum_s_mean |   strength_s_mean |   vol_s_mean |   fib_s_mean |   pivot_s_mean |
|:---------|------------:|---------:|------------:|------:|---------:|---------------:|------------------:|------------------:|-------------:|-------------:|---------------:|
| GOOGL    |          15 |        1 | -0.00039992 |     0 |      nan |            4.5 |               0.5 |               1.5 |         0.25 |        -0.25 |            0.5 |

Top 5 thresholds by Sharpe:
|   threshold |      return |   mdd |   sharpe |   trades |
|------------:|------------:|------:|---------:|---------:|
|          15 | -0.00039992 |     0 |      nan |        1 |
|          20 | -0.00039992 |     0 |      nan |        1 |
|          25 | -0.00039992 |     0 |      nan |        1 |
|          30 | -0.00039992 |     0 |      nan |        1 |
|          35 | -0.00039992 |     0 |      nan |        1 |

## INTC — Threshold Sweep

| symbol   |   threshold |   trades |      return |   mdd |   sharpe |   trend_s_mean |   momentum_s_mean |   strength_s_mean |   vol_s_mean |   fib_s_mean |   pivot_s_mean |
|:---------|------------:|---------:|------------:|------:|---------:|---------------:|------------------:|------------------:|-------------:|-------------:|---------------:|
| INTC     |          15 |        1 | -0.00039992 |     0 |      nan |              5 |                 2 |               1.5 |            0 |        -0.25 |           0.75 |

Top 5 thresholds by Sharpe:
|   threshold |      return |   mdd |   sharpe |   trades |
|------------:|------------:|------:|---------:|---------:|
|          15 | -0.00039992 |     0 |      nan |        1 |
|          20 | -0.00039992 |     0 |      nan |        1 |
|          25 | -0.00039992 |     0 |      nan |        1 |
|          30 | -0.00039992 |     0 |      nan |        1 |
|          35 | -0.00039992 |     0 |      nan |        1 |

## IWM — Threshold Sweep

| symbol   |   threshold |   trades |      return |   mdd |   sharpe |   trend_s_mean |   momentum_s_mean |   strength_s_mean |   vol_s_mean |   fib_s_mean |   pivot_s_mean |
|:---------|------------:|---------:|------------:|------:|---------:|---------------:|------------------:|------------------:|-------------:|-------------:|---------------:|
| IWM      |          15 |        1 | -0.00039992 |     0 |      nan |            4.5 |               0.5 |               1.5 |          0.5 |        -0.25 |           0.75 |

Top 5 thresholds by Sharpe:
|   threshold |      return |   mdd |   sharpe |   trades |
|------------:|------------:|------:|---------:|---------:|
|          15 | -0.00039992 |     0 |      nan |        1 |
|          20 | -0.00039992 |     0 |      nan |        1 |
|          25 | -0.00039992 |     0 |      nan |        1 |
|          30 | -0.00039992 |     0 |      nan |        1 |
|          35 | -0.00039992 |     0 |      nan |        1 |

## LINK-USD — Threshold Sweep

| symbol   |   threshold |   trades |   return |   mdd |   sharpe |
|:---------|------------:|---------:|---------:|------:|---------:|
| LINK-USD |          15 |        0 |        0 |     0 |        0 |

Top 5 thresholds by Sharpe:
|   threshold |   return |   mdd |   sharpe |   trades |
|------------:|---------:|------:|---------:|---------:|
|          15 |        0 |     0 |        0 |        0 |
|          20 |        0 |     0 |        0 |        0 |
|          25 |        0 |     0 |        0 |        0 |
|          30 |        0 |     0 |        0 |        0 |
|          35 |        0 |     0 |        0 |        0 |

## MATIC-USD — Threshold Sweep

| symbol    |   threshold |   trades |   return |   mdd |   sharpe |   trend_s_mean |   momentum_s_mean |   strength_s_mean |   vol_s_mean |   fib_s_mean |   pivot_s_mean |
|:----------|------------:|---------:|---------:|------:|---------:|---------------:|------------------:|------------------:|-------------:|-------------:|---------------:|
| MATIC-USD |          45 |        0 |        0 |     0 |        0 |            nan |               nan |               nan |          nan |          nan |            nan |

Top 5 thresholds by Sharpe:
|   threshold |      return |   mdd |   sharpe |   trades |
|------------:|------------:|------:|---------:|---------:|
|          45 |  0          |     0 |        0 |        0 |
|          50 |  0          |     0 |        0 |        0 |
|          15 | -0.00040008 |     0 |      nan |        1 |
|          20 | -0.00040008 |     0 |      nan |        1 |
|          25 | -0.00040008 |     0 |      nan |        1 |

## META — Threshold Sweep

| symbol   |   threshold |   trades |   return |   mdd |   sharpe |
|:---------|------------:|---------:|---------:|------:|---------:|
| META     |          15 |        0 |        0 |     0 |        0 |

Top 5 thresholds by Sharpe:
|   threshold |   return |   mdd |   sharpe |   trades |
|------------:|---------:|------:|---------:|---------:|
|          15 |        0 |     0 |        0 |        0 |
|          20 |        0 |     0 |        0 |        0 |
|          25 |        0 |     0 |        0 |        0 |
|          30 |        0 |     0 |        0 |        0 |
|          35 |        0 |     0 |        0 |        0 |

## MKR-USD — Threshold Sweep

| symbol   |   threshold |   trades |   return |   mdd |   sharpe |
|:---------|------------:|---------:|---------:|------:|---------:|
| MKR-USD  |          15 |        0 |        0 |     0 |        0 |

Top 5 thresholds by Sharpe:
|   threshold |   return |   mdd |   sharpe |   trades |
|------------:|---------:|------:|---------:|---------:|
|          15 |        0 |     0 |        0 |        0 |
|          20 |        0 |     0 |        0 |        0 |
|          25 |        0 |     0 |        0 |        0 |
|          30 |        0 |     0 |        0 |        0 |
|          35 |        0 |     0 |        0 |        0 |

## MSFT — Threshold Sweep

| symbol   |   threshold |   trades |      return |   mdd |   sharpe |   trend_s_mean |   momentum_s_mean |   strength_s_mean |   vol_s_mean |   fib_s_mean |   pivot_s_mean |
|:---------|------------:|---------:|------------:|------:|---------:|---------------:|------------------:|------------------:|-------------:|-------------:|---------------:|
| MSFT     |          15 |        1 | -0.00039992 |     0 |      nan |            4.5 |               2.5 |                 0 |         0.75 |        -0.25 |           0.75 |

Top 5 thresholds by Sharpe:
|   threshold |      return |   mdd |   sharpe |   trades |
|------------:|------------:|------:|---------:|---------:|
|          15 | -0.00039992 |     0 |      nan |        1 |
|          20 | -0.00039992 |     0 |      nan |        1 |
|          25 | -0.00039992 |     0 |      nan |        1 |
|          30 | -0.00039992 |     0 |      nan |        1 |
|          35 | -0.00039992 |     0 |      nan |        1 |

## NFLX — Threshold Sweep

| symbol   |   threshold |   trades |   return |   mdd |   sharpe |
|:---------|------------:|---------:|---------:|------:|---------:|
| NFLX     |          15 |        0 |        0 |     0 |        0 |

Top 5 thresholds by Sharpe:
|   threshold |   return |   mdd |   sharpe |   trades |
|------------:|---------:|------:|---------:|---------:|
|          15 |        0 |     0 |        0 |        0 |
|          20 |        0 |     0 |        0 |        0 |
|          25 |        0 |     0 |        0 |        0 |
|          30 |        0 |     0 |        0 |        0 |
|          35 |        0 |     0 |        0 |        0 |

## NVDA — Threshold Sweep

| symbol   |   threshold |   trades |      return |   mdd |   sharpe |   trend_s_mean |   momentum_s_mean |   strength_s_mean |   vol_s_mean |   fib_s_mean |   pivot_s_mean |
|:---------|------------:|---------:|------------:|------:|---------:|---------------:|------------------:|------------------:|-------------:|-------------:|---------------:|
| NVDA     |          15 |        1 | -0.00039992 |     0 |      nan |            4.5 |               2.5 |                 0 |         0.25 |        -0.25 |            0.5 |

Top 5 thresholds by Sharpe:
|   threshold |      return |   mdd |   sharpe |   trades |
|------------:|------------:|------:|---------:|---------:|
|          15 | -0.00039992 |     0 |      nan |        1 |
|          20 | -0.00039992 |     0 |      nan |        1 |
|          25 | -0.00039992 |     0 |      nan |        1 |
|          30 | -0.00039992 |     0 |      nan |        1 |
|          35 | -0.00039992 |     0 |      nan |        1 |

## SOL-USD — Threshold Sweep

| symbol   |   threshold |   trades |   return |   mdd |   sharpe |
|:---------|------------:|---------:|---------:|------:|---------:|
| SOL-USD  |          15 |        0 |        0 |     0 |        0 |

Top 5 thresholds by Sharpe:
|   threshold |   return |   mdd |   sharpe |   trades |
|------------:|---------:|------:|---------:|---------:|
|          15 |        0 |     0 |        0 |        0 |
|          20 |        0 |     0 |        0 |        0 |
|          25 |        0 |     0 |        0 |        0 |
|          30 |        0 |     0 |        0 |        0 |
|          35 |        0 |     0 |        0 |        0 |

## XRP-USD — Threshold Sweep

| symbol   |   threshold |   trades |    return |       mdd |       sharpe |   trend_s_mean |   momentum_s_mean |   strength_s_mean |   vol_s_mean |   fib_s_mean |   pivot_s_mean |
|:---------|------------:|---------:|----------:|----------:|-------------:|---------------:|------------------:|------------------:|-------------:|-------------:|---------------:|
| XRP-USD  |          15 |        3 | -0.999889 | -0.669374 | -1.20661e+12 |        2.93333 |               0.4 |           1.16667 |     0.116667 |     0.166667 |      -0.116667 |

Top 5 thresholds by Sharpe:
|   threshold |    return |       mdd |       sharpe |   trades |
|------------:|----------:|----------:|-------------:|---------:|
|          15 | -0.999889 | -0.669374 | -1.20661e+12 |        3 |
|          20 | -0.999889 | -0.669374 | -1.20661e+12 |        3 |
|          25 | -0.999889 | -0.669374 | -1.20661e+12 |        3 |
|          30 | -0.999889 | -0.669374 | -1.20661e+12 |        3 |
|          35 | -0.999889 | -0.669374 | -1.20661e+12 |        3 |
