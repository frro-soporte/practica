# Implementar la funcion crear_tabla, que cree una tabla Persona con:
# - IdPersona: Int() (autoincremental)
# - Nombre: Char(30)
# - FechaNacimiento: Date()
# - DNI: Int()
# - Altura: Int()

import datetime
import pandas as pd

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.

index = ["IdPersona", "Nombre", "FechaNacimiento", "DNI", "Altura"]
columns = {}
df = pd.DataFrame(index=index, columns=columns)
def crear_tabla():
    df = pd.DataFrame(index=index, columns=columns)
    pass


def borrar_tabla():
    df.drop(df.index, inplace=True)
    pass

def fulfill(): #Completa columna e imprime
    df = pd.DataFrame(
        {"Persona": [1, 'Martin', datetime.date(1992, 10, 13), 39120610, 185]},
        index = index
    )
    print(df)
    pass

# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla() #Inicializa tabla
        func() #Ejecuta función
        borrar_tabla() #Borra la tabla
    return func_wrapper

reset_tabla(fulfill())
