# Implementar la función es_primo(), que devuelva un booleano en base a
# si numero es primo o no.


def es_primo(numero):
    if numero == 1:
        return True
    else:
        for i in range(2, numero):
            if numero % i == 0:
                return False
        return True
