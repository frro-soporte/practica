# Implementar la funcion listar_pesos, que devuelva el historial de pesos para una persona dada.
# Debe validar:
# - que el ID de la persona ingresada existe (reutilizando las funciones ya implementadas).

# Debe devolver:
# - Lista de (fecha, peso), donde fecha esta representado por el siguiente formato: AAAA-MM-DD.
#   Ejemplo:
#   [
#       ('2018-01-01', 80),
#       ('2018-02-01', 85),
#       ('2018-03-01', 87),
#       ('2018-04-01', 84),
#       ('2018-05-01', 82),
#   ]
# - False en caso de no cumplir con alguna validacion.

import datetime
import sqlite3

from practico_03.ejercicio_02 import agregar_persona
from practico_03.ejercicio_04 import buscar_persona
from practico_03.ejercicio_06 import reset_tabla
from practico_03.ejercicio_07 import agregar_peso



def listar_pesos(id_persona):
    if buscar_persona(id_persona) != False:
        db = sqlite3.connect('mibase')
        cur = db.cursor()
        cur.execute('SELECT fecha, peso from PersonaPeso where idPersona=?', (id_persona,))
        per = cur.fetchall()
        if per != None:
            li = []
            for i in per:
                i = list(i)
                aux = datetime.datetime.strptime(i[0], '%Y-%m-%d %H:%M:%S')
                aux_1 = aux.date()
                i[0] = aux_1
                li.append(tuple([str(i[0]), i[1]]))
            db.commit()
            return li
        cur.close()
        db.close()
        return False
    return False


@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    agregar_peso(id_juan, datetime.datetime(2018, 5, 1), 80)
    agregar_peso(id_juan, datetime.datetime(2018, 6, 1), 85)
    pesos_juan = listar_pesos(id_juan)
    pesos_esperados = [
        ('2018-05-01', 80),
        ('2018-06-01', 85),
    ]
    assert pesos_juan == pesos_esperados
    # id incorrecto
    assert listar_pesos(200) == False


if __name__ == '___main___':
    pruebas()
