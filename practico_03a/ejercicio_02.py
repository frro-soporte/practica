# Implementar la funcion agregar_persona, que inserte un registro en la tabla Persona
# y devuelva los datos ingresados el id del nuevo registro.

import datetime
#import mysql.connector

from ejercicio_01 import conexion, reset_tabla, Persona, sessionUsuario
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import exc

Base = declarative_base()

def agregar_persona(nombre, nacimiento, dni, altura):
    try:
        conexion()
        per = Persona()
        per.nombre = nombre
        per.fechaNacimiento = nacimiento
        per.dni = dni
        per.altura = altura
        sessionUser = sessionUsuario()
        sessionUser.add(per)
        sessionUser.commit()
        id = (sessionUser.query(Persona).filter(Persona.dni == dni).first()).idPersona
        print('persona insertada con exito')
        return id

    except exc.SQLAlchemyError:
        print(exc.SQLAlchemyError.args)
        return -1

    #print("El id es {0}, el nombre {1}, la fecha de nacimiento {2}, el nro dni {3} y la altura es {4}".format(id, nombre, nacimiento, dni, altura))
    #return id

@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    id_marcela = agregar_persona('marcela gonzalez', datetime.datetime(1980, 1, 25), 12164492, 195)
    assert id_juan > 0
    assert id_marcela > id_juan
