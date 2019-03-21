'''Determinar la cantidad de dígitos de un número ingresado.'''
import math
def cant_digitos(a):
 contador=0
 contador = int(math.log10(a)) + 1






 return contador




 pass




assert cant_digitos(4)==1
assert cant_digitos(44566)==5
assert cant_digitos(444444444444)==12

