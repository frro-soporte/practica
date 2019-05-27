# Implementar la funcion crear_tabla, que cree una tabla Persona con:
# - IdPersona: Int() (autoincremental)
# - Nombre: Char(30)
# - FechaNacimiento: Date()
# - DNI: Int()
# - Altura: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String, DATE
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Persona(Base):
 __tablename__ = 'persona'

 idPersona = Column(Integer, primary_key=True)
 nombre = Column(String(30), nullable=False)
 fechaNacimiento = Column(DATE)
 dni = Column(Integer)
 altura = Column(Integer)

def create_conexion ():
    engine = create_engine('sqlite:///c://Users//Nahuel//Desktop//sqlalchemy_db.db')
    Base.metadata.bind = engine
    DBSession = sessionmaker()
    DBSession.bind = engine
    session = DBSession()


def crear_tabla():
    Base.metadata.create_all()
    pass


def borrar_tabla():
    Base.metadata.drop_all()
    pass


# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        func()
        borrar_tabla()
    return func_wrapper
create_conexion()
crear_tabla()
borrar_tabla()