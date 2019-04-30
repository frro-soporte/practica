# Implementar la funcion borrar_persona, que elimina un registro en la tabla Persona.
# Devuelve un booleano en base a si encontro el registro y lo borro o no.

import datetime

import ejercicio_01
import ejercicio_02

import mysql.connector

def conexion():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="Pruebas-Python"
    )
    return mydb


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

@ejercicio_01.reset_tabla
def pruebas():
    assert borrar_persona(ejercicio_02.agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert borrar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
