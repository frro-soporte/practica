# Implementar la funcion crear_tabla, que cree una tabla Persona con:
# - IdPersona: Int() (autoincremental)
# - Nombre: Char(30)
# - FechaNacimiento: Date()
# - DNI: Int()
# - Altura: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.

import mysql.connector

def conexion():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="Pruebas-Python"
    )
    return mydb


def crear_tabla():
    conn = conexion()
    mycursor = conn.cursor()
    sql = (
        """
        CREATE TABLE Persona (IdPersona int(11) NOT NULL auto_increment primary key,
        Nombre char(30),
        FechaNacimiemto date,
        DNI int(8),
        Altura int(3))"""
    )
    mycursor.execute(sql)
    print('creacion de tabla con exito')

def borrar_tabla():
    conn = conexion()
    mycursor = conn.cursor()
    sql = ("drop table Persona")
    mycursor.execute(sql)
    print('eliminacion de tabla con exito')


# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        func()
        borrar_tabla()
    return func_wrapper
