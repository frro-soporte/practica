# Implementar la funcion buscar_persona, que devuelve el registro de una persona basado en su id.
# El return es una tupla que contiene sus campos: id, nombre, nacimiento, dni y altura.
# Si no encuentra ningun registro, devuelve False.

import sqlite3
import datetime

from practico_03.ejercicio_01 import reset_tabla
from practico_03.ejercicio_02 import agregar_persona


def buscar_persona(id_persona):
    db = sqlite3.connect('mibase')
    cur = db.cursor()

    cur.execute('SELECT id_persona FROM Persona')
    ids = cur.fetchall()
    if(id_persona,) in ids:
        cur.execute('SELECT * FROM Persona WHERE id_persona=?', (id_persona,))
        enc = cur.fetchone()
        cur.close()
        db.commit()
        db.close()
        return enc

    return False


@reset_tabla
def pruebas():
    juan = buscar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert juan == (1, 'juan perez', '1988-05-15 00:00:00', 32165498, 180)
    assert buscar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
