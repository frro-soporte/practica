#Programe una funcion que determine si un numero entero suministrado como argumento es primo .

def es_primo(numero):
    b = True
    for i in range (2,numero):
        if numero % i == 0:
            b = False
            break
    if b:
        print("Es primo")
    else:
        print("No es primo")


def main():
    es_primo(int(input("Ingrese numero: ")))


main()
