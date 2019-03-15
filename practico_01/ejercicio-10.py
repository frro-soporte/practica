# Implementar las funciones superposicion_x(), que tomen dos listas y devuelva un booleano en base a
# si tienen al menos 1 elemento en común.


def mas_larga(xs):
    return sorted(xs, key=len, reverse=True)[0] if xs else []

# Case for empty list
assert mas_larga([]) == []

# Case for one element list
assert mas_larga(["hola"]) == "hola"

# Case for more than one element list
assert mas_larga(["h", "hola", "esternocleidomastoideo", "adios"]) == "esternocleidomastoideo"