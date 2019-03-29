# Implementar la función organizar_estudiantes() que tome como parámetro una lista de Estudiantes
# y devuelva un diccionario con las carreras como keys, y la cantidad de estudiantes en cada una de ellas como values.

from practico_02.ejercicio_04 import Estudiante
def organizar_estudiantes(estudiantes):
    dic = {}
    for e in estudiantes:
        if e.carrera in dic:
            dic[e.carrera] = int(dic[e.carrera])+1
        else:
            dic[e.carrera] = 1

    return dic

est = []
e = Estudiante("isi",2015,10,5)
est.append(e)
e = Estudiante("iq",2015,10,5)
est.append(e)
e = Estudiante("isi",2015,10,5)
est.append(e)
e = Estudiante("im",2015,10,5)
est.append(e)
e = Estudiante("isi",2015,10,5)
est.append(e)
e = Estudiante("iq",2015,10,5)
est.append(e)
e = Estudiante("ie",2015,10,5)
est.append(e)
e = Estudiante("ii",2015,10,5)
est.append(e)

assert organizar_estudiantes(est) == {'isi': 3, 'iq': 2, 'im': 1, 'ie': 1, 'ii': 1}
