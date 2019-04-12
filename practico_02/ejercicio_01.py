# Implementar la clase Rectangulo que contiene una base y una altura, y el método area.


class Rectangulo:


    def __init__(self, base, altura):
        self.rec_base = base
        self.rec_altura = altura

    def area(self):
        area = self.rec_altura*self.rec_base
        print('Area del rectangulo: ' + str(area) + ' mts')
        return area

base= 8
altura= 10
rectangulo = Rectangulo(base,altura)

assert(rectangulo.area())==80