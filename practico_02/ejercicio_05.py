# Implementar la función organizar_estudiantes() que tome como parámetro una lista de Estudiantes
# y devuelva un diccionario con las carreras como keys, y la cantidad de estudiantes en cada una de ellas como values.

from practico_02.ejercicio_04 import Estudiante


import random
import datetime

from practico_02.ejercicio_03 import Persona

from ejercicio_04 import Estudiante

def organizar_estudiantes(estudiantes):
    dic = {}
    for e in estudiantes:
         if e.carrera not in dic:
             dic[e.carrera] = 1
         else:
            dic[e.carrera] = dic[e.carrera] + 1


    return dic




e1 = Estudiante('Juan', 23, 'Masculino', 66, 1.64, 'isi', 2013, 12, 9)
e2 = Estudiante('Franco', 21, 'Masculino', 66, 1.64, 'isi', 2015, 19, 4)
e3 = Estudiante('Esteban', 18, 'Masculino', 66, 1.64, 'arqi', 2018, 17, 2)
e4 = Estudiante('Esteban', 18, 'Masculino', 66, 1.64, 'im', 2018, 17, 2)
e5 = Estudiante('Esteban', 18, 'Masculino', 66, 1.64, 'im', 2018, 17, 2)

li_e = [e1, e2, e3, e4, e5]

assert organizar_estudiantes(li_e) == {'isi': 2, 'arqi': 1, 'im': 2}
