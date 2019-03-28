# Implementar la clase Circulo que contiene un radio, y sus métodos area y perimetro.
# area = pi * rr
import math

class Circulo:

    def __init__(self, radio):
        self.radio = radio


    def area(self):
        return math.pi * math.pow(self.radio,2)

    def perimetro(self):
        return  math.pi * 2 * self.radio

radio = int(input("Ingrese el radio: "))

circulo1 = Circulo(radio)

print("")
print("El radio es: ", circulo1.radio)
print("")
print("El area es: ", circulo1.area())
print("")
print("El perimetr es: ", circulo1.perimetro())

