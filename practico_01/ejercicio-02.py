# Implementar la función mayor, que reciba tres números y devuelva el mayor de ellos.


def mayor(a, b, c):
    numeros = [a, b, c]
    maximo = a
    for numero in numeros:
        if numero > maximo:
            maximo = numero
    return maximo


# si no falla es porque esta bien
assert mayor(1,10,5) == 10
assert mayor(4,9,18) == 18
