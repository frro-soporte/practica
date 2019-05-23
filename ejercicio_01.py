# Implementar la funcion crear_tabla, que cree una tabla Persona con:
# - IdPersona: Int() (autoincremental)
# - Nombre: Char(30)
# - FechaNacimiento: Date()
# - DNI: Int()
# - Altura: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.

import sqlite3

db = sqlite3.connect("D:\\prueba.db")
cur = db.cursor()


def crear_tabla():
    cSQL = 'CREATE TABLE IF NOT EXISTS Persona(idPersona INTEGER PRIMARY KEY ASC, nombre TEXT(30) , fechaNacimiento DATE, dni INTEGER, altura FLOAT)'
    cur.execute(cSQL)
    db.commit()
    return 0


def borrar_tabla():
    cSQL = 'DROP TABLE IF EXISTS Persona'
    cur.execute(cSQL)
    db.commit()


# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        func()
        borrar_tabla()

    return func_wrapper
