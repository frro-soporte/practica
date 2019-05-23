# Implementar la funcion agregar_peso, que inserte un registro en la tabla PersonaPeso.
# Debe validar:
# - que el ID de la persona ingresada existe (reutilizando las funciones ya implementadas).
# - que no existe de esa persona un registro de fecha posterior al que queremos ingresar.

# Debe devolver:
# - ID del peso registrado.
# - False en caso de no cumplir con alguna validacion.

import datetime
import mysql.connector
from ejercicio_01 import conexion
from ejercicio_02 import agregar_persona
from ejercicio_04 import buscar_persona
from ejercicio_06 import reset_tabla


def agregar_peso(id_persona, fecha, peso):
    sqlconn = conexion()
    cursor = sqlconn.cursor()
    #en ningun momento buscar_persona deuvuelve solo true o false
    per = buscar_persona(id_persona)
    if per != False:
        if not exist_persona(id_persona,fecha):
            sql = "INSERT INTO PersonaPeso(IdPersona, Fecha, Peso) values ({0},'{1}',{2})".format(id_persona, fecha, peso)
            cursor.execute(sql)
            sqlconn.commit()
            result = cursor.rowcount
            cursor.close()
            if result > 0:
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def exist_persona(id_persona,fecha):
    sqlconn = conexion()
    cursor = sqlconn.cursor()
    strselect = "select * from PersonaPeso where IdPersona = {0} and Fecha > '{1}'".format(id_persona, fecha)
    cursor.execute(strselect)
    resultado= cursor.fetchall()
    cursor.close()
    sqlconn.close()
    if resultado != []:
        return True
    else:
        return False

@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 26), 80) > 0
    # id incorrecto
    assert agregar_peso(200, datetime.datetime(1988, 5, 15), 80) == False
    # registro previo al 2018-05-26
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 16), 80) == False

if __name__ == '__main__':
    pruebas()
