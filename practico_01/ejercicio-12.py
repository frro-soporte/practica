#Determinar la suma de todos los numeros de 1 a N. N es un número que se ingresa por consola.

def SumaAN(n):
    a = 0
    for i in range(1, n+1):
        a = a + i
    print(a)

def main():
    SumaAN(int(input("Ingrese numero: ")))


main()
