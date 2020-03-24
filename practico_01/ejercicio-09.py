# Implementar la función es_palindromo(), que devuelva un booleano en base a
# si palabra se lee igual de corrido como al revés.


# Ejemplos: arenera, radar, ojo, oso, salas.
# Resolver sin utilizar loops (for/while), sino con slicing.
def es_palindromo(palabra):
    a = len(palabra)
    a = (a//2) + (a%2)
    if palabra[0:a] == palabra[::-1][0:a]:
        return (True)
    else:
        return (False)

assert es_palindromo('salas') == True