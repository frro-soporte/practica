# Implementar la funcion actualizar_persona, que actualiza un registro de una persona basado en su id.
# Devuelve un booleano en base a si encontro el registro y lo actualizo o no.

import datetime

# from practico_03.ejercicio_01 import reset_tabla
# from practico_03.ejercicio_02 import agregar_persona
# from practico_03.ejercicio_04 import buscar_persona
from ejercicio_01 import reset_tabla
from ejercicio_02 import agregar_persona
from ejercicio_04 import buscar_persona
import sqlite3

def actualizar_persona(id_persona, nombre, nacimiento, dni, altura):
    #Aca ya tengo id_persona, entonces solo tengo que hacer un update
    #el problema del id venia de la mano con el datetime
    cursor = db.cursor()

    cSQL = 'UPDATE persona SET nombre= ?, fecha_nacimiento = ?, dni= ?, altura = ? WHERE id_persona = ?'
    tdatos = ( nombre, nacimiento, dni, altura, id_persona )
    cursor.execute(cSQL, tdatos)
    fila = cursor.fetchone()
    db.commit()
    if fila == None:
        return False
    else:

        return fila




@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    actualizar_persona(id_juan, 'juan carlos perez', datetime.datetime(1988, 4, 16), 32165497, 181)
    #assert buscar_persona(id_juan) == (1, 'juan carlos perez', datetime.datetime(1988, 4, 16), 32165497, 181)
    assert buscar_persona(id_juan) == (1, 'juan carlos perez', '1988-04-16 00:00:00', 32165497, 181)
    assert actualizar_persona(123, 'nadie', datetime.datetime(1988, 4, 16), 12312312, 181) is False

if __name__ == '__main__':
    db = sqlite3.connect('persona_db.sqlite')

    pruebas()
