from sqlalchemy.orm import Session

from models import user_model
from schemas import user_schema
from core.security import get_password_hash, verify_password


#READ
def get_user(db: Session, user_id: int):
    return db.query(user_model.User).filter(user_model.User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(user_model.User).offset(skip).limit(limit).all()

def get_by_email(db: Session, email: str):
    return db.query(user_model.User).filter(user_model.User.email == email).first()

#CREATE
def create_user(db: Session, user: user_schema.UserCreate):
    hashed_pass = get_password_hash(user.hashed_password)
    db_user = user_model.User(email=user.email, hashed_password=hashed_pass, name=user.name, lastname=user.lastname)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


#auth for login
def authenticate(db: Session, email: str, password: str):
        user = get_by_email(db, email=email)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user