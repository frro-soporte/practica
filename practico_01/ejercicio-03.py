# Implementar la función operacion, donde:
# - Si multiplicar es True: devolver la multiplicación entre a y b.
# - Si multiplicar es False: devolver la division entre a y b.
# - Si multiplicar es False y b es cero: imprimir por consola "Operación no valida".


def operacion(a, b, multiplicar):
    if not b and not multiplicar:
        print("Operacion no valida")
    elif multiplicar:
        return a*b
    else:
        return a/b
