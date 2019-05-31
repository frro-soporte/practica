# Implementar la función numeros_al_final (), que mueve todos los elementos numéricos
# de lista al final de esta. Devuelve la lista.


# Resolver sin utilizar lista auxiliar
def  numeros_al_final ( lista ):
    listap=[]
    listan=[]
    for element in lista:
        if type(element)==int:
            listan.append(element)
        else:
            listap.append(element)
    lista= listap+listan
    return lista

assert numeros_al_final([1,3,4,5,"ds",5]) == ["ds",1,3,4,5,5]



