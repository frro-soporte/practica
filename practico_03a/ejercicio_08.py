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
from _ast import Tuple
import datetime
import mysql.connector
from sqlalchemy import exc
from ejercicio_01 import conexion, reset_tabla, Persona, sessionUsuario
from ejercicio_02 import agregar_persona
from ejercicio_04 import buscar_persona
from ejercicio_06 import reset_tabla, PersonaPeso
from ejercicio_07 import agregar_peso

def listar_pesos(id_persona):
    perso = buscar_persona(id_persona)
    if(perso != False):
        sqlconn = conexion()
        user = sessionUsuario()
        #persPeso = user.query(PersonaPeso).filter_by(idPersonaPeso=id_persona).all()
        persPeso = user.query(PersonaPeso.fecha, PersonaPeso.peso).all()
        if persPeso != None:
            #for item in persPeso:
             #   pesos = [item.Fecha, item.Peso]
            pesos = [persPeso[0], persPeso[1]]
            return pesos
        else:
            return False
    else:
        return False

@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    agregar_peso(id_juan, datetime.datetime(2018, 5, 1), 80)
    agregar_peso(id_juan, datetime.datetime(2018, 6, 1), 85)
    pesos_juan = listar_pesos(id_juan)
    pesos_esperados = [
        (datetime.date(2018, 5, 1), 80),
        (datetime.date(2018, 6, 1), 85),
    ]
    assert pesos_juan == pesos_esperados
    # id incorrecto
    assert listar_pesos(200) == False


if __name__ == '__main__':
    pruebas()
