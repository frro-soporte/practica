import sqlite3

conn = sqlite3.connect('tabla.db')
cur = conn.cursor()

def crear_tabla():
    cur.execute('CREATE TABLE IF NOT EXISTS tablaPersona(idPersona INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, fechaNacimiento DATE, dni INT, altura INT)')

def borrar_tabla():
    cur.execute('DROP TABLE IF EXISTS tablaPersona')

def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        func()
        borrar_tabla()
    return func_wrapper
