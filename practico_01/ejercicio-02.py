# Implementar la función mayor, que reciba tres números y devuelva el mayor de ellos.

def mayor(a, b, c):
    if a > b:
        if a > c:
            return a
    elif b > c:
        return b
    else:
        return b

assert mayor(10,9,8) == 10
