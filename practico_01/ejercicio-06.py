# Implementar la función multiplicar() que devuelva el producto de todos los números de una lista.


# [1,2,3,4] -> 24
def multiplicar(lista):
    len(lista)
    i=0
    multiplicacion=1
    for i in range(len(lista)):
        multiplicacion *=lista[i]

    return multiplicacion

assert (multiplicar([1,2,3,4]))== 24
