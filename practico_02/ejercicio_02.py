# Implementar la clase Circulo que contiene un radio, y sus métodos area y perimetro.

import math
class Circulo:

    def __init__(self,radio):
        self.radio=radio

    def area(self):
        return (math.pi*(self.radio**2))

    def perimetro(self):
        return (2*math.pi*self.radio)

circulo=Circulo(3)
assert circulo.area() == math.pi*(3**2)
assert circulo.perimetro() == 2*math.pi*3

