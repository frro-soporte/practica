'''Programe una función que determine si un número entero suministrado como argumento es primo.'''


def num_primo(a):


    if (a%2 ==0):
        return ("El numero ingresado no primo:" + str(a))

    else:

        return ("El numero ingresado es primo:" + str(a))



    pass


x = float(input("Ingrese un numero:"))

resultado = num_primo(x)

print(resultado)
