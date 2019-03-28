#Escribir una función que tome un carácter y devuelva True si es una vocal, de lo
#contrario devuelve False.



def esvocal(let):
    if (let=='a' or let=='e' or let=='i' or let=='o' or let=='u'):
        return True
    else:
        return False

assert(esvocal('q')==False)
