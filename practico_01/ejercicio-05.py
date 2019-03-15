# Implementar la función es_vocal, que reciba un carácter y
# devuelva un booleano en base a si letra es una vocal o no.


from functools import reduce

def multip(xs):
    return reduce(lambda x, y: x * y, xs)

# Case for non-empty list
assert multip([1, 2, 3, 4, 5]) == 120