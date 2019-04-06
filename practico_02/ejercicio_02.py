# Implementar la clase Circulo que contiene un radio, y sus métodos area y perimetro.
import math

class Circulo:

    def __init__(self, radio):

       self.radio=radio

    pass

    def area(self):
      return (math.pi *pow(self.radio,2))
    pass

    def perimetro(self):
       return (2*math.pi*self.radio)

    pass


cir=Circulo(5)
print("El área del circulo es: ",cir.area())

print("El perimetro del circulo es : ",cir.perimetro())

assert cir.area()==78.53981633974483
assert cir.perimetro()==31.41592653589793