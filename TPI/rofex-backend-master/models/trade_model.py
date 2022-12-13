from sqlalchemy import Boolean, Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from database.database import Base

class Trade(Base):
    __tablename__ = "trades"

    idtrade                = Column(Integer, primary_key=True, index=True)
    symbol                  = Column(String, index=True)
    size                    = Column(Float, index=True)
    price                   = Column(Float, index=True, unique=True)
    datetime                = Column(DateTime, index=True)
    iduser                  = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="trade")


