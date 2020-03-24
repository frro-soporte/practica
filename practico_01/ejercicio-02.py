# Implementar la función mayor, que reciba tres números y devuelva el mayor de ellos.


def mayor(a, b, c):
    if a>b:
        if a>c:
            return(a)
        else:
            return(c)
    elif b>c:
        return(b)
    else:
        return(c)

# si no falla es porque esta bien
assert mayor(1,10,5) == 10
assert mayor(4,9,18) == 18
