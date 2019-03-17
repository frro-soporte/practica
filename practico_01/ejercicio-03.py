# Implementar la función operacion, donde:
# - Si multiplicar es True: devolver la multiplicación entre a y b.
# - Si multiplicar es False: devolver la division entre a y b.
# - Si multiplicar es False y b es cero: imprimir por consola "Operación no valida".


def operacion(a, b, multiplicar):
    if multiplicar:
        return a*b
    if multiplicar == False:
        if b == 0:
            print("Operación no valida")
        return a/b

print(operacion (1,0,False))
