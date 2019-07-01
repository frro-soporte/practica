
# Implementar la funcion crear_tabla_peso, que cree una tabla PersonaPeso con:
# - IdPersona: Int() (Clave Foranea Persona)
# - Fecha: Date()
# - Peso: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.

from practico_03.ejercicio_01 import borrar_tabla, crear_tabla
import sqlite3

def crear_tabla_peso():
    db = sqlite3.connect('persona_db.sqlite')

    cursor = db.cursor()
    cSQL = 'CREATE TABLE IF NOT EXISTS persona_peso(id_peso INTEGER PRIMARY KEY ASC,' \
           'id_persona INT ,' \
           'fecha_pesaje DATE, ' \
           'peso INT, ' \
           'FOREIGN KEY(id_persona) REFERENCES persona(id_persona))'
    cursor.execute(cSQL)
    db.commit()



def borrar_tabla_peso():
    db = sqlite3.connect('persona_db.sqlite')
    cursor = db.cursor()
    cSQL = 'DROP TABLE IF EXISTS persona_peso'
    cursor.execute(cSQL)
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