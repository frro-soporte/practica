


# 1. Set Up enviroment
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf



# 2. Get data from yahoo.finance
ticker = yf.Ticker('GOOG')
gld = ticker.history(period="1y")
gld.head()


# 3. Disacar unneeded Data

gld_close = pd.DataFrame(gld.Close)


# 4. Use rolling method to compute moving averages
gld_close['MA_9'] = gld_close.Close.rolling(9).mean()
gld_close['MA_21'] = gld_close.Close.rolling(21).mean()


# 5. Plot data and moving averages

plt.figure(figsize=(15, 10))
plt.grid(True)
plt.plot(gld_close['Close'], label='GLD')
plt.plot(gld_close['MA_9'], label="MA 9 day")
plt.plot(gld_close['MA_21'], label="MA 21 day")
plt.legend(loc=2)
plt.show()
