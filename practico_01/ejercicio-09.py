# Implementar la función es_palindromo(), que devuelva un booleano en base a
# si palabra se lee igual de corrido como al revés.


# Ejemplos: arenera, radar, ojo, oso, salas.
# Resolver sin utilizar loops (for/while), sino con slicing.
def generar_n_caracteres(n, char):
    return char * n

# Case for n = 0
assert generar_n_caracteres("h", 0) == ""

# Case for n = 1
assert generar_n_caracteres("h", 1) == "h"

# Case for n >= 1
assert generar_n_caracteres("h", 2) == "hh"