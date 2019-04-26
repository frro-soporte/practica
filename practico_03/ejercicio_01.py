# Implementar la funcion crear_tabla, que cree una tabla Persona con:
# - IdPersona: Int() (autoincremental)
# - Nombre: Char(30)
# - FechaNacimiento: Date()
# - DNI: Int()
# - Altura: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.


import pymysql

# Open db
db = pymysql.connect(host='localhost', user='root', password='852456', port=3306, db='Python')
# Crear cursor
cursor = db.cursor()

def crear_tabla():
    cursor.execute("CREATE TABLE Persona(IdPersona int key auto_increment,"
               " Nombre char(30), "
               "FechaNacimiento date,"
               " DNI int,"
               " Altura int)")
    print("Tabla creada")
    db.close()


def borrar_tabla():
    cursor.execute("DROP TABLE Persona")
    print("Tabla borrada")
    db.close()


def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        func()
        borrar_tabla()
    return func_wrapper
