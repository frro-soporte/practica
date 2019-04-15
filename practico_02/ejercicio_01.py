# Implementar la clase Rectangulo que contiene una base y una altura, y el método area.


class Rectangulo:

	def __init__(self, base, altura):
		self.base = base
		self.altura = altura

	def area(self):
		return self.altura * self.base

assert(Rectangulo(6,13).area() == 78)
