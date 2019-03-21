#9. Definir una función generar_n_caracteres() que tome un entero n y devuelva el
#caracter multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") debería
#devolver "xxxxx”

def generar_n_caracteres(num, carac):
    lista = ''
    for i in range(num):
        lista = lista + carac
    print(lista)

generar_n_caracteres(5, 'x') == 'xxxxx'
