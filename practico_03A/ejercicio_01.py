# Implementar la funcion crear_tabla, que cree una tabla Persona con:
# - IdPersona: Int() (autoincremental)
# - Nombre: Char(30)
# - FechaNacimiento: Date()
# - DNI: Int()
# - Altura: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.engine import create_engine
Base = declarative_base()
engine = create_engine('mysql+pymysql://root:852456@localhost:3306/pythonalchemy')
Base.metadata.bind = engine


class Persona(Base):
    __tablename__ = 'persona'
    IdPersona = Column(Integer, primary_key=True, autoincrement=True)
    Nombre = Column(String(30), nullable=False)
    FechaNacimiento = Column(Date, nullable=False)
    DNI = Column(Integer, nullable=False)
    Altura = Column(Integer, nullable=False)
    
    def __init__(self,nombre, nacimiento, dni, altura):
        self.Nombre = nombre
        self.FechaNacimiento=nacimiento
        self.DNI=dni
        self.Altura= altura


def crear_tabla():
    Base.metadata.create_all(engine)


def borrar_tabla():
    Persona.__table__.drop(engine)


def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        func()
        borrar_tabla()
    return func_wrapper
