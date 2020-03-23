# Implementar la función es_primo(), que devuelva un booleano en base a
# si numero es primo o no.


def es_primo(numero):
    divisores = 0
    for x in range(1, numero + 1):
        if numero % x == 0:
            divisores += 1
    return divisores <= 2


assert es_primo(1)
assert es_primo(2)
assert not es_primo(10)
assert es_primo(17)
