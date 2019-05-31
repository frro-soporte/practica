# Implementar la funcion agregar_peso, que inserte un registro en la tabla PersonaPeso.
# Debe validar:
# - que el ID de la persona ingresada existe (reutilizando las funciones ya implementadas).
# - que no existe de esa persona un registro de fecha posterior al que queremos ingresar.

# Debe devolver:
# - ID del peso registrado.
# - False en caso de no cumplir con alguna validacion.

import datetime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///c://Users//Nahuel//Desktop//sqlalchemy_db.db')
Base.metadata.bind = engine
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

from practico_03_alchemy.ejercicio_02 import agregar_persona
from practico_03_alchemy.ejercicio_06 import reset_tabla, PersonaPeso
from practico_03_alchemy.ejercicio_04 import buscar_persona



def agregar_peso(idPersona, fecha, peso):

    res = buscar_persona(idPersona)

    if res != False:
        result = session.query(PersonaPeso).filter(PersonaPeso.idPersona== idPersona, PersonaPeso.fecha > fecha).all()
        if result == []:
               oper = PersonaPeso(idPersona =idPersona, fecha = fecha, peso = peso)
               session.add(oper)
               session.commit()
               resultado = session.query(PersonaPeso).order_by(PersonaPeso.id.desc()).first()
               return resultado.id
        else:
              return False
    else:
        return False
    pass


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
