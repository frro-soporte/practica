# Implementar la función conversor, que ingrese desde la consola grados Celsius
# y los devuelva transformados a Fahrenheit.


def conversor(grados):
    farenheint=(grados*(9/5))+32
    return farenheint

assert conversor(1)==33.8
assert conversor(0)==32
assert conversor(-5)==23
assert conversor(-20)==-4
