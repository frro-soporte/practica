# Implementar la función es_primo(), que devuelva un booleano en base a
# si numero es primo o no.


def es_primo(numero):
    b = True
    for i in range (2,numero):
        if numero % i == 0:
            b = False
            break
    return b

def main():
    if es_primo(19):
        print("Es primo")
    else:
        print("No es primo")

    if es_primo(15):
        print("Es primo")
    else:
        print("No es primo")


main()
