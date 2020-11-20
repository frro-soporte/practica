import os

from typing import List
from datetime import date

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import pyRofex

from schemas import trade_schema
from models import trade_model
from api import deps
from models import user_model #solo para auth
from api.financeapi.financeapi import get_trade_history

trades_rofex = ["DONov20", "DODic20", "DOEne21", "DOFeb21", "DOMar21"]

router = APIRouter()

#, response_model=List[trade_schema.TradeBaseBase] not working
@router.post("/trade_history/")
def get_trades_history(trade_symbol: str
                        ,current_user: user_model.User = Depends(deps.get_current_user)
                             ):
    """
    Retrieve trade history by trade Symbol (authentication required).
    """
    #agregar exception por si no se conecta a la api de rofex
    if trade_symbol in trades_rofex:
        return get_trade_history(trade_symbol)
    raise HTTPException(status_code=400, detail="Invalid trade symbol") # ver codigo de error en wikipedia.


    #esto para la tabla principal
    #pyRofex.get_market_data(ticker="DODic19",entries=[pyRofex.MarketDataEntry.LAST])
    #esto para los graficos de trades
    #pyRofex.get_trade_history(trade_symbol, "2020-01-01", date.today())
    