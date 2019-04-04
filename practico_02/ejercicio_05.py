# Implementar la función organizar_estudiantes() que tome como parámetro una lista de Estudiantes
# y devuelva un diccionario con las carreras como keys, y la cantidad de estudiantes en cada una de ellas como values.

from practico_02.ejercicio_04 import Estudiante


import random
import datetime

class Persona:

    def __init__(self, nombre, edad, sexo, peso, altura):
        self.nom = nombre
        self.age = edad
        self.sex = sexo
        self.peso = peso
        self.alt = altura
        self.dni = self.generar_dni()

    def es_mayor_edad(self):
        if self.age >= 18:
            return True
        else:
            return False


    def generar_dni(self):
        return random.randint(00000000, 99999999)

    def print_data(self):
        print(' Nombre:' ,self.nom, '\n',
              'Edad>>', self.age, '\n',
              'Sexo>>', self.sex, '\n',
              'Peso>>', self.peso, '\n',
              'Altura>>', self.alt, '\n'
              ' DNI>>>', self.dni, '\n')

class Estudiante(Persona):

    def __init__(self, nombre, edad, sexo, peso, altura, carrera, anio, cantidad_materias, cantidad_aprobadas):
        Persona.__init__(self, nombre, edad, sexo, peso, altura)
        self.carrera = carrera
        self.anio = anio
        self.cm = cantidad_materias
        self.ca = cantidad_aprobadas

    def avance(self):
        av = (self.ca * 100)/self.cm
        return int(av)

    # implementar usando modulo datetime
    def edad_ingreso(self):
        n = int(datetime.datetime.today().strftime('%Y'))
        return self.age - (n-self.anio)

def organizar_estudiantes(estudiantes):
    dic = {}
    for e in estudiantes:
         if e.carrera not in dic:
             dic[e.carrera] = 1
         else:
            dic[e.carrera] = dic[e.carrera] + 1


    print(dic)




e1 = Estudiante('Juan', 23, 'Masculino', 66, 1.64, 'isi', 2013, 12, 9)
e2 = Estudiante('Franco', 21, 'Masculino', 66, 1.64, 'isi', 2015, 19, 4)
e3 = Estudiante('Esteban', 18, 'Masculino', 66, 1.64, 'arqi', 2018, 17, 2)
e4 = Estudiante('Esteban', 18, 'Masculino', 66, 1.64, 'im', 2018, 17, 2)
e5 = Estudiante('Esteban', 18, 'Masculino', 66, 1.64, 'im', 2018, 17, 2)

li_e = [e1, e2, e3, e4, e5]
organizar_estudiantes(li_e)
