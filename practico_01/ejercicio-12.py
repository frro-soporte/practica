#Determinar la suma de todos los números de 1 a N. N es un número que se ingresa por consola.
y=4

def sumar(num):
    x = 1
    n = 1
    while x < num:
        x = x+1
        n = n + x
    return n

assert sumar(y)==10

#print('Ingrese un numero')
#y = int(input())
#suma = sumar(y)
#print('La suma de los numeros 1 hasta',y,'es: ',suma)