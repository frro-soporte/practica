#Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False

vocales = ["a", "e", "i", "o", "u"]

def is_vocal (letra):
    for i in range (0, (len(vocales))):
        if letra == vocales[i]:
            return True
    return False

vocal = input("ingrese la letra a evaluar: \n")
print(is_vocal(vocal))

assert is_vocal("a") == True
assert is_vocal("g") == False
