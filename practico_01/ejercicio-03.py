# Implementar la función operacion, donde:
# - Si multiplicar es True: devolver la multiplicación entre a y b.
# - Si multiplicar es False: devolver la division entre a y b.
# - Si multiplicar es False y b es cero: imprimir por consola "Operación no valida".


def operacion(a, b, multiplicar):
    if multiplicar:
        return a * b
    else:
        if b == 0:
            print("Operacion no valida")
            return 0
        else:
            return a / b


assert operacion(5, 2, 1) == 10
assert operacion(10, 2, 0) == 5
assert operacion(10, 0, 0) == 0
assert operacion(10, 0, 1) == 0

