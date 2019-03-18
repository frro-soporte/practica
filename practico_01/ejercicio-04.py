#Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.

def es_vocal(x):

    if(x=='a'or x=='e'or x=='i' or x=='o' or x=='u'):

        print("True")



    else:
        print("False")


pass

a = input("introduce un cararter: ").lower()

es_vocal(a)
