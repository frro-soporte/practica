# Implementar la función numeros_al_final(), que mueve todos los elementos numéricos
# de lista al final de esta. Devuelve la lista.


# Resolver sin utilizar lista auxiliar
def numeros_al_final(lista):
    i=0
    for letra in lista:
        i=i+1
        if i < len(lista):
            if isinstance(lista[i], int):
                lista.append(lista[i])
                lista.pop(i)

        elif i == len(lista):

                return lista


lista = ['a', 3, 'b', 2 , 'c' , 5, 5]
assert numeros_al_final(lista) == ['a', 'b', 'c', 5, 2, 3, 5]
