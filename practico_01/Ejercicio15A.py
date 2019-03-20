#ParteA
max = 0
vof = False
num = input("Ingrese el numero o fin para finalizar el ingreso ")
num = num.lower()
while (not num.isdigit()) and (num != "fin"):
    num = input("Ingrese solo numeros o fin para finalizar el ingreso ")
    num = num.lower()
if num != "fin":
    min = int(num)
else:
    print("No ha ingresado ningun numero")
    vof = True
while num != "fin":
    num = int(num)
    if num > max:
        max = num
    if num < min:
        min = num
    num = input("Ingrese el numero o fin para finalizar el ingreso ")
    num = num.lower()
    while (not num.isdigit()) and (num != "fin"):
        num = input("Ingrese solo numeros o fin para finalizar el ingreso ")
        num = num.lower()
if vof is False:
    print("El minimo es: ", min)
    print("El maximo es: ", max)


