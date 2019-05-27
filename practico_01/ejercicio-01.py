# 1. Implementar una función max() que tome como argumento dos números y devuelva el mayor de ellos. 
def max(a, b):
    if a >= b:
        return a
    return b

assert max (5,8) == 8
assert max (4,7) == 7


n1 = input('Ingrese 1er numero: ')
n2 = input('Ingrese 2do numero: ')

print ("el numero mayor es: " + max(n1,n2))

