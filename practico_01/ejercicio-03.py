# Implementar la función operacion, donde:
# - Si multiplicar es True: devolver la multiplicación entre a y b.
# - Si multiplicar es False: devolver la division entre a y b.
# - Si multiplicar es False y b es cero: imprimir por consola "Operación no valida".


def operacion(a, b, multiplicar):
    bool(multiplicar)
    if multiplicar:
       return(a*b)
    elif (multiplicar != True and b == 0):
        return("Operación No Válida")
    else:
        return(a/b)



assert operacion(8,2,False) == 4
assert operacion(7,2,True) == 14
assert operacion(7,0,False) == "Operacion No Valida"
