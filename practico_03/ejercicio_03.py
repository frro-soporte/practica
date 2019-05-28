# Implementar la funcion borrar_persona, que elimina un registro en la tabla Persona.
# Devuelve un booleano en base a si encontro el registro y lo borro o no.

import datetime
from ejercicio_02 import agregar_persona
import mysql.connector
from ejercicio_01 import reset_tabla, conexion


def borrar_persona(id_persona):
    try:
        conn = conexion()
        mycursor = conn.cursor()
        sql = "delete from persona where IdPersona = {0}".format(id_persona)
        mycursor.execute(sql)
        conn.commit()
        if mycursor.rowcount > 0:
            return True
        else:
            return False

    except mysql.connector.Error:
        return False

@reset_tabla
def pruebas():
    assert borrar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert borrar_persona(12345) is False

if __name__ == '__main__':
pruebas()