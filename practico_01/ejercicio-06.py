# Implementar la función multiplicar() que devuelva el producto de todos los números de una lista.


# [1,2,3,4] -> 24



def multiplicar(lista):
    total=1
    for elemento in lista:
        total=total*elemento
    return(total)

lista = (1,2,3,4)
assert multiplicar(lista)== 24
