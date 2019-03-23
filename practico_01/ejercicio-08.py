# Implementar la función mitad(), que devuelve la mitad de palabra.
# Si la longitud es impar, redondear hacia arriba.
import math


# hola -> ho
# verde -> ver
def mitad(palabra):
    largo = len(palabra)
    if(largo/2!=0):
        largo = math.ceil(largo/2)
    else: largo=largo/2
    mitad= palabra[0:largo]
    return mitad


assert (mitad('pala')) == 'pa';
assert (mitad('palabra')) == 'pala';
