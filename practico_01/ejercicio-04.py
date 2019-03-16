# Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.


def esvocal(v):
    if v=='a' or v=='e' or v=='i' or v=='o' or v=='u' or v=='A' or v=='E' or v=='I' or v=='O' or v=='U':
        return True
    else:
        return False


assert esvocal('a') == True
assert esvocal('b') == False
    