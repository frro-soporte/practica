# Implementar la funcion agregar_peso, que inserte un registro en la tabla PersonaPeso.
# Debe validar:
# - que el ID de la persona ingresada existe (reutilizando las funciones ya implementadas).
# - que no existe de esa persona un registro de fecha posterior al que queremos ingresar.

# Debe devolver:
# - ID del peso registrado.
# - False en caso de no cumplir con alguna validacion.

import datetime
import pymysql

from ejercicio_02 import agregar_persona
from ejercicio_06 import reset_tabla
from ejercicio_04 import buscar_persona


def agregar_peso(id_persona, fecha, peso):
    connection=pymysql.connect(
            host='localhost',
            user='root',
            password='lalo123',
            db='Soportetp3')
    cursor = connection.cursor()
    results=buscar_persona(id_persona)
    if results:
        csql="SELECT * FROM PersonaPeso WHERE  IdPersona = %s AND Fecha > %s"
        cursor.execute(csql, (id_persona, fecha))
        result=cursor.fetchone()
        if result:
            sql="INSERT INTO PersonaPeso (Fecha,Peso) values (%s,%s)"
            cursor.execute(sql,fecha,peso)
            connection.commit()
            csql1="SELECT * FROM PersonaPeso WHERE IdPersona = %s AND Fecha = %s"
            cursor.execute(csql1,(id_persona,fecha))
            peso = cur.fetchone()
            return peso
    else: False


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
