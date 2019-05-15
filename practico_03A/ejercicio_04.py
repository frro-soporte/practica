# Implementar la funcion buscar_persona, que devuelve el registro de una persona basado en su id.
# El return es una tupla que contiene sus campos: id, nombre, nacimiento, dni y altura.
# Si no encuentra ningun registro, devuelve False.

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ejercicio_01 import Persona,reset_tabla
from ejercicio_02 import agregar_persona
import datetime

Base = declarative_base()
engine = create_engine('mysql://root:852456ale@localhost:3306/python')
Base.metadata.bind = engine
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()


def buscar_persona(id_persona):
    obj=session.query(Persona).filter(Persona.IdPersona==id_persona).first()

    session.commit()
    if obj is None:
     return False
    else:
     return obj 
#Para que el assert de return (obj.IdPersona,obj.Nombre,obj.FechaNacimiento,obj.DNI,obj.Altura)


@reset_tabla

def pruebas():
    juan = buscar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert juan == (1, 'juan perez', datetime.date(1988, 5, 15), 32165498, 180)
    assert buscar_persona(12345) is False


if __name__ == '__main__':
    pruebas()
