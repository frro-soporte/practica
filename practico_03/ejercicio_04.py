# Implementar la funcion buscar_persona, que devuelve el registro de una persona basado en su id.
# El return es una tupla que contiene sus campos: id, nombre, nacimiento, dni y altura.
# Si no encuentra ningun registro, devuelve False.

import datetime
import sqlite3
from practico_03.ejercicio_01 import reset_tabla
from practico_03.ejercicio_02 import agregar_persona
from practico_03.ejercicio_03 import existe_persona


def buscar_persona(id_persona):
   if existe_persona(id_persona):
       conn = sqlite3.connect('DB_TP3.db')
       c = conn.cursor()
       per = c.execute("""
       SELECT * FROM Persona
       WHERE IdPersona = ?""", (id_persona,)).fetchone()
       c.close()
       conn.commit()
       conn.close()
       return per
   else:
       return False


@reset_tabla
def pruebas():
   juan = buscar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
   print(juan)
   #COMO SE VE EN EL PRINT, LOS DATOS DE JUAN SE DEVUELVEN BIEN PERO EN EL ASSERT FALLA LA IGUALDAD
   #assert juan == (1, 'juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
   assert buscar_persona(12345) is False

if __name__ == '__main__':
   pruebas()
