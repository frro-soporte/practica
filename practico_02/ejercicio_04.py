# Escribir una clase Estudiante, que herede de Persona, y que agregue las siguientes condiciones:
# Atributos:
# - nombre de la carrera.
# - año de ingreso a la misma.
# - cantidad de materias de la carrera.
# - cantidad de materias aprobadas.
# Métodos:
# - avance(): indica que porcentaje de la carrera tiene aprobada.
# - edad_ingreso(): indica que edad tenia al ingresar a la carrera (basándose en el año actual).

import random
from datetime import datetime

class Persona:
    def __init__(self, nombre, edad, sexo, peso, altura):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.peso = peso
        self.altura = altura
        self.generar_dni();
    def es_mayor_edad(self):
        if self.edad>=18:
            return True
        else:
            return False
    def generar_dni(self):
        aleatorios = [random.randint(0,9) for _ in range(8)]
        self.dni = int(''.join(str(i) for i in aleatorios))

    def print_data(self):
        print(self.nombre,self.edad,self.sexo,self.peso,self.altura,self.dni)

class Estudiante(Persona):

    def __init__(self, carrera, anio, cantidad_materias, cantidad_aprobadas):
        self.carrera = carrera
        self.anio = anio
        self.cantidad_materias = cantidad_materias
        self.cantidad_aprobadas = cantidad_aprobadas
        Persona.__init__(self,"pedro",25,"M",75,1.75)
    def avance(self):
        return (self.cantidad_aprobadas*100)/self.cantidad_materias

    # implementar usando modulo datetime
    def edad_ingreso(self):
        fecha = datetime.now().date().year
        aniosEstudiando = fecha-self.anio
        return self.edad-aniosEstudiando

est = Estudiante("isi",2015,10,5)
assert est.edad_ingreso() == 21
assert est.avance()==50
