# Implementar la clase Persona con un constructor donde reciba una fecha de nacimiento.
# La clase además debe contener un método edad, que no recibe nada y devuelva la edad de la
# persona (entero).
# Para obtener la fecha actual, usar el método de clase "now" de la clase datetime (ya importada).

from datetime import datetime
class Persona:

    # nacimiento es un objeto datetime.datetime
    def __init__(self, nacimiento):
        self.nacimiento = datetime.strptime(nacimiento, '%d/%m/%Y')

    def edad(self):
        anio = datetime.now().year
        mes = datetime.now().month
        dia = datetime.now().day
        if mes == self.nacimiento.month:
            if dia < self.nacimiento.day:
                return anio - self.nacimiento.year - 1
            else:
                return anio - self.nacimiento.year
        elif mes < self.nacimiento.month:
            return anio - self.nacimiento.year - 1
        else:
            return anio - self.nacimiento.year


p = Persona('04/01/1999')
assert p.edad() == 21
print(p.edad())
