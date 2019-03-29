# Implementar la función numeros_al_final(), que mueve todos los elementos numéricos
# de lista al final de esta. Devuelve la lista.


# Resolver sin utilizar lista auxiliar
def numeros_al_final(lista):

    for i in lista[:]:
        if type(i) == int or type(i) == float:
            lista.append(i)
            lista.remove(i)
    return lista

assert numeros_al_final([1,2,'r','T',4,'B']) == ['r','T','B',1,2,4]