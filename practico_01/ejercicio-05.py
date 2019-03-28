# Escribir una función multip() que multiplique respectivamente todos los números de
# una lista. Por ejemplo: multip([1,2,3,4]) debería devolver 24.
def multip(lista):
    res=1
    for i in lista:
        res=res*i
    return res
assert (multip([2,2,2,2])==16)
