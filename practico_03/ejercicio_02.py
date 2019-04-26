# Implementar la funcion agregar_persona, que inserte un registro en la tabla Persona
# y devuelva los datos ingresados el id del nuevo registro.

import datetime
import pymysql
db = pymysql.connect(host='localhost', user='root', password='852456', port=3306, db='Python')
cursor = db.cursor()
from practico_03.ejercicio_01 import reset_tabla


def agregar_persona(nombre, nacimiento, dni, altura):
    myquery = "INSERT INTO persona(Nombre , FechaNacimiento, DNI , Altura) VALUES (%s, %s, %s, %s)"
    cursor.execute(myquery,(nombre, nacimiento, dni, altura))
    db.commit()
    return int(cursor.lastrowid)

@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    id_marcela = agregar_persona('marcela gonzalez', datetime.datetime(1980, 1, 25), 12164492, 195)
    assert id_juan > 0
    assert id_marcela > id_juan

if __name__ == '__main__':
    pruebas()
