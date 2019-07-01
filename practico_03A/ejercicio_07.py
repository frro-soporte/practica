# Implementar la funcion agregar_peso, que inserte un registro en la tabla PersonaPeso.
# Debe validar:
# - que el ID de la persona ingresada existe (reutilizando las funciones ya implementadas).
# - que no existe de esa persona un registro de fecha posterior al que queremos ingresar.

# Debe devolver:
# - ID del peso registrado.
# - False en caso de no cumplir con alguna validacion.

import datetime
from practico_03A.ejercicio_01 import Persona
import datetime
from sqlalchemy.ext.declarative import declarative_base
from practico_03A.ejercicio_02 import agregar_persona
from practico_03A.ejercicio_04 import buscar_persona
from practico_03A.ejercicio_06 import reset_tabla, Peso



def agregar_peso(id_persona, fecha, peso, session):
    result = buscar_persona(id_persona, session)
    if (result != False): #Aca sabemos que la persona existe, resta verificar que no haya registros posteriores a ese pesaje
        busqueda= session.query(Peso).filter(Peso.persona_id == id_persona).filter(Peso.fecha_peso > fecha).first()
        if (busqueda != None):
            return False

        pesaje = Peso()
        pesaje.fecha_peso = fecha
        pesaje.peso = peso
        pesaje.persona_id = id_persona
        session.add(pesaje)
        session.commit()
        return pesaje.id_peso
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
