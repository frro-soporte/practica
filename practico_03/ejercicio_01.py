# Implementar la funcion crear_tabla, que cree una tabla Persona con:
# - IdPersona: Int() (autoincremental)
# - Nombre: Char(30)
# - FechaNacimiento: Date()
# - DNI: Int()
# - Altura: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.

import sqlite3

def conexion ():
    db = sqlite3.connect('C:\\Users\\Nahuel\\Desktop\\db_python.db')
    return db

def crear_tabla():
    con = conexion()
    c = con.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS "Persona"(
                            idPersona INTEGER PRIMARY KEY AUTOINCREMENT ,
                            nombre char(30),
                            fechaNacimiento DATETIME,
                            dni int,
                            altura int
                        );""")
    c.close()
    con.commit()
    con.close()

def borrar_tabla():
    con = conexion()
    c = con.cursor()

    c.execute("DROP TABLE Persona")

    c.close()
    con.commit()
    con.close()

    pass


# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        func()
        borrar_tabla()

    return func_wrapper
