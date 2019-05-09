# Implementar la clase Persona con un constructor donde reciba una fecha de nacimiento.
# La clase además debe contener un método edad, que no recibe nada y devuelva la edad de la
# persona (entero).
# Para obtener la fecha actual, usar el método de clase "now" de la clase datetime (ya importada).

from _datetime import datetime
from datetime import date
class Persona:

    # nacimiento es un objeto datetime.datetime
    def __init__(self, nacimiento):

        self.nacimiento=nacimiento
        pass

    def edad(self):
        nac=self.nacimiento
        hoy=datetime.now()
        return hoy.year-nac.year- ((hoy.month, hoy.day) < (nac.month, nac.day))
pass


per=Persona(date(1990,5,12))

print(per.edad())

assert per.edad()==28