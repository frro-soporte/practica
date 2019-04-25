# Implementar la clase Circulo que contiene un radio, y sus métodos area y perimetro.

from math import pi

class Circulo:

    def __init__(self, radio):
        self.radio = radio

    def area(self):
        a= pi*self.radio**2
        return a

    def perimetro(self):
        a= 2*pi*self.radio
        return a

algo = Circulo (5)

assert (int(algo.area())==78)
assert (int(algo.perimetro())==31)
