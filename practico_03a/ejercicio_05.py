# Implementar la funcion actualizar_persona, que actualiza un registro de una persona basado en su id.
# Devuelve un booleano en base a si encontro el registro y lo actualizo o no.

import datetime
from sqlalchemy import exc
from ejercicio_01 import conexion, reset_tabla, Persona, sessionUsuario
from ejercicio_02 import agregar_persona
from ejercicio_04 import buscar_persona


def actualizar_persona(id_persona, nombre, nacimiento, dni, altura):

    if (buscar_persona(id_persona) == False):
        return False
    else:
            try:
                sqlconn = conexion()
                user = sessionUsuario()
                per = Persona
                per = user.query(Persona).filter_by(idPersona = id_persona).first()
                per.idPersona = id_persona
                per.nombre = nombre
                per.fechaNacimiento = nacimiento
                per.dni = dni
                per.altura = altura
                user.commit()
                return True
            except exc.SQLAlchemyError:
                return False



@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    actualizar_persona(id_juan, 'juan carlos perez', datetime.date(1988, 4, 16), 32165497, 181)
    assert buscar_persona(id_juan) == (1, 'juan carlos perez', datetime.date(1988, 4, 16), 32165497, 181)
    assert actualizar_persona(123, 'nadie', datetime.date(1988, 4, 16), 12312312, 181) is False

if __name__ == '__main__':
    pruebas()
