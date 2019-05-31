# Implementar la función multiplicar () que devuelva el producto de todos los números de una lista.


# [1,2,3,4] -> 24
def  multiplicar ( lista ):
    producto = 1
    for elemento in lista:
        producto = producto*elemento
    return producto

assert multiplicar([1,2,3,4])==24

