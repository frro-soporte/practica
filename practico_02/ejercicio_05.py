# Implementar la función organizar_estudiantes() que tome como parámetro una lista de Estudiantes
# y devuelva un diccionario con las carreras como keys, y la cantidad de estudiantes en cada una de ellas como values.

from practico_02.ejercicio_04 import Estudiante


def organizar_estudiantes(estudiante):

    dic={'ISI':0,'IQ':0,'ELE':0,'MEC':0}
    i=0
    for i in estudiante:
        if i.carrera in dic:
         dic[i.carrera]+=1


    return dic

pass

li=[]

est1=Estudiante("Mailen", 25, "fem", 80, 1.80, "ISI", 2019, 41, 30)
li.append(est1)
est2=Estudiante("Ferna", 25, "Masc", 100, 1.65, "ISI", 2019, 41, 30)
li.append(est2)
est3=Estudiante("Tincho", 25, "Masc", 150, 2.65, "IQ", 2019, 41, 30)
li.append(est3)
est4=Estudiante("Eli", 25, "Fem", 65, 1.65, "MEC", 2019, 41, 30)
li.append(est4)



print(organizar_estudiantes(li))

assert organizar_estudiantes(li) == {'ISI': 2, 'IQ': 1, 'ELE': 0, 'MEC': 1}