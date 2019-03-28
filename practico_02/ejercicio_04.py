# Escribir una clase Estudiante, que herede de Persona, y que agregue las siguientes condiciones:
# Atributos:
# - nombre de la carrera.
# - año de ingreso a la misma.
# - cantidad de materias de la carrera.
# - cantidad de materias aprobadas.
# Métodos:
# - avance(): indica que porcentaje de la carrera tiene aprobada.
# - edad_ingreso(): indica que edad tenia al ingresar a la carrera (basándose en el año actual).

from ejercicio_03 import Persona
import datetime


class Estudiante(Persona):

    def __init__(self, nombre, edad, sexo, peso, altura, carrera, anio, cantidad_materias, cantidad_aprobadas):
        super().__init__
        self.carrera = carrera
        self.anio = anio
        self.cantidad_materias = cantidad_aprobadas
        self.cantidad_aprobadas = cantidad_aprobadas

    def avance(self):
        porcentaje = (self.cantidad_aprobadas/self.cantidad_materias)*100
        print(porcentaje)
        return porcentaje

    # implementar usando modulo datetime
    def edad_ingreso(self):
        anio = datetime.datetime.now().year - self.anio
        edaddd = self.edad - anio
        print(edaddd)
        return edaddd

a=Estudiante('Pato', 23, 'M', 84, 1.85, 'Ingenieria en Sistemas', 2014, 41, 31)
a.avance()
a.edad_ingreso()
