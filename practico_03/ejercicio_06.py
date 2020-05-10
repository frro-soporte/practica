# Implementar la funcion crear_tabla_peso, que cree una tabla PersonaPeso con:
# - IdPersona: Int() (Clave Foranea Persona)
# - Fecha: Date()
# - Peso: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.

import sqlite3
from practico_03.ejercicio_01 import borrar_tabla, crear_tabla

def crear_tabla_peso():
   conn = sqlite3.connect('DB_TP3.db')
   c = conn.cursor()
   c.execute(
       """CREATE TABLE IF NOT EXISTS tabla_peso(
       Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
       IdPersona INT,
       Fecha DATE,
       Peso INT,
       FOREIGN KEY (IdPersona) REFERENCES Persona(IdPersona)) """)
   c.close()
   conn.commit()
   conn.close()

def borrar_tabla_peso():
   conn = sqlite3.connect('DB_TP3.db')
   c = conn.cursor()
   c.execute("DROP TABLE IF EXISTS tabla_peso")
   c.close()
   conn.commit()
   conn.close()

# no modificar
def reset_tabla(func):
   def func_wrapper():
       crear_tabla()
       crear_tabla_peso()
       func()
       borrar_tabla_peso()
       borrar_tabla()
   return func_wrapper

crear_tabla_peso()
