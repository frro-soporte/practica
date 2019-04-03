
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
from practico_02.ejercicio_03 import Persona

class Estudiante(Persona):

    def __init__(self, nombre, edad, sexo, peso, altura, carrera, anio, cantidad_materias, cantidad_aprobadas):
        super().__init__(nombre, edad, sexo, peso, altura)
        self.carrera = carrera
        self.anio = anio
        self.cantidad_materias = cantidad_materias
        self.cantidad_aprobadas = cantidad_aprobadas

        pass

    def avance(self):
        return (self.cantidad_aprobadas*100/self.cantidad_materias)
        pass

    # implementar usando modulo datetime
    def edad_ingreso(self):
        fecha = datetime.now().date().year
        aniosEstudiando = fecha-self.anio
        return self.edad-aniosEstudiando
        pass


est = Estudiante("Juan",22,"H",75,1.78,"Ingenieria en Sistemas",2016,50,25)
assert est.avance() == 50
assert est.edad_ingreso() == 19

