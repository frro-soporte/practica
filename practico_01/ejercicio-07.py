# Implementar la función numeros_al_final(), que mueve todos los elementos numéricos
# de lista al final de esta. Devuelve la lista.


# Resolver sin utilizar lista auxiliar
def numeros_al_final(lista):
    lista.reverse()
    return lista


def main():
    li = [1, 2, 3, 4, 5, 6, 7, 8]
    print(numeros_al_final(li))


main()
