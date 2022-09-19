# Implementar la funcion borrar_persona, que elimina un registro en la tabla Persona.
# Devuelve un booleano en base a si encontro el registro y lo borro o no.

import datetime
import sqlite3 as db
from practico_03.ejercicio_01 import reset_tabla
from practico_03.ejercicio_02 import agregar_persona


def borrar_persona(id_persona):
    var_db = db.connect('practico-03.db')
    cursor = var_db.cursor()
    query = "DELETE FROM Persona WHERE IdPersona = %s" % id_persona
    cursor.execute(query)
    var_db.commit()
    return False if cursor.rowcount == 0 else True



@reset_tabla
def pruebas():
    assert borrar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert borrar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
