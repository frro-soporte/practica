# Implementar la funcion crear_tabla_peso, que cree una tabla PersonaPeso con:
# - IdPersona: Int() (Clave Foranea Persona)
# - Fecha: Date()
# - Peso: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.

from ejercicio_01 import borrar_tabla, crear_tabla , conexion

def crear_tabla_peso(idpersona,fecha,peso):
    sqlconn = conexion()
    cursor = sqlconn.cursor()
    strsqlcreate = "CREATE TABLE IF NOT EXISTS PersonaxPeso (ID_pesaje INTEGER PRIMARY KEY AUTOINCREMENT , \ ID_persona INTEGER , \ fecha DATETIME NULL ,\ peso FLOAT NULL , CONSTRAINT FK_PersonasPersonaxKilo FOREING KEY(id_Persona) \ REFERENCES persona(ID_Persona) )"
    cursor.execute(strsqlcreate)
    cursor.commit()
    cursor.close()
    sqlconn.close()

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
