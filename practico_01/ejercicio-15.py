#A) Reescriba el programa que pide al usuario una lista de números e imprime en
#pantalla el máximo y mínimo de los números introducidos al final, cuando el usuario
#introduce “fin”.

#B) Escriba ahora el programa de modo que almacene los números que el usuario
#introduzca en una lista y usa las funciones max () y min () para calcular los números
#máximo y mínimo después de que el bucle termine.

#A)
def maxiymini(lis):
    maximo=0
    minimo=2**30
    for i in lis:
        if (type(i)==int):
            if (maximo<i):
                maximo=i
            if(minimo>i):
                minimo=i

    return[maximo,minimo]
    
lista=[20,40,50,80,10,1,87,90,6,8,"fin"]
ma=maxiymini(lista)[0]
assert(maxiymini(lista)[0]==90)
mi=maxiymini(lista)[1]
assert(maxiymini(lista)[1]==1)
print(lista)
print("numero maximo: ",ma,"numero minimo: ",mi)

#B)
def crea_lista(N):
    lis=[]
    for i in range(0,N):
        lis+=[int(input("ingrese una lista de numeros: "))]
    return lis
def calcula_maxmin(lis):
    maxi=max(lis)
    mini=min(lis)
    return[maxi,mini]

N=int(input("ingrese cantidad de numeros a ingresar en la lista: "))
lista=crea_lista(N)
print("el arrelo de numeros ingresados es: ",lista)
print("el maximo es: ",calcula_maxmin(lista)[0])
assert(calcula_maxmin(lista)[0]==max(lista))
print("el minimo es: ",calcula_maxmin(lista)[1])
assert(calcula_maxmin(lista)[1]==min(lista))
