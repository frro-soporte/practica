"""Practica1 Ejercicio 2 Alumno: Pablo Uriel Alvarez Grupo 29"""
"""Defino la funcion mayor que recibe tres numeros y devuelve el mayor de ellos"""
def mayor(a,b,c):
    if( a > b and  a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c

#Verifico con el assert
assert mayor(10,20,30) == 30
assert mayor(3,2,1)== 3
