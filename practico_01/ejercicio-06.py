# Implementar la función multiplicar() que devuelva el producto de todos los números de una lista.


# [1,2,3,4] -> 24
def multiplicar(lista):
    p = 1
    for i in lista:
        p*=i
    return p
