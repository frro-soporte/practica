# Implementar la funcion agregar_peso, que inserte un registro en la tabla PersonaPeso.
# Debe validar:
# - que el ID de la persona ingresada existe (reutilizando las funciones ya implementadas).
# - que no existe de esa persona un registro de fecha posterior al que queremos ingresar.

# Debe devolver:
# - ID del peso registrado.
# - False en caso de no cumplir con alguna validacion.

import datetime
from ejercicio_01 import Persona
import datetime
from sqlalchemy.ext.declarative import declarative_base
from ejercicio_02 import agregar_persona
from ejercicio_04 import buscar_persona
from ejercicio_06 import reset_tabla, Peso

def agregar_peso(id_persona, fecha, peso, session):
    result = buscar_persona(id_persona, session)
    if (result != False):
        busqueda= session.query(Peso).filter(Peso.idPer == id_persona).filter(Peso.fec > fecha).first()
        if (busqueda != None):
            return False

        pesaje = Peso(fecha, peso)
        pesaje.fec = fecha
        pesaje.pes = peso
        pesaje.idPer = id_persona
        session.add(pesaje)
        session.commit()
        return pesaje.idPes
    else:
        return False

@reset_tabla
def pruebas(session):
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180, session)
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 26), 80,session) > 0
    # id incorrecto
    assert agregar_peso(200, datetime.datetime(1988, 5, 15), 80,session) == False
    # registro previo al 2018-05-26
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 16), 80,session) == False

if __name__ == '__main__':
    pruebas()
