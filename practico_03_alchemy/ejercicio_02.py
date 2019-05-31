# Implementar la funcion agregar_persona, que inserte un registro en la tabla Persona
# y devuelva los datos ingresados el id del nuevo registro.

import datetime


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from practico_03_alchemy.ejercicio_01 import reset_tabla
from practico_03_alchemy.ejercicio_01 import Persona

Base = declarative_base()
engine = create_engine('sqlite:///c://Users//Nahuel//Desktop//sqlalchemy_db.db')
Base.metadata.bind = engine
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

def agregar_persona(nombre, nacimiento, dni, altura):
    op = Persona()
    op.nombre = nombre
    op.fechaNacimiento = nacimiento
    op.dni = dni
    op.altura = altura

    session.add(op)

    session.commit()
    return op.idPersona


@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    id_marcela = agregar_persona('marcela gonzalez', datetime.datetime(1980, 1, 25), 12164492, 195)
    assert id_juan > 0
    assert id_marcela > id_juan

if __name__ == '__main__':
    pruebas()
