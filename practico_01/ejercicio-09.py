# Implementar la función es_palindromo(), que devuelva un booleano en base a
# si palabra se lee igual de corrido como al revés.


# Ejemplos: arenera, radar, ojo, oso, salas.
# Resolver sin utilizar loops (for/while), sino con slicing.
def es_palindromo(palabra):
    return palabra == palabra[slice(-1, len(palabra) * (-1) - 1, -1)]


assert es_palindromo("arenera")
assert es_palindromo("radar")
assert es_palindromo("salas")
assert not es_palindromo("palindromo")
