# Implementar la función operacion, donde:
# - Si multiplicar es True: devolver la multiplicación entre a y b.
# - Si multiplicar es False: devolver la division entre a y b.
# - Si multiplicar es False y b es cero: imprimir por consola "Operación no valida".


def operacion(a, b, multiplicar):
    if multiplicar == True:
        return (a*b)
    else:
        if b==0:
            print ("Operación no valida")
        else:
            return (a/b)

assert operacion(1,10,True) == 10
assert operacion(25,5,False) == 5
