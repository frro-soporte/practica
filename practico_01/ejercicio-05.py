# Implementar la función es_vocal, que reciba un carácter y
# devuelva un booleano en base a si letra es una vocal o no.


# Resolver utilizando listas y el operador in.
def es_vocal(letra):
    vocales=['a','e','i','o','u']
    letra=letra.lower()
    if letra in vocales:
        return True
    else:
        return False


assert es_vocal('A')==True
assert es_vocal('e')==True
assert es_vocal('B')==False
assert es_vocal('j')==False
