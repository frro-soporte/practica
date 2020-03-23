# Implementar la función es_vocal, que reciba un carácter y
# devuelva un booleano en base a si letra es una vocal o no.


# Resolver utilizando listas y el operador in.
def es_vocal(letra):
    vocales = ['a', 'e', 'i', 'o', 'u']
    for vocal in vocales:
        if letra == vocal:
            return 1
    return 0


assert es_vocal('i')
assert not es_vocal('b')
