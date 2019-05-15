# Implementar la funcion agregar_peso, que inserte un registro en la tabla PersonaPeso.
# Debe validar:
# - que el ID de la persona ingresada existe (reutilizando las funciones ya implementadas).
# - que no existe de esa persona un registro de fecha posterior al que queremos ingresar.

# Debe devolver:
# - ID del peso registrado.
# - False en caso de no cumplir con alguna validacion.


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Practica01Alchemy import Persona
from Practica06Alchemy import PersonaPeso
from Practica03Alchemy import agregar_persona
from Practica04Alchemy import buscar_persona
from Practica06Alchemy import reset_tabla
import datetime

Base = declarative_base()
engine = create_engine('mysql://root:852456ale@localhost:3306/python')
Base.metadata.bind = engine
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

def agregar_peso(id_persona, fecha, peso):
    x=buscar_persona(id_persona)
    if (x != False) :
        z=session.query(PersonaPeso).filter(PersonaPeso.IdPersona==id_persona,PersonaPeso.Fecha>=fecha).first()

        if z == None:
            pp = PersonaPeso(fecha,peso)
            pp.IdPersona=id_persona
            session.add(pp)
            session.commit()
            return id_persona
        else:
            return False
    else:
        return False



def pruebas():
    id_juan = agregar_persona('juan perez', datetime.date(1988, 5, 15), 32165498, 180)
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 26), 80) > 0
    # id incorrecto

    assert agregar_peso(400, datetime.datetime(1988, 5, 15), 80) == False
    # registro previo al 2018-05-26
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 16), 80) == False

if __name__ == '__main__':
    pruebas()
