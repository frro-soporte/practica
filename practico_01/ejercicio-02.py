# Implementar la función mayor, que reciba tres números y devuelva el mayor de ellos.


def mayor(a, b, c):
    if a > b:
        if a > c:
            return a
    elif b > c:
        return b
    return c

assert mayor(1,2,3) == 3
assert mayor(10,2,1) == 10
assert mayor(-20,-1,-3) == -1