# Implementar la funcion agregar_peso, que inserte un registro en la tabla PersonaPeso.
# Debe validar:
# - que el ID de la persona ingresada existe (reutilizando las funciones ya implementadas).
# - que no existe de esa persona un registro de fecha posterior al que queremos ingresar.

# Debe devolver:
# - ID del peso registrado.
# - False en caso de no cumplir con alguna validacion.

import datetime
import sqlite3
from practico_03.ejercicio_02 import agregar_persona
from practico_03.ejercicio_03 import existe_persona
from practico_03.ejercicio_06 import reset_tabla


def agregar_peso(id_persona, fecha, peso):
   if not existe_persona(id_persona):
       return False
   else:
       if buscar_registro(id_persona, fecha):
           conn = sqlite3.connect('DB_TP3.db')
           c = conn.cursor()
           info = (id_persona,
                   datetime.datetime.strftime(fecha, '%Y-%m-%d'),
                   peso)
           c.execute("""
                   INSERT INTO tabla_peso (
                       IdPersona,
                       Fecha,
                       Peso)
                   VALUES ( ?, ?, ?)
                       """, (info))
           ultId = c.lastrowid
           c.close()
           conn.commit()
           conn.close()
           return ultId
       else:
           return False

def buscar_registro(id_persona, fecha):
   conn = sqlite3.connect('DB_TP3.db')
   c = conn.cursor()
   #BUSCO SI HAY UN REGISTRO MAS NUEVO
   encontrado = c.execute(
       """SELECT EXISTS(
       SELECT 1 FROM tabla_peso
       WHERE IdPersona=? AND Fecha<?
       )""", (id_persona, fecha)).fetchone()
   #BUSCO SI NO HAY REGISTRO
   encontrado2 = c.execute(
       """SELECT NOT EXISTS(
       SELECT 1 FROM tabla_peso
       WHERE IdPersona=?
       )""", (id_persona, )).fetchone()
   c.close()
   conn.commit()
   conn.close()
   if encontrado[0] == 0 and encontrado2[0] == 0:
       print("La persona posee un registro mas nuevo que el que se intenta ingresar")
       return False
   else:
       return True

@reset_tabla

def pruebas():
   id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
   assert agregar_peso(id_juan, datetime.datetime(2018, 5, 26), 80) > 0
   # id incorrecto
   assert agregar_peso(200, datetime.datetime(1988, 5, 15), 80) == False
   # registro previo al 2018-05-26
   assert agregar_peso(id_juan, datetime.datetime(2018, 5, 16), 80) == False

if __name__ == '__main__':

   pruebas()
