# Implementar las funciones superposicion_x (), que tomen dos listas y devuelva un booleano en base a
# si tienen al menos 1 elemento en común.


# se debe implementar utilizando bucles anidados.
def  superposicion_loop ( lista_1 , lista_2 ):
    b=False
    for element1 in lista_1:
        for element2 in lista_2:
            if element1==element2:
                b=True
                break
    return b


# se debe implementar utilizando conjuntos.
def  superposicion_set ( lista_1 , lista_2 ):
    lista=lista_1 & lista_2
    if len(lista) > 0:
        return True
    else:
        return False

assert superposicion_loop(["a","b","c","b"],["d","e","a","a"])== True
assert superposicion_loop(["b","c","b"],["d","e","a","a"])== False

assert superposicion_set({"a","b","c","b"},{"d","e","a","a"}) == True
assert superposicion_set({"b","c","b"},{"d","e","a","a"}) == False

