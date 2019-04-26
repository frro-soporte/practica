# Implementar la funcion buscar_persona, que devuelve el registro de una persona basado en su id.
# El return es una tupla que contiene sus campos: id, nombre, nacimiento, dni y altura.
# Si no encuentra ningun registro, devuelve False.

import datetime
import pymysql
db = pymysql.connect(host='localhost', user='root', password='852456', port=3306, db='Python')
cursor = db.cursor()
from practico_03.ejercicio_01 import reset_tabla
from practico_03.ejercicio_02 import agregar_persona


def buscar_persona(id_persona):
    x=cursor.execute("SELECT IdPersona,Nombre,FechaNacimiento,DNI,Altura FROM Persona where IdPersona = %s",id_persona)
    if x==0:
        return False
    else:
        pers=cursor.fetchone()
        return pers


@reset_tabla
def pruebas():
    juan = buscar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert juan == (1, 'juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    assert buscar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
