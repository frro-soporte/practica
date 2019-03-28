def inversa(cadena):
    index = 0
    invertida = ""
    cant = len(cadena)
    for index in range(cant):
        cant -=1
        invertida += invertida.join(cadena[cant])
    print(invertida)

inversa(input('ingresar cadena'))
