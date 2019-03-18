# Implementar la función conversor, que ingrese desde la consola grados Celsius
# y los devuelva transformados a Fahrenheit.


def conversor(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    print(celsius, '° Celsius son ',fahrenheit, '° Farhenheit')

grados = int(input('Ingrese grados en celsius: '))
conversor(grados)
