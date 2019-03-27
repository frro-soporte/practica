#Determinar la suma de todos los números de 1 a N. N es un número que se ingresa
#por consola.

def sumatoria(n):
    res=0
    for i in range (1,n+1):
        res+=i
    return res
numero=int(input("ingrese numero(N) para sumar de 1 hasta "))
print(sumatoria(numero))
assert(sumatoria(4)==10)
