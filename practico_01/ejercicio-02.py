# Implementar la función mayor, que reciba tres números y devuelva el mayor de ellos.

def mayor(a, b, c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    else:
        if b > c:
            return b
        else:
            return c

print(mayor(2,2,2))
print(mayor(3,1,1))
print(mayor(1,4,1))
print(mayor(1,1,5))

