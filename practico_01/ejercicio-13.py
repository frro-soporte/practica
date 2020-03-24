#Programe una funcion que determine si un numero entero suministrado como argumento es primo

def es_primo(numero):
    divisores = 0
    for x in range(1, numero + 1):
        if numero % x == 0:
            divisores += 1
    return divisores <= 2


if es_primo(int(input())):
    print("Es primo")
else:
    print("No es primo")
