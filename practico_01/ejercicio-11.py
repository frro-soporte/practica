# Implementar la función es_primo(), que devuelva un booleano en base a
# si numero es primo o no.

def es_primo(numero):
    for i in range(2,numero):
        if numero%i == 0:
            return False
    return True

assert es_primo(7) == True
assert es_primo(10) == False
