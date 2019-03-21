## Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse".

def inversa(cad):
    reves = cad[::-1]

    return reves

    pass


cadena = input("Ingrese la cadena de valores:")

assert inversa('tasa')=='asat'
assert inversa('casa')=='asac'
