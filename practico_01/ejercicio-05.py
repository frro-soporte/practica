# Implementar la función es_vocal, que reciba un carácter y
# devuelva un booleano en base a si letra es una vocal o no.


# Resolver utilizando listas y el operador in.

vocales=['a', 'e', 'i', 'o', 'u']

def es_vocal(letra):
    es=False;
    for vocal in vocales:
        if vocal==letra:
            es= True
            return es
        else : return es


assert es_vocal('a') == True
assert es_vocal('x') == False
