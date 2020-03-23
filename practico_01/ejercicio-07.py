# Implementar la función numeros_al_final(), que mueve todos los elementos numéricos
# de lista al final de esta. Devuelve la lista.


# Resolver sin utilizar lista auxiliar
def numeros_al_final(lista):
    largo_lista = len(lista)

    for i in range(largo_lista):
        if type(lista[i]) == int or type(lista[i]) == float:
            lista.append(lista[i])

    i = 0

    while i < largo_lista:
        if type(lista[i]) == int or type(lista[i]) == float:
            lista.pop(i)
            largo_lista = largo_lista - 1

        else:
            i = i + 1
    return lista


assert (numeros_al_final(['p', 4, 1, 'a', 3, 'b'])) == ['p', 'a', 'b', 4, 1, 3]
