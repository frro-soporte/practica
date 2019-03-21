# 3. Definir una función que calcule la longitud de una lista o una cadena dada.

def longitud(cadena):
    i = 0
    if type(cadena) is str or type(cadena) is list:
        for iteracion in cadena:
            i = i + 1
    print(i)
    return i


a = ['a', 1, 1]

assert(longitud(a) == 3)
assert(longitud('pizza') == 5)
