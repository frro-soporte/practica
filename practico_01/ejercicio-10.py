# Implementar las funciones superposicion_x(), que tomen dos listas y devuelva un booleano en base a
# si tienen al menos 1 elemento en común.


# se debe implementar utilizando bucles anidados.
def superposicion_loop(lista_1, lista_2):
   comun=0
   for i in lista_1:
       for j in lista_2:
           if i == j:
               comun=1
               break
   if comun == 1:
    return True
   else:
    return False

# se debe implementar utilizando conjuntos (sets).
def superposicion_set(lista_1, lista_2):
    lista_1=set(lista_1)
    lista_2=set(lista_2)
    lista_1.intersection_update(lista_2)
    if len(lista_1) == 0:
        return False
    else:
        return True

assert superposicion_loop('hola','titi') == False
assert superposicion_loop('hola','ola') == True
assert superposicion_set('hola','titi') == False
assert superposicion_set('hola','ola') == True
