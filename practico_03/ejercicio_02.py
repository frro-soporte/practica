# Implementar la funcion agregar_persona, que inserte un registro en la tabla Persona
# y devuelva los datos ingresados el id del nuevo registro.

import datetime

from ejercicio_01 import *

def agregar_persona(nombre, nacimiento, dni, altura):
    try:
        mycursor = mydb.cursor()
        mycursor.execute(f"INSERT INTO `persona` (`IdPersona`, `Nombre`, `FechaNacimiento`, `DNI`, `Altura`) VALUES (NULL, '{nombre}', '{nacimiento}', '{dni}', '{altura}')")
        mydb.commit()
        query_result = mycursor.fetchone()
    except mysql.connector.Error as error:
        print("Error al registrar persona: {}".format(error))
    else:
        return mycursor.lastrowid
    finally:
        if (mydb.is_connected()):
            mycursor.close()
        pass



"""def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    print(id_juan)
    id_marcela = agregar_persona('marcela gonzalez', datetime.datetime(1980, 1, 25), 12164492, 195)
    print(id_marcela)
    pass

pruebas()"""
