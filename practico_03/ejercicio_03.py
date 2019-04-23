# Implementar la funcion borrar_persona, que elimina un registro en la tabla Persona.
# Devuelve un booleano en base a si encontro el registro y lo borro o no.

import datetime
import  sqlite3
from practico_03.ejercicio_01 import reset_tabla
from practico_03.ejercicio_02 import agregar_persona

conn = sqlite3.connect('tabla.db')
cur = conn.cursor()


def borrar_persona(id_persona):
    cur.execute("SELECT idPersona from tablaPersona where idPersona=?", (id_persona,))
    conn.commit()
    a = cur.fetchone()
    if a is None:
        return False
    else:
        cur.execute("DELETE from tablaPersona where idPersona =?", (id_persona,))
        conn.commit()
        return True



@reset_tabla
def pruebas():
    agregar_persona('juan perez', '05/12/88', 32165498, 180)
    assert borrar_persona()
    assert borrar_persona(12345) is False

if __name__ == 'main':
    pruebas()
