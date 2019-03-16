"""7. Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras
que tienen el mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar")
tendría que devolver True."""

nom = "abalaba"
def es_palindromo(x):
    palindromo = x[::-1]
    if palindromo == x:
        return True
    else:
        return False
print (es_palindromo(nom))
assert es_palindromo("abalaba") == True
