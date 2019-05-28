# Implementar la funcion agregar_persona, que inserte un registro en la tabla Persona
# y devuelva los datos ingresados el id del nuevo registro.

import datetime
import mysql.connector
from ejercicio_01 import conexion, reset_tabla


def agregar_persona(nombre, nacimiento, dni, altura):
    conn = conexion()
    mycursor = conn.cursor()
    sql = "insert into Persona (Nombre, FechaNacimiemto, DNI, Altura) values (%s, %s, %s, %s);"
    datos =(str(nombre), nacimiento, dni, altura)
    mycursor.execute(sql, datos)
    conn.commit()
    sql = "SELECT LAST_INSERT_ID();"

    mycursor.execute(sql)
    data= mycursor.fetchall()
    id = data[0][0]

    print("El id es {0}, el nombre {1}, la fecha de nacimiento {2}, el nro dni {3} y la altura es {4}".format(id, nombre, nacimiento, dni, altura))
    return id


@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    id_marcela = agregar_persona('marcela gonzalez', datetime.datetime(1980, 1, 25), 12164492, 195)
    assert id_juan > 0
    assert id_marcela > id_juan

if __name__ == '__main__':
pruebas()