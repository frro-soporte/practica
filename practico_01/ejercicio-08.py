# Implementar la función mitad(), que devuelve la mitad de palabra.
# Si la longitud es impar, redondear hacia arriba.


# hola -> ho
# verde -> ver
def mitad(palabra):
    a = len(palabra)
    a = (a//2) + (a%2)
    return(palabra[0:a])

assert mitad('verde') == 'ver'