# Implementar la función mayor, que reciba tres números y devuelva el mayor de ellos.


def mayor(a, b, c):
    if (a>b and a>c):
        return a
    else:
        if (b>a and b>c):
            return b
        else:
            return c




assert mayor(5,9,1) == 9
assert mayor(9,5,8) == 9
assert mayor(1,3,5) == 5



n1 = input('Ingrese 1er numero: ')
n2 = input('Ingrese 2do numero: ')
n3 = input('Ingrese 3er numero: ')

print ("el numero mayor es: " + mayor(n1,n2,n3))