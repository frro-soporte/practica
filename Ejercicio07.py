'''Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras
que tienen el mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar")
tendría que devolver True'''

def es_palindromo(a):
    if (a==a[::-1]):
        return ('True')
    return('False')


a= 'radar'
assert  (es_palindromo(a)=='True')
