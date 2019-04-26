# Implementar la funcion agregar_persona, que inserte un registro en la tabla Persona
# y devuelva los datos ingresados el id del nuevo registro.

import datetime
import sqlite3
from ejercicio_01 import reset_tabla,crear_tabla


db = sqlite3.connect('D:\\prueba.db')
cur = db.cursor()


def agregar_persona(nombre, nacimiento, dni, altura):
    cSQL = 'INSERT INTO Persona(nombre,fechaNacimiento,dni,altura) VALUES(?,?,?,?)'
    tdatos = (nombre,nacimiento,dni,altura)
    cur.execute(cSQL,tdatos)
    id = cur.lastrowid
    dato = (id,)
    cur.execute('select idPersona, nombre, fechaNacimiento, dni, altura from Persona where idPersona=?',dato)
    for row in cur:
        print("idPersona: ", row[0])
        print("Nombre: ", row[1])
        print("Fecha de Nacimiento: ", row[2])
        print("DNI: ", row[3])
        print("Altura: ", row[4])
    db.commit()
    return id


@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    id_marcela = agregar_persona('marcela gonzalez', datetime.datetime(1980, 1, 25), 12164492, 195)
    assert id_juan > 0
    assert id_marcela > id_juan


if __name__ == '__main__':
    pruebas()
