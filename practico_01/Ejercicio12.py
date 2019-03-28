'''Determinar la suma de todos los números de 1 a N. N es un número que se ingresa
por consola.'''
def suma():
    numero = int(input("Ingrese un numero"))
    a=0
    while numero >= 0:
        a = a + numero
        numero= numero-1
    print(f"La suma es: {a}")

