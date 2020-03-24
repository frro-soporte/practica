# Determinar la suma de todos los numeros de 1 a N. N es un número que se ingresa
# por consola.


def suma(N):
    sumatoria = 0
    for x in range (1, N):
        sumatoria += x
    return sumatoria


print(suma(int(input())))
