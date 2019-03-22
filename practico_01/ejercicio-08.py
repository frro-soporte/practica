# Implementar la función mitad(), que devuelve la mitad de palabra.
# Si la longitud es impar, redondear hacia arriba.


# hola -> ho
# verde -> ver
import math


def mitad(palabra):
    i = math.ceil(int(len(palabra))/2)
    mit = palabra[0:i]
    print(mit)
    return mit


assert mitad("hola") == "ho"
assert mitad("verde") == "ver"
