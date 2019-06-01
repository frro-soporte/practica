# Implementar la funcion crear_tabla, que cree una tabla Persona con:
# - IdPersona: Int() (autoincremental)
# - Nombre: Char(30)
# - FechaNacimiento: Date()
# - DNI: Int()
# - Altura: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, String, Date, Integer, ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker

base = declarative_base()

def conexion():
    engine = create_engine('sqlite:///database.db', echo = True)
    return engine

def retornarBase():
    return base

def sessionUsuario():
    base.metadata.bind = conexion()
    DBSession = sessionmaker()
    DBSession.bind = conexion()
    session = DBSession()
    return  session

class Persona(base):
    __tablename__='Persona'
    idPersona = Column(Integer, primary_key=True)
    nombre = Column(String(30))
    fechaNacimiento = Column(Date)
    dni = Column(Integer)
    altura = Column(Integer)

def crear_tabla():
    base.metadata.create_all(conexion())
    print('creacion de tabla con exito')

def borrar_tabla():
    Persona.__table__.drop(conexion())
    print('eliminacion de tabla con exito')

# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        func()
        borrar_tabla()
    return func_wrapper
