# Implementar la funcion crear_tabla_peso, que cree una tabla PersonaPeso con:
# - IdPersona: Int() (Clave Foranea Persona)
# - Fecha: Date()
# - Peso: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.

from practico_03.ejercicio_01 import borrar_tabla, crear_tabla

import sqlite3


def crear_tabla_peso():
    conn = sqlite3.connect('tabla.db')
    with conn:
        cur = conn.cursor()
        cur.execute('''
         CREATE TABLE IF NOT EXISTS PersonaPeso(
         idPer INTEGER,
         fecha DATE,
         peso INTEGER,
         FOREIGN KEY(idPer) REFERENCES tablaPersona(idPer))
        ''')


def borrar_tabla_peso():
    conn = sqlite3.connect('tabla.db')
    with conn:
        cur = conn.cursor()
        cur.execute('DROP TABLE IF EXISTS PersonaPeso')



# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        crear_tabla_peso()
        func()
        borrar_tabla_peso()
        borrar_tabla()
    return func_wrapper
