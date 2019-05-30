# Implementar la funcion buscar_persona, que devuelve el registro de una persona basado en su id.
# El return es una tupla que contiene sus campos: id, nombre, nacimiento, dni y altura.
# Si no encuentra ningun registro, devuelve False.

from ejercicio_01 import reset_tabla, Persona
from ejercicio_02 import agregar_persona
import datetime

def buscar_persona(id_persona,session):
    obj = session.query(Persona).filter(Persona.idPer == id_persona).first()
    if obj == None:
        return False
    else:
        list= (obj.idPer, obj.nom, obj.fec, obj.dni, obj.alt)
        return list

@reset_tabla
def pruebas(session):
    juan = buscar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180,session),session)
    print(juan)
    assert juan == (1, 'juan perez', datetime.date(1988, 5, 15), 32165498, 180)
    assert buscar_persona(12345,session) is False


if __name__ == '__main__':

    pruebas()
