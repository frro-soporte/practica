# Implementar la funcion crear_tabla, que cree una tabla Persona con:
# - IdPersona: Int() (autoincremental)
# - Nombre: Char(30)
# - FechaNacimiento: Date()
# - DNI: Int()
# - Altura: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Persona(Base):
    __tablename__ = 'Persona'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(30), nullable=False)
    fechaNacimiento = Column(Date, nullable=False)
    dni = Column(Integer, nullable=False)
    altura = Column(Integer, nullable=False)


engine = create_engine('sqlite:///sqlalchemy_TP3A.db') #lo crea donde se encuentra el archivo .py
Base.metadata.bind = engine

DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

def crear_tabla():
    Base.metadata.create_all(engine)


def borrar_tabla():
    Persona.__table__.drop(engine)

crear_tabla()
borrar_tabla()

# no modificar
"""
 def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        func()
        borrar_tabla()
    return func_wrapper""" 
        #dijo Fran que no va en este TP
