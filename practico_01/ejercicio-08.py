# Implementar la función mitad(), que devuelve la mitad de palabra.
# Si la longitud es impar, redondear hacia arriba.

# hola -> ho
# verde -> ver

def mitad(palabra):
    largo = len(palabra)
    pal = ''
    if largo % 2 == 0:
        indice = int((largo / 2))
        for n in range(0, indice):
            pal = pal + palabra[n]
    else:
        indice = int((largo / 2) + 1)
        for n in range(0, indice):
            pal = pal + palabra[n]
    print(pal)
    return pal


assert mitad('hola') == 'ho'
assert mitad('verde') == 'ver'
