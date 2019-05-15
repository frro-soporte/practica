# Implementar la funcion crear_tabla_peso, que cree una tabla PersonaPeso con:
# - IdPersona: Int() (Clave Foranea Persona)
# - Fecha: Date()
# - Peso: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String , Date,ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,relationship
from ejercicio_01.py import borrar_tabla,crear_tabla,Persona



import datetime

Base = declarative_base()
engine = create_engine('mysql://root:852456ale@localhost:3306/python')
Base.metadata.bind = engine
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

class PersonaPeso:
     __tablename__ = 'personapeso'
    persona = relationship(Persona)
    idpeso=Column(Integer,primary_key=True,autoincrement=True)
    IdPersona = Column(Integer,ForeignKey(Persona.IdPersona))
    Fecha = Column(Date, nullable=False)
    Peso= Column(Integer, nullable=False)


    def __init__(self,nacimiento, peso):
        self.Peso = peso
        self.FechaNacimiento=nacimiento


def crear_tabla_peso():
   Base.metadata.create_all(engine)
def borrar_tabla_peso():
   PersonaPeso.__table__.drop(engine)
   
   
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        crear_tabla_peso()
        func()
        borrar_tabla_peso()
        borrar_tabla()
    return func_wrapper
