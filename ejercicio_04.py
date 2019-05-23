# Implementar la funcion buscar_persona, que devuelve el registro de una persona basado en su id.
# El return es una tupla que contiene sus campos: id, nombre, nacimiento, dni y altura.
# Si no encuentra ningun registro, devuelve False.

import datetime
import sqlite3
from ejercicio_01 import reset_tabla
from ejercicio_02 import agregar_persona

db = sqlite3.connect('D:\\prueba.db')
cur = db.cursor()

def buscar_persona(id_persona):
    cSQL = 'select idPersona,nombre,fechaNacimiento,dni,altura from Persona where idPersona=?'
    id = (id_persona,)
    cur.execute(cSQL,id)
    per = cur.fetchone()
    if per is not None:
        return per
    else:
        return False




@reset_tabla
def pruebas():
    juan = buscar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert juan == (1, 'juan perez','1988-05-15 00:00:00', 32165498, 180.0)
    assert buscar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
