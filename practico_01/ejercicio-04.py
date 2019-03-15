# Implementar la función conversor, que ingrese desde la consola grados Celsius
# y los devuelva transformados a Fahrenheit.


def is_vocal(char):
    return char.lower() in 'aeiou'

# Case for vowels
assert is_vocal('a') is True
assert is_vocal('e') is True
assert is_vocal('i') is True
assert is_vocal('o') is True
assert is_vocal('u') is True

# Case for non-vowels
assert is_vocal('g') is False
