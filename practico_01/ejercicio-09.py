# Implementar la función es_palindromo(), que devuelva un booleano en base a
# si palabra se lee igual de corrido como al revés.

# Ejemplos: arenera, radar, ojo, oso, salas.
# Resolver sin utilizar loops (for/while), sino con slicing.

import math

def es_palindromo(palabra):
    lon = math.ceil(len(palabra)/2)
    pal_1 = palabra [0:lon]
    pal_2 = palabra[:-lon-1:-1]
    if pal_1 == pal_2:
        print('Es palindromo')
        return True
    else:
        print('No es palindromo')
        return False


assert es_palindromo('arenera') == True
assert es_palindromo('radar') == True
assert es_palindromo('oso') == True
assert es_palindromo('ojo') == True
assert es_palindromo('salas') == True





