#Determinar la suma de todos los numeros de 1 a n. N es un numero que se ingresa por consola.

def suma_todos():
    n = int(input("Introduce un numero: "))
    i = 0
    aux = 0
    for i in range(n+1):
        aux = i + aux
    return aux

print(suma_todos())

