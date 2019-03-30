# Implementar la función mayor, que reciba tres números y devuelva el mayor de ellos.

def mayor(a,b,c):
    if (a >= b) and (a >= c):
        return a
    elif (b >= c):
        return b
    else:
        return c

assert mayor(2,6,45) == 45
