# Implementar la funcion crear_tabla, que cree una tabla Persona con:
# - IdPersona: Int() (autoincremental)
# - Nombre: Char(30)
# - FechaNacimiento: Date()
# - DNI: Int()
# - Altura: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.

import sqlite3
conn = sqlite3.connect('tabla.db')
cur = conn.cursor()

def crear_tabla():
    conn.execute('''CREATE TABLE IF NOT EXISTS tablaPersona(
 idPer INTEGER PRIMARY KEY AUTOINCREMENT,
 nom TEXT , 
 nac DATE, 
 dni INTEGER, 
 alt INTEGER                        )''')



def borrar_tabla():
    conn.execute('DROP TABLE IF EXISTS tablaPersona')
    pass


# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        func()
        borrar_tabla()
    return func_wrapper

