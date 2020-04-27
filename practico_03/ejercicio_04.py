# Implementar la funcion buscar_persona, que devuelve el registro de una persona basado en su id.
# El return es una tupla que contiene sus campos: id, nombre, nacimiento, dni y altura.
# Si no encuentra ningun registro, devuelve False.

import datetime

from ejercicio_01 import *
from ejercicio_02 import agregar_persona


def buscar_persona(id_persona):
    try:
        mycursor = mydb.cursor()
        mycursor.execute(f"SELECT * FROM `persona` WHERE `persona`.`IdPersona` = {id_persona}")
        myresult = mycursor.fetchall()
        for x in myresult:
            return x
        return False
    except mysql.connector.Error as error:
        print(f"Error al buscar a la persona con id {id_persona}: {error}")
        return False
    finally:
        if (mydb.is_connected()):
            mycursor.close()
        pass


@reset_tabla
def pruebas():
    juan = buscar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert juan == (1, 'juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    assert buscar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
