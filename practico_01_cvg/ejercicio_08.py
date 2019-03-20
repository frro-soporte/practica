"""
 Definir una función superposicion() que tome dos listas y devuelva True si tienen al
menos 1 miembro en común o devuelva False de lo contrario. Escribir la función
usando el bucle for anidado.

"""

lista_1 = ["a", "b", "c"]
lista_2 = ["b", "d", "e"]

def superposicion (lista1, lista2):
    for i in range (0, len(lista1)):
        for j in range (0, len(lista2)):
            if lista1[i]==lista2[j]:
                return True
    return False

print(superposicion(lista_1, lista_2)
