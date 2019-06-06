# Implementar la funcion buscar_persona, que devuelve el registro de una persona basado en su id.
# El return es una tupla que contiene sus campos: id, nombre, nacimiento, dni y altura.
# Si no encuentra ningun registro, devuelve False.

import datetime
import sqlite3

from practico_03.ejercicio_01 import reset_tabla
from practico_03.ejercicio_02 import agregar_persona


def buscar_persona(id_persona):
    conn = sqlite3.connect('tabla.db')
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT * "
                    "FROM tablaPersona "
                    "WHERE idPer =?", (id_persona,))
        pers = cur.fetchone()
        if pers is None:
            return False
        else:
            return pers

@reset_tabla
def pruebas():
    agregar_persona('juan perez', datetime.datetime(1988,5,15), 32165498, 180)
    juan = buscar_persona(1)
    assert juan == (1, 'juan perez',datetime.datetime(1988,5,15).strftime("%Y-%m-%d %H:%M:%S"), 32165498, 180)
    assert buscar_persona(12345) is False


if __name__ == '__main__':
    pruebas()
