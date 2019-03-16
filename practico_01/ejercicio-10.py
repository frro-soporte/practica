# Escribir una función mas_larga() que tome una lista de palabras y devuelva la más larga

numeros = ['123456', '12345678910', '12345678','123456789']
letras = ['a','aei','aeiou','aeio','ae']

def mas_larga(lista):
    maslargo = len(lista[0])
    numero = lista[0]

    for num in lista:
        if maslargo <= len(num):
            numero = num
            maslargo = len(num)
        else:
            numero = numero

    return numero

assert mas_larga(numeros)=='12345678910'
assert mas_larga(letras)=='aeiou'
