# Implementar la funcion listar_pesos, que devuelva el historial de pesos para una persona dada.
# Debe validar:
# - que el ID de la persona ingresada existe (reutilizando las funciones ya implementadas).

# Debe devolver:
# - Lista de (fecha, peso), donde fecha esta representado por el siguiente formato: AAAA-MM-DD.
#   Ejemplo:
#   [
#       ('2018-01-01', 80),
#       ('2018-02-01', 85),
#       ('2018-03-01', 87),
#       ('2018-04-01', 84),
#       ('2018-05-01', 82),
#   ]
# - False en caso de no cumplir con alguna validacion.

import datetime
import sqlite3
from practico_03.ejercicio_02 import agregar_persona
from practico_03.ejercicio_03 import existe_persona
from practico_03.ejercicio_06 import reset_tabla
from practico_03.ejercicio_07 import agregar_peso


def listar_pesos(id_persona):
   if not existe_persona(id_persona):
       return False
   if not tiene_registro(id_persona):
       return False
   conn = sqlite3.connect('DB_TP3.db')
   c = conn.cursor()
   pesos = c.execute("""
           SELECT Fecha, Peso FROM tabla_peso
           WHERE IdPersona = ?""", (id_persona,)).fetchall()
   c.close()
   conn.commit()
   conn.close()
   return pesos

def tiene_registro(id_persona):
   conn = sqlite3.connect('DB_TP3.db')
   c = conn.cursor()
   encontrado = c.execute("""SELECT EXISTS(SELECT 1 FROM tabla_peso WHERE IdPersona=?)""", (id_persona,)).fetchone()
   c.close()
   conn.commit()
   conn.close()
   if encontrado[0] == 0:
       print("La persona ingresada no tiene registros")
       return False
   else:
       return True

@reset_tabla
def pruebas():
   id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
   agregar_peso(id_juan, datetime.datetime(2018, 5, 1), 80)
   agregar_peso(id_juan, datetime.datetime(2018, 6, 1), 85)
   pesos_juan = listar_pesos(id_juan)
   pesos_esperados = [
       ('2018-05-01', 80),
       ('2018-06-01', 85),
   ]
   assert pesos_juan == pesos_esperados
   # id incorrecto
   assert listar_pesos(200) == False


if __name__ == '__main__':
   pruebas()
