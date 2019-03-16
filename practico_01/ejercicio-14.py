"""14. Programe un algoritmo recursivo que encuentre la salida de un laberinto, teniendo
en cuenta que el laberinto se tomó como entrada y que es una matriz de valores
True, False, (x,y) , donde True indica un obstáculo, False una celda donde se puede
caminar, (x,y) es el punto donde comienza a buscarse la salida y (a,b), la salida del
laberinto . """

Laberinto = [[True,False,"(x,y)"],[True,False,"(z,j)"],[False,True,"(k,m)"],[False,False,"(a,b)"]]

def labe(M):
    i=0
    while i<len(M):
        if ocupado(M[i][0],M[i][1]) is False:
            return M[i][2]
            break
        else:
            i=i+1


def ocupado(obstaculo,casilla):
    if obstaculo == True:
        return True
    if casilla == True:
        return True
    if obstaculo == False and casilla == False:
        return False

print (labe(Laberinto))
