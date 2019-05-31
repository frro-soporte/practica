# Implementar la funcion buscar_persona, que devuelve el registro de una persona basado en su id.
# El return es una tupla que contiene sus campos: id, nombre, nacimiento, dni y altura.
# Si no encuentra ningun registro, devuelve False.

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///c://Users//Nahuel//Desktop//sqlalchemy_db.db')
Base.metadata.bind = engine
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

import datetime

from practico_03_alchemy.ejercicio_01 import reset_tabla, Persona
from practico_03_alchemy.ejercicio_02 import agregar_persona


def buscar_persona(id_persona):
    res = session.query(Persona).filter(Persona.idPersona == id_persona).first()

    if res is not None:
        per = Persona()
        per.idPersona = res.idPersona
        per.nombre = res.nombre
        per.dni = res.dni
        per.fechaNacimiento = res.fechaNacimiento
        per.altura = res.altura
        tup = tuple()

        tup = (per.idPersona,per.nombre,per.fechaNacimiento,per.dni, per.altura)

        return tup
    else:
        return False



@reset_tabla
def pruebas():
    juan = buscar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert juan == (1, 'juan perez', datetime.date(1988, 5, 15), 32165498, 180)
    assert buscar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
