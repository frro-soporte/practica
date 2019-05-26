# Implementar la funcion borrar_persona, que elimina un registro en la tabla Persona.
# Devuelve un booleano en base a si encontro el registro y lo borro o no.

import datetime

from practico_03.ejercicio_01 import reset_tabla
from practico_03.ejercicio_02 import agregar_persona
from practico_03.ejercicio_01 import conexion


def borrar_persona(id_persona):
    con = conexion()
    c = con.cursor()

    query = "DELETE FROM Persona WHERE idPersona = ?"
    c.execute(query,(id_persona,))

    val = c.rowcount

    c.close()
    con.commit()
    con.close()

    if val == 1:
        return True
    else:
        return False


@reset_tabla
def pruebas():

    assert borrar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert borrar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
