# Implementar la funcion borrar_persona, que elimina un registro en la tabla Persona.
# Devuelve un booleano en base a si encontro el registro y lo borro o no.

import datetime
import sqlite3
from ejercicio_01 import reset_tabla
from ejercicio_02 import agregar_persona

db = sqlite3.connect('D:\\prueba.db')
cur = db.cursor()


def borrar_persona(id_persona):
    cSQL = 'select idPersona from Persona where idPersona=?'
    id =(id_persona,)
    cur.execute(cSQL,id)
    res = cur.fetchone()
    if res is not None:  
        cSQL = 'delete from Persona where idPersona=?'
        cur.execute(cSQL,(id_persona,))
        db.commit()
        return True
    else:
        return False

@reset_tabla
def pruebas():
    assert borrar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert borrar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
