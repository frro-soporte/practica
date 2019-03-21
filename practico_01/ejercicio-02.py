#Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.

def mayor(a, b, c):

   if(a>b and a>c):
      return a

   elif(b>a and b>c):

       return b

   elif(a==b and a==c):

       return a


   elif(c>a and c>b):
       return c

   elif(a==b and a>c ):

       return a

   elif (a == b and a < c):

       return c

pass


assert mayor(1,2,3)==3
assert mayor(5,2,4)==5