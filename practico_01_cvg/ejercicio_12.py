#Determinar la suma de todos los números de 1 a N. N es un número que se ingresa por consola

num = int(input("ingrese el numero "))

def suma (num):
    suma = 0
    for i in range(1,num+1):
        suma = suma + i

    return suma

print("la suma es: ", suma(num))

assert suma(3) == 6
assert suma(4) == 10
