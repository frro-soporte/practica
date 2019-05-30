# Implementar la funcion actualizar_persona, que actualiza un registro de una persona basado en su id.
# Devuelve un booleano en base a si encontro el registro y lo actualizo o no.

import sqlalchemy
import datetime

from ejercicio_01 import session, crear_tabla, borrar_tabla, Persona, session
from ejercicio_02 import agregar_persona
from ejercicio_04 import buscar_persona


def actualizar_persona(id_persona, nombre, nacimiento, dni, altura):
    per = session.query(Persona).filter(Persona.id == id_persona).first()
    if per is None:
        return False
    else: 
        per.nombre = nombre
        per.dni = dni
        per.fechaNacimiento = nacimiento
        per.altura = altura
        #solo para probar que anda
        p = ()
        p = (per.id, per.nombre, per.fechaNacimiento, per.dni, per.altura)
        print(p)
        session.commit()
        return True



#@reset_tabla
def pruebas():
    crear_tabla()
    id_juan = agregar_persona('juan perez', datetime.date(1988, 5, 15), 32165498, 180)
    print ("id ", id_juan)
    actualizar_persona(id_juan, 'juan carlos perez', datetime.date(1988, 4, 16), 32165497, 181)
    assert buscar_persona(id_juan) == (1, 'juan carlos perez', datetime.date(1988, 4, 16), 32165497, 181)
    assert actualizar_persona(123, 'nadie', datetime.date(1988, 4, 16), 12312312, 181) is False
    borrar_tabla()

if __name__ == '__main__':
    pruebas()
