# Implementar la función operacion, donde:
# - Si multiplicar es True: devolver la multiplicación entre a y b.
# - Si multiplicar es False: devolver la division entre a y b.
# - Si multiplicar es False y b es cero: imprimir por consola "Operación no valida".


def operacion(a, b, multiplicar):
    if (multiplicar == True):
        return a*b

    else:
        if(b==0):
            print('Operacion no valida')
            return 'Operacion no valida'

        else:
            return a/b



assert operacion(12,3,True) == 36;
assert operacion(12,3,False) == 4;
assert operacion(12,0,False) == 'Operacion no valida';
