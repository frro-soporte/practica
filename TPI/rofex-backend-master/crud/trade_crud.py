from sqlalchemy.orm import Session

from models import trade_model
from schemas import trade_schema

#READ
def get_trade(db:Session, trade_id: int):
    return db.query(trade_model.Trade).filter(trade_model.Trade.idtrade == trade_id).first()

def get_trades(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return db.query(trade_model.Trade).filter(trade_model.Trade.iduser == user_id).limit(limit).all()

#CREATE
def create_trade(db: Session, trade: trade_schema.TradeBase):
    db_trade = trade_model.Trade(symbol=trade.symbol, size=trade.size, price=trade.price, datetime=trade.datetime, iduser=trade.iduser)
    db.add(db_trade)
    db.commit()
    db.refresh(db_trade)
    return db_trade
