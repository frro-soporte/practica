# Implementar la funcion actualizar_persona, que actualiza un registro de una persona basado en su id.
# Devuelve un booleano en base a si encontro el registro y lo actualizo o no.

from ejercicio_01 import reset_tabla, Persona
from ejercicio_02 import agregar_persona
from ejercicio_04 import buscar_persona
from sqlalchemy import update
import datetime


def actualizar_persona(id_persona, nombre, nacimiento, dni, altura,session):
    #list = session.query(Persona).filter(Persona.idPer == id_persona).first()
    obj = buscar_persona(id_persona,session)
    if obj is False:
        return False
    else:
        act = update(Persona).where(Persona.idPer == id_persona).values(nom=nombre,fec=nacimiento, dni=dni, alt=altura)
        session.execute(act)
        session.commit()
        print(obj)


@reset_tabla
def pruebas(session):
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180,session)
    actualizar_persona(id_juan, 'juan carlos perez', datetime.datetime(1988, 4, 16), 32165497, 181,session)
    assert buscar_persona(id_juan,session) == (1, 'juan carlos perez', datetime.date(1988, 4, 16), 32165497, 181)
    assert actualizar_persona(123, 'nadie', datetime.datetime(1988, 4, 16), 12312312, 181,session) is False

if __name__ == '__main__':
    pruebas()

