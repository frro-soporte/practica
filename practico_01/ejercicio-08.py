# Implementar la función mitad(), que devuelve la mitad de palabra.
# Si la longitud es impar, redondear hacia arriba.


def mitad(palabra):
    long=len(palabra)
    if type(long/2) == float:
        tope = (long/2) + 0.5
        return palabra[0:int(tope)]
    else:
        tope=(long/2)
        return palabra[0:tope]

assert mitad('hola') == 'ho'
assert mitad('verde') == 'ver'
