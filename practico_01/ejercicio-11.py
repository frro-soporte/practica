# Implementar la función es_primo(), que devuelva un booleano en base a
# si numero es primo o no.


def es_primo(numero):
    if numero == 2:
        return(True)
    if numero % 2 == 0:
        return (False)
    for i in range(2,numero - 1,1):
        if numero % 2 == 0:
            return (False)
    return (True)

assert es_primo(13) == True
assert es_primo(26) == False