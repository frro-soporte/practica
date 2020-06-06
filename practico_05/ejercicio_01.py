# Implementar un modelo Socio a traves de Alchemy que cuente con los siguientes campos:
# - id_socio: entero (clave primaria, auto-incremental, unico)
# - dni: entero (unico)
# - nombre: string (longitud 250)
# - apellido: string (longitud 250)

from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as db

Base = declarative_base()


class Socio(Base):
    __tablename__ = 'socios'

    id = db.Column('id_socio', db.Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    dni = db.Column('dni', db.Integer, unique=True, nullable=False)
    nombre = db.Column('nombre', db.String(250), nullable=False)
    apellido = db.Column('apellido', db.String(250), nullable=False)