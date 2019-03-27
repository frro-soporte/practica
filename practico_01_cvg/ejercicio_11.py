# Determinar la cantidad de dígitos de un número ingresado.

numero = input("ingrese un numero")


def cant_digitos(num):
    return len(str(num))

print("la cantidad de digitos es: ", cant_digitos(numero))

assert cant_digitos(123456) == 6
assert cant_digitos(1234) == 4