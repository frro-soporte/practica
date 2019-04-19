# Implementar la clase Circulo que contiene un radio, y sus métodos area y perimetro.

class Circulo:

    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.14*(self.radio * self.radio)

    def perimetro(self):
        return 2*3.14*self.radio

radio = input('Ingresar radio')
try:
    r = int(radio)
    c = Circulo(r)
    ac = c.area()
    pc = c.perimetro()
    resultado = "(El radio es de : {}, el area de : {}, y el perimetro de: {})".format(r, ac, pc)
    print(resultado)
except ValueError:
    print('Ingreso valor erroneo')
