# Implementar la función es_primo(), que devuelva un booleano en base a
# si numero es primo o no.


def es_primo(numero):
    if numero == 1 or numero == 0:
        return False

    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True


assert not es_primo(0)
assert not es_primo(1)
assert es_primo(2)
assert es_primo(3)
assert not es_primo(4)
assert es_primo(5)
