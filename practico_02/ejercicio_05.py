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
e = Estudiante("Juan",22,"H",75,1.78,"isi",2015,10,5)
est.append(e)
e = Estudiante("Pedro",19,"H",72,1.79,"iq",2015,10,5)
est.append(e)
e = Estudiante("Gonzalo",25,"H",80,1.90,"isi",2015,10,5)
est.append(e)
e = Estudiante("Federica",21,"M",60,1.78,"im",2015,10,5)
est.append(e)
e = Estudiante("Julia",22,"M",77,1.78,"isi",2015,10,5)
est.append(e)
e = Estudiante("Martin",22,"H",75,1.65,"iq",2015,10,5)
est.append(e)
e = Estudiante("Nicolas",23,"H",96,2.00,"ie",2015,10,5)
est.append(e)
e = Estudiante("Manuel",22,"H",75,1.78,"ii",2015,10,5)
est.append(e)

assert organizar_estudiantes(est) == {'isi': 3, 'iq': 2, 'im': 1, 'ie': 1, 'ii': 1}
