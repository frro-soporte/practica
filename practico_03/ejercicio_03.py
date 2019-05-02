# Implementar la funcion borrar_persona, que elimina un registro en la tabla Persona.
# Devuelve un booleano en base a si encontro el registro y lo borro o no.

import sqlite3
import datetime
from ejercicio_02 import agregar_persona
from ejercicio_01 import reset_tabla
conn = sqlite3.connect('tabla.db')
cur = conn.cursor()


def borrar_persona(id_persona):
    conn = sqlite3.connect('tabla.db')
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT idPer "
                    "FROM tablaPersona "
                    "WHERE idPer =?", (id_persona,))
        conn.commit()
        var = cur.fetchone()
        if var is None:
            return False
        else:
            cur.execute("DELETE "
                        "FROM tablaPersona "
                        "WHERE idPer =?", (id_persona,))
            conn.commit()
            return True
        return False


@reset_tabla
def pruebas():
    assert borrar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert borrar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
