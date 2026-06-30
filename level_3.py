import matplotlib
matplotlib.use('Agg')
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

data = yf.download("^GSPC", start="2024-01-01", end="2026-01-01")["Close"]
returns = data.pct_change().dropna()

mean_return = returns.mean()
volatility = returns.std()

print("Rendimento medio giornaliero:", mean_return)
print("Volatilita giornaliera:", volatility)

n_simulations = 10000
simulated_returns = np.random.normal(mean_return, volatility, n_simulations)

print(simulated_returns[:10])

VaR_95 = np.percentile(simulated_returns, 5)
print("VaR al 95%:", VaR_95)

plt.figure(figsize=(10, 5))
plt.hist(simulated_returns, bins=100, edgecolor='black')
plt.axvline(VaR_95, color='red', linestyle='--', linewidth=2, label=f'VaR 95%: {VaR_95:.4f}')
plt.title("Monte Carlo Simulation - S&P 500 Daily Returns")
plt.xlabel("Simulated Return")
plt.ylabel("Frequency")
plt.legend()
plt.tight_layout()
plt.savefig("montecarlo_var.png")

#95 model confidence
VaR_95_historical = np.percentile(returns.values, 5)
print("VaR storico al 95%:", VaR_95_historical)
print("VaR parametrico al 95%:", VaR_95)

#99 model confidence
VaR_99_historical = np.percentile(returns.values, 1)
VaR_99_parametric = np.percentile(simulated_returns, 1)
print("VaR storico al 99%:", VaR_99_historical)
print("VaR parametrico al 99%:", VaR_99_parametric)