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
from datetime import datetime

dt = datetime.now()

class Estudiante(Persona):

    def __init__(self, nombre, edad,sexo,  altura, peso, carrera, anio, cantidad_materias, cantidad_aprobadas):
        Persona.__init__(self, nombre, edad,sexo, altura, peso)
        self.carrera = carrera
        self.anio = anio
        self.cantidad_materias = cantidad_materias
        self.cantidad_aprobadas = cantidad_aprobadas

    def avance(self):
        return ((self.cantidad_aprobadas/self.cantidad_materias)*100)

    # implementar usando modulo datetime
    def edad_ingreso(self):
        a = dt.year - self.anio
        return(self.edad - a)

#est = Estudiante('Jorge', 25, 'M', 90, 1.70,'ISI',2015, 36, 15)
#print(est.avance(), est.edad_ingreso())