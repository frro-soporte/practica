def superposicion(cad1, cad2):
    for i1 in range(len(cad1)):
        for i2 in range(len(cad2)):
            if cad1[i1] == cad2[i2]:
                return True
    return False


assert superposicion("hola", "1234") is False
assert superposicion("hola", "hijo")

