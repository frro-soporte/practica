# Escribir una funcin que tome un caracter y devuelva True si es Vocal, de lo contrario devuelve false



def esvocal(let):
    if let=="a" or let=="e" or let=="i" or let=="o" or let=="u":
        return True
    else:
        return False

assert (esvocal("v") == False)
assert (esvocal("a") == True)
