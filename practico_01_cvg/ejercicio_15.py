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

#def apartado_b():

import os

print("Ingrese a para ver el apartado A")
print("Ingrese b para ver el apartado B")
resp = input("\n Ingrese la opcion:")
while ( (resp != 'a') or (resp != 'b') ):
    if resp == 'a':
        apartado_a()
    elif resp == 'b':
        apartado_b()
    resp = input("\n Ingrese la opcion:")
