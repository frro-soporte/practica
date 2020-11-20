from typing import List, Optional

from pydantic import BaseModel

class UserBase(BaseModel):
    email: str
    name: Optional[str] = None
    lastname: Optional[str] = None

#Esto para crear
class UserCreate(UserBase):
    hashed_password: str

#Esto para leer (devolver desde la API), por eso no tiene pass
class User(UserBase):
    id: int

    #config de Pydantic
    class Config:
        orm_mode = True