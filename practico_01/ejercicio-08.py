# Implementar la función mitad(), que devuelve la mitad de palabra.
# Si la longitud es impar, redondear hacia arriba.


# hola -> ho
# verde -> ver
def mitad(palabra):
    pass

    return palabra[0:len(palabra) // 2 if len(palabra) % 2 == 0 else ((len(palabra)//2)+1)]
    


palabraImpar = "hola"
palabraPar = "verde"

print(mitad(palabraImpar))
print(mitad(palabraPar))