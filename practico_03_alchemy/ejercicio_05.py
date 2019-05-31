# Implementar la funcion actualizar_persona, que actualiza un registro de una persona basado en su id.
# Devuelve un booleano en base a si encontro el registro y lo actualizo o no.

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, update
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
from practico_03_alchemy.ejercicio_04 import buscar_persona


def actualizar_persona(id_persona, nombre, nacimiento, dni, altura):
    res = buscar_persona(id_persona)

    if res != False:
        query = session.query(Persona).filter(Persona.idPersona == id_persona).first()

        query.nombre = nombre
        query.fechaNacimiento = nacimiento
        query.dni = dni
        query.altura = altura

        session.commit()
        return True
    else:

        return False




@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    actualizar_persona(id_juan, 'juan carlos perez', datetime.datetime(1988, 4, 16), 32165497, 181)
    assert buscar_persona(id_juan) == (1, 'juan carlos perez', datetime.date(1988, 4, 16), 32165497, 181)
    assert actualizar_persona(123, 'nadie', datetime.datetime(1988, 4, 16), 12312312, 181) is False

if __name__ == '__main__':
    pruebas()
