import matplotlib
matplotlib.use('Agg')
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Scarica dati S&P 500
data = yf.download("^GSPC", start="2024-01-01", end="2026-01-01")

# Calcola rendimenti giornalieri
returns = data["Close"].pct_change().dropna()
print(returns.head(10))

# Grafico 1 - Rendimenti nel tempo
plt.figure(figsize=(12, 5))
plt.plot(returns.index, returns.values)
plt.title("S&P 500 - Rendimenti Giornalieri")
plt.xlabel("Data")
plt.ylabel("Rendimento")
plt.axhline(0, color="red", linestyle="--", linewidth=0.8)
plt.tight_layout()
plt.savefig("rendimenti.png")

# Grafico 2 - Distribuzione dei rendimenti
plt.figure(figsize=(10, 5))
plt.hist(returns.values, bins=100, edgecolor='black')
plt.title("Distribuzione dei Rendimenti Giornalieri - S&P 500")
plt.xlabel("Rendimento")
plt.ylabel("Frequenza")
plt.tight_layout()
plt.savefig("distribuzione.png")