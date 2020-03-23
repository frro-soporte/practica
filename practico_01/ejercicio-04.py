# Implementar la función conversor, que ingrese desde la consola grados Celsius
# y los devuelva transformados a Fahrenheit.

# (0 °C × 9/5) + 32 = 32 °F
def conversor(grados):
    return grados * 9 / 5 + 32


print("Ingrese grados celcius:")
grados = int(input())
print(conversor(grados))
