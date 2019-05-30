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
from sqlalchemy.ext.declarative import declarative_base
from ejercicio_02 import agregar_persona
from ejercicio_04 import buscar_persona
from ejercicio_06 import reset_tabla, Peso
from ejercicio_07 import agregar_peso


def listar_pesos(id_persona, session):
    result = buscar_persona(id_persona, session)
    if (result != False):
        lista = session.query(Peso.fec,Peso.pes).filter(Peso.idPer == id_persona).all()
        list = []
        for p in lista:
            list.append((p.fec.strftime("%Y-%m-%d"),p.pes))
        return list
    else:
        return False


@reset_tabla
def pruebas(session):
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180,session)
    agregar_peso(id_juan, datetime.datetime(2018, 5, 1), 80,session)
    agregar_peso(id_juan, datetime.datetime(2018, 6, 1), 85,session)
    pesos_juan = listar_pesos(id_juan,session)
    pesos_esperados = [
        ('2018-05-01', 80),
        ('2018-06-01', 85),
    ]
    assert pesos_juan == pesos_esperados
    # id incorrecto
    assert listar_pesos(200,session) == False


if __name__ == '__main__':
    pruebas()
