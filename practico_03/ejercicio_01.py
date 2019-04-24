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

    cur = db.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS Persona(id_persona INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT(30), fecha_nac DATETIME, dni INTEGER, altura INTEGER)')

    cur.close()
    db.commit()
    db.close()


def borrar_tabla():
    db = sqlite3.connect('mibase')
    cur = db.cursor()
    cur.execute('DROP TABLE IF EXISTS Persona')
    cur.close()
    db.commit()
    db.close()


# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        func()
        borrar_tabla()
    return func_wrapper

