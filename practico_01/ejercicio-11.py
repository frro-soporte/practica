"""11. Determinar la cantidad de dígitos de un número ingresado."""

valor = 1234
def con(x):
    mat = str(x)
    resultado = len(mat)
    return resultado

print(con(valor))
assert con(1234) == 4
