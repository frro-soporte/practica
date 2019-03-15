# Implementar la función suma, que reciba dos números y devuelva su suma.


def max(a, b):
    return a if a > b else b

# Case a > b
assert max(1, 2) == 2

# Case b > a
assert max(2, 1) == 2

# Case a == b
assert max(1, 1) == 1