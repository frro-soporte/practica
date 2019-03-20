def inversa(cadena):
    cad_inv = ""
    for i in range(len(cadena)):
        cad_inv = cad_inv + cadena[len(cadena)-i-1]
    return cad_inv


assert inversa("Hola") == "aloH"
