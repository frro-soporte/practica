# Implementar la funcion agregar_persona, que inserte un registro en la tabla Persona
# y devuelva los datos ingresados el id del nuevo registro.
import mysql.connector
import datetime

from practico_03.ejercicio_01 import reset_tabla


def agregar_persona(nombre, nacimiento, dni, altura):
    connection = mysql.connector.connect(user="root", password="root", host="localhost", database="soportebd")
    cursor = connection.cursor()
    cSQL = "INSERT INTO persona (Nombre, FechaNacimiento, DNI, Altura, IdPersona) VALUES (%s, %s, %s, %s, %s)"
    persona = (nombre, nacimiento, dni, altura, 0)
    cursor.execute(cSQL, persona)
    connection.commit()
    cselectSQL = "SELECT IdPersona FROM persona WHERE DNI = %s"
    cursor.execute(cselectSQL, (dni,))
    result = cursor.fetchone()
    return result[0]


@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    id_marcela = agregar_persona('marcela gonzalez', datetime.datetime(1980, 1, 25), 12164492, 195)
    assert id_juan > 0
    assert id_marcela > id_juan


if __name__ == '__main__':
    pruebas()
