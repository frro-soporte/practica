def apartado_a():
    os.system('cls')
    print("---------------------------------")
    print("* Ingrese los numeros una a la vez")
    print("* Ingrese fin para salir")
    print("---------------------------------")
    num = input("\nIntroduzca un numero: ")
    mayor = int(num)
    menor = int(num)
    while num != 'fin':

        if(num != 'fin'):
             num = int(num)
        if(num > mayor):
            mayor = num
        elif (num<menor):
            menor = num
        num = input("Introduzca un numero: ")

    print("El mayor es :", mayor)
    print("El menor es: ", menor)
    sys.exit()

def apartado_b():
    print("---------------------------------")
    print("* Ingrese los numeros una a la vez")
    print("* Ingrese fin para salir")
    print("---------------------------------")
    num = input("\nIntroduzca un numero: ")
    mayor = int(num)
    menor = int(num)
    i=0
    numeros = []
    while num != 'fin':

        if (num != 'fin'):
            numeros.append(int(num))

        i=i+1
        num = input("Introduzca un numero: ")
    print(numeros)
    print("Maximo: ", max(numeros))
    print("Minimo: ", min(numeros))
    sys.exit()


def max(numeros):
    max = numeros[0]
    for num in numeros:
        if num > max:
            max=num
    return max


def min(numeros):
    min = numeros[0]
    for num in numeros:
        if num < min:
            min = num
    return min

def app():

    print("Ingrese a para ver el apartado A")
    print("Ingrese b para ver el apartado B")
    resp = input("\n Ingrese la opcion:")
    while ( (resp != 'a') or (resp != 'b') ):
        if resp == 'a':
            apartado_a()
        elif resp == 'b':
            apartado_b()
        resp = input("\n Ingrese la opcion:")

import sys

if __name__ == '__main__':
    app()