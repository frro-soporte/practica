# Implementar la funcion buscar_persona, que devuelve el registro de una persona basado en su id.
# El return es una tupla que contiene sus campos: id, nombre, nacimiento, dni y altura.
# Si no encuentra ningun registro, devuelve False.

import datetime
import pymysql

from practico_03.ejercicio_01 import reset_tabla
from practico_03.ejercicio_02 import agregar_persona


def buscar_persona(id_persona):
    connection=pymysql.connect(
            host='localhost',
            user='root',
            password='lalo123',
            db='Soportetp3')
    cursor = connection.cursor()
    sql = "SELECT * FROM persona WHERE IdPersona = %s"
    cursor.execute(sql, id_persona)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    if result:
        return result[0]
    return False




@reset_tabla
def pruebas():
    juan = buscar_persona(agregar_persona('juan perez', datetime.date(1988, 5, 15), 32165498, 180))
    assert juan == (1, 'juan perez', datetime.date(1988, 5, 15), 32165498, 180)
    assert buscar_persona(12345) is False


pruebas()
