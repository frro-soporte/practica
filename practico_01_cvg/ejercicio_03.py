x = "cadenadeprueba"

def calcula_longitud (a):
    return len(a)

cadena = input('Ingrese cadena a calcular longitud ')
print(calcula_longitud(cadena))

assert calcula_longitud("hola") == 4
assert calcula_longitud("como estas") == 10