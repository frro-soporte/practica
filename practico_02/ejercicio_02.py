# Implementar la clase Circulo que contiene un radio, y sus métodos area y perimetro.
# area = pi * rr
import math

class Circulo:

    def __init__(self, radio):
        self.radio = radio


    def area(self):
        res = str(math.pi * math.pow(self.radio,2))
        return res[:res.find(".")+3]


    def perimetro(self):
        res = str(math.pi * 2 * self.radio)
        return res[:res.find(".")+3]


def app():
    radio = int(input("Ingrese el radio: "))

    circulo1 = Circulo(radio)

    print("")
    print("El radio es: ", circulo1.radio)
    print("")
    print("El area es: ", circulo1.area())
    print("")
    print("El perimetr es: ", circulo1.perimetro())

    circulo2 = Circulo(3)
    assert circulo2.perimetro() == "18.84"
    assert circulo2.area() == "28.27"

if __name__ == '__main__':

    app()
