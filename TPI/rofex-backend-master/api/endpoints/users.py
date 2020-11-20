from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from crud import user_crud
from models import user_model
from schemas import  user_schema
from api import deps


router = APIRouter()

@router.post("/users/", response_model=user_schema.User)
def create_user(user: user_schema.UserCreate, db: Session = Depends(deps.get_db)):
    """
    Create new user.
    """
    db_user = user_crud.get_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return user_crud.create_user(db=db, user=user)

@router.get("/users/me", response_model=user_schema.User)
def get_me(db: Session = Depends(deps.get_db),
                current_user: user_model.User = Depends(deps.get_current_user)):
    """
    Get current user.
    """
    return current_user


#@router.get("/users/", response_model=List[user_schema.User])
# def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(deps.get_db)):
#     """
#     Retrieve all the users.
#     """
#     return user_crud.get_users(db, skip=skip, limit=limit)