# Implementar la clase Persona con un constructor donde reciba una fecha de nacimiento.
# La clase además debe contener un método edad, que no recibe nada y devuelva la edad de la
# persona (entero).
# Para obtener la fecha actual, usar el método de clase "now" de la clase datetime (ya importada).
from datetime import datetime

class Persona:

    # nacimiento es un objeto datetime.datetime
    def __init__(self, nacimiento):
        self.nacimiento = nacimiento

    def edad(self):
        dt= datetime.now()
        dif = (dt - self.nacimiento)
        return (dif.days//364)

nac = datetime(1995,8,14)
a = Persona(nac)
print(a.edad())
