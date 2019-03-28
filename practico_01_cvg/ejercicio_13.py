# Programe una función que determine si un número entero suministrado como argumento es primo
def esPrimo (num):
    if num < 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range (2, num):
            if (num % i) == 0:
                return False
        return True

def app():
    num = int(input("ingrese un numero :"))

    if(esPrimo(num)):
        print("El numero es primo")
    else:
        print("El numero no es primo")

    assert esPrimo(2) == True
    assert esPrimo(4) == False

if __name__ == '__main__':
    app()