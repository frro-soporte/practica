# Implementar la función organizar_estudiantes() que tome como parámetro una lista de Estudiantes
# y devuelva un diccionario con las carreras como keys, y la cantidad de estudiantes en cada una de ellas como values.

from practico_02.ejercicio_04 import Estudiante

def organizar_estudiantes(estudiantes):
    dic = {}
    for i in lista:
        if i.ca not in dic:
            dic[i.ca] = 1
        else: dic[i.ca] += 1
    print (dic)

e1 = Estudiante('Juan',27,'H',89,1.87,'ISI',2015,50,25)
e2 = Estudiante('Carlos',27,'H',89,1.87,'ISI',2015,50,25)
e3 = Estudiante('Pedro',27,'H',89,1.87,'IM',2015,50,25)
e4 = Estudiante('Maria',27,'H',89,1.87,'ISI',2015,50,25)
e5 = Estudiante('Eduardo',27,'H',89,1.87,'IE',2015,50,25)
e6 = Estudiante('Julia',27,'H',89,1.87,'IM',2015,50,25)
lista = [e1,e2,e3,e4,e5,e6]

organizar_estudiantes(lista)
