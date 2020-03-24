# Implementar las funciones superposicion_x(), que tomen dos listas y devuelva un booleano en base a
# si tienen al menos 1 elemento en común.


# se debe implementar utilizando bucles anidados.
def superposicion_loop(lista_1, lista_2):
    a = len(lista_1)
    b = len(lista_2)
    c = False
    i = z = 0
    while i < a and c == False:
        while z < b and c == False:
            if lista_1[i] == lista_2[z]:
                c = True
            z=z+1
        i=i+1
        z=0
    return (c)

# se debe implementar utilizando conjuntos (sets).
def superposicion_set(lista_1, lista_2):
    a = set(lista_1) & set(lista_2)
    if len(a) > 0:
        return (True)
    else:
        return (False)

assert superposicion_loop([1,2,3,4],[9,0,3,7]) == True
assert superposicion_set([1,2,13,4],[9,0,3,7]) == False


