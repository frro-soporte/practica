#Escribir una función mas_larga() que tome una lista de palabras y devuelva la más larga

def mas_Larga(ls : list ) :
    for i in range(0,len(ls)-1) :
        for j in range(1,len(ls)) :
            if len(ls[i]) > len(ls[j]) :
                palabra  = ls[i]
            elif len(ls[i]) < len(ls[j]) :
                palabra = ls[j]
    return palabra


assert (mas_Larga(["Hi", "Esto es una prueba", "Soporte"]) == "Esto es una prueba")
