# Implementar la función es_palindromo(), que devuelva un booleano en base a
# si palabra se lee igual de corrido como al revés.
# Ejemplos: arenera, radar, ojo, oso, salas.
# Resolver sin utilizar loops (for/while), sino con slicing.
def es_palindromo(palabra):
    pal = True
    x= palabra[::-1]
    if x != palabra:
        pal = False

    print(pal)
    return pal

assert(es_palindromo('arenera') == True)
assert(es_palindromo('arena') == False)


# Implementar la función numeros_al_final(), que mueve todos los elementos numéricos
# de lista al final de esta. Devuelve la lista.
# Resolver sin utilizar lista auxiliar

def numeros_al_final(lista):
    i = 0
    for palabras in lista:
        if type(lista[i]) is int:
            a = lista[i]
            lista.remove(a)
            lista.append(a)
            i = i - 1
        i = i + 1
    print(lista)


abc = [2, 'avs', 9, 7, 12.3, 'asfa', 6.5, 12]

numeros_al_final(abc)
