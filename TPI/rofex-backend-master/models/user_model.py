from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from database.database import Base
from models import trade_model

class User(Base):
    __tablename__ = "users"

    id                  = Column(Integer, primary_key=True, index=True)
    name                = Column(String, index=True)
    lastname            = Column(String, index=True)
    email               = Column(String, index=True, unique=True)
    hashed_password     = Column(String, index=True)

    trade = relationship("Trade", back_populates="user")





