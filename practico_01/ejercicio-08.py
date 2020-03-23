# Implementar la función mitad(), que devuelve la mitad de palabra.
# Si la longitud es impar, redondear hacia arriba.


# hola -> ho
# verde -> ver
def mitad(palabra):
    mitad_palabra = ""
    for x in range(int(len(palabra)/2 + 0.5)):
        mitad_palabra += palabra[x]
    return mitad_palabra


assert mitad("hola") == "ho"
assert mitad("verde") == "ver"
