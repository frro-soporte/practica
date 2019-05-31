# Implementar la función mitad (), que devuelve la mitad de palabra.
# Si la longitud es impar, redondear hacia arriba.


# hola -> ho
# verde -> ver
def  mitad ( palabra ):
    if len(palabra)%2 == 0:
        subcad=palabra[0:len(palabra)//2]
    else:
        subcad=palabra[0:(len(palabra)//2)+1]
    return subcad

assert mitad("hola")=="ho"
assert mitad("verde")=="ver"
