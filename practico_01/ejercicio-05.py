#5. Escribir una función multip() que multiplique respectivamente todos los números de
#una lista. Por ejemplo: multip([1,2,3,4]) debería devolver 24

def multip(lista):
    i=0
    sum = 1
    for num in lista:
        sum = sum*lista[i]
        i = i + 1
    print(sum)
    return sum

multip([5, 2, 3])
