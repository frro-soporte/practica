def multip(lista):
    mul = 1
    for i in range(len(lista)):
        mul = mul * lista[i]
    return mul


assert multip([1, 2, 3, 4]) == 24
