# Implementar la funcion agregar_peso, que inserte un registro en la tabla PersonaPeso.
# Debe validar:
# - que el ID de la persona ingresada existe (reutilizando las funciones ya implementadas).
# - que no existe de esa persona un registro de fecha posterior al que queremos ingresar.

# Debe devolver:
# - ID del peso registrado.
# - False en caso de no cumplir con alguna validacion.

import datetime
from ejercicio_01 import conexion
from ejercicio_02 import agregar_persona
from ejercicio_04 import buscar_persona
from ejercicio_06 import reset_tabla


def agregar_peso(id_persona, fecha, peso):
    sqlconn = conexion()
    cursor = sqlconn.cursor()
    if buscar_persona(id_persona) and exist_persona(id_persona,fecha):
        strinsert = "INSERT INTO PersonaxPeso(id_persona,fecha,peso) , values (%s,%s,%s)"
        param = (id_persona,fecha,peso)
        cursor.execute(strinsert,param)
        cursor.commit()
        cursor.close()
        return cursor.fechone()[0]
    else:
        return False


def exist_persona(id_persona,fecha):
    sqlconn = conexion()
    cursor = sqlconn.cursor()
    strselect = "select fecha from PersonaxPeso where id_persona = %s ORDER BY fecha"
    parametro= id_persona
    cursor.execute(strselect,parametro)
    resultado= cursor.fetchall()
    cursor.close()
    sqlconn.close()
    if resultado :
        if resultado [0] > fecha:
            return False
        else:
            return True
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
