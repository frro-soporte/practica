# Implementar la funcion actualizar_persona, que actualiza un registro de una persona basado en su id.
# Devuelve un booleano en base a si encontro el registro y lo actualizo o no.

import datetime

from practico_03.ejercicio_01 import reset_tabla
from practico_03.ejercicio_02 import agregar_persona
from practico_03.ejercicio_04 import buscar_persona


def actualizar_persona(id_persona, nombre, nacimiento, dni, altura):

    cursor = db.cursor()
    cSQL = 'UPDATE table_name SET nombre = ?, nacimiento = ?, dni = ?, altura = ? WHERE id_persona = ?'
    cursor.execute(cSQL, nombre, nacimiento, dni, altura, id_persona)
    db.commit()
    
    '''tendria que hacer un select con el id_persona
    cSQL = 'SELECT * FROM persona WHERE id_persona = ?'
    cursor.execute(cSQL, id_persona)
    print(cursor)'''
    # se deberia hacer el if q si esta vacio o no


@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    actualizar_persona(id_juan, 'juan carlos perez', datetime.datetime(1988, 4, 16), 32165497, 181)
    assert buscar_persona(id_juan) == (1, 'juan carlos perez', datetime.datetime(1988, 4, 16), 32165497, 181)
    assert actualizar_persona(123, 'nadie', datetime.datetime(1988, 4, 16), 12312312, 181) is False

if __name__ == '__main__':
    pruebas()
