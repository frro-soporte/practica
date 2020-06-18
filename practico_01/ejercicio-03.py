# Implementar la función operacion, donde:
# - Si multiplicar es True: devolver la multiplicación entre a y b.
# - Si multiplicar es False: devolver la division entre a y b.
# - Si multiplicar es False y b es cero: imprimir por consola "Operación no valida".


def operacion(a, b, multiplicar):
    if multiplicar:
        return a * b
    else:
        return a / b

bool = True
a=1
b=2

#assert operacion(a, b, bool)
print (operacion(a, b, bool))



