# Implementar la funcion crear_tabla_peso, que cree una tabla PersonaPeso con:
# - IdPersona: Int() (Clave Foranea Persona)
# - Fecha: Date()
# - Peso: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.
import pymysql

from practico_03.ejercicio_01 import borrar_tabla, crear_tabla


def crear_tabla_peso():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='lalo123',
        db='Soportetp3')
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS`soportetp3`.`PersonaPeso` (`IdPersona` INT NOT NULL,"
                   "`Fecha` DATE NOT NULL, `Peso` INT NOT NULL, PRIMARY KEY (`IdPersona`, `Fecha`),"
                   "CONSTRAINT `Peso_Persona`"
                   "FOREIGN KEY (`IdPersona`)"
                   "REFERENCES `soportetp3`.`persona` (`idPersona`)ON DELETE NO ACTION ON UPDATE NO ACTION);")
    connection.commit()
    cursor.close()
    connection.close()


def borrar_tabla_peso():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='lalo123',
        db='Soportetp3')
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS PersonaPeso")
    connection.commit()
    cursor.close()
    connection.close()


# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        crear_tabla_peso()
        func()
        borrar_tabla_peso()
        borrar_tabla()

    return func_wrapper
