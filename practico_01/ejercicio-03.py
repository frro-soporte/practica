# Implementar la función operacion, donde:
# - Si multiplicar es True: devolver la multiplicación entre a y b.
# - Si multiplicar es False: devolver la division entre a y b.
# - Si multiplicar es False y b es cero: imprimir por consola "Operación no valida".


def operacion(a, b, multiplicar):
    if multiplicar:
        return a * b
    if b == 0:
        print("operacion no valida")
        return False
    return a / b


assert operacion(8, 2, True) == 16
assert operacion(8, 2, False) == 4
assert not operacion(8, 0, False)
