# Implementar la función mitad(), que devuelve la mitad de palabra.
# Si la longitud es impar, redondear hacia arriba.


# hola -> ho
# verde -> ver
def mitad(palabra):
    l=len(palabra)
    if l%2==0:
        l=l//2
    else:
        l=(l+1)//2
    mitadpalabra=palabra[:l]
    return mitadpalabra

assert mitad('hola') == 'ho'
assert mitad('verde') == 'ver'