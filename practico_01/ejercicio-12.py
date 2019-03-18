'''Determinar la suma de todos los números de 1 a N. N es un número que se ingresa por consola.'''

def suma_n(a):

 cont=0

 for i in range(a+1):
  cont = cont + i

 return cont





 pass

x = int(input("Ingrese un numero: "))

resultado= suma_n(x)

print(resultado)