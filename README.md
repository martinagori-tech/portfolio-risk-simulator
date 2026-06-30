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
- At the 95% confidence level, parametric (normal distribution) VaR closely matches historical VaR (-1.56% vs -1.56%)
- At the 99% confidence level, the gap widens: historical VaR (-2.71%) is notably worse than parametric VaR (-2.22%), confirming the fat-tail behavior observed in the return distribution — the normal model underestimates extreme risk

## Tech Stack
- Python 3.14
- yfinance, pandas, numpy, matplotlib, seaborn, scipy
