#Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.

def mayor(a, b, c):

   if(a>b and a>c):
       print("El mayor numero imgresado es: "+str(a))

   elif(b>a and b>c):

       print("El mayor numero imgresado es: "+str(b))

   elif(a==b and a==c):

       print("El mayor numero ingresado es: "+str(a))


   elif(c>a and c>b):
       print("El mayor numero imgresado es: " + str(c))

   elif(a==b and a>c ):

       print("El mayor numero imgresado es: " + str(a))

   elif (a == b and a < c):

       print("El mayor numero imgresado es: " + str(c))

pass

x:int=int(input("Introduce un numero: "))

y: int=int(input("Introduce un numero: "))

z: int=int(input("Introduce un numero: "))
mayor(x,y,z)