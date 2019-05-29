# Implementar la funcion agregar_peso, que inserte un registro en la tabla PersonaPeso.
# Debe validar:
# - que el ID de la persona ingresada existe (reutilizando las funciones ya implementadas).
# - que no existe de esa persona un registro de fecha posterior al que queremos ingresar.

# Debe devolver:
# - ID del peso registrado.
# - False en caso de no cumplir con alguna validacion.

import datetime
import sqlalchemy
from ejercicio_01 import session, crear_tabla, borrar_tabla
from ejercicio_02 import agregar_persona
from ejercicio_04 import buscar_persona
from ejercicio_06 import PersonaPeso, crear_tabla_peso, borrar_tabla_peso


def agregar_peso(id_persona, fecha, peso):
    res = buscar_persona(id_persona)
    if res is not False:
        #falta validar que no exista registro posterior
        pesos = session.query(PersonaPeso).filter(PersonaPeso.idPer == id_persona, PersonaPeso.fecha > fecha).all()
        if len(pesos) == 0:
            perPeso = PersonaPeso()
            perPeso.fecha = fecha
            perPeso.peso = peso
            perPeso.idPer = id_persona
            session.add(perPeso)
            session.commit()
            return perPeso.id
        else:
            return False
    elif res is False:
        return False




def pruebas():
    crear_tabla()
    crear_tabla_peso()
    id_juan = agregar_persona('juan perez', datetime.date(1988, 5, 15), 32165498, 180)
    assert agregar_peso(id_juan, datetime.date(2018, 5, 26), 80) > 0
    # id incorrecto
    assert agregar_peso(200, datetime.date(1988, 5, 15), 80) == False
    # registro previo al 2018-05-26
    assert agregar_peso(id_juan, datetime.date(2018, 5, 16), 80) == False
    borrar_tabla_peso()
    borrar_tabla()

if __name__ == '__main__':
    pruebas()
