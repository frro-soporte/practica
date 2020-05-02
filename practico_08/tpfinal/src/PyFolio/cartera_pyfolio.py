import pandas as pd
import yfinance as yf
import pyfolio as pf

portfolio = ['YPF', 'GGAL', 'AMZN', 'AAPL', 'TLT', 'SHY', 'IEF']
data = pd.DataFrame(columns=portfolio)
data = yf.download(portfolio, period='10y')['Adj Close']
data = data.pct_change().dropna().mean(axis=1)
print(data)
pf.create_full_tear_sheet(data)

