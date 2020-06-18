# Implementar las funciones superposicion_x(), que tomen dos listas y devuelva un booleano en base a
# si tienen al menos 1 elemento en común.


# se debe implementar utilizando bucles anidados.
def superposicion_loop(lista_1, lista_2):
    c = False
    for a in lista_1:
        for b in lista_2:
            if a == b:
                c = True
                break
    return c


# se debe implementar utilizando conjuntos (sets).
def superposicion_set(lista_1, lista_2):
    if len (lista_1.intersection(lista_2)) > 0:
        return True
    else:
        return False


def main():
    l1 = [1, 2, 3, 4, 5]
    l2 = [4, 6, 7, 8]
    if superposicion_loop(l1, l2):
        print("tienen al menos 1 elemento en comun")
    else:
        print("no tienen elementos en comun")

    l3 = set ([1, 2, 3, 4, 8])
    l4 = set ([5, 6, 7, 8])
    if superposicion_set(l3, l4):
        print("tienen al menos 1 elemento en comun")
    else:
        print("no tienen elementos en comun")


main()
