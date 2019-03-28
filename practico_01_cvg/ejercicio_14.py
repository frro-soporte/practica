"""
Programe un algoritmo recursivo que encuentre la salida de un laberinto, teniendo en cuenta que el
laberinto se tomó como entrada y que es una matriz de valores True, False, (x,y),
donde True indica un obstáculo, False una celda donde se puede caminar,
(x,y) es el punto donde comienza a buscarse la salida y (a,b), la salida del laberinto .

"""
import os

def laberinto (matriz,posicion, salida):
    print("\n"*50)
    os.system('cls')
    x = posicion[0] #coordenada x
    y = posicion[1] #coordenada y
    #print(posicion , salida)
    print_matriz(matriz, posicion)
    if(is_final(matriz,posicion, salida)) == True:
        print ("Laberinto completado")
    else:

        if (can_move_right(matriz,x,y)) == True:
            posicion[1]=posicion[1]+1
            laberinto(matriz,posicion, salida)
        elif (can_move_bottom(matriz,x,y)) == True:
            posicion[0] = posicion[0] + 1
            laberinto(matriz, posicion, salida)
        elif (can_move_up(matriz,x,y)) == True:
            posicion[0] = posicion[0] -1
            laberinto(matriz, posicion, salida)
        else:
            print ("Hubo un error y no se pudo completar el laberinto")

def print_matriz(matriz, posicion):
    matriz2 = matriz
    x = posicion[0]  # coordenada x
    y = posicion[1]  # coordenada y
    matriz2[x][y] = '#'
    for i in range(0,4):
        print(matriz2[i])


def is_final (matriz,posicion, salida):
    x = posicion[0]  # coordenada x de la posicion actual
    y = posicion[1]  # coordenada y de posicion actual

    if (posicion == salida):
        return True
    else:
        return False



def can_move_right (matriz,x,y):
    if (matriz[x][y+1]) == False:
        return True
    else:
        return False

def can_move_up(matriz,x,y):
    if (x==0):
        return False
    else:
        if(matriz[x-1][y])== False:
            return True
        else:
            return False

def can_move_bottom(matriz,x,y):
    if(x==3):
        return False
    else:
        if(matriz[x+1][y])== False:
            return True
        else:
            return False

matriz = [[True,True,True,True],[True,False,False,False],[False,False,True, True],[True,True,True,True]]
entrada = [2,0]
salida = [1,3]

"""
print(laberinto(matriz,entrada, salida))

matriz = [[True,True,False,False],[True,False,False,True],[False,False,True, True],[True,True,True,True]]
entrada = [2,0]
salida = [0,3]

print(laberinto(matriz,entrada, salida))

"""



