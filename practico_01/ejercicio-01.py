# 1. Implementar una función max() que tome como argumento dos números y devuelva el mayor de ellos. 


def max(a, b):
   if a < b:
       return(b)
   return(a)


assert max (100, 2500) == 2500
assert max( 0, -7) == 0

