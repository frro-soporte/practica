# Implementar un modelo Socio a traves de Alchemy que cuente con los siguientes campos:
# - id_socio: entero (clave primaria, auto-incremental, unico)
# - dni: entero (unico)
# - nombre: string (longitud 250)
# - apellido: string (longitud 250)

import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String, Date, DateTime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Socio(Base):
    __tablename__ = 'socios'

    id = Column(Integer, primary_key=True, autoincrement=True)
    dni = Column(Integer, nullable=False, unique=True)
    nombre = Column(String(250), nullable=False)
    apellido = Column(String(250), nullable=False)

    def borrar_tabla(Socio):
     # Crea todas las tablas definidas en los metadatos
     Socio.__table__.drop()