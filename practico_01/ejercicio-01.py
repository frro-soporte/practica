'''Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos'''


def max(a,b):


  if(a>b):
    return a



  elif (a == b):
   return a
  else:
   return b

pass

a: int = int(input("Introduce un numero: "))
b: int = int(input("Introduce un numero: "))



assert max(0,1)==1
assert max(5,7)==7



