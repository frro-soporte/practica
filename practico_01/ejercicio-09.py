#Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n.
# Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx”

def generar_n_caracteres(num : int ,letra: chr(1)) :

    return num * letra


#Prueba de la función


assert(generar_n_caracteres(1,'x')== 'x')
assert(generar_n_caracteres(3,'x')== 'xxx')
