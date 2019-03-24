# Implementar la clase Rectangulo que contiene una base y una altura, y el método area.


class Rectangulo:
    def __init__(self, base, altura):
        self.x = base
        self.y = altura

    def area(self):
        return self.x*self.y


r = Rectangulo(20,10)
assert r.area() == 200
