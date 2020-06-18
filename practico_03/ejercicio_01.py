# Implementar la funcion crear_tabla, que cree una tabla Persona con:
# - IdPersona: Int() (autoincremental)
# - Nombre: Char(30)
# - FechaNacimiento: Date()
# - DNI: Int()
# - Altura: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.
import mysql.connector


def crear_tabla():
    connection = mysql.connector.connect(user="root", password="root", host="localhost", database = "soportebd")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS persona (IdPersona INT AUTO_INCREMENT PRIMARY KEY, Nombre VARCHAR(30), FechaNacimiento DATETIME, DNI INT, Altura DECIMAL)")


def borrar_tabla():
    connection = mysql.connector.connect(user="root", password="root", host="localhost", database = "soportebd")
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS persona")


# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        func()
        borrar_tabla()
    return func_wrapper

