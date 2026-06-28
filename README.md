# Portfolio Risk Simulator

A quantitative analysis of portfolio risk using real market data across three asset classes: S&P 500, Gold, and US 20-year Bonds.

## Objective
To model and stress-test portfolio risk through return analysis, correlation structure, Monte Carlo simulation, and tail-risk scenarios — exploring how diversification holds (or breaks) under market stress.

## Project Structure
- `level_1.py` — S&P 500 daily returns: distribution and time series analysis
- `level_2.py` — Multi-asset correlation matrix and heatmap
- `level_3.py` — Monte Carlo simulation and Value at Risk (VaR) estimation *(coming soon)*
- `level_4.py` — Stress testing: normal conditions vs tail events *(coming soon)*

## Key Findings (so far)
- S&P 500 shows a near-normal return distribution with fat tails — extreme events like the April 2025 tariff shock (-6% in a single day) are more frequent than classical models predict
- In the 2024–2026 period, S&P 500, Gold, and Bonds shorrelations, suggesting genuine diversification benefits

## Tech Stack
- Python 3.14
- yfinance, pandas, numpy, matplotlib, seaborn, scipy

## Author
Martina Gori — incoming MEng ORIE, Cornell Tech
