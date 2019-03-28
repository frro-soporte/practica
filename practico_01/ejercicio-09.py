#Definir una función generar_n_caracteres() que tome un entero n y devuelva el
#caracter multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") debería
#devolver "xxxxx”

def genera_n_caracteres(n,carac):
    res=n*carac
    return res
assert (genera_n_caracteres(4,"g")=="gggg")
