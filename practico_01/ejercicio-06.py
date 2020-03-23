# Implementar la función multiplicar() que devuelva el producto de todos los números de una lista.


# [1,2,3,4] -> 24
def multiplicar(lista):
    resultado = 1
    for numero in lista:
        resultado = resultado * numero
    return resultado


assert multiplicar([2, 3]) == 6
assert multiplicar([1, 2, 3, 4]) == 24
