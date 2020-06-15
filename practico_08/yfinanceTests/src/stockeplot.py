# python_candlestick_chart.py

import matplotlib.pyplot as plt
from mpl_finance import candlestick_ohlc
import pandas as pd
import matplotlib.dates as mpl_dates
import os 

currentDir = os.getcwd()
plt.style.use('ggplot')

# Extracting Data for plotting
data = pd.read_csv(currentDir+'/history/DISCK.csv')
ohlc = data.loc[:, ['Date', 'Open', 'High', 'Low', 'Close']]
ohlc['Date'] = pd.to_datetime(ohlc['Date'])
ohlc['Date'] = ohlc['Date'].apply(mpl_dates.date2num)
ohlc = ohlc.astype(float)
ohlc['MA_9'] = ohlc.Close.rolling(9).mean()
ohlc['MA_21'] = ohlc.Close.rolling(21).mean()
# Creating Subplots
fig, ax = plt.subplots()
am = plt.subplots()

candlestick_ohlc(ax, ohlc.values, width=0.6, colorup='green', colordown='red', alpha=0.8)

# Setting labels & titles
ax.set_xlabel('Date')
ax.set_ylabel('Price')
plt.plot(ohlc['MA_9'], label="MA 9 day")
plt.plot(ohlc['MA_21'], label="MA 21 day")
fig.suptitle('Daily Candlestick Chart of DISCK')

# Formatting Date
date_format = mpl_dates.DateFormatter('%d-%m-%Y')
ax.xaxis.set_major_formatter(date_format)
fig.autofmt_xdate()


plt.show()

