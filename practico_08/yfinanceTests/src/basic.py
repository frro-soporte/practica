import yfinance as yf
import json
ticker = yf.Ticker('GOOG')
print(json.dumps(ticker.info, indent=4, sort_keys=True))