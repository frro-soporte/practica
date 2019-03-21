def maxymin():
    num = 'seguir'
    max = -9999999999
    min = 99999999999
    while num != "fin":
        print("Ingrese un valor, cuando desee cancelar inserte fin")
        num = input()
        if num == 'fin':
            pass
        else:
            num=int(num)
            print("El numero ingresado es: ", num)
            if num > max:
                max = num
            elif num < min:
                min = num
    print("El numero maximo es: ", max)
    print("El Numero minimo es: ", min)


def listamaxymin():
    lista = []
    num='seguir'
    while num != 'fin':
        print("Ingrese un valor, cuando desee cancelar inserte fin")
        num = input()
        if num == 'fin':
            pass
        else:
            print("El numero ingresado es: ", num)
            num=int(num)
            lista.append(num)
    print('El numero maximo es: ', max(lista))
    print('El numero minimo es: ', min(lista))


listamaxymin()
