# Implementar la funcion agregar_peso, que inserte un registro en la tabla PersonaPeso.
# Debe validar:
# - que el ID de la persona ingresada existe (reutilizando las funciones ya implementadas).
# - que no existe de esa persona un registro de fecha posterior al que queremos ingresar.

# Debe devolver:
# - ID del peso registrado.
# - False en caso de no cumplir con alguna validacion.

import datetime

from ejercicio_01 import *
from ejercicio_02 import agregar_persona
from ejercicio_04 import buscar_persona
from ejercicio_06 import reset_tabla

def agregar_peso(id_persona, fecha, peso):
    try:
        mycursor = mydb.cursor()
        if(buscar_persona(id_persona) == False):
            return False
        mycursor.execute(f"INSERT INTO `PersonaPeso` (`IdPersona`, `Fecha`, `Peso`) SELECT '{id_persona}', '{fecha}', {peso} WHERE '{fecha}' > IFNULL((SELECT MAX(Fecha) from `PersonaPeso` WHERE `PersonaPeso`.`IdPersona` = {id_persona}), '1900-01-01 00:00:00')")
        mydb.commit()
        query_result = mycursor.fetchone()
    except mysql.connector.Error as error:
        print("Error al registrar peso de persona: {}".format(error))
        return False
    else:
        if mycursor.rowcount == 0:
            return False
        return mycursor.lastrowid
    finally:
        if (mydb.is_connected()):
            mycursor.close()
        pass


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
