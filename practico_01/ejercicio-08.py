'''Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario.
Escribir la función usando el bucle for anidado.'''


def superposicion(a,b):
 cont=0

 for i in range(0,len(a)):

  for j in range(0,len(b)):

    if(a[i]==b[j]):
       cont = cont + 1

 if (cont > 0):
     return "TRUE"

 else:

     return "False"




pass


x=[1,2,3,4,5]

y=[0,7,8,1,8]

resultado=superposicion(x,y)

print(resultado)