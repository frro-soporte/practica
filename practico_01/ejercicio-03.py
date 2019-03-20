def calc_listas(listita):
    i = 0
    while listita[i] is not None:
        i += 1
        try:
            listita[i]
        except:
            return i


assert calc_listas("hola") == 4
assert calc_listas([1, 2, 3, 4]) == 4