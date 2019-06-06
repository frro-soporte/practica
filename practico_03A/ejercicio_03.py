# Implementar la funcion borrar_persona, que elimina un registro en la tabla Persona.
# Devuelve un booleano en base a si encontro el registro y lo borro o no.



from ejercicio_01 import reset_tabla, Persona
from ejercicio_02 import agregar_persona
import datetime
from sqlalchemy.ext.declarative import declarative_base

def borrar_persona(id_persona, session):
    obj = session.query(Persona).filter(Persona.idPer == id_persona).first()
    if obj == None:
        return False
    else:
        session.delete(obj)
        session.commit()
        return True


@reset_tabla
def pruebas(session):
    assert borrar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180, session),session)
    assert borrar_persona(12345, session) is False

if __name__ == '__main__':

    pruebas()
