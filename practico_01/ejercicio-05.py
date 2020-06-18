# Implementar la función es_vocal, que reciba un carácter y
# devuelva un booleano en base a si letra es una vocal o no.


# Resolver utilizando listas y el operador in.
def es_vocal(letra):
    if letra in ('a','e','i','o','u') :
        return True
    else:
        return False

def main():
    a = input("Ingrese caracter: ")
    if es_vocal(a):
        print("Es vocal")
    else:
        print("Es consonante")


main()
