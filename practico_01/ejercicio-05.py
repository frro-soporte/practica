# Implementar la función es_vocal, que reciba un carácter y
# devuelva un booleano en base a si letra es una vocal o no.


# Resolver utilizando listas y el operador in.

def es_vocal(c):
    vocales = ['a', 'e', 'i' , 'o' ,'u']
    c = c.lower()
    if c in vocales:
        return True
    else:
        return False


assert es_vocal('t') == False
assert es_vocal('a') == True
assert es_vocal('E') == True

