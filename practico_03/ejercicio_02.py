# Implementar la funcion agregar_persona, que inserte un registro en la tabla Persona
# y devuelva de los datos ingresados, el id del nuevo registro.
import sqlite3
import datetime

from practico_03.ejercicio_01 import reset_tabla

def conexion ():
    db = sqlite3.connect('C:\\Users\\Nahuel\\Desktop\\python.db')
    return db

def agregar_persona(nombre, nacimiento, dni, altura):
    con = conexion()
    c = con.cursor()

    query = "INSERT INTO Persona (nombre, fechaNacimiento, dni, altura) VALUES (?,?,?,?)"
    datos = (nombre, datetime.datetime.strftime(
        nacimiento, "%Y-%m-%d"), dni, altura)

    c.execute(query, datos)

    c.close()
    con.commit()
    con.close()

    return c.lastrowid


@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    id_marcela = agregar_persona('marcela gonzalez', datetime.datetime(1980, 1, 25), 12164492, 195)

    assert id_juan > 0
    assert id_marcela > id_juan

if __name__ == '__main__':
    pruebas()
