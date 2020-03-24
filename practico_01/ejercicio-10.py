# Implementar las funciones superposicion_x(), que tomen dos listas y devuelva un booleano en base a
# si tienen al menos 1 elemento en común.


# se debe implementar utilizando bucles anidados.
def superposicion_loop(lista_1, lista_2):
    pass
    
    lista_final = []
    
    for i in lista_1:
    
        if( i not in lista_final) and ( i in lista_2 ):
    
            lista_final.append(i)
            
    if len(lista_final) == 0: 
        return False
    else: 
        return True

# se debe implementar utilizando conjuntos (sets).
def superposicion_set(lista_1, lista_2):
    pass
    
    lista_final = list(set(lista_1) & set(lista_2))

    if len(lista_final) == 0: 
        return False
    else: 
        return True


lista1 = [1,2,3,4,5]
lista2 = [6,7,8]


print(superposicion_loop(lista1,lista2))
print(superposicion_set(lista1,lista2))

lista3 = [1,2,3,4,5]
lista4 = [4,5,6]

print(superposicion_loop(lista3,lista4))
print(superposicion_set(lista3,lista4))