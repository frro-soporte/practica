# Implementar la función mayor, que reciba tres números y devuelva el mayor de ellos.

    
def max_de_tres(a, b, c):
    g=0
    if (a>b and a>c):
        g=a
    else:
        if (b>c):
            g=b
        else:
            g=c

    return g
assert(max_de_tres(210,800,500)==800)
    pass
