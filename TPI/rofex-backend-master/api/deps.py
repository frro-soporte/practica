from typing import Generator

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from passlib.context import CryptContext
from pydantic import ValidationError
from sqlalchemy.orm import Session

from database.database import SessionLocal, engine
from models import user_model
from schemas import user_schema, token_schema
from crud import user_crud
from core import security

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

#start database
user_model.Base.metadata.create_all(bind=engine)

def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
 

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(
            token, security.SECRET_KEY, algorithms=[security.ALGORITHM]
            )
        id_user: int = payload.get("sub")
        if id_user is None:
            raise credentials_exception
        token_data = token_schema.TokenPayload(**payload)
    except jwt.JWTError:
        raise credentials_exception
    user = user_crud.get_user(db, user_id=token_data.sub)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user