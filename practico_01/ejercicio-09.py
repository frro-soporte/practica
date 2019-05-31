# Implementar la función es_palindromo (), que devuelva un booleano en base a
# si la palabra se lee igual que se corrige como al revés.


# Ejemplos: arenera, radar, ojo, oso, salas.
# Resolver sin utilizar loops (for / while), sino con rebanar.
def  es_palindromo ( palabra ):
    if palabra[::-1]==palabra[::]:
        return True
    else:
        return False

assert es_palindromo("arenera")==True
assert es_palindromo("radar")==True
assert es_palindromo("HOLA")==False

