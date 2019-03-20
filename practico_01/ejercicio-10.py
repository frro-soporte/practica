def mas_larga(lista):
    long = []
    for i in range(len(lista)):
        long.append(len(lista[i]))
    return lista[long.index(max(long))] #Devuelve solo la primera en caso que haya cadenas de igual longitud (consultar)


assert mas_larga(["hola","mama","jajaja","Mercury"]) == "Mercury"
