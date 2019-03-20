# Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras
# que tienen el mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar")
# tendría que devolver True



def is_palindromo (cadena):
    if cadena == inversa(cadena):
        return True
    return Falses


def inversa (cadena):
    return cadena [::-1]

cadena = input("ingrese cadena a evaluar \n")
print(is_palindromo(cadena))

assert is_palindromo("radar") == True
assert is_palindromo("das") == False
