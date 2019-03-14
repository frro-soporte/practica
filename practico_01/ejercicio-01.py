#Implementar la función mayor, que reciba tres números y devuelva el mayor de ellos.

a=3
b=6
c=2

def mayor(a, b, c):
    if a > b and a > c:
        solucion = a
    elif b > c:
        solucion = b
    else:
        solucion = c
    return(solucion)

assert mayor(1,2,3) == 3
assert mayor(3,2,1) == 3
assert mayor(1,3,2) == 3
assert mayor(3,3,3) == 3
assert mayor(1,3,3) == 3
assert mayor(3,1,3) == 3
assert mayor(3,3,1) == 3
