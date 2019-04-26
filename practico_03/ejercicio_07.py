# Implementar la funcion agregar_peso, que inserte un registro en la tabla PersonaPeso.
# Debe validar:
# - que el ID de la persona ingresada existe (reutilizando las funciones ya implementadas).
# - que no existe de esa persona un registro de fecha posterior al que queremos ingresar.

# Debe devolver:
# - ID del peso registrado.
# - False en caso de no cumplir con alguna validacion.

import datetime
import sqlite3
from ejercicio_02 import agregar_persona
from ejercicio_04 import buscar_persona
from ejercicio_06 import reset_tabla


db = sqlite3.connect('D:\\prueba.db')
cur = db.cursor()    


def agregar_peso(id_persona, fecha, peso):
    res = buscar_persona(id_persona)
    if (res is not False): #valida que exista ID
        cSQL = 'select * from PersonaPeso where fecha>? and idPersona=?'
        cur.execute(cSQL,(fecha,id_persona))
        fechaPos = cur.fetchall()
        if len(fechaPos) == 0: #no hay registros de fechas posteriores
            cSQL = 'insert into PersonaPeso(idPersona,fecha,peso) values(?,?,?)'
            datos = (id_persona,fecha,peso)
            cur.execute(cSQL,datos)
            db.commit()
            return cur.lastrowid
        else:
            return False
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
