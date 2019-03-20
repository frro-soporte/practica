#ParteB
numeros = []
num = input("Ingrese el numero o fin para finalizar el ingreso ")
num = num.lower()
while (not num.isdigit()) and (num != "fin"):
    num = input("Ingrese solo numeros o fin para finalizar el ingreso ")
    num = num.lower()
while num != "fin":
    numeros.append(int(num))
    num = input("Ingrese el numero o fin para finalizar el ingreso ")
    num = num.lower()
    while (not num.isdigit()) and (num != "fin"):
        num = input("Ingrese solo numeros o fin para finalizar el ingreso ")
        num = num.lower()
if len(numeros) == 0:
    print("No ha ingresado ningun numero")
else:
    print("El mayor es: ", max(numeros))
    print("El menor es: ", min(numeros))
