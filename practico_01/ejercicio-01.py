# 1. Implementar una función max() que tome como argumento dos números y devuelva el mayor de ellos. 


def max(a, b):
   if a < b:
       return(b)
   return(a)


print("Ingresar numero 1: ")
num1 = input()
print("Ingresar numero 2: ")
num2 = input()


print("El número max es: ",max(num1,num2))
