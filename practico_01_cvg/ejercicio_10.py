"""
Escribir una función mas_larga() que tome una lista de palabras y devuelva la más larga
"""

lista = ["hola", "comoestas","si","genidasdasdasadaal"]

def mas_larga(lista):
    lista_mas_larga = ""
    for i in range(0, len(lista)):
        if (len(lista_mas_larga)< len(lista[i])):
            lista_mas_larga = lista[i]
    return lista_mas_larga


assert mas_larga(["jeje", "ja"]) == "jeje"

print(mas_larga(lista))