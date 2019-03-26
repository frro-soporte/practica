# Implementar la función es_primo(), que devuelva un booleano en base a
# si numero es primo o no.


def es_primo(numero):
    for i in range (2, numero):
        if numero % i == 0:
            print ('El numero ingresado NO es un numero primo')
            return False
        else:
            print ('El numero ingresado SI es un numero primo.')
            return True

assert es_primo(7) == True
