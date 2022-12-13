from typing import List, Optional
from datetime import datetime

from pydantic import BaseModel

#ARREGLAR ESTO PLIS testing

class TradeBaseBase(BaseModel):
    symbol: str
    size: float
    price: float
    datetime: datetime

class TradeBase(BaseModel):
    symbol: str
    size: float
    price: float
    datetime: datetime
    iduser: int 
    
    class Config:
        orm_mode = True

class Trade(TradeBase):
    idtrade: int
    class Config:
        orm_mode = True

