# Implementar la funcion actualizar_persona, que actualiza un registro de una persona basado en su id.
# Devuelve un booleano en base a si encontro el registro y lo actualizo o no.

import datetime

from ejercicio_01 import *
from ejercicio_02 import agregar_persona
from ejercicio_04 import buscar_persona


def actualizar_persona(id_persona, nombre, nacimiento, dni, altura):
    try:
        mycursor = mydb.cursor()
        mycursor.execute(f"UPDATE `persona` SET `Nombre` = '{nombre}', `FechaNacimiento` = '{nacimiento}', `DNI` = {dni}, `Altura` = {altura} WHERE `persona`.`IdPersona` = {id_persona}")
        mydb.commit()
        query_result = mycursor.fetchone()
        if(mycursor.rowcount > 0):
            return True
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
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    actualizar_persona(id_juan, 'juan carlos perez', datetime.datetime(1988, 4, 16), 32165497, 181)
    assert buscar_persona(id_juan) == (1, 'juan carlos perez', datetime.datetime(1988, 4, 16), 32165497, 181)
    assert actualizar_persona(123, 'nadie', datetime.datetime(1988, 4, 16), 12312312, 181) is False

if __name__ == '__main__':
    pruebas()
