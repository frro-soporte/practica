# Escribir una función multip() que multiplique respectivamente todos los números de una lista. Por ejemplo: multip([1,2,3,4]) debería devolver 24.

def multiplicar(list):
    acum= 0
    for i in list:
        acum = list[i] * acum

    return acum


pass

listas = [1, 2, 3, 4]




