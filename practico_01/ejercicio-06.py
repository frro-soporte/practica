# Implementar la función multiplicar() que devuelva el producto de todos los números de una lista.


def inversa(string):
    return string[::-1]

# Case for one character string
assert inversa("a") == "a"

# Case for even number of characters
assert inversa("ho") == "oh"

# Case for odd number of characters
assert inversa("hol") == "loh"