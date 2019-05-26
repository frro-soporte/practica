# Implementar la funcion actualizar_persona, que actualiza un registro de una persona basado en su id.
# Devuelve un booleano en base a si encontro el registro y lo actualizo o no.

import datetime

from practico_03.ejercicio_01 import reset_tabla
from practico_03.ejercicio_02 import agregar_persona
from practico_03.ejercicio_04 import buscar_persona
from practico_03.ejercicio_01 import conexion


def actualizar_persona(id_persona, nombre, nacimiento, dni, altura):
    con = conexion()
    c = con.cursor()

    query = "UPDATE Persona SET nombre = ?, fechaNacimiento = ?, dni = ?, altura = ? WHERE idPersona = ?"
    result = c.execute(query, (nombre, nacimiento, dni, altura, id_persona))
    result = result.rowcount
    c.close()
    con.commit()
    con.close()
    if result > 0:
        return True
    else:
        return False




@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    actualizar_persona(id_juan, 'juan carlos perez', datetime.datetime(1988, 4, 16), 32165497, 181)

    con = conexion()
    c = con.cursor()
    res = c.execute("select * from Persona")
    for i in res:
        print (i)
    assert buscar_persona(id_juan) == (1, 'juan carlos perez', '1988-04-16 00:00:00', 32165497, 181)
    """Hubo que modificar el assert se cambio datetime.datetime(1988, 4, 16) por 1988-04-16 00:00:00"""

    assert actualizar_persona(123, 'nadie', datetime.datetime(1988, 4, 16), 12312312, 181) is False

if __name__ == '__main__':
    pruebas()
