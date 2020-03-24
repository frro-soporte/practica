# Implementar la función es_vocal, que reciba un carácter y
# devuelva un booleano en base a si letra es una vocal o no.


# Resolver utilizando listas y el operador in.
def es_vocal(letra):
    vocales = ['a','e','i','o','u']
    return (letra.lower() in vocales)

assert es_vocal('A') == True
assert es_vocal('b') == False