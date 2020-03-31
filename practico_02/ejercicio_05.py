# Implementar la función organizar_estudiantes() que tome como parámetro una lista de Estudiantes
# y devuelva un diccionario con las carreras como keys, y la cantidad de estudiantes en cada una de ellas como values.

from ejercicio_04 import Estudiante

estudiantes = [Estudiante('Jorge', 25, 'M', 90, 1.70,'ISI',2015, 36, 15), Estudiante('Patri',19,'M',76,1.78,'IQ',2019, 42,6),
               Estudiante('Azul', 22, 'F', 63, 1.65, 'IQ',2016,42,24), Estudiante('Leonel', 23, 'M', 73, 1.80, 'IM', 2014, 38, 12)]

def organizar_estudiantes(estudiantes):
    dicc = {}
    i = 0
    for i in estudiantes:
        if i.carrera in dicc.keys():
            dicc[i.carrera] += 1
        else:
            dicc[i.carrera] = 1
    return (dicc)

print(organizar_estudiantes(estudiantes))
