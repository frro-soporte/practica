def multiplicar(lista):
    mult=lista[0]
    for i in lista:
        mult = mult * i
    return (mult)


lista=[1,2,3,4]
assert  (multiplicar(lista)==24)


