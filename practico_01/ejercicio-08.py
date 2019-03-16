# Definir una función superposicion() que tome dos listas y devuelva True 
# si tienen al menos 1 miembro en común o devuelva False de lo contrario.
# Escribir la función usando el bucle for anidado.

frutas = ['manzana', 'pera', 'durazno', 'limón' ]
frutas2 = ['banana', 'anana', 'pera', 'frutilla']

def superposicion(lista1,lista2):
    for item in lista1:
        if item in lista2:
            return True
            break
        else:
            return False



x = superposicion(frutas,frutas2)
print(x)
