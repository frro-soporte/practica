""" 5. Escribir una función multip() que multiplique respectivamente todos los números de
una lista. Por ejemplo: multip([1,2,3,4]) debería devolver 24."""

cadena = [3,1,2,6]

def multip(x):
    cont=1
    for v in x:
        cont=cont*v
    return cont

print(multip(cadena))

assert multip(cadena) == 36
