# Implementar la función mitad(), que devuelve la mitad de palabra.
# Si la longitud es impar, redondear hacia arriba.


# hola -> ho
# verde -> ver
from math import ceil #no pude hacerlo con el import math solo no se xq

def mitad(palabra):
    c = ceil(len(palabra) / 2)
    return palabra[:c]

def main():
    pal = input("Ingrese palabra:")
    print(mitad(pal))


main()
