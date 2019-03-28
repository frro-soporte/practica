'''Definir una función superposicion() que tome dos listas y devuelva True si tienen al
menos 1 miembro en común o devuelva False de lo contrario. Escribir la función
usando el bucle for anidado.'''

def superposicion(a,b):
    for i in a:
        for j in b:
            if i==j:
                c = True
                return c
            c = False
    return c

a= ['a',1,'Hola']
b= [2,'a']
assert  (superposicion(a,b)== True)
