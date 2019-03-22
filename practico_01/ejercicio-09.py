# Implementar la función es_palindromo(), que devuelva un booleano en base a
# si palabra se lee igual de corrido como al revés.


# Ejemplos: arenera, radar, ojo, oso, salas.
# Resolver sin utilizar loops (for/while), sino con slicing.


def es_palindromo(palabra):
    z = False
    x= len(palabra)
    if palabra[0:x] == palabra [::-1]:
        z = True
    return  z

assert es_palindromo("radar") == True
