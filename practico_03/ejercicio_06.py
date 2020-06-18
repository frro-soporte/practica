# Implementar la funcion crear_tabla_peso, que cree una tabla PersonaPeso con:
# - IdPersona: Int() (Clave Foranea Persona)
# - Fecha: Date()
# - Peso: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.

import mysql
from practico_03.ejercicio_01 import borrar_tabla, crear_tabla


def crear_tabla_peso():
    connection = mysql.connector.connect(user="root", password="root", host="localhost", database="soportebd")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE `soportebd`.`persona_peso` (`IdPersona` INT NOT NULL,`Peso` INT NULL,`Fecha` DATETIME NOT NULL,PRIMARY KEY (`IdPersona`, `Fecha`),CONSTRAINT `IdPersona`FOREIGN KEY (`IdPersona`)REFERENCES `soportebd`.`persona` (`IdPersona`))")


def borrar_tabla_peso():
    connection = mysql.connector.connect(user="root", password="root", host="localhost", database="soportebd")
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS persona_peso")


# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        crear_tabla_peso()
        func()
        borrar_tabla_peso()
        borrar_tabla()
    return func_wrapper

