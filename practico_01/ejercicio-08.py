# Implementar la función mitad(), que devuelve la mitad de palabra.
# Si la longitud es impar, redondear hacia arriba.


# hola -> ho
# verde -> ver
def superposicion(xs, ys):
    return len(set(xs) & set(ys)) >= 1

# Case for one or more commmon elements
assert superposicion([1, 2, 3, 4], [3, 6, 9, 12]) is True

# Case for no common elements
assert superposicion(list(range(10)), list(range(10, 20))) is False
