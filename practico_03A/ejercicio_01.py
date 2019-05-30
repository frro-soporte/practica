# Implementar la funcion crear_tabla, que cree una tabla Persona con:
# - IdPersona: Int() (autoincremental)
# - Nombre: Char(30)
# - FechaNacimiento: Date()
# - DNI: Int()
# - Altura: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Date, Integer, ForeignKey, String, Table
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

engine = create_engine('sqlite:///tabla.db', echo=True)
Base.metadata.bind = engine


class Persona(Base):
    __tablename__ = 'tablaPersona'
    idPer = Column(Integer, primary_key=True, autoincrement=True)
    nom = Column(String(30), nullable=False)
    fec = Column(Date, nullable=False)
    dni = Column(Integer, nullable=False)
    alt = Column(Integer, nullable=False)

    def __init__(self,nombre, nacimiento, dni, altura):
        self.nom = nombre
        self.fec =nacimiento
        self.dni =dni
        self.alt = altura


def crear_tabla():
    Base.metadata.create_all(engine)


def borrar_tabla():
    Persona.__table__.drop(engine)


def reset_tabla(func):
    def func_wrapper():
        DBSession = sessionmaker()
        DBSession.bind = engine
        session = DBSession()
        crear_tabla()
        func(session)
        borrar_tabla()
    return func_wrapper
