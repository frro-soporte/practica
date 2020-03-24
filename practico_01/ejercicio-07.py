# Implementar la función numeros_al_final(), que mueve todos los elementos numéricos
# de lista al final de esta. Devuelve la lista.

# Resolver sin utilizar lista auxiliar
def numeros_al_final(lista):
    a = len(lista)
    i = 0
    while i < a:
        b = False
        if isinstance(lista[i], int) or isinstance(lista[i], float):
            lista.append(lista[i])
            lista.pop(i)
            b = True
            a = a-1
        if b== True:
            i=0
        else:
            i=i+1
    return(lista)

assert numeros_al_final([1,2,'a','b',3,5,'cd']) == ['a', 'b', 'cd', 1, 2, 3, 5]




