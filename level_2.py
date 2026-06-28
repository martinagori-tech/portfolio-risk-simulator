import matplotlib
matplotlib.use('Agg')
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Scarica dati multi-asset
tickers = ["^GSPC", "GC=F", "TLT"]
data = yf.download(tickers, start="2024-01-01", end="2026-01-01")["Close"]

# Calcola rendimenti giornalieri
returns = data.pct_change().dropna()
print(returns.head(10))

# Matrice di correlazione
corr_matrix = returns.corr()
print(corr_matrix)

# Heatmap correlazioni
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
plt.title("Correlation Matrix - S&P500, Gold, Bonds")
plt.tight_layout()
plt.savefig("correlazione.png")