#Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la
# cadena "estoy probando" debería devolver la cadena "odnaborp yotse".


def inversa (cadena):

    return cadena [::-1]

cadena = input("inrese una cadena \n")
print(inversa(cadena))

assert inversa("hola como estas ") == "satse omoc aloh"