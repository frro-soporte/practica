#Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras
#que tienen el mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar")
#tendría que devolver True.

def es_palindromo(cadena):
    if(cadena==cadena[::-1]):
        return True
    else:
        return False

assert (es_palindromo("neuquen")==True)
