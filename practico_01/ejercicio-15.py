# Reescribe el programa que pide al usuario una lista de números e imprime en
# pantalla el máximo y mínimo de los números introducidos al final,cuando el usuario
# introduce “fin”. Escribe ahora el programa de modo que almacene los números que
# el usuario introduzca en una lista y usa las funciones Max () y min () para calcular los
# números máximo y mínimo después de que el bucle termine.

def minimo(lista):
    min = lista[0]
    for num in lista:
        if num < min:
            min = num
    return min


def maximo(lista):
    max = lista[0]
    for num in lista:
        if num > max:
            max = num
    return max


array = []
var = input()
while var != "fin":
    array.append(var)
    var = input()
print("Maximo: " + str(maximo(array)) + "\nMinimo: " + str(minimo(array)))

