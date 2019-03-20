#Escribir una función multip() que multiplique respectivamente todos los números de
# una lista. Por ejemplo: multip([1,2,3,4]) debería devolver 24.

lista = [1,2,3,2]

def multiplicar (lista):
    numero = 1
    for i in range (0, len(lista)):
        numero = numero * lista[i]
    return numero

print(multiplicar(lista))

assert multiplicar([1,4,2]) == 8
assert multiplicar([1,1,1,1,1,4]) == 4


