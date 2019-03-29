
# Implementar las funciones superposicion_x(), que tomen dos listas y devuelva un booleano en base a
# si tienen al menos 1 elemento en común.


# se debe implementar utilizando bucles anidados.
def superposicion_loop(lista_1, lista_2):
    for i in lista_1:
        for j in lista_2:
            if i==j:
                return True
    return False


# se debe implementar utilizando conjuntos (sets).
def superposicion_set(lista_1, lista_2):
    set1=set(lista_1)
    set2=set(lista_2)
    if set1.intersection(set2)==set():
        return False
    return True

assert superposicion_set([1,2,3],[3,4,5])==True
assert superposicion_set([1,2,3],[4,5])==False
assert superposicion_loop([1,2,3],[3,4,5])==True
assert superposicion_loop([1,2,3],[4,5])==False