# Implementar la función mayor, que reciba tres números y devuelva el mayor de ellos.


def maximo(a, b, c):
    pass

    if b < a > c : 
        print("El mayor es: ",a)
        return a
    if a < b > c : 
        print("El mayor es: ",b)
        return b
    if b < c > a : 
        print("El mayor es: ",c)
        return c

# Si no falla es porque esta bien
assert maximo(1,10,5) == 10
assert maximo(4,9,18) == 18
