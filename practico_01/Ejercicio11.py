'''Determinar la cantidad de dígitos de un número ingresado.'''
def contar(a):
    return str(a).__len__()

a = 821341
assert contar(a)==6

