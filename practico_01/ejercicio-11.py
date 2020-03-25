# Implementar la función es_primo(), que devuelva un booleano en base a
# si numero es primo o no.

def es_primo(numero):
    n = 0
    for i in range (1,numero+1):
        if ((numero % i) == 0):
            n= n+1
    if (n == 2):
        return True
    else:
        return False
    pass

assert es_primo(8) == False
assert es_primo(11) == True
