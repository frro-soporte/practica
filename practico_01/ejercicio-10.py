# Implementar las funciones superposicion_x(), que tomen dos listas y devuelva un booleano en base a
# si tienen al menos 1 elemento en común.


# se debe implementar utilizando bucles anidados.
def superposicion_loop(lista_1, lista_2):
    for n in lista_1:
        for j in lista_2:
            if n == j:
                print('El primer elemento en común de las listas es:', j)
                return True
    print('No hay elementos en común entre ambas listas.')
    return False

assert superposicion_loop([1,2,3,4],[4,5,6,7,]) == True


# se debe implementar utilizando conjuntos (sets).
def superposicion_set(set1, set2):
    elementos = set1.intersection(set2)
    if elementos != {}:
        print("Hay elemntos en común, que son:", elementos)
        return True
    else:
        print('No hay elementos en común entre ambas listas.')
        return False


assert superposicion_set({1,2,3,4}, {4,4,6,7}) == True
