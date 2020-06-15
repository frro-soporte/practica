import csv
import os
import yfinance as yf

currentdir = os.getcwd()
companies = csv.reader(open('sp500_companies.csv'))

for company in companies:
    print(company)
    symbol, name = company
    history_filename = currentdir + '/history/{}.csv'.format(symbol)
    ticker = yf.Ticker(symbol)
    df = ticker.history(period="1mo")
    cwd = os.path.dirname(history_filename)
    if not os.path.exists(cwd):
        os.makedirs(cwd)
    with open(history_filename, 'w') as f:
        f.write(df.to_csv())
        f.close()
