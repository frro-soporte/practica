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

class Persona(Base):
 __tablename__ = 'persona' # ----nombre de la tabla
 # Definimos las columnas de la tabla Persona
 id_persona = Column(Integer, primary_key=True)
 nombre = Column(String(30), nullable=False)
 fecha_nac = Column(DateTime, nullable=False)
 dni = Column(Integer, nullable=False)
 altura = Column(Integer, nullable=False)

class Peso(Base):
    __tablename__ = 'peso'  # ----nombre de la tabla
    # Definimos las columnas de la tabla Persona
    id_peso = Column(Integer, primary_key=True)
    fecha_peso = Column(DateTime, nullable=False)
    peso = Column(Integer, nullable=False)
    persona_id = Column(Integer, ForeignKey('persona.id_persona'))
    persona = relationship('Persona',lazy='subquery')

def crear_tabla_peso(engine):
    Base.metadata.create_all(engine)


def borrar_tabla_peso():
    Peso.__table__.drop()




# no modificar
def reset_tabla(func):
    def func_wrapper():
        engine = create_engine('sqlite:///personadb_alquemy.db')
        Base.metadata.bind = engine
        # ---- creamos una sesión para admin datos
        DBSession = sessionmaker(bind= engine)
        session = DBSession()
        crear_tabla(engine)
        crear_tabla_peso(engine)
        func(session)
        borrar_tabla_peso()
        borrar_tabla(Persona)
    return func_wrapper
