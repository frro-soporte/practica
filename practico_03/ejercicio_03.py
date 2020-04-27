# Implementar la funcion borrar_persona, que elimina un registro en la tabla Persona.
# Devuelve un booleano en base a si encontro el registro y lo borro o no.

import datetime

from ejercicio_01 import reset_tabla, mysql, mydb, mycursor
from ejercicio_02 import agregar_persona


def borrar_persona(id_persona):
    try:
        mycursor = mydb.cursor()
        mycursor.execute(f"DELETE FROM `persona` WHERE `persona`.`IdPersona` = {id_persona}")
        mydb.commit()
        query_result = mycursor.fetchone()
        if(mycursor.rowcount > 0):
            return True
        return False
    except mysql.connector.Error as error:
        print(f"Error al eliminar a la persona con id {id_persona}: {error}")
        return False
    finally:
        if (mydb.is_connected()):
            mycursor.close()
        pass


@reset_tabla
def pruebas():
    assert borrar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert borrar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
