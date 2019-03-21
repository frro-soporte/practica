#11. Determinar la cantidad de dígitos de un número ingresado


def cantidad(num):
    i = 0
    while num > 1:
        num = num/10
        i = i + 1
    print(i)
    return i


assert(cantidad(500) == 3)

assert(cantidad(9999999999) == 10)

assert(cantidad(0.2) == 0)
