# Implementar la funcion crear_tabla_peso, que cree una tabla PersonaPeso con:
# - IdPersona: Int() (Clave Foranea Persona)
# - Fecha: Date()
# - Peso: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.

import datetime
from practico_03A.ejercicio_01 import Persona
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, Integer, String, Date, DateTime
from practico_03A.ejercicio_01 import borrar_tabla, crear_tabla
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()  # Metadatos


class Peso(Base):
    __tablename__ = 'peso'  # ----nombre de la tabla
    # Definimos las columnas de la tabla Persona
    id_peso = Column(Integer, primary_key=True)
    fecha_peso = Column(DateTime, nullable=False)
    peso = Column(Integer, nullable=False)
    persona_id = Column(Integer, ForeignKey('persona.id'))
    persona = relationship(Persona)

def crear_tabla_peso(engine):
    Base.metadata.create_all(engine)


def borrar_tabla_peso():
    Peso.__table__.drop()


engine = create_engine('sqlite:///personadb_alquemy.db')
Base.metadata.bind = engine
        # ---- creamos una sesión para admin datos
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla(engine)
        crear_tabla_peso(engine)
        func()
        borrar_tabla_peso()
        borrar_tabla()
    return func_wrapper
