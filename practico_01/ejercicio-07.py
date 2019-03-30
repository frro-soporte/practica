# Implementar la función numeros_al_final(), que mueve todos los elementos numéricos
# de lista al final de esta. Devuelve la lista.


def numeros_al_final(lista):
    for i in lista[:]:
        if type(i)==float or type(i)==int or i.isdigit():
            lista.append(i)
            lista.remove(i)
    return lista

assert numeros_al_final(['a',3,'7',5,'g',6,'j','l',10,'P']) == ['a','g','j','l','P',3,'7',5,6,10]
