# Implementar la funcion crear_tabla_peso, que cree una tabla PersonaPeso con:
# - IdPersona: Int() (Clave Foranea Persona)
# - Fecha: Date()
# - Peso: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.

from sqlalchemy import Table, Column, String, Integer, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from ejercicio_01 import borrar_tabla, crear_tabla, conexion, reset_tabla, Persona, sessionUsuario, base
#base = declarative_base()

class PersonaPeso(base):
    __tablename__='PersonaPeso'
    idPersonaPeso = Column(Integer, primary_key=True, nullable=False)
    Fecha = Column(Date)
    Peso = Column(Integer)

def crear_tabla_peso():
    base.metadata.create_all(conexion())
    print('creacion de tabla con exito')

def borrar_tabla_peso():
    PersonaPeso.__table__.drop(conexion())
    print('eliminacion de tabla con exito')

# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        crear_tabla_peso()
        func()
        borrar_tabla_peso()
        borrar_tabla()
    return func_wrapper
