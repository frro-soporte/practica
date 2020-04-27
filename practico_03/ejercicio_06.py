# Implementar la funcion crear_tabla_peso, que cree una tabla PersonaPeso con:
# - IdPersona: Int() (Clave Foranea Persona)
# - Fecha: Date()
# - Peso: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.

from ejercicio_01 import *


def crear_tabla_peso():
    try:
        mycursor.execute("CREATE TABLE `soporte`.`PersonaPeso` ( `IdPersonaPeso` INT NOT NULL AUTO_INCREMENT, `IdPersona` INT NOT NULL , `Fecha` DATE NOT NULL , `Peso` INT NOT NULL , PRIMARY KEY (`IdPersonaPeso`), FOREIGN KEY (`IdPersona`) REFERENCES Persona(`IdPersona`))")
        mydb.commit()
    except mysql.connector.Error as error:
        print("Error al crear tabla PersonaPeso: {}".format(error))


def borrar_tabla_peso():
    try:
        mycursor.execute("DROP TABLE `PersonaPeso`")
        mydb.commit()
    except mysql.connector.Error as error:
        print("Error al borrar tabla PersonaPeso: {}".format(error))

# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        crear_tabla_peso()
        func()
        borrar_tabla_peso()
        borrar_tabla()
    return func_wrapper
