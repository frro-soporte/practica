# Implementar la función operacion, donde:
# - Si multiplicar es True: devolver la multiplicación entre a y b.
# - Si multiplicar es False: devolver la division entre a y b.
# - Si multiplicar es False y b es cero: imprimir por consola "Operación no valida".

def operacion(a, b, multiplicar):
    if multiplicar == True:
        return a*b
    elif multiplicar == False:
        if b == 0:
            return print('Operación no valida')
        return a/b

assert operacion(2,2,True) == 4
assert operacion(2,2,False) == 1
assert operacion(2,0,False) == None
assert operacion(2,4,False) == 0.5