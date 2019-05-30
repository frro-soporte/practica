# Implementar las funciones superposicion_x(), que tomen dos listas y devuelva un booleano en base a
# si tienen al menos 1 elemento en común.


# se debe implementar utilizando bucles anidados 2 for.
def superposicion_loop(lista_1, lista_2):
    resultado=False
    for valor_lista1 in lista_1:
        for valor_lista2 in lista_2:
            if(valor_lista1 == valor_lista2):
                return True
    return resultado



# se debe implementar utilizando conjuntos (sets) diccionario.
def superposicion_set(lista_1, lista_2):
    lista_interseccion = lista_1.intersection(lista_2)
    if lista_interseccion:
        return True
    else:
        return False


assert superposicion_set({'uno','dos','tres'},{'cuatro','dos'})==True
assert superposicion_set({'uno','dos','tres'},{'cuatro','doce'})==False

assert superposicion_loop(['uno','dos','tres'],['cuatro','cinco'])== False
assert superposicion_loop(['uno','dos','tres'],['cuatro','dos'])== True
