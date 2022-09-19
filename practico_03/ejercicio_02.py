# Implementar la funcion agregar_persona, que inserte un registro en la tabla Persona
# y devuelva los datos ingresados el id del nuevo registro.

import datetime
import sqlite3 as db
from practico_03.ejercicio_01 import reset_tabla


def agregar_persona(nombre, nacimiento, dni, altura):
    db_var = db.connect('practico-03.db')
    cursor = db_var.cursor()
    sql = 'Insert into Persona(nombre, FechaNacimiento, DNI, Altura) values(?,?,?,?)'
    query_data = (nombre, nacimiento, dni, altura)
    cursor.execute(sql, query_data)
    db_var.commit()
    id_registro = cursor.lastrowid
    db_var.close()
    return id_registro


@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    id_marcela = agregar_persona('marcela gonzalez', datetime.datetime(1980, 1, 25), 12164492, 195)
    assert id_juan > 0
    assert id_marcela > id_juan

if __name__ == '__main__':
    pruebas()
