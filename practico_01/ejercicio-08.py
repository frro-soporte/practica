# Implementar las funciones superposicion_x(), que tomen dos listas y devuelva un booleano en base a
# si tienen al menos 1 elemento en común.

# se debe implementar utilizando bucles anidados.
def superposicion_loop(lista_1, lista_2):
    ll1 = len(lista_1)
    ll2 = len(lista_2)
    aux2 = False
    i = 0
    for i in range(ll1) :
        j = 0
        for j in range(ll2):
            if lista_1[i] == lista_2[j]:
                aux2 = True
            else:
                pass
    return aux2

print(superposicion_loop([7,2,3],[1,4,5]))
print(superposicion_loop([1,2,3],[1,4,5]))

