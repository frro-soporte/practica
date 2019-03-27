'''A) Reescriba el programa que pide al usuario una lista de números e imprime en pantalla el máximo y mínimo
de los números introducidos al final, cuando el usuario introduce “fin”.'''


def listaNumero():
 max = min = 0

 valor = input("Ingresar valor ('fin' para finalizar):")


 while valor.lower() != 'fin':
   if  max==0 and min==0:
       max=min=int(valor)
   if int(valor) > max:
       max=int(valor)
   if int(valor) < min:
      min = int(valor)

   valor = input("Ingresar valor ('fin' para finalizar):")

 print("El maximo valor es:%s " % max)
 print("El minimo valor es: %s" % min)
 pass


listaNumero()


'''B) Escriba ahora el programa de modo que almacene los números que el usuario introduzca en una lista 
y usa las funciones max () y min () para calcular los números máximo y mínimo después de que el bucle termine.
Por ej.:
Introduzca un número: 6
Introduzca un número: 2
Introduzca un número: 9
Introduzca un número: 3
Introduzca un número: 5
Introduzca un número: fin
Máximo: 9.0
Mínimo: 2.'''

valores=[]

def listaMAXIMIN():

 valor = input("Ingresar valor ('fin' para finalizar):")

 while valor.lower() != 'fin':
     valores.append(valor)
     valor = input("Ingresar valor ('fin' para finalizar):")

 print("El maximo valor es:%s " % max(valores))
 print("El minimo valor es: %s" % min(valores))
 pass


listaMAXIMIN()