# Implementar la función numeros_al_final(), que mueve todos los elementos numéricos
# de lista al final de esta. Devuelve la lista.


# Resolver sin utilizar lista auxiliar
def numeros_al_final(lista):
    print('lista inicial: ', lista)

    print(len(lista))
    i=0
    #while(i<8):
    '''  for value in lista:

        print('Valor: ', value)
        if(value.isdigit()==True):
            print(' es numerico \n')
            #if isinstance(i,(int)):
            lista.append(value)
            del lista[lista.index(value)]
            print('lista actualizada: ',lista)
    print(lista)'''
    for valor in range(len(lista)):
        print('\nvalor: ',valor)
        print('value en index:',lista[valor])
        if(lista[valor].isdigit()==True):
            lista.append(lista[valor])
            del lista[valor]
            valor-=1
    print(lista)


lista = ['a','1','hola','2','3','b','4','5']
numeros_al_final(lista)
