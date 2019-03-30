# Implementar la función multiplicar() que devuelva el producto de todos los números de una lista.

lista = [1, 2, 3, 4, 2]

def multiplicar(lista):
    mult = 1
    for i in lista:
        mult=mult*i
    return mult

assert multiplicar(lista) == 48
