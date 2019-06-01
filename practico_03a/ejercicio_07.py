# Implementar la funcion agregar_peso, que inserte un registro en la tabla PersonaPeso.
# Debe validar:
# - que el ID de la persona ingresada existe (reutilizando las funciones ya implementadas).
# - que no existe de esa persona un registro de fecha posterior al que queremos ingresar.

# Debe devolver:
# - ID del peso registrado.
# - False en caso de no cumplir con alguna validacion.

import datetime
from sqlalchemy import exc
from ejercicio_01 import conexion, Persona, sessionUsuario
from ejercicio_02 import agregar_persona
from ejercicio_04 import buscar_persona
from ejercicio_06 import reset_tabla, PersonaPeso


def agregar_peso(id_persona, fecha, peso):
    conexion()
    user = sessionUsuario()
    if buscar_persona(id_persona) != False :
        if exist_personapeso(id_persona, fecha):
            pp = PersonaPeso()
            pp.idPersona = id_persona
            pp.fecha = fecha
            pp.peso = peso
            user.add(pp)
            user.commit()
            id = (user.query(PersonaPeso).filter_by(idPersona = id_persona).order_by(PersonaPeso.fecha.desc()).first()).idPeso
            if id != None:
                return id
            else:
                return False
        else:
            return False
    else:
        return False


def exist_personapeso(id_persona,fecha):
    conexion()
    user = sessionUsuario()
    per = PersonaPeso()
    per = user.query(PersonaPeso).filter_by(idPersona=id_persona).first()
    if per != None:
        if per.fecha == None:
            return True
        elif datetime.datetime.strftime(per.fecha, '%d%m%y') < datetime.datetime.strftime(fecha, '%d%m%y'):
            return True
        else:
            return False
    else:
        return True

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
