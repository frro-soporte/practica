# Implementar la función mitad(), que devuelve la mitad de palabra.
# Si la longitud es impar, redondear hacia arriba.


# hola -> ho
# verde -> ver
def mitad(palabra):
    a = int(len(palabra))
    if a % 2 == 0:
        a = a // 2
        pal = palabra[:a]
        return pal
    a = a // 2 + 1
    pal = palabra[:a]
    return pal
