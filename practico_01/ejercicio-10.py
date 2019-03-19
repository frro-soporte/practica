# Implementar la funcion mas larga que tome una lista de palabras y devuelva la mas larga

def mas_larga(lista_01):
    lista_aux = lista_01
    ll1= len(lista_01)
    aux = 0
    i = 0
    for i in range(ll1):
        if len(lista_01[i]) > aux:
            aux_2 = lista_01[i]
            aux = len(lista_01[i])
        else:
            pass
    return aux_2


print(mas_larga(["Hola","j","pe"]))
