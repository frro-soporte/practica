def palindromo(cadena):
    index = 0
    invertida = ""
    cant = len(cadena)
    for index in range(cant):
        cant -=1
        invertida += invertida.join(cadena[cant])

    if cadena == invertida:
        return True
    else:
        return False

assert (palindromo(input('ingresar cadena')) == True)
assert (palindromo(input('ingresar cadena')) == False)
