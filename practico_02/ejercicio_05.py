# Implementar la función organizar_estudiantes() que tome como parámetro una lista de Estudiantes
# y devuelva un diccionario con las carreras como keys, y la cantidad de estudiantes en cada una de ellas como values.

from practico_02.ejercicio_04 import Estudiante

est=[]
est.append(Estudiante("Damian",21,"H",75,1.78,'ISI', 2016, 36, 22))
est.append(Estudiante("Agustin",21,"H",75,1.80,'ISI', 2016, 36, 22))
est.append(Estudiante("Roman",21,"H",75,1.50,'IC', 2016, 36, 10))
est.append(Estudiante("Juan",21,"H",75,1.90,'IC', 2016, 36, 15))
est.append(Estudiante("Leo",21,"H",75,1.75,'IC', 2016, 36, 25))

def organizar_estudiantes(est):
    lista = {}

    for i in est:
        if i.carrera in lista:
            lista[i.carrera] += 1
        else:
            lista[i.carrera] = 1
    return lista


print("Alumnos por Carrera: ",organizar_estudiantes(est))
