# Implementar la funcion borrar_persona, que elimina un registro en la tabla Persona.
# Devuelve un booleano en base a si encontro el registro y lo borro o no.

import datetime

import mysql.connector

from practico_03.ejercicio_01 import reset_tabla
from practico_03.ejercicio_02 import agregar_persona


def borrar_persona(id_persona):
    connection = mysql.connector.connect(user="root", password="root", host="localhost", database="soportebd")
    cursor = connection.cursor()
    cSQL = "DELETE FROM Persona WHERE IdPersona = %s"
    cursor.execute(cSQL, (id_persona, ))
    connection.commit()
    if cursor.rowcount > 0:
        return True
    else:
        return False



@reset_tabla
def pruebas():
    assert borrar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert borrar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
