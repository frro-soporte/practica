# Implementar la funcion crear_tabla_peso, que cree una tabla PersonaPeso con:
# - IdPersona: Int() (Clave Foranea Persona)
# - Fecha: Date()
# - Peso: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.
from sqlalchemy import Column, ForeignKey, Integer,Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///c://Users//Nahuel//Desktop//sqlalchemy_db.db')
Base.metadata.bind = engine
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()


from practico_03_alchemy.ejercicio_01 import borrar_tabla, crear_tabla, Persona

class PersonaPeso(Base):
    __tablename__ = 'personaPeso'
    id = Column(Integer, primary_key=True, autoincrement=True)
    idPersona = Column(Integer, ForeignKey(Persona.idPersona))
    fecha = Column(Date, nullable=False)
    peso = Column(Integer, nullable=False)

def crear_tabla_peso():
    Base.metadata.create_all(engine)
    pass


def borrar_tabla_peso():
    Base.metadata.drop_all(engine)
    pass


# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        crear_tabla_peso()
        func()
        borrar_tabla_peso()
        borrar_tabla()
    return func_wrapper


crear_tabla()
crear_tabla_peso()
borrar_tabla_peso()
borrar_tabla()