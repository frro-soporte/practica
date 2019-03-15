# Implementar la función numeros_al_final(), que mueve todos los elementos numéricos
# de lista al final de esta. Devuelve la lista.


# Resolver sin utilizar lista auxiliar
def es_palindromo(string):
    return string == string[::-1]

# Case for palindrome
assert es_palindromo("rayar") is True

# Case for non-palindrome
assert es_palindromo("amor") is False