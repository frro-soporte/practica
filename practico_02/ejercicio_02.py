# Implementar la clase Circulo que contiene un radio, y sus métodos area y perimetro.
import math


class Circulo:
    def __init__(self, radio):
        self.r = radio

    def area(self):
        return math.pi * (self.r**2)

    def perimetro(self):
        return math.pi * 2 * self.r


radio = 1
cir = Circulo(radio)
assert cir.area() == math.pi*(radio**2)
assert cir.perimetro() == math.pi * 2 * radio
