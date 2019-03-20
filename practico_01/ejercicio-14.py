#Programe un algoritmo recursivo que encuentre la salida de un laberinto.

lab = [[True, False, True, True],
       [False, False, True, False],
       [True, True, True, False],
       [True, False, True, True]]


def salida_laberinto(fila, columna):
    if (fila == 3) and (columna ==1):
        print("Salida encontrada en posición: ", str(fila), ",", str(columna))

    elif (lab[fila][columna] == True):
        print("Obstaculo en posición: ", str(fila) + ",", str(columna))
        return False

    elif (lab[fila][columna] == False):
        print("Avanza a la posición: ", str(fila), ",", str(columna))
        lab[fila][columna] = 2

    elif (lab[fila][columna] == 2):
        print("Ya pasó por la posición: ", str(fila), ",", str(columna))
        return False

    salida = (salida_laberinto(fila+1, columna) or salida_laberinto(fila, columna+1) or salida_laberinto(fila-1, columna) or salida_laberinto(fila, columna-1))
    if salida:
        return True

    return False


a = 0
b = 1
salida_laberinto(a, b)
