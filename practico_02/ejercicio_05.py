# Implementar la función organizar_estudiantes() que tome como parámetro una lista de Estudiantes
# y devuelva un diccionario con las carreras como keys, y la cantidad de estudiantes en cada una de ellas como values.

from ejercicio_04 import Estudiante
estudiantes=[]
estudiantes.append(Estudiante("Andrés",22,"M",79,185,"ISI",2016, cantidad_materias = 60,cantidad_aprobadas = 40))
estudiantes.append(Estudiante("Ornela",21,"F",60,170,"ISI",2016, cantidad_materias = 60,cantidad_aprobadas = 40))
estudiantes.append(Estudiante("Chuck",60,"M",100,190,"IC",2000,cantidad_materias= 40,cantidad_aprobadas=30))
estudiantes.append(Estudiante("Obama",60,"M",80,190,"IQ",1996,cantidad_materias= 40,cantidad_aprobadas=30))
estudiantes.append(Estudiante("Trump",70,"M",100,190,"IE",1980,cantidad_materias= 40,cantidad_aprobadas=30))

def organizar_estudiantes(estudiantes):
    datos = {}
    carreras = []
    for i in range(len(estudiantes)):
        if estudiantes[i].carrera not in carreras:
            carreras.append(estudiantes[i].carrera)
            datos[estudiantes[i].carrera] = 1
        else:
            datos[estudiantes[i].carrera] = datos[estudiantes[i].carrera] + 1
    return datos


assert organizar_estudiantes(estudiantes) == {'ISI': 2, 'IC': 1, 'IQ': 1, 'IE': 1}
