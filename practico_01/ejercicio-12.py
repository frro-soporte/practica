'''Determinar la suma de todos los números de 1 a N. N es un número que se ingresa por consola.'''

def suma_n(a):

 cont=0

 for i in range(a+1):
  cont = cont + i

 return cont





 pass

x = int(input("Ingrese un numero: "))

assert suma_n(4)==10
assert suma_n(5)==15
assert suma_n(6)==21