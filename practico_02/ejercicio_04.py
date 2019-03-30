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

    def __init__(self,nombre,edad,sexo,peso,altura,carrera,anioIngreso,cantidadMaterias,cantidadMateriasAprobadas):
        Persona.__init__(self,nombre,edad,sexo,peso,altura)
        self.carrera=carrera
        self.anioIngreso=anioIngreso
        self.cantidadMaterias=cantidadMaterias
        self.cantidadMateriasAprobadas=cantidadMateriasAprobadas

    def avance(self):
        porcentaje=('{0:.2f}'.format((self.cantidadMateriasAprobadas/self.cantidadMaterias)*100))
        return porcentaje

    def edad_ingreso(self):
        edadIng=(self.edad-(int(time.strftime('%Y'))-self.anioIngreso))
        return edadIng

estudiante=Estudiante('Agustin Yurescia',22,'H',69.60,1.75,'ISI',2015,41,27)
assert estudiante.edad_ingreso() == 18
assert estudiante.avance() == '65.85'


