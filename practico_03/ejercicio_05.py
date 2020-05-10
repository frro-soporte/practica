# Implementar la funcion actualizar_persona, que actualiza un registro de una persona basado en su id.
# Devuelve un booleano en base a si encontro el registro y lo actualizo o no.

import datetime
import sqlite3
from practico_03.ejercicio_01 import reset_tabla
from practico_03.ejercicio_02 import agregar_persona
from practico_03.ejercicio_03 import existe_persona
from practico_03.ejercicio_04 import buscar_persona


def actualizar_persona(id_persona, nombre, nacimiento, dni, altura):
   if existe_persona(id_persona):
       conn = sqlite3.connect('DB_TP3.db')
       c = conn.cursor()
       per = c.execute("""
       UPDATE Persona
       SET IdPersona = ?, Nombre = ?, FechaNacimiento = ?, DNI = ?, Altura = ?
       WHERE IdPersona = ?;
       """, (id_persona, nombre, nacimiento, dni, altura, id_persona)).fetchone()
       c.close()
       conn.commit()
       conn.close()
       return per
   else:
       return False


@reset_tabla
def pruebas():
   id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
   actualizar_persona(id_juan, 'juan carlos perez', datetime.datetime(1988, 4, 16), 32165497, 181)
   print(buscar_persona(id_juan))
   #assert buscar_persona(id_juan) == (1, 'juan carlos perez', datetime.datetime(1988, 4, 16), 32165497, 181)
   assert actualizar_persona(123, 'nadie', datetime.datetime(1988, 4, 16), 12312312, 181) is False

if __name__ == '__main__':
   pruebas()
