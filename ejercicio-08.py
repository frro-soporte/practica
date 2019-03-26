# Implementar la función mitad(), que devuelve la mitad de palabra.
# Si la longitud es impar, redondear hacia arriba.


# hola -> ho
# verde -> ver


def mitad(palabra):
    md = int(len(palabra)/2)
    if(len(palabra) % 2 == 0):
        return(palabra[:md])
    else:
        return(palabra[:md+1])
    pass

pal = "palabra"
assert mitad(pal) == "pala"
pal = "hola"
assert mitad(pal) == "ho"
