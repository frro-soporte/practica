# Implementar la función numeros_al_final(), que mueve todos los elementos numéricos
# de lista al final de esta. Devuelve la lista.

# Resolver sin utilizar lista auxiliar
def numeros_al_final(lista):
    i=0
    for i in range(len(lista)):
        if (lista[i].isdigit() == True):
            aux = lista[i]
            lista.pop(i)
            lista.append(aux)
    pass

lista = ["1","a","3","b","5","c","v","2"]
numeros_al_final(lista)
print(lista)
