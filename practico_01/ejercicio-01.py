
# 1. Implementar una función max() que tome como argumento dos números y devuelva el mayor de ellos. 


def max(x,y):
        if x>y:
            return x
        elif x<y:
           return y
        else: print('a y b son iguales')

assert max(10, 5) == 10
assert max(9, 18) == 18
