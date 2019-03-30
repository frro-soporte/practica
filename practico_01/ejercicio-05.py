def multip():
    numeros = [1,2,3,4]
    resultado = 1
    for numero in numeros:
        resultado = resultado*numero
    return resultado

#multip()

assert (multip() == 24)
