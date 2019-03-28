# Determinar la cantidad de dígitos de un número ingresado.
def cant_digitos(num):
    cont = 1
    if num< 9:
        return 1
    while num > 9:
        num = num /10
        cont = cont +1
    return cont

#Prueba de la función

assert(cant_digitos(1)== 1)
assert(cant_digitos(100)== 3)
