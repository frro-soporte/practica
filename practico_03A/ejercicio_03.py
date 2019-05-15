# Implementar la funcion borrar_persona, que elimina un registro en la tabla Persona.
# Devuelve un booleano en base a si encontro el registro y lo borro o no.


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ejercicio_01 import Persona
from ejercicio_02 import agregar_persona
import datetime

Base = declarative_base()
engine = create_engine('mysql://root:852456ale@localhost:3306/python')
Base.metadata.bind = engine
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

def borrar_persona(id_persona):
    obj=session.query(Persona).filter(Persona.IdPersona==id_persona).first()
    if obj is None:
        return False
    else:
        x=session.delete(obj)
        session.commit()
        return True




def pruebas():
    assert borrar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert borrar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
