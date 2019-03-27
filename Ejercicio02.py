def max_de_3(a, b, c):
    if a >= b:
        if a >= c:
            return a
        else:
            return c
    else:
        if b >= c:
            return b
        else:
            return c

assert(max_de_3(5,4,10)==10)
assert(max_de_3(5,10,10)==10)
assert(max_de_3(10,4,5)==10)
