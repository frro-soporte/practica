# Implementar las funciones superposicion_x(), que tomen dos listas y devuelva un booleano en base a
# si tienen al menos 1 elemento en común.


# se debe implementar utilizando bucles anidados.
def superposicion_loop(lista_1, lista_2):
    for i in lista_1:
        for x in lista_2:
            if i == x:
                return True
    return False


# se debe implementar utilizando conjuntos (sets).
def superposicion_set(lista_1, lista_2):
    set1 = set(lista_1)
    set2 = set(lista_2)

    return set1.intersection(set2) != set()


assert (superposicion_loop([1, 2, 3, 4, 5, 6], [6, 7, 8, 9]))
assert (superposicion_set([1, 2, 3, 4, 5, 6], [6, 7, 8, 9]))
assert not (superposicion_loop([1, 2, 3, 4, 5], [6, 7, 8, 9]))
assert not (superposicion_set([1, 2, 3, 4, 5], [6, 7, 8, 9]))
