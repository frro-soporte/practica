# Implementar la función conversor, que ingrese desde la consola grados Celsius
# y los devuelva transformados a Fahrenheit.


def conversor(grados):
    return(grados* (9/5) + 32)

assert conversor(32) == 89.6