# Implementar la funcion actualizar_persona, que actualiza un registro de una persona basado en su id.
# Devuelve un booleano en base a si encontro el registro y lo actualizo o no.

import datetime
import sqlite3
from ejercicio_01 import reset_tabla
from ejercicio_02 import agregar_persona
from ejercicio_04 import buscar_persona

db = sqlite3.connect('D:\\prueba.db')
cur = db.cursor()

def actualizar_persona(id_persona, nombre, nacimiento, dni, altura):
    res = buscar_persona(id_persona)
    print("esto es res: ",res)
    if res is not False:
        cSQL = "UPDATE Persona SET nombre=?,fechaNacimiento=?,dni=?,altura=? where idPersona=(?)"
        datos = (nombre,nacimiento,dni,altura,id_persona)
        cur.execute(cSQL,datos)
        db.commit()
        return True
    else:
        return False


@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180.0)
    actualizar_persona(id_juan, 'juan carlos perez', datetime.datetime(1988, 4, 16), 32165497, 181.0)
    assert buscar_persona(id_juan) == (1, 'juan carlos perez', '1988-04-16 00:00:00', 32165497, 181.0)
    assert actualizar_persona(123, 'nadie', datetime.datetime(1988, 4, 16), 12312312, 181.0) is False

if __name__ == '__main__':
    pruebas()
