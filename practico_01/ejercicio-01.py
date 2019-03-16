#Implementar la función mayor, que reciba tres números y devuelva el mayor de ellos.

a=3
b=6

def mayor(a, b):
    if a > b:
        solucion = a
    else:
        solucion = b
    return(solucion)

assert mayor(1,3) == 3
assert mayor(3,1) == 3
assert mayor(3,3) == 3
