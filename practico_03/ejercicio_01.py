# Implementar la funcion crear_tabla, que cree una tabla Persona con:
# - IdPersona: Int() (autoincremental)
# - Nombre: Char(30)
# - FechaNacimiento: Date()
# - DNI: Int()
# - Altura: Int()
# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.

import sqlite3 as db


def crear_tabla():
    db_var = db.connect('practico-03.db')
    cursor = db_var.cursor()
    query = "CREATE TABLE IF NOT EXISTS Persona(IdPersona INTEGER PRIMARY KEY ASC, Nombre char(30), FechaNacimiento Date, DNI int, altura int)"
    cursor.execute(query)
    db_var.commit()
    db_var.close()
    pass


def borrar_tabla():
    db_var = db.connect('practico-03.db')
    cursor = db_var.cursor()
    cursor.execute("DROP TABLE IF EXISTS Persona")
    db_var.commit()
    db_var.close()
    pass


# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        func()
        borrar_tabla()
    return func_wrapper

