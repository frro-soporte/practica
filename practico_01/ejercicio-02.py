# Implementar la función mayor, que reciba tres números y devuelva el mayor de ellos.


def mayor(a, b, c):
    if a >=b:
        if a >=c:
            return a
        elif c >=b:
            return c
    elif b >= c:
        return b
    pass

n1 = input('Ingrese 1er numero: ')
n2 = input('Ingrese 2do numero: ')
n3 = input('Ingrese 3er numero: ')

print ("el numero mayor es: " + max(n1,n2,n3))
