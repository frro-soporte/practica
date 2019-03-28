#APARTADO A
#Reescriba el programa que pide al usuario una lista de números e imprime en pantalla el máximo y mínimo de los números introducidos al final,
# cuando el usuario introduce “fin

def MaxiMin(L: list):
    maxi= 0
    mini = 0
    ## Funcion que retorna los maximos y minimos numeros
    if len(L) == 0:
        print ('NO INGRESASTE NADA')
    maxi = max(L)
    mini = min(L)
    print('  Numero Maximo  ' + maxi + ' , Numero Minimo ' + mini  + '\n')

iLista = []

#Cargo la lista

iNum = input ("Ingrese numero a cargar en la lista , escribiendo fin finaliza la carga\n")
while iNum != 'fin':
    iLista.append(iNum)
    iNum = input ("Ingrese numero a cargar en la lista , escribiendo fin finaliza la carga\n")
# Llamo función
MaxiMin(iLista)


# ----------------------------------------------
# ----------------------------------------------
# ----------------------------------------------
# ----------------------------------------------


input('Ahora pasaremos al segundo apartado presione una tecla para continuar \n ')

#APARTADO B
#INICIALIZACION
list2 = []
maxx = 0
miin = 0

ingreso = input('ingrese numeros a guardar , escriba fin para finalizar \n')

#Carga
while ingreso != 'fin':
    list2.append(ingreso)
    ingreso = input('ingrese numeros a guardar , escriba fin para finalizar\n')

if len(list2) == 0:
    print("NO INGRESASTE NADA")
else:
    maxx = max(list2)
    miin = min(list2)

print('  Numero Maximo  ' + maxx + ' , Numero Minimo ' + miin  + '\n')
