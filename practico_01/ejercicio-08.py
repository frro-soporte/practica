#Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común
# o devuelva False de lo contrario.
# Escribir la función usando el bucle for anidado


def superposicion(a: list, b: list )  -> bool:

    for i in range(0,len(a)-1):
        for j in range(0,len(b)-1):
            if a[i] == b[j]:
                return True
    return False


## Prueba de la función

a=['a' , 'b' , 'c', 'd' , 'e' , 'f']
b=['c', 'r', 'k','i']
c=[1,2,3,4,5]

assert (superposicion(a,b)== True)
assert (superposicion(a,c)== False )
