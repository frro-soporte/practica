# Definir una función inversa() que calcule la inversión de una cadena.
# Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse". 


def inversa(c):
    inv= c[::-1]
    return inv

assert inversa('hola')=='aloh'
