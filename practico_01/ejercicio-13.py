'''Programe una función que determine si un número entero suministrado como argumento es primo.'''


def num_primo(a):


    if (a%2 ==0):
        return False

    else:

        return True



    pass


x = int(input("Ingrese un numero:"))

assert num_primo(3)==True
assert num_primo(4)==False