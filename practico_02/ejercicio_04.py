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
from practico_02.ejercicio_03 import Persona
from datetime import datetime


class Estudiante(Persona):

    def __init__(self, carrera, anio, cantidad_materias, cantidad_aprobadas,nombre, edad, sexo, peso, altura):
        super().__init__( nombre, edad, sexo, peso, altura)
        self.carrera = carrera
        self.anio = anio
        self.cantidad_materias = cantidad_materias
        self.cantidad_apobadas = cantidad_aprobadas

    def avance(self):
        return ( (self.cantidad_apobadas*100) / self.cantidad_materias)

    # implementar usando modulo datetime
    def edad_ingreso(self):
        anio_actual = (datetime.now().date().year)
        anios_estudiando = anio_actual - self.anio
        return self.edad - anios_estudiando

Estudiante("ISI",2015,40,20,"Juan Cruz",22,"H",70,1.70)

