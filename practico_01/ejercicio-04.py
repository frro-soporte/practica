# Implementar la función conversor, que ingrese desde la consola grados Celsius
# y los devuelva transformados a Fahrenheit.


def conversor(grados):
    x=(grados * 9/5)+ 32
    return x

assert conversor(45) == 113
