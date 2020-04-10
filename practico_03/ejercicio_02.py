# Implementar la funcion agregar_persona, que inserte un registro en la tabla Persona
# y devuelva los datos ingresados el id del nuevo registro.

import datetime

from ejercicio_01 import reset_tabla, df

def agregar_persona(nombre, nacimiento, dni, altura):
    df.insert(len(df)+1, nombre, nacimiento, dni, altura)
    print(df)
    return 0



def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    id_marcela = agregar_persona('marcela gonzalez', datetime.datetime(1980, 1, 25), 12164492, 195)
    assert id_juan > 0
    assert id_marcela > id_juan
    pass

reset_tabla(pruebas)
