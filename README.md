# Stock-Factor Network

This project builds an interactive graph-based analysis system that connects stock tickers with financial factors based on historical market data. The user can explore the network to discover which factors influence which stocks, find similar stocks, and analyze the graph interactively through a command-line interface (CLI).

## Project Overview

- **Goal:** Analyze how different financial factors (like momentum, volatility, and liquidity) influence the returns of various stocks using a network graph structure.
- **Data Source:** Cleaned and processed CRSP-like dataset (`data_2019-2024.csv`) containing stock prices, returns, volumes, and market metrics.
- **Technology Stack:** `pandas`, `networkx`, `statsmodels`, CLI (command-line interface)

## Factor Definitions

The following financial factors were calculated per stock:

| Factor              | Description |
|---------------------|-------------|
| `momentum`          | log(price_t / price_{t-n}) |
| `volatility`        | Rolling standard deviation of returns |
| `liquidity`         | Volume / Shares Outstanding |
| `amplitude`         | (High - Low) / Close Price |
| `dividend_yield`    | DIVAMT / Price |
| `gap_return`        | (Open - Prev Close) / Prev Close |
| `trading_activity`  | Number of trades / rolling mean |
| `market_corr`       | Correlation with market return (vwretd) |

---

## Project Structure

