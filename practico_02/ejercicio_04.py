# Escribir una clase Estudiante, que herede de Persona, y que agregue las siguientes condiciones:
# Atributos:
# - nombre de la carrera.
# - año de ingreso a la misma.
# - cantidad de materias de la carrera.
# - cantidad de materias aprobadas.
# Métodos:
# - avance(): indica que porcentaje de la carrera tiene aprobada.
# - edad_ingreso(): indica que edad tenia al ingresar a la carrera (basándose en el año actual).

import time
from practico_02.ejercicio_03 import Persona

class Estudiante(Persona):

    def __init__(self, nombre, edad, sexo, peso, altura, carrera, anio, cantidad_materias, cantidad_aprobadas):
        Persona.__init__(self, nombre, edad, sexo, peso, altura)
        self.ca=carrera
        self.an=anio
        self.cm=cantidad_materias
        self.caa=cantidad_aprobadas

    def avance(self):
        a = self.caa * 100 / self.cm
        return a

    # implementar usando modulo datetime
    def edad_ingreso(self):
        a = self.ed -( int(time.strftime("%Y")) -self.an)
        return a

algo = Estudiante ('juan',27,'H',89,1.87,'ISI',2015,50,25)
assert (int((algo.avance()))==50)
#print(algo.edad_ingreso())
