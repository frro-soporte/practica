"""
Definir una función generar_n_caracteres() que tome un entero n y devuelva el
caracter multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") debería
devolver "xxxxx”
"""
def generar_n_caracteres (n, x):
    valor = ""
    for i in range (0, int(n)):
        valor = valor + x
    return valor



caracter = input("ingrese caracter ")
entero = input("ingrese entero ")

print(generar_n_caracteres(entero, caracter))

assert generar_n_caracteres(2,"x") == "xx"
assert generar_n_caracteres(3,"a") == "aaa"
