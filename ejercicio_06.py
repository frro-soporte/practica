# Implementar la funcion crear_tabla_peso, que cree una tabla PersonaPeso con:
# - IdPersona: Int() (Clave Foranea Persona)
# - Fecha: Date()
# - Peso: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.

from ejercicio_01 import borrar_tabla, crear_tabla
import sqlite3

db = sqlite3.connect('D:\\prueba.db')
cur = db.cursor()


def crear_tabla_peso():
    cSQL = 'create table if not exists PersonaPeso(idPeso INTEGER PRIMARY KEY ASC,idPersona INTEGER, fecha DATE, peso INTEGER, FOREIGN KEY(idPersona) REFERENCES Persona(idPersona))'
    cur.execute(cSQL)
    db.commit()
    return 0


def borrar_tabla_peso():
    cSQL = 'drop table if exists PersonaPeso'
    cur.execute(cSQL)
    db.commit()


# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        crear_tabla_peso()
        func()
        borrar_tabla_peso()
        borrar_tabla()
    return func_wrapper
