# Implementar la función conversor, que ingrese desde la consola grados Celsius
# y los devuelva transformados a Fahrenheit.



def conversor(grados):
    return(grados * (9/5) + 32)


assert conversor(0) == 32
assert conversor(23) == 73.4
assert conversor(450) == 842
