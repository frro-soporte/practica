# Implementar la funcion crear_tabla_peso, que cree una tabla PersonaPeso con:
# - IdPersona: Int() (Clave Foranea Persona)
# - Fecha: Date()
# - Peso: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.

from practico_03.ejercicio_01 import borrar_tabla, crear_tabla
from practico_03.ejercicio_01 import conexion


def crear_tabla_peso():
    con = conexion()
    c = con.cursor()
    c.execute(
    """
    CREATE TABLE IF NOT EXISTS "PersonaPeso"(
        idPersona INTEGER,
        fecha DATETIME NULL,
        peso INTEGER NULL,
        FOREIGN KEY(idPersona) REFERENCES Persona(idPersona)
        
    );
    """)
    c.close()
    con.commit()
    con.close()


def borrar_tabla_peso():
    con = conexion()
    c = con.cursor()
    c.execute("DROP TABLE PersonaPeso ")
    c.close()
    con.commit()
    con.close()


# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        crear_tabla_peso()
        func()
        borrar_tabla_peso()
        borrar_tabla()
    return func_wrapper
