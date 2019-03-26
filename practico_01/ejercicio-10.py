# Implementar las funciones superposicion_x(), que tomen dos listas y devuelva un booleano en base a
# si tienen al menos 1 elemento en común.


# se debe implementar utilizando bucles anidados.

def superposicion_loop(lista_1, lista_2):
    for i in range(lista_1):
        for x in range(lista_2):
            if(lista_1[i] == lista_2[x]):
                bol = True
                return(bol)
    pass


# se debe implementar utilizando conjuntos (sets).
#def superposicion_set(lista_1, lista_2):
 #   pass

bol = False
lista_1 = ["a", "2", "b", "8"]
lista_2 = ["v", "c", "6", "a"]
#assert superposicion_loop(lista_1, lista_2) == False
superposicion_loop(lista_1, lista_2)
print(bol)
