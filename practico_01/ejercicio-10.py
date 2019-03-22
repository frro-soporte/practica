# Implementar las funciones superposicion_x(), que tomen dos listas y devuelva un booleano en base a
# si tienen al menos 1 elemento en común.


# se debe implementar utilizando bucles anidados.
def superposicion_loop(lista_1, lista_2):
    z = False
    for i in lista_1:
        for j in lista_2:
            if i == j:
                z = True
                break
        if z == True:
            break
    return z


# se debe implementar utilizando conjuntos (sets).
def superposicion_set(lista_1, lista_2):
    z = lista_1 & lista_2
    if z:
        return True
    else:
        return False


assert superposicion_loop("adas","aefg") == True
assert superposicion_set({1, 2, 3, 4, 5},{1, 6, 7, 8, 0}) == True
