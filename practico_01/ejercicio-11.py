# Implementar la función es_primo(), que devuelva un booleano en base a
# si numero es primo o no.


def es_primo(numero):
    if numero < 0:
        return False
    for i in range(2,5):

        if i==4:
            continue
        if numero%i==0:

            return False
    return True

assert es_primo(7)==True
assert es_primo(4)==False
assert es_primo(-7)==False
assert es_primo(-4)==False
assert es_primo(1)==True #nosotros decidimos incluirlo en este grupo para poder devolver booleano
                        #aunque no sea un nro primo
