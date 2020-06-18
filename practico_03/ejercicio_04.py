# Implementar la funcion buscar_persona, que devuelve el registro de una persona basado en su id.
# El return es una tupla que contiene sus campos: id, nombre, nacimiento, dni y altura.
# Si no encuentra ningun registro, devuelve False.

import datetime

import mysql.connector

from practico_03.ejercicio_01 import reset_tabla
from practico_03.ejercicio_02 import agregar_persona


def buscar_persona(id_persona):
    connection = mysql.connector.connect(user="root", password="root", host="localhost", database="soportebd")
    cursor = connection.cursor()
    cSQL = "SELECT * FROM PERSONA WHERE IdPersona = %s"
    cursor.execute(cSQL, (id_persona, ))
    results = cursor.fetchall()
    if len(results)>0:
        return results[0]
    else:
        return False


@reset_tabla
def pruebas():
    juan = buscar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert juan == (1, 'juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    assert buscar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
