# Implementar la clase Circulo que contiene un radio, y sus métodos area y perimetro.
from math import pi


class Circulo:

    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return pow(self.radio,2)*pi

    def perimetro(self):
        return 2*pi*self.radio

assert Circulo(4).area() == 50.26548245743669
assert Circulo(4).perimetro() == 25.132741228718345
