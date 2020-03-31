# Implementar la función organizar_estudiantes() que tome como parámetro una lista de Estudiantes
# y devuelva un diccionario con las carreras como keys, y la cantidad de estudiantes en cada una de ellas como values.

from practico_02.ejercicio_04 import Estudiante


def organizar_estudiantes(estudiantes):
    diccionario = {}
    for obj in estudiantes:
        if obj.carrera in diccionario.keys():
            diccionario[obj.carrera] = int(diccionario[obj.carrera])+1
        else:
            diccionario[obj.carrera] = 1

estudiantes = []
estudiantes.append(Estudiante("ISI",2015,40,39,"Juan Cruz",22,"H",70,1.70))
estudiantes.append(Estudiante("ISI",2014,40,18,"Joaquin",23,"H",67,1.68))
estudiantes.append(Estudiante("CIVIL",2015,40,15,"Roberto",12,"H",62,1.62))
estudiantes.append(Estudiante("MECANICA",2013,40,10,"Pedro",21,"H",88,1.55))
assert organizar_estudiantes(estudiantes) == {'ISI':2,'CIVIL': 1, 'MECANICA': 1}
