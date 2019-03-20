def max_de_3(n1, n2, n3):
    if(n1 > n2) and (n1 > n3):
        return n1
    if (n2 > n3) and (n2 > n1):
        return n2
    if (n3 > n1) and (n3 > n2):
        return n3


assert max_de_3(12, 15, 20) == 20

