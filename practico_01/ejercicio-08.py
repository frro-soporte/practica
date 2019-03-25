# Implementar la función mitad(), que devuelve la mitad de palabra.
# Si la longitud es impar, redondear hacia arriba.


# hola -> ho
# verde -> ver
def mitad(palabra):
    return palabra[:round(len(palabra)/2 + 0.5)]
