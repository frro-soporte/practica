'''Escribir una función mas_larga() que tome una lista de palabras y devuelva la más
larga'''


def mas_larga(a):
    mayor = len(a[0])
    mostrar = a[0]
    for i in a:
        if mayor<= len(i):
            b= i
            mayor=len(i)
    return b

a=['asdasd','asdaaaaaaaa','qw']
assert mas_larga(a) == 'asdaaaaaaaa'


