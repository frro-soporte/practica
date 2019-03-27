#Programe un algoritmo recursivo que encuentre la salida de un laberinto, teniendo
#en cuenta que el laberinto se tomó como entrada y que es una matriz de valores
#True, False, (x,y) , donde True indica un obstáculo, False una celda donde se puede
#caminar, (x,y) es el punto donde comienza a buscarse la salida y (a,b), la salida del
#laberinto


def busca_salida(m):
    for i in range (0,len(m)):        #funcion donde se fija en la matriz si hay un 
                                      # False a la derecha, abajo, a la izquierda o arriba
                                      # si tiene que volver por donde ya pasó, vuelve.
        for j in range(0,len(m[i])):
            if (not m[i][j+1] or m[i][j+1]=="x"):
                m[i][j+1]="x"
                return m
            else:
                if (not m[i+1][j]or m[i+1][j]=="x"):
                    m[i+1][j]="x"
                    return m
                else:
                    if (not m[i][j-1]or m[i][j-1]=="x"):
                        m[i][j-1]="x"
                        return m
                    else:
                        if (not m[i-1][j]or m[i-1][j]=="x"):
                            m[i-1][j]="x"
                            return m
    busca_salida(m)   #no tengo muy claro como hacerlo recursivo sin que produzca error de indice


mat=([["x", True, True, True, False, False, True],  #creacion del laberinto con obstaculos
     [False, False, False, True, True, False, True], #"x" es el objeto que recorre el laberinto
     [True, False, True, True, False, False, False],
     [True, False, False, False, False, True, True]])

print(busca_salida(mat))
