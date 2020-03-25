# Implementar la función es_palindromo(), que devuelva un booleano en base a
# si palabra se lee igual de corrido como al revés.


# Ejemplos: arenera, radar, ojo, oso, salas.
# Resolver sin utilizar loops (for/while), sino con slicing.

def es_palindromo(palabra):
    longitud = int(len(palabra)/2)
    corte_1 = slice(0,longitud,1)
    corte_2= slice(-1,-longitud-1,-1)
    if(palabra[corte_1] == palabra[corte_2]):
        return(True)
    else:
        return(False)
pass


pal = "ojo"
assert es_palindromo(pal) == True
pal= "hola"
assert  es_palindromo(pal) == False
