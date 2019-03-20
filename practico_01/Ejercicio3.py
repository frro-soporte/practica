def calc_listas(listita):
    i = 0
    while listita[i] is not None:
        i += 1
        try:
            listita[i]
        except:
            return i


assert calc_listas("hola") == 4