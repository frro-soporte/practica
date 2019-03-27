# Implementar la función es_primo(), que devuelva un booleano en base a
# si numero es primo o no.


def es_primo(numero):
    return not any([numero%i == 0 for i in range(2,numero)])
