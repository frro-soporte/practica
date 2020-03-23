# Implementar las funciones superposicion_x(), que tomen dos listas y devuelva un booleano en base a
# si tienen al menos 1 elemento en común.


# se debe implementar utilizando bucles anidados.
def superposicion_loop(lista_1, lista_2):
    for x in lista_1:
        for y in lista_2:
            if x == y:
                return True
    return False


# se debe implementar utilizando conjuntos (sets).
def superposicion_set(lista_1, lista_2):
    return lista_1.intersection(lista_2)


assert superposicion_loop(['a', 's', 'd'], ['q', 's', 'e'])
assert superposicion_set(set(['a', 's', 'd']), set(['q', 's', 'e']))
assert not superposicion_loop(['a', 's', 'd'], ['q', 'w', 'e'])
assert not superposicion_set(set(['a', 's', 'd']), set(['q', 'w', 'e']))
