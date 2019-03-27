#Definir una función superposicion() que tome dos listas y devuelva True si tienen al
#menos 1 miembro en común o devuelva False de lo contrario. Escribir la función
#usando el bucle for anidado.

def superposicion(lis1,lis2):
    for i in lis1:
        for j in lis2:
            if(i==j):
                return True
    return False
assert (superposicion("ho","la")==False)
