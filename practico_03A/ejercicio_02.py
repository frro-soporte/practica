# Implementar la funcion agregar_persona, que inserte un registro en la tabla Persona
# y devuelva los datos ingresados el id del nuevo registro.

import datetime

from practico_03A.ejercicio_01 import reset_tabla, Persona
import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()  # Metadatos

def agregar_persona(nombre, nacimiento, dni, altura,session):
    oper = Persona()
    oper.nombre = nombre
    oper.fecha_nac = nacimiento
    oper.dni = dni
    oper.altura = altura
    session.add(oper)
    session.commit()
    return oper.id_persona


@reset_tabla
def pruebas(session):
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180,session)
    id_marcela = agregar_persona('marcela gonzalez', datetime.datetime(1980, 1, 25), 12164492, 195,session)
    print(id_juan, id_marcela)
    assert id_juan > 0
    assert id_marcela > id_juan

if __name__ == '__main__':

    pruebas()
