# Escribir una clase Estudiante, que herede de Persona, y que agregue las siguientes condiciones:
# Atributos:
# - nombre de la carrera.
# - año de ingreso a la misma.
# - cantidad de materias de la carrera.
# - cantidad de materias aprobadas.
# Métodos:
# - avance(): indica que porcentaje de la carrera tiene aprobada.
# - edad_ingreso(): indica que edad tenia al ingresar a la carrera (basándose en el año actual).

import datetime
from practico_02.ejercicio_03 import Persona


class Estudiante(Persona):

    def __init__(self, carrera, anio, cantidad_materias, cantidad_aprobadas):
        super().__init__("Fulanito", 19, 'H', 64.3, 1.72)
        self.carr = carrera
        self.anio = anio
        self.cantm = cantidad_materias
        self.aprob = cantidad_aprobadas

    def avance(self):
        porc = round((self.aprob / self.cantm) * 100, 2)
        return porc

    # implementar usando modulo datetime
    def edad_ingreso(self):
        actual = datetime.date.today()
        dif = actual.year - self.anio
        return self.e - dif


e = Estudiante("Ingeniería en Sistemas", 2018, 20, 10)
assert e.avance() == 50.00
assert e.edad_ingreso() == 18
