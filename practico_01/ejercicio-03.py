# Implementar la función operacion, donde:
# - Si multiplicar es True: devolver la multiplicación entre a y b.
# - Si multiplicar es False: devolver la division entre a y b.
# - Si multiplicar es False y b es cero: imprimir por consola "Operación no valida".

def operacion(a,b,multiplicar):
    if multiplicar:
        return (a*b)
    elif (b==0):
        return 'Operacion no valida'
    else:
        return (a/b)

assert operacion(8,2,True) ==  16
assert operacion(8,2,False) ==  4
assert operacion(8,0,False) == 'Operacion no valida'
