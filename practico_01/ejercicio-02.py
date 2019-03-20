# Implementar la función mayor, que reciba tres números y devuelva el mayor de ellos.

def mayor(a, b, c):
    g=0
    if (a>b and a>c):
        g=a
    else:
        if (b>c):
            g=b
        else:
            g=c

    return g
assert(mayor(600,500,400)==600)
