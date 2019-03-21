#Programe una función que determine si un número entero suministrado como
#argumento es primo.


def primo(num):
    if type(num) is int:
        if num < 1:
            print('False')
            return False
        elif num == 2:
            print('True')
            return True
        else:
            for i in range(2, num):
                if num%i == 0:
                    print('False')
                    return False
            print('True')
            return True
    else:
        print('Ingrese un numero entero')
        return False


assert(primo(5)==True)

assert(primo(0.2)==False)

assert(primo(4)==False)

assert(primo(2)==True)

assert(primo(79)==True)
