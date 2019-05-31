"""Practica1 Ejercicio 3 Alumno: Pablo Uriel Alvarez Grupo 29"""
"""Defino la funcion operacion"""
def operacion(a,b,multiplicacion):
    if(multiplicacion==True):
        return a*b
    elif(multiplicacion==False and b==0):
        print("Operatiria no valida")
    else:
        return a/b

#Uso el assert para probar
   operacion(20,2, True )==10
