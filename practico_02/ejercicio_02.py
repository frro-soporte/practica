# Implementar la clase Circulo que contiene un radio, y sus métodos area y perimetro.
import math


class Circulo:

    def __init__(self, radio):
        self.radio=radio

    def area(self):
         return math.pi * (self.radio**2)


    def perimetro(self):
       return math.pi * self.radio * 2


assert a.area() == 50.26548245743669
assert a.perimetro() == 25.132741228718345
