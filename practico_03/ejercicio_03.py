# Implementar la funcion borrar_persona, que elimina un registro en la tabla Persona.
# Devuelve un booleano en base a si encontro el registro y lo borro o no.

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy import create_engine, delete
from sqlalchemy.orm import sessionmaker
from sqlalchemy import *
import datetime

from ejercicio_01 import Persona, engine, session, Base, crear_tabla, borrar_tabla
from ejercicio_02 import agregar_persona


def borrar_persona(id_persona):
    per = session.query(Persona).get(id_persona)
    if per is None:
        print("Persona no encontrada")
        return False
    else:
        session.delete(per) 
        session.commit()
        print("Persona encontrada")
        return True



#@reset_tabla
def pruebas():
    crear_tabla()
    assert borrar_persona(agregar_persona('juan perez', datetime.date(1988, 5, 15), 32165498, 180))
    assert borrar_persona(12345) is False
    borrar_tabla()

if __name__ == '__main__':
    pruebas()
