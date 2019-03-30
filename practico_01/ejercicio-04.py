def esVocal(caracter) -> bool:
    vocales = ["a", "e", "i", "o", "u"]

    if caracter in vocales:
        return True
    return False



assert (esVocal(input('Ingresar letra')) == True)

assert (esVocal(input('Ingresar letra')) == False)

