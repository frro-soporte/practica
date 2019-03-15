# Implementar la función mayor, que reciba tres números y devuelva el mayor de ellos.


def max_de_tres(a, b, c):
    return max(max(a, b), c)

# Cases a is the biggest

# Case a > c > b
assert max_de_tres(3, 1, 2) == 3

# Case a > b > c
assert max_de_tres(3, 2, 1) == 3

# Cases b is the biggest

# Case b > a > c
assert max_de_tres(2, 3, 1) == 3

# Case b > c > a
assert max_de_tres(1, 3, 2) == 3

# Cases c is the biggest

# Case c > a > b
assert max_de_tres(2, 1, 3) == 3

# Case c > b > a
assert max_de_tres(1, 2, 3) == 3
