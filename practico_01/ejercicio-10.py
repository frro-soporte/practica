# Implementar las funciones superposicion_x(), que tomen dos listas y devuelva un booleano en base a
# si tienen al menos 1 elemento en común.


# se debe implementar utilizando bucles anidados.

def superposicion_x(lista_1, lista_2):
    a = 0
    for i in range(len(lista_1)):
        for j in range(len(lista_2)):
            if(lista_1[i]==lista_2[j]):
                a=a+1
    if (a>=1):
        return True
    else:
        return False


lista_1 = ["1","2", "3", "4"]
lista_2 = ["5", "6", "7", "2"]

assert superposicion_x(lista_1, lista_2) == True


# se debe implementar utilizando conjuntos (sets).
# def superposicion_set(lista_1, lista_2):
#   pass


def superposicion_set(lista_3, lista_4):
    a = 0
    if (lista_3 & lista_4 != set()):
        a = a + 1
    if (a >= 1):
        return True
    else:
        return False


lista_3 = set([1, 2, 3, 4])
lista_4 = set([5, 6, 4, 3])

# assert superposicion_set(lista_1, lista_2) == False

assert superposicion_set(lista_3, lista_4) == True


