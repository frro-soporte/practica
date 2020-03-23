# Implementar la función numeros_al_final(), que mueve todos los elementos numéricos
# de lista al final de esta. Devuelve la lista.


# Resolver sin utilizar lista auxiliar
def numeros_al_final(lista):
    lista1 = []
    for i in lista:
        if type(i) != int:
            lista1.append(i)

    for i in lista:
        if type(i) == int:
            lista1.append(i)

    return lista1
