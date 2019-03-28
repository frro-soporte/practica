#Programe un algoritmo recursivo que encuentre la salida de un laberinto
# teniendo en cuenta que el laberinto se tomó como entrada y que es una matriz de valores True, False, (x,y)
# donde True indica un obstáculo, False una celda donde se puede caminar
# (x,y) es el punto donde comienza a buscarse la salida y (a,b), la salida del laberinto

#defino un laberinto

laberinto = [[True,True,False,True,True],
             [True,False,False,True,True],
             [True,False,False,False,"OUT"],
             [True,True,True,True,True]]
def empezarLaberinto(fil,col):
    if laberinto[fil][col] == "OUT":
        return 'WIN'
    aux1 = fil
    aux2=  col
    if (not laberinto[fil][col+1] or laberinto[fil][col+1]== "OUT"):
        aux2 = col + 1

    if (not laberinto[fil][col-1] or laberinto[fil][col-1]=="OUT"):

        if aux2 != col +1 :
            aux2 = col -1

    if (not laberinto[fil+1][col] or laberinto[fil+1][col]=="OUT"):

        if aux2 != col+1 and aux2 != col-1:
            aux1= fil + 1
    if(not laberinto[fil-1][col] or laberinto[fil-1][col]=="OUT"):
        if aux2 != col + 1 and aux2 != col-1 and aux1 != fil +1 :
            aux1 = fil -1

    print()
    empezarLaberinto(fil,col)


