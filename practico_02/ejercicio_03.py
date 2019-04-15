# Implementar la clase Persona que cumpla las siguientes condiciones:
# Atributos:
# - nombre.
# - edad.
# - sexo (H hombre, M mujer).
# - peso.
# - altura.
# Métodos:
# - es_mayor_edad(): indica si es mayor de edad, devuelve un booleano.
# - print_data(): imprime por pantalla toda la información del objeto.
# - generar_dni(): genera un número aleatorio de 8 cifras y lo guarda dentro del atributo dni.
from random import randint

class Persona:

	def __init__(self, nombre, edad, sexo, peso, altura):
		self.nombre = nombre
		self.edad = edad
		self.sexo = sexo
		self.peso = peso
		self.altura = altura
		self.generar_dni()

	def es_mayor_edad(self):
		return (self.edad >= 18)

	# llamarlo desde __init__
	def generar_dni(self):
		self.dni = ''.join([str(randint(0,9)) for i in range(8)])

	def print_data(self):
		print("--------------------")
		print("Nombre: " + self.nombre)
		print("Edad: " + str(self.edad))
		print("Sexo: " + self.sexo)
		print("Altura: " + str(self.altura))
		print("Dni: " + self.dni)
		print("--------------------")

assert(Persona("test_n",19,"F",65,1.80).es_mayor_edad())

