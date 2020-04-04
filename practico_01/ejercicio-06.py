# Implementar la función multiplicar() que devuelva el producto de todos los números de una lista.

# [1,2,3,4] -> 24


def multiplicar(lista):
    a = 1
    for i in lista:
        a = a * i
    return a


def main():
    li = [1, 2, 3, 4]
    print(multiplicar(li))


main()
