# Implementar la funcion buscar_persona, que devuelve el registro de una persona basado en su id.
# El return es una tupla que contiene sus campos: id, nombre, nacimiento, dni y altura.
# Si no encuentra ningun registro, devuelve False.

import sqlalchemy
import datetime
import sqlalchemy

from ejercicio_01 import Persona, session, crear_tabla, borrar_tabla
from ejercicio_02 import agregar_persona


def buscar_persona(id_persona):
    per = session.query(Persona).filter(Persona.id == id_persona).first()
    if per is None:
        return False
    else:
        pers = ()
        pers = (per.id, per.nombre, per.fechaNacimiento, per.dni, per.altura)
        return pers


#@reset_tabla
def pruebas():
    crear_tabla()
    juan = buscar_persona(agregar_persona('juan perez', datetime.date(1988, 5, 15), 32165498, 180))
    assert juan == (1, 'juan perez', datetime.date(1988, 5, 15), 32165498, 180)
    assert buscar_persona(12345) is False
    borrar_tabla()

    

if __name__ == '__main__':
    pruebas()
