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
    user = sessionUsuario()
    per = buscar_persona(id_persona)
    if per != False:
        if not exist_persona(id_persona,fecha):
            per = PersonaPeso(id_persona, fecha, peso)
            user.add(per)
            user.commit()
            result = user.query(PersonaPeso).filter_by(id_persona).first()
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
    per = user.query(Persona).filter_by(idPersona=id_persona).first()
    if per.fechaNacimiento < fecha:
        return True
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
