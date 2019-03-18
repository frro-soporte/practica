# Implementar la función operacion, donde:
# - Si multiplicar es True: devolver la multiplicación entre a y b.
# - Si multiplicar es False: devolver la division entre a y b.
# - Si multiplicar es False y b es cero: imprimir por consola "Operación no valida".

def operacion(a, b, multiplicar):
    if multiplicar is True :
        return a*b
    elif multiplicar is False and b != 0:
        return a/b
    elif multiplicar is False :
        return 'Operacion no valida'



assert operacion(10,5,False) == 2
assert operacion(10,5,True) == 50
assert operacion(10,0,False) == 'Operacion no valida'

