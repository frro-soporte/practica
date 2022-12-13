import pyRofex
from datetime import date
from typing import List, Union, Dict

import pandas as pd

user = "dbdamix3901" #os.environ["user"]
password = "melulI3)"
account = "REM3901"
        
pyRofex.initialize(user=user, password=password, account=account, environment=pyRofex.Environment.REMARKET)

def get_trade_history(trade_symbol: str): 
    resp = pyRofex.get_trade_history(trade_symbol, "2020-01-01", date.today())
    df = pd.DataFrame(resp["trades"]) 
    del_columns = ["symbol", "servertime", "size"]
    df.drop(del_columns, inplace=True, axis=1)
    di = df.to_json(orient='records')
    return di