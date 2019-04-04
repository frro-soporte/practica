# Implementar la clase Persona con un constructor donde reciba una fecha de nacimiento.
# La clase además debe contener un método edad, que no recibe nada y devuelva la edad de la
# persona (entero).
# Para obtener la fecha actual, usar el método de clase "now" de la clase datetime (ya importada).

import datetime
class Persona:

    # nacimiento es un objeto datetime.datetime
    def __init__(self, nacimiento):
        self.fnac = nacimiento

    def edad(self):
        hoy = datetime.date.today()
        if hoy.month == self.fnac.month:
            if hoy.day <= self.fnac.day:
                return (hoy.year - self.fnac.year) - 1
            else:
                return hoy.year - self.fnac.year
        else:
            if hoy.month <= self.fnac.month:
                return (hoy.year - self.fnac.year) - 1
            else:
                return hoy.year - self.fnac.year

print(datetime.datetime.today())
c = Persona(datetime.datetime(1995,12,1))
assert (c.edad() == 23)
