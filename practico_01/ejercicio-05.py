# Escribir una función multip() que multiplique respectivamente todos los números de una lista. Por ejemplo: multip([1,2,3,4]) debería devolver 24.

def multiplicar(list):
    acum= 1
    for i in range(len(list)):
        acum = list[i] * acum

    return acum


pass



assert multiplicar([1,2,3,4])==24
assert multiplicar([1,2,3,5])==30


