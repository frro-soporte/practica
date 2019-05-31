# Implementar la funcion borrar_persona, que elimina un registro en la tabla Persona.
# Devuelve un booleano en base a si encontro el registro y lo borro o no.

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


from practico_03_alchemy.ejercicio_01 import reset_tabla
from practico_03_alchemy.ejercicio_02 import agregar_persona
from practico_03_alchemy.ejercicio_01 import Persona



def borrar_persona(id_persona):

    res = session.query(Persona).filter(Persona.idPersona == id_persona).first()

    if res is not None:
        session.delete(res)
        session.commit()
        return True
    else:
        return False










@reset_tabla
def pruebas():

    assert borrar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert borrar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
