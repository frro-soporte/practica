#Escribir una función mas_larga() que tome una lista de palabras y devuelva la más
#larga.

def mas_larga(lista):
    larga=""
    for i in lista:
        if (len(larga)<len(i)):
            larga=i
    return larga

assert (mas_larga(["hola","chau","genial","cola","schwegler","buffer"])=="schwegler")
