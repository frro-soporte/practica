# Implementar la funcion agregar_persona, que inserte un registro en la tabla Persona
# y devuelva los datos ingresados el id del nuevo registro.

import datetime

from practico_03.ejercicio_01 import reset_tabla
#from ejercicio_01 import reset_tabla

import sqlite3



def agregar_persona(nombre, nacimiento, dni, altura):
    db = sqlite3.connect('persona_db.sqlite')

    cursor = db.cursor()
    cSQL = 'INSERT INTO persona (nombre, fecha_nacimiento, dni, altura)' \
           'VALUES (?,?,?,?)'
    tdatos = (nombre, nacimiento, dni, altura)
    cursor.execute(cSQL, tdatos)
    id = cursor.lastrowid
    db.commit()
    return id


@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    id_marcela = agregar_persona('marcela gonzalez', datetime.datetime(1980, 1, 25), 12164492, 195)
    assert id_juan > 0
    assert id_marcela > id_juan

if __name__ == '__main__':
    db = sqlite3.connect('persona_db.sqlite')

    pruebas()
