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

mayor =max(a,b)

print("El mayor numero es :"+ str(mayor))



