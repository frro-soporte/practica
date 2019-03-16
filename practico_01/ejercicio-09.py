"""9. Definir una función generar_n_caracteres() que tome un entero n y devuelva el
caracter multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") debería
devolver "xxxxx” """

car = "z"
num = 7

def generar_n_caracteres(cant,caract):
    respuesta= caract * cant
    return respuesta

print (generar_n_caracteres(num,car))
assert generar_n_caracteres(7,"z") == "zzzzzzz"
