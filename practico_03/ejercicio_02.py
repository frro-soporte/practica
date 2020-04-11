# Implementar la funcion agregar_persona, que inserte un registro en la tabla Persona
# y devuelva los datos ingresados el id del nuevo registro.

import datetime
import pymysql

from practico_03.ejercicio_01 import reset_tabla


def agregar_persona(nombre, nacimiento, dni, altura):
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='lalo123',
        db='Soportetp3')
    cursor = connection.cursor()
    consulta = "INSERT INTO persona (Nombre, FechaNacimiento, DNI, Altura) VALUES (%s, %s, %s, %s)"
    persona = (nombre, nacimiento, dni, altura)
    cursor.execute(consulta, persona)
    connection.commit()
    sql = "SELECT IdPersona FROM persona WHERE DNI = %s"
    cursor.execute(sql, dni)
    result = cursor.fetchone()
    return result[0]


@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.date(1988, 5, 15), 32165498, 180)
    id_marcela = agregar_persona('marcela gonzalez', datetime.date(1980, 1, 25), 12164492, 195)
    assert id_juan > 0
    assert id_marcela > id_juan


pruebas()
