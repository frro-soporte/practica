# Implementar la funcion borrar_persona, que elimina un registro en la tabla Persona.
# Devuelve un booleano en base a si encontro el registro y lo borro o no.

import datetime
import sqlite3

from ejercicio_01 import reset_tabla
from ejercicio_02 import agregar_persona


def borrar_persona(id_persona):
    db = sqlite3.connect('mibase')
    cursor = db.cursor()
    id = (id_persona,)
    cursor.execute('Select idPersona from Persona where IdPersona = ?', id)
    if cursor.fetchall() == []:
        db.close()
        return False
    cursor.execute('Delete from Persona where IdPersona = ?', id)
    db.commit()
    db.close()
    return True


@reset_tabla
def pruebas():
    assert borrar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert borrar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
