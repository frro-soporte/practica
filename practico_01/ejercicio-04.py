#Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.

def es_vocal(x):

    if(x=='a'or x=='e'or x=='i' or x=='o' or x=='u'or x=='A'or x=='E'or x=='I' or x=='O' or x=='U'):

        return True



    else:
        return False


pass

assert es_vocal('a')==True
assert es_vocal('g')==False
assert es_vocal('A')==True
assert es_vocal('M')==False
