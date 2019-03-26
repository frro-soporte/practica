# Implementar la función operacion, donde:
# - Si multiplicar es True: devolver la multiplicación entre a y b.
# - Si multiplicar es False: devolver la division entre a y b.
# - Si multiplicar es False y b es cero: imprimir por consola "Operación no valida".


def operacion(a, b, multiplicar):
    if multiplicar is True:
        return a * b
    elif multiplicar is False and b != 0:
        return a / b
    elif multiplicar is False and 0 == b:
        return 'Operacion no valida'

assert operacion(2,3,True)== 6
assert operacion(4,2,False)== 2
assert operacion(4,0,False)=='Operacion no valida'
