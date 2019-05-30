# Implementar la función es_vocal, que reciba un carácter y
# devuelva un booleano en base a si letra es una vocal o no.


# Resolver utilizando listas y el operador in.
def es_vocal(letra):
    if (letra in ['a','e','i','o','u']):
        return True
    else: return False



assert (es_vocal('a')) == True;
assert (es_vocal('e')) == True;
assert (es_vocal('i')) == True;
assert (es_vocal('o')) == True;
assert (es_vocal('u')) == True;
assert (es_vocal('t')) == False;



