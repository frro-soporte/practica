#Programe un algoritmo recursivo que encuentre la salida de un laberinto.

mat = [[True, True, True, False],
       [False, False, True, False],
       [True, True, True, False],
       [False, True, True, True]]


def salida_laberinto(fila, columna):
    if (fila == 3) and (columna ==1):
        print("Salida encontrada en posición: ", str(fila), ",", str(columna))

    elif (mat[fila][columna] == True):
        print("Obstaculo en posición: ", str(fila) + ",", str(columna))
        return False

    elif (mat[fila][columna] == False):
        print("Avanza a la posición: ", str(fila), ",", str(columna))
        mat[fila][columna] = 2

    elif (mat[fila][columna] == 2):
        print("Ya pasó por la posición: ", str(fila), ",", str(columna))
        return False

    salida = (salida_laberinto(fila+1, columna) or salida_laberinto(fila, columna+1) or salida_laberinto(fila-1, columna) or salida_laberinto(fila, columna-1))
    if salida:
        return True

    return False


p1 = 0
p2 = 1
salida_laberinto(p1, p2)
