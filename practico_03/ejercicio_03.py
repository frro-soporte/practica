# Implementar la funcion borrar_persona, que elimina un registro en la tabla Persona.
# Devuelve un booleano en base a si encontro el registro y lo borro o no.

import datetime
import sqlite3
from practico_03.ejercicio_01 import reset_tabla
from practico_03.ejercicio_02 import agregar_persona


def borrar_persona(id_persona):
   if existe_persona(id_persona) == True:
       conn = sqlite3.connect('DB_TP3.db')
       c = conn.cursor()
       c.execute("""DELETE FROM Persona WHERE IdPersona = ?""", (id_persona,))
       c.close()
       conn.commit()
       print("Persona eliminada correctamente")
       conn.close()
       return True
   else:
       return False

def existe_persona(id_persona):
   conn = sqlite3.connect('DB_TP3.db')
   c = conn.cursor()
   encontrado = c.execute("""SELECT EXISTS(SELECT 1 FROM Persona WHERE IdPersona=?)""", (id_persona,)).fetchone()
   #encontrado[0] contiene el primer valor de la tupla encontrado. Es 1 si encuentra y 0 si no encuentra.
   c.close()
   conn.commit()
   conn.close()
   if encontrado[0] == 0:
       print("No existe la persona ingresada")
       return False
   else:
       return True

@reset_tabla
def pruebas():
   assert borrar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
   assert borrar_persona(12345) is False

if __name__ == '__main__':
   pruebas()
