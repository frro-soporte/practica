# Implementar la funcion crear_tabla_peso, que cree una tabla PersonaPeso con:
# - IdPersona: Int() (Clave Foranea Persona)
# - Fecha: Date()
# - Peso: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.

import sqlite3
from practico_03.ejercicio_01 import borrar_tabla, crear_tabla

conn = sqlite3.connect('tabla.db')
cur = conn.cursor()

def crear_tabla_peso():
    cur.execute('CREATE TABLE IF NOT EXISTS personaPeso(idPersona INTEGER, fecha DATE, peso INT, FOREIGN KEY(idPersona) REFERENCES tablaPersona(idPersona))')

def borrar_tabla_peso():
    cur.execute('DROP TABLE IF EXISTS personaPeso')

# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        crear_tabla_peso()
        func()
        borrar_tabla_peso()
        borrar_tabla()
    return func_wrapper
