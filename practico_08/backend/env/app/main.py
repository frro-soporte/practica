# ~/movie_service/app/main.py

import yfinance as yf
import csv
import json
import pandas as pd
from collections import OrderedDict
from fastapi import FastAPI
from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException


app = FastAPI()

@app.get('/info')
async def info(stock: str = 'AAPL'):
    try:
        ticker = yf.Ticker(stock)
        return ticker.info
    except ValueError:
        return HTTPException(status_code=502, detail="Bad Gateway")

@app.get('/historic/')
async def historic(stock: str = 'AAPL', range: str = '1mo'):
    # TODO: i have to fix the problem with range=1d
    """

    Args:
        stock (str, optional): [description]. Defaults to 'GOOG'.
        range (str, optional): [description]. Defaults to '1d'.
            Valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
    Returns:
        [type]: [description]
    """
    ticker = yf.Ticker(stock)
    hist_df = ticker.history(range)
    out = hist_df.to_json(orient='index', date_format='iso')
    # ‘split’, ‘records’, ‘index’, ‘columns’, ‘values’, ‘table’, default=’index'
    return json.loads(out)



# SPY PATTERN SECTION

def is_bullish_candlestick(candle):
    return float(candle['Close']) < float(candle['Open'])

def is_bearish_candlestick(candle):
    return float(candle['Close']) > float(candle['Open'])

def is_bullish_engulfing(candles, index):
    current_day = candles[index]
    previous_day = candles[index - 1]
    if is_bearish_candlestick(previous_day) \
            and float(current_day['Close']) > float(previous_day['Open']) \
            and float(current_day['Open']) < float(previous_day['Close']):
        return True
    return False

def is_bearish_engulfing(candles, index):
    current_day = candles[index]
    previous_day = candles[index - 1]

    if is_bearish_candlestick(previous_day) \
            and current_day['Open'] > previous_day['Close'] \
            and current_day['Close'] < \
            previous_day['Open']:
        return True
    return False

# SPY PATTERN Endpoint
@app.get('/spy_pattern')
async def spy_pattern(stock: str = 'AAPL', range: str = '1mo'):
    """
    Args:
        stock (str, optional): [description]. Defaults to 'GOOG'.
        range (str, optional): [description]. Defaults to '1d'.
            Valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
        """
    ticker = yf.Ticker(stock)
    df = ticker.history(period=range)
    candles = df.to_dict(into=OrderedDict, orient='records')
    candles = candles[-2:]
    print(candles)
    if len(candles) > 1:
        if is_bullish_engulfing(candles, 1):
            return(
                "{} - {} is bullish engulfing ".format(ticker, candles.index))
        else:
            if is_bearish_engulfing(candles, 1):
                return(
                    "{} - {} is bearish engulfing ".format(ticker, candles.index ))
            else:
                return("{} no pattern ".format(ticker))
