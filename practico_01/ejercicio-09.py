# Implementar la función es_palindromo(), que devuelva un booleano en base a
# si palabra se lee igual de corrido como al revés.


# Ejemplos: arenera, radar, ojo, oso, salas.
# Resolver sin utilizar loops (for/while), sino con slicing.
def es_palindromo(palabra):
    palindromo = palabra[::-1]
    return palindromo == palabra


assert(es_palindromo('ajo'))==False;
assert(es_palindromo('ojo'))==True;

