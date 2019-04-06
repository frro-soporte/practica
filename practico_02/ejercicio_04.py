# Escribir una clase Estudiante, que herede de Persona, y que agregue las siguientes condiciones:
# Atributos:
# - nombre de la carrera.
# - año de ingreso a la misma.
# - cantidad de materias de la carrera.
# - cantidad de materias aprobadas.
# Métodos:
# - avance(): indica que porcentaje de la carrera tiene aprobada.
# - edad_ingreso(): indica que edad tenia al ingresar a la carrera (basándose en el año actual).

import random as ran
from datetime import datetime
from ejercicio_03 import Persona

class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, peso, altura, carrera, anio, cantidad_materias, cantidad_aprobadas):
        Persona.__init__(self, nombre, edad, sexo, peso, altura)
        self.carrera = carrera
        self.anio = anio
        self.cant_materias = cantidad_materias
        self.cant_aprobadas = cantidad_aprobadas

    def avance(self):
        return str((self.cant_aprobadas/self.cant_materias)*100) + "%"

    def edad_ingreso(self):
        anio_actual = datetime.now()
        anio_actual = anio_actual.year
        return self.edad - (anio_actual - self.anio)

est = Estudiante("Andrés",22,"M",79,185,"ISI",2016, cantidad_materias = 60,cantidad_aprobadas = 40)

assert est.avance() == str((40/60)*100) + "%"
assert est.edad_ingreso() == 22 - (2019- 2016)


