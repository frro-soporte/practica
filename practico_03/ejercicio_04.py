# Implementar la funcion buscar_persona, que devuelve el registro de una persona basado en su id.
# El return es una tupla que contiene sus campos: id, nombre, nacimiento, dni y altura.
# Si no encuentra ningun registro, devuelve False.

import datetime

from ejercicio_01 import reset_tabla, conexion
from ejercicio_02 import agregar_persona
import mysql.connector

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



@reset_tabla
def pruebas():
    juan = buscar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert juan == (1, 'juan perez', datetime.date(1988, 5, 15), 32165498, 180)
    assert buscar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
