# Implementar la funcion buscar_persona, que devuelve el registro de una persona basado en su id.
# El return es una tupla que contiene sus campos: id, nombre, nacimiento, dni y altura.
# Si no encuentra ningun registro, devuelve False.

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

def buscar_persona(id_persona):
    try:
        conn = conexion()
        mycursor = conn.cursor()
        sql = "select IdPersona, Nombre, FechaNacimiemto, DNI, Altura from persona where IdPersona = {0}".format(id_persona)
        mycursor.execute(sql)
        persona = mycursor.fetchall()
        if mycursor.rowcount > 0:
            for item in persona:
                return item
                #idPersona = item[0]
                #nombre = item[1]
                #fechaNacimiento = item[2]
                #dni = item[3]
                #altura = item[4]
        else:
            return False

    except mysql.connector.Error:
        return False



@ejercicio_01.reset_tabla
def pruebas():
    juan = buscar_persona(ejercicio_02.agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert juan == (1, 'juan perez', datetime.date(1988, 5, 15), 32165498, 180)
    assert buscar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
