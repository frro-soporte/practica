# Implementar la clase Circulo que contiene un radio, y sus métodos area y perimetro.
import math


class Circulo:

    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return self.radio * self.radio * math.pi

    def perimetro(self):
        return self.radio * 2 * math.pi


assert Circulo(1).area() == math.pi
assert Circulo(0.5).perimetro() == math.pi
