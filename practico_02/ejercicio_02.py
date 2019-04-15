# Implementar la clase Circulo que contiene un radio, y sus métodos area y perimetro.

import math

class Circulo:

	def __init__(self, radio):
 		self.radio = radio

	def area(self):
		#area = πr^2
		return (math.pi * (self.radio ** 2))

	def perimetro(self):
		#perimetro = 2πr
		return (2 * math.pi * self.radio)

assert(round(Circulo(6).area()) == 113 and round(Circulo(6).perimetro()) == 38)
