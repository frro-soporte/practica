from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from crud import trade_crud
from models import trade_model
from schemas import  trade_schema
from api import deps
from models import user_model #solo para auth


router = APIRouter()

@router.post("/trade/", response_model=trade_schema.Trade)
def get_trade(  trade_id: int,
                db: Session = Depends(deps.get_db),
                current_user: user_model.User = Depends(deps.get_current_user)):
    """
    Retrieve trade by trade ID (authentication required).
    """
    trade = trade_crud.get_trade(db=db, trade_id=trade_id)
    return trade

@router.post("/trades/", response_model=List[trade_schema.Trade])
def get_trades( user_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(deps.get_db),
                current_user: user_model.User = Depends(deps.get_current_user)):
    """
    Retrieve all the trades of a user by user ID (authentication required).
    """
    trades = trade_crud.get_trades(user_id=user_id, db=db, skip=skip, limit=limit)
    return trades

@router.post("/create-trade/", response_model=trade_schema.Trade)
def create_trade(trade: trade_schema.TradeBase, db: Session = Depends(deps.get_db), 
                current_user: user_model.User = Depends(deps.get_current_user)):
    """
    Creates a new trade (authentication required).
    """
    return trade_crud.create_trade(db=db, trade=trade)

