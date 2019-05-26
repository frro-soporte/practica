# Implementar la funcion agregar_peso, que inserte un registro en la tabla PersonaPeso.
# Debe validar:
# - que el ID de la persona ingresada existe (reutilizando las funciones ya implementadas).
# - que no existe de esa persona un registro de fecha posterior al que queremos ingresar.

# Debe devolver:
# - ID del peso registrado.
# - False en caso de no cumplir con alguna validacion.

import datetime
from sqlalchemy import exc
from ejercicio_01 import conexion, reset_tabla, Persona, sessionUsuario
from ejercicio_02 import agregar_persona
from ejercicio_04 import buscar_persona
from ejercicio_06 import reset_tabla, PersonaPeso


def agregar_peso(id_persona, fecha, peso):
    sqlconn = conexion()
    per = buscar_persona(id_persona)
    user = sessionUsuario()
    if per != False:
        if exist_persona(id_persona, fecha):
            perPeso = PersonaPeso()
            perPeso.idPersona = id_persona
            perPeso.Fecha = fecha
            perPeso.Peso = peso
            user.add(perPeso)
            user.commit()
            result = user.query(PersonaPeso).filter_by(idPersonaPeso = id_persona).first()
            if result != None:
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def exist_persona(id_persona,fecha):
    sqlconn = conexion()
    user = sessionUsuario()
    per = Persona()
    per = user.query(PersonaPeso).filter_by(idPersonaPeso=id_persona).first()
    if per != None:
        if datetime.datetime.strftime(per.Fecha, '%d%m%y') < datetime.datetime.strftime(fecha, '%d%m%y'):
            return True
        else:
            return False
    else:
        return True

@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime(1988, 5, 15), 32165498, 180)
    assert agregar_peso(id_juan, datetime(2018, 5, 26), 80) > 0
    # id incorrecto
    assert agregar_peso(200, datetime(1988, 5, 15), 80) == False
    # registro previo al 2018-05-26
    assert agregar_peso(id_juan, datetime(2018, 5, 16), 80) == False

if __name__ == '__main__':
    pruebas()
