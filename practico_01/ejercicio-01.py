# 1. Implementar una función max() que tome como argumento dos números y devuelva el mayor de ellos. 


def maximo(a, b):
    if a>b:
        return a
    return b

assert maximo(5,1) == 5
assert maximo(2,3) == 3
assert maximo(4,4) == 4
