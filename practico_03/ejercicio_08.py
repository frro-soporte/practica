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

from datetime import date
import sqlalchemy
from ejercicio_01 import Persona, session, crear_tabla, borrar_tabla
from ejercicio_02 import agregar_persona
from ejercicio_06 import crear_tabla_peso, borrar_tabla_peso, PersonaPeso
from ejercicio_07 import agregar_peso
from ejercicio_04 import buscar_persona



def listar_pesos(id_persona):
    per = buscar_persona(id_persona)
    if per is not False:
        pesos = session.query(PersonaPeso).filter(PersonaPeso.idPer == id_persona).all()
        if len(pesos) == 0:
            print("No hay pesos registrados de esta persona.")
            return False
        else:
            lista = []
            i = 1
            for pes in pesos:
                lista.append((pes.fecha, pes.peso))
            return lista
    else:
        return False



#@reset_tabla
def pruebas():
    crear_tabla()
    crear_tabla_peso()
    id_juan = agregar_persona('juan perez', date(1988, 5, 15), 32165498, 180)
    agregar_peso(id_juan, date(2018, 5, 1), 80)
    agregar_peso(id_juan, date(2018, 6, 1), 85)
    pesos_juan = listar_pesos(id_juan)
    pesos_esperados = [
        ('2018-05-01', 80),
        ('2018-06-01', 85),
    ]
    assert pesos_juan == pesos_esperados
    # id incorrecto
    assert listar_pesos(200) == False
    borrar_tabla_peso()
    borrar_tabla()


if __name__ == '__main__':
    pruebas()
