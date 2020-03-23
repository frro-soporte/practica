# Implementar las funciones superposicion_x(), que tomen dos listas y devuelva un booleano en base a
# si tienen al menos 1 elemento en común.


# se debe implementar utilizando bucles anidados.
def superposicion_loop(lista_1, lista_2):
    for i in lista_1:
        for x in lista_2:
            if i == x:
                return True
                break
    return False


# se debe implementar utilizando conjuntos (sets).
def superposicion_set(lista_1, lista_2):
    set1 = set(lista_1)
    set2 = set(lista_2)
    if set1 & set2 == None:
        return False
    else:
        return True
