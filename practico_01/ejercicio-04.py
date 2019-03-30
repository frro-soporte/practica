# Implementar la función conversor, que ingrese desde la consola grados Celsius
# y los devuelva transformados a Fahrenheit.

def conversor(grados):
    far=((grados*9/5)+32)
    return far

grados = float(input('Introduzca una temperatura en grados celsius: '))
print('\nLa temperatura en Farenheit es: ',conversor(grados))
