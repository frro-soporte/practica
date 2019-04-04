# Implementar la clase Rectangulo que contiene una base y una altura, y el método area.


class Rectangulo:

    def __init__(self, base, altura):
        self.b = base
        self.alt = altura

    def area(self):
        ar = self.b * self.alt
        return ar

a = Rectangulo(3,5)
print(a.area())

