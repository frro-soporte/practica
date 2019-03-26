# Implementar la función multiplicar() que devuelva el producto de todos los números de una lista.
# [1,2,3,4] -> 24

def multiplicar(lista):
    resultado = 1
    for n in lista:
        resultado = n * resultado
    return resultado


list = [1, 2, 3, 4]
assert multiplicar(list)== 24
