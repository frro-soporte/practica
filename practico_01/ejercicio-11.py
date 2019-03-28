# Implementar la función es_primo(), que devuelva un booleano en base a
# si numero es primo o no.


def es_primo(numero):
    a=0
    for i in range(1,numero+1):
        if((numero%i) == 0):
            a=a+1

    if(a == 2):
        bol=True
        return bol
    else:
        bol=False
        return bol

num = 7
assert es_primo(num) == True
assert es_primo(269)==True
assert es_primo(4) == False
