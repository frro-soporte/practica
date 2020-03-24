# 1. Implementar una función max() que tome como argumento dos números y devuelva el mayor de ellos. 


def maximo(a, b):
    if a>b:
        return(a)
    else:
        return(b)


# si no falla es porque esta bien
assert maximo(10, 5) == 10
assert maximo(9, 18) == 18
