# Implementar la funcion borrar_persona, que elimina un registro en la tabla Persona.
# Devuelve un booleano en base a si encontro el registro y lo borro o no.

import datetime
import pymysql
db = pymysql.connect(host='localhost', user='root', password='852456', port=3306, db='Python')
cursor = db.cursor()
from practico_03.ejercicio_01 import reset_tabla
from practico_03.ejercicio_02 import agregar_persona


def borrar_persona(id_persona):
    x=cursor.execute("DELETE FROM Persona WHERE IdPersona = %s",id_persona)
    db.commit()
    if x==0:
        return False
    else:
        return True


@reset_tabla
def pruebas():
    assert borrar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert borrar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
