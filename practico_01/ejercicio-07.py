# Implementar la función numeros_al_final(), que mueve todos los elementos numéricos de lista al final de esta. Devuelve la lista.
# Resolver sin utilizar lista auxiliar

def numeros_al_final(lista):
    count = 0
    for i in lista:
        if isinstance(lista[count], int):
            aux = lista[count]
            lista.remove(lista[count])
            lista.append(aux)
        else:
            count = count + 1
    print(lista)


lista = [8,'r',2,3,'j','j',1,'k',4,'b',10,'g',10]
numeros_al_final(lista)
