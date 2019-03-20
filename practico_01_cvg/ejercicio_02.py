# Implementar la función mayor, que reciba tres números y devuelva el mayor de ellos.


def mayor(a, b, c):
    if a >=b:
        if a >=c:
            return a
        elif c >=b:
            return c
    elif b >= c:
        return b



assert mayor(5,9,1) == 9
assert mayor(9,5,8) == 9
#assert mayor(2,5,7) == 7



n1 = input('Ingrese 1er numero: ')
n2 = input('Ingrese 2do numero: ')
n3 = input('Ingrese 3er numero: ')

print ("el numero mayor es: " + max(n1,n2,n3))