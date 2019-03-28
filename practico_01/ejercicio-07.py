def palindromo(cadena):
    index = 0
    invertida = ""
    cant = len(cadena)
    for index in range(cant):
        cant -=1
        invertida += invertida.join(cadena[cant])

    if cadena == invertida:
        print("Es palindromo")
    else:
        print("No es palindromo")


palindromo(input('ingresar cadena'))
