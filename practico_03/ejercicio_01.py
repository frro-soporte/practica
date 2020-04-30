# Implementar la funcion crear_tabla, que cree una tabla Persona con:
# - IdPersona: Int() (autoincremental)
# - Nombre: Char(30)
# - FechaNacimiento: Date()
# - DNI: Int()
# - Altura: Int()
 
# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.
 
import sqlite3
 
def crear_tabla():
   conn = sqlite3.connect('DB_TP3.db')
   c = conn.cursor()
   c.execute(
       """CREATE TABLE IF NOT EXISTS Persona(
       IdPersona INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
       Nombre TEXT,
       FechaNacimiento DATE,
       DNI INT,
       Altura INT) """)
   c.close()
   conn.commit()
   conn.close()
 
 
def borrar_tabla():
   conn = sqlite3.connect('DB_TP3.db')
   c = conn.cursor()
   c.execute("DROP TABLE IF EXISTS Persona")
   c.close()
   conn.commit()
   conn.close()
 
# no modificar
def reset_tabla(func):
   def func_wrapper():
       crear_tabla()
       func()
       borrar_tabla()
 
   return func_wrapper
 
crear_tabla()
borrar_tabla()
