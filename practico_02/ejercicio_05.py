# Implementar la función organizar_estudiantes() que tome como parámetro una lista de Estudiantes
# y devuelva un diccionario con las carreras como keys, y la cantidad de estudiantes en cada una de ellas como values.

from ejercicio_04 import Estudiante


def organizar_estudiantes(estudiantes):
	carreras = {}
	for e in estudiantes:
		if e.carrera in carreras:
			carreras[e.carrera] += 1
		else:
			carreras[e.carrera] = 1
	
	return carreras


es = []
es.append(Estudiante("test_0",21,"F",80,1.80,"Sistemas",2016,20,10))
es.append(Estudiante("test_1",28,"M",70,1.70,"Quimica",2016,20,10))
es.append(Estudiante("test_2",21,"F",40,1.60,"Sistemas",2016,20,10))
es.append(Estudiante("test_3",24,"M",55,1.70,"Mecanica",2016,20,10))
es.append(Estudiante("test_4",18,"F",68,1.90,"Sistemas",2016,20,10))
es.append(Estudiante("test_5",22,"M",89,1.73,"Quimica",2016,20,10))

dic = organizar_estudiantes(es)
assert(dic["Sistemas"] == 3 and dic["Quimica"] == 2 and dic["Mecanica"] == 1)
