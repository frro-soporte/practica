# Implementar la función es_palindromo(), que devuelva un booleano en base a
# si palabra se lee igual de corrido como al revés.


# Ejemplos: arenera, radar, ojo, oso, salas.
# Resolver sin utilizar loops (for/while), sino con slicing.
def es_palindromo(palabra):
    if palabra == palabra[::-1]:
        return True
    else:
        return False


def main():
    pal = input("Ingrese palabra: ")
    if es_palindromo(pal):
        print("Es palindromo")
    else:
        print("No es palindromo")


main()
