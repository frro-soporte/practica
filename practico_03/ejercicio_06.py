# Implementar la funcion crear_tabla_peso, que cree una tabla PersonaPeso con:
# - IdPersona: Int() (Clave Foranea Persona)
# - Fecha: Date()
# - Peso: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.

import sqlite3
from ejercicio_01 import borrar_tabla, crear_tabla


def crear_tabla_peso():
    db = sqlite3.connect('mibase')
    cursor = db.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS PersonaPeso (IdPersona INT, Fecha Date, Peso int, foreign key(IdPersona) references Persona(IdPersona))')
    db.commit()
    db.close()


def borrar_tabla_peso():
    db = sqlite3.connect('mibase')
    curs = db.cursor()
    curs.execute("DROP TABLE IF EXISTS PersonaPeso")
    db.commit()
    db.close()


# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        crear_tabla_peso()
        func()
        borrar_tabla_peso()
        borrar_tabla()
    return func_wrapper
