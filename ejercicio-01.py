"""Practica1 Ejercicio 1 Alumno: Pablo Uriel Alvarez Grupo 29"""

"""Defino la funcion Max()"""
def max(num1,num2):
    if num1>=num2:
        return num1
    else:
        return num2

#Utilizo el asset para verificar
assert max(10,9) == 10
assert max(10,12) == 12

