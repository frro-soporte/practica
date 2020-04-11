# Implementar la funcion actualizar_persona, que actualiza un registro de una persona basado en su id.
# Devuelve un booleano en base a si encontro el registro y lo actualizo o no.

import datetime
import pymysql

from practico_03.ejercicio_01 import reset_tabla
from practico_03.ejercicio_02 import agregar_persona
from practico_03.ejercicio_04 import buscar_persona


def actualizar_persona(id_persona, nombre, nacimiento, dni, altura):
    connection=pymysql.connect(
            host='localhost',
            user='root',
            password='lalo123',
            db='Soportetp3')
    cursor = connection.cursor()
    sql = "SELECT * FROM PERSONA WHERE IdPersona = %s"
    cursor.execute(sql, id_persona)
    result = cursor.fetchone()
    if result:
        sql1 = "UPDATE persona SET Nombre = %s, FechaNacimiento = %s, DNI = %s, Altura = %s WHERE IdPersona = %s"
        persona = (nombre, nacimiento, dni, altura, id_persona)
        cursor.execute(sql1, persona)
        connection.commit()
        return True
    return False


@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.date(1988, 5, 15), 32165498, 180)
    actualizar_persona(id_juan, 'juan carlos perez', datetime.date(1988, 4, 16), 32165497, 181)
    assert buscar_persona(id_juan) == (1, 'juan carlos perez', datetime.date(1988, 4, 16), 32165497, 181)
    assert actualizar_persona(123, 'nadie', datetime.date(1988, 4, 16), 12312312, 181) is False


pruebas()
