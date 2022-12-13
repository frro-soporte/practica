# Implementar la función conversor, que ingrese desde la consola grados Celsius
# y los devuelva transformados a Fahrenheit.


def conversor(grados):
    return grados * 9/5 + 32


# (0°C × 9/5) + 32 = 32°F

c = int(input("Ingrese Grados Celcius: "))
print(conversor(c))
