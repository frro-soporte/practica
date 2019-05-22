# Implementar la funcion crear_tabla_peso, que cree una tabla PersonaPeso con:
# - IdPersona: Int() (Clave Foranea Persona)
# - Fecha: Date()
# - Peso: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.

from ejercicio_01 import borrar_tabla, crear_tabla , conexion
import mysql.connector

def crear_tabla_peso():
    conn = conexion()
    mycursor = conn.cursor()
    sql = """
     CREATE TABLE `PersonaPeso` (
  `IdPersona` int(11),
  `Fecha` date,
  `Peso` int(11),  
  CONSTRAINT `PersonaPeso_persona_fk` 
  FOREIGN KEY (`IdPersona`) REFERENCES `persona` (`IdPersona`) ON UPDATE CASCADE
)
    """
    mycursor.execute(sql)
    print('creacion de tabla con exito')

def borrar_tabla_peso():
    sqlconn = conexion()
    cursor = sqlconn.cursor()
    strsqldrop = "DROP TABLE PersonaPeso"
    cursor.execute(strsqldrop)
    sqlconn.commit()
    cursor.close()
    sqlconn.close()

# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        crear_tabla_peso()
        func()
        borrar_tabla_peso()
        borrar_tabla()
    return func_wrapper
