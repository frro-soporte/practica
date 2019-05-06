# Implementar la funcion actualizar_persona, que actualiza un registro de una persona basado en su id.
# Devuelve un booleano en base a si encontro el registro y lo actualizo o no.

from practico_03A.ejercicio_01 import reset_tabla, Persona
from practico_03A.ejercicio_02 import agregar_persona
from practico_03A.ejercicio_04 import buscar_persona
import datetime


def actualizar_persona(id_persona, nombre, nacimiento, dni, altura,session):
    #Aca ya tengo id_persona, entonces solo tengo que hacer un update
    #el problema del id venia de la mano con el datetime

    lp = session.query(Persona).filter(Persona.id_persona == id_persona).first()
    if lp == None:
        return False
    else:
        lp.nombre = nombre
        lp.fecha_nac = nacimiento
        lp.dni = dni
        lp.altura = altura
        session.commit()
        print(lp.nombre, lp.fecha_nac, lp.dni, lp.altura)
        return True






@reset_tabla
def pruebas(session):
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180,session)
    actualizar_persona(id_juan, 'juan carlos perez', datetime.datetime(1988, 4, 16), 32165497, 181,session)
    assert buscar_persona(id_juan,session) == (1, 'juan carlos perez', datetime.datetime(1988, 4, 16), 32165497, 181)
    #assert buscar_persona(id_juan) == (1, 'juan carlos perez', '1988-04-16 00:00:00', 32165497, 181)
    assert actualizar_persona(123, 'nadie', datetime.datetime(1988, 4, 16), 12312312, 181,session) is False

if __name__ == '__main__':

    pruebas()
