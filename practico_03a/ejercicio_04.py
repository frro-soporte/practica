# Implementar la funcion buscar_persona, que devuelve el registro de una persona basado en su id.
# El return es una tupla que contiene sus campos: id, nombre, nacimiento, dni y altura.
# Si no encuentra ningun registro, devuelve False.

import datetime

from ejercicio_01 import conexion, reset_tabla, Persona, sessionUsuario
from ejercicio_02 import agregar_persona
from sqlalchemy import exc

def buscar_persona(id):
    try:
        conn = conexion()
        user = sessionUsuario()
        per = user.query(Persona).filter_by(idPersona = id).first()
        if per != None:
            perso = Persona()
            perso.idPersona = per.idPersona
            perso.nombre = per.nombre
            perso.fechaNacimiento = per.fechaNacimiento
            perso.dni = per.dni
            perso.altura = per.altura
            #creo tupla
            p = tuple()
            p = (perso.idPersona, perso.nombre, per.fechaNacimiento, perso.dni, perso.altura)

            return p
        else:
            return False

    except exc.SQLAlchemyError:
        print(exc.SQLAlchemyError.args)
        return False

@reset_tabla
def pruebas():
    juan = buscar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert juan == (1, 'juan perez', datetime.date(1988, 5, 15), 32165498, 180)
                  #[1, 'juan perez', datetime.date(1988, 5, 15), 32165498, 180]
    assert buscar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
