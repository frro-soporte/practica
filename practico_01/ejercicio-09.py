'''Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n.
Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx”'''


def generar_n_caracter(a, b):


 b= a*b


 return b



pass


x=int(input("Ingrese un valor entero:"))
y=input("Ingrese un caracter:")

assert generar_n_caracter(5,'a')=='aaaaa'
assert generar_n_caracter(3,'b')=='bbb'