"""15. A) Reescriba el programa que pide al usuario una lista de números e imprime en
pantalla el máximo y mínimo de los números introducidos al final, cuando el usuario
introduce “fin”.
B) Escriba ahora el programa de modo que almacene los números que el usuario
introduzca en una lista y usa las funciones max () y min () para calcular los números
máximo y mínimo después de que el bucle termine.
Por ej.:
Introduzca un número: 6
Introduzca un número: 2
Introduzca un número: 9
Introduzca un número: 3
Introduzca un número: 5
Introduzca un número: fin
Máximo: 9.0
Mínimo: 2."""
#EJERCICIO A
z=0
bandera= True
while z!= "fin":
    print("Introduzca un numero:")
    z = input()
    if bandera==True and z!= "fin":
        maxim=int(z)
        minim=int(z)
        bandera = False
    if z=="fin":
        break
    if int(z)>maxim:
        maxim=int(z)
    if int(z)<minim:
        minim=int(z)
print("Maximo:",maxim)
print("Minimo:",minim)

#EJERCICIO B
"""
x=0
numeros=[]
while x != "fin":
    print ("Introduzca un numero:")
    x = input()
    if x=="fin":
        break
    numeros.append(x)
print("Maximo:",max(numeros))
print("Minimo:",min(numeros))
"""
