#3. Definir una función que calcule la longitud de una lista o una cadena dada

matriz = 'hola'
matriz2 = ['h','o','x']

def long(x):
    contador = 0
    for can in x:
        contador=contador+1
    return contador

print(long(matriz))
print(long(matriz2))

assert long(matriz) == 4
assert long(matriz2) == 3
