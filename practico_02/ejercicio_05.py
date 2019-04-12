# Implementar la función organizar_estudiantes() que tome como parámetro una lista de Estudiantes
# y devuelva un diccionario con las carreras como keys, y la cantidad de estudiantes en cada una de ellas como values.

from ejercicio_04 import Estudiante
import datetime
import random

#Genera lista aleatoria (alternativa)
"""
def genera_lista():

    alumnos = []
    carreras = ['Mecanica', 'Civil', 'Quimica', 'Electrica', 'Sistemas']
    nombres = ['Pedro', 'Juan', 'Guadalupe', 'Bruno', 'Joaquin', 'Santiago', 'Andres', 'Julian']
    cant = int(input('Ingrese cantidad de alumnos a organizar: '))
    now = datetime.datetime.now()
    for i in range (0, cant):
        alumnos.append(Estudiante((carreras[random.randint(0,len(carreras)-1)]), now.year, random.randint(0,35), random.randint(0,35), (nombres[random.randint(0,len(nombres)-1)]), random.randint(18,30), ['M','F'][random.randint(0,1)], random.randint(50,100), random.randint(160,180)))
    return alumnos
"""

def genera_lista():
    estudiantes=[]
    estudiantes.append(Estudiante(anio = 2016, cantidad_materias = 60,cantidad_aprobadas = 40, nombre = "Andrés",edad =22,sexo = "M", peso = 79,altura = 185,carrera = "ISI"))
    estudiantes.append(Estudiante(anio = 2016,cantidad_materias = 60,cantidad_aprobadas = 40, nombre = "Ornela",edad = 21,sexo = "F",peso = 60,altura = 170,carrera = "ISI"))
    estudiantes.append(Estudiante(anio = 2016,cantidad_materias= 40,cantidad_aprobadas=30, nombre ="Chuck",edad = 60,sexo = "M",peso = 100,altura = 190,carrera = "IC"))
    estudiantes.append(Estudiante(anio = 2016,cantidad_materias= 40,cantidad_aprobadas=30, nombre ="Obama",edad = 60,sexo = "M",peso = 80,altura = 190,carrera = "IQ"))
    estudiantes.append(Estudiante(anio = 2016, cantidad_materias= 40,cantidad_aprobadas=30, nombre = "Trump",edad = 70,sexo = "M",peso = 100,altura = 190,carrera = "IE"))
    return estudiantes

def organizar_estudiantes(estudiantes):
    diccionario = {}
    for i in estudiantes:
        if (i.carrera in diccionario):
            diccionario[i.carrera] += 1
        else:
            diccionario[i.carrera] = 1
    return diccionario


print(organizar_estudiantes(genera_lista()))

assert (organizar_estudiantes(genera_lista())) == {'ISI': 2, 'IC': 1, 'IQ': 1, 'IE': 1}


