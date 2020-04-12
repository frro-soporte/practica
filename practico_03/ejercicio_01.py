# Implementar la funcion crear_tabla, que cree una tabla Persona con:
# - IdPersona: Int() (autoincremental)
# - Nombre: Char(30)
# - FechaNacimiento: Date()
# - DNI: Int()
# - Altura: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.

import sqlite3


def crear_tabla():
    db = sqlite3.connect('mibase')
    cursor = db.cursor()
    cSQL = 'CREATE TABLE IF NOT EXISTS Persona(IdPersona INTEGER PRIMARY KEY ASC, Nombre char(30), FechaNacimiento Date, DNI int, altura int)'
    cursor.execute(cSQL)
    db.commit()
    db.close()


def borrar_tabla():
    db = sqlite3.connect('mibase')
    curs = db.cursor()
    curs.execute("DROP TABLE IF EXISTS Persona")
    db.commit()
    db.close()


# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        func()
        borrar_tabla()
    return func_wrapper

