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
		Persona.__init__(self,nombre,edad,sexo,peso,altura)
		self.carrera = carrera
		self.anio = anio
		self.cantidad_materias = cantidad_materias
		self.cantidad_aprobadas = cantidad_aprobadas

	def avance(self):
		return (self.cantidad_aprobadas/self.cantidad_materias)*100

    # implementar usando modulo datetime
	def edad_ingreso(self):
		current_year = datetime.datetime.now().year
		return self.anio + self.edad - current_year

e = Estudiante("test_n",21,"F",80,1.80,"Sistemas",2016,20,10)
assert(e.avance() == 50 and e.edad_ingreso() == 18)
