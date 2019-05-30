# Implementar la funcion crear_tabla, que cree una tabla Persona con:
# - IdPersona: Int() (autoincremental)
# - Nombre: Char(30)
# - FechaNacimiento: Date()
# - DNI: Int()
# - Altura: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.
import sqlite3



def crear_tabla():
    db = sqlite3.connect('persona_db.sqlite')
    cursor = db.cursor()
    cSQL = 'CREATE TABLE IF NOT EXISTS persona(id_persona INTEGER PRIMARY KEY ASC AUTOINCREMENT,' \
           'nombre TEXT(30),' \
           'fecha_nacimiento timestamp, ' \
           'dni INT, ' \
           'altura INT)'
    cursor.execute(cSQL)
    db.commit()


def borrar_tabla():
    db = sqlite3.connect('persona_db.sqlite')
    cursor = db.cursor()
    cSQL = 'DROP TABLE IF EXISTS persona'
    cursor.execute(cSQL)
    db.commit()
    db.close()


# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        #Corre la funcion con la tabla que creamos
        func()
        #Luego de finalizar la funcion elimina la tabla
        borrar_tabla()
    return func_wrapper


