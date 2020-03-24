# Implementar la función es_vocal, que reciba un carácter y
# devuelva un booleano en base a si letra es una vocal o no.


# Resolver utilizando listas y el operador in.
def es_vocal(letra):
    vocales= ['a','e','i','o','u']
    if letra in vocales:
        return True
    else:
        return False
    pass

