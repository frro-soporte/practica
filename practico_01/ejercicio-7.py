def es_palindromo(cadena):
    cad_inv = ""
    cadena = cadena.lower()
    for i in range(len(cadena)):
        cad_inv = cad_inv + cadena[len(cadena)-i-1]
    if cadena == cad_inv:
        return True
    else:
        return False


assert es_palindromo("Radar")
assert es_palindromo("Hola") is False
