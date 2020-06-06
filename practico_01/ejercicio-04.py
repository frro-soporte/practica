# Implementar la función conversor, que ingrese desde la consola grados Celsius
# y los devuelva transformados a Fahrenheit.


def conversor(grados):
    celsius = float(grados) * 9/5 + 32
    return celsius


def main():
    print(conversor(float(input("Ingrese grados celsius: "))))
