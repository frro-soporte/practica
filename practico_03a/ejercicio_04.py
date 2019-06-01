# Implementar la funcion buscar_persona, que devuelve el registro de una persona basado en su id.
# El return es una tupla que contiene sus campos: id, nombre, nacimiento, dni y altura.
# Si no encuentra ningun registro, devuelve False.

import datetime

from ejercicio_01 import conexion, reset_tabla, Persona, sessionUsuario
from ejercicio_02 import agregar_persona
from sqlalchemy import exc

def buscar_persona(id):
    try:
        conexion()
        user = sessionUsuario()
        select = user.query(Persona).filter(Persona.idPersona == id).all()

        if select:
            p = select[0]
            return(p.idPersona,p.nombre,p.fechaNacimiento,p.dni,p.altura)
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
