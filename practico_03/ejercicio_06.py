# Implementar la funcion crear_tabla_peso, que cree una tabla PersonaPeso con:
# - IdPersona: Int() (Clave Foranea Persona)
# - Fecha: Date()
# - Peso: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.
import pymysql
db = pymysql.connect(host='localhost', user='root', password='852456', port=3306, db='Python')
cursor = db.cursor()
from practico_03.ejercicio_01 import borrar_tabla, crear_tabla


def crear_tabla_peso():
    cursor.execute("CREATE TABLE `personapeso` (`IdPersona` int(11) NOT NULL,"
                   " `Fecha` date DEFAULT NULL,"
                   "`Peso` int(11) DEFAULT NULL,"
                   "KEY `IdPersona_idx` (`IdPersona`),"
                   "CONSTRAINT `IdPersona` FOREIGN KEY (`IdPersona`) REFERENCES `persona` (`IdPersona`)"
                   " ON DELETE NO ACTION ON UPDATE NO ACTION)")
    print("Tabla creada")
    db.close()


def borrar_tabla_peso():
     cursor.execute("DROP TABLE PersonaPeso")
     print("Tabla borrada")
     db.close()


# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        crear_tabla_peso()
        func()
        borrar_tabla_peso()
        borrar_tabla()
    return func_wrapper
