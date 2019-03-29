# Implementar la función multiplicar() que devuelva el producto de todos los números de una lista.


# [1,2,3,4] -> 24
def multiplicar(lista):
    multi=1
    i=0
    for i in range(len(lista)):
        multi=multi*lista[i]
    return multi

assert multiplicar([1,2,3,4])==24
assert multiplicar ([1,2,3,-4])==-24
#   -OTRA SOLUCIÓN-
#def multiplicar(lista):
#    multi=1
#    i=0
#    for i in lista:
#        multi=multi*i
#    return multi
#
#assert multiplicar([1,2,3,4])==24
#assert multiplicar ([1,2,3,-4])==-24