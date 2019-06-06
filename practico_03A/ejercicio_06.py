# Implementar la funcion crear_tabla_peso, que cree una tabla PersonaPeso con:
# - IdPersona: Int() (Clave Foranea Persona)
# - Fecha: Date()
# - Peso: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.

import datetime
from ejercicio_01 import Persona
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import Column, ForeignKey, Integer, String, Date, DateTime, create_engine
from ejercicio_01 import borrar_tabla, crear_tabla

Base = declarative_base()  # Metadatos

class Peso(Base):
    __tablename__ = 'peso'
    per = relationship(Persona)
    idPes = Column(Integer, primary_key=True,autoincrement=True)
    fec = Column(Date, nullable=False)
    pes = Column(Integer, nullable=False)
    idPer = Column(Integer, ForeignKey(Persona.idPer))

    def __init__(self,nacimiento, peso):
        self.pes = peso
        self.fec = nacimiento

def crear_tabla_peso(engine):
    Base.metadata.create_all(engine)

def borrar_tabla_peso():
    Peso.__table__.drop()

def reset_tabla(func):
    def func_wrapper():
        engine = create_engine('sqlite:///tabla.db')
        Base.metadata.bind = engine
        DBSession = sessionmaker(bind= engine)
        session = DBSession()
        crear_tabla()
        crear_tabla_peso(engine)
        func(session)
        borrar_tabla_peso()
        borrar_tabla()
    return func_wrapper
