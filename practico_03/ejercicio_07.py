# Implementar la funcion agregar_peso, que inserte un registro en la tabla PersonaPeso.
# Debe validar:
# - que el ID de la persona ingresada existe (reutilizando las funciones ya implementadas).
# - que no existe de esa persona un registro de fecha posterior al que queremos ingresar.

# Debe devolver:
# - ID del peso registrado.
# - False en caso de no cumplir con alguna validacion.

import sqlite3,datetime

from practico_03.ejercicio_02 import agregar_persona
from practico_03.ejercicio_06 import reset_tabla
from practico_03.ejercicio_04 import buscar_persona

conn = sqlite3.connect('tabla.db')
cur = conn.cursor()

def existe_posterior_pesaje(id_persona, fecha):
    cur.execute("SELECT idPersona FROM personaPeso WHERE idPersona=? and fecha>? ",(id_persona,fecha,))
    existe=cur.fetchone()
    if (existe is not None):
        return True
    else:
        return False

def agregar_peso(id_persona,fecha,peso):
    per=buscar_persona(id_persona)
    if (per is not False):
        if existe_posterior_pesaje(id_persona,fecha) is False:
            cur.execute("INSERT INTO personaPeso(idPersona,fecha,peso) VALUES(?,?,?)",(id_persona,fecha,peso,))
            conn.commit()
            return cur.lastrowid
        else:
            return False
    else:
        return False


@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.date(1988,5,15), 32165498, 180)
    assert agregar_peso(id_juan, datetime.date(2018,5,26), 80) > 0
    # id incorrecto
    assert agregar_peso(200, datetime.date(1998,5,15), 80) == False
    # registro previo al 2018-05-26
    assert agregar_peso(id_juan, datetime.date(2018,5,16), 80) == False

if __name__ == 'main':
    pruebas()
