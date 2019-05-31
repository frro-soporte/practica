"""Practica1 Ejercicio 3 Alumno: Pablo Uriel Alvarez Grupo 29"""

#defino la funcion conversor
def conversor(grados):
    grados= ((grados*9) / 5)+32
    return grados

#Verifico la funcion con el assert
assert conversor(100)==212
