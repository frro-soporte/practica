'''Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la
cadena "estoy probando" debería devolver la cadena "odnaborp yotse".'''

def inversa(a):
    b=a[::-1]
    return (b)

a = 'Hola como va'
assert(inversa(a)== 'av omoc aloH')

