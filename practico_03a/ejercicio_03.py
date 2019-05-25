# Implementar la funcion borrar_persona, que elimina un registro en la tabla Persona.
# Devuelve un booleano en base a si encontro el registro y lo borro o no.

import datetime
from ejercicio_02 import agregar_persona
from ejercicio_01 import conexion, reset_tabla, Persona, sessionUsuario
from sqlalchemy import exc

def borrar_persona(id_per):
    try:
        conn = conexion()
        sessionUser = sessionUsuario()
        #per = sessionUser.query(Persona).get(id_per)
        per = sessionUser.query(Persona).filter_by(idPersona = id_per).first()
        sessionUser.delete(per)
        sessionUser.commit()
        id = sessionUser.query(Persona).filter_by(idPersona = id_per).first()
        if id == None:
            print('persona eliminada')
            return True
        else:
            print('persona no eliminada')
            return False
    except exc.SQLAlchemyError:
        print(exc.SQLAlchemyError.args)
        return False

@reset_tabla
def pruebas():
    assert borrar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert borrar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
