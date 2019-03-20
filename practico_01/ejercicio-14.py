def laberinto(lab, rec_lab, x, y, a, b, mov, vof):
    if (x == a) and (y == b):
        vof.append(True)
        rec_lab[x][y] = True
        return rec_lab, vof
    else:
        rec_lab[x][y] = True
        if (lab[x+1][y] is False) and (rec_lab[x+1][y] is False) and (vof[len(vof)-1] is False):
            laberinto(lab, rec_lab, x + 1, y, a, b, "x+", vof)
        if (lab[x][y+1] is False) and (rec_lab[x][y+1] is False) and (vof[len(vof)-1] is False):
            laberinto(lab, rec_lab, x, y + 1, a, b, "y+", vof)
        if (lab[x][y-1] is False) and (rec_lab[x][y-1] is False) and (vof[len(vof)-1] is False):
            laberinto(lab, rec_lab, x, y - 1, a, b, "y-", vof)
        if (lab[x-1][y] is False) and (rec_lab[x-1][y] is False) and (vof[len(vof)-1] is False):
            laberinto(lab, rec_lab, x - 1, y, a, b, "x-", vof)
        elif vof[len(vof)-1] is False:
            if mov == "x+":
                x = x - 1
                return rec_lab, x, vof
            if mov == "x-":
                x = x + 1
                return rec_lab, x, vof
            if mov == "y+":
                y = y - 1
                return y, rec_lab, vof
            if mov == "y-":
                y = y + 1
                return y, rec_lab, vof
    return vof[len(vof)-1]



lab = [[True, True, True, True, True, True],
       [False, False, False, False, False, True],
       [True, True, False, True, False, True],
       [True, True, False, True, False, True],
       [True, False, False, True, False, True],
       [True, True, True, True, False, True]]
x = len(lab)
y = len(lab[0])
rec_lab = [[False for i in range(y)] for j in range(x)]
vof = [False]
assert laberinto(lab, rec_lab, 1, 0, 5, 4, "", vof)




